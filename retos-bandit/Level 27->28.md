
# Objetivo

Hay un repositorio git en ssh://bandit27-git@localhost/home/bandit27-git/repo a través del puerto 2220. La contraseña para el usuario bandit27-git es la misma que para el usuario bandit27.

Clona el repositorio y busca la contraseña para el siguiente nivel.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit27**.
Contraseña: Encontrada en el nivel anterior: `YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS`.

## Solución
```
bandit27@bandit:~$ id
uid=11027(bandit27) gid=11027(bandit27) groups=11027(bandit27)
bandit27@bandit:~$ cd /tmp
bandit27@bandit:/tmp$ mkdir bandit27_certa6
bandit27@bandit:/tmp$ cd bandit27_certa6
bandit27@bandit:/tmp/bandit27_certa6$ git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit27/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/bandit27_certa6$ ls
repo
bandit27@bandit:/tmp/bandit27_certa6$ cd repo
bandit27@bandit:/tmp/bandit27_certa6/repo$ ls
README
bandit27@bandit:/tmp/bandit27_certa6/repo$ cat README
The password to the next level is: AVanL161y9rsbcJIsFHuw35rjaOM19nR
bandit27@bandit:/tmp/bandit27_certa6/repo$ 

```

## Notas adicionales

- `git clone` -> Clona un repositorio de git existente en la direccion actual.
## Referencias

git