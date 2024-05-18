# Objetivo

Me pregunto qué es esto realmente... enc `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len( bandera), 2)])`
1. Puede encontrar algunos decodificadores en línea.

## Solución

Analizando los archivos obtenidos:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ file enc       
enc: Unicode text, UTF-8 text, with no line terminators

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ cat enc          
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ 
```

Con la pista que nos da el reto, iremos a nuestra herramienta ya confiable de descifrado `CyberChef`, para tratar de descifrar lo que nos dice el texto.

Usaremos la opción `Text Encoding Brute Focer` para poder realizar la decodificacion de este texto.
Obtenemos varias salidas, entre ellas vemos fácilmente la bandera:

`picoCTF{16_bits_inst34d_of_8_26684c20}`
## Notas adicionales

## Referencias

- https://gchq.github.io/CyberChef/