# Tema 3: Ciclo de vida de la gestión de riesgos

## 3.1 Introducción

Los contextos cambian
►En general los parámetros y factores que influyen en la estimación del riesgo varían
.►Se debe revisar las evaluaciones inicial, para que siga reflejando la situación del momento.

- **Ciclo de vida de la gestión de riesgos**
proceso cíclico de evaluación y tratamiento del riesgo
mejora continua
metodología objetiva, fiable, medible y replicable

## 3.2 Evaluación de riesgos de TI

- **Evaluación** de riesgos: proceso global compuesto de tres procesos:
    1. **Identificación** del riesgo
    2. **Análisis** del riesgo
    3. **Valoración** del riesgo

### Identificación de riesgos de TI

- *Técnicas*
    - Métodos basados en evidencias
    - Enfoques sistemáticos
    - Razonamiento inductivo
    - Brainstorm
    - Delphi
    - ...
- **Claves** para identificar riesgos:
    - Mayor numero posible de fuentes
    - Filtrado y analizado
    - Detección temprana
- En función del grado de conocimiento, se clasifica en:
    - *Conocido-conocido*: el riesgo es perfectamente conocido.
    - *Conocido-desconocido*: el riesgo se desconoce, pero se sabe que podría existir.
    - *Desconocido-desconocido*
- *Definiciones*:
    - **Vulnerabilidad**
        - Debilidad o fallo que permite o facilita que un atacante pueda comprometer la CID
    - **Impacto**
        - Consecuencia de un evento
    - **Valor del impacto**
        - Forma cuantizada (cualitativamente o cuantitativamente) del impacto
    - **Riesgos emergentes**
        - Riesgos por amenaza nueva
        - Aumento del impacto de una amenaza conocida
        - Aumento de la probabilidad de materialización

### Análisis y valoración de riesgos de TI

- **Comprender los riesgos** de TI
    - Para **determinar y evaluar sus consecuencias**
- Hay que calcular **dos valores** de riesgo:
    - **Riesgo inherente**:
        - Riesgo al que se está expuesto **sin tener en cuenta los controles** implantados
    - **Riesgo real**:
        - Riesgo al que se está expuesto **teniendo en cuenta** la eficacia y la madurez de **los controles** implantados
- **Formula básica** del riesgo:
    - **Riesgo = Impacto x Probabilidad**
    - En función del método empleado se relacionarán de diferentes maneras
        - Tener en cuenta **Vulnerabilidad**, **Criticidad** u otros factores
- **Métodos** de análisis:
    - *Cualitativos*
        - Niveles MA, A, M, B, MB (**escala** de valores **no numéricos**)
    - *Semicuantitativos*
        - Valores **numéricos** en base a **tablas de valoración**
    - *Cuantitativos*
        - Valores **numéricos** en base a **valores del mundo real**
    - Ejemplos de métodos:
        - Matrices de valoración (MAGERIT)
        - ...
- *Importante*:
    - Establecer las **bases y criterios** utilizados
    - Todos los niveles de riesgo **son estimativos**
    - Dejar **constancia** del **nivel de exactitud**

## 3.3 Respuesta y mitigación del riesgo

- *Opciones* de tratamiento del riesgo (ISO 31000)
    - **Evitar** el riesgo decidiendo no iniciar o continuar con la actividad que lo causa
    - **Aceptar** o aumentar el riesgo a fin de perseguir una oportunidad
    - **Eliminar la fuente** del riesgo
    - **Modificar la probabilidad** (impacto)
    - **Modificar las consecuencias** (impacto)
    - **Compartir** el riesgo
    - **Retener** el riesgo en base a una decisión informada

### Mitigacion del riesgo

- *Dos opciones*:
    - Minimizar el **impacto**
    - Minimizar la **probabilidad**
- Para ambas:
    - Ampliar o mejorar **conjunto de controles**
        - Combinación de salvaguardas de diferentes tipos

### Salvaguardas

- *Dos tipos*:
    - **Preventivas**
        - Reducen la probabilidad de materialización de las amenazas
    - **Reactivas**
        - Reducen el impacto de una amenaza cuando se materializa
- **Eficacia** de las salvaguardas:
    - **Grado de implantación**
        - En **porcentaje**
        - Basado en un **modelo de madurez**
    - Grado de **eficacia real**
        - El que tiene en el momento actual
    - Grado de **eficacia intrínseca**
        - Cuando su implantación es total

## 3.4 Monitoreo y reporte de riesgos y controles

- Monitorización permanente
    - Para analizar, comprender y controlar mejor
- *Definiciones*
    - **Medida**
        - Indicación cuantitativa de un **atributos de un elemento**
    - **Métrica**
        - Indicación cuantitativa
        - En que **grado se posee** un **atributo**
    - **Indicador de riesgos**
        - Métrica o combinación de varias
        - Indica en profundidad el **comportamiento de un riesgo**

### Medidas

- *Clases*
    - **Cuantitativas**
        - Un número
    - **Cualitativas ordenadas**
        - Típicamente rangos
    - **Cualitativas**
        - Típicamente clases sin orden
- Permiten **estructurar la información**
    - Para un tratamiento:
        - Analítico
        - Estadístico
        - Descriptivo

### Métricas

- De **cumplimiento**
    - Grado de cobertura de algo
- De **eficacia** y eficiencia
    - Grado de desempeño de una función
- De **impacto**
    - Grado de consecuencias de algo
- *Definición* de una métrica
    - Valor
    - Tipo
    - Propósito
    - Cliente
    - Método de medida
    - Escala
    - Procedimiento
    - Personas a cargo
    - Ciclo de vida
    - Criterios
    - Alcance o dominio

### Indicadores

- *Características* de los indicadores
    - (S) (E) **Específicos**
    - (M) (M) **Medibles**
    - (A) (A) **Alcanzables**
    - (R) (R) **Realistas**
    - (T) (A) **A tiempo**
- *Tipos*:
    - (C) de **cumplimiento**
        - Miden el cumplimiento de las medidas y controles
    - (E) de **efectividad**
        - Miden la efectividad de las respuestas ante incidencias
    - (lead) **predictivos**
- *Tareas* para implantar métricas e indicadores:
    - Determinar las **entidades a medir**
    - Determinar lo **atributos a medir**
    - Determinar los **conceptos medibles**
    - **Definir las métricas**
- **Lo que no se mide no se puede mejorar**
    - *KGI* (Key Goal Indicator)  
    - *KPI* (Key Performance Indicator)
    - **KRI** (Key Risk Indicators)
