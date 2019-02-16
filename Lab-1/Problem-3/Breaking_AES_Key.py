from Crypto.Cipher import AES
import codecs


def check(key, iv):

    key_str = key
    key = codecs.decode(key, "hex")
    iv = codecs.decode(iv, "hex")

    fp = open("aes_weak_ciphertext.hex", "r")
    ciphertext = codecs.decode(fp.read(), "hex")
    fp.close()

    obj = AES.new(key, AES.MODE_CBC, iv)
    text = obj.decrypt(ciphertext)

    try:
        text = text.decode("ascii")
        print("key: " + key_str)
        print("text: " + text)

        fp = open("Solution03.hex", "w")
        fp.write(key_str)
        fp.close()

        return True
    except:
        return False


def main():

    iv = ""
    for i in range(32):
        iv += "0"
    # print(len(iv))

    tmp = ""
    for i in range(64):
        tmp += "0"
    # print(len(tmp))

    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in list:
        for j in range(2):
            key = tmp[:62] + list[j] + i
            # print(key)

            if check(key, iv):
                break


if __name__ == main():
    main()
