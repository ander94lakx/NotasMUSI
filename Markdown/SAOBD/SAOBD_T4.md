# Tema 4: Seguridad en sistemas gestores de bases de datos

## 1. Vulnerabilidades y amenazas en bases de datos

- **Contraseñas débiles** y por defecto
- **Inyecciones SQL en el SGBD** (CWE 89)
- **Excesivos privilegios** en usuarios y grupos (CWE 250, CWE 269)
- **Opciones innecesarias** habilitadas en el SGBD
- **Ataques** a la gestión de **la configuración** (CWE 829, CWE 269)
- **Buffer overflows** (CWE 121 – 122)
- **Escalada de privilegio**s (CWE 264, 269, 250, 272)
- Ataques **(D)DoS**
- **No aplicar** el adecuado nivel de **parches** de seguridad
- **Datos no protegidos** almacenados o en tránsito (TLS)
- **XSS persistente**
- **LFI-RFI** (`SELECT * LOAD_FILE("/etc/shadow")`)
- Webshells (para atacar a BD)

## 2. Seguridad en sistemas gestores de bases de datos

- *Objetivos* de seguridad en BD:
    - **Comprender los riesgos y amenazas** que los SGBD y sus BD instaladas pueden sufrir a partir de su arquitectura y características
    - Identificar los elementos de seguridad de los SGBD
    - Identificar y trazar las actividades y medidas de seguridad del **SSDLC para implantar dichos elementos de seguridad** los **SGBD** en las fases de **diseño, implementación y producción**
- *Objetivos concretos*:
    - **Proteger frente accesos no autorizados** (intencionados o
    - Restricciones de **integridad** en la BD: de dominio, de entidad, clave e integridad referencial
    - Herramientas y mecanismos de **copias de seguridad y restauración**
    - Recuperar la BD llevándola a un **estado consistente**
    - Acceso **concurrente** y ofrecer mecanismos para conservar la consistencia

### Tipos de usuarios en un SGBD

- **Usuario** de la aplicación
    - Operaciones CRUD con limitaciones
- **Propietario de la aplicación**
    - Posee todos los objetos definidos y utilizados por una aplicación
- **Administrador de usuarios de aplicaciones**
    - Privilegios para crear y administrar usuarios y asignar roles de aplicaciones a los
- **Cuenta de aplicación**
    - Proceso automatizado
- **Operador** de base de datos
    - Privilegios administrativos limitados
- **DBA (Administrador)**
    - Privilegios completos para todos los objetos, recursos y usuarios en la base de datos
- **Auditor de base de datos**
    - Gestión de registros de auditoría de base de datos (modo lectura)
    - Solo el tiene acceso (ni el DBA)

### Funciones del usuario DBA

- **Tareas**
    - Instalar SGBD en el sistema informático
    - Crear las BBDD que se vayan a gestionar
    - Crear y mantener los esquemas de BD
    - Crear y mantener las cuentas de usuario de BD
- **Normativa**:
    - Establecer estándares de uso, políticas de acceso y protocolos de trabajo diario para los usuarios de la BD
- **Monitorización**:
    - **Vigilar el trabajo** diario (colaborando resolución de dudas)
    - **Controlar en tiempo real** los accesos, tasas de uso, cargas en los servidores, anomalías, ...
    - Backups periódicos de la BD (o usuario operador)
- **Recuperación**
    - Restaurar la BD después de un incidente material a partir de los backups
- **Mejora continua**
    - Ajustar y optimizar la BD con ayuda de herramientas y estadísticas

## 3. Protección online y auditoría de bases de datos

- **DAM** (*Database Activity Monitoring*)
    - Tecnología de seguridad para el seguimiento y análisis de la actividad en BD
    - **Independiente** del SGBD
    - Supervisión en **tiempo real y continua**
    - Proporcionan alertas en base a diferentes *criterios*:
        - *Control de comportamientos*
        - *Vigilancia del cumplimiento*
        - **Protección contra ciberataques**
- **DAP** (*Database Audit Protection*)
    - Incorporan los criterios de DAM
    - Suites de herramientas para identificar y reportar el comportamiento inapropiado
    - *Capacidades*:
        - Esenciales:
            - **Recolección de eventos, análisis e informe**
            - Gestión y **auditoría de la política** de seguridad de la base de datos.
            - **Monitorización** de actividades privilegiadas
        - Secundarias:
            - Prevención y **bloqueo** de acceso/ataques
            - **Descubrimiento** y clasificación
            - Vulnerabilidades y **gestión de la configuración**
            - **Auditoría** y monitorización de **usuarios y aplicaciones**
            - **Evaluación de usuarios** y permisos
