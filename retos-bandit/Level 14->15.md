
# Objetivo

La contraseña para el siguiente nivel se puede recuperar enviando la contraseña del nivel actual al puerto 30000 en localhost.

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit14**.
Contraseña: Encontrada en el nivel anterior: `fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq`.

## Solución
```
bandit14@bandit:~$ 
bandit14@bandit:~$ nc localhost 30000
fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
Correct!
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt


bandit14@bandit:~$ nmap localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-19 19:07 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00015s latency).
Not shown: 993 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
1111/tcp  open     lmsocialserver
1840/tcp  open     netopia-vo2
4321/tcp  open     rwhois
5120/tcp  filtered barracuda-bbs
8000/tcp  open     http-alt
30000/tcp open     ndmps

Nmap done: 1 IP address (1 host up) scanned in 1.27 seconds
bandit14@bandit:~$ 

```

## Notas adicionales

`nc` -> (`netacat`) Establece la conexión a un servidor + luego, debe indicar hacia donde se hace la conexión (en este caso `localhost`) + al final se el indica el puerto al que ira la conexión (`30000`).
`nmap` -> Escanea la red que se usa para descubrir host y servicios de una red, así como crear un mapa de la red.

## Referencias

ssh, telnet, nc, openssl, s_client, nmap
- [How the Internet works in 5 minutes (YouTube)](https://www.youtube.com/watch?v=7_LPdttKXPc) (Not completely accurate, but good enough for beginners)
- [IP Addresses](http://computer.howstuffworks.com/web-server5.htm)
- [IP Address on Wikipedia](https://en.wikipedia.org/wiki/IP_address)
- [Localhost on Wikipedia](https://en.wikipedia.org/wiki/Localhost)
- [Ports](http://computer.howstuffworks.com/web-server8.htm)
- [Port (computer networking) on Wikipedia](https://en.wikipedia.org/wiki/Port_(computer_networking))