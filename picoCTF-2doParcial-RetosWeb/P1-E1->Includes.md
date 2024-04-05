# Objetivo

¿Puedes conseguir la bandera?
Vaya a este sitio web y vea lo que puede descubrir.
1. ¿Hay más código del que muestra inicialmente el inspector?
## Solución

Debemos inspeccionar el código fuente de la pagina a la cual nos redirige el reto.
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>On Includes</title>
  </head>
  <body>
    <script src="script.js"></script>
  
    <h1>On Includes</h1>
    <p>Many programming languages and other computer files have a directive, 
       often called include (sometimes copy or import), that causes the 
       contents of a second file to be inserted into the original file. These 
       included files are called copybooks or header files. They are often used
       to define the physical layout of program data, pieces of procedural code
       and/or forward declarations while promoting encapsulation and the reuse
       of code.</p>
    <br>
    <p> Source: Wikipedia on Include directive </p>
    <button type="button" onclick="greetings();">Say hello</button>
  </body>
</html>
```
Observamos como en el código vemos un par de links que, al darles clic o inspeccionarlos nos redirige a una nueva pestaña:
1. El primero: `style.css` nos muestra la siguiente informacion: ```
```
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```
2. Para el segundo: `scripts.js`, vemos la siguiente:
```
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_6edef411}
```
## Notas adicionales

Muchas veces encontraremos información que nos puede ser de ayuda al inspeccionar las paginas que queramos y se encuentra escondida sin que nos percatemos.
## Referencias

1. http://saturn.picoctf.net:61941/
2. view-source:http://saturn.picoctf.net:61941/
3. http://saturn.picoctf.net:61941/style.css
4. http://saturn.picoctf.net:61941/script.js