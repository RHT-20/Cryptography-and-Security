import base64


def main():

    cipher = "aGVsbG8geW91IGFyZSBhd2Vzb21lIGZsYWcgaXMgY2hhcmlzbWE="
    plaintext = base64.b64decode(cipher)
    plaintext = plaintext.decode("ascii")
    # print(cipher + "" + plaintext)
    print(plaintext)


if __name__ == main():
    main()
