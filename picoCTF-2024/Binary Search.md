# Description
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_atlas/6/challenge.zip)

Additional details will be available after launching your challenge instance.

# Datos de acceso
ssh -p 51821 [ctf-player@atlas.picoctf.net](mailto:ctf-player@atlas.picoctf.net) 6dd28e9b
# Solución

```
tonyrguez-picoctf@webshell:~/home/ctf-player/drop-in$ ssh -p 51821 ctf-player@atlas.picoctf.net
The authenticity of host '[atlas.picoctf.net]:51821 ([18.217.83.136]:51821)' can't be established.
ED25519 key fingerprint is SHA256:M8hXanE8l/Yzfs8iuxNsuFL4vCzCKEIlM/3hpO13tfQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[atlas.picoctf.net]:51821' (ED25519) to the list of known hosts.
ctf-player@atlas.picoctf.net's password: 
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250  
Higher! Try again.
Enter your guess: 350
Higher! Try again.
Enter your guess: 400
Lower! Try again.
Enter your guess: 370
Higher! Try again.
Enter your guess: 380
Lower! Try again.
Enter your guess: 375
Lower! Try again.
Enter your guess: 373
Lower! Try again.
Enter your guess: 372
Lower! Try again.
Enter your guess: 371
Congratulations! You guessed the correct number: 371
Here's your flag: picoCTF{g00d_gu355_de9570b0}
Connection to atlas.picoctf.net closed.
tonyrguez-picoctf@webshell:~/home/ctf-player/drop-in$ 
```

# Notas
- Al empezar a divinar por la mitad de los datos a adivinar (1-1000), e ir yéndose a la mitad dependiendo de si es más alto o más bajo se puede adivinar el número en menos de 10 intentos

# Referencia