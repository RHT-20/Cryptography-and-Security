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
    t = (b * b) - (4 * a * c)
    t = sqrt(t)
    p = (b + t) // (2 * a)
    q = (b - t) // (2 * a)

    # equation solving using built-in function
    # x = Symbol('x', integer=True)
    # roots = solve((x ** 2) - (x * b) + c, x)
    # if len(roots) == 2:
    #     p = roots[0]
    #     q = roots[1]
    # else:
    #     return False

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


def BS(x):

    lo = 0
    hi = x
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2

        mul = 1
        for i in range(e):
            mul *= mid

        if mul == x:
            res = mid
            break

        if mul < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return res


def problem_1():

    # global n
    # n = 374159235470172130988938196520880526947952521620932362050308663243595788308583992120881359365258949723819911758198013202644666489247987314025169670926273213367237020188587742716017314320191350666762541039238241984934473188656610615918474673963331992408750047451253205158436452814354564283003696666945950908549197175404580533132142111356931324330631843602412540295482841975783884766801266552337129105407869020730226041538750535628619717708838029286366761470986056335230171148734027536820544543251801093230809186222940806718221638845816521738601843083746103374974120575519418797642878012234163709518203946599836959811
    # print("Public Modulo: " + str(n))

    global e
    e = 3
    print("Public Key: " + str(e))

    # fraction_expansion(e, n)

    cipher_text = 2205316413931134031046440767620541984801091216351222789180967130585669043554866325905770867150377611820746759815247778516899403229047066700396787852388511389893043279713280998235746440322483431305358901578692935378439077796777060321410661
    print("Encrypted Message:", cipher_text)

    plain_text = BS(cipher_text)
    print("Decrypted Message:", plain_text)


def check_private_key():

    plain_text = 12345
    cipher_text = bigMOD(plain_text, e, n)
    print(cipher_text)
    plain_text = bigMOD(cipher_text, d, n)
    print(plain_text)


def problem_2():

    global n
    n = "0x02aeb637f6152afd4fb3a2dd165aec9d5b45e70d2b82e78a353f7a1751859d196f56cb6d11700195f1069a73d9e5710950b814229ab4c5549383c2c87e0cd97f904748a1302400dc76b42591da17dabaf946aaaf1640f1327af16be45b8830603947a9c3309ca4d6cc9f1a2bcfdacf285fbc2f730e515ae1d93591ccd98f5c4674ec4a5859264700f700a4f4dcf7c3c35bbc579f6ebf80da33c6c11f68655092bbe670d5225b8e571d596fe426db59a6a05aaf77b3917448b2cfbcb3bd647b46772b13133fc68ffabcb3752372b949a3704b8596df4a44f085393ee2bf80f8f393719ed94ab348852f6a5e0c493efa32da5bf601063a033beaf73ba47d8205db"
    n = int(n, 16)
    print("Public Modulo: " + str(n))

    global e
    e = "0x0285f8d4fe29ce11605edf221868937c1b70ae376e34d67f9bb78c29a2d79ca46a60ea02a70fdb40e805b5d854255968b2b1f043963dcd61714ce4fc5c70ecc4d756ad1685d661db39d15a801d1c382ed97a048f0f85d909c811691d3ffe262eb70ccd1fa7dba1aa79139f21c14b3dfe95340491cff3a5a6ae9604329578db9f5bcc192e16aa62f687a8038e60c01518f8ccaa0befe569dadae8e49310a7a3c3bddcf637fc82e5340bef4105b533b6a531895650b2efa337d94c7a76447767b5129a04bcf3cd95bb60f6bfd1a12658530124ad8c6fd71652b8e0eb482fcc475043b410dfc4fe5fbc6bda08ca61244284a4ab5b311bc669df0c753526a79c1a57"
    e = int(e, 16)
    print("Public Key: " + str(e))

    fraction_expansion(e, n)
    check_private_key()


def main():

    print("Problem-1:")
    problem_1()

    print("Problem-2:")
    problem_2()


if __name__ == main():
    main()
