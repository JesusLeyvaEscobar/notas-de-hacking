# Objetivo

¿Este es un archivo de texto TXT realmente extraño? ¿Puedes encontrar la bandera?
1. ¿Cómo saben los sistemas operativos qué tipo de archivo es? (¡No es sólo el final!
2. Asegúrese de enviar la bandera como picoCTF{XXXXX}
## Solución

```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/extensions]
└─$ file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```
Una vez descargado lo analizamos con `file` y observamos como este archivo, a pesar de que su extensión es `.txt`, nos dice que es un tipo de archivo `PNG`.

```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/extensions]
└─$ xxd flag.txt | head
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 06a1 0000 0260 0802 0000 0085 ad5e  .......`.......^
00000020: 9a00 0000 0173 5247 4200 aece 1ce9 0000  .....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 0000 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f000 0026 9549 4441 5478 5eed dd6b  R$...&.IDATx^..k
00000060: 421b 39b7 05d0 3b2e 0694 f130 9a4c 2683  B.9...;....0.L&.
00000070: f9ae 5f80 4e3d 25bb 4cb3 f15a bfba a14a  .._.N=%.L..Z...J
00000080: 7574 2413 7927 c0ff fd0f 0000 0000 4826  ut$.y'........H&
00000090: e303 0000 0080 6c32 3e00 0000 00c8 26e3  ......l2>.....&.
```
Con la ayuda de los magic bytes, nos daremos cuenta de que en realidad, no se trata de un archivo .txt, sino que es un archivo PNG

Pues su primera linea contiene:
```
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```
Y en la lista de firmas de archivo que encontramos en Internet vemos lo siguiente:
```
|`89 50 4E 47 0D 0A 1A 0A`|`‰PNG␍␊␚␊`|0|png|Image encoded in the Portable Network Graphics|
```

Procedemos a cambiar la extensión de dicho archivo con el siguiente comando:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/extensions]
└─$ mv flag.txt flag.png

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/extensions]
└─$ open flag.png  
```
Y encontraremos una imagen que contiene la siguientencontrasena:
`picoCTF{now_you_know_about_extensions}`
``
## Notas adicionales

- `Formato de archivo`: Es una forma estándar en que la información es codificada y almacenada en un archivo de computadora. Ayuda a especificar como los bits son usados para codificar información en un almacenamiento digital.
- `Magic Bytes`: Bytes que identifican el tipo de archivo, un tipo de firma para saber que tipo de datos contiene el archivo.
- `xxd` -> Crea un volcado hexadecimal de un archivo.
- `mv`-> Usado para mover o renombrar archivos o directorios del sistema de archivos.
## Referencias

- https://en.wikipedia.org/wiki/File_format#:~:text=A%20file%20format%20is%20a,be%20either%20proprietary%20or%20free
- https://en.wikipedia.org/wiki/List_of_file_signatures