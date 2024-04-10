# Objetivo

Hicimos muchas sustituciones para cifrar esto. ¿Puedes descifrarlo? Conéctese con `nc jupiter.challenges.picoctf.org 13758`.
1. La bandera no tiene el formato habitual
## Solución

SI hacemos la conexión que nos indica, obtenemos el siguiente resultado:
```
┌──(jesus㉿KaliJesus)-[~/Desktop/github/notas-de-hacking/RetosCrypo_pt1]
└─$ nc jupiter.challenges.picoctf.org 13758
-------------------------------------------------------------------------------
bturnjwg yqnq lg etvn xojr - xnqkvqube_lg_b_tdqn_ojmiaj_audwxnwjev
-------------------------------------------------------------------------------
hq hqnq utw mvby mtnq wyju j kvjnwqn tx ju ytvn tvw tx tvn gylz wloo hq gjh yqn gluc, jua wyqu l vuaqngwtta xtn wyq xlngw wlmq hyjw hjg mqjuw ie j gylz xtvuaqnlur lu wyq gqj.  l mvgw jbcuthoqarq l yja yjnaoe qeqg wt ottc vz hyqu wyq gqjmqu wtoa mq gyq hjg gluclur; xtn xntm wyq mtmquw wyjw wyqe njwyqn zvw mq luwt wyq itjw wyju wyjw l mlryw iq gjla wt rt lu, me yqjnw hjg, jg lw hqnq, aqja hlwylu mq, zjnwoe hlwy xnlryw, zjnwoe hlwy ytnntn tx mlua, jua wyq wytvrywg tx hyjw hjg eqw iqxtnq mq.
```
Este tipo de cifrado, pudiera llegar a ser un cifrado por sustitución, así que nos ayudaremos de una herramienta en linea para tratar de descifrarlo.
La herramienta que utilizamos, nos dice que la llave para saber que letras se sustituyen por cual, es:
```
abcdefghijklmnopqrstuvwxyz     This clear text ...  
dckvyjswbaqimrlzegxonutfhp**     ... maps to this cipher text
```
Por lo que el texto descifrado es:
```
-------------------------------------------------------------------------------
	congrats here is your flag - frequency_is_c_over_lambda_dnvtfrtayu
-------------------------------------------------------------------------------
we were not much more than a quarter of an hour out of our ship till we saw her sink, and then i understood for the first time what was meant by a ship foundering in the sea.  i must acknowledge i had hardly eyes to look up when the seamen told me she was sinking; for from the moment that they rather put me into the boat than that i might be said to go in, my heart was, as it were, dead within me, partly with fright, partly with horror of mind, and the thoughts of what was yet before me.
```
## Notas adicionales

- `Cifrado por sustitucion`->En criptografía, el cifrado por sustitución es un método de cifrado por el que unidades de texto plano son sustituidas con texto cifrado siguiendo un sistema regular; las "unidades" pueden ser una sola letra, pares de letras, tríos de letras, mezclas de lo anterior, entre otros.
## Referencias

- https://www.guballa.de/substitution-solver