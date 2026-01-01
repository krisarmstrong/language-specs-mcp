package byteorder // import "crypto/internal/fips140deps/byteorder"


FUNCTIONS

func BEAppendUint16(b []byte, v uint16) []byte
func BEAppendUint32(b []byte, v uint32) []byte
func BEAppendUint64(b []byte, v uint64) []byte
func BEPutUint16(b []byte, v uint16)
func BEPutUint32(b []byte, v uint32)
func BEPutUint64(b []byte, v uint64)
func BEUint32(b []byte) uint32
func BEUint64(b []byte) uint64
func LEPutUint64(b []byte, v uint64)
func LEUint16(b []byte) uint16
func LEUint64(b []byte) uint64
