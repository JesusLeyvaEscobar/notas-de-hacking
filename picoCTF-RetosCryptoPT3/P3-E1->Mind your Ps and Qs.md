# Objetivo

En RSA, un valor e pequeño puede ser problemático, pero ¿qué pasa con N? ¿Puedes descifrar esto? valores.
1. Los bits son caros, usé solo un poco más de 100 para ahorrar dinero.
## Solución

Si analizamos el archivo que descargamos en la liga que nos proporciona el reto, encontraremos lo siguiente:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt3]
└─$ ls
values

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt3]
└─$ cat values    
Decrypt my super sick RSA:
c: 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n: 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e: 65537  
```
Aquí, nos da los valores para `c`, `n` y `e`. Este reto, nos pide desencriptar el mensaje con los datos obtenidos. Por lo que iremos a nuestras notas que realizamos en los retos pasados sobre algoritmos simetricos.
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
Y vemos, que para desencriptar, necesitamos `c`, `d` y `n`. Ya tenemos 2 datos, pero nos falta `d` y para obtenerlo, debemos contar con `e` y `tn`, pero para nuestra mala suerte, solo contamos con el primer dato y aqui es donde radica el problema, pues para obtener `tn`, necesitamos 2 datos que son los números primos `p` y `q`. 

Sabemos de antemano que `n` es un valor pequeño, por lo que nos facilita mucho el trabajo de su factorizacion para poder obtener `p` y `q`. Usamos una herramienta en la web la cual nos ayudo a obtener estos 2 numero primos:
- `p = 1593021310640923782355996681284584012117`
- `q = 521911930824021492581321351826927897005221`
Con esto, pudimos realizar las operaciones necesarias para llegar a obtener `d`. Esto lo hicimos con la ayuda de `python3`.

```
┌──(jesus㉿KaliJesus)-[~]
└─$ python3
Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
>>> n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
>>> e = 65537
>>> p = 1593021310640923782355996681284584012117
>>> q = 521911930824021492581321351826927897005221
>>> from Crypto.Util.number import long_to_bytes
>>> from Crypto.Util.number import inverse
>>> tn = (p-1)*(q-1)
>>> d = inverse(e,tn)
>>> m = pow(c,d,n)
>>> long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_23540368}'
>>> 
```
## Notas adicionales

- `python3`-> Si invoca la versión de Python 3 directamente utilizando el comando python3 en lugar de python , se asegurará de que pip se instale en la ubicación adecuada, incluso si hay una versión anterior de Python en el sistema.
## Referencias

- http://factordb.com/