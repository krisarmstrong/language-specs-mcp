package strconv // import "internal/runtime/strconv"


FUNCTIONS

func Atoi(s string) (int, bool)
    Atoi is like Atoi64 but for integers that fit into an int.

func Atoi32(s string) (int32, bool)
    Atoi32 is like Atoi but for integers that fit into an int32.

func Atoi64(s string) (int64, bool)
    Atoi64 parses an int64 from a string s. The bool result reports whether s is
    a number representable by a value of type int64.

