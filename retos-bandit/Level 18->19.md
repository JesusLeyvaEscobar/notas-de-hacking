
# Objetivo

La contraseña para el siguiente nivel se almacena en un archivo Léame en el directorio de inicio. Desafortunadamente, alguien ha modificado .bashrc para cerrar tu sesión cuando inicias sesión con SSH.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit18**.
Contraseña: Encontrada en el nivel anterior: `hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`.

## Solución
```
┌──(jesus㉿KaliJesus)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 /bin/bash
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 

ls
readme
cat readme
awhqfNnAbc1naukrpqDYcF95h7HoMTrC

--------------METODO 2-------------------
┌──(jesus㉿KaliJesus)-[~]
└─$ ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password: 
awhqfNnAbc1naukrpqDYcF95h7HoMTrC
                                                                                                                      
┌──(jesus㉿KaliJesus)-[~]
└─$ 

```

## Notas adicionales

- `/bin/bash` -> Inicia un shell de Bash una vez que la conexión SSH se estableció.
## Referencias

ssh, ls, cat