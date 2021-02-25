# Tema 5: Sociedad de la Información y Comercio Electrónico y Firma Electrónica

> :red_circle: La parte de firma electrónica no entra en preguntas de desarrollo

## 5.2 Firma electrónica

- Qué aporta:
- Asegurar la **integridad** del documento firmado
- Identificar al firmante de manera inequívoca
- Asegurar que el firmante **no puede repudiar** lo firmado
- Qué **NO** aporta la firma electrónica:
- **Confidencialidad** (cifrado)

### Usos de la firma electrónica

- Ciudadanos:
    - **Administración**-e
    - Firmar declaración impuestos (IRPF)
    - **Solicitudes** en registros electrónicos
    - Petición de la vida laboral
    - **Trámites** Municipales
    - Receta electrónica
    - **Compulsa** electrónica
    - Voto electrónico (futuro)
- Empresas
    - **Facturación** electrónica
    - Declaración de **impuestos** (IVA,…)
    - **Firma** de ofertas y pedidos
    - Firma de acuerdos de confidencialidad
    - Firma de contratos laborales
    - Contratación electrónica
    - Registro telemático
    - Visado/firma de proyectos
    - Compulsa electrónica
    - Trámites **notariales**
    - Presentación a **concursos públicos**
    - Firma de código
    - Recopilación consentimientos RGPD
    - Firma de correos, autorizaciones,...

### Importancia de la firma electrónica

- En 2020 se ha incrementado el uso de los certificados y la firma electrónica de forma exponencial
- Se estima que **más del 80%** de los usuarios han realizado **trámites telemáticos con la Administración** Pública en España
- En Europa, 3 de cada 4 de los servicios de las administraciones europeas se han podido gestionar telemáticamente.
- El **teletrabajo y las gestiones online** han impulsado el proceso de digitalización
- Se estima que en 2021 se producirá un aumento de más de un 30% de la firma electrónica

### Reglamento europeo 910/2014 (eIDAS)

Identificación electrónica y los servicios de confianza para las transacciones
electrónicas (*electronic Identification and Trust Services*)

- Objetivos:
    - Crear un **marco jurídico común** y eliminar las barreras entre países
    - Hacer posible la **firma electrónica transfronteriza**
    - Sacar más ventaja de la **identificación electrónica** en el mercado único digital
    - Asegurar que los servicios **funcionan a través de las fronteras** y que gozan del mismo estatuto jurídico que los trámites tradicionales en papel
- Beneficios
    - Ciudadanos
        - **Declaraciones fiscales** en varios países
        - Abrir una **cuenta bancari**a en otro país de la UE
        - Autorizar acceso al historial médico en línea
        - **Estudiantes** que se matriculan o solicitan becas en otro país
        - **Verificación de la edad** para el acceso a las RRSS
        - Reforzar cumplimiento **RGPD**
        - Compartir únicamente la información necesaria para reducir el riesgo de mal uso (caso Cambridge Analytica)
        - Identidad digital esencial en el Desarrollo de sistemas Blockchain.
    - Empresas
        - Presentarse a **concursos públicos en cualquier país de la UE**
            - Firmar y sellar sus ofertas
        - **Contratos telemáticos**
        - **Crear empresas** a través de **Internet**
        - Presentar **informes** anuales **en línea**

### Ley 6/2020

- **Adaptar** el ordenamiento jurídico de España al **marco regulatorio de la UE**
- Regula **determinados** aspectos de los servicios electrónicos de confianza
- **No es** una regulación sistemática de los servicios electrónicos de confianza, que ya han sido legislados por el eIDAS
- **Es un complemento** en aquellos **aspectos concretos** que el Reglamento no ha armonizado y cuyo desarrollo prevé en los ordenamientos de los diferentes Estados miembros

### Certificados electrónicos

#### Tipos de certificados

- Certificado de **firma**: identificación y firma de *personas físicas* (firmantes)
- Certificado de **sello**: sello de *personas jurídicas*
    - Para autenticar cualquier activo digital de la persona^jurídica, por ejemplo, programas informáticos o servidores
- Certificado de autenticación web.
    - Vincula sitio web (dominio de Internet) con persona física o jurídica titular del certificado
- Certificado no cualificado

#### Tipos de Firma

- Firma **avanzada**
    - Permite **identificar al firmante**
    - **Detectar cambios** en datos firmados (integridad)
    - vinculada al firmante de manera única y a los datos a que se refiere
    - Creada por medios que el firmante puede mantener bajo su exclusivo control
- Firma **cualificada**
    - Firma avanzada
    - Basada en un certificado cualificado
    - Generada mediante un **dispositivo cualificado de creación de firma**

