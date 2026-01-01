package fips140only // import "crypto/internal/fips140only"


VARIABLES

var Enabled = godebug.New("fips140").Value() == "only"
    Enabled reports whether FIPS 140-only mode is enabled, in which non-approved
    cryptography returns an error or panics.


FUNCTIONS

func ApprovedHash(h hash.Hash) bool
func ApprovedRandomReader(r io.Reader) bool
