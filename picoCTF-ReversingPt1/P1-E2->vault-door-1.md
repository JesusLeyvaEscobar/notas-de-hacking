# Objetivo

¡Esta bóveda utiliza algunas matrices complicadas! Espero que pueda entenderlo, agente especial. El código fuente de esta bóveda está aquí: VaultDoor1.java
1. Busque el método charAt() en línea.
## Solución

Descargamos y analizamos el archivo .java que nos proporciono el reto.
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ cat VaultDoor1.java         
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
	String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
}
```
Observamos, que pasa algo similar al programa anterior, en donde tenemos un programa principal que verifica una entrada del usuario y dicha entrada es verificada por una función que, en esta caso, contiene la contraseña separada por caracteres, enumerados y revueltos,

Lo que haremos, sera guardar en un archivo de texto estos caracteres enumerados que conforman la contraseña, para posterior, con ayuda de algunos comandos, podremos ordenar y extraer solamente el carácter necesario

Empezaremos:
- `cat`-> Este comando, ya conocido, nos ayuda a leer el archivo de texto, en el cual almacenamos la parte del código fuente que contiene la contraseña.
- `sort`-> Nos ayudara a ordenar las lineas de entrara en orden alfabético. En nuestro caso, ordenara las lineas de forma descendente. 
- `awk`-> Nos ayudara a procesar el texto, y agregaremos la condicion: `{print($3)}`,  el cual nos ayudara mostrar el tercer campo de cada linea. En otras palabras, mostrara la tercer palabra de cada linea del archivo, pues esta es la posicion en la que se encuentra el caracter deseado de la bandera.
- `tr`-> Es un comando similar al anterior, solo que este elimina el caracter que se le indique, en este caso ingresaremos `-d "\n"` para que quite el caracter del enter (\n) o el salto de linea, para poder observar la bandera en una sola linea.

El comando completo, es el siguiente:
`cat bandera | sort | awk '{print($3)}' | tr -d "'" | tr -d "\n"`

Al final obtuvimos el resultado:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ cat bandera | sort | awk '{print($3)}' | tr -d "'" | tr -d "\n"
d35cr4mbl3_tH3_cH4r4cT3r5_75092e  
```
El resultado, lo debemos aunar al comienzo de la bandera que ya conocemos: `picoCTF{` y obtenemos como resultado:

- `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}`
## Notas adicionales


## Referencias

https://www.w3schools.com/java/ref_string_charat.asp