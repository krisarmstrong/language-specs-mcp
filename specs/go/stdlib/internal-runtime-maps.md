package maps // import "internal/runtime/maps"

Package maps implements Go's builtin map type.

Package maps implements Go's builtin map type.

Package maps implements Go's builtin map type.

FUNCTIONS

func OldMapKeyError(t *abi.OldMapType, p unsafe.Pointer) error

TYPES

type Iter struct {
	// Has unexported fields.
}

func (it *Iter) Elem() unsafe.Pointer
    Key returns a pointer to the current element. nil indicates end of
    iteration.

    Must not be called prior to Next.

func (it *Iter) Init(typ *abi.SwissMapType, m *Map)
    Init initializes Iter for iteration.

func (it *Iter) Initialized() bool

func (it *Iter) Key() unsafe.Pointer
    Key returns a pointer to the current key. nil indicates end of iteration.

    Must not be called prior to Next.

func (it *Iter) Map() *Map
    Map returns the map this iterator is iterating over.

func (it *Iter) Next()
    Next proceeds to the next element in iteration, which can be accessed via
    the Key and Elem methods.

    The table can be mutated during iteration, though there is no guarantee that
    the mutations will be visible to the iteration.

    Init must be called prior to Next.

type Map struct {
	// Has unexported fields.
}
    Note: changes here must be reflected in
    cmd/compile/internal/reflectdata/map_swiss.go:SwissMapType.

func NewEmptyMap() *Map

func NewMap(mt *abi.SwissMapType, hint uintptr, m *Map, maxAlloc uintptr) *Map
    If m is non-nil, it should be used rather than allocating.

    maxAlloc should be runtime.maxAlloc.

    TODO(prattmic): Put maxAlloc somewhere accessible.

func (m *Map) Clear(typ *abi.SwissMapType)
    Clear deletes all entries from the map resulting in an empty map.

func (m *Map) Clone(typ *abi.SwissMapType) *Map

func (m *Map) Delete(typ *abi.SwissMapType, key unsafe.Pointer)

func (m *Map) Get(typ *abi.SwissMapType, key unsafe.Pointer) (unsafe.Pointer, bool)
    Get performs a lookup of the key that key points to. It returns a pointer to
    the element, or false if the key doesn't exist.

func (m *Map) Put(typ *abi.SwissMapType, key, elem unsafe.Pointer)

func (m *Map) PutSlot(typ *abi.SwissMapType, key unsafe.Pointer) unsafe.Pointer
    PutSlot returns a pointer to the element slot where an inserted element
    should be written.

    PutSlot never returns nil.

func (m *Map) Used() uint64

