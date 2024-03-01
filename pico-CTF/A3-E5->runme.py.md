# Objetivo

Ejecute el script `runme.py` para obtener la bandera. Descargue el script con su navegador o con `wget` en webshell.
1. Si tiene Python en su computadora, puede descargar el script normalmente y ejecutarlo. De lo contrario, utilice el comando `wget` en el webshell.
2. Para usar `wget` en el webshell, primero haga clic derecho en el enlace de descarga y seleccione "Copiar enlace" o "Copiar dirección de enlace".
3. Escriba todo después del signo de dólar en el shell web: `$ wget,` luego pegue el enlace después del espacio después de `wget` y presione Entrar. ¡Esto descargará el script en el webshell para que puedas ejecutarlo!
4. Finalmente, para ejecutar el script, escriba todo lo que aparece después del signo de dólar y luego presione Intro: `$ python3 runme.py` ¡Debería tener la bandera ahora!
## Solución

```
chuyelhacker-picoctf@webshell:~$ ls
README.txt  runme.py
chuyelhacker-picoctf@webshell:~$ python3 runme.py 
picoCTF{run_s4n1ty_run}
chuyelhacker-picoctf@webshell:~$ ^C
chuyelhacker-picoctf@webshell:~$ 
```

## Notas adicionales

`python3`->Ejecuta scripts de phyton (Version3).
## Referencias