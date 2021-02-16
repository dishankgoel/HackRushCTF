flag = "HackRushCTF{Gh1dr4_1s_Tru!y_4w3s0m3}"
flag = flag[::-1]

encrypted = ""
l = []

for i in range(len(flag)):
    encrypted += chr(int(bin(ord(flag[i]))[2:].zfill(8)[::-1], 2))
    l.append(int(bin(ord(flag[i]))[2:].zfill(8)[::-1], 2))

print(bytes(encrypted, "latin-1"))
print(l)