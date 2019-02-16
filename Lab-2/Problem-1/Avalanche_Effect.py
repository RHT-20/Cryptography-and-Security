def main():

    str1 = "de4960933bf2bac6dd5ab2b55543d20a2043e51b35adab3528cb7fd0454d55f2"
    # print(str1)

    str2 = "78ef06a64e25bc760134d5360a48bf038dafc5a7eab2390ada4d8bd6db19c49d"
    # print(str2)

    bin_str1 = bin(int(str1, 16))[2:].zfill(len(str1)*4)
    bin_str2 = bin(int(str2, 16))[2:].zfill(len(str2)*4)

    cnt = 0
    for i in range(0, len(bin_str1)):
        if bin_str1[i] != bin_str2[i]:
            cnt += 1

    print(cnt)

    fp = open("solution31.hex", "w")
    fp.write(hex(cnt))
    fp.close()


if __name__ == main():
    main()


# To generate SHA-256 hashes:
# openssl dgst -sha256 3.1_input_string.txt 3.1_perturbed_string.txt
