# Objetivo

El nombre del juego es velocidad. ¿Eres lo suficientemente rápido para resolver este problema y mantenerlo por encima de las 50 mph? necesidad de la velocidad.
1. ¿Cuál es la clave final?

## Solución

Descargamos el archivo que nos dan en la descripción del reto.
Lo analizamos:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ file need-for-speed
need-for-speed: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2d0d401d07683664113690a7fb94413a0039d228, not stripped
```
Vemos que se trata de un archivo de 64bits, por lo que le daremos permisos para después poder ejecutarlo.
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ chmod +x need-for-speed

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ ./need-for-speed
Keep this thing over 50 mph!
============================

Creating key...
Not fast enough. BOOM!
```
Vemos que genera la key, pero después de eso termina le programa.

Haremos un vaciado de memoria con `objdump`:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT3]
└─$ objdump -D need-for-speed -M intel |  grep '<main>:' -A20
000000000000091a <main>:
 91a:	55                   	push   rbp
 91b:	48 89 e5             	mov    rbp,rsp
 91e:	48 83 ec 10          	sub    rsp,0x10
 922:	89 7d fc             	mov    DWORD PTR [rbp-0x4],edi
 925:	48 89 75 f0          	mov    QWORD PTR [rbp-0x10],rsi
 929:	b8 00 00 00 00       	mov    eax,0x0
 92e:	e8 a5 ff ff ff       	call   8d8 <header>
 933:	b8 00 00 00 00       	mov    eax,0x0
 938:	e8 f2 fe ff ff       	call   82f <set_timer>
 93d:	b8 00 00 00 00       	mov    eax,0x0
 942:	e8 36 ff ff ff       	call   87d <get_key>
 947:	b8 00 00 00 00       	mov    eax,0x0
 94c:	e8 5b ff ff ff       	call   8ac <print_flag>
 951:	b8 00 00 00 00       	mov    eax,0x0
 956:	c9                   	leave
 957:	c3                   	ret
 958:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
 95f:	00 

0000000000000960 <__libc_csu_init>:
```
Nos daremos cuenta que tiene un timer que es el que establece un tiempo muy corto donde se genera la llave pero no logra imprimirlo porque el timer no lo permite. 

Lo que haremos es abrir el programa con `GDB`:
```
(gdb) disassemble main
Dump of assembler code for function main:
   0x000000000000091a <+0>:	push   rbp
   0x000000000000091b <+1>:	mov    rbp,rsp
   0x000000000000091e <+4>:	sub    rsp,0x10
   0x0000000000000922 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000000000000925 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000000929 <+15>:	mov    eax,0x0
   0x000000000000092e <+20>:	call   0x8d8 <header>
   0x0000000000000933 <+25>:	mov    eax,0x0
   0x0000000000000938 <+30>:	call   0x82f <set_timer>
   0x000000000000093d <+35>:	mov    eax,0x0
   0x0000000000000942 <+40>:	call   0x87d <get_key>
   0x0000000000000947 <+45>:	mov    eax,0x0
   0x000000000000094c <+50>:	call   0x8ac <print_flag>
   0x0000000000000951 <+55>:	mov    eax,0x0
   0x0000000000000956 <+60>:	leave
   0x0000000000000957 <+61>:	ret
End of assembler dump.
(gdb)
```

Nos encontraremos con un `timer` el cual termina el programa muy rápido, entonces tenemos que poner un `break` en dicha linea:
```
(gdb) break main
Breakpoint 1 at 0x91e
(gdb) run
Starting program: /home/jesus/Desktop/github/notas-de-hacking/ReversingPT3/need-for-speed 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x000055555540091e in main ()
(gdb) disassemble main
Dump of assembler code for function main:
   0x000055555540091a <+0>:	push   rbp
   0x000055555540091b <+1>:	mov    rbp,rsp
=> 0x000055555540091e <+4>:	sub    rsp,0x10
   0x0000555555400922 <+8>:	mov    DWORD PTR [rbp-0x4],edi
   0x0000555555400925 <+11>:	mov    QWORD PTR [rbp-0x10],rsi
   0x0000555555400929 <+15>:	mov    eax,0x0
   0x000055555540092e <+20>:	call   0x5555554008d8 <header>
   0x0000555555400933 <+25>:	mov    eax,0x0
   0x0000555555400938 <+30>:	call   0x55555540082f <set_timer>
   0x000055555540093d <+35>:	mov    eax,0x0
   0x0000555555400942 <+40>:	call   0x55555540087d <get_key>
   0x0000555555400947 <+45>:	mov    eax,0x0
   0x000055555540094c <+50>:	call   0x5555554008ac <print_flag>
   0x0000555555400951 <+55>:	mov    eax,0x0
   0x0000555555400956 <+60>:	leave
   0x0000555555400957 <+61>:	ret
End of assembler dump.
(gdb) 
```
Nos damos cuenta, al desensamblar la funcion, que ahi se encuentra el pauntador. Ahora que estamos en ejecucion, vamos a mandar a llamar directamente las funciones `get_key` y `get_flag` para ver si obtenemos la bandera:
```
(gdb) call (int) get_key()
Creating key...
Finished
$1 = 9
(gdb) call (int) print_flag()
Printing flag:
PICOCTF{Good job keeping bus #1f2ac4ec speeding along!}
$2 = 56
(gdb)
```
De este modo, encontraremos la bandera.
## Notas adicionales

- `objdump`-> Muestra información sobre uno o más archivos de objetos.
	- `-D`-> Desensambla todo.
	- `-M`-> Pase la información específica del objetivo al desensamblador.
- `GDB`-> El depurador de proyectos GNU, le permite ver lo que está pasando 'dentro' de otro programa mientras se ejecuta - o lo que otro programa estaba haciendo en el momento en que se estrelló.
## Referencias

- https://www.sourceware.org/gdb/
