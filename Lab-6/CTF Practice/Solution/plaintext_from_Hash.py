import pymd5


def main():

    hash1 = "202cb962ac59075b964b07152d234b70"

    plaintext = "123"
    print("Plain text: " + plaintext)
    md5_obj = pymd5.md5(plaintext)
    hash2 = md5_obj.hexdigest()

    print(hash1)
    print(hash2)

    if hash1 == hash2:
        print("Ok")
    else:
        print("Not Ok")


if __name__ == main():
    main()
