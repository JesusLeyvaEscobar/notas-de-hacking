
# Objetivo

La contraseña para el siguiente nivel se almacena en el archivo `data.txt` junto a la palabra `millionth`.

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit7**.
Contraseña: **Encontrada en el nivel anterior: `z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S`.**

## Solución
```
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ wc -l data.txt
98567 data.txt
bandit7@bandit:~$ head data.txt
gallop	hu3ZhCrGRvfaO5jsY6ttvApzVCA2Hjvs
Aurelia's	ikl4F3cK5m6Cl6HAxva6zUAVJhI2Cvc6
stoicism	JiW9ts44udf20bJHe8H5dS1c99Muwz42
embodies	vWheZcAsQHZNnerI3ViW8wqOKIx0kbgR
Plato	dW2U8E5FfuAvNLdGDupP8GAxr922ZV0x
cultivation	A90E75jvWbEKrijFxM4GxqHEw8c8U2Bf
stable	omR4PHolFwbI0IEJsanveA21yWvFy8a7
bedspread	VlBFxuEDi3phEpljbKbahRJvJxfh3k9M
oppressing	hQTiEm5XF3cUQSEiBjh7sekemLOKBrcJ
darnedest	9O2zdCLKVoW5u34P9T7EKTZXcMRE6xh5
bandit7@bandit:~$ tail data.txt
bookkeeping	3qCNwJCGR6esdjIgCyyubIDYuZG8YTIb
coarsen	yeQFtsspdMHS4lZKwmJG6Oes6JZpvEYk
methanol	q0uEpjSocMpf4TaHo78t8E2Bsc1uTOcK
Formica	mo0dVnMSPCo9WdHItXLHMeD0w6SqbMvF
dankness's	YOdD93vvBemBnw7xH0XNKUwPkEfpe7H7
threaten	pOaRPotuhqaf7d9lM0chKcHSM5xQ23qU
monastic	HmNtOzjzjVBHmoKRMH2CMArixJtnt5X3
flank's	234YYMFvjRGfWFZeVlijZAoSaDJSZR3m
demarcates	42GyLcNN2VyYVQAzLk6lH1KoPF7gU60v
biceps's	InBCsYpHT8o1atjygiRFnVE2ExoyirYv
bandit7@bandit:~$ grep millionth data.txt
millionth	TESKZC0XvTetK0S9xNwm25STk5iWrBvP
bandit7@bandit:~$ exit
logout
Connection to bandit.labs.overthewire.org closed.
                                                                                                    
┌──(jesus㉿KaliJesus)-[~]
└─$ 

```

## Notas adicionales

Usamos `wc -l` para a saber el numero de lineas que tiene el archivo a especificar.
- `head` -> Muestra las primeras 10 lineas del archivo.
- `tail` -> Muestra las ultimas 10 lineas del archivo.
Ahora, veremos el comando `grep` para filtrar lineas a un patrón.
La forma de usarlo es: `grep` + [palabra a buscar] + [nombre del archivo].
## Referencias

[man](https://man7.org/linux/man-pages/man1/man.1.html), grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd