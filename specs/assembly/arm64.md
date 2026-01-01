# ARM64 (AArch64) Assembly Reference

## Registers

### General Purpose

| Register | Alias | Purpose |
|----------|-------|---------|
| X0-X7 | - | Arguments/results, caller-saved |
| X8 | XR | Indirect result location |
| X9-X15 | - | Temporary, caller-saved |
| X16-X17 | IP0-IP1 | Intra-procedure scratch |
| X18 | PR | Platform register (reserved) |
| X19-X28 | - | Callee-saved |
| X29 | FP | Frame pointer |
| X30 | LR | Link register (return address) |
| SP | - | Stack pointer |
| XZR | - | Zero register (reads as 0, writes ignored) |
| PC | - | Program counter (not directly accessible) |

### 32-bit Aliases

W0-W30 = lower 32 bits of X0-X30
WZR = 32-bit zero register
WSP = 32-bit stack pointer

### Special Registers

```asm
// System registers (EL0 accessible)
MRS X0, NZCV        // Condition flags
MSR NZCV, X0

// PSTATE flags
N - Negative
Z - Zero  
C - Carry
V - Overflow
```

### SIMD/FP Registers

```asm
// 128-bit vector registers
V0-V31

// Scalar views
B0-B31   // 8-bit
H0-H31   // 16-bit
S0-S31   // 32-bit (single)
D0-D31   // 64-bit (double)
Q0-Q31   // 128-bit (quad)
```

## Calling Convention (AAPCS64)

```asm
// Arguments: X0-X7 (integer), V0-V7 (float)
// Return: X0 (and X1 for 128-bit)
// Caller-saved: X0-X18, V0-V7, V16-V31
// Callee-saved: X19-X28, V8-V15
// Stack: 16-byte aligned

// Function prologue
my_func:
    stp x29, x30, [sp, #-16]!  // Push FP and LR
    mov x29, sp                  // Set frame pointer

// Function epilogue
    ldp x29, x30, [sp], #16     // Pop FP and LR
    ret
```

## Addressing Modes

```asm
// Immediate offset
LDR X0, [X1]            // Base
LDR X0, [X1, #8]        // Base + offset
LDR X0, [X1, #-8]       // Base - offset

// Register offset
LDR X0, [X1, X2]        // Base + register
LDR X0, [X1, X2, LSL #3] // Base + (register << 3)

// Pre-indexed (update base)
LDR X0, [X1, #8]!       // X1 += 8, then load

// Post-indexed (update base)
LDR X0, [X1], #8        // Load, then X1 += 8

// PC-relative
LDR X0, label           // PC-relative literal
ADR X0, label           // PC-relative address
ADRP X0, label          // PC-relative page address
```

## Data Movement

```asm
// Move
MOV X0, X1              // Register to register
MOV X0, #42             // Immediate (16-bit)
MOV X0, #0xFFFF0000     // Immediate with shift
MOVN X0, #0             // Move NOT
MOVZ X0, #0x1234        // Move with zero
MOVK X0, #0x5678, LSL #16  // Move keep

// Load/Store
LDR X0, [X1]            // Load 64-bit
LDRB W0, [X1]           // Load byte (zero extend)
LDRH W0, [X1]           // Load halfword
LDRSB X0, [X1]          // Load byte (sign extend)
LDRSH X0, [X1]          // Load halfword (sign extend)
LDRSW X0, [X1]          // Load word (sign extend)

STR X0, [X1]            // Store 64-bit
STRB W0, [X1]           // Store byte
STRH W0, [X1]           // Store halfword

// Load/Store pair
LDP X0, X1, [X2]        // Load pair
STP X0, X1, [X2]        // Store pair

// Exclusive access (atomics)
LDXR X0, [X1]           // Load exclusive
STXR W2, X0, [X1]       // Store exclusive (W2 = status)
```

## Arithmetic

```asm
// Addition/Subtraction
ADD X0, X1, X2          // X0 = X1 + X2
ADD X0, X1, #42         // X0 = X1 + 42
ADDS X0, X1, X2         // Add, set flags
SUB X0, X1, X2          // Subtract
SUBS X0, X1, X2         // Subtract, set flags
ADC X0, X1, X2          // Add with carry
SBC X0, X1, X2          // Subtract with carry
NEG X0, X1              // Negate

// Multiplication
MUL X0, X1, X2          // X0 = X1 * X2 (low 64 bits)
SMULL X0, W1, W2        // Signed multiply long
UMULL X0, W1, W2        // Unsigned multiply long
SMULH X0, X1, X2        // Signed multiply high
UMULH X0, X1, X2        // Unsigned multiply high
MADD X0, X1, X2, X3     // X0 = X3 + X1 * X2
MSUB X0, X1, X2, X3     // X0 = X3 - X1 * X2

// Division
SDIV X0, X1, X2         // Signed divide
UDIV X0, X1, X2         // Unsigned divide
```

## Bitwise Operations

