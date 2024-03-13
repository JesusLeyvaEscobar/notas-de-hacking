# Objetivo

Este jardín contiene más de lo que parece.
1. ¿Qué es un editor hexadecimal?
## Solución

Descargamos la imagen que nos proporciona el link del concurso, y con la terminal de Kali analizamos el tipo de archivo el cual es `garden.jpg` y con el hexeditor lo vamos a analizar.
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/gloryofthegarden]
└─$ ls
garden.jpg

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/gloryofthegarden]
└─$ file garden.jpg
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/gloryofthegarden]
└─$ open garden.jpg

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/gloryofthegarden]
└─$ hexeditor garden.jpg
```

Con la ayuda de los comandos del editor, presionamos CTRL + W para realizar una búsqueda en todo el código que nos arrojo el comando.

Seleccionamos la opción: `search for text strings` y enseguida, ingresamos las primeras letras con las que siempre comienza nuestra clave: `picoCTF`

00230560  72 65 20 69  73 20 61 20   66 6C 61 67  20 22 70 69                re is a flag "pi
00230570  63 6F 43 54  46 7B 6D 6F   72 65 5F 74  68 61 6E 5F               coCTF{more_than_
00230580  6D 33 33 74  73 5F 74 68   65 5F 33 79  33 65 42 64              m33ts_the_3y3eBd
00230590  42 64 32 63  63 7D 22 0A                                                            Bd2cc}".

Aquí nos encontramos con la bandera escondida en código hexadecimal, puesto que la primera letra de la bandera `p` equivale al `70` en hexa. De ahí en adelante, los siguientes códigos equivalen a la bandera.

La bandera final fue: `picoCTF{more_than_m33ts_the_3y3eBdBd2cc}`

## Notas adicionales

## Referencias

- https://es.wikipedia.org/wiki/Editor_hexadecimal
- 