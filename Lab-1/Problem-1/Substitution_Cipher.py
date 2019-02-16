def main():

    fp = open("sub_key.txt", "r")
    key = fp.read()
    fp.close()
    print("key: " + key)

    fp = open("sub_ciphertext.txt", "r")
    ciphertext = fp.read()
    fp.close()
    print("cipher text: " + ciphertext)

    map = {}
    char = 65
    for i in key:
        map[i] = chr(char)
        # print(i+" "+map[i])
        char = char + 1

    output = ""
    for i in ciphertext:

        char = ord(i)

        if 65 <= char <= 90:
            output += map[i]
        else:
            output += i

    print("original text: " + output)

    fp = open("solution01.txt", "w")
    fp.write(output)
    fp.close()


if __name__ == main():
    main()
