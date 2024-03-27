# Objetivo
Know of little and big endian?`nc titan.picoctf.net 59784`. [Source](https://artifacts.picoctf.net/c_titan/79/flag.c)
# Datos de acceso
nc titan.picoctf.net 59784
# Solución
```
tonyrguez-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/79/flag.c
--2024-03-13 22:58:33--  https://artifacts.picoctf.net/c_titan/79/flag.c
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.128, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3666 (3.6K) [application/octet-stream]
Saving to: 'flag.c'

flag.c                                          100%[======================================================================================================>]   3.58K  --.-KB/s    in 0s      

2024-03-13 22:58:33 (1.53 GB/s) - 'flag.c' saved [3666/3666]

tonyrguez-picoctf@webshell:~$ pico flag.c
tonyrguez-picoctf@webshell:~$ nc titan.picoctf.net 59784
Welcome to the Endian CTF!
You need to find both the little endian and big endian representations of a word.
If you get both correct, you will receive the flag.
Word: tyrlz
Enter the Little Endian representation: 7a6c727974
Correct Little Endian representation!
Enter the Big Endian representation: 7479726c7a
Correct Big Endian representation!
Congratulations! You found both endian representations correctly!
Your Flag is: picoCTF{3ndi4n_sw4p_su33ess_d58517b6}


```
# Notas
- La palabra dada por el programa es transformada en hexadecimal en cyberchef, para el formato de little endian primero se ponen los últimos 2 bytes en hexa, después los que siguen y así sucesivamente. Para big endian se guarda en el orden dado en cyberchef para así obtener la bandera.
# Referencia