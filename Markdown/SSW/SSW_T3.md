# Tema 3: Codificación segura

## 1. Listado de vulnerabilidades en el código (ejemplos, problemas y soluciones)

- *Manejo de la entrada de datos*
    - Límites de confianza
    - Comprobar la longitud de entrada
    - Comprobar el tamaño de los campos numéricos
    - *Prevenir vulnerabilidades de meta-caracteres*
        - SQL injection
        - Path Traversal
        - Inyección de comandos
        - Falsificación de logs
- *Desbordamiento de buffer*
    - Seguridad de tipo
    - Seguridad en llamadas a métodos nativos
    - Desbordamiento de buffer basado en el stack
    - *Reserva dinámica de memoria (heap overflow)*
        - Memory leaks
        - Use after free
        - Dereference after free
        - Double free
        - Null dereference
    - *Manipulación de strings*
        - Funciones peligrosas
        - Errores de truncado
        - Mantenimiento del `\0`
        - Format strings
- *Integers overflows*
    - Integer overflows
    - Conversiones entre enteros con signo y sin signo
- *Errores y excepciones*
    - Manejar errores mediante códigos de retorno
    - Manejo de errores mediante excepciones
    - Desasignar los recursos que no se van a utilizar en adelante
- *Privacidad y confidencialidad*
    - Mantener las password fuera del código fuente
    - Número aleatorios
- *Programas privilegiados*
    - Manejo de los privilegios
    - *Ataques de escalada de privilegios*
        - Ataque de condiciones de carrera en el acceso a ficheros
        - Ficheros temporales inseguros
        - Inyección de comandos
        - Descriptores de ficheros

## 2. Manejo de la entrada de datos

- Una de las **medidas más importantes** que un programador puede realizar:
    - **Validar todas las entradas de datos**
- ¿Qué validar?
    - Validar **toda la entrada**
    - Validar la entrada de **todas las fuentes**
        - No solo la del usuario, también:
            - Linea de comandos, archivos de configuración, otros archivos, servicios de red, URL, Cookies, ...
    - Establecer fronteras de confianza
    - Comprobar tanto sintaxis como semántica
- ¿Cómo validar?
    - Usar una **fuerte validación** de entrada
    - Evitar poner en la lista negra
    - No confundir usabilidad y seguridad
    - No confundir la validación de funcionalidad con la validación de entrada para la seguridad
    - Rechazar datos maliciosos
    - Hacer una buena validación de entrada por defecto
    - Siempre comprobar la longitud de entrada
    - Limitar la entrada numérica

### Establecer los límites de confianza

```java
String user_state = "Unknown";
try {
    HttpSession user_session = Init.sessions.get(tmpUser.getUser());
    user_state = user_session == null ? "Unknown" :
    (String) user_session.getAttribute("USER_STATUS");
    user_state = user_state == null ? "Available" : user_state;
}
...
%>
<%=user_state %>
```

- :no_entry_sign:
- **Problema**:
    - No se valida la variable de sesión HTTP
    - Se usa después para genera un JSP 🠒 **XSS**
- **Solución**:
    - Validar la entrada

```java
status = request.getParameter("status");
if (status != null && status.length() > 0) {
    session.setAttribute("USER_STATUS", status);
}
```

- :no_entry_sign:
- **Problema**:
    - No se filtra el dato, se puede setear cualquier cosa
- **Solución**:
    - Validar la entrada

### Comprobar la longitud de entrada

```java
if (path != null && path.length() > 0 && path.length() <= MAXPATH) { // OK!
    fileOperation(path);
}
```

- :heavy_check_mark:
- Se asegura que la longitud no haga fallar ni crashear el programa

### Comprobar el tamaño de los campos numéricos

```java
void* doAlloc(int sz) {
    return malloc(sz); /* Implicit conversion here: malloc() accepts an unsigned argument. */
}
```

- :no_entry_sign:
- **Problema**:
    - Conversión implícita
    - No se limita el tamaño de memoria que se puede reservar
- **Solución**:
    - Comprobar los límites y valores razonables

### Prevenir vulnerabilidades de meta-caracteres

- Hay caracteres que pueden modificar los comandos, segun la tecnología varía
- Hay que controlar que la entrada no contenga esos caracteres

