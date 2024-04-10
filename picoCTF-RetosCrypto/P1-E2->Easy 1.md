# Objetivo

El bloc de un solo uso puede ser criptográficamente seguro, pero no cuando se conoce la clave. ¿Puedes resolver esto? Le proporcionamos la bandera cifrada, la clave y una tabla para ayudar a `UFJKXQZQUNB` con la clave de `SOLVECRYPTO`. ¿Puedes utilizar esta tabla para resolverlo?.
1. Envíe su respuesta en nuestro formato de bandera. Por ejemplo, si su respuesta fue "hola", enviaría "picoCTF{HELLO}" como bandera.
2. Utilice todas las mayúsculas para el mensaje.
## Solución

Vemos el contenido del archivo txt que nos proporcionan en el reto:
```  
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ ls
ciphertext  table.txt  the_numbers.png
  
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ cat table.txt      
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
   +----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```
Vamos hacer un proceso de descripción, usando la tabla anterior, la llave y el texto cifrado, con la ayuda del cifrado de vigenere.
Vamos a buscar la letra que corresponda en la LLAVE (columnas), y que coincida con la letra equivalente en el texto CIFRADO (filas) y la letra que encontremos en esta interseccion, es la que debe ir en el texto plano.

LLAVE	        : S O L V E C R Y P T O
CIFRADO	: U F J K X Q Z Q U N B

PLANO	    : C R Y P T O I S F U N

Otra forma, es usando cyberchef, solo agregamos el algoritmo `Vigenere Decode` y listo. Obtenemos la clave: `CRYPTOISFUN`
Usamos las notas que nos deja el reto, para poder completar la clave:
`picoCTF{CRYPTOISFUN}`

## Notas adicionales

- `El cifrado Vigenère`: es un cifrado basado en diferentes series de caracteres o letras del cifrado César formando estos caracteres una tabla, llamada tabla de Vigenère, que se usa como clave. El cifrado de Vigenère es un cifrado polialfabético y de sustitución. El cifrado Vigenère se ha reinventado muchas veces.
## Referencias

- https://gchq.github.io/CyberChef/
- http://www.ugr.es/~anillos/textos/pdf/2012/EXPO-1.Criptografia/02a11.htm#:~:text=El%20cifrado%20Vigen%C3%A8re%20es%20un,se%20ha%20reinventado%20muchas%20veces.