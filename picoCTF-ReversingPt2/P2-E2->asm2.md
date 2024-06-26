# Objetivo

¿Qué devuelve asm2(0x4,0x2d)? Envíe la bandera como un valor hexadecimal (comenzando con '0x'). NOTA: Su envío para esta pregunta NO estará en el formato de bandera normal. Fuente
1. condiciones de montaje
## Solución

Esto es lo que encontramos en el archivo que descargamos:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/ReversingPT2]
└─$ cat test.S.1
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret 
```

En esencia, este código lo que hace es un ciclo que se repite 118 veces, hasta que la condición dada sea falsa. Cada y que se realiza un ciclo se le suma 1 a nuestra variable inicial, la cual fue `0x2d`. 

Realizando las 118 iteraciones al valor `0x2d`, obtendremos como resultado `0xa3`. Esta es nuestra bandera resultante.

## Notas adicionales

- `push`-> Empuja un valor en la pila.
- `mov`-> Mueve datos de una ubicación a otra.
- `sub`-> Resta un operando de otro.
- `jmp`-> Salto incondicional a una dirección especificada.
- `add`-> Suma un operando a otro.
- `cmp`-> Compara dos operandos.
- `jle`-> Salto si menor o igual (se utiliza para comparaciones con signo).
- `leave`-> Libera el marco de la pila.
- `ret`-> Retorna de una subrutina.
## Referencias

https://www.cs.virginia.edu/~evans/cs216/guides/x86.html