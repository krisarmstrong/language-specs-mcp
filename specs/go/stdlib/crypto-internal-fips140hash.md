package fips140hash // import "crypto/internal/fips140hash"


FUNCTIONS

func Unwrap(h hash.Hash) hash.Hash
    Unwrap returns h, or a crypto/internal/fips140 inner implementation of h.

    The return value can be type asserted to one
    of crypto/internal/fips140/sha256.Digest,
    crypto/internal/fips140/sha512.Digest, or
    crypto/internal/fips140/sha3.Digest if it is a FIPS 140-3 approved hash.

func UnwrapNew[Hash hash.Hash](newHash func() Hash) func() hash.Hash
    UnwrapNew returns a function that calls newHash and applies Unwrap to the
    return value.

