## Objetivo 
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/71/challenge.zip)

## Solución
```bash
luispuentes-picoctf@webshell:~$ ls
Parcial1  README.txt  challenge.zip  drop-in
luispuentes-picoctf@webshell:~$ cd drop-in/
luispuentes-picoctf@webshell:~/drop-in$ ls
flag.py
luispuentes-picoctf@webshell:~/drop-in$ python3 flag.py 
Printing the flag...
luispuentes-picoctf@webshell:~/drop-in$ git log
luispuentes-picoctf@webshell:~/drop-in$ git branch -a
 feature/part-1
  feature/part-2
  feature/part-3
luispuentes-picoctf@webshell:~/drop-in$ git checkout feature/part-1
Switched to branch 'feature/part-1'
luispuentes-picoctf@webshell:~/drop-in$ ls
flag.py
luispuentes-picoctf@webshell:~/drop-in$ python3 flag.py 
Printing the flag...
picoCTF{t3@mw0rk_luispuentes-picoctf@webshell:~/drop-in$ git checkout feature/part-2
Switched to branch 'feature/part-2'
luispuentes-picoctf@webshell:~/drop-in$ python3 flag.py 
Printing the flag...
m@k3s_th3_dr3@m_luispuentes-picoctf@webshell:~/drop-in$ git checkout feature/part-3
Switched to branch 'feature/part-3'
luispuentes-picoctf@webshell:~/drop-in$ python3 flag.py 
Printing the flag...
w0rk_4c24302f}
luispuentes-picoctf@webshell:~/drop-in$

picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_4c24302f}
```


## Notas
En 3 branch estaba la contraseña dividida, al ir cambiando entre ellos y ejecutar el archivo en python, revelaba las partes de la contraseña.

## Referencias
Manual de usuario del comando git.