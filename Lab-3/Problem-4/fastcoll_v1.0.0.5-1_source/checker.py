import pymd5

md5 = ""
for i in range(0, 64):
    file = "file" + str(i)
    fp = open(file, "rb")
    s = fp.read()
    fp.close()

    obj = pymd5.md5(s)
    hexd = obj.hexdigest()
    print(hexd)

    if not i:
        md5 = hexd
        print(md5)
    elif md5 != hexd:
        break

print("ok")


f1 = open("hash.hex", "w")
f1.write("1d9743e14477a3c10568b07ddb604c70")
f1.close()
