# Objetivo

¿Puedes encontrar los robots? https://jupiter.challenges.picoctf.org/problem/60915/ (enlace) o http://jupiter.challenges.picoctf.org:60915
## Solución

Ingresamos la pagina:
https://jupiter.challenges.picoctf.org/problem/60915/robots.txt
Encontramos:
`User-agent: *
`Disallow: /8028f.html`
Luego sustituimos:
https://jupiter.challenges.picoctf.org/problem/60915//8028f.html
Nos arroja lo siguiente:
`Guess you found the robots  
`picoCTF{ca1cu1at1ng_Mach1n3s_8028f}`
## Notas adicionales

La clave estaba en encontrar los robots de la pagina para obtener la sección que faltaba en la liga para encontrar la contraseña.
## Referencias

