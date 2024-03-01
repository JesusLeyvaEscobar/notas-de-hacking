# Objetivo

¿Puedes mirar los datos en este binario: estático? ¡Este script BASH podría ayudar!
## Solución

```
chuyelhacker-picoctf@webshell:~$ ls
README.txt  ltdis.sh  static
chuyelhacker-picoctf@webshell:~$ file static
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=17ad46e6c58b7c40148a89923e314662595d101b, not stripped
chuyelhacker-picoctf@webshell:~$ strings static | grep pico
picoCTF{d15a5m_t34s3r_ccb2b43e}
chuyelhacker-picoctf@webshell:~$ 

```

## Notas adicionales

- `strings`->Nos muestra las cadenas de caracteres imprimibles que se encuentren en el fichero que se le indica.
- `grep`->Nos ayudo como un "filtro" para buscar en un archivo o pagina, cierta palabra pues elimina la información inútil que no coincida con lo que le indiquemos. Se usa: `grep` + `caracter a buscar`.
## Referencias

