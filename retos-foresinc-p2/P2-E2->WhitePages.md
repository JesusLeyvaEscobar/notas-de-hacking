# Objetivo

Dejé de usar YellowPages y pasé a WhitePages... ¡pero la página que me dieron está toda en blanco!
## Solución

Descargamos el archivo y analizamos que tipo de archivo es:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/whitepages]
└─$ file whitepages.txt
whitepages.txt: Unicode text, UTF-8 text, with very long lines (1376), with no line terminators

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/whitepages]
└─$ wc whitepages.txt             
   0    0 2982 whitepages.txt
```
Vemos que es un archivo unicode y vemos que su tamano es una sola linea con un tamano de 2982.

Mostraremos el contenido en hexadecimal del archivo, sus primeros 100 bytes:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/whitepages]
└─$ xxd -l 100 -g 1 whitepages.txt
00000000: e2 80 83 e2 80 83 e2 80 83 e2 80 83 20 e2 80 83  ............ ...
00000010: 20 e2 80 83 e2 80 83 e2 80 83 e2 80 83 e2 80 83   ...............
00000020: 20 e2 80 83 e2 80 83 20 e2 80 83 e2 80 83 e2 80   ...... ........
00000030: 83 e2 80 83 20 e2 80 83 e2 80 83 20 e2 80 83 20  .... ...... ... 
00000040: 20 20 e2 80 83 e2 80 83 e2 80 83 e2 80 83 e2 80    ..............
00000050: 83 20 20 e2 80 83 20 e2 80 83 e2 80 83 20 e2 80  .  ... ...... ..
00000060: 83 20 20 e2 
```
Nos dice que hay 2 tipos de caracteres, y observamos una secuencia que se repite: ``
`e2 80 83` después de que sale 4 veces, observamos un `20` y luego se vuelve a repetir, este `e2 80 82` representa un `SPACE` en la codificación unicode UT-8. Lo que haremos es convertir estas secuencias a 1 y 0 y convertir esa secuencia de binario a ascii y vemos que obtenemos.

Usamos el siguiente comando para reemplazar la secuencia de bytes por 0 y 1
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/whitepages]
└─$ sed 's/\xe2\x80\x83/0/g' whitepages.txt | sed 's/\x20/1/g'
00001010000010010000100101110000011010010110001101101111010000110101010001000110000010100000101000001001000010010101001101000101010001010010000001010000010101010100001001001100010010010100001100100000010100100100010101000011010011110101001001000100010100110010000000100110001000000100001001000001010000110100101101000111010100100100111101010101010011100100010000100000010100100100010101010000010011110101001001010100000010100000100100001001001101010011000000110000001100000010000001000110011011110111001001100010011001010111001100100000010000010111011001100101001011000010000001010000011010010111010001110100011100110110001001110101011100100110011101101000001011000010000001010000010000010010000000110001001101010011001000110001001100110000101000001001000010010111000001101001011000110110111101000011010101000100011001111011011011100110111101110100010111110110000101101100011011000101111101110011011100000110000101100011011001010111001101011111011000010111001001100101010111110110001101110010011001010110000101110100011001010110010001011111011001010111000101110101011000010110110001011111001100110110010100110010001101000011001000110011001100000011100000110001011001000110011000111001011000010110010001100001011000100011001001100001001110010110010000111001001101100110000101100110011001000110000100110100011000110110011001100001011001000011011001111101000010100000100100001001 
```
Ahora usaremos cyberchef para decoficar este dato binario y obtenemos esto de resultado:
```

		picoCTF

		SEE PUBLIC RECORDS & BACKGROUND REPORT
		5000 Forbes Ave, Pittsburgh, PA 15213
		picoCTF{not_all_spaces_are_created_equal_3e2423081df9adab2a9d96afda4cfad6}
```

## Notas adicionales

- `Unicode`-> Estándar de codificación de caracteres disenado para facilitar el tratamiento informático, transmisión y visualización de textos de numerosos idiomas y disciplinas técnicas.
- `sed`-> Permite reemplazar un carácter por otro. Tiene 3 partes:
	1. La primer parte te dice que vas hacer
	2. La segunda
## Referencias

- https://es.wikipedia.org/wiki/Unicode
- https://gchq.github.io/CyberChef/