## Objetivo 
Someone's commits seems to be preventing the program from working. Who is it?You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_titan/74/challenge.zip)

## Solución
```bash
luispuentes-picoctf@webshell:~$ ls
Parcial1  README.txt  challenge.zip  drop-in  runme.py
luispuentes-picoctf@webshell:~$ cd drop-in/
luispuentes-picoctf@webshell:~/drop-in$ git log
luispuentes-picoctf@webshell:~/drop-in$ 


commit ccf857444761e8380204eafd76e677f9e7e71a94
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    important business work

commit 0fe87f16cbd8129ed5f7cf2f6a06af6688665728
Author: picoCTF{@sk_th3_1nt3rn_ea346835} <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    optimize file size of prod code

commit 7e8a2415b6cca7d0d0002ff0293dd384b5cc900d
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    create top secret project
```


## Notas
En el git log se encontró la contraseña como autor de edición del archivo.

## Referencias
https://primer.picoctf.org/#_git_version_control
https://github.com/LuissPuentes/FundamentosSeguridad/blob/main/OverTheWire_Wargames/Bandit%20Level%2029%20to%2030.md

