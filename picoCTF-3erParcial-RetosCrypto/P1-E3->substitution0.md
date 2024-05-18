# Objetivo

Ha llegado un mensaje pero parece estar todo codificado. Por suerte parece tener la clave al principio. ¿Puedes descifrar este cifrado de sustitución?
Descarga el mensaje aquí.
1. Prueba un ataque de frecuencia. Una herramienta en línea podría ayudar.
## Solución

Despues de analizar el texto obtenido por el enlace que nos proporciona el reto, vemos lo siguiente:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/3erParcial-RetosCrypto]
└─$ cat message.txt   
ZGSOCXPQUYHMILERVTBWNAFJDK 

Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.

Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}   
```
Resolvimos algunos retos similares durante el semetre, por lo que sabemos  que se trata de un algoritmo de cifrado de sustitucion que contiene una llave la cual nos ayudara a descifrar lo que dice el texto.

Nos ayudaremos de una herramienta en linea para poder descifrar fácilmente lo que dice el texto.
EL resultado obtenido fue el siguiente:
```
Hereupon Legrand arose, with a grave and stately air, and brought me the beetle  
from a glass case in which it was enclosed. It was a beautiful scarabaeus, and, at  
that time, unknown to naturalists--of course a great prize in a scientific point  
of view. There were two round black spots near one extremity of the back, and a  
long one near the other. The scales were exceedingly hard and glossy, with all the  
appearance of burnished gold. The weight of the insect was very remarkable, and,  
taking all things into consideration, I could hardly blame Jupiter for his opinion  
respecting it.  
  
The flag is: picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}
```
## Notas adicionales

- `Cifrado de sustitucion`->En criptografía, un cifrado de sustitución es un método de cifrado en el que unidades de texto sin formato se reemplazan con el texto cifrado, de una manera definida, con la ayuda de una clave;
## Referencias

- https://www.dcode.fr/monoalphabetic-substitution
- https://es.wikipedia.org/wiki/Cifrado_por_sustituci%C3%B3n