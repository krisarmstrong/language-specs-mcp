package pbkdf2 // import "crypto/internal/fips140/pbkdf2"


FUNCTIONS

func Key[Hash hash.Hash](h func() Hash, password string, salt []byte, iter, keyLength int) ([]byte, error)
