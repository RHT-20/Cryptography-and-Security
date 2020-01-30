.global _main

.data
filename: .string "/bin/sh"

.section .text

_main:

push	%ebp
mov	%esp,%ebp

mov	$0xb, %eax
mov	$filename, %ebx

push	$0x0
push	$filename
mov	%esp, %ecx

mov	$0x0, %edx

int $0x80

leave
ret

