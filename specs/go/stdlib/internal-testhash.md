package testhash // import "internal/testhash"


FUNCTIONS

func TestHash(t *testing.T, mh MakeHash)
    TestHash performs a set of tests on hash.Hash implementations, checking the
    documented requirements of Write, Sum, Reset, Size, and BlockSize.

func TestHashWithoutClone(t *testing.T, mh MakeHash)

TYPES

type MakeHash func() hash.Hash

