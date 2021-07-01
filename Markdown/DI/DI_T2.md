# Tema 2: Tipos delictivos I. Fraudes en la red

## 1. Introducción

- Las estafas son los delitos que **más rápido y con más éxito** han realizado la migración **desde la vida real a la virtual**
- Existe una mayor incidencia de **cifra negra** (delitos no denunciados)
    - Suelen ser por importes bajos
    - "No merece la pena denunciar"
- Categorías principales:
    - Phishing
    - Fraude en medios de pago físicos
    - Otros tipos de fraude

## 2. Estafas en banca electrónica. **Phishing**

- **Phishing**:
    - Aquellas **acciones** desarrolladas **con fin de obtener**
        - **mediante ingeniería social y/o malware**
    - La **información** necesaria para **acceder de manera no autorizada** a **determinados servicios** (no únicamente financieros)
    - **Suplantando** en ellos **la identidad** de su legítimo titular
- También se usa el termino para describir el **proceso delictivo completo**
    - Tres fases:
        1. Captura de datos
        2. Captación de mulas
        3. Transferencia, monetización y envío de lo defraudado

### Fase I: Captura de datos

- Obtención de datos confidenciales (usuarios, claves, números de teléfono, direcciones, documentación, números de tarjetas de crédito, etc.)
    - Cualquier dato que le permita o le acerque a su objetivo (suplantar identidad)
- Esto se puede llevar a cabo a través de:
    - **Ingeniería social**
    - **Malware**
- Con esos datos se puede:
    - **Continuar el ciclo (phishing bancario)**
    - Vender o usar los datos (para cualquier tipo de phishing)
        - Generacion de botnets
        - Venta de datos, usuarios, contraseñas, ...
        - Preparación de nuevos ataques

#### Ingeniería social

- Conjunto de técnicas para engañar al usuario para conseguir sus datos
- Tipos:
    - **Web falsa**
        - *Typosquatting* (usar URL o dominios parecidos para buscar el error o engañar al usuario)
    - **Correos fraudulentos**
        - Buscan engañar al usuario para que proporcione sus datos
        - Imitan apariencia de correos originales (*truco*: buscar pequeñas discrepancias, errores de ortografía)
        - Imitan direcciones con dominios similares
        - Ocultan URL
    - **Smishing** (phisihng a través de SMS)
        - Usan los SMS como vector para engañar
        - URL falsas enviadas por SMS
    - **Vishing** (fishing a través de llamadas de voz)
        - Pedir datos
    - **Whaling**
        - Phishing dirigido a un usuario concreto
        - Más común en entornos empresariales
            - Fraude al CEO

#### Malware

- A lo largo de los años, se han ido **mejorando la seguridad** ante este tipo de ataques de phishing
    - Campañas de advertencia y sensibilización
    - Medidas de autenticacion más seguras
        - Tarjetas de coordenadas
        - SMS de verificación
- De la misma manera, se ha diseñado **malware especifico para ayudar a los cibercriminales** con sus tareas delictivas, que complementa a la ingeniería social
    - Hay ciertos tipos de **malware pensados para robar** este tipo de **información personal**
        - Vectores de ataque:
            - **Vulnerabilidades**
            - **Técnicas de ingeniería social**
- Tipos de malware más comunes:
    - **Keyloggers**
        - Permiten **registrar las pulsaciones** del teclado del usuario
        - Debido a ello, los sistemas bancarios comenzaron a implementar teclados en pantalla
    - **Screenloggers**
        - Monitorizan la **pantalla** del usuario
        - Son efectivos con sistemas que usan teclados en pantalla
    - **Troyanos bancarios**
        - Específicamente diseñados y desarrollados para robar información bancaria
        - Su diseño les permite **determinar cuándo** deben activarse y **comenzar a actuar**
        - **Modifican las webs de entidades bancarias** para añadir campos trampa o para **monitorizar** los datos introducidos por el usuario
        - Ejemplos: *ZeuS*, *Spy Eye*
    - **Alteración de DNS: Pharming**
        - **Modificar** el servicio de **DNS para redirigir a paginas fraudulentas**
        - Pueden realizarse tanto **a un usuario** concreto como **al propio servidor DNS**
        - Algunos permiten instalar certificados SSL para validar la conexión con la página falsa

### Fase 2: Captación de mulas

- Fase **específica para ataques de phishing orientados a banca electrónica**
- **Mulas**: intermediarios para recibir el dinero robado
    - Reciben pequeñas cantidades para que no parezca fraudulento
    - Después traspasan este dinero y se llevan una parte
- ¿**Cómo captar** mulas?: **Engañar o persuadir** a víctimas
    - Correos electrónicos ofreciendo "oportunidad única"
    - Encubrir la actividad como algo legal
- La complejidad y nivel de refinado de las operaciones depende del tipo de organización cibercriminal

### Fase 3: Transferencia, monetización y envío de lo defraudado

