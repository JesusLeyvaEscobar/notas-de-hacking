# Objetivo

Encuentra la bandera que se mantiene en este servidor para adelantarte a la competencia http://mercury.picoctf.net:47967/
1. Quizás tengas más de 2 opciones.
2. Consulte herramientas como Burpsuite para modificar sus solicitudes y observar las respuestas.
## Solución

- `Proxy`: Ayuda a ocultar direcciones reales y que todas las solicitudes se hagan a través del proxy.

Debemos instalar `FoxyProxy` como extencion en nuestro navegador, para poder cambiar entre proxys (o des habilitarlo) según lo necesitemos.

Ahora, vamos abrir el programa `Burp Suite`, que ya viene con Kali y vamos a agregar a nuestro navegador 
```

ORIGINAL:
GET /index.php? HTTP/1.1
Host: mercury.picoctf.net:47967
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://mercury.picoctf.net:47967/index.php
Upgrade-Insecure-Requests: 1

EDITADA:
HEAD /index.php? HTTP/1.1
Host: mercury.picoctf.net:47967
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://mercury.picoctf.net:47967/index.php
Upgrade-Insecure-Requests: 1

GET /v1/tiles HTTP/1.1
Host: contile.services.mozilla.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Te: trailers
Connection: close

Cambiamos de pestana, nos vamos a la seccion history, buscamos la que editamos y encontraremos, en la seccion Response, lo siguiente:

HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_cca66bd3}
Content-type: text/html; charset=UTF-8

```
## Referencias

- https://developer.mozilla.org/es/docs/Web/HTTP/Methods
- https://en.wikipedia.org/wiki/Burp_Suite
- https://learn.onemonth.com/web-hacking-tools-proxies/