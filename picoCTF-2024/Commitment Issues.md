## Objetivo 
I accidentally wrote the flag down. Good thing I deleted it!You download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/77/challenge.zip)

## Solución
```bash
luispuentes-picoctf@webshell:~$ ls
Parcial1  README.txt  bin  challenge.zip  crackme100  drop-in  root
luispuentes-picoctf@webshell:~$ cd drop-in/
luispuentes-picoctf@webshell:~/drop-in$ git log


commit e1237df82d2e69f62dd53279abc1c8aeb66f6d64 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:14 2024 +0000

    remove sensitive info

commit 3d5ec8a26ee7b092a1760fea18f384c35e435139
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:14 2024 +0000

    create flag
(END)

luispuentes-picoctf@webshell:~/drop-in$ git checkout 3d5ec8a26ee7b092a1760fea18f384c35e435139
Note: switching to '3d5ec8a26ee7b092a1760fea18f384c35e435139'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 3d5ec8a create flag
luispuentes-picoctf@webshell:~/drop-in$ ls
message.txt
luispuentes-picoctf@webshell:~/drop-in$ cat message.txt 
picoCTF{s@n1t1z3_30e86d36}
luispuentes-picoctf@webshell:~/drop-in$ 
```


## Notas
En el git log se encontro un registro de historial de edicion, el cual al analizarlo se obtiene la contraseña.

## Referencias
Manual de usuario del comando git.