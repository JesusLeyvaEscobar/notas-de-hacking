# Objetivo

Usar netcat (nc) será bastante importante. ¿Puedes conectarte a jupiter.challenges.picoctf.org en el puerto 25103 para obtener la bandera?
1. nc [tutorial](https://linux.die.net/man/1/nc)

## Solución

```
Enter your picoCTF username: chuyelhacker
Enter your picoCTF password (characters will be hidden): 

==========================================================================

Welcome to the picoCTF webshell!

💻  The webshell is intended only for solving picoCTF challenges. Any
   other usage is a violation of our terms and conditions.

📹  Sessions are monitored and logged to prevent abuse. Please do not
   enter any sensitive information into the webshell.

🗄  Files stored outside of your home directory will not persist between
   webshell sessions.

🌐  Network connectivity and resources are limited. Some limits can be
   checked by typing usage.

😴  Idle sessions will automatically log out after 15 minutes.

📚  For more information and a beginner's guide, type less ~/README.txt.

==========================================================================

chuyelhacker-picoctf@webshell:~$ ls
README.txt
chuyelhacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 25103
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
^C
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `nc`->Nos ayudo a acceder a puertos TCP/UDP, ya sea de la misma maquina o de otras maquinas remotas.
## Referencias

https://linux.die.net/man/1/nc