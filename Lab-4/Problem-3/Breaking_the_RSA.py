from sympy import *

d = 0
e = 0
n = 0
ary = []


def sqrt(x):

    lo = 0
    hi = x
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if (mid * mid) <= x:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return res


def equation_solver(a, b, c):

    # equation solving using quadratic equation solving formula
    # t = (b * b) - (4 * a * c)
    # t = sqrt(t)
    # p = (b + t) // (2 * a)
    # q = (b - t) // (2 * a)

    # equation solving using built-in function
    x = Symbol('x', integer=True)
    roots = solve((x ** 2) - (x * b) + c, x)
    if len(roots) == 2:
        p = roots[0]
        q = roots[1]
    else:
        return False

    if (p * q) == n:
        print("p: " + str(p))
        print("q: " + str(q))
        return True

    return False


def check(tk, td):

    if not tk:
        return False
    if (tk >= td) or (td == 1):
        return False
    if not (td % 2):
        return False

    phi = (e * td) - 1
    # print("e:", e, "d:", td, "phi(n):", phi)

    if not (phi % tk):
        phi //= tk
        b = n - phi + 1
        if equation_solver(1, b, n):
            global d
            d = td
            print("Private key: " + str(d))
            return True
        else:
            return False
    else:
        return False


def fraction_expansion(x, y):

    # print(x, y)

    if not y:
        return

    top = 1
    bottom = (x // y)
    # print(bottom)

    for i in ary:
        top += (i * bottom)
        top, bottom = bottom, top

    top, bottom = bottom, top
    # print(top, bottom)

    if not check(top, bottom):
        ary.insert(0, (x // y))
        fraction_expansion(y, (x % y))


def bigMOD(x, y, mod):

    x %= mod
    res = 1

    while y:
        if not (y % 2):
            x = (x * x) % mod
            y //= 2
        else:
            res = (res * x) % mod
            y -= 1

    return res


def decryption():

    fp = open("4.3_ciphertext.hex", "r")
    ciphertext_str = fp.read()
    fp.close()

    ciphertext = int(ciphertext_str, 16)
    print("Encrypted Message:", ciphertext)

    decrypted_msge = bigMOD(ciphertext, d, n)
    print("Decrypted Message:", decrypted_msge)


def main():

    fp = open("4.4_public_key.hex", "r")
    e_str = fp.read()
    fp.close()

    global e
    e = int(e_str, 16)
    print("Public Key: " + str(e))

    fp = open("4.5_modulo.hex", "r")
    n_str = fp.read()
    fp.close()

    global n
    n = int(n_str, 16)
    print("Public Modulo: " + str(n))

    fraction_expansion(e, n)
    decryption()


if __name__ == main():
    main()
