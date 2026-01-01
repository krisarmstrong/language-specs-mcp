package sha256 // import "crypto/internal/fips140/sha256"

Package sha256 implements the SHA-224 and SHA-256 hash algorithms as defined in
FIPS 180-4.

TYPES

type Digest struct {
	// Has unexported fields.
}
    Digest is a SHA-224 or SHA-256 hash.Hash implementation.

func New() *Digest
    New returns a new Digest computing the SHA-256 hash.

func New224() *Digest
    New224 returns a new Digest computing the SHA-224 hash.

func (d *Digest) AppendBinary(b []byte) ([]byte, error)

func (d *Digest) BlockSize() int

func (d *Digest) Clone() (hash.Cloner, error)

func (d *Digest) MarshalBinary() ([]byte, error)

func (d *Digest) Reset()

func (d *Digest) Size() int

func (d *Digest) Sum(in []byte) []byte

func (d *Digest) UnmarshalBinary(b []byte) error

func (d *Digest) Write(p []byte) (nn int, err error)

