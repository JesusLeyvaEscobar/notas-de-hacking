
# Objetivo

Hay un binario setuid en el directorio de inicio que hace lo siguiente: establece una conexión con el host local en el puerto que especifica como argumento de la línea de comando. Luego lee una línea de texto de la conexión y la compara con la contraseña del nivel anterior (bandit20). Si la contraseña es correcta, transmitirá la contraseña para el siguiente nivel (bandit21).

NOTA: Intente conectarse a su propio demonio de red para ver si funciona como cree
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit20**.
Contraseña: Encontrada en el nivel anterior: `VxCazJaVykI6W36BkBU0mJTCM8rR95XT`.

## Solución
```
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Oct  5 06:19 .
drwxr-xr-x 70 root     root      4096 Oct  5 06:20 ..
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
-rwsr-x---  1 bandit21 bandit20 15600 Oct  5 06:19 suconnect
bandit20@bandit:~$ ./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.
bandit20@bandit:~$ nc -lnvp 6709 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
[1] 3065227
bandit20@bandit:~$ Listening on 0.0.0.0 6709

bandit20@bandit:~$ jobs
[1]+  Running                 nc -lnvp 6709 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT &
bandit20@bandit:~$ ./suconnect 6709
Connection received on 127.0.0.1 33910
Read: VxCazJaVykI6W36BkBU0mJTCM8rR95XT
Password matches, sending next password
NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
[1]+  Done                    nc -lnvp 6709 <<< VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit20@bandit:~$ 
```

## Notas adicionales

- `nc` -> Abre un servidor en el puerto que se le indique.
- `<<<` -> Usado para enviar la contraseña que queramos al servidor que se indico anteriormente.
- `&` -> Usado para ejecutar el servidor en segundo plano.
- `jobs` -> Verifica el estado de los trabajos, para confirmar que el servidor esta en ejecucion.
## Referencias

ssh, nc, cat, bash, screen, tmux, Unix ‘job control’ (bg, fg, jobs, &, CTRL-Z, …)