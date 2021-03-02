# Tema 2: Seguridad en Linux

## 2.1 Introducción a la seguridad en Linux

Los OS basados en Linux tienen tres partes: HW, kernel y aplicaciones

### Kernel

Para entender la seguridad en el núcleo de Linux hay que tener claro los
siguientes aspectos:
Las opciones de red
Los algoritmos de cifrado que soporta
Hardware de cifrado que soporta
El sistema de archivos
Las herramientas del proyecto GNU

#### El sistema de archivos

En un sistema operativo Linux podemos tener diferentes tipos de archivos:

| Símbolo   | Tipo de archivo                     |
|-----------|-------------------------------------|
| `-`       | Archivo regular                     |
| `d`       | Directorio                          |
| `l`       | Enlace                              |
| `c`       | Dispositivos orientado a caracteres |
| `s`       | Socket                              |
| `p`       | Pipe                                |
| `b`       | Dispositivo orientado a bloques     |

##### Permisos

En función del tipo de archivos se podrá tener unos permisos u otros. La estructura de los permisos (al examinarlos por ejemplo con un `ls -al`) se puede ver al principio de cada entrada:

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

En la primera parte es donde se puede apreciar el sistema de permisos:

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

Aclaraciones:
    - Permiso de ejecución sobre una carpeta implica que se pueda acceder a ella o no

### Seguridad en la instalación

La mayor parte de distribuciones disponen de dos modos:

- Arranque normal
- Arranque en modo *live*

Es recomendable utilizar el modo live para hacer cualquier operación previa sobre los discos o particiones.

**Recomendación:** cifrado del disco con LUKS.

#### sistema de carpetas de Linux

- /
    - `/bin`: binarios
    - `/boot`: archivos relacionados con GRUB
    - `/dev`: Discos duros, etc.
    - `/etc`: ficheros de configuración del sistema y de aplicaciones + scripts que se ejecutan al iniciar el sistema
    - `/home`: carpetas personales, accesibles solo por cada usuario y root
    - `/lib`: librerías del sistema y drivers
    - `/lost+found`: donde se almacenan las cosas en caso de que pete
    - `/media`, `/mnt`: punto de montaje para unidades extraíbles o temporales
    - `/opt`: paquetes adicionales para aplicaciones
    - `/proc`: información dinámica del kernel de Linux
    - `/root`: es la carpeta personal del administrador (`root` no tiene carpeta en `/home`)
    - `/sbin`: binarios del sistema
    - `/tmp`: ficheros temporales (se limpia cada vez que arranca el sistema)
    - `/usr`: configuración y aplicaciones instaladas
    - `/var`: ficheros dinámicos, como buffers, logs, ...

Conviene separar en particiones ciertos directorios del sistema
    - Lo mas común es separar `/boot` y `/home` del resto del fs:
        - Se separa el sector de arranque del resto para securizarlo
        - Se separa `/home` del resto para tener por separado los archivos personales
    - Añadir una partición `swap` para paginar memoria

### Protección del sistema de arranque (BIOS/UEFI, GRUB, Terminal…)

- GRUB es el gestor de arranque por defecto en la mayoría de distribuciones Linux
- Para protegerlo se puede asignar una contraseña (contra cambios) de la siguiente manera

    1. `grub-mkpasswd-pbkdf2` para btener un hash PBKDF2 de la contraseña que queramos configurar
    contraseña

    2. Configurar un superusuario con esa contraseña modificando el fichero `/etc/grub.d/40_custom`:

        ```bash
        set superusers="superusuario"
        password_pbkdf2 superusuario <hash_generado>
        ```

    3. Editar del fichero`/etc/default/grub` la línea:

        ```bash
        GRUB_TERMINAL=console
        ```

    4. `update-grub` para actualizar GRUB

### Actualización del sistema operativo

Actualizar los paquetes es fundamental. Cada distro tiene sus métodos.

- Debian (Ubuntu)

    ```bash
    apt update
    apt upgrade
    ```

- Red hat / Fedora

    ```bash
    yum check-update
    yum install update
    ```

- Suse

    ```bash
    zypper refresh
    zypper update
    ```

- Arch linux

    ```bash
    pacman –Syu
    ```

- Gentoo

    ```bash
    emerge rsync
    emerge --update --deep @world
    ```

- Slackware

    ```bash
    slackpkg update
    slackpkg upgrade-all
    ```

### Bastionado (*hardening*) del sistema operativo

#### *Hardening*: Ejecución de comandos de administración

- `root` (`UID=0`) es el administrador del sistema y tiene permisos completos
- solo es recomendable para algunas opraciones de administrador
    - Es mejor técnica ganar privilegios desde un usuario normal. Dos metodos
        1. Convertirse en `root` usando `su`
        2. Usar `sudo`
            - Modificar `/etc/sudoers` para ver que usuarios pueden ejecutar sudo
                - Por defecto: usuarios del grupo `sudo` pueden ejecutar `sudo`
    - `root` hace que se pierda la trazabilidad de los cambios
- **CONCLUSIÓN**:
    - Fuck `root`, always `sudo`/`su`

#### *Hardening*: Usuarios

- Gestionar los usuarios que hay en el sistema para evitar que tenga privilegios de mas o usuarios no necesarios
- Hay muchos mas usuarios de los creados "manualmente"
    - Hay programas o servicios que tienen sus propios usuarios y grupos específicos que se son creados automáticamente por ellos

- Comandos básicos
    - `useradd`/`groupadd`
    - `usermod`/`groupmod`
    - `userdel`/`groupdel`
    - `adduser` (versión de "alto nivel" que usa `useradd` por debajo)
    - `deluser` (versión de "alto nivel" que usa `userdel` por debajo)
    - `passwd`

