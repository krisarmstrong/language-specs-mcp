# Assembly Generation Checklist

**Read this BEFORE writing assembly code. These fundamentals prevent bugs.**

## Critical: You Must Do These

### 1. Save and Restore Callee-Saved Registers
```asm
; x86-64 (System V ABI): rbx, rbp, r12-r15 must be preserved
; Windows: rbx, rbp, rdi, rsi, r12-r15 must be preserved

; BAD - clobbers callee-saved register
my_function:
    mov rbx, rdi        ; Overwrites caller's rbx!
    ; ...
    ret

; GOOD - save and restore
my_function:
    push rbx            ; Save callee-saved
    push r12

    mov rbx, rdi        ; Now safe to use
    ; ...

    pop r12             ; Restore in reverse order
    pop rbx
    ret
```

### 2. Maintain Stack Alignment
```asm
; x86-64: Stack must be 16-byte aligned before CALL

; BAD - misaligned call
my_function:
    push rbx            ; Stack now 8-byte aligned
    call other_func     ; CRASH or undefined behavior!

; GOOD - maintain alignment
my_function:
    push rbx            ; -8 bytes
    sub rsp, 8          ; Align to 16 bytes

    call other_func     ; Stack is aligned

    add rsp, 8
    pop rbx
    ret

; Or use even number of pushes
my_function:
    push rbx
    push r12            ; Two pushes = 16 bytes, aligned
    call other_func
    pop r12
    pop rbx
    ret
```

### 3. Clear Direction Flag Before String Operations
```asm
; BAD - assumes DF is clear
my_function:
    rep movsb           ; Direction unknown!

; GOOD - explicitly clear
my_function:
    cld                 ; Clear direction flag (forward)
    rep movsb

; Or set if needed
    std                 ; Set for backward
    rep movsb
    cld                 ; Always clear before return (ABI requirement)
```

### 4. Zero-Extend When Moving to Larger Registers
```asm
; BAD - upper bits may contain garbage
mov eax, [data]         ; Clears upper 32 bits (OK in x86-64)
movzx rax, byte [data]  ; GOOD - zero-extends
movsx rax, byte [data]  ; GOOD - sign-extends

; On x86-64, writing to 32-bit register zeros upper 32 bits
mov eax, 5              ; rax = 0x0000000000000005 (OK)

; But 8/16-bit writes don't clear upper bits
mov al, 5               ; Only changes lowest byte
mov ax, 5               ; Only changes lowest 16 bits
```

### 5. Use Appropriate Memory Addressing
```asm
; Always specify size when ambiguous
; BAD
mov [rdi], 0            ; What size? Error!

; GOOD - explicit size
mov byte [rdi], 0       ; 1 byte
mov word [rdi], 0       ; 2 bytes
mov dword [rdi], 0      ; 4 bytes
mov qword [rdi], 0      ; 8 bytes
```

## Important: Strong Recommendations

### 6. Comment Register Usage
```asm
; GOOD - document what each register holds
; Input:  rdi = pointer to buffer
;         rsi = buffer length
;         rdx = character to find
; Output: rax = index of character, or -1 if not found
; Clobbers: rcx, r8
find_char:
    xor eax, eax            ; index = 0
.loop:
    cmp rax, rsi            ; if index >= length
    jge .not_found          ;   return -1
    cmp byte [rdi + rax], dl; if buffer[index] == char
    je .found               ;   return index
    inc rax                 ; index++
    jmp .loop
```

### 7. Use Local Labels for Loop Targets
```asm
; BAD - pollutes global namespace
outer_loop:
    ; ...
inner_loop:             ; Name collision risk
    ; ...
    jmp inner_loop
    jmp outer_loop

; GOOD - local labels (NASM syntax)
process_array:
.outer:
    ; ...
.inner:
    ; ...
    jmp .inner          ; Local to process_array
    jmp .outer

; In GAS, use numeric labels
1:
    ; ...
    jmp 1b              ; Jump backward to 1
    jmp 1f              ; Jump forward to 1
```

