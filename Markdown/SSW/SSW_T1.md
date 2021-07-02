# Tema 1: El problema de la seguridad en el software

## 1. El problema de la seguridad en el software

- Las aplicaciones presentan defectos, debilidades de diseño o configuraciones inseguras
- Principales causas:
    - Tamaño excesivo y complejidad
    - Mezcla de código proveniente de varios orígenes
    - Integración de los componentes del software defectuosa
    - Debilidades y fallos en la especificación de requisitos y diseño
    - componentes que contienen vulnerabilidades o código malicioso embebido
    - Falta de herramientas y un entorno de pruebas adecuados
    - Cambios de requisitos
    - Mezcla de equipos de desarrolladores
    - Falta de conocimiento de prácticas de programación segura

## 2. Vulnerabilidades y su clasificación

- *Vulnerabilidad*: **fallo de**
    - **Implementación**: al programarlo
    - **Configuración**: al instalarlo o desplegarlo
    - **Diseño**
- *Factores* de una vulnerabilidad (INTECO):
    - Producto
    - Dónde
    - Causa y consecuencia
    - Impacto
    - Vector

### Ciclo de vida de una vulnerabilidad

1. **Descubrimiento**
    - Detección de un fallo en el software (producido en desarrollo o en producción)
2. **Utilización**
    - Los agentes maliciosos desarrollan el exploit adecuado para poder lanzar ataques
3. **Verificación inicial** de la vulnerabilidad
    - Comprobar que esa vulnerabilidad existe y es replicable
4. **Solución**
    - Para mitigar el problema
5. **Difusión**
    - Los medios de comunicación dan publicidad al incidente
6. **Medidas**
    - Los afectados toman medidas para mitigar (si es posible)
7. **Corrección** y nueva verificación
    - Se arregla el origen del problema
8. **Búsqueda**
    - Se buscan vulnerabilidades similares
9. **Actualización**
    - Los sitios no actualizados vuelven a ser víctimas.

### Gestión de vulnerabilidades

- Hay muchos tipos de vulnerabilidades
- Existen **estándares** para clasificarlas, como:
    - **CVE** (*Common Vulnerabilities and Exposures*)
        - Administrado por el MITRE
        - Normaliza la descripción de vulnerabilidades
        - Código único: `CVE-AAAA-XXXX` (Año y ID único)
    - **CVSS** (*Common Vulnerability Scoring System*)
        - Sirve para **escalonar la severidad** de una vulnerabilidad en base a:
            - Explotabilidad e Impacto
    - **CWE** (*Common Weakness Enumeration*)
        - Conjunto unificado de vulnerabilidades y defectos de software medibles
    - **CVRF** (*Common Vulnerability Reporting Framework*)
        - Esquema XML
        - Compartir información crítica sobre vulnerabilidades
    - **NVD** (*National Vulnerability Database*)
        - Base de datos del gobierno estadounidense

### Clasificación de vulnerabilidades

