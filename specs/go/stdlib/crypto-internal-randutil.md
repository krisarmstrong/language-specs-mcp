package randutil // import "crypto/internal/randutil"

Package randutil contains internal randomness utilities for various crypto
packages.

FUNCTIONS

func MaybeReadByte(r io.Reader)
    MaybeReadByte reads a single byte from r with 50% probability. This is
    used to ensure that callers do not depend on non-guaranteed behaviour, e.g.
    assuming that rsa.GenerateKey is deterministic w.r.t. a given random stream.

    This does not affect tests that pass a stream of fixed bytes as the random
    source (e.g. a zeroReader).

