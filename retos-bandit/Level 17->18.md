
# Objetivo

Hay 2 archivos en el directorio de inicio: contraseñas.antiguas y contraseñas.nuevas. La contraseña para el siguiente nivel está en contraseñas.nueva y es la única línea que se ha cambiado entre contraseñas.antiguas y contraseñas.nuevas.

NOTA: si has resuelto este nivel y ves "¡Adiós!" al intentar iniciar sesión en bandit18, esto está relacionado con el siguiente nivel, bandit19.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit17**.
Contraseña: Encontrada en el nivel anterior: `Archivo guardado como TheKey`.

## Solución
```
┌──(jesus㉿KaliJesus)-[~]
└─$ ssh -i TheKey bandit17@bandit.labs.overthewire.org -p 2220 

bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ ls -la
total 36
drwxr-xr-x  3 root     root     4096 Oct  5 06:19 .
drwxr-xr-x 70 root     root     4096 Oct  5 06:20 ..
-rw-r-----  1 bandit17 bandit17   33 Oct  5 06:19 .bandit16.password
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit18 bandit17 3300 Oct  5 06:19 passwords.new
-rw-r-----  1 bandit18 bandit17 3300 Oct  5 06:19 passwords.old
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
drwxr-xr-x  2 root     root     4096 Oct  5 06:19 .ssh
bandit17@bandit:~$ wc -l passwords.old
100 passwords.old
bandit17@bandit:~$ wc -l passwords.new
100 passwords.new
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< p6ggwdNHncnmCNxuAt0KtKVq185ZU7AW
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
bandit17@bandit:~$ diff passwords.old passwords.new --color
42c42
< p6ggwdNHncnmCNxuAt0KtKVq185ZU7AW
---
> hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
bandit17@bandit:~$ 



```

## Notas adicionales

- `diff` -> Comando usado para comparar el contenido de dos archivos.
## Referencias

cat, grep, ls, diff