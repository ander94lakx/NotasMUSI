# Tema 2: Criptografía clásica y cifra moderna

## 1. Principios de Kerschhoffs (1883)

Son una serie de principios que se deben cumplir en criptografía para que el **sistema** sea seguro y práctico:

- **En la práctica, indescifrable**
    - Es decir, que aunque se pueda romper por fuerza bruta, esa fuerza bruta sea demasiado grande en comparación con la capacidad de cómputo global existente

- El sistema **no debe ser secreto**

- La **clave** del sistema debe ser **fácil de memorizar** y comunicar a otros
    - Además **debe ser cambiable** y modificable por los interlocutores válidos

- El sistema **debe poder aplicarse** a  un sistema de transmisión de datos
    - Es decir, que no sea demasiado pesado

- El sistema **debe ser portable** y su uso no deberá requerir la intervención de varias personas.

- El sistema debe ser **fácil de usar**, no requerirá conocimientos especiales ni tendrá una larga serie de reglas

## 2. Clasificación de los sistemas de cifra clásica

- Transposición (difusión)
    - Grupos
    - Escítala
    - Series
    - Columnas
    - Filas
- Sustitución (confusión)
    - Monoalfabética
        - Monográmica
            - Alfabeto estándar
                - ***César***
                - ***Afín***
            - Alfabeto mixto
        - Poligrámica
            - Digrámica
                - *Playfair*
            - N-Grámica
                - ***Hill*** :red_circle:
    - Polialfabética
        - No periódica
            - *Vernan*
        - Periódica
            - Lineales
                - Alfabeto estándar
                    - ***Vigenère*** :red_circle:
                - Alfabeto mixto
            - Progresivos
                - *Enigma*

## 3. Cifrado por permutación

- Consisten en recolocar los elementos
- Poco seguros
    - Grupos
    - Escítala
    - Series
    - Columnas
    - Filas

## 4. Cifrado por sustitución

| A | B | C | D | E | F | G | H | I | J | K  | L  | M  | N  |
|---|---|---|---|---|---|---|---|---|---|----|----|----|----|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| Ñ  | O  | P  | Q  | R  | S  | T  | U  | V  | W  | X  | Y  | Z  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

### Cifrado César

- Inverso aditivo B = -3 → `K mod 27 = -3 + 27 = 24`

- `C = (M + B) mod 27`
    - Para cifrar `B = -3 = 24`
    - Para descifrar `B = 3`
- Ejemplo:
    - `M = UN ABRAZO` → `C = RK XYOXWL`

### Decimación

- **Cifrado**: `C = a·m mod n`
- **Descifrado**: `M = c·inv(a, n) mod n`
    - Donde:
        - `a` se elige
        - `n` es el tamaño del cuerpo
        - `inv(a, n)` es el inverso de `a` en el módulo `n`

### Afín

- **Cifrado**: `C = (a·m + b) mod n`
- **Descifrado**: `M = (c - b) · inv(a, n) mod n`
    - Donde:
        - `a` y `b` se eligen
        - `n` es el tamaño del cuerpo
        - `inv(a, n)` es el inverso de `a` en el módulo `n`
- Ejemplo:
    - Mensaje = "HOLA MUNDO"
    - Clave: `a = 2` `b = 5`
        - `H = 7` → `c = (2·7 + 5) mod 27 = 19` → S
        - `O = 15` → `c = (2·15 + 5) mod 27 = 8` → I
        - ...
        - Criptograma = "SIAF CTELI"
    - Criptograma = "SIAF CTELI"
    - Clave: `a = 2` `b = 5` `inv(2, 27)=14`
        - `S = 19` → `m = (19 - 5) · 14 mod 27 = 7` → H
        - `I = 8` → `m = (8 - 5) · 14 mod 27 = 15` → O
        - `A = 0` → `m = (0 - 5) · 14 mod 27 = -70 mod 27 = -16 mod 27 -> 11 mod 27 = 11` → L
        - ...
        - Mensaje = `HOLA MUNDO`

### Cifrado de Vigenère

