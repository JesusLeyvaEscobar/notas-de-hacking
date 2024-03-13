# Objetivo

Decodifica este mensaje de la luna.
1. ¿Cómo se enviaron a la Tierra las imágenes del alunizaje?
2. ¿Cuál es la mascota de CMU?, eso podría ayudar a seleccionar una opción de RX.
## Solución

Descargamos el archivo y analizamos que tipo de archivo es:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/m00nwalk]
└─$ ls
message.wav
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/m00nwalk]
└─$ file message.wav
message.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz
```
Nos guiaremos de las notas que contiene el reto, para poder resolverlo. Con la primera nota sabemos que el audio esta codificado con `SSTV`, entonces lo primero que debemos de hacer es usar un decodificador en linea, encontraremos uno en github
En este repositorio, vemos que podemos decodificar en las 3 variantes de la codificacion SSTV:
```
- Martin 1, 2
- Scottie 1, 2, DX
- Robot 36, 72
```
La segunda pista nos dice que tipo de codificacion estan usando, en este caso es la `Sctorrie 1,2,DX`. Ahora procedemos a instalar esta herramienta de GItHub con los comandos de ayuda, desde el directorio `opt`:
```
$ git clone https://github.com/colaclanth/sstv.git

$ sudo python3 setup.py install
```
 Una vez instalado, regresamos a nuestro directorio donde esta el archivo y lo vamos a ejecutar:
```
 ┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/m00nwalk]
└─$ ls
message.wav

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/m00nwalk]
└─$ sstv -d message.wav -o result.png 
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...   [##############################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!
```
Listo, no queda es verificar que se decodifico y creo el archivo final:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/m00nwalk]
└─$ ls
message.wav  result.png

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/m00nwalk]
└─$ open result.png
```
Al abrir la imagen, obtenemos la bandera:
`picoCTF{beep_boop_im_in_space}`
## Notas adicionales

- `sstv`-> Usamos un repositorio para ejecutar esta herramienta de de-codificación SSTV, en este le vamos a indicar con `-d` el nombre del archivo que esta codificado y en seguida, con `-o` el nombre que tomara el archivo final con la de-codificacion.
## Referencias

- https://github.com/colaclanth/sstv
