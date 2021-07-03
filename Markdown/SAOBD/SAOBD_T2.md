# Tema 2: Seguridad en aplicaciones online

## 1. Seguridad en el diseño de las aplicaciones web

### Autenticación

- **Autenticación** 🠒 Gestión de sesiones 🠒 Autorización
- Su función es identificar al usuario de la aplicación
- *Métodos*:
    - Basic (HTTP)
    - Digest (HTTP)
    - Active Directory
    - SSO (Single Sign On)
    - TLS (Certificados digitales cliente)
    - Autenticación de múltiples factores
    - Autenticación desde la aplicación web (basada en formularios)

#### Basic (HTTP)

- Credenciales enviadas **“en claro” (base64)**
- **Cada petición** HTTP incluye las credenciales
- **Historial** y caché (ya que se envían por **GET**)
- Protegerlas con HTTPS (TLS)
    - Transmisión **insegura**
    - Exposición **repetitiva**
    - Almacenamiento inseguro (cache del navegador)
- **Muy insegura**
- *Posibles ataques*:
    - Reply attacks
    - Sniffing
    - Transmision en claro
    - Fuerza bruta
    - MITM

#### Digest (HTTP)

- **Challenge/Response** (nonce)
    - Challenge (+user/pass) Hash (MD5) 🠒 Response
    - Servidor comprueba el response
- **Protección frente a replay** (nonce por petición)
    - Nonce sensible al tiempo (10 segundos)
- **Cada petición** HTTP incluye las credenciales
    - Confidencialidad con HTTPS (TLS)
    - Autenticación mutua con HTTPS (TLS)
- Para que sea realmente seguro **hay que usar cnonce**
- *Posibles ataques*:
    - Fuerza bruta (por eso necesita cnonce)
    - MITM

#### Active Directory

- Son transparentes a la aplicación
- No son comunes en internet
    - Usados en controladores de dominio (intranet)
- No se necesitan almacenar credenciales en la aplicación

##### NTLM

- Dos peticiones challenge/response
    - Hash HMAC-MD5
- *Posibles ataques*:
    - Caché de hashes/credenciales de usuarios que han iniciado sesión en una máquina comprometida
    - Volcado de memoria del proceso lsass.exe
    - Volcado de SAM
    - MITM (Captura de challenges/responses)

##### Kerberos

- Está basado en tokens (tickets)
- *Proceso* de autenticación:
    1. Obtención de credenciales del KDC:
        - Autenticación del usuario → TGT (Ticket Granting Ticket)
    2. Petición de autenticación al KDC para un servicio:
        - <TGT, Servicio> → TGS (Ticket Granting Service)
    3. Presentación del ticket al servidor final:
        - TGS → Servicio
- *Posibles ataques*:
    - Overpass The Hash/Pass The Key (PTK)
    - Pass-the-ticket
    - En caso de que el atacante tenga acceso de administrador en una máquina:
        - Golden/Silver Ticket
    - Kerberoasting
        - Intentar obtener la contraseña de un servicio a partir de su TGS

#### SSO (Single Sign On)

- Valido tanto para internet como para intranet
- Inicio único de sesión 🠒 token
- Muchos métodos para hacerlo
    - **SAML**, **Kerberos**, **OAuth2+OPENID**, ...
- **Usar siempre TLS** (servidor y cliente)
- La **generación** de tokens debe ser **segura**
- Válidez de los tokens corta

#### TLS

- Certificados digitales **en cliente y servidor**
- Autentificación en ambos sentidos (HTTPS)
- Una de las opciones más seguras si se implementa
- **Requiere una PKI** (ej. DNIe)
- Soporte HTTPs
- *Vulnerabilidaes*:
    - Protección en la autenticación y no durante el resto de la sesión
    - Re-negociación SSL/TLS iniciada por cliente
    - MITM (Gen. de certificados)

#### Autenticación de múltiples factores

- La autenticación de múltiples factores factores se basan en:
    - Algo que **sé**: contraseña o PIN
    - Algo que **tengo**: token, Smart card, Yubikey
    - Algo que **soy**: biometría

