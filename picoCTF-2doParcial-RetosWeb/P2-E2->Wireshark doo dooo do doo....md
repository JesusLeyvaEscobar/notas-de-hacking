# Objetivo

¿Puedes encontrar la bandera? tiburón1.pcapng.
## Solución

Descargamos el archivo para inspeccionarlo con WireShark:
Vemos que contiene un par de TCP y luego se usa el protocolo HTTP, asi que analizaremos estos TCP y en el stream 5 encontramos algo que resulta un poco familiar a lo que podria ser la bandera:
```
GET / HTTP/1.1
Host: 18.222.37.134
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

HTTP/1.1 200 OK
Date: Mon, 10 Aug 2020 01:51:45 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Fri, 07 Aug 2020 00:45:02 GMT
ETag: "2f-5ac3eea4fcf01"
Accept-Ranges: bytes
Content-Length: 47
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html

Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}
```
Parece ser nuestra cadena, pero al parecer usaron ROT13 para codificarlo, por lo que nos ayudamos de la herramienta CyberChef para comprobar que esta sea la bandera.

La codificación nos dio como resultado:
`The flag is picoCTF{p33kab00_1_s33_u_deadbeef}`
## Notas adicionales

- `ROT13`-> Cifrado que consta en cambiar la letra actual por la letra que se encuentra 13 posiciones adelante de la letra actual.
## Referencias

- https://gchq.github.io/CyberChef/