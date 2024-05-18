# Objetivo

¿Qué significan las banderas?
1. La bandera tiene el formato PICOCTF{}
## Solución

Al analizar el archivo que nos descarga el enlace anexado al reto, vemos lo siguiente:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ file flag.png      
flag.png: PNG image data, 1642 x 1095, 8-bit/color RGB, non-interlaced
 
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ open flag.png  
```

No es mas que un archivo PNG, que al abrirlo nos damos cuenta que son banderas acomodadas, algunas entre corchetes lo que nos da a entender que se trata de algun codigo que representa cada bandera.

Investigando en la web, me percato que existe un codigo llamado: `Codigo internacional de banderas`. Buscamos el significado de cada bandera para representarlo a manera de texto y asi intentar obtener la bandera.

El resultado, después de representar con caracteres cada bandera, es:
`picoCTF{f1ag5and5tuff}`
## Notas adicionales

- `Codigo internacional de banderas`->Las banderas, insignias y distintivas tienen la forma de cuadra, corneta, gallardete o gallardetón.
## Referencias

- https://www.gob.mx/cms/uploads/attachment/file/2949/C_digo_Internacional_de_Banderas.pdf