#### Autenticación desde la aplicación web (basada en formularios)

- Utiliza formularios HTML 🠒 POST
- **Flexibilidad en la BD** de usuarios y credenciales
- Utiliza ID de sesión vía cookie (caducidad)
    - Requiere gestión de sesiones
    - Solicitar autenticacion ante cambios de derechos de acceso
- **HTTPS**

### Seguridad en la autenticación

- *Considerar*:
    - ¿Qué proteger? Buen diseño
    - Contraseñas fuertes
    - Hash + SALT (info extra para el hash de contraseña)
    - No almacenar secretos en el cliente
        - No recordar contraseñas
    - CAPTCHAs
    - Tiempo máximo de expiración
    - Deshabilitar cuentas
- *Recomendaciones*:
    - Tokens / nonces de un solo uso
    - CRNG para generar los tokens
    - Comprobar ruta de certificación en TLS
    - **Combinar distintos métodos** de autenticación.
    - **TLS requerido** para combinar con todos los demás métodos
        - Digest y NTLMv2 sólo si se combinan con TLS
    - **No utilizar HTTP  basic**
    - AD mejor con Kerberos que NTLM
    - Autenticación basada en formularios
        - Usar **APIs/frameworks existentes**

### Gestión de sesiones

- Autenticación 🠒 **Gestión de sesiones** 🠒 Autorización
- **HTTP sin estado**:
    - Hay que mantener información (o estado) por usuario
- Sesiones:
    - Variables que se pueden utilizar en cada una de las interacciones del usuario con la aplicación Web hasta que finalice su sesión
- **ID de sesión** (token):
- *Formas*:
    - **Cookie** (cabecera HTTP estándar): `Cookie: id=012345; ...`
        - El más común
        - Otra cabecera HTTP estándar `Set-Cookie: id=012345`
            - **Usar**:
                - **`secure`** (solo HTTPS)
                - **`HttpOnly`** (no desde scripts)
        - Enviada en cada petición
    - Parámetro URL (URL rewriting): `https://portal.example.com/ private;id=01234...`
    - Argumento URL (petición GET): `https://portal.example.com/ private?id=01234...`
    - Argumento cuerpo (petición POST): `id=012345&...`
    - Campo oculto de formulario (HTML): `<input type="hidden" name="id" value="012345">`
- *Debe ser*:
    - **No predecible** (~ aleatorio)
    - **Largo**, para evitar ataques de fuerza bruta
    - **Sin significado**, para que no se puedan extraer datos de él
    - **Expiración**, **limitaciones de uso**, ...
- *Ataques*:
    - **Revelación** (pasivo)
    - **Captura de la sesión** (activo)
        - MITM, vulnerabilidades del navegador
        - **Robo** de sesión
            - XSS para inyectar código para enviar `document.cookie` a una URL suya
            - Sidejacking
        - **Fijación de sesión**
    - Predicción y **fuerza bruta** de la sesión
- *Defensas*:
    - **Timeouts** y **limpiar** cookies en cliente
    - Renovación de ID al autenticar o cambiar privilegios
    - Propiedades de las cookies
        - **`secure`** (solo HTTPS)
        - **`HttpOnly`** (no desde scripts)
        - **`SameSite: strict`**
    - **Nunca revelar** ID de sesión (secure)
    - Monitorizar

### Autorización

- Autenticación 🠒 Gestión de sesiones 🠒 **Autorización**
- Consiste en asegurarse que los usuarios solo pueden realizar acciones dentro
de su nivel de privilegios
- *Tipos* de usuarios (normales, que acceden a servicios, al SGBD, al SO, admins, ...)
- *Proceso*:
    1. Usuario hace petición (envía ID sesión)
    2. Se comprueban los permisos del recurso que quiere acceder
    3. Se comprueba si el usuario tiene los permisos
        - Sí 🠒 Acceso permitido
        - No 🠒 Acceso NO permitido
- *Forma*:
    - **MAC** (*Mandatory Access Control*) 🠒 adm. Sistema
        - Mínimo número de administradores con máximo control
    - **DAC** (*Discretionary Access Control*) 🠒 propietarios objetos
        - Admin por grupos (aplicaciones)
    - **RBAC** (*Role Based Access Control*)
    - Sistemas híbridos
        - RBAC + DAC (Facebook)
        - MAC + DAC (Linux)
