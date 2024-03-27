## Solución: 
──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ wget https://artifacts.picoctf.net/c_titan/9/flag2of2-final.pdf
--2024-03-13 16:00:41--  https://artifacts.picoctf.net/c_titan/9/flag2of2-final.pdf
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.26, 3.161.55.61, 3.161.55.64, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.26|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3362 (3.3K) [application/octet-stream]
Saving to: ‘flag2of2-final.pdf’

flag2of2-final.pdf                        100%[====================================================================================>]   3.28K  --.-KB/s    in 0s      

2024-03-13 16:00:41 (16.5 MB/s) - ‘flag2of2-final.pdf’ saved [3362/3362]

                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ ls
flag2of2-final.pdf
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ open flag2of2-final.pdf 
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ hexeditor flag2of2-final.pdf 
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ hexeditor flag2of2-final.pdf
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ hexeditor flag2of2-final.pdf
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ mv flag2of2-final.pdf flag2of2-final.png 
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ ls
flag2of2-final.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ open flag2of2-final.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ open flag2of2-final.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ cp flag2of2-final.png 
cp: missing destination file operand after 'flag2of2-final.png'
Try 'cp --help' for more information.
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ cp flag2of2-final.png flagcopia.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ ls
flag2of2-final.png  flagcopia.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ mv flagcopia.png flagcopia.pdf          
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ open flagcopia.pdf     
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/SecretPolygon]
└─$ 
picoCTF{f1u3n7_1n_pn9_&_pdf_7f9bccd1}
## Contraseña obtenida: 
picoCTF{f1u3n7_1n_pn9_&_pdf_7f9bccd1}

## Notas
Es importante saber manipular los distintos archivos y formatos, ya que manipulando su extensión nos podemos apoyar de muchas maneras. 


