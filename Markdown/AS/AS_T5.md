# Tema 5: Auditorías de cumplimiento y metodologías de auditoría

## 1. Auditorías de cumplimiento

### Auditoría de protección de datos :red_circle:

- *Objetivo*:
    - Comprobar y adecuar el **nivel de seguridad de los datos personales**
    - **Adecuarse a la legislación** vigente (RGPD, LOPDGDD)
- Son **obligatorias para** organizaciones que traten **datos personales**:
    - Tratamiento **masivo**
    - Tratamiento de **categorías especiales**
- EL RGPD distingue **dos partes** de la auditoría:
    - **Auditoría de seguridad** (verificar el análisis de riesgos y controles)
        - Seguridad y violaciones de seguridad
        - EIPD
        - Protección de datos desde el diseño
        - Seguridad del procesamiento
    - **Auditoría de cumplimiento**
        - Principios
        - Derechos del interesado
        - Perfiles
        - Responsable del tratamiento
        - Delegado de protección de datos (DPD)
        - Transferencias de datos a terceros países u organizaciones internacionales
- **Fases** de una auditoría de PD:
    1. **Inicio y planificación**
    2. **Auditoría** de PD
        - Auditoría de **seguridad**
        - Auditoría de **cumplimiento**
    3. **Conclusiones, resultados e informe** de auditoría

### Auditoría del Esquema Nacional de Seguridad (ENS)

- ENS
    - Principios básicos y requisitos mínimos medidas de protección que implantar
    - Para los SGSI de las AAPP
- La **auditoría del ENS** (anexo III). **Guías**:
    - **CCN-STIC 802**
        - Guía de **auditoría**
        - Pasos:
            1. Planificación preliminar
                - Objetivo, alcance, solicitar información
            2. Programa de auditoría
                - Tipos de pruebas y plan
            3. Revisión y pruebas
                - Revisión de documentación
                - Entrevistas
                - Pruebas
            4. Conclusiones
                - Informe
                - Grado de cumplimiento
    - **CCN-STIC 808**
        - Guía de **verificación** del cumplimiento de las medidas del ENS
- *Objetivos*:
    - **Dar cumplimiento al RD** 3/2010 (ENS) y verificar el cumplimiento de los requisitos establecidos
    - Emitir una **opinión independiente** y objetiva **del cumplimiento** del ENS
    - Posibilitar la **obtención de la Certificación** de Conformidad
    - Sustentar la **confianza** que merece el sistema auditado sobre el nivel de seguridad implantado
    - Calibrar la **capacidad** del sistema **para garantizar la CIDAT**

### Auditoría de PCI-DSS

- PCI DSS
    - **Normas de seguridad** de datos de la industria de **tarjetas de pago**
    - De **obligado cumplimiento** para comerciantes, entidades emisoras, procesadores, pasarelas de pago, etc.
- Datos a proteger
    - **Datos del titular** de la tarjeta (CHD)
        - Numero de cuenta, nombre, fecha de caducidad, ...
    - Datos confidenciales **de autenticación** (SAD)
        - Contenido del chip, CCV, PIN, ...
- **Requisitos a auditar**
    - Desarrollar y mantener **redes y sistemas seguros**
    - **Protección de los dato**s del titular (cifrado, almacenamiento)
    - Programa de administración de **vulnerabilidades**
    - Medidas solidas de **control de acceso seguro**
    - **Supervisión de las redes**
    - Implementación de una **política de seguridad**
    - **Si no se puede** cumplir con algún criterio:
        - **Controles de compensación**
- **Proceso de auditoría**
    1. Alcance de evaluación
    2. Auditoría del entorno (los requisitos)
    3. Informe de evaluación
        - Cuestionario de autoevaluación (SAQ)
        - Informe sobre cumplimiento (ROC)
    4. Informes de cumplimento
        - Atestación de cumplimiento (AOC)
    5. Presentación de resultados
- Auditoría 🠒 certificación:

### Auditoría de certificación del SGSI :red_circle:

- *Objetivo*
    - Verificar la implantación del SGSI de acuerdo a una norma concreta, como por ejemplo la ISO 27001 certificación
- *Ventajas* de certificarse:
    - Para los sistemas de Información
        - Sistematizar las actividades
        - Clasificar los activos de información
        - Analizar riesgos
        - Establecer objetivos de seguridad
        - Diseñar y establecer controles
        - Establecer planes de continuidad
        - Mejora continua
    - Para el negocio
        - Integrar la gestión de la seguridad en el marco empresarial
        - Mejorar la imagen
        - Compromiso con el cumplimiento legal
