from subprocess import call

numOfFile = 1
while True:
    if numOfFile == 64:
        break

    call("./fastcoll -p prefix -o col1 col2", shell=True)

    f1 = open("col1", "rb")
    str1 = f1.read()
    f1.close()
    l1 = len(str1) - 128

    f2 = open("col2", "rb")
    str2 = f2.read()
    f2.close()
    l2 = len(str2) - 128

    # print(l1, l2)

    k = 0
    for i in str1:
        if not l1:
            str1 = str1[k:]
            break
        l1 -= 1
        k += 1

    k = 0
    for i in str2:
        if not l2:
            str2 = str2[k:]
            break
        l2 -= 1
        k += 1

    cnt = 0
    for i in range(0, numOfFile):
        fTmp = "fTmp" + str(i)
        file = "file" + str(cnt)

        call("cat " + fTmp + " > " + file, shell=True)

        fp = open(file, "ab")
        fp.write(str1)
        fp.close()

        cnt += 1

        file = "file" + str(cnt)

        call("cat " + fTmp + " > " + file, shell=True)
        fp = open(file, "ab")
        fp.write(str2)
        fp.close()

        cnt += 1

    numOfFile *= 2
    
    for i in range(0, numOfFile):
        file = "file" + str(i)
        fTmp = "fTmp" + str(i)
        call("cat " + file + " > " + fTmp, shell=True)

    call("cat file0 > prefix", shell=True)