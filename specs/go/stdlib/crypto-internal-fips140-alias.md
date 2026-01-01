package alias // import "crypto/internal/fips140/alias"

Package alias implements memory aliasing tests. This code also exists as
golang.org/x/crypto/internal/alias.

FUNCTIONS

func AnyOverlap(x, y []byte) bool
    AnyOverlap reports whether x and y share memory at any (not necessarily
    corresponding) index. The memory beyond the slice length is ignored.

func InexactOverlap(x, y []byte) bool
    InexactOverlap reports whether x and y share memory at any non-corresponding
    index. The memory beyond the slice length is ignored. Note that x and y can
    have different lengths and still not have any inexact overlap.

    InexactOverlap can be used to implement the requirements of the
    crypto/cipher AEAD, Block, BlockMode and Stream interfaces.

