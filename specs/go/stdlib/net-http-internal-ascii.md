package ascii // import "net/http/internal/ascii"


FUNCTIONS

func EqualFold(s, t string) bool
    EqualFold is strings.EqualFold, ASCII only. It reports whether s and t are
    equal, ASCII-case-insensitively.

func Is(s string) bool
    Is returns whether s is ASCII.

func IsPrint(s string) bool
    IsPrint returns whether s is ASCII and printable according to
    https://tools.ietf.org/html/rfc20#section-4.2.

func ToLower(s string) (lower string, ok bool)
    ToLower returns the lowercase version of s if s is ASCII and printable.

