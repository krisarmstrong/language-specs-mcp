package gcm // import "crypto/internal/fips140/aes/gcm"


FUNCTIONS

func GHASH(key *[16]byte, inputs ...[]byte) []byte
    GHASH is exposed to allow crypto/cipher to implement non-AES GCM modes.
    It is not allowed as a stand-alone operation in FIPS mode because it is not
    ACVP tested.

func SealWithRandomNonce(g *GCM, nonce, out, plaintext, additionalData []byte)
    SealWithRandomNonce encrypts plaintext to out, and writes a random
    nonce to nonce. nonce must be 12 bytes, and out must be 16 bytes longer
    than plaintext. out and plaintext may overlap exactly or not at all.
    additionalData and out must not overlap.

    This complies with FIPS 140-3 IG C.H Scenario 2.

    Note that this is NOT a [cipher.AEAD].Seal method.


TYPES

type CMAC struct {
	// Has unexported fields.
}
    CMAC implements the CMAC mode from NIST SP 800-38B.

    It is optimized for use in Counter KDF (SP 800-108r1) and XAES-256-GCM
    (https://c2sp.org/XAES-256-GCM), rather than for exposing it to applications
    as a stand-alone MAC.

func NewCMAC(b *aes.Block) *CMAC

func (c *CMAC) MAC(m []byte) [aes.BlockSize]byte

type CounterKDF struct {
	// Has unexported fields.
}
    CounterKDF implements a KDF in Counter Mode instantiated with CMAC-AES,
    according to NIST SP 800-108 Revision 1 Update 1, Section 4.1.

    It produces a 256-bit output, and accepts a 8-bit Label and a 96-bit
    Context. It uses a counter of 16 bits placed before the fixed data. The
    fixed data is the sequence Label || 0x00 || Context. The L field is omitted,
    since the output key length is fixed.

    It's optimized for use in XAES-256-GCM (https://c2sp.org/XAES-256-GCM),
    rather than for exposing it to applications as a stand-alone KDF.

func NewCounterKDF(b *aes.Block) *CounterKDF
    NewCounterKDF creates a new CounterKDF with the given key.

func (kdf *CounterKDF) DeriveKey(label byte, context [12]byte) [32]byte
    DeriveKey derives a key from the given label and context.

type GCM struct {
	// Has unexported fields.
}
    GCM represents a Galois Counter Mode with a specific key.

func New(cipher *aes.Block, nonceSize, tagSize int) (*GCM, error)

func (g *GCM) NonceSize() int

func (g *GCM) Open(dst, nonce, ciphertext, data []byte) ([]byte, error)

func (g *GCM) Overhead() int

func (g *GCM) Seal(dst, nonce, plaintext, data []byte) []byte

type GCMForSSH struct {
	// Has unexported fields.
}

func NewGCMForSSH(cipher *aes.Block) (*GCMForSSH, error)
    NewGCMForSSH returns a new AEAD that works like GCM, but enforces the
    construction of nonces as specified in RFC 5647.

    This complies with FIPS 140-3 IG C.H Scenario 1.d.

func (g *GCMForSSH) NonceSize() int

func (g *GCMForSSH) Open(dst, nonce, ciphertext, data []byte) ([]byte, error)

func (g *GCMForSSH) Overhead() int

func (g *GCMForSSH) Seal(dst, nonce, plaintext, data []byte) []byte

type GCMForTLS12 struct {
	// Has unexported fields.
}

func NewGCMForTLS12(cipher *aes.Block) (*GCMForTLS12, error)
    NewGCMForTLS12 returns a new AEAD that works like GCM, but enforces the
    construction of nonces as specified in RFC 5288, Section 3 and RFC 9325,
    Section 7.2.1.

    This complies with FIPS 140-3 IG C.H Scenario 1.a.

func (g *GCMForTLS12) NonceSize() int

func (g *GCMForTLS12) Open(dst, nonce, ciphertext, data []byte) ([]byte, error)

func (g *GCMForTLS12) Overhead() int

func (g *GCMForTLS12) Seal(dst, nonce, plaintext, data []byte) []byte

type GCMForTLS13 struct {
	// Has unexported fields.
}

func NewGCMForTLS13(cipher *aes.Block) (*GCMForTLS13, error)
    NewGCMForTLS13 returns a new AEAD that works like GCM, but enforces the
    construction of nonces as specified in RFC 8446, Section 5.3.

func (g *GCMForTLS13) NonceSize() int

func (g *GCMForTLS13) Open(dst, nonce, ciphertext, data []byte) ([]byte, error)

func (g *GCMForTLS13) Overhead() int

func (g *GCMForTLS13) Seal(dst, nonce, plaintext, data []byte) []byte

type GCMWithCounterNonce struct {
	// Has unexported fields.
}

func NewGCMWithCounterNonce(cipher *aes.Block) (*GCMWithCounterNonce, error)
    NewGCMWithCounterNonce returns a new AEAD that works like GCM, but enforces
    the construction of deterministic nonces. The nonce must be 96 bits,
    the first 32 bits must be an encoding of the module name, and the last 64
    bits must be a counter.

    This complies with FIPS 140-3 IG C.H Scenario 3.

func (g *GCMWithCounterNonce) NonceSize() int

func (g *GCMWithCounterNonce) Open(dst, nonce, ciphertext, data []byte) ([]byte, error)

func (g *GCMWithCounterNonce) Overhead() int

func (g *GCMWithCounterNonce) Seal(dst, nonce, plaintext, data []byte) []byte

