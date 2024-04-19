# Objetivo

Encontramos este extraño mensaje transmitiéndose a los servidores, creemos que tenemos un esquema de descifrado que funciona.
Descarga el mensaje aquí.
Tome cada número mod 37 y asígnelo al siguiente conjunto de caracteres: 0-25 es el alfabeto (mayúscula), 26-35 son los dígitos decimales y 36 es un guión bajo.
Envuelva su mensaje descifrado en el formato de bandera picoCTF (es decir, `picoCTF{decrypted_message}`)
1. ¿Sabes qué significa mod 37?.
2. mod 37 significa módulo 37. Da el resto de un número después de dividirlo por 37.
## Solución

Analizando el archivo .txt que nos proporciona el reto, vemos que se trata de numeros a los cuales debemos hacerle mod 37. y al resultado, asignarlo segun nos dice en las indicaciones. Para esto, realizamos un pequeno programa en python el cual nos ayuda a realizar estas acciones sin tener que hacerla nosotros mismos una por una, boteniendo asi el siguiente codigo:
```
datos = open('message.txt').read().split()

print(datos)

flag = ''

for n in datos:
        c = int(n) % 37
        if c >= 0 and c <= 25:
                s = chr(c+65)
        elif c >= 26 and c <= 35:
                s = chr(c+22)
        else:
                s = '_'
        flag += s

print(f"picoCTF{{{flag}}}")
```
Luego de ejecutar el script, obtuvimos la bandera:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt3]
└─$ python3 exp.py 
['165', '248', '94', '346', '299', '73', '198', '221', '313', '137', '205', '87', '336', '110', '186', '69', '223', '213', '216', '216', '177', '138']
picoCTF{R0UND_N_R0UND_B6B25531}

```
## Notas adicionales

- `python3`-> Si invoca la versión de Python 3 directamente utilizando el comando python3 en lugar de python , se asegurará de que pip se instale en la ubicación adecuada, incluso si hay una versión anterior de Python en el sistema.
## Referencias

