## Objetivo 
How well can you perfom basic binary operations?Start searching for the flag here `nc titan.picoctf.net 62817`

## Solución
```bash
luispuentes-picoctf@webshell:~/drop-in$  nc titan.picoctf.net 62817

Welcome to the Binary Challenge!"
Your task is to perform the unique operations in the given order and find the final result in hexadecimal that yields the flag.

Binary Number 1: 11110110
Binary Number 2: 10000001


Question 1/6:
Operation 1: '&'
Perform the operation on Binary Number 1&2.
Enter the binary result: 10000000
Correct!

Question 2/6:
Operation 2: '>>'
Perform a right shift of Binary Number 2 by 1 bits .
Enter the binary result: 01000000
Correct!

Question 3/6:
Operation 3: '*'
Perform the operation on Binary Number 1&2.
Enter the binary result: 0111101111110110
Correct!

Question 4/6:
Operation 4: '+'
Perform the operation on Binary Number 1&2.
Enter the binary result: 000101110111
Correct!

Question 5/6:
Operation 5: '<<'
Perform a left shift of Binary Number 1 by 1 bits.
Enter the binary result: 11101100      
Incorrect. Try again
Enter the binary result: 1110110 
Incorrect. Try again
Enter the binary result: 111101100   
Correct!

Question 6/6:
Operation 6: '|'
Perform the operation on Binary Number 1&2.
Enter the binary result: 11110111
Correct!

Enter the results of the last operation in hexadecimal: f7

Correct answer!
The flag is: picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_aeaf4b09}
```


## Notas
se obtuvo la bandera solamente realizando las operaciones solicitadas.
