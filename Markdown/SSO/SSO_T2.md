# Tema 2: Seguridad en Linux

## 1. Introducción a la seguridad en Linux

### Kernel

- Aspectos relevantes sobre la seguridad en Linux:
    - Las opciones de red
    - Los algoritmos de cifrado que soporta
    - Hardware de cifrado que soporta
    - El sistema de archivos
    - Las herramientas del proyecto GNU

#### El sistema de archivos

- En un sistema operativo Linux podemos tener diferentes tipos de archivos:
    - `-`: Archivo regular
    - `d`: Directorio
    - `l`: Enlace
    - `c`: Dispositivos orientado a caracteres
    - `s`: Socket
    - `p`: Pipe
    - `b`: Dispositivo orientado a bloques

##### Permisos

- En función del tipo de archivos se podrá tener unos permisos u otros
- La estructura de los permisos se puede ver al principio de cada entrada
    - Al examinarlos, por ejemplo, con un `ls -al`:

```bash
total 32
drwxr-xr-x 4 ander ander 4096 Feb 24 14:22 ./
drwxr-xr-x 3 root  root  4096 Feb 12 22:39 ../
-rw------- 1 ander ander   71 Feb 24 14:22 .bash_history
-rw-r--r-- 1 ander ander  220 Feb 12 22:39 .bash_logout
-rw-r--r-- 1 ander ander 3771 Feb 12 22:39 .bashrc
drwx------ 3 ander ander 4096 Feb 24 14:22 .config/
drwxr-xr-x 2 ander ander 4096 Feb 12 22:39 .landscape/
-rw-r--r-- 1 ander ander    0 Mar  2 15:12 .motd_shown
-rw-r--r-- 1 ander ander  807 Feb 12 22:39 .profile
-rw-r--r-- 1 ander ander    0 Feb 12 22:39 .sudo_as_admin_successful
```

- Detalle de permisos:

```bash
0 1 2 3 4 5 6 7 8 9     [usr]  [grp]

d r w x r - x r - x  2  ander  ander  4096  Feb 12 22:39  .landscape/
```

- `0`: tipo de archivo
- `1-3`: permisos de lectura/escritura/ejecución (rwx) del archivo del owner del archivo
- `4-6`: permisos de lectura/escritura/ejecución (rwx) del archivo para el grupo de usuarios al que pertenece el archivo
- `7-9`: permisos de lectura/escritura/ejecución (rwx) del archivo para el resto
- `[usr]`: El usuario dueño del archivo
- `[grp]`: El grupo dueño del archivo
- Aclaraciones:
    - Permiso de ejecución sobre una carpeta implica que se pueda acceder a ella o no

### Seguridad en la instalación

- La mayor parte de distribuciones disponen de dos modos:
    - Arranque normal
    - Arranque en modo *live*
- Recomendable utilizar el modo live para hacer cualquier operación previa sobre los discos o particiones
- **Recomendación:** cifrado del disco con LUKS

#### Estructura de directorios de Linux

- `/`
    - **`/bin`**: binarios
    - **`/boot`**: archivos relacionados con GRUB
    - **`/dev`**: discos duros, etc.
    - **`/etc`**: ficheros de **configuración del sistema** y de aplicaciones + scripts que se ejecutan al iniciar el sistema
    - **`/home`**: carpetas personales, accesibles solo por cada usuario y root
    - **`/lib`**: librerías del sistema y drivers
    - **`/lost+found`**: donde se almacenan las cosas en caso de que pete
    - **`/media`**, **`/mnt`**: punto de montaje para **unidades extraíbles** o temporales
    - **`/opt`**: paquetes adicionales para aplicaciones
    - **`/proc`**: información **dinámica del kernel** de Linux
    - **`/root`**: es la carpeta personal del administrador (`root` no tiene carpeta en `/home`)
    - **`/sbin`**: binarios del sistema
    - **`/tmp`**: ficheros temporales (se limpia cada vez que arranca el sistema)
    - **`/usr`**: **configuración y aplicaciones** instaladas
    - **`/var`**: ficheros dinámicos, como buffers, **logs**, ...

#### Particionado en la instalación

