package zstd // import "internal/zstd"

Package zstd provides a decompressor for zstd streams, described in RFC 8878.
It does not support dictionaries.

TYPES

type Reader struct {
	// Has unexported fields.
}
    Reader implements io.Reader to read a zstd compressed stream.

func NewReader(input io.Reader) *Reader
    NewReader creates a new Reader that decompresses data from the given reader.

func (r *Reader) Read(p []byte) (int, error)
    Read implements io.Reader.

func (r *Reader) ReadByte() (byte, error)
    ReadByte implements io.ByteReader.

func (r *Reader) Reset(input io.Reader)
    Reset discards the current state and starts reading a new stream from r.
    This permits reusing a Reader rather than allocating a new one.

