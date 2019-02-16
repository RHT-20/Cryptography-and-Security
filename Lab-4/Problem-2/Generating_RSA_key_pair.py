from Crypto.PublicKey import RSA


def main():

    key = RSA.generate(2048)
    public_key = key.publickey()
    private_key = key.exportKey('PEM')

    message = "hello world"

    encrypted_message = key.encrypt(message, public_key)
    print("Encrypted Message: " + str(encrypted_message))
    decrypted_message = key.decrypt(encrypted_message)
    print("Decrypted Message: " + str(decrypted_message))

    encrypted_message = key.encrypt(message, private_key)
    print("Encrypted Message: " + str(encrypted_message))
    decrypted_message = key.decrypt(encrypted_message)
    print("Decrypted Message: " + str(decrypted_message))


if __name__ == main():
    main()


# Run from Terminal:
# python2 Generating_RSA_key_pair.py
