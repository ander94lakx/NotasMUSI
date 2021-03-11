# Tema 4: Autenticación y Funciones Hash

## 4.1 Integridad y autenticación

- La autenticación se puede realizar en base a:
    - Algo que sé (contraseña)
    - Algo que tengo (una tarjeta)
    - Algo que soy (humano con huella dactilar, iris, ...)

- Autenticación completa: Integridad mensaje
    - No se ha modificado al transmitirse o almacenarse

- Enfoques de autenticación
    - Con cifrado convencional
        - Simétrico
        - Asimétrico
    - Sin cifrado
        - Códigos de autenticación
        - Funciones hash

## 4.2 Características y propiedades de las funciones hash

- "Huella dactilar de un mensaje o conjunto de bits
- *Entrada*:
    - De **cualquier tamaño**
- *Salida*:
    - Cadena de bits de **longitud fija**
- **Características**
    - **Unidireccional**
    - Facilidad de cálculo
    - Ajustar el tamaño, p.e. para la firma
    - **Difusión** o efecto avalancha
    - **Resistencia simple** a colisiones
        - Sabiendo M, no se puede encontrar M' tal que h(M) = h(M')
    - **Resistencia fuerte** a colisiones
        - No se pueden encontrar un par aleatorio de mensajes tal que h(M1) = h(M2)
        - Paradoja del cumpleaños
            - 23 > 50%
        - El esfuerzo medio baja a 2^(n/2)

## 4.3 Esquemas de autenticación

### Autenticación sin cifrado

- Emisor calcula h(M) y envía ambos
- Receptor recibe ambos
- Receptor calcula el hash del mensaje
- Receptor compara el hash calculado con el recibido
- (Uso de *keyed hashes*)

### Autenticación con cifrado asimétrico

- Emisor calcula h(M)
- Emisor usa d (clave privada) y cifra h(M)
- Emisor envía mensaje y el hash cifrado
- Receptor usa e (clave pública) del emisor y descifra el hash h(M)
- Receptor calcula el hash del mensaje
- Receptor compara el hash calculado con el que ha descifrado

## 4.4 Función hash MD5

- Diseñada en 1991 por Ron Rivest
- *litte endian*
- **Rota en 2005**
- Procesa los mensajes en **bloques de 512 bits** → **salida de 128 bits**
    - Expande M en bloques de 512 hasta el ultimo, en el que deja 64 bits de hueco
- Cuatro vectores iniciales ABCD
- 4 Rondas (Funciones F, G, H, I)
    - 1a ronda: `F = (B AND C) OR (NOT B AND D)`
    - 2a ronda: `G = (B AND D) OR (C AND NOT D)`
    - 3a ronda `H = (B XOR C XOR D)`
    - 4a ronda `I = (C XOR (B OR NOT D))`
- **16 vueltas** por rondandas (64 bloques)

## 4.5 Función hash SHA-1

- Diseñada por la NSA en 1995
- *big endian*
- **Salida de 160 bits**
- Vectores iniciales ABCDE (32 bits más que MD5 por la E)
- 4 Rondas (Funciones F, G, H, I)
    - 1a ronda: `F = (B AND C) OR (NOT B AND D)`
    - 2a ronda: `G = (B XOR C XOR D)`
    - 3a ronda: `H = (B AND C) OR (B AND D) OR (C AND D)`
    - 4a ronda: `I = (B XOR C XOR D)`
- **20 vueltas** por ronda (80 palabras)
- Primeras 16 palabras (mensaje)
    - 16 * 32 = 512
- 16 - 79 modificaciones de las palabras previas

## 4.6 Funciones hash SHA-256

- Familia SHA-2 creada por la NSA en 2001
- SHA-256 el mas famoso
    - **Salida de 256 bits**
- 8 vectores (256 bits)
- Operaciones muy similares a SHA-1

4.7 Conclusiones y usos futuros

- MD5 roto desde 2004
- Más usado actualmente SHA-256
- Octubre 2012 → Concurso NIST para SHA-3
    - BLAKE, Ghostl, JH, Keccak y Skein
        - Ganador **Keccak** > SHA-3
