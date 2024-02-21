
# Objetivo

Las credenciales para el siguiente nivel se pueden recuperar enviando la contraseña del nivel actual a un puerto en localhost en el rango 31000 a 32000. Primero averigüe cuál de estos puertos tiene un servidor escuchando en ellos. Luego averigüe cuáles de ellos hablan SSL y cuáles no. Solo hay 1 servidor que le dará las siguientes credenciales, los demás simplemente le enviarán todo lo que les envíe.
## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit16**.
Contraseña: Encontrada en el nivel anterior: `JQttfApK4SeyHwDlI9SXGR50qclOAil1`.

## Solución
```
bandit16@bandit:~$ 
bandit16@bandit:~$ nmap 127.0.0.1 -p 31000-32000
Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-21 18:18 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00011s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE
31046/tcp open  unknown
31518/tcp open  unknown
31691/tcp open  unknown
31790/tcp open  unknown
31960/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
bandit16@bandit:~$ openssl s_client -connect localhost:31046
CONNECTED(00000003)
80DBF0F7FF7F0000:error:0A0000F4:SSL routines:ossl_statem_client_read_transition:unexpected message:../ssl/statem/statem_clnt.c:398:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 293 bytes and written 300 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify error:num=10:certificate has expired
notAfter=Feb 20 17:51:06 2024 GMT
verify return:1
depth=0 CN = localhost
notAfter=Feb 20 17:51:06 2024 GMT
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA1
   v:NotBefore: Feb 20 17:50:06 2024 GMT; NotAfter: Feb 20 17:51:06 2024 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCzCCAfOgAwIBAgIEQ9wEgDANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMjQwMjIwMTc1MDA2WhcNMjQwMjIwMTc1MTA2WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDA
gdd50zQdwKnADuCYAoUSFvGreD2Mr/e6QZK+31XsKXCd/+cGHdmkqerggVlwno8T
3lmAaRw+Pk/nNdn3xJEGGq5guV2YhAnT+IQgP6+76ii/4gUCQxnaTtmslJDSfv7i
km+qYsFRL1YdtOo5od2etkLdorXGqGcIrB6ilCgKgQ2Q7FqMjh7n37HPk8yaWCwX
M/JZ7jkXw4mf2Un9UILgo/oJfR0JhMq6cDkHztG0E6j5ruknDeeOMGimH9pmzaa9
xdJe1GTtk+v03FIng0IfHi0HVPUCN8dl9rKLzn/LKZ3UftyffIErE7nDCLaGpVBK
DQzkq5gMPShGa1RT7nkFAgMBAAGjZTBjMBQGA1UdEQQNMAuCCWxvY2FsaG9zdDBL
BglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0ZWQgYnkgTmNhdC4g
U2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3DQEBBQUAA4IBAQBh
XmVUELbEPhoHaMrhwHyd24bRzYiiOemi75OA6QywOLh7moC8MGKvtI0mHhhA+lfB
eEvOOPwL5om4culG+KnC24fdWzwX/PPtkYKocNSrIQINrVhTwBbGwnC+WCSYizZS
43Zav+szrJ6H66qO4x4wXU9p1qC24dIpY5dfBsy4m8P/XzUtg68YJng1EIuGM6DF
CnMWXUB0cfUgBsbWPMrQlJd5sHifKeglK3kBCXn3zb9T881YbLNAwMK2a5SnPdh8
eTg1e7pdNYwPvHcxYPySGyQCkLpLHduWUxVNrUfsVHrxI6rrHynZ5vv4+ulAmhAc
YoU33/wx/D1oycw1GLHh
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
    Session-ID: D2883C22D9B2C4FCDBB9F2985A7FD3FAF48589CF7847181E6EED6D99E91BF817
    Session-ID-ctx: 
    Resumption PSK: EF5DBAF9B2768FE7ED0024464868E2911686D8CC8D1F9C72C70636897368C87D89C62C52D3D0AA905FE45DA1E9942AF1
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 92 ed 0d d5 75 f9 0c 95-ed 08 73 73 af f3 6c c3   ....u.....ss..l.
    0010 - 45 ad 9d 21 45 32 68 63-d6 98 6d d8 cf 71 b5 69   E..!E2hc..m..q.i
    0020 - 3e 19 fb 07 41 bf 9a 54-94 a4 0e e3 40 6a b1 01   >...A..T....@j..
    0030 - 32 37 73 e3 9c be 65 6e-ad 9c 61 01 53 d6 47 b2   27s...en..a.S.G.
    0040 - cb 1a 23 2e 75 24 23 71-72 ca a4 6f 74 b0 51 b6   ..#.u$#qr..ot.Q.
    0050 - 95 07 42 58 2b 59 7a 09-aa 8b 69 8c f2 a7 58 4f   ..BX+Yz...i...XO
    0060 - e5 dd ea 74 61 61 29 2f-e9 2a 8d fe 2c 51 10 d8   ...taa)/.*..,Q..
    0070 - d8 03 f6 17 b6 88 fc f2-88 6c 24 22 06 0e 19 f4   .........l$"....
    0080 - ab 23 86 eb b3 53 5f 65-20 09 b1 b7 7c 3f dd 48   .#...S_e ...|?.H
    0090 - 88 63 79 69 82 c0 ac 14-dc 37 80 cd 28 74 32 88   .cyi.....7..(t2.
    00a0 - 3d 2f d1 6f b1 75 62 b2-01 9d b3 10 8a fd 00 a4   =/.o.ub.........
    00b0 - ad e9 cb 38 e7 3a a7 6c-c8 4f 1d 7c e7 7a 95 1b   ...8.:.l.O.|.z..
    00c0 - da 66 f3 04 12 a2 70 15-27 dd ca 58 47 af 86 2b   .f....p.'..XG..+

    Start Time: 1708539527
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
    Session-ID: BB485EEC699F2FA5F39C727657D00F65B430D372B03F7ECD7EAEE554932F3E92
    Session-ID-ctx: 
    Resumption PSK: 5AECBB744791E35558DF7C3CF918C1A1FDB9D989CE56DD63B8DB9D15BF7549008B7B412B0F065CAEFC4557176E47A2FC
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 92 ed 0d d5 75 f9 0c 95-ed 08 73 73 af f3 6c c3   ....u.....ss..l.
    0010 - 79 1a 75 84 03 bc e4 d7-31 73 75 9e 38 1a d8 25   y.u.....1su.8..%
    0020 - 91 bc e2 18 e8 5f a3 de-29 9f f0 a5 ac 1c 6a dc   ....._..).....j.
    0030 - 9a fd b5 8b dc cc 49 2b-55 ab 3c 1d c3 73 ec 31   ......I+U.<..s.1
    0040 - 94 3a 0d 25 01 e8 28 50-bb 91 a7 a5 fd fb ee fd   .:.%..(P........
    0050 - fc ab 59 30 d5 61 65 8e-e9 90 16 92 03 5b b7 74   ..Y0.ae......[.t
    0060 - f5 19 67 9a 22 ce 35 98-8b 0c be 07 c8 68 ca 42   ..g.".5......h.B
    0070 - 9b 09 c0 e9 7c f5 e6 fe-fb b3 81 84 b5 4b fc 72   ....|........K.r
    0080 - 07 67 e2 de be 05 01 4a-44 30 f6 4a f8 66 9f d4   .g.....JD0.J.f..
    0090 - a2 20 49 99 cb 53 a6 03-bd 74 62 77 09 17 f4 12   . I..S...tbw....
    00a0 - af 1b 71 99 f2 ba c9 11-ee b1 40 35 8f 09 6a 37   ..q.......@5..j7
    00b0 - 03 dd e7 15 74 cb 5a 08-89 44 4e 25 72 bc 5d d1   ....t.Z..DN%r.].
    00c0 - 35 6d 9d cb f7 03 39 3e-be a4 ad 6f 85 f2 1f b8   5m....9>...o....

    Start Time: 1708539527
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
JQttfApK4SeyHwDlI9SXGR50qclOAil1
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
bandit16@bandit:~$ 

```

## Notas adicionales

- `nmap` -> Lo usamos para realizar el escaneo de puertos en una red y obtener información sobre los servicios que están en ejecución en un host especifico.
- `openssl s_client`-> Inicia una conexión SSL/TSL y verifica detalles de certificados, cadenas de cifrados y otros parámetros de seguridad en un servidor.
## Referencias

ssh, telnet, nc, openssl, s_client, nmap
[Port scanner on Wikipedia](https://en.wikipedia.org/wiki/Port_scanner)