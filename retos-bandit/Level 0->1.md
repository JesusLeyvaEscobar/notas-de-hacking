
# Objetivo

La contraseña para el siguiente nivel se almacena en un archivo llamado **readme** ubicado en el directorio de inicio. Utilice esta contraseña para iniciar sesión en bandit1 usando SSH. Siempre que encuentres una contraseña para un nivel, usa SSH (en el puerto 2220) para iniciar sesión en ese nivel y continuar el juego.

## Datos de acceso al nivel

Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit0**.
Contraseña: **bandit0**.

## Solución
```
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ file readme
readme: ASCII text
bandit0@bandit:~$ cat readme
NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
bandit0@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
                                                                                                    
┌──(jesus㉿KaliJesus)-[~]
└─$ 

```

## Notas adicionales

Aprendí los siguientes comandos:
- ls -> Se usa para mostrar la lista de archivos que contiene el directorio actual
- cd -> Ayuda actualizar el directorio de trabajo
- cat -> Se utilizo para mostrar el contenido de un archivo
- file -> Mostro el tipo de archivo que deseamos

## Referencias

[ls](https://man7.org/linux/man-pages/man1/ls.1.html) , [cd](https://man7.org/linux/man-pages/man1/cd.1p.html) , [cat](https://man7.org/linux/man-pages/man1/cat.1.html) , [file](https://man7.org/linux/man-pages/man1/file.1.html) , [du](https://man7.org/linux/man-pages/man1/du.1.html) , [find](https://man7.org/linux/man-pages/man1/find.1.html)
