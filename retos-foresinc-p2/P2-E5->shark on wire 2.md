# Objetivo

Encontramos esta captura de paquete. Recupera la bandera que fue sustraída de la red.
## Solución

Descargamos el archivo
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/sharkonwire2]
└─$ ls
capture.pcap
```
Vemos que es un archivo `.pcap` por lo que usaremos de nuevo la herramienta Wireshark.
Si lo analizamos, vemos que en el stream 32 tenemos el dato: `START` y en el 60: `FINISH`, estos rango de streams tienen en comun que todos van al mismo puerto.
Usamos un filtro para que solo muestre los archivos enviados al puerto 22.
Observamos que el dato enviado esta en codigo ASCII sumandole 5000, entonces debemos hacer algo que nos permita traducir este codigo ASCII. Pero primero exportaremos los paquetes capturados enviados al puerto 22, como texto plano:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/sharkonwire2]
└─$ ls
capture.pcap  data.txt
```
Vamos a ingresar el siguiente comando para obtener solamente los dato que nosotros queremos rescatar de la captura de paquetes:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/picoCTF/foresinc_p2/sharkonwire2]
└─$ cat data.txt | grep UDP | awk '{print $7}' | cut -c2- | grep -v 000
112
105
099
111
067
084
070
123
112
049
076
076
102
051
114
051
100
095
100
097
116
097
095
118
049
097
095
115
116
051
103
048
125
```
Despues, solo usamos el CyberChef para convertir estos datos Decimales a ASCII y delimitamos que va a ser por linea la codificacion, obtenemos lo siguiente:
`picoCTF{p1LLf3r3d_data_v1a_st3g0}`

## Notas adicionales

- `grep`-> Filtra lo que le indiquemos en seguida.
- `awk`-> Permite explorar archivos y llevar a cabo determinadas acciones.
- `cut`-> Borra secciones, campos o caracteres de la salida de un comando o de cada una de las lineas de un fichero de texto.
## Referencias

