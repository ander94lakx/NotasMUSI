# Tema 1: Búsqueda de vulnerabilidades

## 1. Introducción

### Conceptos

- Hacker
    - **White-Hat**
        - Amplios conocimientos
        - Código ético
    - **Gray-Hat**
        - Combinación de White-Hay y Black-Hat
    - **Black-Hat**
        - No cumplen la ley
        - Usuarios malignos
- Metodología
    - Permite realizar los procesos de pentesting y de auditoria en base a las mejores técnicas
    - Ejemplo
        - **OSSTMM**: Open Source Security Methodology Manual
        - **SANS**: Conducting a Penetration Test on an Organization
        - **NIST**: Guideline on Network Security Testing
        - **ISACA**: Testing IT Systems Security With Tiger Team
        - **OWASP**: Open Web Application Security Project
        - **OWISAM**: Open Wireless Security Assessment Methodology
        - **OASAM**: Open Android Security Assessment Methodology
- Modalidades de auditoría
    - **Black Box**
        - No se tiene conocimiento del interior del sistema
        - Test de penetración como lo haría un atacante real
        - Es el más realista
    - **White box**
        - Se tiene conocimiento completo del sistema
        - Se hace como si se fuera un empleado interno
        - No es realista
    - **Gray Box**
        - Se tiene cierto conocimiento del sistema
        - Test de penetración como un empleado de la empresa
        - Puede ser realista en ciertos casos (permite ver que puede hacer un empleado desde dentro)

## 2. Ingeniería social

> "El factor determinante de la seguridad de las empresas es la capacidad de los usuarios de interpretar correctamente las políticas de seguridad y hacerlas cumplir" - Kevin Mitnick

- Técnica que trata de **engañar y persuadir**, con la pretensión de **conseguir información útil** y significativa de su **víctima**
- Lo más común es que se haga a través de **canales tecnológicos** (internet, teléfono), pero no tiene por qué
- El **punto más débil** de la seguridad de un sistema es el factor **humano**

### Phishing

- Técnica que consiste en **suplantar una identidad para obtener información**, normalmente credenciales de acceso como contraseñas y usuarios
- Muchos vectores de ataque
    - Mail
    - SMS, teléfono
    - Mobile phishing (Bar spoofing)
    - Codigos QR (QRLJacking)
    - Urls maliciosas (Punycode)

### Clasificación de técnicas de ingeniería social

- Pasivas
    - Observación
- No presenciales
    - Correo electrónico
    - Teléfono
    - Correo ordinario y fax
- Presenciales no agresivas
    - Hablar con la gente
    - Vigilancia
    - Seguimiento
    - Acreditaciones falsas
    - Desinformación
- Presenciales agresivas
    - Suplantación de identidad
    - Chantaje o extorsión
    - Despersonalización (alcohol, drogas…)
    - Presión psicológica

### Medidas de prevención

- **Concienciación** sobre seguridad
    - "nunca compartir la contraseña", no dar información de más, ...
- **Filtrado** de correo
    - El mail es uno de los puntos principales de phising
- **Descentralización**
    - En una empresa, es decir, tener bien definidos y separados los diferentes sistemas por los que se va a transmitir la información

### SEToolkit

- **Herramienta muy potente** para hacer ataques de ingeniería social, como por ejemplo:
    - Spear-Phishing Attack Vectot
    - Website Attack Vector
    - Mass Mailer
    - Infectious Media Generator
    - Wireless Access Point Attack Vector
    - QRCode Generator Attack Vector
    - ...
- Funciona como un Metasploit pero especializado para ingeniería social
- Repo: <https://github.com/trustedsec/social-engineer-toolkit>

## 3. Footprinting

- **Footprinting**:
    - Proceso de **búsqueda** de toda la **información pública**, ya sea publica a propósito o por desconocimiento, que pueda haber del sistema a auditar
    - Buscar *todas las huellas posibles*:
        - **Direcciones IP**
        - **Servidores** internos
        - **Cuentas de correo** de los usuarios
        - **Nombres** de máquinas
        - Información del **DNS**
        - Tipos de servidores
        - **Ficheros** con cuentas y/o credenciales
        - **Impresoras**
        - **Cámaras IP**
        - **Metadatos**
        - Etc.
    - Datos que se van a usar en fases posteriores de la auditoría

### Primeros pasos

- Seleccionar un objetivo
- Navegar por su pagina web, aplicaciones,.. bucar erores
- Buscar "elementos olvidados", errores en llamadas a servidores o BD, ....

### Buscadores

