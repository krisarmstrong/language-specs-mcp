package msan // import "internal/msan"

Package msan contains helper functions for manually instrumenting code for the
memory sanitizer. This package exports the private msan routines in runtime
unconditionally but without the "msan" build tag they are no-ops.

CONSTANTS

const Enabled = false

FUNCTIONS

func Free(addr unsafe.Pointer, sz uintptr)
func Malloc(addr unsafe.Pointer, sz uintptr)
func Move(dst, src unsafe.Pointer, sz uintptr)
func Read(addr unsafe.Pointer, sz uintptr)
func Write(addr unsafe.Pointer, sz uintptr)