- *Implementación*
    - Si es "casera" 🠒 SP antes que queries
    - **Confiar en frameworks y herramientas** como OAuth
- *Ataques*:
    - Secuestro de sesiones (credenciales)
    - Session fixation
    - Alteración de parámetros
    - XSS
    - CSRF
    - TOCTOU
- *Defensas*:
    - **Matriz de control de accesos** 🠒 **Roles x Permisos**
    - Principio de **mínimo privilegio**
    - **Separación de tareas**
    - Proteger el sistema de ficheros
        - Importante para mitigar ataques LFI/RFI
    - No implementaciones propias

### Cabeceras de seguridad HTTP

- **`Strict-Transport-Security` (HSTS)**: especifica que solo se pueden usar conexiones HTTPS
- **`Public-Key-Pins` (HPKP)**: mecanismo de seguridad para HTTPS para resistir la suplantación con certificados fraudulentos
- **`X-Frame-Options`**: mejora la protección contra el clickjacking
- **`X-XSS-Protection`**: protección básica contra ataques XSS
- **`X-Content-Type-Options`**: evita que el navegador interpreta otro tipo de contenido que el declarado en el header
- **`X-Content-Security-Policy`**: Establece una política de CSP que ayuda a mitigar diferentes tipos de ataques como inyecciones o XSS

### Seguridad en aplicaciones RIA

- Aplicaciones web con AJAX permiten mayor funcionalidad, pero hay que considerara algunos *aspectos de seguridad*:
- **Aumento de la superficie** de ataque
    - Más parte ejecutándose en cliente 🠒 mayor superficie de ataque
    - Potenciación del XSS, CSRF y SQLi
    - Acceso al DOM
- **Exposición de la lógica** de la aplicación en el cliente
- **Exposición de funciones** internas **del servidor**
    - AJAX usa todo el rato funciones de la API del servidor 🠒 más información sobre el servidor para el atacante
- **Violación de la política del mismo origen**
    - Para poder ofrecer diferentes servicios, todo tiene que pasar antes por el servidor
        - El cliente no puede conectar con diferentes sitios (fallo de seguridad)
    - Sobrecarga el servidor y ademas hay diferentes scripts de diferentes sitios en un mismo lugar
- Repudio de peticiones
- Mayor **dificultad en la auditoría** de aplicaciones
    - Hay que revisar el código del cliente a fondo

## 2. Evaluación de la seguridad de las aplicaciones web

- Para garantizar la seguridad de las aplicaciones web es necesario revisar su seguridad
    - Revisiones de código manuales
    - Revisiones con diversos tipos de herramientas semiautomáticas
- Utilizar metodologías para estas revisiones facilita el proceso
    - **OWASP Testing Guide**
        - Metodología abierta para probar la seguridad de aplicaciones web con **11 categorías**:
            1. **OTG-INFO**: Recolección de información
            2. **OTG-CONFIG**: Gestión de la configuración
            3. **OTG-IDENT**: Pruebas sobre la administración de identidades
            4. **OTG-AUTHN**: Pruebas de autenticación
            5. **OTG-AUTHZ**: Autorización
            6. **OTG-SESS**: Gestión de sesiones
            7. **OTG-INPVAL**: Validación de datos
            8. **OTG-ERR**: Manejo de errores
            9. **OTG-CRYPST**: Pruebas sobre debilidades en la criptografía
            10. **OTG-BUSLOGIC**: Lógica del negocio
            11. **OTG-CLIENT**: Lado del cliente

### Herramientas de análisis de la seguridad de aplicaciones web

- **Tipos** de herramientas semiautomáticas:
    - Análisis estático:
        - **SAST** (*Static Analysis Security Rools*)
    - Análisis dinámico:
        - Black box:
            - **DAST** (*Dynamic Analysis Security Tools*)
        - White box:
            - **RAST/IAST** (*Real/Interactive Analysis Security Tools*)
            - **RASP** (*Real Analysis Self Protection*): RAST + capacidad para bloquear
    - **Herramientas híbridas**