- Son una **gran fuente de información**
- Usan crawlers que en ocasiones **encuentra páginas y archivos que no deberían** estar publicados
- Permiten **buscar subdominios** o dominios asociado
- Tienen **herramientas avanzadas** para filtrar resultados muy útiles para footprinting
    - Por ejemplo los Google Dorks:
        - `site`: para listar toda la información de un dominio concreto.
        - `""`: frase exacta.
        - `-`: no buscar.
        - `*`: comodín.
        - `link`: enlaces a dicha página.
        - `info`: muestra información de la página.
        - `inurl`: para buscar páginas con ciertas palabras en la URL
        - `intitle`: para buscar páginas con ciertas palabras en el campo title.
        - `cache`: caché de Google almacenada
        - `filetype` o `ext`: para buscar archivos de  un formato determinado.
        - Más Dorks: <http://www.exploit-db.com/google-dorks/>
- Hay herramientas que automatizan todos estos procesos

### Servicios web

- Servicios con los que **extraer datos del dominio** objetivo:
    - Dirección IP
    - Subdominios
    - El registrador del dominino (whois)
    - Localización
    - Trazas
    - Servidores DNS
    - Etc.
- Ejemplos
    - Netcraft:
        - Para listar y analizar subdominios
        - <http://searchdns.netcraft.com>
    - Cuwhois:
        - Para hacer un whois
        - <http://www.cuwhois.com>
    - IPTools:
        - <http://www.iptools.com>
    - Yougetsignal:
        - Puertos abiertos, localización, traza de red
        - <http://www.yougetsignal.com>
    - Intodns:
        - Información sobre el servidor DNS
        - <http://www.intodns.com>
    - 123people:
        - Información sobre personas
        - <http://www.123people.es>

#### Peticiones HTTP

- Puede ocurrir que algún webmaster intente engañar:
    - Colocando por ejemplo en un IIS6 una página de error falsa de Apache
    - Necesario contrastar la información
        - Consultar el banner del servidor Web

### DNS

- Es un punto del que se puede sacar **mucha información**
- 4 Técnicas:
    - **Forzar una transferencia de zona** en el servidor DNS
    - **Resolución inversa** mediante los registros PTR a partir de una IP
    - Ataques de **fuerza bruta** utilizando **diccionarios o fuzzers**
    - Ataques de fuerza bruta **identificando relaciones**

### Metadatos

- Si se obtienen archivos de los servidores o a través de los buscadores, los metadatos pueden ser una gran fuente de información
    - Nombres (que pueden llevar a posibles credenciales)
    - Mails
    - Programas usados
    - Y muchos más
- Hay herramientas que permiten automatizar la extracción de archivos y metadatos de un dominio, como la FOCA

#### FOCA

- Herramienta para ayudar en la recolección de ficheros publicados en websites, la extracción de metadatos y el análisis de los mismos
- <https://www.elevenpaths.com/es/innovacion-laboratorio/herramientas/foca>

### Otras herramientas de footprintign

### TheHarvester

- Herramienta para realizar una **búsqueda en los principales motores** y RRSS como Google, Bing, Twitter o LinkedIn, entre otras
- Encuentra correos, servidores y subdominios del dominio junto con sus direcciones IP

#### Maltego

- Herramienta con **entorno gráfico y muchísimas opciones** para obtener información
- Permite **dibujar gráficos de información la entidad** a auditar
    - Con información de personas, correos, documentos, ...
- También permite búsqueda de dispositivos, redes, DNS, documentos, teléfonos, localizaciones, ...
    - E integrar toda esa información en los grafos de Información y relacionar los elementos entre sí

#### "Have I Been Pwned"

- **Base de datos** con listas de correos o **usuarios comprometidos** en algún ataque conocido
- También puede tener enlaces a ficheros con los leaks de dichas credenciales
- Buena herramienta para sacar contraseñas de un usuario o mail encontrado durante el proceso

### Recomendaciones contra procesos de footprinting

- Hay una serie de recomendaciones para evitar o minimizar el efecto de estos procesos de footprinting por parte de las organizaciones y/o personas:
- **Cuidar la información pública** que hay en Internet
    - Configurar lo que se quiere que sea público y privado
- Tener **bien configurados y actualizados los servidores** web y DNS de la compañía
- Tener **separados los correos** de la entidad de los personales
- **Limpiar de metadatos** los documentos públicos

## 4. Fingerprinting

- El **fingerprinting** es el proceso de **recolección de información** en el que se **interactúa directamente** con los sistemas
- Obtener información sobre los **recursos** de las máquina(s) de un objetivo:
    - Puertos abiertos
    - Hosts en la red
    - SO utilizado
    - Software detrás de los puertos
        - Versiones
    - Firewalls, IPS, IDS
    - Etc.
