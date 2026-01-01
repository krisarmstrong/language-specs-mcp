package ed25519 // import "crypto/internal/fips140/ed25519"


FUNCTIONS

func Sign(priv *PrivateKey, message []byte) []byte
func SignCtx(priv *PrivateKey, message []byte, context string) ([]byte, error)
func SignPH(priv *PrivateKey, message []byte, context string) ([]byte, error)
func Verify(pub *PublicKey, message, sig []byte) error
func VerifyCtx(pub *PublicKey, message []byte, sig []byte, context string) error
func VerifyPH(pub *PublicKey, message []byte, sig []byte, context string) error

TYPES

type PrivateKey struct {
	// Has unexported fields.
}

func GenerateKey() (*PrivateKey, error)
    GenerateKey generates a new Ed25519 private key pair.

func NewPrivateKey(priv []byte) (*PrivateKey, error)

func NewPrivateKeyFromSeed(seed []byte) (*PrivateKey, error)

func (priv *PrivateKey) Bytes() []byte

func (priv *PrivateKey) PublicKey() []byte

func (priv *PrivateKey) Seed() []byte

type PublicKey struct {
	// Has unexported fields.
}

func NewPublicKey(pub []byte) (*PublicKey, error)

func (pub *PublicKey) Bytes() []byte

