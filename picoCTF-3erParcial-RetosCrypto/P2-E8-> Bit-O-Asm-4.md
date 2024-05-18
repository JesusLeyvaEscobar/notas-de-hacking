# Objetivo

¿Puedes averiguar qué hay en el registro eax? Coloque su respuesta en el formato de indicador picoCTF: picoCTF{n} donde n es el contenido del registro eax en la base numérica decimal. Si la respuesta fuera 0x11, tu indicador sería picoCTF{17}.
Descargue el volcado de ensamblaje aquí.
1. No le digas a nadie que te dije esto, pero puedes resolver este problema sin comprender la relación de comparación/salto.
2. Por supuesto, si eres realmente bueno, sólo necesitarás un intento para resolver este problema.
## Solución

Vemos el código descargado:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ cat disassembler-dump0_d.txt                                     
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

En el registro `eax` tiene el valor final despues de que se realizan algunas operaciones en la funcion.

La variable inicial que se almacena en `[rbp-0x4]` contiene el valor `0x9fe1a`. Luego se realiza una comparación con `0x2710` si este dato inicial es menor que `0x2710`, se le va a sumar el valor `0x65`; en caso de que fuera mayor, entonces se le resta este mismo valor `0x65`.

Realizaremos las operaciones correspondientes en python para obtener el resultado final:

```
┌──(jesus㉿KaliJesus)-[~]
└─$ python3
Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> hex(0x2710>=0x9fe1a)
'0x0'
>>> hex(0x9fe1a-0x65)
'0x9fdb5'
>>> 
```
Como vimos, el resultado si es menor, por lo que debimos restarle `0x65`.

Ahora solo realizamos la conversion y adjuntamos el resultado a nuestro formato de la bandera:
`
```
>>> ascii(0x9fdb5)
'654773'
>>> 
```

Obtenemos como resultado final:
- `picoCTF{654773}`
## Notas adicionales


## Referencias

