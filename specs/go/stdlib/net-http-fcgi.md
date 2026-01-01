package fcgi // import "net/http/fcgi"

Package fcgi implements the FastCGI protocol.

See https://fast-cgi.github.io/ for an unofficial mirror of the original
documentation.

Currently only the responder role is supported.

VARIABLES

var ErrConnClosed = errors.New("fcgi: connection to web server closed")
    ErrConnClosed is returned by Read when a handler attempts to read the body
    of a request after the connection to the web server has been closed.

var ErrRequestAborted = errors.New("fcgi: request aborted by web server")
    ErrRequestAborted is returned by Read when a handler attempts to read the
    body of a request that has been aborted by the web server.


FUNCTIONS

func ProcessEnv(r *http.Request) map[string]string
    ProcessEnv returns FastCGI environment variables associated with the request
    r for which no effort was made to be included in the request itself - the
    data is hidden in the request's context. As an example, if REMOTE_USER
    is set for a request, it will not be found anywhere in r, but it will be
    included in ProcessEnv's response (via r's context).

func Serve(l net.Listener, handler http.Handler) error
    Serve accepts incoming FastCGI connections on the listener l, creating a
    new goroutine for each. The goroutine reads requests and then calls handler
    to reply to them. If l is nil, Serve accepts connections from os.Stdin.
    If handler is nil, http.DefaultServeMux is used.