- Consiste en la ejecución de la operación
    - **Usar los datos robados** para **transferir el dinero a las mulas**
        - Días y horas no laborables (retrasar el tiempo hasta que se den cuenta)
    - Esperar a que **las mulas muevan el dinero**
        - Empresas internacionales de **envío de dinero**
        - Países de europa del este o paraísos fiscales
        - En algunos casos esta entrega **puede ser presencial**
        - Puede llegar a usarse para **comprar monedas virtuales** y revender estas

### Consejos para prevenir phishing

- Prestar **atención a las URL** (acortadores de enlaces, URL hijacking)
- Comprobar los **certificados** de la web
- Fijarse en la **sintaxis** de las webs y los correos desconocidos
- Mantener **actualizado el navegador**
- Usar un navegador diferente para gestiones bancarias
- Comprobar **dominios en las direcciones de correos** electrónicos
- **No descargar adjuntos** en correos electrónicos de remitentes desconocidos

## 3. Fraude en medios de pago físico

- Cualquier fraude relacionado con medios de pago físicos
    - Tarjetas de crédito
    - Pagos por NFC con el móvil

### Card no present fraud (CNP Fraud)

- Usar técnicas (normalmente phishing) para:
    - **Robar la información de una tarjeta de crédito** (número, fecha de caducidad, CVC)
    - Para **poder hacer pagos y compras con ella** a través de internet
- Compra de objetos de fácil reventa (productos electrónicos)
- Domicilios no relacionados con los autores

### Skimming

- Conjunto de **técnicas y procedimientos para** llegar a conseguir el **clonado de una tarjeta** bancaria
    - Copia de información de banda magnética, chip o contactless
    - Es **necesario saber el pin para usar** la tarjeta clonada
- Las técnicas concretas consisten normalmente en:
    1. **Instalación física de sistemas lectores**
        - Se instalan en los cajeros y se diseñan a medida para ocultarse sobre ellos
        - Dos tipos:
            - **Sistema de clonado de tarjetas**
                - **Se superpone** sobre la ranura para tarjetas o el lector NFC
                - Clona los datos
                - Envía los datos de manera inalámbrica
                - O es recogido posteriormente para obtener los datos manualmente
            - **Sistema para obtener el PIN**
                - Hay diversos tipos:
                    - **Teclados superpuestos**
                    - **Cámaras ocultas** en el cajero
                    - **Cámaras térmicas**
    2. Empleado confabulado
        - Consiste en que **un empleado se encargue de clonar las tarjetas** con un clonador cuando un cliente se la entregue para realizar gestiones
        - Se suele **combinar con técnicas de observación** para obtener **el PIN**
    3. Clonado sutil
        - Pensado para tarjetas con NFC (*contactless*)
        - Un **atacante se acerca de manera sigilosa** y pueda clonar la tarjeta con un dispositivo oculto

#### Reventa y uso de clonados de tarjetas

- La **información** de clonado y PIN se suele **revender**
    - Suele venderse en lotes
    - Sus precios varian en función del tipo de tarjeta
- También se puede **usar para generar tarjetas falsas** con esa información
    - Ello requiere material muy especifico
        - Impresoras de alta calidad
        - Hologramas falsificados
        - Troqueladoras precisas
        - Codificadores de tarjetas
    - Este tipo de productos también se pueden vender en el mercado negro

## 4. Otros tipos de fraude en la red

- Existen todo tipo de forma para estafar por la red, solo limitadas por la imaginación del delincuente
- Algunos ejemplos conocidos:
    - *"Carta Nigeriana"*
        - Timo por correo electrónico
        - Se hace pasar por un príncipe o alguien rico que necesita dinero prometiendo devolver más dinero a cambio
        - Busca robar dinero
    - *"Premio de la lotería"*
        - Timo por correo electrónico
        - Busca engañar a la victima con un falso premio de lotería
        - Sus objetivos son ponerse en contacto para robar datos o estafar dinero
    - *"Venta de vehículos a través de Internet"*
        - Consiste en la venta de un producto falso (normalmente vehículos)
        - Productos "ganga" que suelen estar en otros países (como los vendedores)
        - Usan empresas de escrow falsas para aparentar legitimidad
        - Buscan robar dinero en forma de adelantos o fianzas
    - *"Romancescam"*
        - Cualquier tipo de estafa que involucre un componente románticos
        - Suelen ser lentas y meticulosas
        - Ejemplo: *"Novia Rusa"*
            - Mujer falsa que simula afecto para conseguir dinero a cambio
    - *"Accidente o enfermedad en un país extranjero"*
        - Compleja de realizar
        - Busca robar dinero haciéndose pasar por un conocido en una situación de necesidad urgente
    - Falsos antivirus (Rogues)
        - Maquear que se hace pasar por amenaza falsa y engaña para comprar un producto antimalware falso
    - SIM swapping
