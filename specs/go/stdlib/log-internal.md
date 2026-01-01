package internal // import "log/internal"

Package internal contains definitions used by both log and log/slog.

VARIABLES

var DefaultOutput func(pc uintptr, data []byte) error
    DefaultOutput holds a function which calls the default log.Logger's output
    function. It allows slog.defaultHandler to call into an unexported function
    of the log package.

