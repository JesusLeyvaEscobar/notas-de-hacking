
# Objetivo

La contraseña para el siguiente nivel se almacena en el archivo `data.txt` en una de las pocas cadenas legibles por humanos, precedida por varios caracteres "=".

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit9**.
Contraseña: **Encontrada en el nivel anterior: `EN632PlfYiZbn3PhVK3XOGSlNInNE00t`.**

## Solución
```
bandit9@bandit:~$ 
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ file data.txt
data.txt: data
bandit9@bandit:~$ ls -la
total 40
drwxr-xr-x  2 root     root     4096 Oct  5 06:19 .
drwxr-xr-x 70 root     root     4096 Oct  5 06:20 ..
-rw-r--r--  1 root     root      220 Jan  6  2022 .bash_logout
-rw-r--r--  1 root     root     3771 Jan  6  2022 .bashrc
-rw-r-----  1 bandit10 bandit9 19379 Oct  5 06:19 data.txt
-rw-r--r--  1 root     root      807 Jan  6  2022 .profile
bandit9@bandit:~$ strings data.txt | grep "=="
x]T========== theG)"
========== passwordk^
========== is
========== G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
bandit9@bandit:~$ 
```

## Notas adicionales

- `strings` -> Extrae las cadenas de un archivo binario.
## Referencias

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
