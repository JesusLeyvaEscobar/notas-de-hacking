# Objetivo

Descargue el archivo de captura de paquetes y utilice un software de análisis de paquetes para encontrar la bandera.
1. Wireshark, si puede instalarlo y usarlo, es probablemente el producto de software de análisis de paquetes más amigable para principiantes.
## Solución

Este reto no presento mayor dificultad, pues solamente se necesito abrir el archivo con WireShark para analizar los paquetes, nuestra bandera la encontramos al analizar el stream 0 de los TCP:
`p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ 0 1 b 0 a 0 d 6 }`
## Notas adicionales


## Referencias