- Lo más típico para realizar esta tarea es el **escaneo de puertos**
    - Dos principales **problemas**:
        - Hace mucho ruido
        - Hay mecanismos que los bloquean y alertan de ellos (Firewalls e IPS)

### Nmap (escaneo de puertos)

- Herramienta para escanear puertos y realizar tareas de fingerprinting
- Muy potente
    - Motor de scripts (NSE) con gran cantidad de scripts incluidos de diferentes categorías
        - Con esos scripts se pueden detectar muchas vulnerabilidades conocidas e incluso realizar labores básicas de explotación
- Opción con interfaz gráfica (Zenmap)

#### TCP Connect() (`-sT`)

- Intenta abrir una conexión TCP
- Para determinar **puertos abiertos**ç
- Realiza todo el Handshake TCP

#### TCP SYN (`-sS`)

- El **más utilizado**
- Efectivo y silencioso
- Para determinar **puertos abiertos**
- Envía un paquete SYN al receptor
    - Si **se recibe SYN+ACK** → **ABIERTO**
        - En ese caso se envía un RST+ACK para finalizar la conexión (no se abre)

#### TCP ACK (`-sA`)

- Indica si un puerto tiene **un firewall**
- Enviará un paquete solo con el flag ACK activado
    - Si se recibe RST → el puerto esta ABIERTO o CERRADO
    - Si **no se recibe nada** → **FILTRADO**

#### TCP NULL (`-sN`)

- Sirve para descubrir **puertos cerrados**
- Paquete con todos los flags desactivados
    - Si no se recibe nada → **ABIERTO**
    - Si se recibe RST+ACK → **CERRADO**

#### TCP XMAS (`-sX`)

- Envía paquetes con los flags FIN, PSH y URG activados
- Sirve para descubrir **puertos cerrados**
    - Si no se recibe nada → **ABIERTO**
    - Si se recibe RST+ACK → **CERRADO**

#### TCP FIN (`-sF`)

- Sirve para descubrir **puertos cerrados**
- Sirve para descubrir **puertos cerrados**
- Manda un paquete con el flag de FIN activado
    - Si no se recibe nada → **ABIERTO**
    - Si se recibe RST+ACK → **CERRADO**

#### TCP IDLE (`-sI`)

- Más complejo
- Requiere de una máquina extra (zombie)
- Lento y poco usado

### Wireshark (sniffing de paquetes)

- **Sniffing**: **capturar paquetes** enviados y recibidos en redes locales, ya sea inalámbricas o por cable
- Es necesario estar en la red
    - Por cable:
        - Todos los paquetes sin cifrar excepto los de conexiones seguras (SSL)
    - Inalámbrica:
        - Solo parquees de redes abiertas
            - Capturar paquetes para romper la red

## 5. Análisis de la información

- Tras recopilar una gran cantidad de información, toca analizarla y quedarse con la **información util**
- **¿Que se puede hacer con cada tipo de información?**

| Dato                                      | Uso                                                                           |
|-------------------------------------------|-------------------------------------------------------------------------------|
| Nombres                                   | Deducir el usuario y cuentas en servicios                                     |
| Emails                                    | Conseguir accesos remotos a servidores                                        |
| La plataforma                             | Posibles vulnerabilidades o elementos mal configurados de esa |  |plataforma  |
| Un sitio web o subdominio                 | Vulnerabilidades y puestos                                                    |
| Agentes externos (ISP, proveedores, etc.) | Posibles vías a través de las que interceptar comunicaciones                  |
| Una intranet/extranet                     | Extraer datos internos interesantes                                           |
| Una carpeta o archivo oculto              | Datos de interés                                                              |
| Teléfonos y direcciones                   | Para hacer ingeniería social                                                  |
| Passwords                                 | Para probarlas en servicios                                                   |
| Datos personales                          | Probarlos como passwords o usarlos como ingeniería social                     |
| Un tipo de regla de firewall o IDS        | Técnicas para aludirlo o inhabilitarlo                                        |
| Arquitecturas y Protocolos                | Información para saber como poder articular un ataque                         |
| Puertos abiertos                          | Extraer información como versión, servicios, vulnerabilidades de ese servicio |
| Dirección IP                              | Tratar de ubicar en la red                                                    |
| Clase de antivirus                        | Buscar vulnerabilidades que no detecte ese antivirus                          |
| Una versión de aplicación                 | Búsqueda de vulnerabilidades concretas                                        |
