# Objetivo

¿Puedes descifrar este mensaje?
Descifre este mensaje usando esta clave "CYLAB".
1. https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
## Solución

Abrimos el archivo obtenido por el enlace anexado al reto:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ cat cipher.txt
rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}
```

Como nos dice el reto, este tipo de encriptado se trata del encriptado del `Vigenère cipher`, por lo que ahora usaremos una herramienta en linea que nos ayude a decifrar este tipo de cifrado con la ayuda de la clave quie nos proporciona el reto. 

El resultado es el siguiente:

`picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}`
## Notas adicionales

- `Cifrado Vigenère`->Método de cifrado de texto alfabético donde cada letra del texto plano se codifica con un cifrado César diferente, cuyo incremento está determinado por la letra correspondiente de otro texto, la clave.
## Referencias

- https://www.dcode.fr/chiffre-vigenere