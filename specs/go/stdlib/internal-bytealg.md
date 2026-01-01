package bytealg // import "internal/bytealg"


CONSTANTS

const MaxBruteForce = 16
    Empirical data shows that using Index can get better performance when len(s)
    <= 16.

const PrimeRK = 16777619
    PrimeRK is the prime base used in Rabin-Karp algorithm.


VARIABLES

var MaxLen int
    MaxLen is the maximum length of the string to be searched for (argument b)
    in Index. If MaxLen is not 0, make sure MaxLen >= 4.


FUNCTIONS

func Compare(a, b []byte) int
func CompareString(a, b string) int
func Count(b []byte, c byte) int
func CountString(s string, c byte) int
func Cutover(n int) int
    Cutover reports the number of failures of IndexByte we should tolerate
    before switching over to Index. n is the number of bytes processed so far.
    See the bytes.Index implementation for details.

func Equal(a, b []byte) bool
    Equal reports whether a and b are the same length and contain the same
    bytes. A nil argument is equivalent to an empty slice.

    Equal is equivalent to bytes.Equal. It is provided here for convenience,
    because some packages cannot depend on bytes.

func HashStr[T string | []byte](sep T) (uint32, uint32)
    HashStr returns the hash and the appropriate multiplicative factor for use
    in Rabin-Karp algorithm.

func HashStrRev[T string | []byte](sep T) (uint32, uint32)
    HashStrRev returns the hash of the reverse of sep and the appropriate
    multiplicative factor for use in Rabin-Karp algorithm.

func Index(a, b []byte) int
    Index returns the index of the first instance of b in a, or -1 if b is not
    present in a. Requires 2 <= len(b) <= MaxLen.

func IndexByte(b []byte, c byte) int
func IndexByteString(s string, c byte) int
func IndexRabinKarp[T string | []byte](s, sep T) int
    IndexRabinKarp uses the Rabin-Karp search algorithm to return the index of
    the first occurrence of sep in s, or -1 if not present.

func IndexString(a, b string) int
    IndexString returns the index of the first instance of b in a, or -1 if b is
    not present in a. Requires 2 <= len(b) <= MaxLen.

func LastIndexByte(s []byte, c byte) int
func LastIndexByteString(s string, c byte) int
func LastIndexRabinKarp[T string | []byte](s, sep T) int
    LastIndexRabinKarp uses the Rabin-Karp search algorithm to return the last
    index of the occurrence of sep in s, or -1 if not present.

func MakeNoZero(n int) []byte
    MakeNoZero makes a slice of length n and capacity of at least n Bytes
    without zeroing the bytes (including the bytes between len and cap).
    It is the caller's responsibility to ensure uninitialized bytes do not leak
    to the end user.

