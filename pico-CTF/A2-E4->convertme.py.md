# Objetivo

Ejecute el script Python y convierta el número dado de decimal a binario para obtener la bandera.
1. ¡Busque una aplicación de conversión de números decimales a binarios en la web o use la calculadora de su computadora!
2. No es necesario realizar ingeniería inversa a la función str_xor para este desafío.
3. Si tiene Python en su computadora, puede descargar el script normalmente y ejecutarlo. De lo contrario, utilice el comando wget en el webshell.
4. Para usar wget en el webshell, primero haga clic derecho en el enlace de descarga y seleccione "Copiar enlace" o "Copiar dirección de enlace".
5. Escriba todo después del signo de dólar en el shell web: $ wget, luego pegue el enlace después del espacio después de wget y presione Entrar. ¡Esto descargará el script en el webshell para que puedas ejecutarlo!
6. Finalmente, para ejecutar el script, escriba todo lo que esté después del signo de dólar y luego presione enter: $ python3 convertme.py
## Solución

```
chuyelhacker-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/24/convertme.py
--2024-02-28 04:44:03--  https://artifacts.picoctf.net/c/24/convertme.py
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.160.22.43, 3.160.22.128, 3.160.22.92, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.160.22.43|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1189 (1.2K) [application/octet-stream]
Saving to: 'convertme.py'

convertme.py                      100%[==========================================================>]   1.16K  --.-KB/s    in 0s      

2024-02-28 04:44:03 (36.3 MB/s) - 'convertme.py' saved [1189/1189]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  convertme.py
chuyelhacker-picoctf@webshell:~$ python convertme.py
If 91 is in decimal base, what is it in binary base?
Answer: 1011011
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_722f6b39}
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `python`-> Ejecuta scripts de phyton.

## Referencias

https://es.planetcalc.com/375/