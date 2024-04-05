# Objetivo

¡Conéctese a este servidor PostgreSQL y encuentre la bandera!
`psql -h saturn.picoctf.net -p 60413 -U postgres pico`
Password is `postgres`
1. ¿Qué contiene una base de datos SQL?
## Solución

```
┌──(jesus㉿KaliJesus)-[~]
└─$ psql -h saturn.picoctf.net -p 60413 -U postgres pico
Contraseña para usuario postgres: 
psql (16.1 (Debian 16.1-1), servidor 15.2 (Debian 15.2-1.pgdg110+1))
Digite «help» para obtener ayuda.

pico=# \dt
        Listado de relaciones
 Esquema | Nombre | Tipo  |  Dueño   
---------+--------+-------+----------
 public  | flags  | tabla | postgres
(1 fila)

pico=# select * from public.flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 filas)

pico=# 

```
Realizamos una inspección al listado de tablas a las cuales tenemos acceso y realizamos una consulta con la sentencia `select` para que nos muestre los registros que contiene la relación `public`.
## Notas adicionales

- `\dt`-> Muestra las tablas en la BD
## Referencias

- https://platzi.com/discusiones/1566-bd/84219-el-codedtcode-para-listar-las-tablas-que-contiene-la-base-de-datos-actual-tambien-es-un-estandar-de-sql-o-es-de-google/