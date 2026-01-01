package internal // import "net/http/internal"

Package internal contains HTTP internals shared by net/http and
net/http/httputil.

VARIABLES

var ErrLineTooLong = errors.New("header line too long")

FUNCTIONS

func NewChunkedReader(r io.Reader) io.Reader
    NewChunkedReader returns a new chunkedReader that translates the data read
    from r out of HTTP "chunked" format before returning it. The chunkedReader
    returns io.EOF when the final 0-length chunk is read.

    NewChunkedReader is not needed by normal applications. The http package
    automatically decodes chunking when reading response bodies.

func NewChunkedWriter(w io.Writer) io.WriteCloser
    NewChunkedWriter returns a new chunkedWriter that translates writes into
    HTTP "chunked" format before writing them to w. Closing the returned
    chunkedWriter sends the final 0-length chunk that marks the end of the
    stream but does not send the final CRLF that appears after trailers;
    trailers and the last CRLF must be written separately.

    NewChunkedWriter is not needed by normal applications. The http package
    adds chunking automatically if handlers don't set a Content-Length header.
    Using newChunkedWriter inside a handler would result in double chunking or
    chunking with a Content-Length length, both of which are wrong.


TYPES

type FlushAfterChunkWriter struct {
	*bufio.Writer
}
    FlushAfterChunkWriter signals from the caller of NewChunkedWriter that each
    chunk should be followed by a flush. It is used by the net/http.Transport
    code to keep the buffering behavior for headers and trailers, but flush out
    chunks aggressively in the middle for request bodies which may be generated
    slowly. See Issue 6574.

