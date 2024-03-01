# Objetivo

Corrija el error de sintaxis en este script de Python para imprimir la bandera.
1. La sangría es muy significativa en Python
2. Para ver el archivo en el webshell, haga: $ nano fixme1.py
3. Para salir de nano, presione Ctrl y x y siga las instrucciones en pantalla.
4. No es necesario realizar ingeniería inversa a la función str_xor para este desafío.

## Solución

```
chuyelhacker-picoctf@webshell:~$ ls
README.txt
chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/26/fixme1.py
--2024-02-28 05:22:16--  https://artifacts.picoctf.net/c/26/fixme1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.43, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 837 [application/octet-stream]
Saving to: 'fixme1.py'

fixme1.py                         100%[==========================================================>]     837  --.-KB/s    in 0s      

2024-02-28 05:22:17 (38.0 MB/s) - 'fixme1.py' saved [837/837]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  fixme1.py
chuyelhacker-picoctf@webshell:~$ nano fixme1.py
chuyelhacker-picoctf@webshell:~$ python fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `nano`->Nos ayudo a ver y editar archivos de texto existentes directamente desde una nueva terminal.

## Referencias