- **Conviene separar en particiones** ciertos directorios del sistema
    - Lo más común es **separar `/boot` y `/home`** del resto del fs:
        - Se separa el sector de arranque del resto para securizarlo
        - Se separa `/home` del resto para tener por separado los archivos personales
    - Añadir una **partición `swap`** para paginar memoria

### Protección del sistema de arranque (BIOS/UEFI, GRUB, Terminal…)

- GRUB es el **gestor de arranque por defecto** en la mayoría de distribuciones Linux
- Para protegerlo se puede asignar una contraseña (contra cambios) de la siguiente manera:

```bash
# 1. grub-mkpasswd-pbkdf2 para obtener un hash PBKDF2 de la contraseña que queramos configurar
grub-mkpasswd-pbkdf2

# 2. Configurar un superusuario con esa contraseña modificando el fichero /etc/grub.d/40_custom:
set superusers="superusuario"
password_pbkdf2 superusuario <hash_generado>

# 3. Editar del fichero`/etc/default/grub` la línea:
GRUB_TERMINAL=console
    
# 4. update-grub para actualizar GRUB
update-grub
```

### Actualización del sistema operativo

- Actualizar los paquetes es fundamental. Cada distro tiene sus métodos

### Bastionado (*hardening*) del sistema operativo

#### *Hardening*: Ejecución de comandos de administración

- `root` (`UID=0`) es el administrador del sistema y tiene permisos completos
    - Solo es recomendable para algunas operaciones de administrador
    - Es mejor técnica ganar privilegios desde un usuario normal. Dos métodos:
        1. Convertirse en `root` usando `su`
        2. Usar `sudo`
            - Modificar `/etc/sudoers` para ver que usuarios pueden ejecutar sudo
                - Por defecto: usuarios del grupo `sudo` pueden ejecutar `sudo`
    - `root` hace que se pierda la trazabilidad de los cambios
- **CONCLUSIÓN**:
    - Fuck `root`, always `sudo`/`su`

#### *Hardening*: Usuarios

- **Gestionar los usuarios** que hay en el sistema para **evitar que tenga privilegios de más** o usuarios no necesarios
- Hay muchos más usuarios de los creados "manualmente"
    - Hay programas o servicios que tienen sus propios usuarios y grupos específicos que se son creados automáticamente por ellos
- Comandos básicos:
    - `useradd`/`groupadd`
    - `usermod`/`groupmod`
    - `userdel`/`groupdel`
    - `adduser` (versión de "alto nivel" que usa `useradd` por debajo)
    - `deluser` (versión de "alto nivel" que usa `userdel` por debajo)
    - `passwd`

#### *Hardening*: Permisos

- Es conveniente saber **como modificar los permisos** para evitar que usuarios no autorizados accedan a donde no deban
- **`chmod`**
    - Para cambiar los permisos de un archivo, directorio, etc.
        - Modo "caracteres"
        - Modo "octetos" (más comodo)

| Permiso | Número | R | W | X |
|:-------:|:------:|:-:|:-:|:-:|
| `---`   | 0      | 0 | 0 | 0 |
| `--x`   | 1      | 0 | 0 | 1 |
| `-w-`   | 2      | 0 | 1 | 0 |
| `-wx`   | 3      | 0 | 1 | 1 |
| `r--`   | 4      | 1 | 0 | 0 |
| `r-x`   | 5      | 1 | 0 | 1 |
| `rw-`   | 6      | 1 | 1 | 0 |
| `rwx`   | 7      | 1 | 1 | 1 |

| Modo "caracteres"        | Modo "octetos" |
|--------------------------|----------------|
| `chmod u=rwx,g=rwx,o=rx` | `chmod 775`    |
| `chmod u=rwx,g=rx,o=`    | `chmod 760`    |
| `chmod u=rw,g=r,o=r`     | `chmod 644`    |
| `chmod u=rw,g=r,o=`      | `chmod 640`    |
| `chmod u=rw,go=`         | `chmod 600`    |
| `chmod u=rwx,go=`        | `chmod 700`    |

- **Umask permite configurar los permisos por defecto** para los ficheros creados por un usuario
    - <https://phoenixnap.com/kb/what-is-umask>
- Permisos SETUID y SETGID
    - **SETUID** → El proceso adquiere los permisos del propietario del fichero:
        - `chmod u+s calculadora`
    - **SETGID** → El proceso adquiere los permisos del grupo del fichero:
        - `chmod g+s calculadora`
