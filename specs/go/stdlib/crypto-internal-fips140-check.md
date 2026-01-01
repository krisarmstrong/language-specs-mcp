package check // import "crypto/internal/fips140/check"

Package check implements the FIPS 140 load-time code+data verification.
Every FIPS package providing cryptographic functionality except hmac and sha256
must import crypto/internal/fips140/check, so that the verification happens
before initialization of package global variables. The hmac and sha256 packages
are used by this package, so they cannot import it. Instead, those packages
must be careful not to change global variables during init. (If necessary,
we could have check call a PostCheck function in those packages after the check
has completed.)

VARIABLES

var Linkinfo struct {
	Magic [16]byte
	Sum   [32]byte
	Self  uintptr
	Sects [4]struct {
		// Note: These must be unsafe.Pointer, not uintptr,
		// or else checkptr panics about turning uintptrs
		// into pointers into the data segment during
		// go test -race.
		Start unsafe.Pointer
		End   unsafe.Pointer
	}
}
    Linkinfo holds the go:fipsinfo symbol prepared by the linker. See
    cmd/link/internal/ld/fips.go for details.

var Verified bool
    Verified is set when verification succeeded. It can be expected to always be
    true when fips140.Enabled is true, or init would have panicked.