| Ataque              | Implicaciones                                                   |
|---------------------|-----------------------------------------------------------------|
| **SQL Injection**   | Accede/modifica datos en la base de datos                       |
| **XPath Injection** | Accede/modifica datos en formato XML                            |
| **SSI Injection**   | Ejecuta comandos sobre el servidor y accede a datos sensibles   |
| **LDAP Injection**  | Bypass de autenticación                                         |
| **MX Injection**    | Usa el servidor de correos como una máquina de spam             |
| **HTTP Injection**  | Modifica o intoxica el caché de los sitios web                  |

#### SQL injection

```java
String userName = ctx.getAuthenticatedUserName();
String itemName = request.getParameter("itemName");
String query = "SELECT * FROM items WHERE owner = '"
                            + userName + "' AND itemname = '"
                            + itemName + "'";
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(query);
```

- :no_entry_sign:
- **Problema**:
    - No se comprueba la entrada
    - Se puede realizar una **SQL Injection** usando:
        - ``` name' OR 'a'='a ```
- **Solución**:
    - Eliminar carácteres especiales (validar entrada)
    - Usar Stored Procedures (SP)

#### Manipulación de rutas (Path Traversal)

- Caracteres peligrosos: `/`, `\`, `.`

```java
String rName = request.getParameter("reportName");
File rFile = new File("/usr/local/apfr/reports/" + rName);
rFile.delete();
```

- :no_entry_sign:
- **Problema**:
    - No se comprueba la entrada 🠒 **Inyeccion de path** como: `../../tomcat/conf/server.xml`
        - Se puede acceder a tantos arcivos tenga acceso como el proceso que lo ejecuta
- **Solución**:
    - Whitelists
    - Filtrado de patrones de ruta o caracteres especiales

#### Inyección de comandos

```java
String btype = request.getParameter("backuptype");
String cmd = new String("cmd.exe /K \"c:\\util\\rmanDB.bat "
                        + btype + "&&c:\\utl\\cleanup.bat\"")
