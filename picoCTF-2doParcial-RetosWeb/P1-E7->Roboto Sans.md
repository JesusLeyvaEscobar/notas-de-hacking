# Objetivo

La bandera está en algún lugar de esta aplicación web, no necesariamente en el sitio web. Encuéntralo.
Mira esto.
## Solución

Entramos a la pagina principal, analizamos los archivos robots con la siguiente liga:
`http://saturn.picoctf.net:63195/robots.txt`
Donde nos muestra lo siguiente:
```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

Si lo vemos bien, se trata de código en base64, por lo que recurriremos a usar CyberCheaf para decodificarlo, en lo que nos arrojara la siguiente información:

`flag1.txt`
`js/myfile.txt`

Si buscamos esta segunda linea en la URL, nos manda a la bandera:
`http://saturn.picoctf.net:63195/js/myfile.txt`
`picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}`
## Notas adicionales

## Referencias

- https://gchq.github.io/CyberChef/