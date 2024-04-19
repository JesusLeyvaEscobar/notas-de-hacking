# Objetivo

¿Qué tal un poco de escondite?
Mira esta imagen aquí.
1. Descarga la imagen e intenta extraerla.
## Solución

Lo primero va a ser descargar el archivo que nos proporcionan en el reto. Cuando lo abrimos vemos que se trata de una imagen referente al cifrado Atbash. 
Si observamos la descripción del reto, sabemos que debemos extraer información que aparentemente viene oculta en esta imagen con extensión `jpg`. Sabemos que a la acción de ocultar información en imágenes y audio le llaman esteganografia. En este caso, usaremos la herramienta `StegHide` para poder extraer la información oculta en esta imagen.
Primero, vamos a instalar la herramienta en nuestro sistema, con la ayuda del siguiente comando:
- `sudo apt-get install steghide -y`
Ahora, una vez en el directorio vamos realizar los siguientes pasos:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt3]
└─$ steghide extract -sf atbash.jpg          
Anotar salvoconducto: 
anoto los datos extraidos e/"encrypted.txt".

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt3]
└─$ ls
atbash.jpg  encrypted.txt  exp.py  message.txt  scrambled1.png  scrambled2.png  values

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt3]
└─$ cat encrypted.txt
krxlXGU{zgyzhs_xizxp_92533667}
```
Si vemos el contenido en el texto extraído, se trata de un texto similar a la bandera. Ahora, recordando un poco lo que encontramos en la imagen, podemos deducir que, probablemente, este texto se encuentra cifrado en `Atbash`, por lo que veremos si nuestra ya confiable herramienta `CyberChef` nos ayuda a descifrar el texto.
Busquemos `Atbash` en `CyberCheg` y efectivamente, encontramos `Atbash Cipher` y en la entrada, ingresamos el texto extraído de la imagen y nuestra salida encontramos la bandera:
- `picoCTF{atbash_crack_92533667}'
## Notas adicionales

- `Steghide`-> Es una herramienta de esteganografía que permite ocultar información en imágenes y audio.
- `Atbash`-> Es un método muy común de cifrado del alfabeto hebreo. Pertenece a la llamada criptografía clásica y es un tipo de cifrado por sustitución. Se le denomina también método de espejo, pues consiste en sustituir la primera letra por la última, la segunda por la penúltima y así sucesivamente.
- `sudo apt-get install steghide -y`-> Comando para instalar la herramienta `StegHide` mediante la terminal de comandos en Linux.
## Referencias

- https://daniellerch.me/stego/intro/tools-es/#steghide
- https://es.wikipedia.org/wiki/Atbash
- https://www.geeksforgeeks.org/how-to-install-steghide-tool-in-linux/
- https://gchq.github.io/CyberChef/