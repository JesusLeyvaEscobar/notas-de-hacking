# Objetivo

Hemos recuperado un archivo binario y uno de texto. ¿Puedes invertir la bandera?
1. objdump y Gihdra son algunas herramientas que podrían ayudar con esto
## Solución

Analizamos los archivos descargados:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ file rev           
rev: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=523d51973c11197605c76f84d4afb0fe9e59338c, not stripped

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ file rev_this
rev_this: ASCII text, with no line terminators

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ cat rev_this      
picoCTF{w1{1wq84fb<1>49} 
```
El archivo `rev_this` tiene la bandera cifrada y con el otro archivo `rev` nos ayudaremos para descifrarla.

Si vemos las pistas, nos dice que podemos ayudarnos de algunas herramientas para descifrar el la bandera. Comenzando por `objdump`.

Desensamblamos la funcion `main` con la ayuda del siguiente comando:
``
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ objdump -D rev -M intel | grep '<main>:' -A50 
0000000000001185 <main>:
    1185:	55                   	push   rbp
    1186:	48 89 e5             	mov    rbp,rsp
    1189:	48 83 ec 50          	sub    rsp,0x50
    118d:	48 8d 35 74 0e 00 00 	lea    rsi,[rip+0xe74]        # 2008 <_IO_stdin_used+0x8>
    1194:	48 8d 3d 6f 0e 00 00 	lea    rdi,[rip+0xe6f]        # 200a <_IO_stdin_used+0xa>
    119b:	e8 d0 fe ff ff       	call   1070 <fopen@plt>
    11a0:	48 89 45 e8          	mov    QWORD PTR [rbp-0x18],rax
    11a4:	48 8d 35 68 0e 00 00 	lea    rsi,[rip+0xe68]        # 2013 <_IO_stdin_used+0x13>
    11ab:	48 8d 3d 63 0e 00 00 	lea    rdi,[rip+0xe63]        # 2015 <_IO_stdin_used+0x15>
    11b2:	e8 b9 fe ff ff       	call   1070 <fopen@plt>
    11b7:	48 89 45 e0          	mov    QWORD PTR [rbp-0x20],rax
    11bb:	48 83 7d e8 00       	cmp    QWORD PTR [rbp-0x18],0x0
    11c0:	75 0c                	jne    11ce <main+0x49>
    11c2:	48 8d 3d 57 0e 00 00 	lea    rdi,[rip+0xe57]        # 2020 <_IO_stdin_used+0x20>
    11c9:	e8 62 fe ff ff       	call   1030 <puts@plt>
    11ce:	48 83 7d e0 00       	cmp    QWORD PTR [rbp-0x20],0x0
    11d3:	75 0c                	jne    11e1 <main+0x5c>
    11d5:	48 8d 3d 7e 0e 00 00 	lea    rdi,[rip+0xe7e]        # 205a <_IO_stdin_used+0x5a>
    11dc:	e8 4f fe ff ff       	call   1030 <puts@plt>
    11e1:	48 8b 55 e8          	mov    rdx,QWORD PTR [rbp-0x18]
    11e5:	48 8d 45 b0          	lea    rax,[rbp-0x50]
    11e9:	48 89 d1             	mov    rcx,rdx
    11ec:	ba 01 00 00 00       	mov    edx,0x1
    11f1:	be 18 00 00 00       	mov    esi,0x18
    11f6:	48 89 c7             	mov    rdi,rax
    11f9:	e8 42 fe ff ff       	call   1040 <fread@plt>
    11fe:	89 45 dc             	mov    DWORD PTR [rbp-0x24],eax
    1201:	83 7d dc 00          	cmp    DWORD PTR [rbp-0x24],0x0
    1205:	7f 0a                	jg     1211 <main+0x8c>
    1207:	bf 00 00 00 00       	mov    edi,0x0
    120c:	e8 6f fe ff ff       	call   1080 <exit@plt>
    1211:	c7 45 f8 00 00 00 00 	mov    DWORD PTR [rbp-0x8],0x0
    1218:	eb 23                	jmp    123d <main+0xb8>
    121a:	8b 45 f8             	mov    eax,DWORD PTR [rbp-0x8]
    121d:	48 98                	cdqe
    121f:	0f b6 44 05 b0       	movzx  eax,BYTE PTR [rbp+rax*1-0x50]
    1224:	88 45 ff             	mov    BYTE PTR [rbp-0x1],al
    1227:	0f be 45 ff          	movsx  eax,BYTE PTR [rbp-0x1]
    122b:	48 8b 55 e0          	mov    rdx,QWORD PTR [rbp-0x20]
    122f:	48 89 d6             	mov    rsi,rdx
    1232:	89 c7                	mov    edi,eax
    1234:	e8 27 fe ff ff       	call   1060 <fputc@plt>
    1239:	83 45 f8 01          	add    DWORD PTR [rbp-0x8],0x1
    123d:	83 7d f8 07          	cmp    DWORD PTR [rbp-0x8],0x7
    1241:	7e d7                	jle    121a <main+0x95>
    1243:	c7 45 f4 08 00 00 00 	mov    DWORD PTR [rbp-0xc],0x8
    124a:	eb 43                	jmp    128f <main+0x10a>
    124c:	8b 45 f4             	mov    eax,DWORD PTR [rbp-0xc]
    124f:	48 98                	cdqe
    1251:	0f b6 44 05 b0       	movzx  eax,BYTE PTR [rbp+rax*1-0x50]
```
Lo que podemos rescatar de desensamblar  el `main`, es que los registros han cambiado de nombre (al cambiar de 32 a 64 bits, inician con una R en lugar de una E). 
Después de ver y analizar este código, vamos a usar `Ghidra` para continuar con el descifrado de la bandera.
Creamos un nuevo proyecto dentro de la aplicación de `Ghidra`, para después importar el archivo binario del reto. 
Buscamos la función `main` y veremos la función en ensamblador pero también veremos un código de la función similar al lenguaje C.

Si lo analizamos, en lenguaje C, lo que hace de manera general es, cambiar la una parte de la bandera con la ayuda de un `and` para cambiar el dato según sea par o impar. Para poder decodificar, nos ayudaremos de un programa en python.

Creamos un archivo:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ nano exp.py 
```
en el cual pondremos el siguiente código:
```
d = open("rev_this").read()
flag = ""
for j in range(8, 23):
        if j &  1 == 0:
                flag += chr(ord(d[j]) - 5)
        else:
                flag += chr(ord(d[j]) + 2)
print(flag)
```
Y lo ejecutamos:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ python3 exp.py
r3v3rs36ad73964
```
Nos regresa solamente la parte que se decodifico, por lo que a esto tenemos que juntarlo al formato que ya conocemos de la bandera, obteniendo asi:

- `picoCTF{r3v3rs36ad73964}`
## Notas adicionales

- `objdump`-> Muestra información sobre uno o más archivos de objetos.
	- `-D`-> Desensambla todo.
	- `-M`-> Pase la información específica del objetivo al desensamblador.
- `Ghidra`-> Un conjunto de herramientas de ingeniería inversa de software (SRE) desarrollado por la Dirección de Investigación de la NSA en apoyo de la misión de ciberseguridad.
## Referencias

- https://man7.org/linux/man-pages/man1/objdump.1.html
- https://ghidra-sre.org/