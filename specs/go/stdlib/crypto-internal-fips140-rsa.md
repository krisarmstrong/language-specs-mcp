package rsa // import "crypto/internal/fips140/rsa"


VARIABLES

var ErrDecryption = errors.New("crypto/rsa: decryption error")
var ErrMessageTooLong = errors.New("crypto/rsa: message too long for RSA key size")
var ErrVerification = errors.New("crypto/rsa: verification error")

FUNCTIONS

func DecryptOAEP(hash, mgfHash hash.Hash, priv *PrivateKey, ciphertext []byte, label []byte) ([]byte, error)
    DecryptOAEP decrypts ciphertext using RSAES-OAEP.

func DecryptWithCheck(priv *PrivateKey, ciphertext []byte) ([]byte, error)
    DecryptWithCheck performs the RSA private key operation and checks the
    result to defend against errors in the CRT computation.

func DecryptWithoutCheck(priv *PrivateKey, ciphertext []byte) ([]byte, error)
    DecryptWithoutCheck performs the RSA private key operation.

func Encrypt(pub *PublicKey, plaintext []byte) ([]byte, error)
    Encrypt performs the RSA public key operation.

func EncryptOAEP(hash, mgfHash hash.Hash, random io.Reader, pub *PublicKey, msg []byte, label []byte) ([]byte, error)
    EncryptOAEP encrypts the given message with RSAES-OAEP.

func PSSMaxSaltLength(pub *PublicKey, hash hash.Hash) (int, error)
    PSSMaxSaltLength returns the maximum salt length for a given public key and
    hash function.

func SignPKCS1v15(priv *PrivateKey, hash string, hashed []byte) ([]byte, error)
    SignPKCS1v15 calculates an RSASSA-PKCS1-v1.5 signature.

    hash is the name of the hash function as returned by crypto.Hash.String or
    the empty string to indicate that the message is signed directly.

func SignPSS(rand io.Reader, priv *PrivateKey, hash hash.Hash, hashed []byte, saltLength int) ([]byte, error)
    SignPSS calculates the signature of hashed using RSASSA-PSS.

func VerifyPKCS1v15(pub *PublicKey, hash string, hashed []byte, sig []byte) error
    VerifyPKCS1v15 verifies an RSASSA-PKCS1-v1.5 signature.

    hash is the name of the hash function as returned by crypto.Hash.String or
    the empty string to indicate that the message is signed directly.

func VerifyPSS(pub *PublicKey, hash hash.Hash, digest []byte, sig []byte) error
    VerifyPSS verifies sig with RSASSA-PSS automatically detecting the salt
    length.

func VerifyPSSWithSaltLength(pub *PublicKey, hash hash.Hash, digest []byte, sig []byte, saltLength int) error
    VerifyPSS verifies sig with RSASSA-PSS and an expected salt length.


TYPES

type PrivateKey struct {
	// Has unexported fields.
}

func GenerateKey(rand io.Reader, bits int) (*PrivateKey, error)
    GenerateKey generates a new RSA key pair of the given bit size. bits must be
    at least 32.

func NewPrivateKey(N []byte, e int, d, P, Q []byte) (*PrivateKey, error)
    NewPrivateKey creates a new RSA private key from the given parameters.

    All values are in big-endian byte slice format, and may have leading zeros
    or be shorter if leading zeroes were trimmed.

func NewPrivateKeyWithPrecomputation(N []byte, e int, d, P, Q, dP, dQ, qInv []byte) (*PrivateKey, error)
    NewPrivateKeyWithPrecomputation creates a new RSA private key from the given
    parameters, which include precomputed CRT values.

func NewPrivateKeyWithoutCRT(N []byte, e int, d []byte) (*PrivateKey, error)
    NewPrivateKeyWithoutCRT creates a new RSA private key from the given
    parameters.

    This is meant for deprecated multi-prime keys, and is not FIPS 140
    compliant.

func (priv *PrivateKey) Export() (N []byte, e int, d, P, Q, dP, dQ, qInv []byte)
    Export returns the key parameters in big-endian byte slice format.

    P, Q, dP, dQ, and qInv may be nil if the key was created with
    NewPrivateKeyWithoutCRT.

func (priv *PrivateKey) PublicKey() *PublicKey

type PublicKey struct {
	N *bigmod.Modulus
	E int
}

func (pub *PublicKey) Size() int
    Size returns the modulus size in bytes. Raw signatures and ciphertexts for
    or by this public key will have the same size.

