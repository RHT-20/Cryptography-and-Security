def WHA(input_str):

    mask = 0x3FFFFFFF
    # print(bin(mask))

    outHash = 0
    for i in input_str:
        byte = ord(i)

        intermediate_value = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
        # print(bin(intermediate_value))

        outHash = (outHash & mask) + (intermediate_value & mask)

    # print(outHash)
    print(hex(outHash))

    return outHash


def main():

    fp = open("3.2_input_string.txt", "r")
    input_str = fp.read()
    fp.close()
    print(input_str)

    output_str = input_str[len(input_str)-1:] + input_str[0:len(input_str)-1]
    print(output_str)

    WHA(input_str)
    WHA(output_str)

    fp = open("solution32.txt", "w")
    fp.write(output_str)
    fp.close()


if __name__ == main():
    main()


# Solution: any permutation of the input string.
