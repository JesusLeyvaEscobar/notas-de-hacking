# Objetivo

Los atacantes han ocultado información en una gran masa de datos en el pasado, tal vez todavía lo estén haciendo.
Descarga los datos aquí.
1. Descargue el archivo y busque la bandera según el prefijo conocido.
## Solución

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ wget https://artifacts.picoctf.net/c/126/anthem.flag.txt 
--2024-04-04 23:11:08--  https://artifacts.picoctf.net/c/126/anthem.flag.txt
Resolviendo artifacts.picoctf.net (artifacts.picoctf.net)... 13.249.21.66, 13.249.21.85, 13.249.21.46, ...
Conectando con artifacts.picoctf.net (artifacts.picoctf.net)[13.249.21.66]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 108668 (106K) [application/octet-stream]
Grabando a: «anthem.flag.txt»

anthem.flag.txt              100%[============================================>] 106.12K   611KB/s    en 0.2s    

2024-04-04 23:11:09 (611 KB/s) - «anthem.flag.txt» guardado [108668/108668]

                                                                                                                  
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ ls
 anthem.flag.txt          'P1-E3->Local Authority.md'  'P1-E9->SQL Direct.md'
 cat.jpg                  'P1-E4->Search source.md'    'P2-E1->information.md'
 drawing.flag.svg         'P1-E5->Forbidden Paths.md'  'P2-E2->Wireshark doo dooo do doo....md'
'P1-E1->Includes.md'      'P1-E6->Power Cookie.md'     'P2-E3->Enhance!.md'
'P1-E2->Inspect HTML.md'  'P1-E7->Roboto Sans.md'      'P2-E4->Lookey here.md'
'P1-E2->.md'              'P1-E8->Secrets.md'           shark1.pcapng
                                                                                                                  
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ cat anthem.flag.txt                                                
      ANTHEM
      by Ayn Rand

        CONTENTS
         PART ONE
         PART TWO
         PART THREE
         PART FOUR
         PART FIVE
         PART SIX
         PART SEVEN
         PART EIGHT
         PART NINE
         PART TEN
         PART ELEVEN
         PART TWELVE

      PART ONE

      It is a sin to write this. It is a sin to think words no others
      think and to put them down upon a paper no others are to see. It
      is base and evil. It is as if we were speaking alone to no ears
      but our own. And we know well that there is no transgression
      blacker than to do or think alone. We have broken the laws. The
      laws say that men may not write unless the Council of Vocations
      bid them so. May we be forgiven!
...
      And here, over the portals of my fort, I shall cut in the stone
      the word which is to be my beacon and my banner. The word which
      will not die, should we all perish in battle. The word which can
      never die on this earth, for it is the heart of it and the
      meaning and the glory.

      The sacred word:
      EGO
```

Al analizarlo, nos damos cuenta que es muchísima información la que contenía este archivo, así que vamos a realizar un filtro en nuestro análisis, con `grep` y que solo nos muestre información que coincida con `pico`:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ cat anthem.flag.txt | grep 'pico'
      we think that the men of picoCTF{gr3p_15_@w3s0m3_2116b979}
    
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ 
```
Listo, si se encuentra la bandera en todos estos datos del archivo.
## Notas adicionales

- `cat`-> Usado para crear o mostrar el contenido de archivos existentes.
- `grep`-> Lee la entrada estándar o una lista de archivos, e imprime las líneas que contengan coincidencias para la expresión regular.
## Referencias

