## Objetivo
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.You can download the challenge files here:

- `[challenge.zip](https://artifacts.picoctf.net/c_rhea/12/challenge.zip)`

The same files are accessible via SSH here:`ssh -p 51735 ctf-player@rhea.picoctf.net`Using the password `6dd28e9b`. Accept the fingerprint with `yes`, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

- Checksum: 03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
- To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.

## Solución
```bash
luispuentes-picoctf@webshell:~$ ssh -p 62153 ctf-player@rhea.picoctf.net
The authenticity of host '[rhea.picoctf.net]:62153 ([3.136.191.228]:62153)' can't be established.
ED25519 key fingerprint is SHA256:QKdv+RGJL0UYRDM66IiGQ5dsXOX7DQFqB7umTylh+IU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[rhea.picoctf.net]:62153' (ED25519) to the list of known hosts.
ctf-player@rhea.picoctf.net's password: 
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.5.0-1014-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
ctf-player@pico-chall$ cat checksum.txt 
03b52eabed517324828b9e09cbbf8a7b0911f348f76cf989ba6d51acede6d5d8
ctf-player@pico-chall$ cat decrypt.sh 

        #!/bin/bash

        # Check if the user provided a file name as an argument
        if [ $# -eq 0 ]; then
            echo "Expected usage: decrypt.sh <filename>"
            exit 1
        fi

        # Store the provided filename in a variable
        file_name="$1"

        # Check if the provided argument is a file and not a folder
        if [ ! -f "/home/ctf-player/drop-in/$file_name" ]; then
            echo "Error: '$file_name' is not a valid file. Look inside the 'files' folder with 'ls -R'!"
            exit 1
        fi

        # If there's an error reading the file, print an error message
        if ! openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "/home/ctf-player/drop-in/$file_name" -k picoCTF; then
            echo "Error: Failed to decrypt '$file_name'. This flag is fake! Keep looking!"
        fi
        ctf-player@pico-chall$ 
ctf-player@pico-chall$ decrypt.sh checksum.txt 
bad magic number
Error: Failed to decrypt 'checksum.txt'. This flag is fake! Keep looking!
ctf-player@pico-chall$ decrypt.sh files/*
picoCTF{trust_but_verify_00011a60}
ctf-player@pico-chall$
```


## Notas
con la parte del comando donde se pasa el nombre del archivo, que en este caso se coloco files/*, permitio que ingresara todos los archivos que estaban en la carpeta files para comprobarlos todos, uno de ellos nos dio la bandera

## Referencias
https://es.wikipedia.org/wiki/Suma_de_verificaci%C3%B3n