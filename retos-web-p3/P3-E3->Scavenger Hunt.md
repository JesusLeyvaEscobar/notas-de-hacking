# Objetivo

Hay información interesante escondida en este sitio http://mercury.picoctf.net:39491/. ¿Puedes encontrarlo?
1. Deberías tener suficientes pistas para encontrar los archivos, no ejecutes fuerza bruta.
## Solución

Inspeccionamos la pagina web, con click derecho y viendo el codigo fuente de la pagina, obtenemos lo siguiente:
```
		JS (JavaScript)|
	</p>|
<!-- Here's the first part of the flag: picoCTF{t -->|
	</div>|
```
Observamos que nos dejan la primera parte de la bandera en una sección de este código.

Si continuamos analizando el código, veremos que se encuentra, en la 6ta linea de código, un enlace a la hoja de estilos. Damos click sobre ella y encontraremos lo siguiente:
```
#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }

/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```
En las ultimas 3 lineas del código, encontramos la segunda parte de la bandera. Ya no hay mas que hacer en este sitio de la hoja de estilos, por lo que regresamos.

En la siguiente linea consecutiva a donde encontramos el link de la hoja de estilos, veremos que esta otro enlace para inspeccionar el JavaScript. Aqui veremos lo siguiente:
```
/* How can I keep Google from indexing my website? */
```
La ultima linea del código, es este comentario. Recordemos que este tema ya lo habíamos visto cuando resolvimos retos relacionados con Robots, por lo que regresamos a la pagina principal y buscamos los robots. El enlace utilizado es el siguiente:
	`http://mercury.picoctf.net:39491/robots.txt`
Y lo que nos desglosa es lo siguiente:
```
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```
Una tercera parte de la bandera y una pista mas para encontrar la siguiente parte de la misma.
Esta ultima pista, nos incita a buscar los archivos que se encuentran en directorio `htaccess` de los servidores de apache. Vamos a editar la pagina principal ingresando lo siguiente:
`http://mercury.picoctf.net:39491/.htaccess`
Encontramos la siguiente configuración:
```
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```
La ultima pista, nos indica que debemos indagar en los archivos que se almacenan en MAC, mas en especifico hablaremos del archivo `.DS_Store` que contiene información de la configuración de la carpeta en la cual se encuentre este archivo.
Vamos a ingresar esta extensión al enlace original para ver si tenemos acceso a este archivo:
`http://mercury.picoctf.net:39491/.DS_Store`
Y nos arroja lo siguiente:
`Congrats! You completed the scavenger hunt. Part 5: _f7ce8828}`

Todas estas secciones adicionales al enlace de la pagina original, no deberían ser accesibles pero para este reto, pues se omitió el tema de seguridad.

La contraseña al final, fue: `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_f7ce8828}`
## Notas adicionales

- Los ficheros `.htaccess` facilitan una forma de realizar cambios en la configuración en contexto directorio.
- En mac, un archivo`.DS_Store` es aquel que almacena atributos personalizados de la carpeta que lo contiene, como la posición de los iconos o la imagen de fondo.
## Referencias

Inspeccion del código fuente:
- view-source:http://mercury.picoctf.net:39491/
Inspeccion de la hoja de estilos:
- http://mercury.picoctf.net:39491/mycss.css
Inspeccion del JavaScript:
- http://mercury.picoctf.net:39491/myjs.js
Inpeccion de los Robots:
- http://mercury.picoctf.net:39491/robots.txt
Informacion sobre los Servidores de Apache:
- https://httpd.apache.org/docs/2.4/es/howto/htaccess.html
Informacion obtenida sobre los archivos `.DS_Store` para MAC:
- https://es.wikipedia.org/wiki/.DS_Store