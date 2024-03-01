# Objetivo

¿Puedes descifrar la contraseña para obtener la bandera?
Descargue el verificador de contraseñas `aquí` y también necesitará la `bandera` cifrada y el `hash` en el mismo directorio.
Hay 7 contraseñas potenciales y 1 es correcta. Puede encontrarlos examinando el script de verificación de contraseñas.
1. Para ver el archivo nivel3.hash.bin en el webshell, haga: $ bvi nivel3.hash.bin
2. Para salir de bvi escriba :q y presione enter.
## Solución

Al ejecutar el comando `nano level3.py`, y analizar lo que contiene, nos encontramos con esta seccion:
```
# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
```

Probamos hasta acertar en la ejecucion del programa.
```
chuyelhacker-picoctf@webshell:~$ ls
README.txt  level3.flag.txt.enc  level3.hash.bin  level3.py
chuyelhacker-picoctf@webshell:~$ nano level3.py
chuyelhacker-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: f09e
That password is incorrect
chuyelhacker-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: 4dcf
That password is incorrect
chuyelhacker-picoctf@webshell:~$ python level3.py
Please enter correct password for flag: 87ab
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
chuyelhacker-picoctf@webshell:~$ 
```
## Notas adicionales

- `python`->Ejecuta scripts de phyton.
- `nano`->Nos ayudo a ver y editar archivos de texto existentes directamente desde una nueva terminal.
## Referencias