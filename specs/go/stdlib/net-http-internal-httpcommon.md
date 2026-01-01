package httpcommon // import "net/http/internal/httpcommon"


VARIABLES

var (
	ErrRequestHeaderListSize = errors.New("request header list larger than peer's advertised limit")
)

FUNCTIONS

func CachedCanonicalHeader(v string) (string, bool)
    CachedCanonicalHeader returns the canonical form of a well-known header
    name.

func CanonicalHeader(v string) string
    CanonicalHeader canonicalizes a header name. (For example, "host" becomes
    "Host".)

func IsRequestGzip(method string, header map[string][]string, disableCompression bool) bool
    IsRequestGzip reports whether we should add an Accept-Encoding: gzip header
    for a request.

func LowerHeader(v string) (lower string, ascii bool)
    LowerHeader returns the lowercase form of a header name, used on the wire
    for HTTP/2 and HTTP/3 requests.


TYPES

type EncodeHeadersParam struct {
	Request Request

	// AddGzipHeader indicates that an "accept-encoding: gzip" header should be
	// added to the request.
	AddGzipHeader bool

	// PeerMaxHeaderListSize, when non-zero, is the peer's MAX_HEADER_LIST_SIZE setting.
	PeerMaxHeaderListSize uint64

	// DefaultUserAgent is the User-Agent header to send when the request
	// neither contains a User-Agent nor disables it.
	DefaultUserAgent string
}
    EncodeHeadersParam is parameters to EncodeHeaders.

type EncodeHeadersResult struct {
	HasBody     bool
	HasTrailers bool
}
    EncodeHeadersParam is the result of EncodeHeaders.

func EncodeHeaders(ctx context.Context, param EncodeHeadersParam, headerf func(name, value string)) (res EncodeHeadersResult, _ error)
    EncodeHeaders constructs request headers common to HTTP/2 and HTTP/3.
    It validates a request and calls headerf with each pseudo-header and
    header for the request. The headerf function is called with the validated,
    canonicalized header name.

type Request struct {
	URL                 *url.URL
	Method              string
	Host                string
	Header              map[string][]string
	Trailer             map[string][]string
	ActualContentLength int64 // 0 means 0, -1 means unknown
}
    Request is a subset of http.Request. It'd be simpler to pass an
    *http.Request, of course, but we can't depend on net/http without creating a
    dependency cycle.

type ServerRequestParam struct {
	Method                  string
	Scheme, Authority, Path string
	Protocol                string
	Header                  map[string][]string
}
    ServerRequestParam is parameters to NewServerRequest.

type ServerRequestResult struct {
	// Various http.Request fields.
	URL        *url.URL
	RequestURI string
	Trailer    map[string][]string

	NeedsContinue bool // client provided an "Expect: 100-continue" header

	// If the request should be rejected, this is a short string suitable for passing
	// to the http2 package's CountError function.
	// It might be a bit odd to return errors this way rather than returing an error,
	// but this ensures we don't forget to include a CountError reason.
	InvalidReason string
}
    ServerRequestResult is the result of NewServerRequest.

func NewServerRequest(rp ServerRequestParam) ServerRequestResult

