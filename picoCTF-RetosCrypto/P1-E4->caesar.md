# Objetivo

Descifre este mensaje.
1. tutorial de cifrado césar
## Solución

Descargamos, analizamos el tipo de archivo y lo abrimos, para notar que tenemos la clave con un cifrado parecido a ROT13
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ ls
ciphertext  table.txt  the_numbers.png
  
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ file ciphertext     
ciphertext: ASCII text, with no line terminators
   
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ cat ciphertext     
picoCTF{ynkooejcpdanqxeykjrbdofgkq} 
```
Vemos que tiene un cifrado en la parte que viene entre corchetes de la clave, con la ayuda de la liga a la que nos da en las notas, (el Cifrado Cesar), debemos analizar para saber cuantas rotaciones son necesarias para obtener una clave legible y saber si tenemos la contrasen correcta. 
En mi caso, en la rotacion 30 me aparecio el siguiente mensaje decodificado: `crossingtherubiconvfhsjkou`. Lo sustituimos en la parte que viene rotada dentro de las llaves de la bandera para ver si funciona.

`picoCTF{crossingtherubiconvfhsjkou} `
## Notas adicionales

- `rot13`-> ROT13 es un sencillo cifrado César utilizado para ocultar un texto sustituyendo cada letra por la letra que está trece posiciones por delante en el alfabeto. A se convierte en N, B se convierte en O y así hasta la M, que se convierte en Z.
## Referencias

- https://gchq.github.io/CyberChef/