- **Según la fase** se utilizan unas u otras:
    - Implementación: SAST
    - Pruebas: DAST, RAST/IAST, híbridas
    - Despliegue-Producción: RASP

### SAST

- Permiten analizar el código fuente y encontrar de manera rápida muchas vulnerabilidades
- Siempre va a haber un proceso de:
    - **Interpretar** resultados
    - Descartar **falsos positivos**
        - Estas herramientas tienden a mostrar mas errores de los que hay "por si acaso"
    - Búsqueda manual de **falsos negativos**
- *Ejemplos*: Fortify SCA,, Synopsys
- Son **muy útiles desde fases tempranas** del desarrollo
- Algunas incluso tienen herramientas de reversing
    - Con ello se puede auditar también librerías comerciales de terceros (aunque estén pensadas mas para malware)
    - El análisis sera de peor calidad

### DAST

- Permiten buscar vulnerabilidades con la aplicación en ejecución
- Permiten **automatizar pruebas** de penetración y cubrir gran superficie de ataque
    - Son **muy efectivas** buscando posibles **vulnerabilidades conocidas** como:
        - XSS, SQLi, Path traversal, Command Injection, defectos de configuración, HTTP response splitting, ...
- También dan falsos positivos (y falsos negativos)
- *Ejemplos*: Webinspect, OWASP ZAP, ...

- *Fases*:
    - **Reconocimiento** de las capas de la aplicación
        - Averiguar: tecnologías usadas, OS, servidor de aplicaciones, SGBD, puertos, lenguajes, ...
    - **Crawling**
        - Descubrimiento de paginas, directorios, formularios y y todo el contenido.
    - **Scan pasivo**
        - Análisis de headers GET/POST a la aplicación web para buscar debilidades o fallos de configuración
        - Se suele realizar junto al crawling
    - **Scan activo**
        - Inyecta payloads en los campos para probar vulnerabilidades
        - Mete mucho ruido
    - **Auditoria**
        - Proceso manual para documentar todo

### RAST/IAST y RASP

- Se ejecutan **en el entorno real** y sobre el codigo ejecutable
- **Controlan desde dentro** su estado (variables, memoria, peticiones)
- Permiten **detectar** amenazas **en tiempo real**
- Tienen un gran inconveniente: **disminuir el rendimiento**
- Segun sus acciones, se dividen en:
    - RAST/IAST 🠒 Generar un informe
    - RASP 🠒 Bloquear

## 3. Seguridad *online*

- Una vez desplegada la aplicación hay una serie de tareas de operación y mantenimiento
- Es importante tener en cuenta la seguridad en ese punto
    - Mecanismos de protección para aplicaciones (web) desplegadas 🠒 **Web Application Firewall (WAF)**

### WAF (Web Application Firewalls)

- Analiza el tráfico de aplicaciones web (HTTP/HTTPS) en base a reglas
    - Whitelist o blacklist
    - Conexiones **SSL/TLS instalando el certificado** del servidor
    - Corta el tráfico detectado como ataque (incluso sanear)
- *Tipos*:
    - Dispositivo: SW + HW específico
    - Hardware : Funciones embebidas en el HW
    - Software
    - Plugin de software (Modsecurity Apache Tocmcat)
    - Cloud
- *Despliegue*:
    - **Fuera** de linea (pasivo)
        - Recibe una copia de trafico y la analiza (pruebas, ...)
        - No evita ataques
    - En línea
        - **Proxy inverso**
            - Bloquean de forma activa el tráfico (~ IDS)
        - **Proxy transparente**
            - Puente de nivel 2 entre el FW de red y el servidor de aplicaciones
    - **Embebido en host**
- *Considerar*:
    - Soluciones de mercado
    - Impacto en el rendimiento y modos de alta disponibilidad
    - Integración en el SIEM
    - Configuraciones robustas
    - *Ejemplo*: ModSecurity 🠒 Filtrado (HTTP(S)), monitorización, bloqueo shellcodes, bloqueo IP
