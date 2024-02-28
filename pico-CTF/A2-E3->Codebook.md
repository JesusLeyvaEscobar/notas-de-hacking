# Objetivo

Ejecute el script de Python code.py en el mismo directorio que codebook.txt.

1. En el webshell, use ls para ver si ambos archivos están en el directorio en el que se encuentra.
2. No es necesario realizar ingeniería inversa a la función str_xor para este desafío.
## Solución

```
chuyelhacker-picoctf@webshell:~$ ls
README.txt
chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/1/code.py
--2024-02-28 03:56:19--  https://artifacts.picoctf.net/c/1/code.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.92, 3.160.22.128, 3.160.22.43, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.92|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1278 (1.2K) [application/octet-stream]
Saving to: 'code.py'

code.py                           100%[==========================================================>]   1.25K  --.-KB/s    in 0s      

2024-02-28 03:56:19 (66.2 MB/s) - 'code.py' saved [1278/1278]

chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/1/codebook.txt
--2024-02-28 03:56:32--  https://artifacts.picoctf.net/c/1/codebook.txt
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.92, 3.160.22.16, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27 [application/octet-stream]
Saving to: 'codebook.txt'

codebook.txt                      100%[==========================================================>]      27  --.-KB/s    in 0s      

2024-02-28 03:56:32 (769 KB/s) - 'codebook.txt' saved [27/27]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  code.py  codebook.txt
chuyelhacker-picoctf@webshell:~$ python code.py
picoCTF{c0d3b00k_455157_d9aa2df2}
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `python`-> Ejecuta scripts de phyton.

## Referencias

https://gchq.github.io/CyberChef/