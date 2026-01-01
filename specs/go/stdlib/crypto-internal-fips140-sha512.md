package sha512 // import "crypto/internal/fips140/sha512"

Package sha512 implements the SHA-384, SHA-512, SHA-512/224, and SHA-512/256
hash algorithms as defined in FIPS 180-4.

TYPES

type Digest struct {
	// Has unexported fields.
}
    Digest is a SHA-384, SHA-512, SHA-512/224, or SHA-512/256 hash.Hash
    implementation.

func New() *Digest
    New returns a new Digest computing the SHA-512 hash.

func New384() *Digest
    New384 returns a new Digest computing the SHA-384 hash.

func New512_224() *Digest
    New512_224 returns a new Digest computing the SHA-512/224 hash.

func New512_256() *Digest
    New512_256 returns a new Digest computing the SHA-512/256 hash.

func (d *Digest) AppendBinary(b []byte) ([]byte, error)

func (d *Digest) BlockSize() int

func (d *Digest) Clone() (hash.Cloner, error)

func (d *Digest) MarshalBinary() ([]byte, error)

func (d *Digest) Reset()

func (d *Digest) Size() int

func (d *Digest) Sum(in []byte) []byte

func (d *Digest) UnmarshalBinary(b []byte) error

func (d *Digest) Write(p []byte) (nn int, err error)

