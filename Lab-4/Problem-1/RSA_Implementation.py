import random
from math import gcd

MXN = 1005
primeList = []
mark = {}


def sieve():

    primeList.append(2)
    i = 4

    while i < MXN:
        mark[i] = True
        i += 2

    i = 3
    while i < MXN:
        if i not in mark:
            primeList.append(i)
            j = i * i
            while j < MXN:
                mark[j] = True
                j += i
        i += 2

    # print(len(primeList))


def phi(x):

    cnt = 0
    for i in range(1, x):
        if gcd(x, i) == 1:
            cnt += 1

    return cnt


def bigMOD(x, y, mod):

    x %= mod
    res = 1

    while y:
        if (y % 2) == 1:
            res = (res * x) % mod
            y -= 1
        else:
            x = (x * x) % mod
            y //= 2

    return res


def RSA():

    p = 0
    q = 0
    while (p * q) < 100:

        i = random.randint(0, len(primeList)-1)
        p = primeList[i]

        i = random.randint(0, len(primeList)-1)
        q = primeList[i]

    print("p: " + str(p))
    print("q: " + str(q))

    n = p * q
    phi_n = (p-1) * (q-1)
    print("n: " + str(n))
    print("phi(n): " + str(phi_n))

    e = 0
    for i in primeList:
        if gcd(i, phi_n) == 1:
            e = i
            break
    print("Public key: " + str(e))

    d = bigMOD(e, (phi(phi_n)-1), phi_n)
    print("Private key: " + str(d))

    msge = int(input("Enter your message: "))
    encrypted_msge = bigMOD(msge, e, n)
    decrypted_msge = bigMOD(encrypted_msge, d, n)
    print("Encrypted Message: " + str(encrypted_msge))
    print("Decrypted Message: " + str(decrypted_msge))


def main():

    sieve()
    RSA()


if __name__ == main():
    main()


# a^ϕ(n) ≡ 1 (mod n) ​[​Euler's Theorem]
# e * d ≡ 1 (mod ϕ(n))
# a^ϕ(ϕ(n)) ≡ 1 (mod ϕ(n))
# e * e^ϕ(ϕ(n))−1 ≡ 1 (mod ϕ(n))
# So, d = e^ϕ(ϕ(n))−1
