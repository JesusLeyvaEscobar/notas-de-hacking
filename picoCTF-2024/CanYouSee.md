## Objetivo 
How about some hide and seek?Download this file [here](https://artifacts.picoctf.net/c_titan/6/unknown.zip).

## Solución
```bash
luispuentes-picoctf@webshell:~$ ls
Parcial1  README.txt  enc_flag  level3.flag.txt.enc  level3.hash.bin  level3.py  multipage-html-img1.jpg  runme.py  ukn_reality.jpg  unknown.zip
luispuentes-picoctf@webshell:~$ exiftool ukn_reality.jpg 
ExifTool Version Number         : 12.40
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.2 MiB
File Modification Date/Time     : 2024:02:15 22:40:21+00:00
File Access Date/Time           : 2024:03:12 23:58:41+00:00
File Inode Change Date/Time     : 2024:03:12 23:57:55+00:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
luispuentes-picoctf@webshell:~$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==" | base64
Y0dsamIwTlVSbnROUlRjMFJEUTNRVjlJU1VSRU0wNWZZVFprWmpoa1lqaDlDZz09Cg==
luispuentes-picoctf@webshell:~$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==" | base64 -d
picoCTF{ME74D47A_HIDD3N_a6df8db8}
luispuentes-picoctf@webshell:~$
```


## Notas
exiftool nos muestra información de la imagen donde pueden venir datos interesantes.
## Referencias
Manual de usuario del comando exiftool.