### 8. Prefer Efficient Instructions
```asm
; Zeroing a register
mov rax, 0              ; 7 bytes
xor eax, eax            ; 2 bytes, faster, clears flags predictably

; Testing for zero
cmp rax, 0              ; Longer encoding
test rax, rax           ; Preferred, same effect on ZF

; Multiplication by small constants
imul rax, 5             ; OK
lea rax, [rax + rax*4]  ; Often faster for small constants

; Doubling
add rax, rax            ; Preferred over shl rax, 1
```

### 9. Handle Carry/Overflow Correctly
```asm
; Check for overflow after addition
add rax, rbx
jc .overflow            ; Unsigned overflow
jo .signed_overflow     ; Signed overflow

; Multi-precision addition (128-bit example)
add rax, [num2_low]     ; Add low parts
adc rdx, [num2_high]    ; Add high parts + carry
```

### 10. Use Proper Calling Conventions
```asm
; System V AMD64 (Linux, macOS):
; Args: rdi, rsi, rdx, rcx, r8, r9, then stack
; Return: rax (rdx:rax for 128-bit)
; Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

; Windows x64:
; Args: rcx, rdx, r8, r9, then stack
; Shadow space: 32 bytes before call
; Return: rax

; Example: calling printf on Linux
section .data
    fmt: db "Value: %d", 10, 0

section .text
    mov rdi, fmt        ; First arg: format string
    mov esi, 42         ; Second arg: value (32-bit OK)
    xor eax, eax        ; No vector args
    call printf
```

## Memory and Data

### 11. Align Data Appropriately
```asm
section .data
    align 16            ; Align to 16 bytes for SSE
    vector: times 4 dd 1.0

    align 8
    value: dq 0

section .bss
    align 4096          ; Page-aligned buffer
    buffer: resb 4096
```

### 12. Use Appropriate Section for Data
```asm
section .data           ; Initialized data (read-write)
    count: dd 10
    message: db "Hello", 0

section .rodata         ; Read-only data
    constant: dq 3.14159

section .bss            ; Uninitialized data
    buffer: resb 1024   ; Reserve 1024 bytes

section .text           ; Code
    global main
main:
    ; ...
```

### 13. Handle SIMD Alignment Requirements
```asm
; SSE requires 16-byte alignment for movaps
movaps xmm0, [rdi]      ; Requires 16-byte aligned address
movups xmm0, [rdi]      ; Unaligned OK but slower

; AVX relaxes alignment for VEX-encoded instructions
vmovaps ymm0, [rdi]     ; Still better if aligned
vmovups ymm0, [rdi]     ; OK unaligned

; Check alignment at runtime if needed
test rdi, 15            ; Check if 16-byte aligned
jnz .unaligned
```

## Security

### 14. Clear Sensitive Data
```asm
; After using sensitive data, clear it
; Simple clear (may be optimized away)
mov qword [secret], 0

; More reliable: use volatile operations
; or mark memory as volatile in inline asm

; Clear registers
xor eax, eax
xor edx, edx
```

### 15. Avoid Buffer Overflows
```asm
; BAD - no bounds check
copy_string:
    mov al, [rsi]
    mov [rdi], al
    inc rsi
    inc rdi
    test al, al
    jnz copy_string
    ret

; GOOD - check bounds
copy_string_safe:
    ; rdi = dest, rsi = src, rdx = max_len
    test rdx, rdx
    jz .done
.loop:
    mov al, [rsi]
    mov [rdi], al
    test al, al
    jz .done
    inc rsi
    inc rdi
    dec rdx
    jnz .loop
.done:
    ret
```

---

**Quick Reference - Copy This Mental Model:**
- Save/restore callee-saved registers
- Maintain 16-byte stack alignment before calls
- `cld` before string operations
- Zero-extend when needed (movzx)
- Explicit memory operand sizes
- Comment register usage thoroughly
- Local labels for loops (`.label`)
- `xor reg, reg` to zero
- `test reg, reg` for zero check
- Follow calling convention precisely
- Align data appropriately
- Handle SIMD alignment
- Clear sensitive data
