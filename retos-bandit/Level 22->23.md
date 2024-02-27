
# Objetivo

Un programa se ejecuta automáticamente a intervalos regulares desde cron, el programador de trabajos basado en el tiempo. Busque en /etc/cron.d/ la configuración y vea qué comando se está ejecutando.

NOTA: Mirar scripts de shell escritos por otras personas es una habilidad muy útil. El guión de este nivel se ha hecho intencionadamente fácil de leer. Si tiene problemas para entender lo que hace, intente ejecutarlo para ver la información de depuración que imprime.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit22**.
Contraseña: Encontrada en el nivel anterior: `WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff`.

## Solución
```
bandit22@bandit:~$ ls /etc/cron.d/ -la
total 56
drwxr-xr-x   2 root root  4096 Oct  5 06:20 .
drwxr-xr-x 106 root root 12288 Oct  5 06:20 ..
-rw-r--r--   1 root root    62 Oct  5 06:19 cronjob_bandit15_root
-rw-r--r--   1 root root    62 Oct  5 06:19 cronjob_bandit17_root
-rw-r--r--   1 root root   120 Oct  5 06:19 cronjob_bandit22
-rw-r--r--   1 root root   122 Oct  5 06:19 cronjob_bandit23
-rw-r--r--   1 root root   120 Oct  5 06:19 cronjob_bandit24
-rw-r--r--   1 root root    62 Oct  5 06:19 cronjob_bandit25_root
-rw-r--r--   1 root root   201 Jan  8  2022 e2scrub_all
-rwx------   1 root root    52 Oct  5 06:20 otw-tmp-dir
-rw-r--r--   1 root root   102 Mar 23  2022 .placeholder
-rw-r--r--   1 root root   396 Feb  2  2021 sysstat
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:~$ cat //usr/bin/cronjob_bandit23.sh
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$ whoami
bandit22
bandit22@bandit:~$ myname=$(whoami)
bandit22@bandit:~$ echo I am user $myname
I am user bandit22
bandit22@bandit:~$ echo I am user $myname | md5sum
8169b67bd894ddbb4412f91573b38db3  -
bandit22@bandit:~$ echo I am user $myname | md5sum | cut -d ' ' -f 1
8169b67bd894ddbb4412f91573b38db3
bandit22@bandit:~$ 
bandit22@bandit:~$ myname=bandit23
bandit22@bandit:~$ echo I am user $myname | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
bandit22@bandit:~$ 
```

## Notas adicionales

- `cat //usr/bin/cronjob_bandit23.sh`-> Muestra el contenido del script `/usr/bin/cronjob_bandit23.sh`. Este script realiza algunas operaciones con el nombre de usuario (`myname`) y genera una ruta de destino (`mytarget`) mediante el uso de `md5sum`.
- El script copia el contenido del archivo de contraseña del usuario actual (`/etc/bandit_pass/$myname`) a un archivo temporal en `/tmp/`.
- Se realiza una serie de comandos para entender cómo se genera el valor de `mytarget` utilizando el nombre de usuario (`myname`), la función `md5sum`, y `cut`.
- Se cambia el valor de `myname` a `bandit23` y se vuelve a generar el valor de `mytarget` para obtener la dirección en la cual se encuentra la contraseña. 
- AL final, vamos al archivo temporal de la dirección que nos dio en el paso anterior, y observamos que se encuentra la contraseña en el nuevo `mytarget`.
## Referencias

cron, crontab, crontab(5) (use “man 5 crontab” to access this)