# Objetivo

¿Puedes encontrar la bandera en el archivo sin ejecutarla?
1. [strings](https://linux.die.net/man/1/strings)

## Solución

```
chuyelhacker-picoctf@webshell:~$ ls
README.txt
chuyelhacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
--2024-02-28 05:26:36--  https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 776032 (758K) [application/octet-stream]
Saving to: 'strings'

strings                           100%[==========================================================>] 757.84K  1.86MB/s    in 0.4s    

2024-02-28 05:26:37 (1.86 MB/s) - 'strings' saved [776032/776032]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  strings
chuyelhacker-picoctf@webshell:~$ strings strings | grep 'pico'
picoCTF{5tRIng5_1T_d66c7bb7}
chuyelhacker-picoctf@webshell:~$ 

```

## Notas adicionales

- `strings`->
- `grep`->
## Referencias

https://linux.die.net/man/1/strings