- Hay Rankins para clasificar vulnerabilidades, como:
    - [**MITRE Top 25**](http://cwe.mitre.org/top25/)
        - Cualquier tipo de SW
        - Ayuda a conocer las vulnerabilidades más graves que puede tener un SW
        - Prevenir, mitigar y principios de programación segura
    - [**OWASP Top 10**](https://owasp.org/www-project-top-ten/)
        - Vulnerabilidades web
        - Ordenada por criticidad
        - Consejos para mitigarlas o eliminarlas
    - [**WASC Threat Classification v2.0**](http://www.webappsec.org/projects/threat/)
        - Vulnerabilidades web
        - Amenazas, debilidades y ataques

## 3. Propiedades software seguro

### Esenciales

- **Confidencialidad**
    - Software y datos ocultos a usuarios no autorizados
    - Cifrado, técnicas de ocultación, ...
- **Integridad**
    - Que el código y los activos que manejan no se altere de manera indebida
    - Tanto en desarrollo como en operación
    - Firmas, monitorización
- **Disponibilidad**
    - Que el software es accesible a quienes lo requieran
    - Alta disponibilidad, sistemas distribuidos, ...

### Complementarias

- **Fiabilidad**
    - Que el software funcione de la manera esperada en todas las situaciones
    - Testeo de SW, control de I/O, interfaces
- **Autenticación**
    - Que el SW pueda garantizar que alguien (proceso, persona, ...) es quien dice ser
- **Trazabilidad**
    - Que se puedan imputar acciones a un usuario sobre un SW
- **Robustez**
    - Capacidad para resistir los ataques
- **Resiliencia**
    - Capacidad para recuperarse ante ataques y mitigar daños
- **Tolerancia**
    - Capacidad para tolerar errores

### ¿Cómo lograr esas propiedades?

- Aspectos a tener en cuenta:
    - Principios de diseño y buenas prácticas de desarrollo
    - Herramientas de desarrollo
    - Evaluar los componentes adquiridos
    - Configuraciones desplegadas
    - Ambiente de operación
    - Conocimiento Profesional

## 4. Principios de diseño seguridad del software

| Principio                                                        | Objetivo                                                                                                                                  |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Defensa en profundidad                                           | Varias capas de seguridad para reducir la probabilidad de comprometer el sistema                                                          |
| Simplicidad del diseño                                           | Reducir la complejidad del diseño para minimizar el número de vulnerabilidades explotables                                                |
| Mínimo privilegio                                                | Dar en todo momento el conjunto mínimo de privilegios para poder funcionar para minimizar riesgo de explotación                           |
| Separación de privilegios                                        | Asignación a las diferentes entidades de un rol que implique el acceso a un subconjunto de funciones o tareas y a los datos necesarios    |
| Separación de dominios                                           | Minimizar la probabilidad de que los atacantes obtengan fácilmente acceso a otros recursos como ubicaciones de memoria u objetos de datos |
| Separación código, ejecutables y datos configuración y programa  | Reducir la probabilidad de que un ciberatacante que haya accedido a los datos pueda acceder al código y a la configuración                |
| Entorno de producción o ejecución inseguro                       | Evitar vulnerabilidades aplicando una serie de principios de validación de las entradas                                                   |
| Registro de eventos de seguridad                                 | Generar logs de seguridad para garantizar que las acciones realizadas por un ciberatacante se observan y registran                        |
| Fallar de forma segura                                           | Reducir la posibilidad de explotar vulnerabilidades si el programa falla                                                                  |
| Diseño de software resistente                                    | Reducir al mínimo el tiempo que un software vulnerable es incapaz de protegerse de los ataques                                            |
| La seguridad por oscuridad: error                                | Concienciarse de que la seguridad por oscuridad no proporciona un mecanismo de defensa real                                               |
| Seguridad por defecto                                            | Reducir la superficie de ataque de una aplicación o sistema                                                                               |

### Defensa en profundidad

- Establecer **varias capas de seguridad** para reducir la probabilidad de comprometer el sistema
    - **Si falla una** (o varias), **se tiene el resto**
- Muy común en redes
    - Establecer medidas de seguridad en las diferentes capas
        - Ejemplo: Cifrado en aplicación + WAF + TLS + IPSec
- Muchísimas técnicas para logra esto
    - S-SDLC, Cifrados, FW, WAF, SIEM, segmentación de redes, ....
    - Varían en función del tipo de SW a desarrollar

### Simplicidad diseño

- Cuanto más sencillo es el diseño es **más difícil cagarla**
- KISS (*Keep It Simple, Stupid*)
- *Formas*
    - Limitar numero de estados del SW
    - Procesos deterministas
    - Evitar funcionalidad innecesaria
    - Minimizar tareas
    - Desacoplamiento
    - Facilidad de uso
    - ...

### Mínimo privilegio

- Conceder a cada entidad (usuario, proceso, dispositivo) el **conjunto más restrictivo de privilegios**
    - Si después necesita más se le puede dar
    - Cuando los deje de necesitar, se le quitan
- **Minimiza el daño** que se puede hacer si se explota una vulnerabilidad

### Separación privilegios

- Separar los privilegios para **dar a cada** usuario/proceso **lo que necesita**
    - Acceder a las funciones del sistema que necesita
    - Acceder a los datos que necesita
- Es otra forma del principio de mínimo privilegio:
    - Minimiza los daños
- *Ejemplo*: servidor web (usuario solo necesita leer, admin necesita más cosas)

### Separación dominios

- Es otra forma del principio de mínimo privilegio
    - Cada parte a sus tareas especificas
- Minimizar la probabilidad de que los atacantes obtengan fácilmente acceso a otros recursos como ubicaciones de memoria u objetos de datos
- *Técnicas* de aislamiento variadas:
    - VM
    - Sandboxing
    - Jaulas chroot
    - TMP (Win11 :))

### Separación de código, ejecutables y datos de configuración y programa

- **Reducir** la probabilidad de que un **ciberatacante que haya accedido a los datos pueda acceder al código y a la configuración**
    - **Permisos** de escritura y lectura **de los datos** de programa **únicamente para el programa**
    - **Datos de configuración** del programa **solo** accesibles por el **administrador**
    - Almacenar los archivos de datos, configuración y programas ejecutables en los **directorios separados** del sistema de archivos
    - **Cifrar** todos los archivos **ejecutables**
    - **Cifrado de archivos** y firma digital

### Entorno ejecución inseguro

- Hay que **asumir que** todos los componentes del **entorno de producción son inseguros**
- Hya que evaluar la seguridad de los sistemas donde se va a ejecutar el SW
- También hay que evaluar que el SW sea resistente
    - Identificar fuentes de datos externas y evaluar la seguridad:
        - Llamadas al sistema
        - Llamadas a otros programas, middlewares, APIs ...
        - Flujo de datos apps cliente-servidor
    - Esto puede dar a muchos ataques que pueden explotar estas vulnerabilidades, como:
        - Buffer overflows, inyección de comandos, revelación de información ([ver más](https://github.com/ander94lakx/NotasMUSI/blob/master/Markdown/SSW/SSW_T3.md))

### Registro de eventos de seguridad

- Generar eventos (logs) de seguridad
    - **Garantizar que las acciones** realizadas por un **ciberatacante** se observan y **registran**
- Hay que tratar con seguridad estos logs
    - Pueden ser una fuente de información explotable si no se protegen

### Fallar de forma segura

- **Reducir la posibilidad de explotar vulnerabilidades si el programa falla**
- *Mecanismos*:
    - Control de excepciones
    - *Watchdogs*
    - Asegurarse de comenzar y terminar en un estado seguro
    - Evitar problemas de sincronización

### Diseño SW resistente

- **Reducir** al mínimo el **tiempo que un software** vulnerable **es incapaz de protegerse** de los ataques
- *Mecanismos*
    - Limitación de recursos y privilegios
    - Monitorización
    - Detección de estados anómalos
    - Técnicas de recuperación

### Seguridad por oscuridad: error

- **No usar mecanismos de seguridad por ofuscación**
    - Consisten en ocultar información para que sea difícil de obtener. Ejemplos:
        - Guardar información en binarios
        - Contraseñas en código fuente
        - Carpetas ocultas
        - Cambios de valores por defecto para ocultar info (puertos, nombres de usuario, ...)
- Estos mecanismos **solo retrasan lo inevitable**

### Seguridad por defecto

- Diseñar sistemas con:
    - Mínima funcionalidad requerida
    - Mínimos privilegios posibles
    - Desactivar todo lo necesario
    - Lo más simple posible
- Para poder minimizar la superficie de ataque a un sistema

## 5. Tipos de S-SDLC

- S-SDLC: *Secure Software Development Life Cycle*
    - Son SDLC pero con añadidos para buenas practicas de seguridad
        - (SDLC: proceso cíclico para planificar, diseñar, implementar y desplegar un SW)
- **Mejoran la capacidad para detectar y eliminar errores de diseño**
- *Elementos clave*:
    - **Hitos** de control
    - **Principios de desarrollo de software seguros**
    - **Requisitos** adecuados
    - **Arquitectura y diseño** adecuados
    - **Codificación** segura
    - **Integración** de forma segura de los módulos y componentes del software
    - **Pruebas** de seguridad
    - **Despliegue** y distribución segura

### McGraw’s Seven Touchpoints

- Una serie de **mejores prácticas de seguridad** a aplicar a los artefactos **de cada fase**
    1. **Revisión de código**
    2. Análisis de riesgo arquitectónico
    3. **Pruebas de penetración**
    4. Pruebas de seguridad basados en riesgo
    5. **Casos de abuso**
    6. Requisitos de seguridad
    7. Operaciones de seguridad
    8. Revisión externa
- Cada punto se puede aplicar en diferentes fases del S-SDLC
- Hay muchas metodologías más:
    - Microsoft Trustworthy Computing SDL
    - Team Software Process (TSP):
    - Oracle Software Security Assurance
    - ...

## 6. Metodologías y estándares

- Hay que implantar un
    - **Estándar de calidad de software**
        - Que funcione correctamente conforme a las especificaciones
    - **Estándar de seguridad**
        - Que tenga el mínimo de vulnerabilidades y sea lo mas confiable posible
- Hay muchas organizaciones que elaboran metodologías para ello: ISO, IEC, NIST
- Estándares
    - De calidad:
        - ISO/IEC JTC1 SC7: Ingeniería de software y de sistemas
        - ISO 9126: Calidad del producto
        - ISO 14598: Evaluación de productos de software
    - De seguridad
        - SSE-CMM (ISO/IEC 21827) (*System Security Engineering Capability Maturity Model*)
        - ISO/IEC 27034-1 (*Information technology — Security techniques — Application security*)
        - ISO/IEC 15408 (*Evaluation Criteria for IT Security. The Common Criteria*)
