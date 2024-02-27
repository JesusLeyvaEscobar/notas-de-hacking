# Objetivo

¿Puedes invocar indicadores de ayuda para una herramienta o binario? Este programa tiene información extraordinariamente útil...

## Solución

```
chuyelhacker-picoctf@webshell:~$ wget https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm
--2024-02-26 18:46:58--  https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10936 (11K) [application/octet-stream]
Saving to: 'warm'

warm                      100%[===================================>]  10.68K  --.-KB/s    in 0s      

2024-02-26 18:46:58 (68.1 MB/s) - 'warm' saved [10936/10936]

chuyelhacker-picoctf@webshell:~$ ls
README.txt  flag  flag.1  warm
chuyelhacker-picoctf@webshell:~$ chmod +x warm
chuyelhacker-picoctf@webshell:~$ ls
README.txt  flag  flag.1  warm
chuyelhacker-picoctf@webshell:~$ ./warm
Hello user! Pass me a -h to learn what I can do!
chuyelhacker-picoctf@webshell:~$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}
chuyelhacker-picoctf@webshell:~$ 
```
## Notas adicionales

Se requirio hacer el programa descargado como ejecutable.
- `chmod +x warm`-> Convierte al archivo warm como ejecutable.
- `./warm`-> Ejecuta el archivo warm.
## Referencias

