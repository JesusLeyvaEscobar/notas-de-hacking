## Objetivo 
Can you get the real meaning from this file.Download the file [here](https://artifacts.picoctf.net/c_titan/3/enc_flag).

## Solución
```bash
luispuentes-picoctf@webshell:~$ ls
Parcial1  README.txt  enc_flag  multipage-html-img1.jpg  runme.py
luispuentes-picoctf@webshell:~$ cat enc_flag | base64   
WWlka00wSnhaR3R3UWxSWWRIRmhSM2cyWVVoc1ptRjZUbkZsVkd3eldWUk9jbGd5YTNsTlJGSnZZ
VEp2TW1aUlBUMG5DZz09Cg==
luispuentes-picoctf@webshell:~$ cat enc_flag | base64 -d
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=='
luispuentes-picoctf@webshell:~$ echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ==" | base64 -d
wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}luispuentes-picoctf@webshell:~$

    CYBERCHEF
Amount =  1: xqkwKBN{kimaiz_l3kz9xb3l_j204ilk6}
Amount =  2: yrlxLCO{ljnbja_m3la9yc3m_k204jml6}
Amount =  3: zsmyMDP{mkockb_n3mb9zd3n_l204knm6}
Amount =  4: atnzNEQ{nlpdlc_o3nc9ae3o_m204lon6}
Amount =  5: buoaOFR{omqemd_p3od9bf3p_n204mpo6}
Amount =  6: cvpbPGS{pnrfne_q3pe9cg3q_o204nqp6}
Amount =  7: dwqcQHT{qosgof_r3qf9dh3r_p204orq6}
Amount =  8: exrdRIU{rpthpg_s3rg9ei3s_q204psr6}
Amount =  9: fyseSJV{squiqh_t3sh9fj3t_r204qts6}
Amount = 10: gztfTKW{trvjri_u3ti9gk3u_s204rut6}
Amount = 11: haugULX{uswksj_v3uj9hl3v_t204svu6}
Amount = 12: ibvhVMY{vtxltk_w3vk9im3w_u204twv6}
Amount = 13: jcwiWNZ{wuymul_x3wl9jn3x_v204uxw6}
Amount = 14: kdxjXOA{xvznvm_y3xm9ko3y_w204vyx6}
Amount = 15: leykYPB{ywaown_z3yn9lp3z_x204wzy6}
Amount = 16: mfzlZQC{zxbpxo_a3zo9mq3a_y204xaz6}
Amount = 17: ngamARD{aycqyp_b3ap9nr3b_z204yba6}
Amount = 18: ohbnBSE{bzdrzq_c3bq9os3c_a204zcb6}
Amount = 19: picoCTF{caesar_d3cr9pt3d_b204adc6}
```


## Notas
Se desecripto de base 64 la cadena obtenida 2 veces y dio un formato parecido a la bandera por lo que en cyberchef se aplico un rot13 de fuerza bruta y se obtuvo el password en la linea 19.

## Referencias
https://gchq.github.io/CyberChef/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