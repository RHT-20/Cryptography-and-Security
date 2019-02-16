from Crypto.Cipher import AES
import codecs


def main():

    fp = open("aes_key.hex", "r")
    tmp = fp.read()
    fp.close()
    key = codecs.decode(tmp, "hex")
    print("key: " + tmp)

    fp = open("aes_iv.hex", "r")
    tmp = fp.read()
    fp.close()
    iv = codecs.decode(tmp, "hex")
    print("iv: " + tmp)

    fp = open("aes_ciphertext.hex", "r")
    tmp = fp.read()
    fp.close()
    ciphertext = codecs.decode(tmp, "hex")
    print("cipher text: " + tmp)

    obj = AES.new(key, AES.MODE_CBC, iv)
    text = obj.decrypt(ciphertext).decode("ascii")
    print("original text: " + text)

    fp = open("solution02.txt", "w")
    fp.write(text)
    fp.close()


if __name__ == main():
    main()
