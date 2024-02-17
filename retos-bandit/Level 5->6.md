
# Objetivo

La contraseña para el siguiente nivel se almacena en un archivo en algún lugar del directorio `inhere` y tiene todas las siguientes propiedades:
- legible por humanos
- 1033 bytes de tamaño
- no ejecutable

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit5**.
Contraseña: **Encontrada en el archivo legible del directorio `inhere` del nivel anterior: `lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR`.**

## Solución
```
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ find . -readable -size 1033c -type f
./maybehere07/.file2
bandit5@bandit:~/inhere$ cd maybehere07
bandit5@bandit:~/inhere/maybehere07$ cat .file2
P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU
bandit5@bandit:~/inhere/maybehere07$ exit
logout
Connection to bandit.labs.overthewire.org closed.
                                                                                                    
┌──(jesus㉿KaliJesus)-[~]
└─$ 

```

## Notas adicionales

- l`s -R `-> Lista archivos de manera recursiva (muestra el contenido en lista lo que contiene cada archivo)
- `find` -> Ayuda a buscar archivos, usando ciertas restricciones/filtros. En este nivel, se requirieron usar:
	- `.` -> Buscar del directorio actual hacia abajo.
	- `-readable` -> Que el archivo sea legible para nosotros como humanos (Se encuentre en ASCII).
	- `-size 1033c` -> Que el tamaño del archivo sea de 1033 y la `c` es para indicar que se trata de bytes.
	- `type f` -> Que el tipo de archivo sea de cierto tipo, en este caso `f` para que sea archivo regular.
## Referencias

[ls](https://man7.org/linux/man-pages/man1/ls.1.html) , [cd](https://man7.org/linux/man-pages/man1/cd.1p.html) , [cat](https://man7.org/linux/man-pages/man1/cat.1.html) , [file](https://man7.org/linux/man-pages/man1/file.1.html) , [du](https://man7.org/linux/man-pages/man1/du.1.html) , [find](https://man7.org/linux/man-pages/man1/find.1.html)
