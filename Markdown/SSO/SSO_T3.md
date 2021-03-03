# Tema 2: Seguridad en otros Sistemas Operativos

## 2.1 Seguridad en macOS

### Autenticación local & Open Directory

- **Autenticación local**:
    - Autenticarse una sola vez y obtener:
        - Keychain del sistema,
        - Servicios de directorio para autenticación en red
- **PAM** (*Pluggable Authentication Modules*):
    - macOS, como Linux, soporta PAM
- **Open Directory**:
 Servicio de directorio que almacena información sobre la red, los usuarios y recursos. **Tres componentes** principales:
    - **Servidor LDAP** (basado en OpenLDAP)
        - Se usa en grandes organizaciones
    - **Servidor de contraseñas**
        - Controla la autenticación
        - Separado del servidor LDAP
    - **KDC** (*Kerberos Distribution Center*) para intercambiar claves de forma segura (SSO (*Single Sign-On*))
        - KDC local pero se puede conectar Open Directory al KDC de otra máquina
        - Con un solo usuario y contraseña Kerberos gestiona la autenticación a **todos** los servicios y sistemas
        - Safari, NFS, SMB, AFP, mail, Telnet, SSH, VPN, ...
- **Active Directory** (AD):
    - Permite a macOS interactuar con redes Windows
- **Tarjetas inteligentes**

### Keychain

- Es el gestor de contraseñas integrado en macOS
- Centraliza todas las contraseñas
- Triple DES
- Directorios de almacenamiento de claves

    ```bash
    ~/Library/Keychains/
    /Library/Keychains/
    /Network/Library/Keychains/
    ```

### Sistemas de permisos y autorización

- macOS hereda el sistema de permisos de UNIX
- Cuenta `root` deshabilitada por defecto
    - `sudo` para ejecutar comandos con elevación de privilegios
- Tres tipos de usuarios en macOS
    - **Usuario**: sin privilegios, solo puede modificar aspectos locales a su cuenta
    - **Administrador**: puede hacer todas las operaciones de `root` *excepto* tocar archivos del dominio del sistema
    - **Root**
- Fichero de configuración para los permisos de cada usuario:
    - `System/Library/Security/authorization`
    - `.plist` (XML)

### FileVault

- Herramienta de cifrado de disco
- AES-XTS-128 o AES-XTS-256
- Muy util para un usuario
    - En ámbitos multiusuario puede dar problemas
        - Solo es usuario que ha cifrado el disco puede descifrarlo

### GateKeeper

- Protección para aplicaciones que se descargan directamente de internet:
    - (Tiene algunas funciones como el UAC de Windows)
    - Añade atributos de metadatos en el momento de la descarga, con información como origen, fecha, hora…
    - Avisa al intentar ejecutar aplicaciones descargadas de internet
    - Si la aplicación no esta firmada genera otro aviso

### Xprotect

- Sistema de protección contra malware integrado en macOS:
    - Contiene un conjunto de firmas para malware conocido
    - Hace comprobaciones de versiones de las aplicaciones:
    - Deshabilita versiones de aplicaciones que contienen vulnerabilidades conocidas
    - Se actualiza automáticamente
    - Ficheros principales:
        - `XProtect.plist`: firmas de malware
        - `XProtect.meta.plist`: versiones de plugins contiene las versiones de los plugins
        - `Exceptions.plist`: sitios exluidos de XProtect

### Firewall

#### Application Layer Firewall (ALF)

- Firewall personal
    - Por defecto viene desactivado
- Se configura mediante una interfaz gráfica
- Permite bloquear solo las **conexiones entrantes**
- Como **política por defecto** bloquea las conexiones entrantes a software no firmado

#### Packet Filter (PF)

- Cortafuegos a más bajo nivel
    - Estilo iptables
- Se configura con:
    - `pfctl`: utilidad para configurarlo
    - `/etc/pf.conf`: fichero de configuración por defecto

### Logs

- El sistema de logs de macOS es **casi idéntico al de Linux**
- Permite loguear, entre otras cosas:
    - Autenticación (locales y remotas (SSH, VNC, ...))
    - Actividad del firewall
    - Sudo
    - Ficheros compartidos
    - Acceso web
    - DNS Lookup
    - Avisos de software de seguridad
- Los logs se guardan en /var/log:
    - `/Library/Logs`: aplicaciones comunes
    - `~/Library/Logs`: aplicaciones del usuario
- Niveles de severidad clavado al de Linux:
    - *Emergency* (Nivel 0)
    - *Alert* (Nivel 1)
    - *Critical* (Nivel 2)
    - *Error* (Nivel 3)
    - *Warning* (Nivel 4)
    - *Notice* (Nivel 5)
    - *Info* (Nivel 6)
    - *Debug* (Nivel 7)
