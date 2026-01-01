package hkdf // import "crypto/internal/fips140/hkdf"


FUNCTIONS

func Expand[H hash.Hash](h func() H, pseudorandomKey []byte, info string, keyLen int) []byte
func Extract[H hash.Hash](h func() H, secret, salt []byte) []byte
func Key[H hash.Hash](h func() H, secret, salt []byte, info string, keyLen int) []byte
