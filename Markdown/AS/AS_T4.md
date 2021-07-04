# Tema 4: Auditorías operativas/técnicas

## 1. Introducción y objetivos

- Dos tipos de auditorías de seguridad:
    - Auditoría de seguridad operativa/técnica
        - Seguridad **física**: Protección del **HW, instalaciones**, ...
        - Seguridad **lógica**: **Uso del** SW, HW, comunicaciones
        - Seguridad de las **operaciones**: **operaciones de seguridad de los CPD**
    - Auditoría de cumplimiento de la seguridad de la información

## 2. Auditorías de la infraestructura física

- Las infraestructuras físicas se enfrentan a riesgos:
    - Industriales
    - Humanos
    - Acciones malintencionadas
- Es importante centrarse también en controles físicos y no solo en controles lógicos
- **Clasificación** de controles según **ISACA**:
    - *Administrativos*
        - Políticas, procedimientos, ...
    - *Técnicos*
        - Controles lógicos: red, sistemas IDS, antivirus, ...
    - **Físicos**
- **Elementos auditoría física**
    - Factores de riesgo externos
    - Sistemas de seguridad física
    - Controles ambientales
    - Alimentación eléctrica
    - Protección contra el fuego
    - Protección TEMPEST

## 3 Auditorías de sistemas de recuperación ante desastres :red_circle:

- Plan de Contingencia de las Tecnologías de la Información y las Comunicaciones (TIC)
    - Entre otras cosas, *contiene*:
        - **Plan de Recuperación ante Desastres** (**DRP**, *Disaster Recovery Plan*)
- **Fases de un DRP**
    - **Alinearlo** con el plan de continuidad de negocio
    - Realizar una **evaluación de riesgos**
    - Llevar a cabo un **análisis de impacto** de negocio
    - **Desarrollar las medidas de recuperación** para los servicios y aplicaciones
    - **Realizar pruebas**
    - **Actualizar y mejorar** el plan
    - **Capacitar a los encargados de ponerlo en marcha, concienciar y difundir** el plan
- **Aspectos a auditar**
    1. La **resiliencia** del sistema
        - Verificar sistemas de redundancia HW
    2. **Copias de seguridad y restauración** de datos
        - Verificar que los procedimientos son apropiados
        - Verificar la capacidad de recuperación de las copias
    3. Verificar la integridad y **precisión del DRP**
        - Verificar que existe
        - Verificar que se actualiza y se prueba continuamente
        - Verificar que aborda los diferentes escenarios de desastre
    4. Evaluar el **desempeño del personal** involucrado en el DRP
        - Nivel de entrenamiento y conciencia
- El **DRP se puede activar por**:
    - Pérdida de conectividad
    - Pérdida de sistema IT critico
    - Pérdida de CPD
    - Pérdida de datos críticos
    - Pérdida de instalaciones
    - Pérdida de servicios clave (cloud, ..)

## 4. Auditoría de las operaciones

- *Áreas* que deberían cubrirse se encuentran las siguientes (operaciones de, por ejemplo, un CPD):
    - La **vigilancia de las instalaciones**
    - **Funciones y responsabilidades** del personal del centro de datos
    - **Segregación de las tareas** del personal del centro de datos
    - **Respuesta a emergencias** y desastres
    - **Mantenimiento** de las instalaciones y el equipo
    - Planificación de la **capacidad del centro** de datos
    - **Gestión de activos**
    - **Contenido y ubicación del almacenamiento** fuera de línea

## 5. Auditorías técnicas de seguridad

- *Objetivo*:
    - **Analizar la seguridad** implantada en los **sistemas de información** y telecomunicaciones
- *Tipos*:
    - Auditoría de **seguridad en sistemas** :white_square:
    - Auditoría de **seguridad en redes** :white_square:
    - **Pruebas de penetración** :white_square: :white_square_button: :black_square:
    - Auditorías de **aplicaciones web** (DAST):black_square:
    - Auditoría **redes WIFI** :black_square:
    - Auditorías de **sistemas de seguridad perimetral** :white_square:
    - Auditoría de **aplicaciones** :white_square:
    - Auditorías de **sistemas de VoIP** :white_square:
    - Auditoría de **seguridad en dispositivos móviles** :white_square:
    - Auditorías de **denegación de servicio** :black_square:
- Se pueden clasificar en:
    - **Caja blanca**
    - **Caja negra**
    - **Caja gris**
- **Fases** básicas de auditorías técnicas:
    1. La **recopilación de información** del sistema por auditar
    2. **Análisis de vulnerabilidades**
    3. **Explotación** y ataque de las vulnerabilidades detectadas
    4. Realización de **informe técnico** y ejecutivo

### Auditoría de seguridad en sistemas

- Análisis y revisión de la seguridad de:
    - **BD, servidores, DNS, equipos, VM, almacenamiento**, ...
