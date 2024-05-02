d = open("rev_this").read()
flag = ""
for j in range(8, 23):
        if j &  1 == 0:
                flag += chr(ord(d[j]) - 5)
        else:
                flag += chr(ord(d[j]) + 2)
print(flag)
