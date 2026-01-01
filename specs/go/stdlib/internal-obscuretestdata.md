package obscuretestdata // import "internal/obscuretestdata"

Package obscuretestdata contains functionality used by tests to more easily work
with testdata that must be obscured primarily due to golang.org/issue/34986.

FUNCTIONS

func DecodeToTempFile(name string) (path string, err error)
    DecodeToTempFile decodes the named file to a temporary location.
    If successful, it returns the path of the decoded file. The caller is
    responsible for ensuring that the temporary file is removed.

func ReadFile(name string) ([]byte, error)
    ReadFile reads the named file and returns its decoded contents.

func Rot13(data []byte) []byte
    Rot13 returns the rot13 encoding or decoding of its input.

