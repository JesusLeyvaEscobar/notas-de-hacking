## Solución
resm-picoctf@webshell:~$ ssh ctf-player@titan.picoctf.net -p 65080 
The authenticity of host '[titan.picoctf.net]:65080 ([3.139.174.234]:65080)' can't be established.
ED25519 key fingerprint is SHA256:4S9EbTSSRZm32I+cdM5TyzthpQryv5kudRP9PIKT7XQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[titan.picoctf.net]:65080' (ED25519) to the list of known hosts.
ctf-player@titan.picoctf.net's password:  6dd28e9b
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_5d09a462}
Connection to titan.picoctf.net closed.
resm-picoctf@webshell:~$ 

## Contraseña obtenida
picoCTF{s3cur3_c0nn3ct10n_5d09a462}

## Notas 
Es importante el uso del SSH ya que es el comando el cual nos permite realizar disntintas conexiones remotas.