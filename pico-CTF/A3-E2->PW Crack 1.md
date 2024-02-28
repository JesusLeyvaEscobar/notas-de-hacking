# Objetivo

¿Puedes descifrar la contraseña para obtener la bandera?
Descargue el verificador de contraseñas aquí y también necesitará la bandera cifrada en el mismo directorio.
## Solución

```
chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/11/level1.py
--2024-02-28 05:40:20--  https://artifacts.picoctf.net/c/11/level1.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.16, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 876 [application/octet-stream]
Saving to: 'level1.py'

level1.py                         100%[==========================================================>]     876  --.-KB/s    in 0s      

2024-02-28 05:40:20 (27.5 MB/s) - 'level1.py' saved [876/876]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  level1.py
chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/11/level1.flag.txt.enc
--2024-02-28 05:40:34--  https://artifacts.picoctf.net/c/11/level1.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.16, 3.160.22.128, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 30 [application/octet-stream]
Saving to: 'level1.flag.txt.enc'

level1.flag.txt.enc               100%[==========================================================>]      30  --.-KB/s    in 0s      

2024-02-28 05:40:34 (1.44 MB/s) - 'level1.flag.txt.enc' saved [30/30]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  level1.flag.txt.enc  level1.py
chuyelhacker-picoctf@webshell:~$ python level1.py
Please enter correct password for flag: n
That password is incorrect
chuyelhacker-picoctf@webshell:~$ cat level1.flag.txt.enc
A
 Rr1wQ  nVT_nPRVWchuyelhacker-picoctf@webshell:~$ nano level1.py
chuyelhacker-picoctf@webshell:~$ python level1.py
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `python`->
- `nano`->
## Referencias

