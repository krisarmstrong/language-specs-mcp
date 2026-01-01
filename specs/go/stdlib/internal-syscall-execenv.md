package execenv // import "internal/syscall/execenv"


FUNCTIONS

func Default(sys *syscall.SysProcAttr) ([]string, error)
    Default will return the default environment variables based on the process
    attributes provided.

    Defaults to syscall.Environ() on all platforms other than Windows.

