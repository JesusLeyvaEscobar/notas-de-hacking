# Objetivo

A veces es necesario manejar datos de proceso fuera de un archivo. ¿Puedes encontrar una manera de conservar el resultado de este programa y buscar la bandera? Conéctese a `jupiter.challenges.picoctf.org 14291`.
1. Recuerde que el formato de la bandera es picoCTF{XXXX}
2. ¿Qué es una pipa? No, no ese tipo de pipa... Este  [kind](http://www.linfo.org/pipes.html)
## Solución

```
chuyelhacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 14291 
Not a flag either
Again, I really don't think this is a flag
Not a flag either
I don't think this is a flag either
This is defintely not a flag
^C
chuyelhacker-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 14291 | grep picoCTF
picoCTF{digital_plumb3r_ea8bfec7}
^C
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

- `grep`->Nos ayudo como un "filtro" para buscar en un archivo o pagina, cierta palabra pues elimina la información inútil que no coincida con lo que le indiquemos. Se usa: `grep` + `caracter a buscar`.

## Referencias

https://www.linfo.org/pipes.html