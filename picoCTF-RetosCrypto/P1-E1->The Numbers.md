# Objetivo

Los números... ¿qué significan?
1. La bandera tiene el formato PICOCTF{}
## Solución

Descargamos los datos que nos da el reto, y lo abrimos:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ ls                  
the_numbers.png

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ open the_numbers.png
```
En la imagen, vemos el formato de la bandera cifrado con números. Como la pista nos dice, la bandera tiene el formato picoCTF{}, vamos a ver que letras corresponden a cada numero que contiene al principio de la imagen:

picoCTF{???????????????} 
- p = 16
- i = 9
- c = 3
- o = 15
- C = 3
- t = 20
- f = 6

si lo analizamos, veremos que cada numero corresponde a la posición de su letra que representa en el abecedario. Entonces, vamos a sustituir cada numero por la letra que se encuentre en dicha posición.
Esto nos da como resultado: 

`picoCTF{thenumbersmason}`
## Notas adicionales

- Investigando, se trata del uso la decodificacion A1Z26.
## Referencias