- **Auditoría 101**: Buscar ficheros con bit `SETUID y SETGID:

```bash
find / \( -perm -4000 -o -perm 2000 \) –ls
```

- `lsattr`/`chattr`
    - Listar o modificar los atributos de los ficheros
- ACLs (Access Control Lists) → `getfacl` y `setfacl`
    - <http://bencane.com/2012/05/27/acl-using-access-control-lists-on-linux/>

#### *Hardening*: Deshabilitar servicios innecesarios

- Para ver que servicios de red hay a la escucha:

```bash
netstat –atu
# O tambien
cat /etc/inetd.conf
```

- Para ver que servicios están habilitados:

```bash
systemctl list-units | grep enable
```

- Iniciar y denener servicios

```bash
# Servicios basados en /etc/init.d

sudo /etc/init.d/<service_name> stop    # Denener el servicio
sudo /etc/init.d/<service_name> start   # Iniciar el servicio
sudo update-rc.d <service_name> disable # Deshabilitar arranque al inicio
sudo update-rc.d <service_name> enable  # Habilitar arranque al inicio del sistema

# Servicios basados en Upstart

sudo service <service_name> stop        # Denener el servicio
sudo service <service_name> start       # Denener el servicio
sudo vi /etc/init/cron.conf             # Modificar arranques al iniciar
```

#### *Hardening*: Cifrado de información

- Dos niveles de cifrado
    - Cifrado a **nivel** sistema de **ficheros**:
        - eCryptfs, EncFS, …
    - Cifrado a **nivel** de bloque/**dispositivo**:
        - dm-crypt+LUKS
        - Veracrypt …

#### *Hardening*: Terminales habilitados

- Los "terminales" que se usan habitualmente no son terminales reales, sino emulaciones de terminal
- En linux, se puede acceder a las **terminales reales** mediante **CTRL+ALT+F1-12** (dependiendo de que terminales se encuentre habilitadas)
- Se puede modificar las terminales habilitadas modificando el fichero **`/etc/securetty`**

## 2. Autenticación SSH

- El **uso de SSH es muy común** para poder realizar labores de administración o despliegue sobre servidores de manera remota
- SSH es uno de los servicios de Linux **más usados**
- Es uno de los **vectores principales** por donde se puede **intentar atacar**
    - Fuerza bruta ([Hydra](https://github.com/vanhauser-thc/thc-hydra))
    - Explotación de vulnerabilidades
    - Malas configuraciones
    - Robo de credenciales
- Es esencial **fortificarlo**
    - Directivas de configuración
    - Limitar informacion hacia el exerior
    - Claves RSA
    - 2FA

### OpenSSH: Configuración

- Ficheros de configuración:

```bash
/etc/ssh/ssh_config     # Cliente SSH
/etc/ssh/sshd_config    # Servidor SSH
/etc/pam.d/sshd         # Configuracion PAM (Pluggable Authentication Module)
/etc/init.d/sshd        # Arranque del servicio
```

#### Configuración segura del servidor SSH

- Muchas opciones que revisar para asegurar que la configuración es segura. Entre otras:
    - ¿**Cambiar el puerto** por defecto?
    - Permitir **únicamente interfaz** que va a recibir las peticiones
        - Solo desde red de gestión
    - Utilizar solamente la **última versión**
    - **Nunca permitir a root** conectarse por SSH
    - Limitar el acceso**usuarios concretos**
    - **Reducir**
        - **tiempo de intento** de autenticación
        - **número de intentos** de autenticación
    - **Denegar** conexiones al **servidor gráfico** X11

```bash
Port 22                             # ¿Se recomienda cambiar el puerto por defecto?
ListenAddress 192.168.1.2           # Interfaz que va a recibir las peticiones 
                                        # Solo desde red de gestión
Protocol 2                          # Utilizar solamente la última versión (2)
PermitRootLogin no                  # Nunca permitir a root conectarse por SSH
AllowUsers user1 user2@83.45.258.21 # Permitir acceso solo a usuarios concretos
LoginGraceTime 10                   # Reducir tiempo de "intento" de autenticación
MaxAuthTries 10                     # Reducir número de intentos de autenticación
MaxStartups N                       # Número de sesiones sin autenticación
X11Forwarding no                    # Denegar conexiones al servidor gráfico X11
```

### Minimizar la exposiciónn de informacion

- Ejemplo de banner SSH:

```bash
kali@kali~$ ssh alumno@192.168.1.48
alumno@192.168.1.48 password:
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.19.0-25-generic x86-64)

