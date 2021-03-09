from binascii import hexlify

big_number = 13269353506569762322866448443179444023604712744966341096534397703952746262066379915270
exponent = 0x10001

flag = b"---REDACTED---" # Who knows what was here?
flag = int(hexlify(flag), 16)

magic = pow(flag, exponent, big_number)
print("Something magical: {}".format(magic))

# Something magical: 1190180964733245137384972297461802113210633791027492695067903719077825144431176576299