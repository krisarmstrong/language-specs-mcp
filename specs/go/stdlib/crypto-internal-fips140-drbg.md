package drbg // import "crypto/internal/fips140/drbg"

Package drbg provides cryptographically secure random bytes usable by FIPS code.
In FIPS mode it uses an SP 800-90A Rev. 1 Deterministic Random Bit Generator
(DRBG). Otherwise, it uses the operating system's random number generator.

CONSTANTS

const (
	SeedSize = keySize + aes.BlockSize
)

FUNCTIONS

func Read(b []byte)
    Read fills b with cryptographically secure random bytes. In FIPS mode,
    it uses an SP 800-90A Rev. 1 Deterministic Random Bit Generator (DRBG).
    Otherwise, it uses the operating system's random number generator.

func ReadWithReader(r io.Reader, b []byte) error
    ReadWithReader uses Reader to fill b with cryptographically secure random
    bytes. It is intended for use in APIs that expose a rand io.Reader.

    If Reader is not the default Reader from crypto/rand, randutil.MaybeReadByte
    and fips140.RecordNonApproved are called.

func ReadWithReaderDeterministic(r io.Reader, b []byte) error
    ReadWithReaderDeterministic is like ReadWithReader, but it doesn't call
    randutil.MaybeReadByte on non-default Readers.


TYPES

type Counter struct {
	// Has unexported fields.
}
    Counter is an SP 800-90A Rev. 1 CTR_DRBG instantiated with AES-256.

    Per Table 3, it has a security strength of 256 bits, a seed size of 384
    bits, a counter length of 128 bits, a reseed interval of 2^48 requests,
    and a maximum request size of 2^19 bits (2^16 bytes, 64 KiB).

    We support a narrow range of parameters that fit the needs of our RNG:
    AES-256, no derivation function, no personalization string, no prediction
    resistance, and 384-bit additional input.

    WARNING: this type provides tightly scoped support for the DRBG
    functionality we need for FIPS 140-3 _only_. This type _should not_ be used
    outside of the FIPS 140-3 module for any other use.

    In particular, as documented, Counter does not support the derivation
    function, or personalization strings which are necessary for safely using
    this DRBG for generic purposes without leaking sensitive values.

func NewCounter(entropy *[SeedSize]byte) *Counter

func (c *Counter) Generate(out []byte, additionalInput *[SeedSize]byte) (reseedRequired bool)
    Generate produces at most maxRequestSize bytes of random data in out.

func (c *Counter) Reseed(entropy, additionalInput *[SeedSize]byte)

type DefaultReader interface {
	// Has unexported methods.
}
    DefaultReader is a sentinel type, embedded in the default
    crypto/rand.Reader, used to recognize it when passed to APIs that accept a
    rand io.Reader.

