# Objetivo

¿Puedes averiguar qué hay en el registro eax? Coloque su respuesta en el formato de indicador picoCTF: picoCTF{n} donde n es el contenido del registro eax en la base numérica decimal. Si la respuesta fuera 0x11, tu indicador sería picoCTF{17}.
Descargue el volcado de ensamblaje aquí.
1. No todo lo que aparece en este listado de desmontaje es óptimo.
## Solución

Analizando el archivo descargado:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ cat disassembler-dump0_c.txt
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]
<+32>:    imul   eax,DWORD PTR [rbp-0x8]
<+36>:    add    eax,0x1f5
<+41>:    mov    DWORD PTR [rbp-0x4],eax
<+44>:    mov    eax,DWORD PTR [rbp-0x4]
<+47>:    pop    rbp
<+48>:    ret
```

Observamos que este código realiza operaciones por lo que, con la ayuda de python realizamos las operaciones que pide:

```
──(jesus㉿KaliJesus)-[~]
└─$ python3
Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> hex(0x9fe1a*0x4)
'0x27f868'
>>> hex(0x27f868+0x1f5)
'0x27fa5d'
>>> ascii(0x27fa5d)
'2619997'
>>> 
```

El resultado, lo juntamos al formato que ya conocemos de la bandera y obtenemos:

`picoCTF{2619997}`
## Notas adicionales


## Referencias

