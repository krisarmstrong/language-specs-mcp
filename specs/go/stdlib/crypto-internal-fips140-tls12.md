package tls12 // import "crypto/internal/fips140/tls12"


FUNCTIONS

func MasterSecret[H hash.Hash](hash func() H, preMasterSecret, transcript []byte) []byte
    MasterSecret implements the TLS 1.2 extended master secret derivation,
    as defined in RFC 7627 and allowed by SP 800-135, Revision 1, Section 4.2.2.

func PRF[H hash.Hash](hash func() H, secret []byte, label string, seed []byte, keyLen int) []byte
    PRF implements the TLS 1.2 pseudo-random function, as defined in RFC 5246,
    Section 5 and allowed by SP 800-135, Revision 1, Section 4.2.2.

