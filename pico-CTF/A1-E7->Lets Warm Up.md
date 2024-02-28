# Objetivo

Si te dijera que una palabra comienza con 0x70 en hexadecimal, ¿con qué comenzaría en ASCII?

Envíe su respuesta en nuestro formato de bandera. Por ejemplo, si su respuesta fue "hola", enviaría "picoCTF{hola}" como bandera.

## Solución

```
Usamos el convertidor CyberChef.
Como entrada seleccionamos From Hex, y delimitamos el operador a 0x.

En la entrada ingresamos 0x70 y obtenemos como salida una p.
Esto lo agregamos a la bandera para obtener:
picoCTF{p}
```

## Notas adicionales

## Referencias

https://gchq.github.io/CyberChef/