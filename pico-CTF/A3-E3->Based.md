# Objetivo

Para obtener realmente 1337, debes comprender diferentes codificaciones de datos, como hexadecimal o binaria. ¿Puedes obtener la bandera de este programa para demostrar que estás en camino de convertirte en 1337? Conéctese con nc jupiter.challenges.picoctf.org 15130.
## Solución

```
chuyelhacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
pear
Please give the 01110000 01100101 01100001 01110010 as a word.
...
you have 45 seconds.....

Input:
pear
Please give me the  164 141 142 154 145 as a word.
Input:
table                  
Please give me the 636f6c6f7261646f as a word.
Input:
colorado
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}
^C
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

Nos dio una serie de datos en diferentes bases binarias, debíamos convertir según la base para obtener un carácter el cual debíamos ingresar para avanzar, para traducir estos datos usamos la ya confliable CybeChef.
## Referencias

https://gchq.github.io/CyberChef/