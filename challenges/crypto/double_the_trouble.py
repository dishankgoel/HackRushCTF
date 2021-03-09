import hashlib
import base64
from Crypto.Cipher import AES
import random
import string

def random_key():
    possible = list(string.printable)
    n = len(possible)
    key = b"".join([possible[random.randint(0, n - 1)].encode() for i in range(32)])
    key = b'0'*29 + key[-3:]
    print(key)
    return key

key1 = random_key()
key2 = random_key()

plaintext = b"testing 1..2..3!"


iv = hashlib.md5(b"Goodluck!").digest()

aes1 = AES.new(key1, AES.MODE_CBC, iv = iv)
single_pass = aes1.encrypt(plaintext)

aes2 = AES.new(key2, AES.MODE_CBC, iv = iv)
encrypted = aes2.encrypt(single_pass)

print(base64.b64encode(encrypted))

encrypted = b'v8MshgtU1CfDNDuajMHzkQ==' # Result of testing

# encrypted_flag = b"aUyXnj4SxFmYht39qIppFKIVDjQ/tTBbPwpSLo2IoHo="





