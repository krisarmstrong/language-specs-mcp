package testpty // import "internal/testpty"

Package testpty is a simple pseudo-terminal package for Unix systems,
implemented by calling C functions via cgo.

VARIABLES

var ErrNotSupported = errors.New("testpty.Open not implemented on this platform")

FUNCTIONS

func Open() (pty *os.File, processTTY string, err error)
    Open returns a control pty and the name of the linked process tty.

    If Open is not implemented on this platform, it returns ErrNotSupported.


TYPES

type PtyError struct {
	FuncName    string
	ErrorString string
	Errno       error
}

func (e *PtyError) Error() string

func (e *PtyError) Unwrap() error

