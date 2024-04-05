# Objetivo

¿Puedes conseguir la bandera?
Vaya a este sitio web y vea lo que puede descubrir.
1. ¿Cómo se comprueba la contraseña en este sitio web?

## Solución

Si realizamos una inspección del código fuente en la pagina principal, no encontraremos nada raro como la bandera o indicios de la misma, pero al realizar un intento para poder loggearnos, nos redirige a una pagina con el siguiente mensaje:
`Log In Failed` y si realizamos nuevamente, el proceso de inspección desde esta pagina, encontraremos el siguiente código:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Login Page</title>
  </head>
  <body>
    <script src="secure.js"></script>
    
    <p id='msg'></p>
    
    <form hidden action="admin.php" method="post" id="hiddenAdminForm">
      <input type="text" name="hash" required id="adminFormHash">
    </form>
    
    <script type="text/javascript">
      function filter(string) {
        filterPassed = true;
        for (let i =0; i < string.length; i++){
          cc = string.charCodeAt(i);
          
          if ( (cc >= 48 && cc <= 57) ||
               (cc >= 65 && cc <= 90) ||
               (cc >= 97 && cc <= 122) )
          {
            filterPassed = true;     
          }
          else
          {
            return false;
          }
        }
        
        return true;
      }
    
      window.username = "admin";
      window.password = "admin";
      
      usernameFilterPassed = filter(window.username);
      passwordFilterPassed = filter(window.password);
      
      if ( usernameFilterPassed && passwordFilterPassed ) {
      
        loggedIn = checkPassword(window.username, window.password);
        
        if(loggedIn)
        {
          document.getElementById('msg').innerHTML = "Log In Successful";
          document.getElementById('adminFormHash').value = "2196812e91c29df34f5e217cfd639881";
          document.getElementById('hiddenAdminForm').submit();
        }
        else
        {
          document.getElementById('msg').innerHTML = "Log In Failed";
        }
      }
      else {
        document.getElementById('msg').innerHTML = "Illegal character in username or password."
      }
    </script>
    
  </body>
</html>
```
Inspeccionamos algunos de los enlaces que nos proporciona el código, y en la sección de `secure.js`, encontraremos esta sección de código:
```
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```
La contraseña y usuarios correctos para poder acceder en la pagina principal.

Podemos regresar a la pagina principal para ver si estos datos nos sirven de algo o en su defecto sean verdaderos y en efecto, nos deja entrar y nos muestra la bandera:
`picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}`
## Notas adicionales


## Referencias

- view-source:http://saturn.picoctf.net:49386/login.php
- http://saturn.picoctf.net:49386/secure.js