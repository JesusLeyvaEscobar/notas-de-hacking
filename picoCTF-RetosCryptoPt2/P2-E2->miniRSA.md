# Objetivo

Descifremos esto: ¿texto cifrado? Algo parece un poco pequeño.
1. RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
2. ¿Cómo podría tener una e demasiado pequeña afectar la seguridad de esta clave de 2048 bits?
3. Asegúrate de no perder precisión, los números son bastante grandes (aparte del valor e)
## Solución

Debemos descargar y analizar el archivo que nos proporciona el reto:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt2]
└─$ cat ciphertext

N: 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e: 3

ciphertext (c): 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125 
```
Retomando las notas anteriores respecto a RSA:
```
c - Texto cifrado
m - mensaje texto plano
p - primo 1
q - primo 2
n - modulo
tn - totient n (euler)
e - exponente (llave publica) 2^16~+1=65537
d - llave privada

n = p * q
tn = (p-1)*(q-1)
d = e mod inv tn / inverse(e,tn)

Encriptar	: c = m ^ e mod n / pow(m,e,n)
Desencriptar	: m = c ^ d mod n / pow(c,d,n)
```
Este problema, nos dice que debemos ver como es posible que un exponente tan pequeño (e=3) puede afectar la llave de seguridad de una llave de 2048 bits?. Debemos despejar la formula obtenida para encriptar, de la forma:
```
Encriptar	: c = m ^ e mod n / pow(m,e,n)
Desencriptar	: m = c ^ d mod n / pow(c,d,n)

c = m ^ e
c = m ^ 3
m = 3 raiz c
```
Para obtener solamente el mensaje en texto plano. Nos ayudaremos de python nuevamente para poder realizar las operaciones necesarias con precision, ayudandonos de librerias que manejan numeros grandes de alta precision:
```
┌──(jesus㉿KaliJesus)-[~]
└─$ python3
Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from gmpy2 import *
>>> from Crypto.Util.number import long_to_bytes
>>> 
>>> gmpy2.get_context().precision=2048
>>> 
>>> e = 3
>>> c = 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125
>>> root, exact = iroot(c, e)
>>> root
mpz(13016382529449106065894479374027604750406953699090365388202874238148389207291005)
>>> long_to_bytes(root)
b'picoCTF{n33d_a_lArg3r_e_606ce004}'
>>> 
```
Y, ademas usamos python para convertir el texto plano en la bandera que necesitamos encontrar.
## Notas adicionales

 `Algoritmo asimetrico`-> RSA (Rivest, Shamir y Adleman) es un sistema criptográfico de clave pública desarrollado en 1979, que utiliza factorización de números enteros. Es el primer y más utilizado algoritmo de este tipo y es válido tanto para cifrar como para firmar digitalmente.
## Referencias

- https://simple.wikipedia.org/wiki/RSA_algorithm