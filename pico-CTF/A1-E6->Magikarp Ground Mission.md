# Objetivo

¿Sabes cómo moverte entre directorios y leer archivos en el shell? Inicie el contenedor, `ssh` y luego `ls` una vez conectado para comenzar. Inicie sesión a través de `ssh` como `ctf-player` con la contraseña, `abcba9f7`
Detalles adicionales estarán disponibles después de lanzar su instancia de desafío.
## Solución

```
chuyelhacker-picoctf@webshell:~$ ssh ctf-player@venus.picoctf.net -p 54274
ctf-player@venus.picoctf.net's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1041-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Wed Feb 28 01:01:51 2024 from 127.0.0.1
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
ctf-player@pico-chall$ cat  instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  boot  etc   instructions-to-3of3.txt  lib64  mnt  proc  run   srv  tmp  var
bin            dev   home  lib                       media  opt  root  sbin  sys  usr
ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cat instructions-to-3of3.txt 
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ ~
-bash: /home/ctf-player: Is a directory
ctf-player@pico-chall$ cd /home/ctf-player
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt
21cac893}
ctf-player@pico-chall$ Connection to venus.picoctf.net closed by remote host.
Connection to venus.picoctf.net cl
```

## Notas adicionales

- `ls`->Muestra una lista de archivos y directorios.
- `cat`->Usado para crear o mostrar el contenido de archivos existentes.
## Referencias

