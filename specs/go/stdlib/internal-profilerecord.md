package profilerecord // import "internal/profilerecord"

Package profilerecord holds internal types used to represent profiling records
with deep stack traces.

TODO: Consider moving this to internal/runtime, see golang.org/issue/65355.

TYPES

type BlockProfileRecord struct {
	Count  int64
	Cycles int64
	Stack  []uintptr
}

type MemProfileRecord struct {
	AllocBytes, FreeBytes     int64
	AllocObjects, FreeObjects int64
	Stack                     []uintptr
}

func (r *MemProfileRecord) InUseBytes() int64

func (r *MemProfileRecord) InUseObjects() int64

type StackRecord struct {
	Stack []uintptr
}

