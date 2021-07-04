# Tema 2: Gobierno y gestión de la función de auditoría

## 1. Gestión de la función de auditoría

- Organización de la función de auditoría
- Gestión de los recursos de auditoría de sistemas de información
- Ubicación del departamento de auditoría
    - Jerarquía suficiente para poder inmiscuirse en cualquier unidad
    - Tipo de funciones relacionadas con la dirección, control y coordinación
    - Suficiente autoridad
- Miembros de una unidad de auditoría interna
    - **Director** de auditoría
    - **Gerente** de auditoría: Asiste al director
    - **Supervisor** de auditoría: supervisa el cumplimiento diversas auditorías
    - **Encargado** de auditoría: planea y conduce auditorías (líder de un equipo de auditores)
    - Auditor **ayudante**
    - Auditor **junior**: lleva los cafés y cobra la mitad de su jornada en negro
- El **equipo auditor debe**:
    - **Conocer la organización** (áreas, áreas auxiliares, trabajo desarrollado, estudios organizacionales)
    - Tienen que **ser**:
        **Objetivo**, **responsable**, **integro**, **confidencial**, **comprometido** y **honesto**

## 2. Clasificación de los controles

- **Controles**:
    - Acciones y mecanismos definidos para prevenir o reducir el impacto de los eventos no deseados
- *Clasificación*:
    - *General*:
        - **Voluntarios**: cuando la organización los diseña con el fin de mejorar los procesos.
        - **Obligatorios**: (por auditoría o regulación)
        - **Manuales**: cuando son ejecutados por personas.
        - **Automáticos**: si son llevados a cabo a través de sistemas de información automatizados.
        - **Generales**
        - **De aplicación**: (integrados en SW)
    - En base en su *aplicabilidad*:
        - **Físicos u operacionales**: orientados a la protección del entorno y de los recursos físicos
            - *Ejemplos*: Puertas, cerraduras, ventanas
        - **Lógicos o técnicos**: basados en Hw y SW
            - Ejemplos: criptografía, antimalware, firewalls
        - **Administrativos o de gestión**: procedimientos, políticas, directrices para proteger el entorno
            - *Ejemplos*: Política de seguridad, gestión de privilegios, controles de contratación de personal
    - En base a su *naturaleza*:
        - **Preventivos**: para mitigar el impacto o la probabilidades
        - **Detectivos**: informar de hechos no deseados
        - **Correctivos**: cuando se produce un incidente
    - En base a su *comportamiento*:
        - **Defensivos**
            - **Salvaguardas**: para impedir que una amenaza se materialice
                - Directivos: acuerdos de confidencialidad, SLA
                - Disuasorios: avisos de advertencia, video-vigilancia, ..
                - Preventivos: vallas, firewalls, ...
            - **Contramedidas**: para cuando ya se ha materializado una amenaza
                - De engaño: honeypots, ...
                - Detectivos: logs, IDS, ...
                - Correctivos: extintores, finalizacion de contrato,,...
                - De recuperación: backups, procesamiento de datos alternativo, ...
        - **Ofensivos**
            - **Pasivos**:
                - Ejemplos: sniffing, ...
            - **Activos**:
                - Ejemplos: escáneres de vulnerabilidades, auditorías técnicas, ...
        - **Alternativos o compensatorios**: controles secundarios de mitigación

## 3. La regla de oro

- La *regla de oro* para diseñar e implantar controles
    - **Principio básico de proporcionalidad** (tener en cuenta):
        - **Coste del** diseño, implantación, monitorización y mantenimiento del **control**
        - **Coste del impacto que tiene el riesgo** si se materializa
        - **Coste potencial de la no implementación del control**
    - **Riesgo vs. control vs. coste**

## ANEXO: Listado con ejemplos de controles
