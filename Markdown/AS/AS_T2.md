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

## ANEXO: Listado con ejemplos de controles (thanks [@1nc0gn1t0guy](https://github.com/1nc0gn1t0guy))

- Controles *preventivos*:
    1. Conexión redundante a la red eléctrica con compañías diferentes.
    2. Backups
    3. Realizar firmas antes de realizar cualquier pago
    4. Pedir que los empleados no fumen para evitar incendios
    5. Utilizar IPS
    6. Utilizar contraseñas seguras
    7. No usar dispositivos móviles en el entorno de trabajo
    8. No utilizar el ordenador corporativo en casa
    9. No utilizar el ordenador corporativo en redes públicas
    10. Utilizar principio de mínimos privilegios
    11. Concienciar a los empleados sobre las buenas prácticas
    12. Entrenar a los empleados
    13. Usar fuerte criptografía para la transmisión de datos
    14. Controlar los programas descargados en los ordenadores
    15. Proteger los ordenadores contra robo o daños naturales
- Controles *detectivos*:
    1. Utilizar herramientas para controlar los ordenadores en la nube
    2. Puntos de verificación en los trabajos de producción
    3. Mensajes de error
    4. Utilizar IDS
    5. Generar alertas sobre intrusiones
    6. Utilizar cámaras de seguridad conectadas 24/7
    7. Usar alarmas contra incendios
    8. Usar alarmas contra inundación
    9. Usar alarmas contra intrusos
    10. Detector de subidas de tensión
    11. Antivirus controlando el ordenador para detectar amenazas
    12. Detector de intrusiones wifi
    13. Detector de ataques de fuerza bruta
    14. Sistemas SIEM
    15. Detector de escaneo de puertos
- Controles *correctivos*:
    1. Sistema de restauración automático
    2. Utilización de un SAI frente a apagón
    3. Sumideros para evacuar agua en caso de inundación
    4. Extintores de emergencia
    5. Sistema de apagado de incendios automático
    6. Utilización de fusibles frente a subidas de tensión
    7. Corte de acceso a sistemas ante un ataque
    8. IPS que corte el acceso a un sistema posiblemente atacado
    9. Sistema de apagado automático de sistemas
    10. Utilización de los backups en caso de error
    11. Demanda en caso de traición a la empresa
    12. Formateo en caso de error
    13. Subcontratar equipo de respuesta a incidentes
    14. Finalización del contrato
    15. Honey net para engañar al atacante y contener su ataque mientras se mitiga el fallo
