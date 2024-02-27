# Objetivo

Este archivo tiene una bandera a la vista (también conocida como "claro").

## Solución

```
chuyelhacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag--2024-02-26 18:32:57--  https://mercury.picoctf.net/static/fb851c1858cc762bd4eed569013d7f00/flag
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 34 [application/octet-stream]
Saving to: 'flag.1'

flag.1                    100%[===================================>]      34  --.-KB/s    in 0s      

2024-02-26 18:32:57 (14.6 MB/s) - 'flag.1' saved [34/34]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  flag
chuyelhacker-picoctf@webshell:~$ cat flag
picoCTF{s4n1ty_v3r1f13d_28e8376d}
chuyelhacker-picoctf@webshell:~$ 
```
## Notas adicionales


## Referencias

