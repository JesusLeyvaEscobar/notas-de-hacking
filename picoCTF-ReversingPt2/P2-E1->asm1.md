# Objetivo

¿Qué devuelve asm1(0x2e0)? Envíe la bandera como un valor hexadecimal (comenzando con '0x'). NOTA: Su envío para esta pregunta NO estará en el formato de bandera normal. Fuente
1. condiciones de montaje
## Solución

Analizando el archivo que descargamos en la liga del reto, vemos que obtenemos lo siguiente:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT2]
└─$ cat test.S        
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3fb
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x280
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0xa
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0xa
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x559
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0xa
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xa
	<+60>:	pop    ebp
	<+61>:	ret  
```
Estas, son instrucciones en ensamblador, que ya deberíamos conocer desde semestres pasados. Vamos a verificar que 

```
[ebp    ] < ebp < esp
[ret    ] ebp + 0x4
[0x2e0  ] ebp + 0x8   

[0x2e0  ] eax
asm1:
        <+0>:   push   ebp
        <+1>:   mov    ebp,esp
        <+3>:   cmp    DWORD PTR [ebp+0x8],0x3fb
        <+10>:  jg     0x512 <asm1+37>
        <+12>:  cmp    DWORD PTR [ebp+0x8],0x280
        <+19>:  jne    0x50a <asm1+29>
        <+21>:  mov    eax,DWORD PTR [ebp+0x8]
        <+24>:  add    eax,0xa
        <+27>:  jmp    0x529 <asm1+60>
        <+29>:  mov    eax,DWORD PTR [ebp+0x8]
        <+32>:  sub    eax,0xa
        <+35>:  jmp    0x529 <asm1+60>
        <+37>:  cmp    DWORD PTR [ebp+0x8],0x559
        <+44>:  jne    0x523 <asm1+54>
        <+46>:  mov    eax,DWORD PTR [ebp+0x8]
        <+49>:  sub    eax,0xa
        <+52>:  jmp    0x529 <asm1+60>
        <+54>:  mov    eax,DWORD PTR [ebp+0x8]
        <+57>:  add    eax,0xa
        <+60>:  pop    ebp
        <+61>:  ret  
```
Haremos las operaciones correspondientes:

`<+3>:   cmp    DWORD PTR [ebp+0x8],0x3fb`
 Compara `0x3fb` con el contenido de `ebp + 0x8` que es `[0x2e0  ]`
 y al hacer las operaciones en python obtenemos:
```
>>> 0x2e0 > 0x3fb
False
```
Como esta comparación no es verdadera, no va a realizar la siguiente instrucción que es:
`jg     0x512 <asm1+37>`
sino que va a la siguiente comparacion de 
`cmp    DWORD PTR [ebp+0x8],0x280` 
con el mismo contenido de `ebp + 0x8` que es `[0x2e0  ]`
y al realizarlo en python obtenemos:
```
>>> 0x2e0 > 0x280
True
```
Y asi realizaremos las operaciones necesarias segun las condiciones de comparación.

Al final, el registro `eax` almacena nuestro resultado, el cual fue: `0x2d6`.

Todas operaciones que se realizaron en python fueron las siguientes:
```
┌──(jesus㉿KaliJesus)-[~]
└─$ python3
Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 0x2e0 > 0x3fb
False
>>> 0x2e0 > 0x280
True
>>> hex (0x2e0 - 0xa)
'0x2d6
>>> 
```

## Notas adicionales

- `MOV`-> Copia el elemento de datos al que se hace referencia por su segundo operando en la ubicación mencionada por su primer operando. Mientras que los movimientos de registro a registro son posibles, dirija memoria a memoria los movimientos no lo son.
- `JMP`-> La instrucción JMP proporciona un nombre de etiqueta donde el flujo de control se transfiere inmediatamente. Existen varios tipos de Saltos, con diferentes condiciones para realizar la acion.
- `DWORD`-> 
- `PUSH`-> Coloca su operando en la parte superior de la pila compatible con hardware en la memoria.
- `POP`-> Elimina el elemento de datos de 4 bytes de la parte superior de la pila soportada por hardware en el operando especificado.
- `EBP`->Apuntador que se queda en la parte de abajo de una pila.
## Referencias

https://www.cs.virginia.edu/~evans/cs216/guides/x86.html