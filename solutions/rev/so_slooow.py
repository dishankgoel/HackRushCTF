flag = "HackRushCTF{D0nt_6rut3_f0rc3_1t}"

start_key = 0x1337

p = 10**9 + 7

d = [i for i in range(start_key + 1)]

for i in range(3, start_key + 1):
    d[i] = (d[i - 1] + d[i - 3])%p

key = d[start_key]

encoded = []

for i in range(len(flag)):
    encoded.append(ord(flag[i])^(key))
    if(i%2 == 0):
        key += 0x1337

print(encoded)

# Solution part

decoded = []
key = d[start_key]
print(key)
flag = [272258510, 272263388, 272263390, 272268191, 272268198, 272273246, 272273240, 272278026, 272278049, 272283085, 272283103, 272287915, 272287892, 272292919, 272292969, 272297802, 272297825, 272302659, 272302599, 272307673, 272307672, 272312528, 272312508, 272317564, 272317482, 272322339, 272322354, 272327355, 272327383, 272332174, 272332235, 272337035]

for i in range(len(flag)):
    decoded.append(chr(flag[i]^key))
    if(i%2 == 0):
        key += 0x1337

print("".join(decoded))
