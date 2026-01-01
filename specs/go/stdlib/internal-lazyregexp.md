package lazyregexp // import "internal/lazyregexp"

Package lazyregexp is a thin wrapper over regexp, allowing the use of global
regexp variables without forcing them to be compiled at init.

TYPES

type Regexp struct {
	// Has unexported fields.
}
    Regexp is a wrapper around regexp.Regexp, where the underlying regexp will
    be compiled the first time it is needed.

func New(str string) *Regexp
    New creates a new lazy regexp, delaying the compiling work until it is first
    needed. If the code is being run as part of tests, the regexp compiling will
    happen immediately.

func (r *Regexp) FindAllString(s string, n int) []string

func (r *Regexp) FindString(s string) string

func (r *Regexp) FindStringSubmatch(s string) []string

func (r *Regexp) FindStringSubmatchIndex(s string) []int

func (r *Regexp) FindSubmatch(s []byte) [][]byte

func (r *Regexp) MatchString(s string) bool

func (r *Regexp) ReplaceAllString(src, repl string) string

func (r *Regexp) SubexpNames() []string

