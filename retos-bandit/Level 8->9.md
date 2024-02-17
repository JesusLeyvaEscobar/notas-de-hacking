
# Objetivo

La contraseña para el siguiente nivel se almacena en el archivo `data.txt` y es la única línea de texto que aparece solo una vez.

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit8**.
Contraseña: **Encontrada en el nivel anterior: `TESKZC0XvTetK0S9xNwm25STk5iWrBvP`.**

## Solución
```
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ wc -l data.txt
1001 data.txt
bandit8@bandit:~$ sort data.txt | uniq -u
EN632PlfYiZbn3PhVK3XOGSlNInNE00t
bandit8@bandit:~$ 

```

## Notas adicionales

- `sort` -> Ordena lineas de un archivo de texto.
- `|` -> Aúna 2 comandos.
- `uniq` -> Filtra/cuenta las lineas que están repetidas 
	- `uniq -u` Toma las lineas ordenadas que da el `sort` y toma solo las que no se repitan.
## Referencias

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
[Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php)
