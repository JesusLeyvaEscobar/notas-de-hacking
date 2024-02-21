
# Objetivo

Para obtener acceso al siguiente nivel, debe utilizar el binario setuid en el directorio de inicio. Ejecútelo sin argumentos para saber cómo usarlo. La contraseña para este nivel se puede encontrar en el lugar habitual (/etc/bandit_pass), después de haber utilizado el binario setuid.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit19**.
Contraseña: Encontrada en el nivel anterior: `awhqfNnAbc1naukrpqDYcF95h7HoMTrC`.

## Solución
```
bandit19@bandit:~$ 
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ls -la
total 36
drwxr-xr-x  2 root     root      4096 Oct  5 06:19 .
drwxr-xr-x 70 root     root      4096 Oct  5 06:20 ..
-rwsr-x---  1 bandit20 bandit19 14876 Oct  5 06:19 bandit20-do
-rw-r--r--  1 root     root       220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root      3771 Jan  6  2022 .bashrc
-rw-r--r--  1 root     root       807 Jan  6  2022 .profile
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
VxCazJaVykI6W36BkBU0mJTCM8rR95XT
bandit19@bandit:~$ 

```

## Notas adicionales

- `./bandit20-do cat /etc/bandit_pass/bandit20` ->Usamos el comando `cat` para mostrar el contenido del archivo que se encuentra en `/etc/bandit_pass/bandit20`. Ejecutamos los privilegios de administrador del usuario `bandit20` y por consiguiente nos muestra el contenido de ese archivo.
## Referencias

[setuid on Wikipedia](https://en.wikipedia.org/wiki/Setuid)
