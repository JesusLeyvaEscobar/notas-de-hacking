# Objetivo

Ha llegado un segundo mensaje por correo y parece casi idéntico al primero. Quizás vuelva a funcionar lo mismo.
Descarga el mensaje aquí.
1. Prueba un ataque de frecuencia
2. ¿La puntuación y las palabras individuales te ayudan a realizar alguna sustitución?
## Solución

Analizando el archivo, encontramos nuevamente un texto cifrado pero en esta ocasión no nos da la el alfabeto de la llave para desencriptarlo.
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ cat message.txt.1
SYTe (eakdy tkd sjbyndr yar thjm) jdr j yobr kt skxbnyrd ersndzyo skxbryzyzkc. Skcyreyjcye jdr bdrercyrq gzya j ery kt sajhhrcmre gazsa yrey yarzd sdrjyzwzyo, yrsaczsjh (jcq mkkmhzcm) evzhhe, jcq bdklhrx-ekhwzcm jlzhzyo. Sajhhrcmre nenjhho skwrd j cnxlrd kt sjyrmkdzre, jcq garc ekhwrq, rjsa ozrhqe j eydzcm (sjhhrq j thjm) gazsa ze enlxzyyrq yk jc kchzcr eskdzcm erdwzsr. SYTe jdr j mdrjy gjo yk hrjdc j gzqr jddjo kt skxbnyrd ersndzyo evzhhe zc j ejtr, hrmjh rcwzdkcxrcy, jcq jdr akeyrq jcq bhjorq lo xjco ersndzyo mdknbe jdkncq yar gkdhq tkd tnc jcq bdjsyzsr. Tkd yaze bdklhrx, yar thjm ze: bzskSYT{TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS} 
```

Usaremos nuevamente una herramienta web para desencriptar pero en esta ocasión usaremos fuerza bruta para lograrlo, pues al no contar con una llave es un poco mas complejo pero no imposible.

El resultado fue el siguiente:
```
CTFS (SHORT FOR CAPTURE THE FLAG) ARE A TYPE OF COMPUTER SECURITY COMPETITION. CONTESTANTS ARE PRESENTED WITH A SET OF CHALLENGES WHICH TEST THEIR CREATIVITY, TECHNICAL (AND GOOGLING) SKILLS, AND PROBLEM-SOLVING ABILITY. CHALLENGES USUALLY COVER A NUMBER OF CATEGORIES, AND WHEN SOLVED, EACH YIELDS A STRING (CALLED A FLAG) WHICH IS SUBMITTED TO AN ONLINE SCORING SERVICE. CTFS ARE A GREAT WAY TO LEARN A WIDE ARRAY OF COMPUTER SECURITY SKILLS IN A SAFE, LEGAL ENVIRONMENT, AND ARE HOSTED AND PLAYED BY MANY SECURITY GROUPS AROUND THE WORLD FOR FUN AND PRACTICE. FOR THIS PROBLEM, THE FLAG IS: PICOCTF{FR3QU3NCY_4774CK5_4R3_C001_7AA384BC}
```
## Notas adicionales

- `Cifrado de sustitucion`->En criptografía, un cifrado de sustitución es un método de cifrado en el que unidades de texto sin formato se reemplazan con el texto cifrado, de una manera definida, con la ayuda de una clave;
## Referencias

- https://www.dcode.fr/monoalphabetic-substitution
- https://es.wikipedia.org/wiki/Cifrado_por_sustituci%C3%B3n
