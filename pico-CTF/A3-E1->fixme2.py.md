# Objetivo

Corrija el error de sintaxis en el script de Python para imprimir la bandera.
Descargar el script Python
## Solución

```
chuyelhacker-picoctf@webshell:~$ ls
README.txt
chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/5/fixme2.py
--2024-02-28 05:34:55--  https://artifacts.picoctf.net/c/5/fixme2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.16, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1029 (1.0K) [application/octet-stream]
Saving to: 'fixme2.py'

fixme2.py                         100%[==========================================================>]   1.00K  --.-KB/s    in 0s      

2024-02-28 05:34:55 (344 MB/s) - 'fixme2.py' saved [1029/1029]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  fixme2.py
chuyelhacker-picoctf@webshell:~$ nano fixme2.py
chuyelhacker-picoctf@webshell:~$ python fixme2.py
  File "/home/chuyelhacker-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
chuyelhacker-picoctf@webshell:~$ nano fixme2.py
chuyelhacker-picoctf@webshell:~$ python fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `nano`->
- `python`->
## Referencias

