# Objetivo

¿Puedes descifrar la contraseña para obtener la bandera?
Descargue el verificador de contraseñas aquí y también necesitará la bandera cifrada en el mismo directorio.
## Solución

```
chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/13/level2.py
--2024-02-28 05:54:15--  https://artifacts.picoctf.net/c/13/level2.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.16, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 914 [application/octet-stream]
Saving to: 'level2.py'

level2.py                         100%[==========================================================>]     914  --.-KB/s    in 0s      

2024-02-28 05:54:16 (34.1 MB/s) - 'level2.py' saved [914/914]

chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/13/level2.flag.txt.enc
--2024-02-28 05:54:24--  https://artifacts.picoctf.net/c/13/level2.flag.txt.enc
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.16, 3.160.22.92, 3.160.22.43, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.16|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 31 [application/octet-stream]
Saving to: 'level2.flag.txt.enc'

level2.flag.txt.enc               100%[==========================================================>]      31  --.-KB/s    in 0s      

2024-02-28 05:54:24 (640 KB/s) - 'level2.flag.txt.enc' saved [31/31]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  level2.flag.txt.enc  level2.py
chuyelhacker-picoctf@webshell:~$ nano level2.py
chuyelhacker-picoctf@webshell:~$ python level2.py
Please enter correct password for flag: de76
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_489dea9a}
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `python`->Ejecuta scripts de phyton.
- `nano`->Nos ayudo a ver y editar archivos de texto existentes directamente desde una nueva terminal.
- Usamos cyberchef para descifrar la contraseña que contenia el script `level2.py`
## Referencias

https://gchq.github.io/CyberChef/