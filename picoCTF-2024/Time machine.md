## Solución
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine]
└─$ wget https://artifacts.picoctf.net/c_titan/68/challenge.zip
--2024-03-13 15:39:55--  https://artifacts.picoctf.net/c_titan/68/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.55.26, 3.161.55.64, 3.161.55.100, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.55.26|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17738 (17K) [application/octet-stream]
Saving to: ‘challenge.zip’

challenge.zip                             100%[====================================================================================>]  17.32K  --.-KB/s    in 0.002s  

2024-03-13 15:39:55 (6.84 MB/s) - ‘challenge.zip’ saved [17738/17738]

                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine]
└─$ ls
challenge.zip
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine]
└─$ unzip challenge.zip 
Archive:  challenge.zip
   creating: drop-in/
  inflating: drop-in/message.txt     
   creating: drop-in/.git/
   creating: drop-in/.git/branches/
  inflating: drop-in/.git/description  
   creating: drop-in/.git/hooks/
  inflating: drop-in/.git/hooks/applypatch-msg.sample  
  inflating: drop-in/.git/hooks/commit-msg.sample  
  inflating: drop-in/.git/hooks/fsmonitor-watchman.sample  
  inflating: drop-in/.git/hooks/post-update.sample  
  inflating: drop-in/.git/hooks/pre-applypatch.sample  
  inflating: drop-in/.git/hooks/pre-commit.sample  
  inflating: drop-in/.git/hooks/pre-merge-commit.sample  
  inflating: drop-in/.git/hooks/pre-push.sample  
  inflating: drop-in/.git/hooks/pre-rebase.sample  
  inflating: drop-in/.git/hooks/pre-receive.sample  
  inflating: drop-in/.git/hooks/prepare-commit-msg.sample  
  inflating: drop-in/.git/hooks/update.sample  
   creating: drop-in/.git/info/
  inflating: drop-in/.git/info/exclude  
   creating: drop-in/.git/refs/
   creating: drop-in/.git/refs/heads/
 extracting: drop-in/.git/refs/heads/master  
   creating: drop-in/.git/refs/tags/
 extracting: drop-in/.git/HEAD       
  inflating: drop-in/.git/config     
   creating: drop-in/.git/objects/
   creating: drop-in/.git/objects/pack/
   creating: drop-in/.git/objects/info/
   creating: drop-in/.git/objects/43/
 extracting: drop-in/.git/objects/43/246218ab4fc7b30e9a9dff073e012316851469  
   creating: drop-in/.git/objects/25/
 extracting: drop-in/.git/objects/25/16effb8d70e33bdd0023629b164a77225e1ec2  
   creating: drop-in/.git/objects/70/
 extracting: drop-in/.git/objects/70/5ff639b7846418603a3272ab54536e01e3dc43  
  inflating: drop-in/.git/index      
 extracting: drop-in/.git/COMMIT_EDITMSG  
   creating: drop-in/.git/logs/
  inflating: drop-in/.git/logs/HEAD  
   creating: drop-in/.git/logs/refs/
   creating: drop-in/.git/logs/refs/heads/
  inflating: drop-in/.git/logs/refs/heads/master  
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine]
└─$ ls
challenge.zip  drop-in
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine]
└─$ file drop-in                               
drop-in: directory
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine]
└─$ cd drop-in    
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine/drop-in]
└─$ ls
message.txt
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine/drop-in]
└─$ file message.txt 
message.txt: ASCII text, with no line terminators
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine/drop-in]
└─$ nano message.txt 
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/Timemachine/drop-in]
└─$ git log                                    
commit 705ff639b7846418603a3272ab54536e01e3dc43 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:36 2024 +0000

    picoCTF{t1m3m@ch1n3_b476ca06}

## Contraseña obtenida: 
picoCTF{t1m3m@ch1n3_b476ca06}
## Notas: 
Es importante saber el historial de commits de un archivo, en este nivel por ejemplo para poder obtener nuestro flag, fue importante saber el historial de commits a traves del comando Git Log.
