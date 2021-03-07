# Tema 2: Vulnerabilidades y ataques en redes

## 2.1 Introducción

- Aumento de la interconexión de sistemas y redes
- Aumento de transmisión de información sensible por las redes
- Aumento de capacidades técnicas para hacer ataques de red
- **Es necesario evaluar la seguridad de la red de una organización**

## 2.2 Modelo de seguridad OSI

- Recomendación X.800 de la ITU
- Visión general de la seguridad:
    - **Ataques a la seguridad**
        - Ataques que buscan destruir, robar, exponer, ... información
    - **Mecanismos de seguridad**
        - Mecanismo que se implementa para reforzar un sistema
    - **Servicios de seguridad**
        - Servicios que garantizan la seguridad adecuada de los sistemas y las comunicaciones
            - Los servicios se *diseñan para*:
                - Frenar *ataques a la seguridad*
                - Haciendo uso de *mecanismos de seguridad*
            - Ejemplos:
                - Confidencialidad
                - Integridad
                - Disponibilidad
                - Autenticación
                - No Repudio
                - Control de acceso

## 2.3 Ataques a la seguridad

- **Asalto deliberado** a la seguridad del sistema
    - Eludir las protecciones
    - Hacer uso inadecuado de los recursos

### Ataques pasivos

- Escucha u observación no autorizada de las comunicaciones
    - **Difíciles de detectar**
- Tipos
    - Obtención de los contenidos de los mensajes
    - Análisis de tráfico

### Ataques Activos

- Modificación del flujo de datos o elaboración de flujos falsos
    - **Difíciles de evitar** (Detección)
- Tipos
    - Suplantación
    - Repetición
    - Modificación de los mensajes
    - Interrupción del servicio

## 2.4 Servicios de seguridad

Servicio suministrado por uno o más niveles de un sistema abierto
de comunicación, que garantiza la seguridad del sistema y de las
transferencias de datos.

- **Autenticación** (entidades o datos)
    - De entidades (con conexión)
    - Del origen de datos (sin conexión)

- **Control de acceso**
    - Prevención del uso no autorizado de un recurso

- Servicio de **Confidencialidad**
    - De la conexión
    - No orientada a conexión
    - De campos seleccionados
    - Del flujo del tráfico

- **Integridad** de los datos
    - De la conexión con recuperación
    - De la conexión sin recuperación
    - De la conexión de campos seleccionados
    - No orientada a conexión
    - No orientada a conexión de campos seleccionados

- **No repudio**
    - En origen
    - En destino

- **Disponibilidad**
    - Cualidad de estar accesible y utilizable a petición de una entidad autorizada

## 2.5 Mecanismos de seguridad

Mecanismo concreto que se utiliza para mitigar ataques y ofrecer servicios de seguridad.

- Cifrado
- Firma digital
- Mecanismos de Integridad de los Datos
- Mecanismos de Control de Acceso
- Mecanismos de Intercambio de Autenticación
- Mecanismos de Rellenado de Tráfico
- Mecanismos de Control de Encaminamiento
- Mecanismos de Notarización

| Servicio / Mecanismo                   | Cifrado | Firma | Control de acceso | Integridad | Intercambio de autentificación | Relleno tráfico | Control del enrutamiento | Notarización |
|---------------------------------------:|:-------:|:-----:|:-----------------:|:----------:|:------------------------------:|:---------------:|:------------------------:|:------------:|
| Autenticacion entidades origen/destino | :x:     | :x:   |                   |            | :x:                            |                 |                          |              |
| Autenticacion del origen de los datos  | :x:     | :x:   |                   |            |                                |                 |                          |              |
| Control de acceso                      |         |       | :x:               |            |                                |                 |                          |              |
| Confidencialidad                       | :x:     |       |                   |            |                                |                 | :x:                      |              |
| Confidencialidad del flujo             | :x:     |       |                   |            |                                | :x:             | :x:                      |              |
| Integridad de los datos                | :x:     | :x:   |                   | :x:        |                                |                 |                          |              |
| No repudio                             |         | :x:   |                   | :x:        |                                |                 |                          | :x:          |
| Disponibilidad                         |         |       |                   | :x:        | :x:                            |                 |                          |              |

| Servicio / Ataque                      | Obtención del mensaje | Análisis del tráfico | Suplantación de identidad | Repetición | Modificación del mensaje | Denegación de servicio (DoS) |
|---------------------------------------:|:---------------------:|:--------------------:|:-------------------------:|:----------:|:------------------------:|:----------------------------:|
| Autenticacion entidades origen/destino |                       |                      | :x:                       |            |                          |                              |
| Autenticacion del origen de los datos  |                       |                      | :x:                       |            |                          |                              |
| Control de acceso                      |                       |                      | :x:                       |            |                          |                              |
| Confidencialidad                       | :x:                   |                      |                           |            |                          |                              |
| Confidencialidad del flujo             |                       | :x:                  |                           |            |                          |                              |
| Integridad de los datos                |                       |                      |                           | :x:        | :x:                      |                              |
| No repudio                             |                       |                      |                           |            |                          |                              |
| Disponibilidad                         |                       |                      |                           |            |                          | :x:                          |