#### Fimrma electrónica

- La firma electrónica cualificada (QES):
    - **Misma validez legal que la firma manuscrita**
    - Tiene una **presunción de autenticidad**
    - Es la **única reconocida** por todos los Estados miembro de la **UE**
- La firma electrónica no cualificada (avanzada):
    - No puede ser rechazada jurídicamente
    - **El creador** de la firma quien **tiene que demostrar su validez**

#### Pros y contras de cada tipo de firma

|                      | Firma electrónica (simple) |       Firma electrónica avanzada      |     Firma electrónica cualificada    |
|----------------------|:--------------------------:|:-------------------------------------:|:------------------------------------:|
| Facilidad de uso     |     :heavy_check_mark:     |           :heavy_check_mark:          |                  :x:                 |
| Seguridad            |             :x:            | :heavy_check_mark: :heavy_minus_sign: | :heavy_check_mark: :heavy_plus_sign: |
| Garantías legales    |             :x:            | :heavy_check_mark: :heavy_minus_sign: | :heavy_check_mark: :heavy_plus_sign: |
| Requiere dispositivo |             :x:            |                  :x:                  |          :heavy_check_mark:          |


### Prestadores de Servicios Electrónicos de Confianza (PSEC)

- Entidades que expiden certificados electrónicos o presta otros servicios en relación con la firma electrónica
- En inglés: *Qualified Trust Service Provider* (QTSP)

#### Obligaciones de los PSEC

- Proteger los datos personales
- No almacenar ni copiar los datos de creación de firma
- Utilizar sistemas fiables
- Tomar medidas contra la falsificación y por la confidencialidad
- Garantía económica
- Superar las auditorías realizadas
- Mantener directorio actualizado, integro y disponible de certificados
- Publicar Declaración de Prácticas de Certificación (DPC)
- Medidas de seguridad técnicas y organizativas
- Disponible al público

#### Responsabilidades de los PSEC

- Responderán por:
    - Daños y perjuicios en caso de incumplimiento.
    - Falta o retraso inclusión en CRLs de extinción o suspensión
- Limitaciones de responsabilidad:
    - **No** serán responsables **si el firmante**:
        - **No protege** adecuadamente la **clave privada**
        - No solicita la suspensión o revocación en caso necesario
        - Firma con **certificado expirado, revocado o suspendido**
    - No serán responsables si el destinatario:
        - No comprueba extinción o suspensión o no verifica firma
- Obligaciones de seguridad de la información
    - Tomar las medidas para resolver incidentes de seguridad
    - Notificar al Ministerio (Asuntos Económicos y Transformación Digital) de violaciones de seguridad

##### PSEC en España

Públicos
    - CERES-FNMT
        - Alcance: todos los ciudadanos
    - Comunidades autónomas (Cataluña, País Vasco y Valencia)
Privados
    - Colegios profesionales: Abogados, Notarios, Médicos, Ingenieros, Registradores…
- Categorías de servicios
    - Servicios de certificación basados en certificados **cualificados**
    - Servicios de certificación basados en certificados **no cualificados**
    - Servicios de **validación temporal**
    - Otros servicios (p.e. certificados de Atributo o Autoridad)

### Dispositivos Cualificados de Creación de Firma (DSCF/QSCD)

- Ofrecen seguridad razonable de que:
    - Los datos utilizados para la generación de firma (clave privada)
    - No pueden ser obtenidos a través de:
        - Los datos de verificación de firma
        - De la firma
- Firma protegida contra la falsificación
- No altera los datos/documento a firmar

#### Legislación

- **Decisión de Ejecución (UE) 2016/650** de la Comisión:
    - Normas para la evaluación de la seguridad de los QSCD

#### Organismo de Certificación - Centro Criptológico Nacional (OC-CNN)

- Certifica la seguridad de productos y sistemas de TI
    - Asegura que:
        - Tengan diseño adecuado y apropiado
        - Estén correctamente implementados
        - No realicen funciones no deseadas
    - Tiene una lista con productos certificados
        - El **DNI 3.0** es un producto certificado com DQCF
- Acredita laboratorios de evaluación de la seguridad TI

#### Tipos de DQCF

- Tarjetas inteligentes / tokens
- DNIe

### Certificados digitales

- Solicitarlo a un PSEC
    - En función del tipo de certificado se puede requerir trámite presencial para solicitarlo
    - eIDAS planta la base para:
        - Identificación por video remoto
        - Gestión centralizada de certificados digitales
        - Uso del movil como elemento de identificación
- Tipos:
    SW: Se gestiona con el SO y según el tipo con programas
    HW: Se entrega en mano o por correspondencia
