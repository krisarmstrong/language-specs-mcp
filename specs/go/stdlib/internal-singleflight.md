package singleflight // import "internal/singleflight"

Package singleflight provides a duplicate function call suppression mechanism.

TYPES

type Group struct {
	// Has unexported fields.
}
    Group represents a class of work and forms a namespace in which units of
    work can be executed with duplicate suppression.

func (g *Group) Do(key string, fn func() (any, error)) (v any, err error, shared bool)
    Do executes and returns the results of the given function, making sure that
    only one execution is in-flight for a given key at a time. If a duplicate
    comes in, the duplicate caller waits for the original to complete and
    receives the same results. The return value shared indicates whether v was
    given to multiple callers.

func (g *Group) DoChan(key string, fn func() (any, error)) <-chan Result
    DoChan is like Do but returns a channel that will receive the results when
    they are ready.

func (g *Group) ForgetUnshared(key string) bool
    ForgetUnshared tells the singleflight to forget about a key if it is not
    shared with any other goroutines. Future calls to Do for a forgotten key
    will call the function rather than waiting for an earlier call to complete.
    Returns whether the key was forgotten or unknown--that is, whether no other
    goroutines are waiting for the result.

type Result struct {
	Val    any
	Err    error
	Shared bool
}
    Result holds the results of Do, so they can be passed on a channel.

