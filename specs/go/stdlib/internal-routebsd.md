package routebsd // import "internal/routebsd"

Package routebsd supports reading interface addresses on BSD systems. This is
a very stripped down version of x/net/route, for use by the net package in the
standard library.

TYPES

type Addr interface {
	// Family returns an address family.
	Family() int
}
    An Addr represents an address associated with packet routing.

type InetAddr struct {
	IP netip.Addr
}
    An InetAddr represent an internet address using IPv4 or IPv6.

func (a *InetAddr) Family() int

type InterfaceAddrMessage struct {
	Version int    // message version
	Type    int    // message type
	Flags   int    // interface flags
	Index   int    // interface index
	Addrs   []Addr // addresses

	// Has unexported fields.
}
    An InterfaceAddrMessage represents an interface address message.

type InterfaceMessage struct {
	Version int    // message version
	Type    int    // message type
	Flags   int    // interface flags
	Index   int    // interface index
	Name    string // interface name
	Addrs   []Addr // addresses

	// Has unexported fields.
}
    An InterfaceMessage represents an interface message.

func (m *InterfaceMessage) MTU() int
    MTU returns the interface MTU.

type InterfaceMulticastAddrMessage struct {
	Version int    // message version
	Type    int    // message type
	Flags   int    // interface flags
	Index   int    // interface index
	Addrs   []Addr // addresses

	// Has unexported fields.
}
    An InterfaceMulticastAddrMessage represents an interface multicast address
    message.

type LinkAddr struct {
	Index int    // interface index when attached
	Name  string // interface name when attached
	Addr  []byte // link-layer address when attached
}
    A LinkAddr represents a link-layer address.

func (a *LinkAddr) Family() int
    Family implements the Family method of Addr interface.

type Message interface {
	// Has unexported methods.
}
    A Message represents a routing message.

func FetchRIBMessages(typ, arg int) ([]Message, error)
    FetchRIBMessages fetches a list of addressing messages for an interface.
    The typ argument is something like syscall.NET_RT_IFLIST. The argument is an
    interface index or 0 for all.

