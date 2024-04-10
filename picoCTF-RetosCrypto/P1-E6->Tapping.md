# Objetivo

Hay golpecitos provenientes de los cables. ¿Qué dice `nc jupiter.challenges.picoctf.org 9422`?
1. ¿Qué tipo de codificación utiliza guiones y puntos?
2. La bandera tiene el formato PICOCTF{}
## Solución

Si entramos al en lace que nos da el reto, obtenemos:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ nc jupiter.challenges.picoctf.org 9422
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- } 

```
Las pistas, nos da indicios para pensar que este tipo de codificación es clave morse. entonces usaremos cyberchef para tratar de descifrarlo con `FROM MORSE CODE`.

Obtenemos el siguiente resultado:
- `PICOCTFM0RS3C0D31SFUN2683824610`
si lo acomodamos, segun nos indica la siguiente pista, obtenemos la bandera:
- `PICOCTF{M0RS3C0D31SFUN2683824610}`
## Notas adicionales

- `Clave morse`-> El código morse, también conocido como alfabeto morse o clave morse es un sistema de representación de letras y números mediante señales emitidas de forma intermitente.
## Referencias

- https://es.wikipedia.org/wiki/C%C3%B3digo_morse
- https://gchq.github.io/CyberChef/