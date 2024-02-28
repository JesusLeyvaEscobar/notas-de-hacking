# Objetivo

¿Puedes encontrar la bandera en el archivo? Sería muy tedioso revisar esto manualmente, algo me dice que hay una manera mejor.

## Solución

```
chuyelhacker-picoctf@webshell:~$ ls
README.txt
chuyelhacker-picoctf@webshell:~$ wget https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file
--2024-02-28 04:56:30--  https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file
Resolving jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)... 3.131.60.8
Connecting to jupiter.challenges.picoctf.org (jupiter.challenges.picoctf.org)|3.131.60.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14551 (14K) [application/octet-stream]
Saving to: 'file'

file                              100%[==========================================================>]  14.21K  --.-KB/s    in 0s      

2024-02-28 04:56:30 (345 MB/s) - 'file' saved [14551/14551]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  file
chuyelhacker-picoctf@webshell:~$ cat file | grep 'pico'
picoCTF{grep_is_good_to_find_things_f77e0797}
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `grep`->

## Referencias

https://ryanstutorials.net/linuxtutorial/grep.php