* Documentation: https://help.ubuntu.com
```

- *OBJETIVO*: Reducir el banner que se muestra al intentar conectarse por SSH. Pasos:

```bash
#  1. Abrir el banner y modificarlo
vi /etc/ssh/sshd_banner

# 2. Añadir al fichero de configuracion del servidor (`/etc/sshd/sshd_config`) la siguiente linea para usar el banner:
Banner /etc/ssh/sshd_banner

# 3. Reiniciar el servicio de SSH:
/etc/init.d/sshd restart
```

- *Otra opción*: editar el propio binario `/usr/sbin/sshd` con algun editor de binarios como `hexedit`

### Acceso SSH con claves RSA

- Metodo **más seguro que** la autenticación por **contraseña**
    - **Impide** ataques por **fuerza bruta**
    - **Limita las máquinas** que pueden conectarse
    - Es mucho más facil robar una contraseña que una clave RSA
        - Las claves RSA se almacenan en las máquinas cliente cifradas con contraseña

- Pasos para configurar acceso a SSH con claves RSA:

```bash
# 1. Generar par de claves en el cliente y mandar la clave pública al servidor
ssh-keygen -t rsa –b 2048
scp -p id_rsa.pub alumno@IP_SERVIDOR:/tmp/

# 2. En el servidor, añadir dicha clave al fichero de claves autorizadas:
mkdir .ssh
chmod 700 .ssh/
cat /tmp/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 .ssh/authorized_keys
rm /tmp/id_rsa.pub

# 3. Deshabilitar la autenticación con contraseña en el servidor modificando el archivo /etc/ssh/sshd_config:
nano /etc/ssh/sshd_config
PasswordAuthentication no
```

### Segundo factor de autenticación (2FA)

- Es una buena opcion si se quiere seguir usando la contraseña para acceder

```bash
# 1. Modificar el fichero /etc/pam.d/sshd y añadir configuracion para F2A concreto:
auth required pam_google_authenticator.so

# 2. En el fichero /etc/ssh/sshd_config, activar la verificación en dos pasos:
ChallengeResponseAuthentication yes

