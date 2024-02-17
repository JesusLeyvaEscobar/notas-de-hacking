cat 
# Objetivo

La contraseña para el siguiente nivel se almacena en un archivo llamado **spaces in this filename ubicado en el directorio de inicio.

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit2**.
Contraseña: **Encontrada en el archivo *`-`* del nivel anterior: `rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi`.**

## Solución
```
bandit2@bandit:~$ 
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ file spaces in this filname
spaces:  cannot open `spaces' (No such file or directory)
in:      cannot open `in' (No such file or directory)
this:    cannot open `this' (No such file or directory)
filname: cannot open `filname' (No such file or directory)
bandit2@bandit:~$ cat spaces in this filname
cat: spaces: No such file or directory
cat: in: No such file or directory
cat: this: No such file or directory
cat: filname: No such file or directory
bandit2@bandit:~$ cat spaces\ in\ this\ filename
aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
bandit2@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
                                                                                                    
┌──(jesus㉿KaliJesus)-[~]
└─$ 

```

## Notas adicionales

Para este nivel nos encontramos con un archivo que contenía la contraseña, el cual, en su nombre contenía espacios. Esta practica de dejar espacios en Linux no es recomendada y lo mejor es evitar espacios pues linux detecta estos espacios como argumentos separados, para evitarlo tenemos algunas formas de lidiar con este tipo de archivos:
- Poner el nombre del archivo entre comillas dobles (") o simles(').
- Poner un guion invertido (\) antes de cada espacio del nombre del archivo.

Esta solución la encontré en la siguiente pagina web: https://linuxhandbook.com/filename-spaces-linux/

## Referencias

[ls](https://man7.org/linux/man-pages/man1/ls.1.html) , [cd](https://man7.org/linux/man-pages/man1/cd.1p.html) , [cat](https://man7.org/linux/man-pages/man1/cat.1.html) , [file](https://man7.org/linux/man-pages/man1/file.1.html) , [du](https://man7.org/linux/man-pages/man1/du.1.html) , [find](https://man7.org/linux/man-pages/man1/find.1.html)
[Google Search for “spaces in filename”](https://www.google.com/search?q=spaces+in+filename)