#### *Hardening*: Permisos

- Es conveniente saber como modificar los permisos para evitar que usuarios no autorizados accedan a donde no deban.
- `chmod`
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

- Umask permite configurar los permisos por defecto para los ficheros creados por un usuario
    - <https://phoenixnap.com/kb/what-is-umask>
- Permisos SETUID y SETGID
    - SETUID → El proceso adquiere los permisos del propietario del fichero:
        - chmod u+s calculadora
    - SETGID → El proceso adquiere los permisos del grupo del fichero:
        - chmod g+s calculadora
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
    - Cifrado a nivel sistema de ficheros:
        - eCryptfs, EncFS, …
    - Cifrado a nivel de bloque/dispositivo:
        - dm-crypt+LUKS
        - Veracrypt …

#### *Hardening*: Terminales habilitados

- Los "terminales" que usamos habitualmente no son terminales reales, sino emulaciones de terminal.
- En linux, se puede acceder a las terminales reales mediante CTRL+ALT+F1-12 (dependiendo de que terminales se encuentre habilitadas)
- Se puede modificar las terminales habilitadas modificando el fichero `/etc/securetty`

## 5.2 Autenticación SSH

- El uso de SSH es muy comun para poder realizar labores de administracion o despliegue sobre servidores de manera remota
- SSH es uno de los servicios de Linux más usados
- Es uno de los vectores principales por donde se puede intentar atacar
    - Fuerza bruta ([Hydra](https://github.com/vanhauser-thc/thc-hydra))
    - Explotación de vulnerabilidades
    - Malas configuraciones
    - Robo de credenciales
- Es esencial fortificarlo
    - Directivas de configuración
    - Limitar informacion hacia el exerior
    - Claves RSA
    - 2FA

### OpenSSH: Configuración

- Ficheros de configuración:
    - Cliente SSH

        ```bash
        /etc/ssh/ssh_config
        ```

    - Servidor SSH

        ```bash
        /etc/ssh/sshd_config
        ```

    - Configuracion PAM (*Pluggable Authentication Module*)

        ```bash
        /etc/pam.d/sshd
        ```

    - Arranque del servicio

        ```bash
        /etc/init.d/sshd
        ```

#### Configuración segura del servidor SSH

```bash
Port 22                             # ¿Se recomienda cambiar el puerto por defecto?
ListenAddress 192.168.1.2           # Interfaz que va a recibir las peticiones 
                                    #       → Solo desde red de gestión
Protocol 2                          # Utilizar solamente la última versión (2)
PermitRootLogin no                  # Nunca permitir a root conectarse por SSH
AllowUsers user1 user2@83.45.258.21 # Permitir acceso a solo a usuarios concretos
LoginGraceTime 10                   # Reducir tiempo de "intento" de autenticación
MaxAuthTries 10                     # Reducir número de intentos de autenticación
MaxStartups N                       # Número de sesiones sin autenticación
X11Forwarding no                    # Denegar conexiones al servidor gráfico X11
```

### Minimizar la exposiciñon de informacion

Ejemplo de banner SSH:

```bash
kali@kali~$ ssh alumno@192.168.1.48
alumno@192.168.1.48's password
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.19.0-25-generic x86-64)

 * Documentation: https://help.ubuntu.com
```

*OBJETIVO*: Reducir el banner que se muestra al intentar conectarse por SSH. Pasos:

1. Abrir el banner y modificarlo

    ```bash
    vi /etc/ssh/sshd_banner
    ```

2. Añadir al fichero de configuracion del servidor (`/etc/sshd/sshd_config`) la siguiente linea para usar el banner:

    ```bash
    Banner /etc/ssh/sshd_banner
    ```

3. Reiniciar el servicio de SSH:

    ```bash
    /etc/init.d/sshd restart
    ```

*Otra opción*: editar el propio binario `/usr/sbin/sshd` con algun editor de binarios como `hexedit`.

### Acceso SSH con claves RSA

- Metodo mas seguro que la autenticación por contraseña
    - Impide ataques por fuerza bruta
    - Limita las máquinas que pueden conectarse
    - Es mucho mas facil robar una contraseña que una clave RSA
        - Las claves RSA se almacenan en las máquinas cliente cifradas con contraseña

- Pasos para configurar acceso a SSH con claves RSA:

    1. Generar par de claves en el cliente y mandar la clavepública al servidor

        ```bash
        ssh-keygen -t rsa –b 2048
        scp -p id_rsa.pub alumno@IP_SERVIDOR:/tmp/
        ```

    2. En el servido, añadir dicha clave al fichero de claves autorizadas:

        ```bash
        mkdir .ssh
        chmod 700 .ssh/
        cat /tmp/id_rsa.pub >> ~/.ssh/authorized_keys
        chmod 600 .ssh/authorized_keys
        rm /tmp/id_rsa.pub
        ```

    3. Deshabilitar la autenticación con contraseña en el servidor modificando el archivo `/etc/ssh/sshd_config`:

        ```bash
        PasswordAuthentication no
        ```

### Segundo factor de autenticación (2FA)

- Es una buena opcion si se quiere seguir usando la contraseña para acceder
- Pasos:

    1. Modificar el fichero `/etc/pam.d/sshd` y añadir configuracion para F2A concreto:

        ```bash
        auth required pam_google_authenticator.so
        ```

    2. En el fichero `/etc/ssh/sshd_config`, activar la verificación en dos pasos:

        ```bash
        ChallengeResponseAuthentication yes
        ```

    3. Reiniciar el servidor SSH:

        ```bash
        sudo service ssh restart
        ```