- **Antes** de realizar una auditoría de certificación (externa) 🠒 **auditoría interna**
    - Según la ISO 27001, objetivos de auditoría interna:
        - Verificar los requisitos de la empresa
        - Verificar los requisitos de la norma (114 controles)
    - Considerar:
        - Tiempo (muchos controles)
        - Responsabilidades
        - Preparación
        - Departamentos
        - Hallazgos
        - Correcciones
- **Fases**
    - Auditoría interna
        1. Planificación de la auditoría
        2. Auditoría **interna**
            - Auditoría **documentación**
            - Auditoría de **eficiencia de controles**
        3. Conclusiones, resultado e informe
    - Auditoría de certificación (AENOR)
        1. Cuestionario preliminar
        2. Auditoría **FASE 1** (no presencial)
            - Estudio de la **documentación**
            - Informe preliminar
        3. Auditoría **FASE 2** (presencial)
            - Realización de la auditoría
        4. **PAC** (Plan de Acciones correctivas)
            - Se evalúa
        5. **Obtener certificación**
- Hay muchas herramientas SW que ayudan (ISOTools, SandaSGRC, ...)

## 2. Metodologías de auditorías de seguridad

- **Metodología**:
    - Conjunto de procedimientos documentados diseñados para alcanzar los objetivos
    - *Beneficios*
        - **Estandarizar el proceso** de auditoría
            - Más **sencillo**
            - Orden **adecuado** para realizar pruebas
            - Mayor organización
            - Mejores resultados
    - Permite que las pruebas sean:
        - **Cuantificables**
        - **Consistentes y repetibles**
        - **Válidas** más allá del periodo actual
        - Exhaustivas
        - Coherentes
- Ejemplos de metodologías de auditorías *técnicas*
    - **ISSAF** (*Information System Security Assessment Framework*)
    - **OSSTMM** (*Open Source Security Testing Methodology Manual*)
    - **PTES** (*Penetration Testing Execution Standard*)
    - **NIST 800-115** (*Technical Guide to Information Security Testing and Assessment*)
    - **OWASP** (*Open Web Application Security Project*)
    - **OWISAM** (*Open Wireless Security Assessment Methodology*)
    - **OASAM** (*Open Android Security Assessment Methodology*)
    - **CC** (*Common Criteria ISO 15408*)

### ISSAF (*Information System Security Assessment Framework*)

- Metodología estructurada de análisis de seguridad PTF (*Penetration Testing Framework*)
- *Fases*
    1. **Planeación** y preparación
    2. **Evaluación**:
        - **Recolección de información**
        - **Mapeo** de red
        - **Identificación** de **vulnerabilidades**
        - Penetración
        - Ganar **acceso y escalar** privilegios
        - **Comprometer** usuarios y sitios remotos
        - **Mantener** el acceso
        - **Borrar** las huellas
    3. **Presentación** de informes, limpieza y destrucción de artefactos:
        - Presentación de **informes**
        - **Limpieza** y destrucción de artefactos

### OSSTMM (*Open Source Security Testing Methodology Manual*)

- Uno de los estándares más completos para auditorías de aplicaciones
- Incluye **reglas** para saber **cuándo y qué elementos son testeados**
- *Secciones*:
    - Sección A: Seguridad de la **información**
    - Sección B: Seguridad de los **procesos**
    - Sección C: Seguridad en las tecnologías de **Internet**
    - Sección D: Seguridad en las **comunicaciones**
    - Sección E: Seguridad **inalámbrica**
    - Sección F: Seguridad **física**
- Las pruebas son:
    - Prácticas y eficientes
    - Cuantificables
    - Repetibles
    - Validas a un futuro
    - Basadas en el mérito del testeador, no en marcas
    - Exhaustivas
    - Acordes a las legislaciones
- *Tipos de pruebas*:
    - Búsqueda de vulnerabilidades
    - Escaneo de seguridad
    - Pruebas de intrusión
    - Evaluación de riesgo
    - Auditoría de seguridad
    - Hacking ético
    - Pruebas de seguridad y su equivalente militar

### PTES (*Penetration Testing Execution Standard*)

- Conjunto de **buenas prácticas** para **pentesting** estructuradas en **7 fases**:
    1. Autorización inicial
    2. Recolección de información
    3. Modelado de amenazas
    4. Análisis de vulnerabilidades
    5. Explotación
    6. Post-explotación
    7. Informe

### NIST 800-115 (*Technical Guide to Information Security Testing and Assessment*)

- Metodología elaborada por el NIST para evaluaciones de seguridad que contiene **4 fases**:
    1. **Planificación**: identificar objetivos, amenazas y controles para mitigar riesgos
    2. **Descubrimiento**: de vulnerabilidades y su análisis
    3. **Explotación**: se ejecutan las pruebas de penetración con los objetivos identificados
    4. **Informe**: Se analizan los resultados identificando las vulnerabilidades encontradas y recomendaciones para mitigarlas

