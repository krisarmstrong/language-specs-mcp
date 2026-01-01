package race // import "internal/race"

Package race contains helper functions for manually instrumenting code for the
race detector.

The runtime package intentionally exports these functions only in the race
build; this package exports them unconditionally but without the "race" build
tag they are no-ops.

CONSTANTS

const Enabled = false

FUNCTIONS

func Acquire(addr unsafe.Pointer)
func Disable()
func Enable()
func Errors() int
func Read(addr unsafe.Pointer)
func ReadObjectPC(t *abi.Type, addr unsafe.Pointer, callerpc, pc uintptr)
func ReadPC(addr unsafe.Pointer, callerpc, pc uintptr)
func ReadRange(addr unsafe.Pointer, len int)
func Release(addr unsafe.Pointer)
func ReleaseMerge(addr unsafe.Pointer)
func Write(addr unsafe.Pointer)
func WriteObjectPC(t *abi.Type, addr unsafe.Pointer, callerpc, pc uintptr)
func WritePC(addr unsafe.Pointer, callerpc, pc uintptr)
func WriteRange(addr unsafe.Pointer, len int)
