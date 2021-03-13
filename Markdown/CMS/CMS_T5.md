# Tema 5: Algoritmos de cifra asimétrica

## 1. Generalidades de la cifra asimétrica

- Se usan diferentes claves para cifrar y descifrar
- Dos tipos de clave:
    - Clave privada
    - Clave pública
- Casos de uso
    - Confidencialidad
        - Alice -> Bob
        - Bob tiene clave publica
        - Alice se guarda esa clave
        - Alice cifra un mensaje con esa clave publica
        - Solo Bob puede descifrar ese mensaje
            - Usando su clave privada
    - Autenticación e integridad
        - Alice quiere firmar un mensaje
        - Alice firma el mensaje
            - Calcula el hash del mensaje y lo cifra con su clave privada
        - Alice envia el mensaje y el hash firmado
        - Bob coge ambas
            - Calcula el hash del mensaje
            - Descifra la firma (hash cifrado por Alice) con la clave pública
            - Comprueba que son iguales

## 2. Intercambio de clave de Diffie y Hellman

- Sirve para poder intercambiar una clave (secreto)
- Proceso:

1. Se escoge:
    - primo **p** y un generador **α** de primos públicos
2. A y B calculan y envían X
    - A genera un número aleatorio **a**
        - Envía → **X(a)**
            - `X(a) = α^a mod p`
    - B genera un número aleatorio **b**
        - Envía → **X(b)**
            - `X(b) = α^b mod p`
3. A y B calculan K
    - A calcula K
        - `K = X(b)^a mod p = α^(b·a) mod p`
    - B calcula K
        - `K = X(b)^b mod p = α^(a·b) mod p`
    - Ambos **tienen K**

- Ejemplo:
    - Se escoge:
        - Primo p = 4999
        - Generador α = 82
    - A genera número aleatorio 104 (a) y calcula X(a) = X(104)
        - `X(a) = α^a mod p = 82^104 mod 4999 = 4586`
        - Se lo envía a B
    - B genera numero aleatorio 52 (b) y calcula X(b) = X(52)
        - `X(b) = α^b mod p = 82^52 mod 4999 = 1488`
        - Se lo envía a A
    - A calcula K
        - `K = X(b)^a mod p = 1488^104 mod 4999 = (82^(52·104) mod 4999) = 3497`
    - B calcula K
        - `K = X(a)^b mod p = 4586^52 mod 4999 = (82^(104·52) mod 4999) = 3497`

## 3. El algoritmo RSA

## 4. El algoritmo de Elgamal

## 5. Ataques a RSA

## 6. Certificados digitales
