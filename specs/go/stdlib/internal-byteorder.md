package byteorder // import "internal/byteorder"

Package byteorder provides functions for decoding and encoding little and big
endian integer types from/to byte slices.

FUNCTIONS

func BEAppendUint16(b []byte, v uint16) []byte
func BEAppendUint32(b []byte, v uint32) []byte
func BEAppendUint64(b []byte, v uint64) []byte
func BEPutUint16(b []byte, v uint16)
func BEPutUint32(b []byte, v uint32)
func BEPutUint64(b []byte, v uint64)
func BEUint16(b []byte) uint16
func BEUint32(b []byte) uint32
func BEUint64(b []byte) uint64
func LEAppendUint16(b []byte, v uint16) []byte
func LEAppendUint32(b []byte, v uint32) []byte
func LEAppendUint64(b []byte, v uint64) []byte
func LEPutUint16(b []byte, v uint16)
func LEPutUint32(b []byte, v uint32)
func LEPutUint64(b []byte, v uint64)
func LEUint16(b []byte) uint16
func LEUint32(b []byte) uint32
func LEUint64(b []byte) uint64
