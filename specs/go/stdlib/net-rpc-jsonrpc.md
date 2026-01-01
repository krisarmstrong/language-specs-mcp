package jsonrpc // import "net/rpc/jsonrpc"

Package jsonrpc implements a JSON-RPC 1.0 ClientCodec and ServerCodec for the
rpc package. For JSON-RPC 2.0 support, see https://godoc.org/?q=json-rpc+2.0

FUNCTIONS

func Dial(network, address string) (*rpc.Client, error)
    Dial connects to a JSON-RPC server at the specified network address.

func NewClient(conn io.ReadWriteCloser) *rpc.Client
    NewClient returns a new rpc.Client to handle requests to the set of services
    at the other end of the connection.

func NewClientCodec(conn io.ReadWriteCloser) rpc.ClientCodec
    NewClientCodec returns a new rpc.ClientCodec using JSON-RPC on conn.

func NewServerCodec(conn io.ReadWriteCloser) rpc.ServerCodec
    NewServerCodec returns a new rpc.ServerCodec using JSON-RPC on conn.

func ServeConn(conn io.ReadWriteCloser)
    ServeConn runs the JSON-RPC server on a single connection. ServeConn blocks,
    serving the connection until the client hangs up. The caller typically
    invokes ServeConn in a go statement.

