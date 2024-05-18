# Objetivo

El código Morse es bien conocido. ¿Puedes descifrar esto?
Descargue el archivo aquí.
Envuelve tu respuesta con picoCTF{}, coloca guiones bajos en lugar de pausas y usa todo en minúsculas.
1. Audacity es un programa realmente bueno para analizar audio en código morse.
## Solución

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ ls
morse_chal.wav

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ file morse_chal.wav                         
morse_chal.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ 
```
Después de descargar y hacer un análisis básico del archivo, observamos que se trata de un archivo de audio. Pero si intentamos abrirlo, no nos dejara.

Usaremos la herramienta de audio que nos recomienda el reto: `Audacity`, para darnos cuenta que encontraremos espectros de patrones en código morse, por lo que usaremos otra herramienta web para descifrar código morse.

Esta herramienta nos ayuda a decodificar el mensaje oculto en codigo morse en el audio. El resultado obtenido fue el siguiente:
`WH47 H47H 90D W20U9H7`

Ahora, solamente lo vamos a adaptar al formato de la bandera para obtener el resultado final:
`picoCTF{WH47_H47H_90D_W20U9H7}`
## Notas adicionales

- `Codigo Morse`->El código morse, también conocido como alfabeto morse o clave morse es un sistema de representación de letras y números mediante señales emitidas de forma intermitente.
## Referencias

- https://morsecode.world/international/decoder/audio-decoder-adaptive.html
- https://es.wikipedia.org/wiki/C%C3%B3digo_morse