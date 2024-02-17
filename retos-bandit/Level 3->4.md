
# Objetivo

La contraseña para el siguiente nivel se almacena en un archivo oculto en el directorio interno.

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit3**.
Contraseña: **Encontrada en el archivo `spaces in this filename` del nivel anterior: `aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG`.**

## Solución
```
bandit3@bandit:~$ 
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ find
.
./.hidden
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Oct  5 06:19 .
drwxr-xr-x 3 root    root    4096 Oct  5 06:19 ..
-rw-r----- 1 bandit4 bandit3   33 Oct  5 06:19 .hidden
bandit3@bandit:~/inhere$ cat .hidden
2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe
bandit3@bandit:~/inhere$ exit
logout
Connection to bandit.labs.overthewire.org closed.
                                                                                                    
┌──(jesus㉿KaliJesus)-[~]
└─$ 
```

## Notas adicionales

En este nivel, tuvimos que acceder a una carpeta que contenía un archivo oculto, con la ayuda del comando `find` nos dimos cuenta que había un archivo oculto llamado `.hidden` y para comprobar que esto fuera correcto, hicimos uso de el comando `ls` con sus parámetros `l` + `a` que nos ayudo a mostrar la lista en formato de lista larga con todos los archivos contenidos en el directorio y efectivamente tenemos un archivo extra (aparte de `.` y `..` que son los directorios anteriores) que se llama `.hidden`.

- `ls -la` -> Muestra los archivos en formato largo, incluyendo los ocultos.

## Referencias

[ls](https://man7.org/linux/man-pages/man1/ls.1.html) , [cd](https://man7.org/linux/man-pages/man1/cd.1p.html) , [cat](https://man7.org/linux/man-pages/man1/cat.1.html) , [file](https://man7.org/linux/man-pages/man1/file.1.html) , [du](https://man7.org/linux/man-pages/man1/du.1.html) , [find](https://man7.org/linux/man-pages/man1/find.1.html)