```asm
// Logical
AND X0, X1, X2          // Bitwise AND
ORR X0, X1, X2          // Bitwise OR
EOR X0, X1, X2          // Bitwise XOR
BIC X0, X1, X2          // Bit clear (AND NOT)
ORN X0, X1, X2          // OR NOT
EON X0, X1, X2          // XOR NOT
MVN X0, X1              // NOT

// Shifts
LSL X0, X1, #4          // Logical shift left
LSR X0, X1, #4          // Logical shift right
ASR X0, X1, #4          // Arithmetic shift right
ROR X0, X1, #4          // Rotate right

// Bit manipulation
CLZ X0, X1              // Count leading zeros
RBIT X0, X1             // Reverse bits
REV X0, X1              // Reverse bytes
REV16 X0, X1            // Reverse bytes in halfwords
REV32 X0, X1            // Reverse bytes in words
```

## Comparison and Branching

```asm
// Compare
CMP X0, X1              // Compare (SUBS, discard result)
CMP X0, #42             // Compare with immediate
CMN X0, X1              // Compare negative (ADDS)
TST X0, X1              // Test bits (ANDS)
TST X0, #0xFF           // Test with immediate

// Conditional branch
B.EQ label              // Branch if equal (Z=1)
B.NE label              // Branch if not equal (Z=0)
B.LT label              // Branch if less than (signed)
B.LE label              // Branch if less or equal
B.GT label              // Branch if greater than
B.GE label              // Branch if greater or equal
B.LO label              // Branch if lower (unsigned, C=0)
B.LS label              // Branch if lower or same
B.HI label              // Branch if higher (unsigned)
B.HS label              // Branch if higher or same (C=1)
B.MI label              // Branch if minus (N=1)
B.PL label              // Branch if plus (N=0)
B.VS label              // Branch if overflow (V=1)
B.VC label              // Branch if no overflow

// Unconditional branch
B label                 // Branch
BL label                // Branch with link (call)
BR X0                   // Branch to register
BLR X0                  // Branch with link to register
RET                     // Return (BR X30)

// Compare and branch
CBZ X0, label           // Branch if zero
CBNZ X0, label          // Branch if not zero
TBZ X0, #5, label       // Test bit and branch if zero
TBNZ X0, #5, label      // Test bit and branch if not zero
```

## Conditional Operations

```asm
// Conditional select
CSEL X0, X1, X2, EQ     // X0 = (EQ) ? X1 : X2
CSINC X0, X1, X2, NE    // X0 = (NE) ? X1 : X2+1
CSINV X0, X1, X2, LT    // X0 = (LT) ? X1 : ~X2
CSNEG X0, X1, X2, GT    // X0 = (GT) ? X1 : -X2

// Conditional increment/negate
CINC X0, X1, EQ         // X0 = (EQ) ? X1+1 : X1
CNEG X0, X1, EQ         // X0 = (EQ) ? -X1 : X1
CSET X0, EQ             // X0 = (EQ) ? 1 : 0
CSETM X0, EQ            // X0 = (EQ) ? -1 : 0
```

## SIMD/NEON

```asm
// Load/Store
LD1 {V0.16B}, [X0]      // Load 16 bytes
LD1 {V0.8H}, [X0]       // Load 8 halfwords
LD1 {V0.4S}, [X0]       // Load 4 singles
LD1 {V0.2D}, [X0]       // Load 2 doubles
ST1 {V0.16B}, [X0]      // Store

// Arithmetic
ADD V0.4S, V1.4S, V2.4S // Vector add
SUB V0.4S, V1.4S, V2.4S // Vector subtract
MUL V0.4S, V1.4S, V2.4S // Vector multiply
FADD V0.4S, V1.4S, V2.4S // Float add
FMUL V0.4S, V1.4S, V2.4S // Float multiply

// Comparison
CMEQ V0.4S, V1.4S, V2.4S // Compare equal
CMGT V0.4S, V1.4S, V2.4S // Compare greater than
```

## System Instructions

```asm
// Memory barriers
DMB SY                  // Data memory barrier
DSB SY                  // Data synchronization barrier
ISB                     // Instruction synchronization barrier

// Cache operations
DC CVAC, X0             // Clean data cache
IC IVAU, X0             // Invalidate instruction cache

// System calls
SVC #0                  // Supervisor call (syscall)
HVC #0                  // Hypervisor call
SMC #0                  // Secure monitor call

// Hints
NOP                     // No operation
WFE                     // Wait for event
WFI                     // Wait for interrupt
SEV                     // Send event
YIELD                   // Yield
```

## Common Patterns

### Function Call

```asm
// Call function with 4 arguments
MOV X0, #1              // arg1
MOV X1, #2              // arg2
MOV X2, #3              // arg3
MOV X3, #4              // arg4
BL function

// Save/restore callee-saved registers
func:
    STP X29, X30, [SP, #-32]!
    STP X19, X20, [SP, #16]
    MOV X29, SP
    
    // function body
    
    LDP X19, X20, [SP, #16]
    LDP X29, X30, [SP], #32
    RET
```

### Loop

```asm
// for (int i = 0; i < n; i++)
    MOV X19, #0         // i = 0
loop:
    CMP X19, X20        // i < n?
    B.GE done
    
    // loop body
    
    ADD X19, X19, #1    // i++
    B loop
done:
```

### System Call (Linux)

```asm
// write(1, message, length)
MOV X0, #1              // fd = stdout
ADR X1, message         // buffer
MOV X2, #13             // length
MOV X8, #64             // syscall: write
SVC #0

// exit(0)
MOV X0, #0              // status
MOV X8, #93             // syscall: exit
SVC #0
```
