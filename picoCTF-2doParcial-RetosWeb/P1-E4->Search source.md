# Objetivo

El desarrollador de este sitio web dejó por error un artefacto importante en la fuente del sitio web, ¿puedes encontrarlo?
El sitio web está aquí
1. ¿Cómo podría reflejar el sitio web en su máquina local para poder utilizar herramientas de búsqueda más potentes?
## Solución

```
──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/P2_RetosWeb]
└─$ httrack http://saturn.picoctf.net:59405/
Mirror launched on Wed, 03 Apr 2024 19:13:00 by HTTrack Website Copier/3.49-5 [XR&CO'2014]
mirroring http://saturn.picoctf.net:59405/ with the wizard help..
* saturn.picoctf.net:59405/js/jquery.mCustomScrollbar.concat.min.js (45479 bytes21/26: saturn.picoctf.net:59405/js/jquery.mCustomScrollbar.concat.min.js (0 byteDone.: saturn.picoctf.net:59405/images/fevicon.png (153 bytes) - 404
Thanks for using HTTrack!
                                                                                
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/P2_RetosWeb]
└─$ ls
backblue.gif  hts-cache    index.html
fade.gif      hts-log.txt  saturn.picoctf.net_59405
                                                                                
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/P2_RetosWeb]
└─$ cd saturn.picoctf.net_59405
                                                                                
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/P2_RetosWeb/saturn.picoctf.net_59405]
└─$ grep -R pico
css/style.css:/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7} **/
index-2.html:<!-- Mirrored from saturn.picoctf.net:59405/index.html by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 04 Apr 2024 01:13:26 GMT -->
index-2.html:<!-- Mirrored from saturn.picoctf.net:59405/index.html by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 04 Apr 2024 01:13:26 GMT -->
index.html:<!-- Mirrored from saturn.picoctf.net:59405/ by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 04 Apr 2024 01:13:03 GMT -->
index.html:<!-- Mirrored from saturn.picoctf.net:59405/ by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 04 Apr 2024 01:13:24 GMT -->
                                                                                
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/P2_RetosWeb/saturn.picoctf.net_59405]
└─$ 
```
Observamos en las coincidencias de la búsqueda con `grep`, la bandera del reto:
`picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7}`
## Notas adicionales

- `grep`->Nos ayudo como un "filtro" para buscar en un archivo o pagina, cierta palabra pues elimina la información inútil que no coincida con lo que le indiquemos. Se usa: `grep` + `caracter a buscar`.
- `httrack`-> Nos ayuda a descargar el contenido de un sitio web (o parte de el) para tenerlo de forma local en nuestro computador.
## Referencias

- https://www.httrack.com/