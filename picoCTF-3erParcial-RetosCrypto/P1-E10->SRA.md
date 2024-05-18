# Objetivo

Hace poco me enteré del criptosistema de clave pública SRA... o espera, ¿se suponía que era RSA? Hmmm, probablemente debería comprobarlo...
Detalles adicionales estarán disponibles después de lanzar su instancia de desafío.
## Solución

Usaremos un script que nos ayudara a descifrar los datos encriptados que nos proporciona la conexion al servidos que nos da el reto. Llame a este script `RSA` y su codigo es el siguiente:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ cat RSA.py
from pwn import *
import primefac
from itertools import combinations
from Crypto.Util.number import long_to_bytes

def sub_lists (l):
    comb = []

    for i in range(1,len(l)+1):
        comb += [list(j) for j in combinations(l, i)]
    return comb

def divisors(phi):
   print("Dame los divisores de ", phi-1)
   return(eval(input()))


r = remote('saturn.picoctf.net', 57732)

r.recvuntil("anger =")
ciphertext=int(r.recvline())

r.recvuntil("envy =")
d=int(r.recvline())
print("cipher=",ciphertext)
print("d=",d)
print(r.recvuntil("vainglory?"))
r.recvline()

factors=divisors(d*65537)
combos = sub_lists(factors)
primes = set()

for l in combos:
   product = 1
   
   for k in l:
      product = product * k
   
   if product.bit_length()==128 and primefac.isprime(product+1):
      primes.add(product+1)
print(primes)
primelist = list(primes)

for p in primelist:
   for q in primelist:
      n=p*q

      plain = pow(ciphertext,d,n)
      try:
         plaintext = long_to_bytes(plain)
         print(plaintext.decode())
         r.sendline(plaintext.decode())
         print(r.recvline())
         print(r.recvline())
         print(r.recvline())
      except:
         continue
                 
```

Hace la conexión directa al puerto del servidor, y almacena los datos del texto cifrado, d y lo unico que tenemos que hacer, es ayudarlo con los divisores de un numero que nos proporciona para que asi pueda hacer uso de fuerza bruta intentando descifrar el mensaje.

Nos ayudamos de una pagina web que obtiene numeros primos fatorizando el dato.
Luego de correr el script, e ingresar los datos que nos pide, obtenemos el siguiente resultado:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ python3 RSA.py
[+] Opening connection to saturn.picoctf.net on port 57732: Done
/home/jesus/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto/RSA.py:20: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.recvuntil("anger =")
/home/jesus/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto/RSA.py:23: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.recvuntil("envy =")
cipher= 36488046745037732668124177753437187229993677282078503905826318517788748861873
d= 37056448673173501462887952471478107678871037453288900040674951983864405077721
/home/jesus/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto/RSA.py:27: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  print(r.recvuntil("vainglory?"))
b'vainglory?'
Dame los divisores de  2428568476693771765373287741123260742950171181576194641965714328166521515578601176
[2, 2, 2, 3, 7, 7, 23, 31, 1847, 3709, 4091, 5147, 27731273, 541920257, 2986387586967959018287, 447398745594195402330541]
{236270994660423754555304841487598328907, 240646035965749089842106056032497303127, 179519386174746856030250933119171132829, 291613051369216744675865529182144927899}
FhYe9V6R5bfuaJml
/home/jesus/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto/RSA.py:53: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  r.sendline(plaintext.decode())
b'> FhYe9V6R5bfuaJml\r\n'
b'Conquered!\r\n'
b'picoCTF{7h053_51n5_4r3_n0_m0r3_ba95c657}\r\n'
FhYe9V6R5bfuaJml
[*] Closed connection to saturn.picoctf.net port 57732
```

## Notas adicionales

Cabe mencionar, que el script no es propio si no que fue rescatado de la web, anexando en las referencias.
## Referencias

- https://www.youtube.com/watch?v=3DPWLnrqHZ0