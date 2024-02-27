
# Objetivo

Hay un repositorio git en ssh://bandit30-git@localhost/home/bandit30-git/repo a través del puerto 2220. La contraseña para el usuario bandit30-git es la misma que para el usuario bandit30.

Clona el repositorio y busca la contraseña para el siguiente nivel.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit30**.
Contraseña: Encontrada en el nivel anterior: `xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS`.

## Solución
```
bandit30@bandit:~$ id
uid=11030(bandit30) gid=11030(bandit30) groups=11030(bandit30)
bandit30@bandit:~$ cd /tmp
bandit30@bandit:/tmp$ mkdir bandit30_certa6
bandit30@bandit:/tmp$ cd bandit30_certa6
bandit30@bandit:/tmp/bandit30_certa6$ git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit30/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit30/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit30-git@localhost's password: 
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
bandit30@bandit:/tmp/bandit30_certa6$ ls
repo
bandit30@bandit:/tmp/bandit30_certa6$ cd repo
bandit30@bandit:/tmp/bandit30_certa6/repo$ ls
README.md
bandit30@bandit:/tmp/bandit30_certa6/repo$ cat README.md
just an epmty file... muahaha
bandit30@bandit:/tmp/bandit30_certa6/repo$ git log
commit d39631d73f786269b895ae9a7b14760cbf40a99f (HEAD -> master, origin/master, origin/HEAD)
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Oct 5 06:19:45 2023 +0000

    initial commit of README.md
bandit30@bandit:/tmp/bandit30_certa6/repo$ git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
bandit30@bandit:/tmp/bandit30_certa6/repo$ git tag
secret
bandit30@bandit:/tmp/bandit30_certa6/repo$ git how secret
git: 'how' is not a git command. See 'git --help'.

The most similar command is
	show
bandit30@bandit:/tmp/bandit30_certa6/repo$ git show secret
OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt
```

## Notas adicionales

- `git tag` -> Verificamos etiquetas dentro de un repositorio.
## Referencias

git