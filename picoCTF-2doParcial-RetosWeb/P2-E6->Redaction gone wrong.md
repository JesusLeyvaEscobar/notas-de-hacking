# Objetivo

Ahora NO me ves.
Este informe contiene algunos datos críticos, algunos de los cuales han sido redactados correctamente, mientras que otros no. ¿Puedes encontrar una clave importante que no haya sido redactada correctamente?
1. ¿Cómo puede estar seguro de la redacción?
## Solución

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ open Financial_Report_for_ABC_Labs.pdf
```
Si intentamos abrir el archivo, observamos que se trata de un PDF con texto, el cual contiene algunas partes censuradas, pero que al seleccionarlas, podemos copiar los caracteres, los cuales son los siguientes:
```
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.
Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.
```
Así que, muy escondida la clave que digamos, pues no estaba jaja.
## Notas adicionales


## Referencias

