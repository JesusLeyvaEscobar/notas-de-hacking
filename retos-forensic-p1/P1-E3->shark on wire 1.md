# Objetivo

Encontramos esta captura de paquete. Recuperar la bandera.
1. Intente utilizar una herramienta como Wireshark.
2. ¿Qué son los `streams`?.
## Solución

Descargamos el archivo del enlace que nos proporciona la pagina, y vemos que tipo de archivo es:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/sharkonwire1]
└─$ ls               
capture.pcap

┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc/sharkonwire1]
└─$ file capture.pcap
capture.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)
```
Vemos que es un archivo con extension `.cap` por lo que usamos `Wireshark` para abrirlo.
Abrimos la captura que se nos descargo con anterioridad, y analizamos algun tipo de archivo UDP.
1. Vamos a darle seguir, luego UDP Stream
Nos dirige al stream 4, solo buscamos entre los grupos de paquetes y, en nuestro caso, al llegar al Stream 6 encontraremos una bandera que nos sirve para completar el reto:
`picoCTF{StaT31355_636f6e6e}`

## Notas adicionales

- `Captura de paquetes`-> Es un API que permite capturar paquetes de datos que viajan de las capas 2 y 7 del modelo OSI.
- `Wireshark`-> Es una herramienta (analizador de protocolos), con una interfaz gráfica que permite navegar atraves de los paquetes envivo en la red, o sobre una captura de paquetes realizada previamente.
## Referencias

- https://es.linkedin.com/pulse/network-traffic-analysis-qu%C3%A9-es-un-archivo-pcap-arturo-e-torres#:~:text=La%20captura%20de%20paquetes%20o,2%2D7%20del%20modelo%20OSI.