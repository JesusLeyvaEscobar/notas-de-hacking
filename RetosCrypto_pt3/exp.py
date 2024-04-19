datos = open('message.txt').read().split()

print(datos)

flag = ''

for n in datos:
	c = int(n) % 37
	if c >= 0 and c <= 25:
		s = chr(c+65)
	elif c >= 26 and c <= 35:
		s = chr(c+22)
	else:
		s = '_'
	flag += s

print(f"picoCTF{{{flag}}}")
