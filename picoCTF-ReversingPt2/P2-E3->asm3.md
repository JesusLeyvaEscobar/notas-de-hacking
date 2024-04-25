# Objetivo

¿Qué devuelve asm3(0xd73346ed,0xd48672ae,0xd3c8b139)? Envíe la bandera como un valor hexadecimal (comenzando con '0x'). NOTA: Su envío para esta pregunta NO estará en el formato de bandera normal. Fuente
1. más(?) registros
## Solución

Descargaremos y analizamos el archivo que se nos proporciono en el reto:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT2]
└─$ ls
test.S  test.S.1  test.S.2  test.S.3
   
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT2]
└─$ cat test.S.3       
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xa]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xc]
	<+15>:	add    ah,BYTE PTR [ebp+0xd]
	<+18>:	xor    ax,WORD PTR [ebp+0x10]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret   
```

Este código, en esta ocasión hace direccionamientos de 16 y 8 bits a comparación de los retos anteriores, donde eran direccionamientos de 32 bits. Por lo que tendremos que tomar partes del registro y no todo el registro completo, este proceso/análisis puede demorar mas que en los retos pasados, por lo que en esta ocasión optaremos por usar herramientas que nos ayudaran a facilitar este análisis y sobre todo a agilizar lo.

Usaremos, para este reto, un simulador de `assembly` en linea. Solo copiaremos el código del reto y lo pegamos en el apartado correspondiente, después quitaremos los indicadores de linea de código, ya que no son necesarios.

También, debemos poner la función principal y debemos agregar los parámetros que se nos proporcionan en la descripción del reto. Después, vamos a llamar a la funcion `asm3`. Al final, lo que copiamos en la pagina web nos quedaría algo así:

```
start:
	push	0xd3c8b139
	push	0xd48672ae
	push	0xd73346ed
	call asm3


asm3:
	push   ebp
	mov    ebp,esp
	xor    eax,eax
	mov    ah,BYTE PTR [ebp+0xa]
	shl    ax,0x10
	sub    al,BYTE PTR [ebp+0xc]
	add    ah,BYTE PTR [ebp+0xd]
	xor    ax,WORD PTR [ebp+0x10]
	nop
	pop    ebp
	ret
```

En la opción: `Windows`->`Registers`, encontraremos los registros que nos devuelve el programa al finalizar. A nosotros nos interesa en particular, el registro `EAX`, que contiene: `0xC36B`.

Entonces, nuestra bandera fue: `0xC36B`.

## Notas adicionales


## Referencias

- https://carlosrafaelgn.com.br/Asm86/