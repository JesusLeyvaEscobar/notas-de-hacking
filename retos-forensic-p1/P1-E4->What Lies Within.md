# Objetivo

Hay algo en el edificio. ¿Puedes recuperar la bandera?
1. Hay datos codificados en alguna parte... puede que haya un decodificador en línea.
## Solución

Realizamos los pasos que ya conocemos, analizar el tipo de archivo y abrirlo:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/whatlieswithin]
└─$ ls
buildings.png
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/whatlieswithin]
└─$ file buildings.png
buildings.png: PNG image data, 657 x 438, 8-bit/color RGBA, non-interlaced
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/whatlieswithin]
└─$ open buildings.png
```
Al abrirlo, notamos que efectivamente es una imagen pero que a simple vista no nos proporciona mas información relevante para resolver encontrar la bandera.

Usaremos un decodificador como herramienta en la consola,  en especifico la herramienta `zsteg`.

```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/whatlieswithin]
└─$ zsteg -a buildings.png | grep picoCTF
b1,rgb,lsb,xy       .. text: "picoCTF{h1d1ng_1n_th3_b1t5}"
```
Le decimos a la herramienta que use todas las tecnicas de decodificado que maneja, pero que la filtre para que muestre solamente la que nos de el resultado que coincida con `picoCTF`.
## Notas adicionales

- `Esteganografia`-> Es una técnica que implica ocultar información sensitiva dentro de un archivo o mensaje ordinario para que no sea detectado.
- `zsteg`-> Herramienta usada para detectar la estenografiara LSB solo en el caso de imagines PNG y BMP. 
## Referencias

- https://latam.kaspersky.com/resource-center/definitions/what-is-steganography
- https://wiki.bi0s.in/steganography/zsteg/