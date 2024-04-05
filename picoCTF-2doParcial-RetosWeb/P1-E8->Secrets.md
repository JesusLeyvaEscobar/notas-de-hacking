# Objetivo

Tenemos varias páginas ocultas. ¿Puedes encontrar el que tiene la bandera?
El sitio web se está ejecutando aquí.
1. carpetas carpetas carpetas
## Solución

- Primera inspección:
Aquí, observamos en el código:
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <meta name="description" content="" />
    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
    <!-- title -->
    <title>home</title>
    <!-- css -->
    <link href="secret/assets/index.css" rel="stylesheet" />
  </head>
  <body>
    <!-- ***** Header Area Start ***** -->
    <div class="topnav">
      <a class="active" href="#home">Home</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
    </div>

    <div class="imgcontainer">
      <img
        src="secret/assets/DX1KYM.jpg"
        alt="https://www.alamy.com/security-safety-word-cloud-concept-image-image67649784.html"
        class="responsive"
      />
      <div class="top-left">
        <h1>If security wasn't your job, would you do it as a hobby?</h1>
      </div>
    </div>
  </body>
</html>
```
Que probablemente, podemos acceder a diferentes carpetas: En la sección de `sources`, vemos como encontramos una posible nueva dirección/carpeta llamada `secret`, lo integramos al URL y corroboramos que funcione.

- Segunda inspección:
En efecto,que se trata de una nueva carpeta a la cual accedemos con la siguiente dirección:
`http://saturn.picoctf.net:62050/secret/`, nos arroja el siguiente código al inspeccionar:
```
<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="stylesheet" href="hidden/file.css" />
  </head>

  <body>
    <h1>Finally. You almost found me. you are doing well</h1>
    <img src="https://media1.tenor.com/images/0a6aff9f825af62c05adfbd75039cc7b/tenor.gif?itemid=4648337" alt="Something Like That GIF - Andy Parksandrecreation Wtf GIFs" style="max-width: 833px; background-color: rgb(151, 121, 85);" width="833" height="937.125">
  </body>
</html>
```
De nueva cuenta, observamos que posiblemente podemos tener acceso a una nueva carpeta llamada `hidden`, así que hacemos el mismo procedimiento que en paso el anterior.

- Tercera inspección:
Obtenemos una nueva posible/carpeta con los datos de la inspección anterior: `http://saturn.picoctf.net:62050/secret/hidden/`.
```
<!DOCTYPE html>
<html>
  <head>
    <title>LOGIN</title>
    <!-- css -->
    <link href="superhidden/login.css" rel="stylesheet" />
  </head>
  <body>
    <form>
```
Aquí, nuevamente podemos observar que se trata de una nueva ruta (`superhidden`), asi que realizamos el mismo procedimiento. 

- Cuarta inspección:
Nuestra nueva dirección: `http://saturn.picoctf.net:62050/secret/hidden/superhidden/`, funciona correctamente, y nos da indicios de que llegamos a la bandera, solo inspeccionamos una ultima vez:
```
<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="stylesheet" href="mycss.css" />
  </head>

  <body>
    <h1>Finally. You found me. But can you see me</h1>
    <h3 class="flag">picoCTF{succ3ss_@h3n1c@10n_51b260fe}</h3>
  </body>
</html>
```
Encontramos la carpeta correcta.
## Notas adicionales


## Referencias

