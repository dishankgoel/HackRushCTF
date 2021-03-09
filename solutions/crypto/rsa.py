from binascii import unhexlify

e = 0x10001

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x - (b//a)*y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if(g != 1):
        return -1
    return x%m

def solve_rsa(n, factors, c):

    ds = []
    for i in range(len(factors)):
        ds.append(modinv(e, factors[i] - 1))

    m = factors[0]
    ts = []
    for i in range(1, len(factors)):
        ts.append(modinv(m, factors[i]))
        m = m*factors[i]
    xs = []
    for i in range(len(factors)):
        xs.append(pow((c%factors[i]), ds[i], factors[i]))

    x = xs[0]
    m = factors[0]

    for i in range(1, len(factors)):
        x += m*((xs[i] - x % factors[i]) * (ts[i - 1] % factors[i]))
        m = m*factors[i]
    
    print("[*] flag: {}".format(unhexlify(hex(x%m)[2:])))


n = 25992347861099219061069221843214518860756327486173319027118759091795941826930677
c = 23026963612553138453994241341858545669161954498018923158210487520942937328899463
factors = [3757160792909754673945392226295475594863, 6918082374901313855125397665325977135579]

solve_rsa(n, factors, c)

n = 13269353506569762322866448443179444023604712744966341096534397703952746262066379915270
c = 1190180964733245137384972297461802113210633791027492695067903719077825144431176576299
factors = [2, 3, 5, 7, 11, 13, 17, 3757160792909754673945392226295475594863, 6918082374901313855125397665325977135579]

solve_rsa(n, factors, c)