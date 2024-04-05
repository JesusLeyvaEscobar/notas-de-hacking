# Objetivo

Descarga este archivo de imagen y encuentra la bandera.

## Solución
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ wget https://artifacts.picoctf.net/c/101/drawing.flag.svg                             
--2024-04-04 22:57:27--  https://artifacts.picoctf.net/c/101/drawing.flag.svg
Resolviendo artifacts.picoctf.net (artifacts.picoctf.net)... 13.249.21.32, 13.249.21.66, 13.249.21.85, ...
Conectando con artifacts.picoctf.net (artifacts.picoctf.net)[13.249.21.32]:443... conectado.
Petición HTTP enviada, esperando respuesta... 200 OK
Longitud: 4149 (4.1K) [application/octet-stream]
Grabando a: «drawing.flag.svg»

drawing.flag.svg             100%[============================================>]   4.05K  --.-KB/s    en 0s      

2024-04-04 22:57:27 (89.0 MB/s) - «drawing.flag.svg» guardado [4149/4149]

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ ls                        
 cat.jpg                     'P1-E4->Search source.md'    'P2-E1->information.md'
 drawing.flag.svg            'P1-E5->Forbidden Paths.md'  'P2-E2->Wireshark doo dooo do doo....md'
'P1-E1->Includes.md'         'P1-E6->Power Cookie.md'     'P2-E3->Enhance!.md'
'P1-E2->Inspect HTML.md'     'P1-E7->Roboto Sans.md'       shark1.pcapng
'P1-E2->.md'                 'P1-E8->Secrets.md'
'P1-E3->Local Authority.md'  'P1-E9->SQL Direct.md'

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ strings drawing.flag.svg  
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   viewBox="0 0 210 297"
   version="1.1"
   id="svg8"
   inkscape:version="0.92.5 (2060ec1f9f, 2020-04-08)"
   sodipodi:docname="drawing.svg">
  <defs
     id="defs2" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.69833333"
     inkscape:cx="400"
     inkscape:cy="538.41159"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:window-width="1872"
     inkscape:window-height="1016"
     inkscape:window-x="48"
     inkscape:window-y="27"
     inkscape:window-maximized="1" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1">
    <ellipse
       id="path3713"
       cx="106.2122"
       cy="134.47203"
       rx="102.05357"
       ry="99.029755"
       style="stroke-width:0.26458332" />
    <circle
       style="fill:#ffffff;stroke-width:0.26458332"
       id="path3717"
       cx="107.59055"
       cy="132.30211"
       r="3.3341289" />
    <ellipse
       style="fill:#000000;stroke-width:0.26458332"
       id="path3719"
       cx="107.45217"
       cy="132.10078"
       rx="0.027842503"
       ry="0.031820003" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:0.00352781px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0.26458332;"
       x="107.43014"
       y="132.08501"
       id="text3723"><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08501"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3748">p </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.08942"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3754">i </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09383"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3756">c </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.09824"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3758">o </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10265"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3760">C </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.10706"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3762">T </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11147"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3764">F { 3 n h 4 n </tspan><tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11588"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
         id="tspan3752">c 3 d _ 2 4 3 7 4 6 7 5 }</tspan></text>
  </g>
</svg>

┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/picoCTF-2doParcial-RetosWeb]
└─$ 
```

Analizando el archivo, con el comando `strings`, no nos resulta difícil darnos cuenta, que al final encontraremos partes de la bandera segmentadas y espaciados entre carácter, solo necesitamos unirlos y listo.

`picoCTF { 3 n h 4 n c 3 d _ 2 4 3 7 4 6 7 5 }`
## Notas adicionales

- `strings` -> Extrae las cadenas de un archivo binario.
## Referencias

- https://infolinux.es/comando-strings-de-linux-obten-cadenas-de-texto-de-archivos-article-about-linux-command-strings-retrieve-text-strings-from-files/#:~:text=El%20comando%20%E2%80%9Cstrings%E2%80%9D%20es%20una,que%20contenga%20texto%20legible%20incrustado.