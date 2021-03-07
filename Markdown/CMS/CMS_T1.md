# Tema 1: Fundamentos de criptografía y seguridad

## 1. ¿Qué es la criptografía?

- Herramientas matemáticas, técnicas y algoritmos
    - Que con el uso de una o más **claves**
    - Permiten cifrar la información, protegerla y dotarla al menos de:
        - **Confidencialidad** e **Integridad**

## 2. Codificar VS Cifrar

- Codificar: usar un código para representar elementos
- Cifrar: transformar inflamación mediante el uso de una **clave**

## 3. Terminología

- Mensaje: mensaje sin cifrar, puede ser texto, stream de bits, cualquier tipo de información.
- Criptograma: salida que se obtiene tras cifrar un mensaje
- Clave: elemento que se utiliza para la transformación de un mensaje en un criptograma y viceversa
    - Clave de descifrado: clave que se utiliza para convertir un cifrado de un

## 4. Contextualización de la criptografía

- Criptología: disciplina que se dedica al estudio de la escritura secreta
    - **Criptografía**: estudia de los algoritmos, protocolos y sistemas que se utilizan para proteger la información
    - Esteganografía: estudia cómo *ocultar* mensajes con información privada por un canal inseguro
    - **Criptoanálisis**: estudia los sistemas criptográficos para encontrar debilidades y romper dichos sistemas

## 5. Clasificación de los criptosistemas

- Criptografía clásica
- Criptografía moderna
    - Se puede clasificar por:
        - Naturaleza clave:
            - Criptografía simétrica: se usa la misma clave para cifrar y descifrar
            - Criptografía asimétrica: se usan claves diferentes para el cifrado y el descifrado
        - Tratamiento de la información:
            - Cifrado en flujo
            - Cifrado por bloque

## 6. Personajes relevantes en el desarrollo de la criptografía

- Claude Shannon: padre de la teoría de la información
- Horst Feistel: desarrolló el algoritmo DES (ya sustituido por AES)
- Whitfield Diffie y Martin Hellman: desarrollaron un protocolo para establecer claves entre dos partes conocido como protocolo **Diffie-Hellman**

## 7. Matemáticas discretas

Son el pilar fundamental de la criptografía.
Principales conceptos usados ampliamente en criptografía:

- Aritmética modular
- Inversos en un cuerpo
- Algoritmo extendido de Euclides AEE
- Raíces primitivas de un cuerpo
- Exponenciación rápida

### Aritmética modular

Conjunto de valores finito y "cíclico".

Módulo (equivalente al resto de la división):

- `15 mod 11 = 4`
- `20 mod 5 = 0`
- `198 mod 27 = 9`

Clases de equivalencia:

- Ejemplo módulo 4:
    - -3 equivale a 1 en módulo 4 (`-3 + 4 = 1`)
    - 10 equivale a 2 en módulo 4 (`10 mod 4 = 2`)
    - -9 equivale a 3 en módulo 4 (`-9 mod 4 = 3`)

Operaciones en aritmética modular:

- Suma
- Resta
- Multiplicación
- Potencia
    - Ampliamente usado en criptografía de clave pública
    - Exponenciación rápida
    - Criptografía de clave pública
- La división no es posible
    - Uso de inversos multiplicativos

### Inversos en un cuerpo

Inverso aditivo de `x` en módulo `n` (`inv+(x, n)`):

- Número que sumado a `x` da 0
- Ejemplo:
    - Inverso aditivo de 23 en módulo 60

```bash
inv+(23, 60) = 37 

23 + 37 mod 60 
= 60 mod 60 
= 0)
```

Inverso XOR de `x` en módulo `n` (`invXOR(x, n)`):

- El mismo número (`invXOR(x, n) = x`)
- Ejemplo:

```bash
invXOR(23, 60) = 23

23 xor 60 = 43
43 xor 60 = 23
```

Inverso multiplicativo de `x` en módulo `n` (`inv(x, n)`):

- Multiplicado por `x` da 1
- Ejemplo:

```bash
inv(23, 60) = 47

23 · 47 = 1081
1081 = 18 · 60 + 1
1081 mod 60 = 1
```

### AEE (Algoritmo Extendido de Euclides)

Sirve para encontrar el inverso multiplicativo de x (`x = inv(a, n)`)

#### Ejemplo para `inv(9, 25)`

1. ¿Existe el inverso? ¿Son coprimos?
    - Si `mcd(9, 25) = 1` -> sí existe
2. AEE
    - `g[0, 1] = n, a,`
    - `u[0, 1] = 1, 0`
    - `v[0, 1] = 0, 1`
    - Mientras `g[i] != 0`:
        - `y[i+1] = int(g[i-1] / g[i])`
        - `g[i+1] = g[i-1] mod g[i]`
        - `u[i+1] = u[i-1] - y[i+1] · u[i]`
        - `v[i+1] = v[i-1] - y[i+1] · v[i]`

```bash
    i |  y[i]  g[i]  u[i]  v[i]
    ------------------------------
    0 |   -    25     1     0
      |
    1 |   -     9     0     1
      |
    2 |   2     7     1    -2
      |
    3 |   1     2    -1     3
      |
    4 |   3     1     4   -11
    ------------------------------
    5 |   2     0    -9    25

    inv(9, 25) = -11 = 14
    
    -11 + 25 = 14
```

3. Comprobar
    - u[f] = a && v[f] = n
    - (x · a) mod n = 1
        - `(14 · 9) mod 25 = 126 mod 25 = (5 · 25 + 1) mod 25 = 1`

#### Ejemplo para `inv(9, 275)`