- **Cifrado**: `C[i] = (M[i] + K[i]) mod n`
- **Descifrado**: `M[i] = (C[i] - K[I]) mod n`
    - Donde:
        - `M[i]` es cada una de las letras del mensaje
        - `K[i]` es cada uno de los caracteres de la clave
            - Si la clave es menor que el mensaje, **se va repitiendo**
        - `C[i]` es cada uno de las letras del mensaje
- Ejemplo:
    - Mensaje: "HERMOSO"
    - Clave: "CIELO"
        - Expansión de clave para cubrir todo el mensaje: "CIELOCI"
    - Operaciones:
        - `C[i] = "H" + "C" mod 27 = 7 + 2 mod 27 = 9` → "J"
        - `C[i] = "E" + "I" mod 27 = 4 + 8 mod 27 = 12` → "M"
        - `C[i] = "R" + "E" mod 27 = 18 + 4 mod 27 = 22` → "V"
        - `C[i] = "M" + "L" mod 27 = 12 + 11 mod 27 = 23` → "W"
        - `C[i] = "O" + "O" mod 27 = 15 + 15 mod 27 = 3` → "D"
        - `C[i] = "S" + "C" mod 27 = 19 + 2 mod 27 = 21` → "U"
        - `C[i] = "O" + "I" mod 27 = 15 + 8 mod 27 = 23` → "W"
    - Criptograma: "JMVWDUW"

#### Criptoanálisis del cifrado de Vigenère Kasiski

- Consiste en **reducir de cifrado polialfabético a monoalfabético**
- Buscar los elementos más repetidos
- Correlar con las letras más comunes del alfabeto **A → E → O**
    - Buscar separaciones de espacios entre ellas:
        - **A → (+4) → E (+11) → O**

## 5. Cifrado por matrices

### Cifrado de Hill

- B(M): Bloques de n letras del mensaje N
- K = matriz(nxn)
- **Cifrado**: `C = K x B(M) mod n`
    - (Matriz(nxn) X Matriz(nx1) = Matriz(nx1))
- **Descifrado**: `M = K^-1 x B(C) mod n`
    - **Matriz inversa** de la clave K: `K^-1`
    - **Misma operación** pero con matriz inversa los bloques del criptograma
- Ejemplo:
    - Mensaje: "RRG"
    - Clave: [5, 24, 1; 13, 10, 10; 20, 17, 15]
        - C = [5, 24, 1; 13, 10, 10; 20, 17, 15] x [18; 18; 6] mod 27 = [15; 15; 0]
    - Mensaje cifrado: [15; 15; 0] = "OOA"
        - M: [14, 16, 1; 10, 2, 7; 15, 7, 6] x [15; 15; 0] mod 27 = [18; 18; 6]

```text
    5  24   1         18              15
 ( 13  10  10 )  X  ( 18 ) mod 27 = ( 15 )
   20  17  15          6               0

   14  16   1         15              18
 ( 10   2   7 )  X  ( 15 ) mod 27 = ( 18 )
   15   7  16          0               0
```

#### Criptoanálisis del cifrado de Hill

- **Gauss-Jordan**

## 6. Características de los sistemas de cifra modernos

- Se cifra haciendo uso de bits y no de letras
- En función de como se trate el mensaje
    - Cifra en flujo
    - Cifra en bloque
- En función de si se usa la misma clave o no para descifrar
    - Cifrado simétrico
    - Cifrado asimétrico
- Seguridad computacional:
    - Con los recursos actuales (ojo con la computación cuántica) es materialmente imposible romperla (al menos los algoritmos fuertes), aunque sea matemáticamente posible

## 7. Cifra simétrica versus cifra asimétrica

- Cifrado **simétrico**
    - Confidencialidad
    - Sin intercambio de clave
    - Autenticación parcial
    - Sin firma digital
    - Claves:
        - Longitud pequeña (centenares bits)
        - Vida corta (sesión)
        - Número elevado (mala gestión)
    - Velocidad (MB/s)
- Cifrado **asimétrico**
    - Confidencialidad
    - Con intercambio de clave
    - Autenticación total
    - Con firma digital
    - Claves:
        - Longitud grande (miles de bits)
        - Vida larga (1 o 2 años)
        - Número reducido (buena gestión)
    - Velocidad (KB/s)
