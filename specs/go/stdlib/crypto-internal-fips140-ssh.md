package ssh // import "crypto/internal/fips140/ssh"

Package ssh implements the SSH KDF as specified in RFC 4253, Section 7.2 and
allowed by SP 800-135 Revision 1.

FUNCTIONS

func Keys[Hash hash.Hash](hash func() Hash, d Direction,
	K, H, sessionID []byte,
	ivKeyLen, keyLen, macKeyLen int,
) (ivKey, key, macKey []byte)

TYPES

type Direction struct {
	// Has unexported fields.
}

var ServerKeys, ClientKeys Direction
