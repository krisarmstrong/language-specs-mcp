package fips140tls // import "crypto/tls/internal/fips140tls"

Package fips140tls controls whether crypto/tls requires FIPS-approved settings.

FUNCTIONS

func Force()
    Force forces crypto/tls to restrict TLS configurations to FIPS-approved
    settings. By design, this call is impossible to undo (except in tests).

func Required() bool
    Required reports whether FIPS-approved settings are required.

    Required is true if FIPS 140-3 mode is enabled with GODEBUG=fips140=on, or
    if the crypto/tls/fipsonly package is imported by a Go+BoringCrypto build.

func TestingOnlyAbandon()
