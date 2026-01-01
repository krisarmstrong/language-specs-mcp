package sig // import "crypto/internal/boring/sig"

Package sig holds “code signatures” that can be called and will result in
certain code sequences being linked into the final binary. The functions
themselves are no-ops.

FUNCTIONS

func BoringCrypto()
    BoringCrypto indicates that the BoringCrypto module is present.

func FIPSOnly()
    FIPSOnly indicates that package crypto/tls/fipsonly is present.

func StandardCrypto()
    StandardCrypto indicates that standard Go crypto is present.

