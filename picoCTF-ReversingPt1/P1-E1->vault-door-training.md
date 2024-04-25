# Objetivo

Tu misión es ingresar al laboratorio del Dr. Evil y recuperar los planos de su Proyecto Doomsday. El laboratorio está protegido por una serie de puertas de bóveda cerradas con llave. Cada puerta está controlada por una computadora y requiere una contraseña para abrirse. Desafortunadamente, nuestros agentes encubiertos no han podido obtener las contraseñas secretas de las puertas de las bóvedas, ¡pero uno de nuestros agentes junior obtuvo el código fuente de la computadora de cada bóveda! Deberá leer el código fuente de cada nivel para descubrir cuál es la contraseña para la puerta de esa bóveda. Como calentamiento, hemos creado una réplica del salto en nuestras instalaciones de entrenamiento. El código fuente de la bóveda de entrenamiento está aquí: VaultDoorTraining.java
1. La contraseña se revela en el código fuente del programa.
## Solución

Descargamos el archivo que contiene el enlace que nos proporciona el reto, para después analizarlo, como nos dice en la pista 1. Se trata del código fuente de un programa que se realizo en Java.
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ ls
VaultDoorTraining.java

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ cat VaultDoorTraining.java           
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
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

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");
    }
}

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ 
```
Si analizamos el código, observamos que este código fuente lee una entrada del usuario, la cual, comienza con `picoCTF{` y valida esta entrada según lo que ingrese el usuario para dar acceso o negarlo en caso de que la contraseña sea incorrecta. Dicha entrada/contraseña la manda a otra función llamada `checkPassword`, esta función contiene la contraseña correcta así que aquí solo verifica que sea la misma y regresa un valor booleano verdadero o falso.

Si juntamos estos 2 valores, la parte de la entrada que contiene picoCTF{ con la contraseña de la función `checkPassword`, obtendremos la bandera para completar el reto.

Bandera: `picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}`
## Notas adicionales


## Referencias

