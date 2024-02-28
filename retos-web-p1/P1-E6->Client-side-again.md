# Objetivo

¿Podrás entrar en este portal súper seguro? https://jupiter.challenges.picoctf.org/problem/6353/ (enlace) o http://jupiter.challenges.picoctf.org:6353
1. ¿Qué es la ofuscación?

## Solución

```
Inspeccionando el codigo fuente, encontraremos una linea que define la variable, entonces nos ayudamos de un sitio web para des-ofurcar el codigo y hacerlo mas legible. Nos da el codigo, en el cualn encontraremos la siguiente variable que contiene la contrasena en partes:

var _0x5a46 = ["0a029}", "_again_5", "this", "Password Verified", "Incorrect password", "getElementById", "value", "substring", "picoCTF{", "not_this"];

Solo la "armamos" y listo.
picoCTF{not_this_again_50a029}

```
## Notas adicionales


## Referencias

http://jsnice.org/