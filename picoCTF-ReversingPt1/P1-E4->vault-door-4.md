# Objetivo

Esta bóveda utiliza codificación ASCII para la contraseña. El código fuente de esta bóveda está aquí: VaultDoor4.java
1. Utilice un motor de búsqueda para encontrar una "tabla ASCII".
2. También necesitarás saber la diferencia entre números octales, decimales y hexadecimales.
## Solución

Vemos que al analizar el archivo `.java` que se nos descargo usando el enlace que viene en la pagina del reto, observamos:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ cat VaultDoor4.java
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}
```
El programa, funciona con la misma ideología de retos anteriores: Espera una entrada del usuario con el formato de la bandera `picoCTF`, en donde toma el texto dentro de los corchetes para mandarlo a una función booleana de validación de password. Es en esta función donde radica la forma en que vamos a descubrir cual es la contraseña correcta que nos permitirá validar la entrada.

Vemos que tenemos diferentes codigos ASCII en decimal y hexadecimal, por lo que usaremos la función `String.fromCharCode()` para interpretar estos valores como códigos Unicode correspondientes. Luego, vemos que ya tenemos una sección con caracteres, estos solamente los vamos a juntar con los convertidos anteriormente. Nos ayudaremos de un join para quitar la separacion por comas de esta ultima linea de caracteres. Obtendremos como resultado, la parte interna de la bandera:
```
String.fromCharCode(106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146) + ['4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b'].join("")
"jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b"
```

Al final, solamente juntamos el resultado con el formato de la bandera que ya conocemos:
`picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}`
## Notas adicionales


## Referencias

