# Objetivo

¿Puedes conseguir la bandera?
Descarga este binario.
Aquí están las instrucciones de prueba de manejo:
```
- `$ chmod +x gdbme`
- `$ gdb gdbme`
- `(gdb) layout asm`
- `(gdb) break *(main+99)`
- `(gdb) run`
- `(gdb) jump *(main+104)`
```
## Solución

En este reto, debemos usar los comandos que se nos proporcionaron en la descripción. 

Una vez hecho esto, lo abrimos con `gbd`. Nos ayudamos del comando `layout` y en la linea 99 ingresaremos un `break` para que no se ejecute el `sleep` en el código y asi no se brinque la bandera (`break *(main+99)`).

Luego, usaremos `run` y `jump` para brincar a la linea 104 en donde nos arroja la bandera:

- `picoCTF{d3bugg3r_dr1v3_197c378a}`
## Notas adicionales

- `gdb`-> Inicia el depurador de GNU (GDB).
- `info functions`-> Muestra la lista de funciones disponibles en el programa.
- `att intel`-> Cambia el formato de visualización de ensamblado a sintaxis de Intel.
- `set dissasembly-flavor intel`-> Establece la sintaxis de desensamblado en Intel.
- `disassembly main`-> Muestra el ensamblado de la función `main`.
- `break *(main+99)`-> Establece un punto de interrupción en la instrucción número 99 dentro de la función `main`.
- `run`-> Ejecuta el programa.
- `jump *(main+104)`-> Salta a la instrucción número 104 dentro de la función `main`.
## Referencias

