package sysrand // import "crypto/internal/sysrand"

Package rand provides cryptographically secure random bytes from the operating
system.

FUNCTIONS

func Read(b []byte)
    Read fills b with cryptographically secure random bytes from the operating
    system. It always fills b entirely and crashes the program irrecoverably if
    an error is encountered. The operating system APIs are documented to never
    return an error on all but legacy Linux systems.