1. ¿Existe el inverso? ¿Son coprimos?
    - Si `mcd(9, 275) = 1` -> sí existe
2. AEE
    - `g[0, 1] = n, a,`
    - `u[0, 1] = 1, 0`
    - `v[0, 1] = 0, 1`
    - Mientras `g[i] != 0`:
        - `y[i+1] = int(g[i-1] / g[i])`
        - `g[i+1] = g[i-1] mod g[i]`
        - `u[i+1] = u[i-1] - y[i+1] · u[i]`
        - `v[i+1] = v[i-1] - y[i+1] · v[i]`

```bash
    i |  y[i]  g[i]  u[i]  v[i]
    ------------------------------
    0 |   -    275    1     0
      |
    1 |   -     9     0     1
      |
    2 |  30     5     1   -30
      |
    3 |   1     4    -1    31
      |
    4 |   1     1     2   -61
    ------------------------------
    5 |   4     0    -9   275

    inv(9, 275) = -61 = 214
    
    -61 + 275 = 214
```

3. Comprobar
    - u[f] = a && v[f] = n
    - (x · a) mod n = 1
        - `(214 · 9) mod 275 = 1926 mod 275 = (7 · 275 + 1) mod 275 = 1`

### Algoritmo de exponenciación rápida

- `x = A^B mod n`
- Ejemplo: `x = 19^83 mod 91`
    1. Representación binaria:
        - 83 = 1010011
            - b[6] = 1
            - b[5] = 0
            - b[4] = 1
            - b[3] = 0
            - b[2] = 0
            - b[1] = 1
            - b[0] = 1
    2. Comienza como `x = 1`
        - Si b[i] = 1
            - `x^2 · A mod n`
        - Si b[i] = 0
            - `x^2 mod n`

|  i  |  b  |  x                |  x  |
| --- | --- | ----------------- | --- |
|  6  |  1  | `1^2 · 19 mod 91` |  19 |
|  5  |  0  |     `19^2 mod 91` |  88 |
|  4  |  1  | `1^2 · 19 mod 91` |  80 |
|  3  |  0  |     `19^2 mod 91` |  30 |
|  2  |  0  |     `19^2 mod 91` |  81 |
|  1  |  1  | `1^2 · 19 mod 91` |  80 |
|  0  |  1  | `1^2 · 19 mod 91` |  24 |

### Concepto de raíz primitiva

- Usado en Diffie Hellman y ElGamal
    - α = raíz primitiva o generador
    - Tomado como base y elevado a todos los número del cuerpo generan todos los números de ese cuerpo

- Raíces Raíces primitivas de 17 = {3, 5, 6, 7, 10,11, 12, 14}
    - Demostración de que 5 es raíz primitiva de 17
        - `5^0 mod 17 = 1`
        - `5^1 mod 17 = 14`
        - `5^2 mod 17 = 8`
        - `5^3 mod 17 = 6`
        - `5^4 mod 17 = 13`
        - `5^5 mod 17 = 14`
        - `5^6 mod 17 = 2`
        - `5^7 mod 17 = 10`
        - `5^8 mod 17 = 16`
        - `5^9 mod 17 = 12`
        - `5^10 mod 17 = 9`
        - `5^11 mod 17 = 11`
        - `5^12 mod 17 = 4`
        - `5^13 mod 17 = 3`
        - `5^14 mod 17 = 15`
        - `5^15 mod 17 = 7`
        - `5^16 mod 17 = 1`

## 8. Problemas matemáticos en la criptografía

Se usan para tener funciones en un solo sentido

### Problema de la Factorización Entera (PFE)

- Usado en el algoritmo RSA
- Se basa en que es fácil multiplicar dos primos entre sí
    - **pero** o muy difícil encontrar los factores primos que al multiplicarlos entre sí den el producto
- `p · q = n -> 113 · 113 = 14803`
    - Con números pequeños es fácil pero con números más grandes se complica
        - No hay un método para hacerlo, solo fuerza bruta
        - el tiempo necesario para obtener los factores crece de manea exponencial cuanto más grande sean los factores
            - En la practica es imposible romperlo
                - La computación cuántica puede que haga que eso cambie

### Problema del Logaritmo discreto (PLD)

- Utilizado en el algoritmo Diffie-Hellman
- Fácil hallar:
    - `β = α^x mod p`
- Calcular el logaritmo es fácil pero no en aritmética modular
    - `x = (log_α β) mod p`
    - Aun conociendo α, β y p, hallar x es computacionalmente intratable

## 9. Teoría de la información

### Concepto de entropía

- Mide el "desorden"
- Esta profundamente relacionado con la probabilidad
    - Distribución completamente igualitaria en el espacio de probabilidades => Entropía máxima

### Redundancia del lenguaje

- Concepto necesario al codificar
- No todas las letras del alfabeto se usan de igual manera
    - Si se quiere tener optimizado al máximo posible el espacio, al codificar se debe usar los códigos más cortos para los valores más usados, y viceversa

- ASCII no es nada optimo, utiliza 8 bits para cada carácter 2^8 = 256

- Español 27 letras (mayúsculas)
    - Supuestas equiprobables log_2 27 = 4,75 bits/letra (**ratio absoluto o R**)
        - 5 bits para todos los caracteres: 2^5 = 32 > 27
    - **Codificación óptima, r** Códigos cortos a las letras más frecuentes (codificación de Huffman)
        - r = 1,5 bits/letra
    - **Redundancia del lenguaje D(x)**:
        - `D(x) = R - r = 4.75 - 1.5 = 3.25`
        - `D(x) / R = 3.25 / 4.75 = 68.4%`
