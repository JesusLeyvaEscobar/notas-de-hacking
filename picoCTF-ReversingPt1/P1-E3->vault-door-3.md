# Objetivo

Esta bóveda utiliza bucles for y matrices de bytes. El código fuente de esta bóveda está aquí: VaultDoor3.java
1. Cree una tabla que contenga cada valor de las variables del bucle y el índice de búfer correspondiente en el que escribe.
## Solución

Descargamos y le damos `cat` al archivo que del reto. Obtenemos lo siguiente:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ cat VaultDoor3.java                                            
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}

```
Es algo similar a los retos anteriores: El usuario ingresa una bandera con el formato `picoCTF`, el programa toma solamente la parte de adentro de la bandera. Esta parte la pasa como parámetro a la función `checkPassword` como parámetro `password`, donde checa que cumpla con ciertas características, después toma ciertas partes de la contraseña para meterlo a varios ciclos que verifican que esta contraseña cumpla con las restricciones de los ciclos para verificar que sea la correcta.

Para enfrentarnos a este reto nos auxiliaremos de la consola de javascript en nuestro navegador web Mozilla.

Una vez en la consola, vamos a almacenar el valor de la variable que se usa en el codigo fuente:
`var password = 'jU5s_a_sna_3lpm18g947_u_4_m9r54f';`
Luego, crearemos un buffer:
`var buffer = Awway(32);`
Despues, ponemos los ciclos que se describen en el codigo fuente, por los cuales pasan secciones de la bandera que ingreso el usuario, para comprobar que esta sea correta. Lo que se ingreso fue lo siguiente:
```
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i<17; i-=2) {
            buffer[i] = password.charAt(i);
        }
"g"
```
Ahora, solo vamos a ver que contiene el buffer, lo cual practicamente es la contrasena, pero vamos a usar `join` para unir estos caracteres y obtenemos el siguiente resultado:
```
buffer.join("")
"jU5t_a_s1mpl3_an4gr4m_4_u_79958f"
```
A esto, lo debemos ingresar entre los corchetes que contiene el formato de la bandera, para obtener nuestro resultado:
`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}`
## Notas adicionales


## Referencias