Runtime.getRuntime().exec(cmd);
```

- :no_entry_sign:
- **Problema**:
    - Se puede inyectar un comando como 🠒 `&& del c:\\dbms\\*.*`
        - Si el proceso tiene privilegios, se puede ejecutar cualquier cosa
- **Solución**:

#### Falsificación de logs

```java
String val = request.getParameter("val");
try {
int value = Integer.parseInt(val);
}
catch (NumberFormatException) {
log.info("Failed to parse val = " + val);
}
```

- :no_entry_sign:
- **Problema**:
    - No se filtran los caracteres especiales HTML
    - Si llega con algo como: `«twenty-one%0a%0aINFO:+User+logged+out%3dbadguy»` 🠒 Inyectada info falsa
- **Solución**:
    - Filtrar caracteres especiales

## 3. Desbordamiento de buffer

### Seguridad de tipo

```c
int (*cmp)(char*,char*);
int *p = (int*)malloc(sizeof(int));
*p = 1;
cmp = (int (*)(char*,char*))p;
cmp(“hola”,”adios”); // El programa realiza un crash
```

- :no_entry_sign:
- **Problema**:
    - Se usa un puntero como si fuera de otro tipo (`int` 🠒 `funcion`)
    - Puede dar desbordamientos y chrasheos
- **Solución**:
    - No cambiar entre tipos de punteros
    - Lenguajes seguros (Java, ...) no lo tienen

### Seguridad en llamadas a métodos nativos

- **Lenguajes como Java eliminan algunos peligros** que tienen lenguajes como C/C++:
    - Manipulación de punteros implícita
    - Límites de arrays, strings son automáticamente comprobados
    - Null pointers capturados en excepciónes
    - Las operaciones aritméticas están bien definidas
    - Control de acceso a ficheros y sockets mediante: JVM 🠒 Security Manager
- Aun asi **pueden dar problemas de memoria** a niveles más bajos: (JVM en C)

```java
class Echo {
    public native void runEcho();
    static {
        System.loadLibrary("echo");
    }
    public static void main(String[] args) {
        new Echo().runEcho();
    }
}
```

```c
#include <jni.h>
#include "Echo.h" // Echo class compiled with javah
#include <stdio.h>
JNIEXPORT void JNICALL
Java_Echo_runEcho(JNIEnv *env, jobject obj)
{
    char buf[64];
    gets(buf);
    printf(buf);
}
```

- :no_entry_sign:
- **Problema**:
    - Se hace uso de una **librería nativa programada en C**
        - Si tiene vulnerabilidades se pueden explotar desde el programa de Java
- **Solución**:
    - Hacer uso de **librerías nativas seguras**

### Desbordamiento de buffer basado en el stack

```c
void trouble() {
    int a = 32; /*integer*/
    char line[128]; /*character array*/
    gets(line); /*read a line from stdin*/
}
```

- :no_entry_sign:
- **Problema**:
    - `gets()` lee hasta encontrar final de linea (`\0`), por lo que se puede desbordar el buffer
    - Se puede pisar la dirección del stack y hacer que salte a otro sitio o resbale con NOPs
        - Inyectar shellcodes
    - [Más info](https://github.com/ander94lakx/NotasMUSI/blob/master/Markdown/AV/AV_T2.md#ejemplo-de-buffer-overflow)
- **Solución**:
    - Limitar el numero de caracteres a leer

### Reserva dinámica de memoria (heap overflow)

- Con memoria dinámica también se pueden dar overflows
- Con la memoria dinámica, se pueden distinguir las siguientes vulnerabilidades:
    - Memoria no utilizada, sin desasignar (memory leaks)
    - Use after free
    - Dereference after free
    - Double free
    - Null dereference

#### Memoria no utilizada, sin desasignar (memory leaks)

```c
#include <stdlib.h>
void function_which_allocates(void) {
    float * a = malloc(sizeof(float) * 45);
    return;
}
int main(void) {
    function_which_allocates();
    // ....
}
```

- :no_entry_sign:
- **Problema**:
    - Se reserva memoria para 45 floats en una funcion local
    - Se retorna
    - Desde fuera no se tiene acceso al puntero 🠒 **No se puede liberar la memoria**: Memory leak
    - Puede desde malgastar memora a suponer un problema de seguridad
- **Solución**:
    - Librera la memoria tras usarla

#### Use after free

```c
char* ptr = (char*)malloc (SIZE);
// ...
if (tryOperation() == OPERATION_FAILED) {
    free(ptr);
    errors++;
}
// ...
if (errors > 0) {
    logError("operation aborted before commit", ptr);
}
```

- :no_entry_sign:
- **Problema**:
    - Se esta usando un **puntero** que **ya ha sido liberado**
    - Si un **atacante llena esa zona** 🠒 **buffer overfloy**
- **Solución**:
    - No usar punteros ya liberados

#### Dereference after free

```c
#include <stdio.h>
#include <unistd.h>
#define BUFSIZER1 512
#define BUFSIZER2 ((BUFSIZER1/2) - 8)
int main(int argc, char **argv) {
    char *buf1R1;
    char *buf2R1;
    char *buf2R2;
    char *buf3R2;
    buf1R1 = (char *) malloc(BUFSIZER1);
    buf2R1 = (char *) malloc(BUFSIZER1);
    free(buf2R1);
    buf2R2 = (char *) malloc(BUFSIZER2);
    buf3R2 = (char *) malloc(BUFSIZER2);
    strncpy(buf2R1, argv[1], BUFSIZER1-1); /* lo vuelvo a utilizar */
    free(buf1R1);
    free(buf2R2);
    free(buf3R2);
}
```

- :no_entry_sign:
- **Problema**:
    - El punteo `buf1R1` se vuelve a usar tras ser liberado
    - Puede desde crashear a leer algo corrupto o malicioso
- **Solución**:
    - No usar punteros liberados

#### Double free

```c
int * ab = (int*) malloc (SIZE);
// ...
if (c == 'EOF') {
free(ab); 
}
// ...
free(ab);
```

- :no_entry_sign:
- **Problema**:
    - Se libera un puntero dos veces
    - Puede corromper la memoria o abrir brechas para realizar buffer overflow
- **Solución**:
    - No liberar un puntero ya liberado

#### Null dereference

```c
#include <stdlib.h>
int main(int argc, char *argv[]) {
    int k = 0;
    int *p = (int *) NULL;
    switch (k) {
        case 0:
            if (*p) k = *p;
        default:
            break;
    }
    return 0;
}
```

- :no_entry_sign:
- **Problema**:
    - Se usa un puntero nulo
    - Segmentation fault
- **Solución**:
    - No usar punteros nulos (comprobacion)

### Manipulación de strings

- Con respecto a la manimpulacion de strings, se pueden encontrar diversos problemas:
    - Funciones inherentemente peligrosas
    - Operaciones con strings de tamaño limitado
    - Errores de truncado
    - Mantenimiento del carácter nulo de terminación
    - Errores de formato de cadena (format strings)

#### Funciones inherentemente peligrosas

- Entre ellas, las más comunes en C son:
    - `gets()`
    - `scanf()` (`fscanf()`, `wscanf()`)
    - `strcpy()` (`wcscpy()`, `lstrcpy()`)
    - `sprintf()` (`fprintf()`, `printf()`, `swprintf()`)

```c
char line[512];
gets(line);
```

```c
char var[128], val[15 * 1024], ..., boundary[128], buffer[15 * 1024];
// ...
for(;;) {
    // ...
    // Si la variable es seguida por filename="name"' es un fichero
    inChar = getchar();
    if (inChar == ';') {
        //...
        // scan tiene el formato definido pero no la cantidad de datos incluir en buffer
        scanf(" Formato: %s ", buffer);
```

```c
char *FixFilename(char *filename, int cd, int *ret) {
    // ...
    char fn[128], user[128], *s;
    // ...
    s = strrchr(filename,'/');
    if(s) {
        strcpy(fn,s+1);
```

```c
char speed[128];
// ...
sprintf(speed, "%s/%d", (cp = getenv("TERM")) ? cp : "", (def_rspeed > 0) ? def_rspeed : 9600);
```

- :no_entry_sign:
- **Problema**:
    - Se explotan llamadas a funciones inseguras
    - Este tipo de funciones tienen  el inconventiene de leer hasta carácter nulo `\0`
        - Las hace fácilmente explotables
    - Segun el tipo se pueden hacer diferentes acciones:
        - Jugar con las combicaciones de tamaños y conversiones de formatos
            - Buffer overflow
- **Solución**:
    - Usar versiones seguras de estas funciones

#### Errores de truncado

```c
char path[PATH_MAX];
char buf[PATH_MAX];
if(S_ISLNK(st.st_mode)) {
    len = readlink(link, buf, sizeof(path));
    buf[len] = '\0';
}
strncpy(path, buf, len);
```

- :no_entry_sign:
- **Problema**:
    - **Off-by-one**
        - Al copias se usa un len incorrecto, ya que el `\0` se pone despues y la longitud que de puede ser hasta `sizeof(path)`
- **Solución**:
    - Nunca truncar los datos
    - Si la entrada es demasiado grande ir leyendo iterativamente

#### Mantenimiento del carácter nulo de terminación

```c
char buf[MAXPATH];
readlink(path, buf, MAXPATH);
int length = strlen(buf);
```

- :no_entry_sign:
- **Problema**:
    - `readlink()` no termina con `\0` su buffer
    - Valor incorrecto de `length`
- **Solución**:
    - Nunca asumir que los datos estan bien terminados

#### Errores de formato de cadena (format strings)

| Par.  | Salida                                                                                                                              | Pasado como |
|-------|-------------------------------------------------------------------------------------------------------------------------------------|-------------|
| `%d`   | Formato de enteros                                                                                                                  | Valor       |
| `%f`   | Formato de punto flotante                                                                                                           | Valor       |
| `%s`   | Formato cadena                                                                                                                      | Referencia  |
| `%x`   | Formato hexadecimal                                                                                                                 | Valor       |
| `%p`   | Muestra el correspondiente valor del puntero                                                                                        | Referencia  |
| `%n`   | En el entero correspondiente a esta especificación de formato se almacena el número de caracteres hasta ahora escritos en el buffer | Referencia  |
| `<n>$` | Parámetro de acceso directo                                                                                                         | Valor       |

```c
// Vulnerable.c:
#include <stdio.h>
int main(void) {
    char texto[30];
    scanf(“%29s”, texto);
    printf(texto);
    return 0;
}
```

- :no_entry_sign:
- **Problema**:
    - No se espedifica el tipo de dato en `printf()`
    - Un atacante podría usar `%x` y `%s` para acceder a los conenidos
        - Podría usar `%n` para escribir en las direcciones de memoria
- **Solución**:
    - Filtrar parámetros de formato de cadena

## 4. Integers overflows

- Consiste en almacenar un valor demasiado grande en una variable para hacer que pueda sobrepasar y:
    - Vuelva a cero (unsigned)
    - Número negativo muy grande (signed)

### Integer overflows

```c
unsigned int readamt;
readamt = getstringsize();
if (readamt > 1024)
    return -1;
readamt--; // don't allocate space for '\n'
buf = malloc(readamt);
```

- :no_entry_sign:
- **Problema**:
    - Si `getstringsize()` llega a devulver `0` 🠒 malloc brutalmente grande
- **Solución**:
    - Comprobar límites superiores e inferiores

```c
int ConcatBuffers(char *buf1, char *buf2, size_t len1, size_t len2){
    char buf[0xFF];
    if((len1 + len2) > 0xFF) return -1;
    memcpy(buf, buf1, len1);
    memcpy(buf + len1, buf2, len2);
    // do stuff with buf
    return 0;
}
```

- :no_entry_sign:
- **Problema**:
    - Si la suma de `len1 + len2` hace overflow
        - Se pasa el control del `if` y se puede hacer buffer overflow en los `memcpy()`
        - Ejemplo: `len1 = 0x103; len2 = 0xFFFFFFFC`
- **Solución**:
    - Comparar todas las longitudes, no la suma

### Conversiones entre enteros con signo y sin signo

```c
char* processNext(char* strm) {
    char buf[512];
    short len = *(short*) strm;
    strm += sizeof(len);
    if (len <= 512) {
        memcpy(buf, strm, len);
        process(buf);
        return strm + len;
    }
    else {
        return -1;
    }
}
```

- :no_entry_sign:
- **Problema**:
    - `len` está declarado como tipo short (con signo)
    - Al compararse se compara con signo
    - Si len fuera negativo, tendia un valor adecuado pero
    - Al hacer el `memcpy` ahi se convierte a unsigned 🠒 mucha reserva de memoria 🠒 buffer overflow
- **Solución**:
    - Usar tipso adecuados

## 5. Errores y excepciones

- Las excepciones son un avance en comparacion a otros metodos:
    - C 🠒 códigos de error
    - C++ 🠒 mezcla de códigos de erorr y excepciones sin comprobar
    - Java 🠒 excepciones comprobadas

### Manejar errores mediante códigos de retorno

```c
char buf[10], cp_buf[10];
fgets(buf, 10, stdin);
strcpy(cp_buf, buf);
```

- :no_entry_sign:
- **Problema**:
    - No se comprueba el código de error de `fgets()`
    - Si ha dado error, puede dejar el buffer sin `\0` 🠒 buffer overflow
- **Solución**:
    - Comprobar los códigos de error

```java
FileInputStream fis;
byte[] byteArray = new byte[1024];
for (Iterator i=users.iterator(); i.hasNext();) {
    String userName = (String) i.next();
    String pFileName = PFILE_ROOT + "/" + userName;
    FileInputStream fis = new FileInputStream(pFileName);
    try {
        fis.read(byteArray); // El fichero es siempre de 1k bytes
        processPFile(userName, byteArray);
    }
    finally {
        fis.close();
    }
```

- :no_entry_sign:
- **Problema**:
    - No se mira el valor de retorno de `read()` (numero de bytes leídos)
    - Se procesa el archivo sin más
    - Se puede aprovechar para meter informacion dañina
- **Solución**:
    - Comprobar siempre que los valores de retorno de una funcion sean los esperados

### Manejo de errores mediante excepciones

- Las excepciones permiten la separación entre el código que sigue un camino esperado y el código que maneja circunstancias anormales
- Requiere que ante excepciones *checked* haya que implementar código
- Tipos:
    - **Checked**: requieren ser manejadas
        - O se tratan
        - O se delegan para que se traten desde fuera
        - Pero en algun momento se tienen que tratar
        - Es un enfoque seguro
        - Ejemplo: Java
    - **Unchecked**: no tienen que ser declaradas
        - Se pueden ignorar y el compilador no se queja
        - Es más peligroso
        - Ejemplo: C++
- **Consejos**:
    - Caputar extensiones en el nivel superior
    - No incluir `return` en el bloque `finally`
        - Es como si nunca hubiera saltado la excepcion
    - Caputrar solamente lo que se este preparado para manejar
        - Nada de capturar `Exception` a secas
    - No dejar execepciones con el bloque `catch` vacío
        - Al menos informar, loguear, ...

```java
catch (RareException e) {
    throw RuntimeException("Esto nunca debe ocurrir ", e);
}
```

- :heavy_check_mark:

### Desasignar los recursos que no se van a utilizar en adelante

```c
char* getBlock(int fd) {
    char* buf = (char*) malloc(BLOCK_SIZE);
    if (!buf) {
        return NULL;
    }
    if (read(fd, buf, BLOCK_SIZE) != BLOCK_SIZE) {
        return NULL;
    }
    return buf;
}
```

- :no_entry_sign:
- **Problema**:
    - En ningun momento se libera el recurso cargado
        - **Resource leak**
    - Esto puede llevar a:
        - Pérdidas de rendimiento
        - Denegacion de servicio
            - El recurso lo necesita más procesos y lo tiene uno permantentemente cogido
- **Solución**:
    - Liberar recursos cuando ya no sean necesarios

## 6. Privacidad y confidencialidad

- Es esencial no dejar datos pesonales en las aplicaciones
- Manejar ese tipo de datos de manera segura y fuera del código
    - **Especialmente contraseñas**

### Mantener las password fuera del código fuente

```java
public class DbUtil {
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection("jdbc:mysql://ixne.com/rxsql", "chan", "0uigoT0");
    }
}
```

- :no_entry_sign:
- **Problema**:
    - Usuario hardcodeado
    - Password hardcodeada
        - Se puede sacar haciendo reversing
        - Problema grave
- **Solución**:
    - Nunca contraseñas en el código
    - Buena **estrategia de gestión de contraseñas**

### Estrategia de gestión de contraseñas

- Cifrar las password con una implementación de algoritmos criptográficos robustos
    - Almacenar la clave para descifrar contraseñas en fichero separado y aislado de los admins
- Contraseñas robustas
    - Contraseñas outbound: largas y aleatorias (generador seguro)

### Número aleatorios

- Dos tipos de generadores de números aleatorios:
    - PRNG **estadístico**
        - Valores uniformes
        - Predecibles
        - **Inseguros para usos criptográficos**
    - PRNG **criptográfico**
        - Robustos
        - Mecanismos de entropia para asegurar en casoso como criptografia o generacion aleatoria

```java
String generateCouponCode(String couponBase) {
    Random ranGen = new Random();
    ranGen.setSeed((new Date()).getTime());
    return(couponBase + Gen.nextInt(400000000));
}
```

- :no_entry_sign:
- **Problema**:
    - Se usa una funcion de generacion de numeros aleatoria insegura
- **Solución**:
    - Usar implementacion segura: `Java.security.SecureRandom`
    - Usar un PRNG criptográfico

## 7. Programas privilegiados

- La mayor parte de los programas se ejecutan con un **conjunto de privilegios heredados del usuario** con el que se ejecutan
- Los programas privilegiados tienen privilegios adicionales para hacer operaciones que si no no podrían hacer
    - Bien programado
        - Limita lo que los usuarios pueden hacer con él
    - Mal programado
        - Deja campo para atacantes para explotar vulnerabilidades para **escalar privilegios**
- Escalada de privilegios horizontal
    - Acceso a los recursos de otro usuario

### Principio de mínimo privilegio

- **Cuantos más privilegios** tiene un programa, **mayor daño potencial** puede causar
- Principio del minimo privilegio
    - Solo privilegos para las tareas y momentos concretos en los que son necesarios
    - Reducir al mínimo la cantidad de daño que pueden causar
- En fucion de cuanto necesiten privilegios: **nivel de privilegio**
    - Programas **normales**
        - Ejemplo: Visual Studio Code
    - Programas **de sistema** que corren con privilegios de root para la duración de su ejecución
        - Ejemplo: Init
    - Programas que necesitan **privilegios** para usar un conjunto fijo de recursos del sistema cuando se ejecutan **al principio**
        - Ejemplo: Apache httpd (para usar puertos < 1024)
    - Programas que requieren **privilegios** de root **intermitentemente** a lo largo de su ejecución
        - Ejemplos: Un demonio de FTP

### Manejo de los privilegios

```c
chroot("/var/ftproot");
if (fgets(filename, sizeof(filename), network) != NULL) {
    if (filename[strlen(filename) - 1] == '\n') {
        filename[strlen(filename) - 1] = '\0';
    }
    localfile = fopen(filename, "r");
    while ((len = fread(buf, 1, sizeof(buf), localfile)) != EOF) {
    (void) fwrite(buf, 1, len, network);
    }
}
```

- :no_entry_sign:
- **Problema**:
    - Se eleva privilegios para ejecutar el `chroot()`
    - no se reducen los privilegrios tras hacerlo
    - El resto de operaciones se hacen como `root`
        - Si se explotara una vulnerabilidad en ese momento 🠒 **owned**
    - Una **jaula chroot tiene sus debilidades**
        - Archivos ya habiertos
        - No cambia el pwd
        - Puede fallar
        - Requiere privilegios
- **Solución**:
    - Reducir los privilegios cuando no sean necesarios
    - Eliminar los privilegios permanentemente si no se van a usar más
    - No usar jaulas chroot para evitar *traversal path*

### Manejo de excepciones en programas privilegiados

- Iportante para programas privilegiados:
    - Importante especialmente con programas privilegiados:
        - **Comprobar cada** condición de **error**
    - **Seguridad sobre robustez**: terminación ante errores
        - No intentar reponerse de errores inesperados
    - **Inhabilitar señales** antes de la elevación de privilegios

### Ataques de escalada de privilegios

- Consisten en:
    - Encontrar una debilidad en un servicio o cuenta mal protegida y obtener acceso de bajo privilegio
    - Usar eso para explotar una vulnerabilidad en un programa privilegiado
    - Tomar el control de la máquina
- **Formas** comunes **de escalar privilegios**:
    - Condiciones de carrera de acceso a archivos
    - Permisos de archivo débiles
    - Archivos temporales inseguros
    - Inyección de comandos
    - Mal uso de descriptores de archivo estándar

#### Ataque de condiciones de carrera en el acceso a ficheros

- **time-of-check**, **time-of-use** (TOCTOU)
- Se aprovechan de los tiempos entre verificacion y acción
- Secuencia
    1. Programa comprueba algo de un archivo
    2. Atacante cambia para que se refiera a otro archivo (symlink)
    3. El programa realiza una operacion sobre el archivo (que el atacante ya ha "trucado")

```c
for (int i=1; i < argc; i++) {
    /* make sure that the user can read the file, then open it */
    if (!access(argv[i], O_RDONLY)) {
        fd = open(argv[i], O_RDONLY);
    }
    print(fd);
}
```

- :no_entry_sign:
- **Problema**:
    - El tiempo que pasa entre el `access()` y el `open()` es > 0 (obvio)
    - Normalmente el tiempo es muy corto, pero hay mecanismos para haltear o ampliar el margen para atacar
- **Solución**:
    - :man_shrugging:

#### Ficheros temporales inseguros

- **Problema**:
- Si se usa siempre un nombre igual para un archivo temporal para hacer mutex
    - Se puede crear ese archivo para hacer un DoS a la aplicación
- **Solución**:
    - Archivos temproales sobre directorio que no es publicamente accesible
    - Archivos temporales con nombres aleatorios (PRNG criptografico)

#### Inyección de comandos

- Consiste en usar la inyeccion de comandos de algun tipo (normalmente shell) para ganar privilegios

#### Descriptores de ficheros

- Descriptores de archivo estándar:
    - `stdin` (FD 0)
    - `stdout` (FD 1)
    - `stderr` (FD 2)
- Son los que usa por defecto el terminal o las funciones de C como `printf()`

```c
fd = open("/etc/passwd", O_RDWR);
/// ...
if (!process_ok(argv[1])) {
    perror(argv[1]);
}
```

```c
int main(int argc, char* argv[]) {
    (void) close(2);
    execl("victim", "victim", "attacker:<pw>:0:1:Super-User-2:...", NULL);
    return 1;
}
```

- :no_entry_sign:
- **Problema**:
    - El programa de arriba usa perror para escribir un error en la salida de errores estandar
        - Lo que escribe es el argumento
    - Si otro programa (el de abajo) ejecuta el primero pero cerrando el FD 2 (el de errores)
    - Cuando el programa de arriba haga open le devolverá el FD 2 (el siguiente libre)
    - Cuando haga el `perror(argv[1])` escribira el argumento
        - Pero no en la salida de errores, sino en `/etc/passwd`
        - El programa atacante aprovecha esto para escribir una entrada en ese archivo que le de accesos con privilegios root
- **Solución**:
    - Asegurarse que los tres primeros descriptores de archivo (0, 1, 2) se abren a archivos seguros conocidos antes del comienzo de su ejecución

    ```c
    int main(int argc, char* argv[]) {
        if (open("/dev/null", O_WRONLY) < 0 ||
            open("/dev/null", O_WRONLY) < 0 ||
            open("/dev/null", O_WRONLY) < 0) {
            exit(-1);
        }
        // ...
    }
    ```
