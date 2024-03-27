──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise]
└─$ wget https://artifacts.picoctf.net/c_atlas/3/challenge.zip
--2024-03-13 16:18:48--  https://artifacts.picoctf.net/c_atlas/3/challenge.zip
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.161.225.62, 3.161.225.11, 3.161.225.60, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.161.225.62|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 741 [application/octet-stream]
Saving to: ‘challenge.zip’

challenge.zip                             100%[====================================================================================>]     741  --.-KB/s    in 0s      

2024-03-13 16:18:49 (17.3 MB/s) - ‘challenge.zip’ saved [741/741]

                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise]
└─$ ls
challenge.zip
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise]
└─$ unzip challenge.zip
Archive:  challenge.zip
   creating: home/ctf-player/drop-in/
 extracting: home/ctf-player/drop-in/flag.png  
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise]
└─$ ls
challenge.zip  home
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise]
└─$ cd home        
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise/home]
└─$ ls     
ctf-player
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise/home]
└─$ file ctf-player
ctf-player: directory
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Desktop/Concurso picoCTF/ScanSurprise/home]
└─$ cd ctf-player
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/Concurso picoCTF/ScanSurprise/home/ctf-player]
└─$ ls           
drop-in
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/Concurso picoCTF/ScanSurprise/home/ctf-player]
└─$ cd drop-in   
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ ls
flag.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ open flag.png     
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ cp flag.png                        
cp: missing destination file operand after 'flag.png'
Try 'cp --help' for more information.
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ cp flag.png flagc 
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ ls               
flagc  flag.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ mv flagc flagc.txt            
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ ls
flagc.txt  flag.png
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ cat flagc.txt    
�PNG
▒
IHDRcc��,�PLTE�����tRNS��ȵ��    pHYs

�s�m ���nn��w��                     ��~��IDAT8��Ի�� �y�
               ��tD���
                      @�
                        ��
�
�Ju�p��]���I���K�*n���T�\�▒�t�"NNI�`���(m��7ʢ*�p��%S�)����s�dVI����^��D▒lP����6<{��m���q$�e��+YQ�}з�'�C�Pž�m��G��~&�R��FO�Yi��_���
                                                                                                                                  r������tIEND�B`�                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ sudo apt install zbar-tools

[sudo] password for kali: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package zbar-tools
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ sudo apt update            
Get:1 http://kali.download/kali kali-rolling InRelease [41.5 kB]
Get:2 http://kali.download/kali kali-rolling/main amd64 Packages [19.8 MB]
Get:3 http://kali.download/kali kali-rolling/main amd64 Contents (deb) [47.2 MB]                                                                                      
Get:4 http://kali.download/kali kali-rolling/contrib amd64 Packages [119 kB]                                                                                          
Get:5 http://kali.download/kali kali-rolling/contrib amd64 Contents (deb) [258 kB]                                                                                    
Get:6 http://kali.download/kali kali-rolling/non-free amd64 Packages [194 kB]                                                                                         
Get:7 http://kali.download/kali kali-rolling/non-free amd64 Contents (deb) [893 kB]                                                                                   
Get:8 http://kali.download/kali kali-rolling/non-free-firmware amd64 Packages [33.0 kB]                                                                               
Get:9 http://kali.download/kali kali-rolling/non-free-firmware amd64 Contents (deb) [16.8 kB]                                                                         
Fetched 68.6 MB in 44s (1,574 kB/s)                                                                                                                                   
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
418 packages can be upgraded. Run 'apt list --upgradable' to see them.
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ sudo apt install zbar-tools

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  zbarcam-gtk zbarcam-qt
The following NEW packages will be installed:
  zbar-tools
0 upgraded, 1 newly installed, 0 to remove and 418 not upgraded.
Need to get 37.7 kB of archives.
After this operation, 102 kB of additional disk space will be used.
Get:1 http://http.kali.org/kali kali-rolling/main amd64 zbar-tools amd64 0.23.93-1+b1 [37.7 kB]
Fetched 37.7 kB in 1s (37.6 kB/s)                  
Selecting previously unselected package zbar-tools.
(Reading database ... 404048 files and directories currently installed.)
Preparing to unpack .../zbar-tools_0.23.93-1+b1_amd64.deb ...
Unpacking zbar-tools (0.23.93-1+b1) ...
Setting up zbar-tools (0.23.93-1+b1) ...
Processing triggers for dbus (1.14.10-4) ...
Processing triggers for kali-menu (2023.4.7) ...
Processing triggers for man-db (2.12.0-3) ...
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/ScanSurprise/home/ctf-player/drop-in]
└─$ zbarimg flag.png 
QR-Code:picoCTF{p33k_@_b00_a81f0a35}
scanned 1 barcode symbols from 1 images in 0.1 seconds

