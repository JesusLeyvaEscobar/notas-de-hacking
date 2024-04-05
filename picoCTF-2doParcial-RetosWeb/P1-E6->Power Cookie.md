# Objetivo

¿Puedes conseguir la bandera?
Vaya a este sitio web y vea lo que puede descubrir.
1. ¿Sabes cómo modificar las cookies?
## Solución

Entramos a la pagina y observamos lo siguiente:
```
# Online Gradebook

Continue as guest (Este es un boton)
```

Y si damos clic sobre el botón `Continue as guest`, nos manda el siguiente mensaje:

`We apologize, but we have no guest services at the moment.`

ES momento de analizar las cookies en esta pagina: Vemos que en la actual pagina, tenemos una cookie llamada `isAdmin`, solo cambiamos el valos de `0` a `1`, guardamos la cookie y recargamos lapagina, obtendremos el siguiente resultado:

`picoCTF{gr4d3_A_c00k13_65fd1e1a}`
## Notas adicionales

## Referencias

