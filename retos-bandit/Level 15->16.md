
# Objetivo

La contraseña para el siguiente nivel se puede recuperar enviando la contraseña del nivel actual al puerto 30001 en localhost mediante cifrado SSL.

Nota útil: ¿Obtienes “HEARTBEATING” y “Read R BLOCK”? Utilice -ign_eof y lea la sección "COMANDOS CONECTADOS" en la página de manual. Junto a 'R' y 'Q', el comando 'B' también funciona en esta versión de ese comando...

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit14**.
Contraseña: Encontrada en el nivel anterior: `jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt`.

## Solución
```
bandit15@bandit:~$ nc localhost 30001
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
bandit15@bandit:~$ NO HIZO NADA
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 18 10:54:16 2024 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 18 10:54:16 2024 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 18 10:53:16 2024 GMT; NotAfter: Feb 18 10:54:16 2024 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEcjY6OTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjQwMjE4MTA1MzE2WhcNMjQwMjE4MTA1NDE2WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCz
TX1NLedZhpQfXiWbWWD2BlNYjANpj+TnzUOI9ZbKJnOQJAbFfWZLA6No7XOStgje
+RPIoAHrX42G95VDfWtRms+qCsCTlUaS9291dZJQ3iOjBIE+PvmRcGdUlFJXDYa6
E61L2DKLbb8YSAnSuUPG3K7CtdxJpA5DpCBCmHEA9t5gZ5HGo9Gt9Kay9lhApX78
ocytwwHG15LplXI6LQB3ykhyCAcfljR3azd90T83dz7kLyM7yIMt60k1kemuX6RW
qSvkCvxmckRFoQPjwKZUopGLlhcC58Kb2xlwEGK+9j/ibBRkmEdBkOOeb5pJol7K
Wkd9LdG0nTWrggni7EKbAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQCA
j53OECoyjZMkHINZj35xk2kKQc9Jj9XjoCE0HlooUWd1ETik/2TkIbdWenozDrgH
10Jqmu/zAEhQkfFALBXCR7Vo0319yvR3rlnC2TdzMeBeUQ/n6ivPsCCL6SF8UTWT
XZJoTEfmp+Ma4zup/mEs23uO/FQ0J3LmSgICtXzPCA09M/ffj2UgTENdTHDltQxl
nQpzF+U40+bg/2PQ83XOTQJbZVbU2FnP/MitSYycxemLJXzbdsIxQhQy0VmTY73E
ZFemHVTbzEzcsCJRak4AyPZ9Zpi2uozHA8r1PqtnDzsN5FBFwuJxCuc+F8QeHh9e
QoyfsotkA6BO0LBqWNvE
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1339 bytes and written 373 bytes
Verification error: certificate has expired
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 10 (certificate has expired)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: F1C61E33AC749B82B46A1F41A03AE3D778668AD10F1BAD0D66C39D6078EFE2A9
    Session-ID-ctx: 
    Resumption PSK: 51488C6E8520ABD774D740D6E584AF140E6D913397633715C1F5576F360B6101104D067FA88EFA614F70A4BE6186FE39
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - dc 1b 67 7e 6b 49 ec f9-e1 0a 8a 6e cb ac b4 e6   ..g~kI.....n....
    0010 - 62 dd 7b ed ab 8e 39 c7-ee 96 e6 6f b4 90 4d 71   b.{...9....o..Mq
    0020 - 00 89 e1 0d 98 f6 2e a1-13 65 f6 0a 1a bc 00 c3   .........e......
    0030 - 99 7f 66 aa f5 16 50 5f-d2 1b 0a a5 e5 ce 62 97   ..f...P_......b.
    0040 - 1e 0f 68 82 40 76 64 90-76 de d1 4e 23 ad fc 93   ..h.@vd.v..N#...
    0050 - 46 a6 f8 46 2d de 4e 9c-6b 3b 63 2e 78 e1 bd 83   F..F-.N.k;c.x...
    0060 - 04 ac 88 d2 08 15 5a 6b-58 6f 84 db 40 97 42 66   ......ZkXo..@.Bf
    0070 - 38 7e b6 8c 7c 40 b8 82-db 0e cc 3d 48 2e 39 86   8~..|@.....=H.9.
    0080 - da 21 d0 88 d7 e8 d3 42-ae bf 31 4c 2e ce cd 96   .!.....B..1L....
    0090 - 38 4d a1 08 f4 65 53 b4-1d 8a 4b b4 64 d2 71 85   8M...eS...K.d.q.
    00a0 - a4 7d 2b dd 9d cb b5 66-d1 49 6e 94 8c e1 ac 29   .}+....f.In....)
    00b0 - 90 a7 a2 5c 6d 92 64 58-11 a7 cc 9e df b9 22 3f   ...\m.dX......"?
    00c0 - 8e b0 34 7f 8d 8d 9a b7-51 20 cf d7 67 45 8e 9f   ..4.....Q ..gE..

    Start Time: 1708370630
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: C508037CB4E210E01C89390BDA78ABC42EC299A9682F730CED56B3EF0296D861
    Session-ID-ctx: 
    Resumption PSK: F349EB0E50F4FB80719C558495438F17BC135F1AAFF3FEDE25BFD333D17449F1836A6EC1ADF30BFF9C8DD276A1478E05
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - dc 1b 67 7e 6b 49 ec f9-e1 0a 8a 6e cb ac b4 e6   ..g~kI.....n....
    0010 - 5a 8b 1d be e0 5c b7 e2-98 fc ee ee 54 41 24 53   Z....\......TA$S
    0020 - 90 88 24 9c 15 40 fc 7e-e4 d3 c9 9b 3c cc ab 17   ..$..@.~....<...
    0030 - 8f 30 34 9e d0 90 26 64-71 37 ef 6d 30 58 45 87   .04...&dq7.m0XE.
    0040 - a7 b0 27 68 7c 94 e8 b5-62 03 33 ea ef 6c a1 56   ..'h|...b.3..l.V
    0050 - ee 51 7b 57 e9 d0 93 24-86 5f 1f a9 84 a5 b0 18   .Q{W...$._......
    0060 - 8d f0 a6 fc 6a 30 d5 03-e4 2f 48 54 cf 5b 32 1d   ....j0.../HT.[2.
    0070 - e8 90 34 9e 64 3b 2a 52-f9 eb 80 1c 24 c2 42 b2   ..4.d;*R....$.B.
    0080 - aa 7b 26 43 3f 90 24 60-59 d8 d9 db 0d d6 1a 9b   .{&C?.$`Y.......
    0090 - 15 cf 68 7e 26 fd ac 6f-56 f7 b7 e9 f0 07 f1 31   ..h~&..oV......1
    00a0 - 1a b3 84 23 81 42 b4 d6-4a 0e 79 58 a4 2e f1 b0   ...#.B..J.yX....
    00b0 - 35 34 4d 23 88 2c 8f f3-8d 80 45 85 6f d4 05 5d   54M#.,....E.o..]
    00c0 - 2a 91 79 61 58 b6 54 77-b3 8a f3 a4 78 78 e4 69   *.yaX.Tw....xx.i

    Start Time: 1708370630
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
Correct!
JQttfApK4SeyHwDlI9SXGR50qclOAil1

closed
bandit15@bandit:~$ 

```

## Notas adicionales

`openssl s_client` -> Es usado para iniciar una conexión SSL/TLS y verifica detalles de certificados, cadenas de certificados y otros parámetros de seguridad en un servidor. 
## Referencias

ssh, telnet, nc, openssl, s_client, nmap
- [Secure Socket Layer/Transport Layer Security on Wikipedia](https://en.wikipedia.org/wiki/Secure_Socket_Layer)
- [OpenSSL Cookbook - Testing with OpenSSL](https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html)