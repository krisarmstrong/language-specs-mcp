package checktest // import "crypto/internal/fips140/check/checktest"

Package checktest defines some code and data for use in the
crypto/internal/fips140/check test.

VARIABLES

var BSS *int
var DATA = struct {
	P *int
	X int
}{&NOPTRDATA, 3}
    DATA needs to have both a pointer and an int so that _some_ of it gets
    initialized at link time, so it is treated as DATA and not BSS. The pointer
    is deferred to init time.

var NOPTRBSS int
var NOPTRDATA int = 1
var RODATA int32 // set to 2 in asm.s
    The linkname here disables asan registration of this global, because asan
    gets mad about rodata globals.


FUNCTIONS

func PtrStaticData() *uint32
func PtrStaticText() unsafe.Pointer
func TEXT()