### OWASP (*Open Web Application Security Project*)

- OWASP tiene la OTG (**OWASP Testing Guide**)
    - Metodología abierta para probar la seguridad de aplicaciones web con **11 categorías**:
        1. **OTG-INFO**: Recolección de información
        2. **OTG-CONFIG**: Gestión de la configuración
        3. **OTG-IDENT**: Pruebas sobre la administración de identidades
        4. **OTG-AUTHN**: Pruebas de autenticación
        5. **OTG-AUTHZ**: Autorización
        6. **OTG-SESS**: Gestión de sesiones
        7. **OTG-INPVAL**: Validación de datos
        8. **OTG-ERR**: Manejo de errores
        9. **OTG-CRYPST**: Pruebas sobre debilidades en la criptografía
        10. **OTG-BUSLOGIC**: Lógica del negocio
        11. **OTG-CLIENT**: Lado del cliente
    - Desarrolla las **técnicas y herramientas** a usar para auditar

### OWISAM (*Open Wireless Security Assessment Methodology*)

- Metodología abierta para probar la seguridad de redes inalambricas con en **10 categorías**:
    1. **OWISAM-DI**: Descubrimiento de dispositivos
    2. **OWISAM-FP**: Fingerprinting
    3. **OWISAM-AU**: Pruebas sobre la autenticación
    4. **OWISAM-CP**: Cifrado de las comunicaciones
    5. **OWISAM-CF**: Configuración de la plataforma
    6. **OWISAM-IF**: Pruebas de infraestructura
    7. **OWISAM-DS**: Pruebas de denegación de servicio
    8. **OWISAM-GD**: Pruebas sobre directivas y normativa
    9. **OWISAM-CT**: Pruebas sobre los clientes inalámbricos
    10. **OWISAM-HS**: Pruebas sobre hostspots y portales cautivos

### OASAM (*Open Android Security Assessment Methodology*)

- Metodología abierta para probar la seguridad de dispositivos Android con **9 categorías**:
    1. **OASAM-INFO**: Recolección de información
    2. **OASAM-CONF**: Configuration and Deploy Management
    3. **OASAM-AUTH**: Autenticación
    4. **OASAM-CRYPT**: Criptografía
    5. **OASAM-LEAK**: Fugas de información
    6. **OASAM-DV**: Validación de datos
    7. **OASAM-IS**: Intentos de spoofing
    8. **OASAM-UIR**: Unauthorized Intent Receipt
    9. **OASAM-BL**: Lógica de negocio

### CC (*Common Criteria ISO 15408*)

- Conjunto de directrices para la validación de la seguridad de los productos TIC
- *Documentos*:
    - *Protection profile* **(PP)**: requisitos y especificaciones genéricos de seguridad de los productos TIC
    - *Target of evaluation* **(TOE)**: lo que se pretende evaluar
    - *Security target* **(ST)**: requisitos de seguridad específicos que se **solicitan evaluar** en el TOE (con el PP tomado como referencia)
        - *Requisitos funcionales de seguridad* **(SFR)**
        - *Requisitos de aseguramiento de seguridad* **(SAR)**
- Tras el proceso de **evaluación** del TOE, **niveles de confianza**:
    - EAL1: funcionalidad probada
    - EAL2: estructuralmente probado
    - EAL3: probado y verificado metódicamente
    - EAL4: diseñado, probado y revisado metódicamente
    - EAL5: diseñado y probado semi-formalmente
    - EAL6: diseño verificado y probado semi-formalmente
    - EAL7: diseño verificado y probado formalmente
- Para obtener esta certificación
    - Pasar pruebas: **metodología CEM** (*Common Methodology for Information Technology Security Evaluation*

### Comparativa entre metodologías

|                      | ISAAF | OSSTMM | PTES | NIST 800-115 | OWASP | OWISAN | OASAM | CC |
|----------------------|:-----:|:------:|:----:|:------------:|:-----:|:------:|:-----:|:--:|
| *Seg. sistemas TIC*  | X     | X      | X    | X            | X     | X      |       |    |
| *Seg. productos TIC* |       |        |      |              |       |        | X     | X  |
| *Seg WiFi*           | X     | X      | X    |              |       | X      | X     |    |
| *Seg. física*        |       | X      |      |              |       |        |       |    |
| *Ing. social*        | X     | X      |      | X            |       |        |       |    |
| *Métricas*           |       | X      |      |              |       |        |       |    |
| *Informes pruebas*   | X     | X      | X    | X            |       |        |       | X  |
| *Método pruebas*     | X     |        | X    |              | X     | X      | X     | X  |
| *Gestión proyecto*   |       |        | X    |              |       |        |       | X  |
| *Autorización*       | X     | X      | X    |              |       |        |       | X  |
