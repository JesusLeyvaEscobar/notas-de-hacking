# Objetivo

¿Puedes averiguar qué hay en el registro eax al final de la función principal? Coloque su respuesta en el formato de indicador picoCTF: picoCTF{n} donde n es el contenido del registro eax en la base numérica decimal. Si la respuesta fuera 0x11, tu indicador sería picoCTF{17}.
Desmonta esto.
1. ¡gdb es un muy buen depurador para usar en este problema y muchos otros!
2. main es en realidad un símbolo reconocido que se puede usar con los comandos gdb
## Solución

Analizando el codigo:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ gdb -q debugger0_a
Reading symbols from debugger0_a...
(No debugging symbols found in debugger0_a)
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000001129 <+0>:	endbr64
   0x000000000000112d <+4>:	push   %rbp
   0x000000000000112e <+5>:	mov    %rsp,%rbp
   0x0000000000001131 <+8>:	mov    %edi,-0x4(%rbp)
   0x0000000000001134 <+11>:	mov    %rsi,-0x10(%rbp)
   0x0000000000001138 <+15>:	mov    $0x86342,%eax
   0x000000000000113d <+20>:	pop    %rbp
   0x000000000000113e <+21>:	ret
End of assembler dump.
(gdb) 
```

Si lo analizamos vemos que en EAX tenemos una carga del valor `0x86342`. Por lo tanto, el resultado es: `549698`.

Acomodando el formato de la bandera, obtenemos:

- `picoCTF{549698}`
## Notas adicionales


## Referencias

