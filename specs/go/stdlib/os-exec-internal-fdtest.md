package fdtest // import "os/exec/internal/fdtest"

Package fdtest provides test helpers for working with file descriptors across
exec.

FUNCTIONS

func Exists(fd uintptr) bool
    Exists returns true if fd is a valid file descriptor.

