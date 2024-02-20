
# Objetivo

La contraseña para el siguiente nivel se almacena en el archivo data.txt, que contiene datos codificados en base64.

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit10**.
Contraseña: **Encontrada en el nivel anterior: `G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s`.**

## Solución
```
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIDZ6UGV6aUxkUjJSS05kTllGTmI2blZDS3pwaGxYSEJNCg==
bandit10@bandit:~$ cat data.txt | 64 -d
64: command not found
bandit10@bandit:~$ cat data.txt | base64 -d
The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
bandit10@bandit:~$ 

```

## Notas adicionales

- `nombre del archivo | base -d` -> Codifica de base64 para poder leer un texto codificado en base64
- `base64 -d nombre del archivo` -> Otra forma de codificar cualquier texto/archivo en base64
## Referencias

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
[Base64 on Wikipedia](https://en.wikipedia.org/wiki/Base64)

