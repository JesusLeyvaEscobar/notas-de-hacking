
# Objetivo

Hay un repositorio git en ssh://bandit28-git@localhost/home/bandit28-git/repo a través del puerto 2220. La contraseña para el usuario bandit28-git es la misma que para el usuario bandit28.

Clona el repositorio y busca la contraseña para el siguiente nivel.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit28**.
Contraseña: Encontrada en el nivel anterior: `AVanL161y9rsbcJIsFHuw35rjaOM19nR`.

## Solución
```
bandit28@bandit:~$ id
uid=11028(bandit28) gid=11028(bandit28) groups=11028(bandit28)
bandit28@bandit:~$ cd /tmp
bandit28@bandit:/tmp$ mkdir bandit28_certa
bandit28@bandit:/tmp$ cd bandit28_certa
bandit28@bandit:/tmp/bandit28_certa$ git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo 
Cloning into 'repo'...
The authenticity of host '[localhost]:2220 ([127.0.0.1]:2220)' can't be established.
ED25519 key fingerprint is SHA256:C2ihUBV7ihnV1wUXRb4RrEcLfXC5CXlhmAAM/urerLY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Could not create directory '/home/bandit28/.ssh' (Permission denied).
Failed to add the host to the list of known hosts (/home/bandit28/.ssh/known_hosts).
                         _                     _ _ _   
                        | |__   __ _ _ __   __| (_) |_ 
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_ 
                        |_.__/ \__,_|_| |_|\__,_|_|\__|
                                                       

                      This is an OverTheWire game server. 
            More information on http://www.overthewire.org/wargames

bandit28-git@localhost's password: 
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
bandit28@bandit:/tmp/bandit28_certa$ ls
repo
bandit28@bandit:/tmp/bandit28_certa$ cd repo
bandit28@bandit:/tmp/bandit28_certa/repo$ ls
README.md
bandit28@bandit:/tmp/bandit28_certa/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/bandit28_certa/repo$ git log
commit 14f754b3ba6531a2b89df6ccae6446e8969a41f3 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Oct 5 06:19:41 2023 +0000

    fix info leak

commit f08b9cc63fa1a4602fb065257633c2dae6e5651b
Author: Morla Porla <morla@overthewire.org>
Date:   Thu Oct 5 06:19:41 2023 +0000

    add missing data

commit a645bcc508c63f081234911d2f631f87cf469258
Author: Ben Dover <noone@overthewire.org>
Date:   Thu Oct 5 06:19:41 2023 +0000

    initial commit of README.md
bandit28@bandit:/tmp/bandit28_certa/repo$ git checkout f08b9cc63fa1a4602fb065257633c2dae6e5651bNote: switching to 'f08b9cc63fa1a4602fb065257633c2dae6e5651b'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at f08b9cc add missing data
bandit28@bandit:/tmp/bandit28_certa/repo$ ls
README.md
bandit28@bandit:/tmp/bandit28_certa/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

bandit28@bandit:/tmp/bandit28_certa/repo$ 

```

## Notas adicionales

- `git log` -> Muestra los commits realizados.
- `git checkout` -> Lo usamos para regresar a un punto de guardado.
## Referencias

git