# Tema 2: Criptografía clásica y cifra moderna

## 2.1 Principios de Kerschhoffs (1883)

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

## 2.2 Clasificación de los sistemas de cifra clásica

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

## 2.3 Cifrado por permutación

- Consisten en recolocar los elementos
- Poco seguros
    - Grupos
    - Escítala
    - Series
    - Columnas
    - Filas

## 2.4 Cifrado por sustitución

### Cifrado César

- Inverso aditivo B = -3 → `K mod 27 = -3 + 27 = 24`

    | A | B | C | D | E | F | G | H | I | J | K  | L  | M  | N  | Ñ  | O  | P  | Q  | R  | S  | T  | U  | V  | W  | X  | Y  | Z  |
    |---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

- `C = (M + B) mod 27`
    - Para cifrar `B = -3 = 24`
    - Para descifrar `B = 3`
- Ejemplo: `M = UN ABRAZO` → `C = RK XYOXWL`

### Cifrado por decimación y afín

#### Decimación

- Cifrado: `C = a·m mod n`
- Descifrado: `M = c·inv(a,n) mod n`
    - Donde:
        - `a` se elige
        - `n` es el tamaño del cuerpo
        - `inv(a, n)` es el inverso de `a` en el módulo `n`

#### Afín

- Cifrado: `C = (a·m+b) mod n`
- Descifrado: `M = (c-b) · inv(a,n) mod n`
    - Donde:
        - `a` y `b` se eligen
        - `n` es el tamaño del cuerpo
        - `inv(a, n)` es el inverso de `a` en el módulo `n`

Ejemplo

- Mensaje = “HOLA MUNDO”
- Clave: `a=2` `b=5`
    - `H = 7` → `c = (2·7+5) mod 27 = 19` → S
    - `O = 15` → `c = (2·15+5) mod 27 = 8` → I
    - Criptograma = `SIAF CTELI`
- Criptograma = `SIAF CTELI`
- Clave: `a=2` `b=5` `inv(2,27)=14`
    - `S = 19` → `m = (19-5)·14 mod 27 = 7` → H
    - `I = 8` → `m = (8-5)·14 mod 27 = 15` → O
    - `A = 0` → `m = (0-5)·14 mod 27 = -70 mod 27 = -16 mod 27 -> 11 mod 27 = 11` → L
    - Mensaje = `HOLA MUNDO`

### Cifrado de Vigenère

## 2.5 Cifrado por matrices

### Cifrado de Hill

## 2.6 Características de los sistemas de cifra modernos

## 2.7 Cifra simétrica versus cifra asimétrica

## 2.8 Usos de estos algoritmos
