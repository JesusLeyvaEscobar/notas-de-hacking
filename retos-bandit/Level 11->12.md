
# Objetivo

La contraseña para el siguiente nivel se almacena en el archivo data.txt, donde todas las letras minúsculas (a-z) y mayúsculas (A-Z) se han rotado 13 posiciones.

## Datos de acceso al nivel
Host al que se va a conectar: **bandit.labs.overthewire.org**.
Puerto: **2220**.
Usuario: **bandit11**.
Contraseña: Encontrada en el nivel anterior: `6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM`.

## Solución
```
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf WIAOOSFzMjXXBC0KoSKBbJ8puQm5lIEi
bandit11@bandit:~$ cat data.txt | tr "a-zA-Z" "n-zamN-ZA-M"
ESP passworO Ts MGYMMMDXKwMMZA0ImMIZoH8NSMz5yGCv
bandit11@bandit:~$ cat data.txt | tr "a-zA-Z" "n-za-mN-ZA-M"
The password is JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
bandit11@bandit:~$ 

```

## Notas adicionales

- `tr` -> Realiza una transliteracion de caracteres.
- `a-zA-Z`-> Es la representacion de las letras del alfabeto en minusculas y mayusculas.
- `n-zamN-ZA-M` -> Ayuda a reemplazar cada letra por la 13va letra del alfabeto que se encuentre después de esa letra.
## Referencias

grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
[Rot13 on Wikipedia](https://en.wikipedia.org/wiki/Rot13)

