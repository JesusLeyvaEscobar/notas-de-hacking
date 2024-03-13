# Objetivo

Encontramos este archivo. Recuperar la bandera.
1. Intente arreglar el encabezado del archivo.
## Solución

Como primer paso, descargamos y analizamos el tipo de archivo, asi como sus magic bytes:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/c0rrupt]
└─$ xxd mystery | head 
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..
```
Claramente, este archivo esta dañado, pero sabemos, por sus primeros bites, que el unico tipo de archivo que coincide con este, es el PNG. Sabiendo esto, intentaremos corregis sus primeros bytes para que coincidan con el tipo de archivo PNG y asi corregir este encabezado dañado. Esto lo realizaremos con un editor hexadecimal.

Este es el encabezado anterior:
```
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
```
Este es el nuevo encabezado:
```
00000000  89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  43 22 44 52   .PNG........C"DR
```

Aun después de esto, el programa todavía no se puede reconocer como un archivo PNG, por lo que ahora procederemos a reparar los chuncks dañados con el editor hexadeimal. Sabemos que el siguiente chunck debe de reconocerse como `IHDR`, por lo que editaremos el chunk poniendo su equivalente en hexadecimal.

Este es el encabezado anterior:
```
00000000  89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  43 22 44 52   .PNG........C"DR
```
Este es el nuevo encabezado:
```
00000000  89 50 4E 47  0D 0A 1A 0A   00 00 00 0D  49 48 44 52   .PNG........IHDR
```
Despues de esto, nuestro archivo ya es reconocido por el SO como un archivo PNG:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/c0rrupt]
└─$ file mystery
mystery: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
```
Pero al abrirlo, aun contiene errores, por lo que ahora usaremos una herramienta que verifica la integridad de los archivos PNG, para verificar que es lo que esta mal en este archivo.

```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/c0rrupt]
└─$ pngcheck -v mystery
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERRORS DETECTED in mystery
```
Nos dice, efectivamente hay errores de redundancia cíclica en el chunk `pHYs`, por lo que regresaremos al hexeditor para verificarlo.

Teníamos un error en las dimensiones de estas dimensiones, lo editamos.
```
00000040  00 09 70 48  59 73 00 00   16 25 00 00  16 25 01 49   ..pHYs...%...%.I
```
Ejecutamos nuevamente `pngckeck`:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/c0rrupt]
└─$ pngcheck -v mystery
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
:  invalid chunk length (too large)
ERRORS DETECTED in mystery
```
Observamos que aun tiene errores en el siguiente chunck. Despues de este chunck `pHYs`, viene el chunk `IDAT`.
```
00000050  52 24 F0 00  00 FF A5 49   44 41 54 78  5E EC BD 3F    R$.....IDATx^..?
```
Verificamos con hexeditor:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/c0rrupt]
└─$ pngcheck -v mystery
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 5669x5669 pixels/meter (144 dpi)
  chunk IDAT at offset 0x00057, length 65445
    zlib: deflated, 32K window, fast compression
  chunk IDAT at offset 0x10008, length 65524
  chunk IDAT at offset 0x20008, length 65524
  chunk IDAT at offset 0x30008, length 6304
  chunk IEND at offset 0x318b4, length 0
No errors detected in mystery (9 chunks, 96.3% compression).
```
Ya contamos con la imagen corregida, solo la abrimos y checamos la bandera.
## Notas adicionales

- `Magic Bytes`-> Bytes que identifican el tipo de archivo, un tipo de firma para saber que tipo de datos contiene el archivo.
- `Chunks`-> Después del encabezado, viene una serie de chunks, donde cada uno contiene cierta información acerca de la imagen.
- `xxd` -> Crea un volcado hexadecimal de un archivo.
- `pngcheck`-> Verifica la integridad de los archivos PNG.
## Referencias

- https://en.wikipedia.org/wiki/List_of_file_signatures
