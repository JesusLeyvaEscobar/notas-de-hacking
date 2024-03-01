# Objetivo

Hay un buen programa con el que puedes hablar usando este comando en un shell: $ nc mercury.picoctf.net 22902, pero no habla inglés...
## Solución

```
chuyelhacker-picoctf@webshell:~$ nc mercury.picoctf.net 22902
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
100 
51 
100 
102 
100 
54 
100 
102 
125 
10 
^C
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

Se uso la pagina de traducción de código Cybercheaf usando la formula:
- From Charcode
- Base: 10
Se obtuvo: `picoCTF{g00d_k1tty!_n1c3_k1tty!_d3dfd6df}`.
- `nc`->Nos ayudo a acceder a puertos TCP/UDP, ya sea de la misma maquina o de otras maquinas remotas.
## Referencias

https://gchq.github.io/CyberChef/