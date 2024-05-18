# Objetivo

Un músico nos dejó un mensaje. ¿Qué significa?
## Solución

Analizando el archivo obtenido, vemos lo siguiente:

```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ cat message.txt.2
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

Vemos, que aquí encontraremos el formato de la bandera, pero con un pequeño truco y es que al parecer, cada caracter esta dado entre paréntesis, por lo que aparentemente son coordenadas. Como el reto, hace alusion al mundo, asumimos que son coordenadas en el mapa de la tierra. 

Buscare algunas de estas coordenadas en el ya conocido Google Maps, para ver si encontramos algo interesante.

En efecto, se tratan de coordenadas del mundo. Vamos a ordenad en lista las ubicaciones que nos arroja cada coordenada para analizar un poco mejor la informacion:

- `35.028309, 135.753082`-> Nakanocho, Kamigyō-ku, Kioto, Prefectura de Kioto 602-0958, Japón.
- `46.469391, 30.740883`-> Odesa, Odesa Oblast, Ucrania, 65000.
- `39.758949, -84.191605`-> Dayton, OH 45402, Estados Unidos.
- `41.015137, 28.979530`-> Hoca Paşa, 34110 Fatih/Provincia de Estambul, Turquía.
- `24.466667, 54.366669`-> Hazza ' Bin Zayed The First St - Al Manhal - Abu Dhabi - Emiratos Árabes Unidos.
- `3.140853, 101.693207`-> Room 11, Level 2, Bangunan Sulaiman, Jalan Sultan Hishamuddin, 50000 Kuala Lumpur, Malasia.
- `9.005401, 38.763611`-> Kirkos, Adís Abeba, Etiopía.
- `-3.989038, -79.203560`-> Av. Nueva Loja, Loja, Ecuador.
- `52.377956, 4.897070`-> Martelaarsgracht 5, 1012 TM Amsterdam, Países Bajos.
- `41.085651, -73.858467`-> Sleepy Hollow, NY 10591, Estados Unidos.
- `57.790001, -152.407227`-> 111 Lower Mill Bay Rd, Kodiak, AK 99615, Estados Unidos.
- `31.205753, 29.924526`-> Faculty Of Engineering, Al Azaritah WA Ash Shatebi, Bab Sharqi, Alexandria Governorate 5423021, Egipto.

Intentaremos primeramente, ordenas cada ciudad en el su lugar correspondiente segun el formato de la bandera:

picoCTF{ (Kioto) (Odesa) (Dayton) (Istanbul) (Abu Dhabi) (Kuala  Lumpur) _ (Adís Abeba) (Loja) (Amsterdam) (Sleepy Hollow) (Kodiak)(Alexandria) }

Tomare solamente las iniciales de cada ciudad, para ver si el resultado es la bandera:

`picoCTF{KODIAK_ALASKA}`
## Notas adicionales


## Referencias

- https://www.google.com.mx/maps/preview