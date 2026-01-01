package slicereader // import "internal/coverage/slicereader"


TYPES

type Reader struct {
	// Has unexported fields.
}

func NewReader(b []byte, readonly bool) *Reader

func (r *Reader) Offset() int64

func (r *Reader) Read(b []byte) (int, error)

func (r *Reader) ReadString(len int64) string

func (r *Reader) ReadULEB128() (value uint64)

func (r *Reader) ReadUint32() uint32

func (r *Reader) ReadUint64() uint64

func (r *Reader) ReadUint8() uint8

func (r *Reader) Seek(offset int64, whence int) (ret int64, err error)