# 3. Reiniciar el servidor SSH:
sudo service ssh restart
```

## 3. Otras medidas de seguridad: Syslog, SELinux, AppArmor, Grsecurity

### Syslog

- **Sistema estándar logs** (local + red)
    - Casi todas las distribuciones de Linux lo tienen
    - Permite registrar todo tipo de eventos
- Los mensajes tienen un **formato estandarizado**
- Los logs se guardan en:
    - **`/var/log`**
- Servidor para almacenamiento y gestion de logs:
    - `syslogd/syslog-ng/rsyslog`
- Para usarlo se arranca:
    - `/etc/init.d/sysklogd`
- Configuración en:
    - **`/etc/syslog.conf`**

#### Niveles de log

- `0`: Emergency
- `1`: Alerts
- `2`: Critical
- `3`: Errors
- `4`: Warnings
- `5`: Notification
- `6`: Information
- `7`: Debug

#### *Facilities*

- Permiten categorizar los logs
    - `auth`: Logs de autenticación
    - `cron`: Logs provenientes del planificador
    - `daemon`: Logs provenientes de los demonios
    - `kern`: Logs del kernel
    - `lpr`: Logs de impresoras
    - `mail`: Logs del sistema de correo
    - `user`: Logs provinientes de procesos de usuario
    - `local0 - local7`: Definidos por el usuario
    - `syslog`: Logs procedentes del propio syslog

#### logrotate

```bash
# /etc/logrotate.conf:
/var/log/syslog {
    create 700 test test # Permisos y dueños fichero log
    daily # Rotar el log diariamente
    size 100M # Rotar el log si llega a 100MB
    rotate 7 # Mantener histórico de 7 ficheros de log
    compress # Comprimirlos con gzip
}
```

#### Journalctl

- El sistema de logs de systemd

### SELinux

- Es un módulo de seguridad propio del kernel de linux
    - **Proteger** un sistema contra **malas configuraciones o aplicaciones comprometidas**
- Define una política de seguridad que establece, por ejemplo, a qué ficheros puede acceder cada proceso (independientemente de sus permisos)
- SELinux asigna **etiquetas asociadas a usuarios y procesos**:
    - Nombre de Usuario
    - Rol
    - Tipo/Nivel/Dominio
- Las **restricciones** vienen determinadas por las **reglas establecidas en la política**

#### Discretionary Access Control (DAC)

- Mecanismo de **control de acceso** común para **sistemas UNIX**
    - **Todo proceso se ejecuta bajo un usuario y un grupo**
    - El proceso **tiene acceso a lo del usuario y grupo**
    - Por ejemplo:
        - `apache` se ejecutará como `apache:apache`
        - El proceso httpd tiene acceso a todos los ficheros y directorios a los que tiene acceso el usuario apache
        - Esto se extiende a todos los scripts que se ejecuten bajo este demonio (php, cgi, ...)

#### Mandatory Access Control (MAC) (SELinux)

- Permite **definir permisos** para los procesos **mediante políticas**
- **Controla con qué partes** del sistema **puede interactuar cada proceso**
    - Protege datos de acceso no autorizado
    - Protege otros demonios de acceso no autorizado
    - Protege puertos/sockets/ficheros
    - Protege contra exploits
    - Ayuda a prevenir escaladas de privilegios
- **No es una solución mágica**
    - Política correcta de firewall
    - Monitorización del sistema y logs
    - Actualizar el sistema / asegurar scripts expuestos al público

#### Modos de SELinux

- Tres **modos**
    - **Enforcing**
        - Alerta y aplica acciones establecidas si se viola alguna regla
    - **Permissive**
        - SELinux aplica las políticas pero no toma acciones, solo alerta
    - **Disabled**
- Se configura en `/etc/selinux/config`

#### Políticas de SELinux

- La configuración se puede encontrar en `/etc/selinux/config`
    - **Targeted**
        - Solo una serie de procesos se controlan con SELinux
        - Es la política por defecto
        - Es un control eficaz
        - Para el resto solo se aplica la politica estándar de linux (DAC)
    - **Multinivel (MLS/MCS)**:
        - Control estricto (insfraestructuras críticas, etc.)

### AppArmor

- **Programa de seguridad** para Linux
- Fue creado como una alternativa **más sencilla que SELinux**
- **Perfiles** de AppArmor
    - Ficheros de texto en `/etc/apparmor.d` con los nombres de los binarios
    - Dos **tipos de reglas**
        - **Path**:
            - A que ficheros puede acceder una aplicación
        - **Capability entries**:
            - Que privilegios puede usar un proceso
    - Dos **modos** de ejecución:
        - **complain**: solo logging, no toma acciones
        - **enforce**: logging + tomar acciones

### Grsecurity

- Conjunto de parches con mejoras de seguridad para el kernel de Linux
    - Sistema de control de acceso basado en Roles.
        - Se definen un conjunto de roles a los que les asigna los privilegios mínimos necesarios para desempeñarlos
- **Restringe la utilidad de chroot** para prevenir escaladas de privilegios
- Viene con PAX:
    - Pila no ejecutable
    - Espacio de memoria de aplicación solo lectura
    - **ASLR** (*Address Space Layout Randomization*)
        - Para **evitar *buffer overflows***

## 4. Securizar el acceso a red: IPtables, SIEM, UTM…

- Bloquear hosts permitidos y denegados
    - `/etc/hosts.allow` y `/etc/hosts.deny`
- Cortafuegos (iptables) y otras medidas

### IPTables (Netfilter)

- IPtables: componente de netfilter
    - **Cortafuegos de estado**
    - `**Reglas + Cadenas + Tablas**
        - Se define mediante reglas que se evalúan secuencialmente
        - Las reglas se agrupan en cadenas
        - A su vez las cadenas se agrupan en tablas asociadas a diferentes tipos de procesamiento de paquetes

#### Tablas

- **`filter`** → Filtra paquetes (es la que se usa por defecto)
- **`nat`** → NAT paquetes
- **`mangle`** → Modifica paquetes (por ejemplo su TTL)
- **`raw`** → Permite deshabilitar el connection tracking
- **`security`** → Usado por SELinux