- Puntos importantes:
    - Revisar configuración de los sistemas con la **guía de configuración de la organización** (CCN, NIST, DISA)
    - Arquitecturas de **alta disponibilidad**
    - Analizar **vulnerabilidades** (Nessus, OpenVAS, ...)
    - Informes de disponibilidad e utilización del HW
    - **Documentación** de sistemas
    - **Procedimientos** y controles
    - Fortaleza de **contraseñas**

### Auditoría de seguridad en redes

- Análisis y revisión de la seguridad de:
    - **Infraestructura de red corporativa**
- Puntos importantes:
    - Arquitectura, topología y componentes de la red
    - **HW** de la red
    - **Uso y métricas** de la red (informes)
    - Armarios y **cableado**
    - **Servidores** de red
    - **Planes** y procedimientos de seguridad de la red
    - *Herramientas*: **Sniffing, MITM, análisis de  vulnerabilidades**, ...

### Pruebas de penetración

- Análisis y revisión de la seguridad de:
    - Equipos y sistemas *mediante*:
        - **Test de intrusión controlados**
- Puntos importantes:
    1. **Recopilación** de la información
    2. **Análisis** de vulnerabilidades
    3. **Explotación** de vulnerabilidades
    4. **Post-explotación**
    5. **Informe**

### Auditorías de aplicaciones web

- Análisis y revisión de la seguridad de:
    - Una o varias **aplicaciones web**
- Puntos importantes:
    - Uso de metodologías como **OWASP** (*Open Web Application Security Project*)
    - DAST (*Dynamic Application Security testing*) (OWASP ZAP, Burpsuite)

### Auditoría redes WIFI

- Análisis y revisión de la seguridad de:
    - **Redes inalambricas**
- Puntos importantes:
    - Descubrimiento y **fingerprinting**
    - Comprobación de sistemas de **autenticacion, cifrado**
    - Revision de **configuración**
    - Pruebas de **DoS**
    - **Búsqueda de *rogue AP***
    - ...
    - Uso de metodologías como **OWISAM** (*Open WIreless Security Assessment Methodology*)
    - *Herramientas*: Aircrack-ng, Wifite, ...

### Auditorías de sistemas de seguridad perimetral

- Análisis y revisión de la seguridad de:
    - Mecanismos de **seguridad perimetral** (AP, Firewall, DMZ, ...)
- Puntos importantes:
    - Auditar **apps o webs expuestos**
    - Auditar **elementos de la DMZ**: DNS, apps, ...)
    - Auditar elementos de protección: **Firewalls, WAF, proxies**
    - **Pentesting *black box***

### Auditoría de aplicaciones

- Análisis y revisión de la seguridad de:
    - **Software y aplicaciones**
- Puntos importantes:
    1. **Planificación**
    2. Recolección de **info**
    3. **Ejecución** de la auditoría
        - Controles de **entrada/salida**
        - **Análisis de código fuente**
        - **Análisis dinámico**
        - **Criptografía**
        - **Contraseñas**
        - ...
    4. **Informes**

### Auditoría de seguridad en dispositivos móviles

- Análisis y revisión de la seguridad de:
    - **Dispositivos móviles corporativos**
- Puntos importantes:
    - **Políticas de uso**
    - **Administración** de los dispositivos
    - Sistemas de **protección** (antimalware, etc.)
    - **Cifrado**
    - **Configuración de las comunicaciones**
    - Uso de metodologías como **OASAM** (*Open Android Security Assessment Methodology*)

### Auditorías de denegación de servicio

- Análisis y revisión de la seguridad de:
    - *Los sistemas ante*:
        - **Ataques de DoS**
- Puntos importantes:
    - Ataques **volumétricos**: HTTP Flood, SYN Flood, UDP Flood
    - Ataques por **fragmentación**: IP Fragmentation, Tear drop
    - Ataques a la **capa de aplicación**
    - Ataque de **consumo del estado de TCP**
    - *Herramientas*: LOIC, hping3, Thor Hammer, ...

### Auditorías de sistemas de VoIP

- Análisis y revisión de la seguridad de:
    - **Protocolos y sistemas de llamadas** por internet
- Puntos importantes:
    - Ataques de tipo: Vishing, Fuzzing, Floods, DoS, Hijacking, ...
    - Comprobar configuración y protocolos
    - Fingerprinting (REGISTER, INVITE, OPTION)
    - Analizar vulnerabilidades

## 6. Auditoría del acceso lógico

- **Evaluar los controles de protección y gestión** de los activos de información
- Tareas del auditor:
    - Obtener una **compresión general de los riesgos de seguridad** a los que se enfrenta los sistemas TIC de la organización
    - **Documentar y evaluar los controles** sobre las rutas de acceso potencial para ver si son adecuados, eficientes y efectivos
    - **Probar los controles** sobre las rutas de acceso para verificar si están funcionado y son efectivos
    - **Evaluar el ambiente de control de acceso** para determinar si se logran los objetivos de control
    - **Evaluar el ambiente de seguridad** para determinar si es adecuado
