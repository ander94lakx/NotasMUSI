# Tema 2: Seguridad en el ciclo de vida del software

## 1. Introducción a la seguridad en ciclo de vida del software (S-SDLC)

- Ciclo de vida de desarrollo de software seguro
    - Ciclo de vida de desarrollo de SW que permite:
        - Desarrollo de software mas seguro
- **Elementos**:
    - [Modelado de amenazas](#2-Modelado-de-amenazas)
    - [Casos de abuso](#3-Casos-de-abuso)
    - [Modelado de ataques](#4-Modelado-de-ataques)
    - [Ingeniería requisitos de seguridad](#5-Ingeniería-de-requisitos-de-seguridad)
    - [Análisis de riesgo arquitectónico](#6-Análisis-de-riesgo-arquitectónico)
    - [Patrones de diseño](#7-Patrones-de-diseño)
    - [Pruebas de seguridad basadas en riesgo](#8-Pruebas-de-seguridad-basadas-en-riesgo)
    - [Revisión de código](#9-Revisión-de-código)
    - [Pruebas de penetración](#10-Pruebas-de-penetración)
    - [Operaciones de seguridad](#11-Operaciones-de-seguridad)
    - [Revisión externa](#12-Revisión-externa)

| Práctica de seguridad / Fase SDLC      | 1- Requisitos | 2- Diseño | 3- Codificación | 4- Pruebas | 5- Despliegue | 6- Operación |
|----------------------------------------|:-------------:|:---------:|:---------------:|:----------:|:-------------:|:------------:|
| Modelado de amenazas                   | X             | X         |                 |            |               |              |
| Casos de abuso                         | X             |           |                 |            |               |              |
| Modelado de ataques                    | X             | X         | X               | X          | X             | X            |
| Ingeniería requisitos de seguridad     | X             |           |                 |            |               |              |
| Análisis de riesgo arquitectónico      | X             | X         |                 | X          | X             | X            |
| Patrones de diseño                     |               | X         |                 |            |               |              |
| Pruebas de seguridad basados en riesgo |               | X         | X               | X          | X             | X            |
| Revisión de código                     |               |           | X               |            |               |              |
| Pruebas de penetración                 |               |           |                 |            | X             | X            |
| Operaciones de seguridad               |               |           |                 |            |               | X            |
| Revisión externa                       |               |           | X               | X          |               | X            |

## 2. Modelado de amenazas

- Hay 3 tipos de amenazas y hay que tener en cuenta las tres:
    - Involuntaria
    - Intencional, pero no maliciosa
    - Maliciosa
- Análisis de riesgos:
    - Procedimiento sistemático para estimar la magnitud y probabilidad de los riesgo
- *Modelado de amenazas*:
    - **Proceso de análisis de riesgos aplicado al diseño y desarrollo de SW**
    - *Objetivos*:
        - Identificar potenciales amenazas
        - Proporcionar información sobre cuales serías las contramedidas para mitigarlas
    - **Metodología** de modelado de amenazas con **4 fases**:
        1. *Modelado*
            - **DFD** (Diagrama de flujo de datos): Entidades externas, procesos, almacenes de datos, flujos de trabajo, ...
        2. *Identificación de amenazas*
            - **STRIDE** para identificar las amenazas
                *Spoofing* 🠒 Autenticación
                *Tampering* 🠒 Integridad
                *Repudiation* 🠒 No repudio
                *Infromation disclosure* 🠒 Confidencialidad
                *DoS* 🠒 Disponibilidad
                *Elevation o privilege* 🠒 Autorización
            - **DREAD** para valorar las amenazas
                - *Damage* 🠒 ¿cuál es el daño que puede originar la vulnerabilidad si llega a ser explotada?
                - *Reproducibility* 🠒 ¿es fácil reproducir las condiciones que propicien el ataque?
                - *Exploitability* 🠒 ¿es sencillo llevar a cabo el ataque?
                - *Affected* 🠒 ¿cuántos usuarios se verían afectados?
                - *Discoverability* 🠒 ¿es fácil encontrar la vulnerabilidad?
                - Riesgo = Probabilidad 𝑥 Impacto potencial = (𝑅 + 𝐸 + 𝐷𝐼) 𝑥 (𝐷 + 𝐴) = 𝑃 𝑥 𝐼𝑃
        3. *Mitigación*
        4. *Valoración*

## 3. Casos de abuso

- *Caso de abuso*:
    - Lo **inverso a un caso de uso**
        - **Funcionalidad que el sistema no debe permitir**
            - Secuencia completa de acciones que resulta en una pérdida para la organización
- Son un excelente **medio de análisis de amenazas**
- Consiste en **pensar la forma en la que una funcionalidad puede ser explotada**
- Casos de abuso 🠒 **Casos de uso de seguridad**
    - Con los casos de abuso se ven las amenazas
    - Con los casos de uso de seguridad se ven los requisitos de seguridad

## 4. Modelado de ataques

- Dos perspectivas
Defensor
Atacante
- Formas de modelar la perspectiva del atacante
    - **Patrones de ataque**
    - **Árboles de ataque**

### Patrones de ataque

- Ataque:
    Aprovecha una vulnerabilidad de una aplicación mediante un exploit
- **Patrones de ataque**:
    - **Mecanismo para representar** en detalle **la perspectiva del ciberatacante** acerca de cómo los ataques se llevan a cabo los ataques
        - Métodos más frecuentes de explotación (exploit)
        - Técnicas usadas para comprometer el software
- Proporciona valor en todas las fases del desarrollo
    - Especificar requisitos 🠒 para ver a que se enfrenta
    - Diseño 🠒 para que el diseño sea seguro
    - Programación 🠒 eliminar vulnerabilidades del código
    - Pruebas 🠒 Elaborar pruebas contra esos patrones
    - Despliegue 🠒 elegir que políticas de seguridad implementar
- Un catálogo de patrones de ataques:
    - **CAPEC** (*Common Attack Pattern Enumeration and Classification*) **del MITRE**
        - Contiene muchísima información de cada patrón:
            - Severidad, requisitos, posibles explotaciones, recursos necesarios, ejemplos, soluciones, ...

### Patrones de ataque

- Árboles de ataque:
    - **Método sistemático para caracterizar la seguridad** de un sistema
- El objetivo del atacante se coloca en la parte superior
    - Posibles alternativas de ataque en las ramas del árbol
        - En las hojas 🠒 diferentes métodos de ataque
- El recorrido en árbol permite identificar **todas las posibles técnicas** que podrían ser utilizados para comprometer la seguridad del sistema
- Se enfoca en las **causas** del problema
- **Representación**
    Sencilla de seguir
        - **Textual**
        - **Gráfica**
    - Conexión AND
        - Son la combinación de eventos necesarias para alcanzar ese punto
    - Conexión OR
        - Son diferentes formas de llegar al mismo lugar
    - *Ejemplo*:

        ```text
        Objetivo: Falsificar una Reserva de vuelos
            1. Convencer al empleado de agregar una reserva falsa
                1.1 Chantaje empleado
                1.2 Amenazar empleado
            2. Acceder y modificar la base de datos de vuelos
                2.1 Realizar una inyección SQL en la página Web
                2.2 Iniciar una sesión en la base de datos
                    2.2.1 Adivinar la contraseña
                    2.2.2 Obtener la contraseña rastreando la red (sniff)
                    2.2.3 Robar la contraseña del servidor
                        2.2.3.1 Obtener una cuenta del servidor (AND)
                            2.2.3.1.1 Desbordamiento de buffer
                            2.2.3.1.2 Obtener acceso cuenta empleado
                        2.2.3.2 Explotar condición de carrera acceso perfil protegido
        ```

## 5. Ingeniería de requisitos de seguridad

- Gran parte de las vulnerabilidades y debilidades del software tienen su origen en unos requisitos inadecuados, inexactos e incompletos
- Consiste en **integrar los requisitos de seguridad en la ingeniería de requisitos**
- No confundir:
    - Requisitos **servicios de seguridad** (funcionales o positivos)
        - **Funciones que implementan políticas de seguridad**
            - **Ejemplos**: control de acceso, autorización, cifrado, gestión de claves
        - Requisitos de **software seguro** (no funcionales o negativos)
            - Requisitos que afectan directamente a la **probabilidad de que el software sea seguro**
                - Completos
                - Precisos
                - Coherentes
                - Trazables
                - Verificables
- Es necesario definir también estos requisitos al inicio del SDLC (fase de requisitos)
- Herramientas:
    1. Identificación de amenazas (DFD)
    2. Modelado de amenazas
    3. Identificar casos de abuso
    4. Desarrollar patrones de ataque (CAPEC)
    5. Usar los patrones de ataque para desarrollar los casos de abuso
    6. Desarrollar los requisitos de seguridad
        - Funcionales
            - En base a las salvaguardas
        - No funcionales
            - En base a los patrones de ataque y casos de abuso

## 6. Análisis de riesgo arquitectónico

- Aplicar el **procedimiento de análisis y gestión de riesgos** para **identificar** las salvaguardas, mecanismos y técnicas concretas a implementar
- Elementos fundamentales:
    - **Determinar los límites** del sistema y datos sensibles y críticos
    - **Identificar las amenazas** y las fuentes relevantes de ataque
    - **Identificar vulnerabilidades** posibles
    - Discutir las **posibles modificaciones**
    - Determinar la **probabilidad de riesgo**
    - **Clasificar los riesgos**
    - Desarrollar una **estrategia de mitigación**
    - **Recomendar las salvaguardas** para mitigar los riesgos
- **Proceso de análisis** de riesgo arquitectónico
    - **Análisis de resistencia** al ataque
        - Modelos como STRIDE
    - **Análisis de ambigüedad**
        - Crear una **técnica de análisis crítica para encontrar nuevos defectos**, puntos de conflicto y de inconsistencia
    - **Análisis de debilidad**
        - Impacto de dependencias del software externo

## 7. Patrones de diseño

- *Patrón de diseño*:
    - Una solución general repetible a un problema de **ingeniería de software**
- *Patrón de diseño **de seguridad***:
    - Una solución general repetible a un problema de **seguridad del software**

## 8. Pruebas de seguridad basadas en riesgo

- No son pruebas basadas en la funcionalidad del código, sino para:
    - **Determinar cómo se comportará en condiciones anómalas y hostiles**
    - **Comprobar si está libre de vulnerabilidades**
- **Técnicas**:
    - **Caja blanca**
        - Revisión de Diseño
        - Análisis estático de código
        - Inyección de fallos en el código fuente
    - **Caja negra**
        - Pruebas de penetración
        - Análisis dinámico
        - Fuzzing testing
        - Análisis de código binario
        - Inyección de fallos en binarios
        - Escaneo de vulnerabilidades
    - **Caja gris**
        - Análisis híbrido
- Según el tipo de prueba, irá en una fase u otra del SDLC

|                                         | Arquitectura y Diseño | Codificación | Pruebas | Operación y Producción |
|-----------------------------------------|:---------------------:|:------------:|:-------:|:----------------------:|
| Revisión de Diseño                      | X                     |              |         |                        |
| Análisis estático de código             |                       | X            |         |                        |
| Inyección de fallos en el código fuente |                       | X            | X       |                        |
| Fuzzing testing                         |                       | X            | X       |                        |
| Análisis híbrido                        |                       |              | X       |                        |
| Análisis de código binario              |                       |              | X       |                        |
| Inyección de fallos en binarios         |                       |              | X       |                        |
| Análisis dinámico                       |                       |              | X       | X                      |
| Escaneo de vulnerabilidades             |                       |              | X       | X                      |
| Pruebas de penetración                  |                       |              | X       | X                      |

### Caja blanca

- *Ventajas*
    - Análisis con conocimiento completo
    - Es eficaz para hallar errores de programación
    - Permite una corrección temprana
- *Desventajas*
    - Da muchos falsos positivos
    - No detecta todo tipo de vulnerabilidades
- **Revisión de Diseño**
    - Son la categoría más difícil de manejar
    - Ejemplos de problemas: uso de canales de datos sin protección, mecanismos de control de acceso incorrectos, carencia de auditorías, ...
- **Análisis estático de código**
    - Una de las prácticas más importantes y útiles
- **Inyección de fallos en el código fuente**
    - Forma de análisis dinámico que permite ver como reacciona el SW en situaciones anómalas
    - Es compleja de realizar

### Caja negra

- *Ventajas*
    - Permite hacer pruebas desde la perspectiva de un atacante
    - No hay que entrar en elo código fuente
- *Desventajas*
    - Hay fallos en el código que son mas difíciles de detectar
    - Requiere desplegar y ejecutar la aplicación
- **Pruebas de penetración**
    - Es un conjunto de pruebas que engloban a otras como escanear vulnerabilidades, fuzz testing, análisis dinámico (DAST) de aplicaciones web
    - Consiste buscar y explotar vulnerabilidades en entornos controlados
- **Análisis dinámico (DAST)**
    - Se usan en aplicaciones web mientras se ejecutan
    - Permiten detectar vulnerabilidades comunes (SQLi, command injection, path traversal, ...)
    - Dos fases
        1. Fase de rastreo
        2. Fase de pruebas manipulando cada petición
    - *Ejemplos de herramientas*: BurpSuite, OWASP ZAP
- **Fuzzing testing**
    - Introducción de datos no válidos en las diferentes entradas de una aplicación
    - Permite detectar fallos a la hora de tratar las entradas
        Este tipo de fallos son tan comunes como peligrosos
    - *Ejemplos de herramientas*: Mangle, Wfuzz, Spike
- **Análisis de código binario**
    - Se usan decompiladores, desensambladores para analizar el código maquina en búsqueda de fallos
    - *Ejemplos de herramientas*: IDA PRO, WinDbg
- **Inyección de fallos en binarios**
    - Permite simular fallos ante situaciones anómalas en binarios en ejecución
- **Escaneo de vulnerabilidades**
    - Permite automatizar las búsquedaa de vulnerabilidades conocidas en los sistemas
    - *Ejemplos de herramientas*: Nessus, OpenVAS, Nmap

### Caja gris

- Es una mezcla de caja blanca y caja negra
- **Análisis híbrido (IAST)** (*Interactive Application Security Testing*)
    - Usar el código fuente, modificarlo con un agente, compilarlo y hacer pruebas dinámicas
    - Tres tipos de análisis:
        - Análisis de cobertura
        - Análisis de frecuencia de espectro
        - Análisis de patrones
    - *Ejemplos de herramientas*: Valgrind, INSURE

## 9. Revisión de código

- El análisis estático de código fuente es la **actividad más importante de entre las mejores prácticas de seguridad**
- Es muy eficaz para encontrar errores durante del desarrollo
- Principal **problema**: **falsos positivos**
    - Aunque **mucho peor** es un **falso negativo**

### Herramientas de análisis estático de código

- Dos tipos de herramientas de análisis estático:
    - Herramientas para *descubrir bugs*
    - Herramientas para **descubrir fallos de seguridad**
- Este tipo de herramientas requieren repaso humano
- **Componentes**:
    - **Analizador léxico**
        - Primera fase
    - **Analizador sintáctico**
        - Convierte la entrada del analizador léxico en un árbol
    - **Analizador semántico**
        - Utiliza el arbo para comprobar restricciones y limitaciones
    - Estructuras de datos (tablas de símbolos y de tipos) para poder ubicarlos
- *Tipos de análisis*:
    - **Análisis estructural**: comprueba la estructura y typechecking
    - **Análisis de flujo de control**: exploración de los diferentes caminos de ejecución e las funciones
    - **Análisis de flujo de datos**: examinan los caminos de movimiento de datos a través de un programa
    - **Taint Propagation**: análisis de flujo de datos para determinar qué es lo que un atacante puede controlar desde las diversas entradas a la aplicación
    - **Pointer Aliasing**: Detecta punteros que apuntan sobre las mismas direcciones de memoria
    - **Análisis local**: Analiza una función individualmente en búsqueda de código inalcanzable
    - **Análisis global**: hace comprobaciones de las interacciones entre las funciones
    - **Interpretación abstracta**
    - **Transformadores de predicados**
    - **Model checking**: Busca patrones comunes para ver si están o si faltan y son necesarios (asignar/liberar memoria, ...)
    - **SAT Solvers**: evalúa expresiones en búsqueda de alguna combinación de valores que hagan la expresión TRUE
- *Ejemplos de herramientas*: FindBugs, SCA Fortify, Cppcheck

## 10. Pruebas de penetración

- **Pruebas** para **comprobar**
    - La **seguridad del software**
    - La **eficacia de las salvaguardas**
- Engloban **todo un conjunto de técnicas y herramientas**
    - Herramientas de recolección de información
    - Escáneres de vulnerabilidades
    - Herramientas de explotación automáticas
    - Fuzz testing
    - Herramientas de análisis dinámico (DAST)
- El **plan de pruebas de penetración** debe capturar:
    - La **política de seguridad** del sistema se supone que debe respetar
    - **Amenazas previstas**
    - **Riesgos de seguridad** (conducido por casos de abuso, riesgos arquitectónicos y modelos de ataque)
    - Secuencias de **ataques probables** que se puedan producir
- *Consideraciones*:
    - Se realizan en las **últimas fases** del SDLC (despliegue y operación)
        - Como se aplican "al final", no se puede depender únicamente de este tipo de herramientas
            - Detectarían los errores tarde en el desarrollo
    - Son pruebas de **caja negra**
    - Tienen que **verficar los aspectos negativos**
    - Nunca garantizan que no haya ninguna vulnerabilidad
    - Suelen ser requisitos para el proceso de aceptación final

## 11. Operaciones de seguridad

- Las fases finales del SDLC requieren una serie de operaciones de distribución y despliegue
    - También hay aspectos de seguridad a tener en cuenta en estas fases
- **Distribución**:
    - *Objetivo*: **Reducir** al mínimo las **posibilidades de acceso y manipulación del software** durante la **transmisión** de un proveedor a su consumidor
    - *Buenas prácticas*:
        - **Cambio de los valores de configuración** predeterminados
        - Utilizar mecanismos de **distribución estándar**
        - **Configuración por defecto segura y lo más restrictiva** posible
        - Guía de configuración de seguridad
        - Herramienta de **instalación automática**
        - Establecer un medio de autenticación para la instalación y configuración
        - Interfaces y **scripts de configuración/instalación seguros**
- **Despliegue**
    - **Objetivo**: realizar una **configuración cuidadosa del entorno** donde se va a desplegar el software
    - Hay que *tener en cuenta*
        - Nivel de **red**
        - Nivel del **sistema operativo** y de otros programas usados, como **SGBD**
        - La **configuración** del la aplicación y del sistema
    - Todo ello es lo que se conoce como **Hardening**
        - Hay muchas guías y estándares para ello (NIST, CCN, ...)
- **Operaciones**
    - También hay que tener en cuenta los aspectos de seguridad mencionados para las operaciones de mantenimiento y respuesta de incidentes

## 12. Revisión externa

- Es bastante **eficaz** y fundamental **aportando otra visión** de la seguridad del sistema y del riesgo
    - Contribuye a una **mejora de la seguridad**
- Es **recomendable** tanto en **etapas de codificación como al final**
    En el primer caso, realizar **detecciones tempranas** de aspectos importantes de seguridad
