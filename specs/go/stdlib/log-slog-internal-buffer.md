package buffer // import "log/slog/internal/buffer"

Package buffer provides a pool-allocated byte buffer.

TYPES

type Buffer []byte
    Buffer is a byte buffer.

    This implementation is adapted from the unexported type buffer in
    go/src/fmt/print.go.

func New() *Buffer

func (b *Buffer) Free()

func (b *Buffer) Len() int

func (b *Buffer) Reset()

func (b *Buffer) SetLen(n int)

func (b *Buffer) String() string

func (b *Buffer) Write(p []byte) (int, error)

func (b *Buffer) WriteByte(c byte) error

func (b *Buffer) WriteString(s string) (int, error)

