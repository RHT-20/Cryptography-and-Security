fp = open("dict.txt", 'w')


def init():

    dict = {}
    dict['l'] = 'o'
    dict['e'] = 'g'
    dict['u'] = 'r'
    dict['k'] = 'k'
    dict['h'] = 'h'
    dict['z'] = 't'
    dict['o'] = 'l'
    dict['n'] = 'n'
    dict['s'] = 's'
    dict['b'] = 'b'
    dict['t'] = 'z'

    # rbszizrzig

    # ogrk hg tl’n srbszizrzig
    # leuk he zo’n subst

    list = ['o', 'g', 'r', 'k', 'h', 't', 'l', 'n', 's', 'b', 'z']
    return dict, list


def bruteforce(pos, text, list):

    if pos >= len(text)-1:
        fp.write(text)
        fp.write("\n")
        # print(text)
        return

    for i in range(97, 123):
        x = chr(i)
        if x not in list:
            text = text[:pos] + x + text[pos+1:]
            list.append(x)
            # print(text)
            # return
            bruteforce(pos+1, text, list)
            list.remove(x)


def main():

    dict, list = init()
    # bruteforce(0, "substitutie", list)

    text = "substitutie"
    for i in range(97, 123):
        x = chr(i)
        if x not in list:
            text = text[:5] + x + text[6:9] + x + text[10:]
            fp.write(text)
            fp.write("\n")


if __name__ == main():
    main()
