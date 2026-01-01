package macOS // import "crypto/x509/internal/macos"

Package macOS provides cgo-less wrappers for Core Foundation and
Security.framework, similarly to how package syscall provides access to
libSystem.dylib.

CONSTANTS

const (
	// various macOS error codes that can be returned from
	// SecTrustEvaluateWithError that we can map to Go cert
	// verification error types.
	ErrSecCertificateExpired = -67818
	ErrSecHostNameMismatch   = -67602
	ErrSecNotTrusted         = -67843
)

FUNCTIONS

func CFArrayAppendValue(array CFRef, val CFRef)
func CFArrayGetCount(array CFRef) int
func CFDataGetBytePtr(data CFRef) uintptr
func CFDataGetLength(data CFRef) int
func CFDataToSlice(data CFRef) []byte
    CFDataToSlice returns a copy of the contents of data as a bytes slice.

func CFEqual(a, b CFRef) bool
func CFErrorGetCode(errRef CFRef) int
func CFNumberGetValue(num CFRef) (int32, error)
func CFRelease(ref CFRef)
func CFStringToString(ref CFRef) string
    CFStringToString returns a Go string representation of the passed in
    CFString, or an empty string if it's invalid.

func ReleaseCFArray(array CFRef)
    ReleaseCFArray iterates through an array, releasing its contents, and then
    releases the array itself. This is necessary because we cannot, easily,
    set the CFArrayCallBacks argument when creating CFArrays.

func SecCertificateCopyData(cert CFRef) ([]byte, error)
func SecTrustEvaluateWithError(trustObj CFRef) (int, error)
func SecTrustSetVerifyDate(trustObj CFRef, dateRef CFRef) error

TYPES

type CFRef uintptr
    CFRef is an opaque reference to a Core Foundation object. It is a pointer,
    but to memory not owned by Go, so not an unsafe.Pointer.

func BytesToCFData(b []byte) CFRef

func CFArrayCreateMutable() CFRef

func CFArrayGetValueAtIndex(array CFRef, index int) CFRef

func CFDateCreate(seconds float64) CFRef

func CFDictionaryGetValueIfPresent(dict CFRef, key CFString) (value CFRef, ok bool)

func CFErrorCopyDescription(errRef CFRef) CFRef

func CFStringCreateExternalRepresentation(strRef CFRef) (CFRef, error)

func SecCertificateCreateWithData(b []byte) (CFRef, error)

func SecPolicyCreateSSL(name string) (CFRef, error)

func SecTrustCopyCertificateChain(trustObj CFRef) (CFRef, error)

func SecTrustCreateWithCertificates(certs CFRef, policies CFRef) (CFRef, error)

func SecTrustEvaluate(trustObj CFRef) (CFRef, error)

func TimeToCFDateRef(t time.Time) CFRef
    TimeToCFDateRef converts a time.Time into an apple CFDateRef.

type CFString CFRef

func StringToCFString(s string) CFString
    StringToCFString returns a copy of the UTF-8 contents of s as a new
    CFString.

type OSStatus struct {
	// Has unexported fields.
}

func (s OSStatus) Error() string

