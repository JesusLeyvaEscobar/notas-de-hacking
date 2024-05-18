# Objetivo

¿Puedes averiguar qué hay en el registro eax? Coloque su respuesta en el formato de indicador picoCTF: picoCTF{n} donde n es el contenido del registro eax en la base numérica decimal. Si la respuesta fuera 0x11, tu indicador sería picoCTF{17}.
Descargue el volcado de ensamblaje aquí.
1. Como ocurre con la mayoría de los ensamblajes, hay mucho ruido en el volcado de instrucciones. Encuentre la única línea que pertenece a esta pregunta y no lo dude.
## Solución

Analizando el archivo descargado:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ ls          
asciiftw  crackme.py  disassembler-dump0_a.txt  enc  keygenme-trial.py
                                                                              
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ cat disassembler-dump0_a.txt                                       
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

Vemos que en el registro EAX tenemos el dato 0x30 en hexadecimal, y como el reto nos dice que la bandera esta en el formato `picoCTF{n}` donde `n` es el dato de EAX pero convertido desde hexadecimal. Nuestra bandera quedaria de la siguiente forma:

`picoCTF{48}`
## Notas adicionales


## Referencias

