package math // import "internal/runtime/math"


CONSTANTS

const (
	MaxUint32  = ^uint32(0)
	MaxUint64  = ^uint64(0)
	MaxUintptr = ^uintptr(0)

	MaxInt64 = int64(MaxUint64 >> 1)
)

FUNCTIONS

func Add64(x, y, carry uint64) (sum, carryOut uint64)
    Add64 returns the sum with carry of x, y and carry: sum = x + y + carry.
    The carry input must be 0 or 1; otherwise the behavior is undefined.
    The carryOut output is guaranteed to be 0 or 1.

    This function's execution time does not depend on the inputs. On supported
    platforms this is an intrinsic lowered by the compiler.

func Mul64(x, y uint64) (hi, lo uint64)
    Mul64 returns the 128-bit product of x and y: (hi, lo) = x * y with the
    product bits' upper half returned in hi and the lower half returned in lo.
    This is a copy from math/bits.Mul64 On supported platforms this is an
    intrinsic lowered by the compiler.

func MulUintptr(a, b uintptr) (uintptr, bool)
    MulUintptr returns a * b and whether the multiplication overflowed.
    On supported platforms this is an intrinsic lowered by the compiler.

