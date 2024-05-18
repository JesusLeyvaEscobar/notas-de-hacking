# Objetivo

¿Puedes averiguar qué hay en el registro eax? Coloque su respuesta en el formato de indicador picoCTF: picoCTF{n} donde n es el contenido del registro eax en la base numérica decimal. Si la respuesta fuera 0x11, tu indicador sería picoCTF{17}.
Descargue el volcado de ensamblaje aquí.
1. Los PTR o 'punteros' hacen referencia a una ubicación en la memoria donde se pueden almacenar valores.
## Solución

Haciendole un `cat` al archivo descargado, vemos que contiene:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ cat disassembler-dump0_b.txt
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```
En el registro `eax` tenemos: `DWORD PTR [rbp-0x4]`. Se trata de un apuntador a la instrucción anterior, la cual es: `[rbp-0x4],0x9fe1a`. Este dato: `0x9fe1a` debemos convertirlo de hexadecimal y el resultado lo pondremos dentro de los corchetes en el formato habitual de la bandera.
El resultado fue:
- `picoCTF{654874}`

## Notas adicionales


## Referencias

