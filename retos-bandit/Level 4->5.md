
# Objetivo

La contraseña para el siguiente nivel se almacena en el único archivo legible por humanos en el directorio `inhere`. Consejo: si tu terminal está estropeado, prueba el comando “reset”.


## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit4**.
Contraseña: **Encontrada en el archivo oculto `.hidden` del directorio `inhere` del nivel anterior: `2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe`.**

## Solución
```
bandit4@bandit:~$ 
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ find
.
./-file01
./-file02
./-file08
./-file06
./-file00
./-file04
./-file05
./-file07
./-file03
./-file09
bandit4@bandit:~/inhere$ file ./-file01
./-file01: data
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat < -file07
lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
bandit4@bandit:~/inhere$ 
```

## Notas adicionales

Este nivel nos da indicaciones que la contraseña esta almacenada en uno de los archivos contenidos en el directorio `inhere`, por lo que primero vimos que archivos contenía este directorio para después, con el comando `file` analizar el primero de todos y observar que sera ilegible, por lo que hacemos uso de `file ./*` para saber que tipo de archivos son todos y cada uno de los que se encuentran en este directorio. Se observa que solamente uno de ellos es texto en ASCII, por ende, es el único que podremos interpretar como humanos, tal y como lo dice las indicaciones.

- Un `*` ayuda a señalar a todos los archivos contenidos en un directorio.
## Referencias

[ls](https://man7.org/linux/man-pages/man1/ls.1.html) , [cd](https://man7.org/linux/man-pages/man1/cd.1p.html) , [cat](https://man7.org/linux/man-pages/man1/cat.1.html) , [file](https://man7.org/linux/man-pages/man1/file.1.html) , [du](https://man7.org/linux/man-pages/man1/du.1.html) , [find](https://man7.org/linux/man-pages/man1/find.1.html)
