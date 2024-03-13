# Objetivo

Encuentra la bandera en esta imagen.
1. ¿Qué significa meta en el contexto de los archivos?
2. ¿Has oído hablar alguna vez de los metadatos?
## Solución

Realizamos las acciones normales, descargamos el archivo proporcionado, analizamos el tipo de archivo y despues lo abrimos para ver su contenido:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/someta]
└─$ ls
pico_img.png
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/someta]
└─$ file pico_img.png
pico_img.png: PNG image data, 600 x 600, 8-bit/color RGB, non-interlaced
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/someta]
└─$ open pico_img.png
```
El archivo, visualmente no proporciona información acerca de la bandera para resolver el problema.
Lo que haremos, sera analizar los metadatos de este archivo con la herramienta de la linea de comandos `ExifTool`.

```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/someta]
└─$ exiftool pico_img.png
ExifTool Version Number         : 12.67
File Name                       : pico_img.png
Directory                       : .
File Size                       : 109 kB
File Modification Date/Time     : 2020:10:26 12:38:23-06:00
File Access Date/Time           : 2024:03:13 00:42:24-06:00
File Inode Change Date/Time     : 2024:03:13 00:42:08-06:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 600
Image Height                    : 600
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Software                        : Adobe ImageReady
XMP Toolkit                     : Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27
Creator Tool                    : Adobe Photoshop CS6 (Windows)
Instance ID                     : xmp.iid:A5566E73B2B811E8BC7F9A4303DF1F9B
Document ID                     : xmp.did:A5566E74B2B811E8BC7F9A4303DF1F9B
Derived From Instance ID        : xmp.iid:A5566E71B2B811E8BC7F9A4303DF1F9B
Derived From Document ID        : xmp.did:A5566E72B2B811E8BC7F9A4303DF1F9B
Warning                         : [minor] Text/EXIF chunk(s) found after PNG IDAT (may be ignored by some readers)
Artist                          : picoCTF{s0_m3ta_eb36bf44}
Image Size                      : 600x600
Megapixels                      : 0.360
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/someta]
└─$ 
```
Aqui vemos en los detalles, en el apartado `Artist`, la bandera que necesitaremos.
## Notas adicionales

- `Metadatos`-> Son datos que proporcionan información acerca de otros datos, pero no el contenido de esos otros datos. Ayudan al usuario a encontrar información relevante y descubrir recursos.
- `ExifTool`-> Una biblioteca de Perl, para trabajar con meta datos desde la linea de comandos.
- Me pareció muy interesante saber como hay mas allá que los datos del archivo para saber que contiene, desconocía del todo esta parte de un archivo, como lo son los meta datos
## Referencias

- https://es.wikipedia.org/wiki/Metadatos