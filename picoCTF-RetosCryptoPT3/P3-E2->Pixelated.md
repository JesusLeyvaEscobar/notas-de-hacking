# Objetivo

Tengo estas 2 imágenes, ¿puedes hacer una bandera con ellas? revuelto1.png revuelto2.png
- [https://en.wikipedia.org/wiki/Visual_cryptography](https://en.wikipedia.org/wiki/Visual_cryptography)
- Piense en diferentes formas de "apilar" imágenes
## Solución

Nos ayudaremos de una herramienta llamada `stegsolve`, que encontramos en un repositorio en GitHub, la cual debemos instalar con los siguientes comandos:
```
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar
```

Una vez instalada, la mandamos a llamas/la ejecutamos. Los pasos fueron los siguientes:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypto_pt3]
└─$ java -jar /opt/stegsolve.jar 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
```

Nos abrirá una nueva ventana en la que podemos abrir la primera imagen desde:
- `File`->`Open`
Luego, en el apartado `Analyse`->`Image Combiner` y seleccionamos la segunda imagen.

Nos abrirá, nuevamente, otra ventana en donde nos dice que tipo de operación lógicas se va a realizar con las 2 imágenes seleccionadas. La operación lógica, que nos permite combinar estas imágenes para poder visualizar la bandera, es la operación lógica `ADD` , en esta imagen resultante podemos observar la bandera con la leyenda: `picoCTF{0542dc1d}`
## Notas adicionales

- `Cryptografia visual`-> Es una técnica criptográfica que permite cifrar información visual (imágenes, texto, etc.) de tal manera que la información descifrada aparezca como una imagen visual.
## Referencias

- https://imagemagick.org/index.php