#### Cadenas

- Varían en funció de la tabla
    - **`INPUT`**: paquetes de entrada
    - **`OUTPUT`**: paquetes de salida
    - **`FORWARD`**: paquetes que no tienen como origen ni destino el cortafuegos
    - **`PREROUTING`**: enrutar paquetes de entrada de NAT
    - **`POSTROUTING`**: erutar paquetes de salidad de NAT

#### Reglas

```bash
iptables –t <table> –{A|I|R|D} <chain> <match> –j <target>
```

Objetivos de reglas `(<target>`):

- **`ACCEPT`**: Se acepta el paquete
- **`DROP`**: Se descarta el paquete
- **`REJECT`**: Igual que 'DROP', pero envía un paquete de error al origen
- **`LOG`**: Loguear el paquete
- `QUEUE`: Este destino hace que el paquete sea enviado a una cola de recepción.
- `DNAT`: Se reescribe la dirección y/o puertos destino del paquete
- `SNAT`: Se reescribe la dirección y/o puertos origen del paquete con una IP estática
- `MASQUERADE`: Similar SNAT pero basado en la IP (e.g. dinámica) de la interfaz de salida
- `<chain>`: Salta a esa cadena y empieza a procesar sus reglas
- `RETURN` (retorno): El paquete deja de recorrer esa cadena y vuelve a la anterior

### UTM

- *Unified Threat Management*
- Un **producto todo-en-uno** que incluye múltiples soluciones de seguridad:
    - Firewall de red
    - NIDS
    - Antivirus
    - Anti-spam
    - VPN
    - Filtro de contenido
    - Balanceador de carga
    - Control de acceso basado en identidad
    - QoS
    - Prevención de pérdida de datos (DLP)
    - Emisor de informes
    - ...
- Ejemplo: *pfSense*

### SIEM

- *Security Information and Event Management*
- Software que proporciona:
    - Un **análisis en tiempo real** de las **alertas de seguridad generadas** por los dispositivos hardware y las aplicaciones que hay en una red
– Ejemplo.: *OSSIM*

## 5. Proxies e IDS

### Proxy

- Serivdor intermediario entre peticiones
- *Permite*
    - **Control de acceso**
    - **Registro del trafico**
    - **Restriccion de contenidos**
    - **Mejora de rendimiento**
    - Anonimato
    - ...
- *Ventajas*
    - Tener comunicaciones bajo control
        - Fácil denegar o permitir el acceso a subredes y equipos
        - Es facil crear *blacklists*
    - Caché comun (acelera acceso a webs que suelen usar varios usuarios)
    - Generacion de informes de trafico
    - El proxy hace de barrera
- *Desventajas*
    - Es necesario configurarlo en cada aplicación
    - Si falla se corta la conexion a internet (proxy de respaldo)
    - Requiere mantenimiento
    - Privacidad y seguridad (todo pasa por el proxy)

#### Squid

- Uno de los proxies más famosos para linux
- Se configura en `/etc/squid/squid.conf`
- Listas de control de acceso donde se identifica a que elementos se aplica y los filtros

```bash
acl <nombre_lista> <tipo> <elemento_lista>
```

- Parámetros
    - `http_port`: Puerto del proxy
    - `cache_dir`: Directorio donde almacenará la cache
    - `cache_dir` aufs /var/spool/squid 2048 16 256
    - `cache_replacement_policy`: Política de reemplazo de objetos en caché
    - `maximum_object_size`: Tamaño máximo del objeto que va a ser almacenado en cache
    - `cache_mem`: Memoria de objetos en transito

### IDS

- Programas capaces de **detectar accesos no autorizados** y peticiones maliciosas mediante patrones o heurísticas
- Tipos de IDS (fuentes de alertas):
    - **Host-based (HIDS)**
        - Se ejecuta en el propio quipo final
        - Sirve para poder detectar intrusiones en el sistema final y recoger información sobre ellas
        - Ejemplo: *OSSEC*
    - **Network-based (NIDS)**
        - Captura tráfico de una interfaz de red
            - Modo online (inline)
            - Tipo offline (network tap)
        - Compara las capturas con firmas preestablecidas
        - Ejemplo: *Snort*
