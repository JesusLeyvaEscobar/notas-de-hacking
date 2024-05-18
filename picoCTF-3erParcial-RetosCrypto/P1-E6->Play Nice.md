# Objetivo

No todos los cifrados antiguos eran tan malos... La bandera no tiene el formato estándar. `nc mercury.picoctf.net 6057` playfair.py
## Solución

Al hacer la conexión al enlace que nos proporciona el reto, nos encontramos con lo siguiente:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ nc mercury.picoctf.net 6057                                   
Here is the alphabet: meiktp6yh4wxruavj9no13fb8d027c5glzsq
Here is the encrypted message: y7bcvefqecwfste224508y1ufb21ld
What is the plaintext message?    
```
De antemano, ya sabemos que este reto esta relacionado con el `Cifrado de PlayFair`, teniendo eso en cuenta ahora analizamos lo que encontramos:
Es un alfabeto con el cual vamos a trabajar como parte del esquema de cifrado de `PlayFairy` y también encontramos un mensaje encriptado que debemos decodificar ayudándonos del alfabeto.

Ahora, vamos a analizar el archivo llamado `playfair.py`, que nos proporciona el reto y esto es lo que encontramos:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ cat playfair.py
#!/usr/bin/python3 -u
import signal

SQUARE_SIZE = 6


def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

def encrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix)
	p2 = get_index(pair[1], matrix)

	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] + 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] + 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1)  % SQUARE_SIZE][p2[1]]
	else:
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def encrypt_string(s, matrix):
	result = ""
	if len(s) % 2 == 0:
		plain = s
	else:
		plain = s + "meiktp6yh4wxruavj9no13fb8d027c5glzsq"[0]
	for i in range(0, len(plain), 2):
		result += encrypt_pair(plain[i:i + 2], matrix)
	return result

alphabet = open("key").read().rstrip()
m = generate_square(alphabet)
msg = open("msg").read().rstrip()
enc_msg = encrypt_string(msg, m)
print("Here is the alphabet: {}\nHere is the encrypted message: {}".format(alphabet, enc_msg))
signal.alarm(18)
resp = input("What is the plaintext message? ").rstrip()
if resp and resp == msg:
	print("Congratulations! Here's the flag: {}".format(open("flag").read()))

# https://en.wikipedia.org/wiki/Playfair_cipher
```

Al principio del código, vemos un dato muy importante, el cual es el tamaño de la cuadricula, nos dice que es de 6.

Sabiendo esto, nos iremos a decodificar el texto con la ayuda de una herramienta en linea.
Ingresamos el mensaje encriptado, ajustamos la cuadricula a 6x6 e ingresamos el alfabeto. 
El resultado devuelto es:
`wd9bukbspdtj7skd3kl8d6oa3f03g0`

Este resultado lo ingresaremos en la parte del mensaje de texto plano que nos solicita para realizar la descripción. Entonces, aquí encontraremos nuestra bandera:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ nc mercury.picoctf.net 6057
Here is the alphabet: meiktp6yh4wxruavj9no13fb8d027c5glzsq
Here is the encrypted message: y7bcvefqecwfste224508y1ufb21ld
What is the plaintext message? wd9bukbspdtj7skd3kl8d6oa3f03g0
Congratulations! Here's the flag: 2e71b99fd3d07af3808f8dff2652ae0e

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ 
```
## Notas adicionales

- `Cifrado de Playfair`->El cifrado de Playfair es un método manual de criptografía simétrica por medio de sustitución. El sistema de cifrado toma pares de letras, o digramas, y las cambia mediante una tabla generada por una clave.
- `vi`+ `nombre del archivo`-> Abre o crea un archivo con ese nombre. 
## Referencias

- https://es.wikipedia.org/wiki/Cifrado_de_Playfair#:~:text=El%20cifrado%20de%20Playfair%20fue,lo%20promovi%C3%B3%20para%20uso%20militar.