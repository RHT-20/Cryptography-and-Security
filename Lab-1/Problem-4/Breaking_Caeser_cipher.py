def init_probability_table():

    prob={}
    prob['A'] = prob['a'] = 8.167
    prob['B'] = prob['b'] = 1.492
    prob['C'] = prob['c'] = 2.782
    prob['D'] = prob['d'] = 4.253
    prob['E'] = prob['e'] = 12.702
    prob['F'] = prob['f'] = 2.228
    prob['G'] = prob['g'] = 2.015
    prob['H'] = prob['h'] = 6.094
    prob['I'] = prob['i'] = 6.996
    prob['J'] = prob['j'] = 0.153
    prob['K'] = prob['k'] = 0.772
    prob['L'] = prob['l'] = 4.025
    prob['M'] = prob['m'] = 2.406
    prob['N'] = prob['n'] = 6.749
    prob['O'] = prob['o'] = 7.507
    prob['P'] = prob['p'] = 1.929
    prob['Q'] = prob['q'] = 0.095
    prob['R'] = prob['r'] = 5.987
    prob['S'] = prob['s'] = 6.327
    prob['T'] = prob['t'] = 9.056
    prob['U'] = prob['u'] = 2.758
    prob['V'] = prob['v'] = 0.978
    prob['W'] = prob['w'] = 2.360
    prob['X'] = prob['x'] = 0.150
    prob['Y'] = prob['y'] = 1.974
    prob['Z'] = prob['z'] = 0.074

    return prob


def calc_value(freq, prob, l):

    sum = 0

    for i in range(65, 91):
        C = freq[chr(i)]
        E = l * prob[chr(i)]
        dif = C - E
        sum = sum + ((dif * dif)/E)

    # print(sum)
    return sum


def chi_Square(text):

    prob = init_probability_table()

    freq = {}
    for i in range(65, 91):
        freq[chr(i)] = 0

    for ch in text:
        if 'A' <= ch <= 'Z':
            freq[ch] = freq[ch] + 1

    # for i in range(65, 91):
    #    print(freq[chr(i)])

    return calc_value(freq, prob, len(text))


def solve():

    fp = open("ciphertext.txt", "r")
    cipher_text = fp.read()
    fp.close()
    print("cipher text: " + cipher_text)

    shift = 0
    min_val = 99999999999999999999
    opt_text = cipher_text

    l = len(cipher_text)
    for i in range(0, 26):

        # forward move
        tmp_str = cipher_text.upper()
        # print(tmp_str)
        for j in range(0, l):

            x = tmp_str[j:j + 1]
            # print(x)

            x = ord(x)
            if x < 65 or x > 90:
                continue

            x += i
            if x > 90:
                x -= 26
            x = chr(x)
            # print(x)

            tmp_str = tmp_str[0:j] + x + tmp_str[j + 1:]

        # print(tmp_str)
        val = chi_Square(tmp_str)
        # print(val)
        if min_val > val:
            shift = i
            min_val = val
            opt_text = tmp_str

        # backward move
        tmp_str = cipher_text.upper()
        for j in range(0, l):

            x = tmp_str[j:j+1]
            # print(x)

            x = ord(x)
            if x < 65 or x > 90:
                continue

            x -= i
            if x < 65:
                x += 26
            x = chr(x)
            # print(x)

            tmp_str = tmp_str[0:j] + x + tmp_str[j+1:]

        # print(tmp_str)
        val = chi_Square(tmp_str)
        # print(val)
        if min_val > val:
            shift = -i
            min_val = val
            opt_text = tmp_str

    # print(shift)
    # print(min_val)
    print("original text: " + opt_text)


def main():
    solve()


if __name__ == main():
    main()
