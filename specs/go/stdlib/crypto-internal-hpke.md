package hpke // import "crypto/internal/hpke"


CONSTANTS

const (
	AEAD_AES_128_GCM      = 0x0001
	AEAD_AES_256_GCM      = 0x0002
	AEAD_ChaCha20Poly1305 = 0x0003
)
const DHKEM_X25519_HKDF_SHA256 = 0x0020
const KDF_HKDF_SHA256 = 0x0001

VARIABLES

var SupportedAEADs = map[uint16]struct {
	keySize   int
	nonceSize int
	aead      func([]byte) (cipher.AEAD, error)
}{

	AEAD_AES_128_GCM:      {keySize: 16, nonceSize: 12, aead: aesGCMNew},
	AEAD_AES_256_GCM:      {keySize: 32, nonceSize: 12, aead: aesGCMNew},
	AEAD_ChaCha20Poly1305: {keySize: chacha20poly1305.KeySize, nonceSize: chacha20poly1305.NonceSize, aead: chacha20poly1305.New},
}
var SupportedKDFs = map[uint16]func() *hkdfKDF{

	KDF_HKDF_SHA256: func() *hkdfKDF { return &hkdfKDF{crypto.SHA256} },
}
var SupportedKEMs = map[uint16]struct {
	curve   ecdh.Curve
	hash    crypto.Hash
	nSecret uint16
}{

	DHKEM_X25519_HKDF_SHA256: {ecdh.X25519(), crypto.SHA256, 32},
}

FUNCTIONS

func ParseHPKEPrivateKey(kemID uint16, bytes []byte) (*ecdh.PrivateKey, error)
func ParseHPKEPublicKey(kemID uint16, bytes []byte) (*ecdh.PublicKey, error)

TYPES

type AEADID uint16

type KDFID uint16

type KemID uint16

type Recipient struct {
	// Has unexported fields.
}

func SetupRecipient(kemID, kdfID, aeadID uint16, priv *ecdh.PrivateKey, info, encPubEph []byte) (*Recipient, error)

func (r *Recipient) Open(aad, ciphertext []byte) ([]byte, error)

type Sender struct {
	// Has unexported fields.
}

func SetupSender(kemID, kdfID, aeadID uint16, pub *ecdh.PublicKey, info []byte) ([]byte, *Sender, error)

func (s *Sender) Seal(aad, plaintext []byte) ([]byte, error)

