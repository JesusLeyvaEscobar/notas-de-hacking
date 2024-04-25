# Objetivo

En el último desafío, dominaste los números octales (base 8), decimales (base 10) y hexadecimales (base 16), ¡pero esta puerta de bóveda utiliza un cambio de base y codificación de URL diferente! El código fuente de esta bóveda está aquí: VaultDoor5.java
1. Puede que le resulte útil una herramienta de codificación/descodificación, como https://encoding.tools/
2. Lea los artículos de Wikipedia sobre codificación de URL y codificación base 64 para comprender cómo funcionan y cómo se ven los resultados.
## Solución

Examinaremos el codigo fuente descargado desde el enlace que nos proporcionara el reto, obtendremos lo siguiente:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT1]
└─$ cat VaultDoor5.java
import java.net.URLDecoder;
import java.util.*;

class VaultDoor5 {
    public static void main(String args[]) {
        VaultDoor5 vaultDoor = new VaultDoor5();
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

    // Minion #7781 used base 8 and base 16, but this is base 64, which is
    // like... eight times stronger, right? Riiigghtt? Well that's what my twin
    // brother Minion #2415 says, anyway.
    //
    // -Minion #2414
    public String base64Encode(byte[] input) {
        return Base64.getEncoder().encodeToString(input);
    }

    // URL encoding is meant for web pages, so any double agent spies who steal
    // our source code will think this is a web site or something, defintely not
    // vault door! Oh wait, should I have not said that in a source code
    // comment?
    //
    // -Minion #2415
    public String urlEncode(byte[] input) {
        StringBuffer buf = new StringBuffer();
        for (int i=0; i<input.length; i++) {
            buf.append(String.format("%%%2x", input[i]));
        }
        return buf.toString();
    }

    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0";
        return base64Encoded.equals(expected);
    }
}
```
El programa, funciona con la misma ideología de retos anteriores: Espera una entrada del usuario con el formato de la bandera `picoCTF`, en donde toma el texto dentro de los corchetes para mandarlo a una función booleana de validación de password. Es en esta función donde radica la forma en que vamos a descubrir cual es la contraseña correcta que nos permitirá validar la entrada.

En este caso, la función que verifica la contraseña funciona, en una primera instancia, convirtiendo a bytes lo que ingreso el usuario para después mandarlo a una función llamada `urlEnconde`, la cual realiza una codificación para devolverlo y, de nueva cuenta, convertirlo a bytes y ahora codificarlo en base 64 para después compararse con otro texto ya declarado y también en base 64 para verificar que sea correcto.

Entonces, tenemos 2 codificaciones:
- `Codificacion URL`
- `Codificacion Base 64`

Lo que haremos primero, sera decodificarlo de base 64 y despues decodificacion url, obtendremos la bandera.

Para esto, nos ayudaremos de nuestra herramienta de decodifican: `CyberChef`:
Ingresaremos la cadena completa: 
`JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0`.

`CyberChef`, en automático detecta el tipo de decodificacion que tiene nuestro código, inclusive nos realiza las 2 decodificaciones de un solo movimiento.
Al final, obtenemos la siguiente salida:

`c0nv3rt1ng_fr0m_ba5e_64_e3152bf4`

A esto, lo complementamos con el formato de bandera habitual que ya conocemos para obtener:

- `picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}`

## Notas adicionales

- `Codificacion URL`-> Usada para cuando el navegador solicita al servidor WEB un URL, entonces lo hace con caracteres del conjunto de código ASCII, entonces cuando contiene caracteres que no pueden ser transmitidos deben ser convertidos a ASCII para poder ser enviados como parte del URL. Entonces, cada carácter se convierte a una representación de 2 números hexadecimales precedidos de un signo %.
## Referencias

- https://www.w3schools.com/html/html_links.asp
- https://gchq.github.io/CyberChef/