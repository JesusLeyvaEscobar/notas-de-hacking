# Objetivo

¿Puedes averiguar qué hay en el registro eax al final de la función principal? Coloque su respuesta en el formato de indicador picoCTF: picoCTF{n} donde n es el contenido del registro eax en la base numérica decimal. Si la respuesta fuera 0x11, tu indicador sería picoCTF{17}.
Depura esto.
1. Puede calcular eax usted mismo o puede establecer un punto de interrupción después del cálculo e inspeccionar eax para permitir que el programa haga el trabajo pesado por usted.
## Solución

Observamos el programa:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosReversing]
└─$ gdb -q debugger0_b                                  
Reading symbols from debugger0_b...
(No debugging symbols found in debugger0_b)
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000401106 <+0>:	endbr64
   0x000000000040110a <+4>:	push   %rbp
   0x000000000040110b <+5>:	mov    %rsp,%rbp
   0x000000000040110e <+8>:	mov    %edi,-0x14(%rbp)
   0x0000000000401111 <+11>:	mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:	movl   $0x1e0da,-0x4(%rbp)
   0x000000000040111c <+22>:	movl   $0x25f,-0xc(%rbp)
   0x0000000000401123 <+29>:	movl   $0x0,-0x8(%rbp)
   0x000000000040112a <+36>:	jmp    0x401136 <main+48>
   0x000000000040112c <+38>:	mov    -0x8(%rbp),%eax
   0x000000000040112f <+41>:	add    %eax,-0x4(%rbp)
   0x0000000000401132 <+44>:	addl   $0x1,-0x8(%rbp)
   0x0000000000401136 <+48>:	mov    -0x8(%rbp),%eax
   0x0000000000401139 <+51>:	cmp    -0xc(%rbp),%eax
   0x000000000040113c <+54>:	jl     0x40112c <main+38>
   0x000000000040113e <+56>:	mov    -0x4(%rbp),%eax
   0x0000000000401141 <+59>:	pop    %rbp
   0x0000000000401142 <+60>:	ret
End of assembler dump.
```

Este codigo ejecuta un bucle desde 0 a 606, en cata iteracion `eax` se suma a la direccion `[rbp-0x4]`. Esta direccion, inicialmente tiene un valor que cambiara con cada iteracion. El valor final despues de ejecutar el conteo, es: `307019`

El formato final de la bandera quedaria:
`picoCTF{307019}`
## Notas adicionales


## Referencias

