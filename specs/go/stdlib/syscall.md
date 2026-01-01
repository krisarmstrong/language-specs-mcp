package syscall // import "syscall"

Package syscall contains an interface to the low-level operating system
primitives. The details vary depending on the underlying system, and by default,
godoc will display the syscall documentation for the current system. If you
want godoc to display syscall documentation for another system, set $GOOS and
$GOARCH to the desired system. For example, if you want to view documentation
for freebsd/arm on linux/amd64, set $GOOS to freebsd and $GOARCH to arm.
The primary use of syscall is inside other packages that provide a more portable
interface to the system, such as "os", "time" and "net". Use those packages
rather than this one if you can. For details of the functions and data types
in this package consult the manuals for the appropriate operating system.
These calls return err == nil to indicate success; otherwise err is an operating
system error describing the failure. On most systems, that error has type Errno.

NOTE: Most of the functions, types, and constants defined in this package are
also available in the golang.org/x/sys package. That package has more system
call support than this one, and most new code should prefer that package where
possible. See https://golang.org/s/go1.4-syscall for more information.

CONSTANTS

const (
	AF_APPLETALK                      = 0x10
	AF_CCITT                          = 0xa
	AF_CHAOS                          = 0x5
	AF_CNT                            = 0x15
	AF_COIP                           = 0x14
	AF_DATAKIT                        = 0x9
	AF_DECnet                         = 0xc
	AF_DLI                            = 0xd
	AF_E164                           = 0x1c
	AF_ECMA                           = 0x8
	AF_HYLINK                         = 0xf
	AF_IEEE80211                      = 0x25
	AF_IMPLINK                        = 0x3
	AF_INET                           = 0x2
	AF_INET6                          = 0x1e
	AF_IPX                            = 0x17
	AF_ISDN                           = 0x1c
	AF_ISO                            = 0x7
	AF_LAT                            = 0xe
	AF_LINK                           = 0x12
	AF_LOCAL                          = 0x1
	AF_MAX                            = 0x28
	AF_NATM                           = 0x1f
	AF_NDRV                           = 0x1b
	AF_NETBIOS                        = 0x21
	AF_NS                             = 0x6
	AF_OSI                            = 0x7
	AF_PPP                            = 0x22
	AF_PUP                            = 0x4
	AF_RESERVED_36                    = 0x24
	AF_ROUTE                          = 0x11
	AF_SIP                            = 0x18
	AF_SNA                            = 0xb
	AF_SYSTEM                         = 0x20
	AF_UNIX                           = 0x1
	AF_UNSPEC                         = 0x0
	AF_UTUN                           = 0x26
	B0                                = 0x0
	B110                              = 0x6e
	B115200                           = 0x1c200
	B1200                             = 0x4b0
	B134                              = 0x86
	B14400                            = 0x3840
	B150                              = 0x96
	B1800                             = 0x708
	B19200                            = 0x4b00
	B200                              = 0xc8
	B230400                           = 0x38400
	B2400                             = 0x960
	B28800                            = 0x7080
	B300                              = 0x12c
	B38400                            = 0x9600
	B4800                             = 0x12c0
	B50                               = 0x32
	B57600                            = 0xe100
	B600                              = 0x258
	B7200                             = 0x1c20
	B75                               = 0x4b
	B76800                            = 0x12c00
	B9600                             = 0x2580
	BIOCFLUSH                         = 0x20004268
	BIOCGBLEN                         = 0x40044266
	BIOCGDLT                          = 0x4004426a
	BIOCGDLTLIST                      = 0xc00c4279
	BIOCGETIF                         = 0x4020426b
	BIOCGHDRCMPLT                     = 0x40044274
	BIOCGRSIG                         = 0x40044272
	BIOCGRTIMEOUT                     = 0x4010426e
	BIOCGSEESENT                      = 0x40044276
	BIOCGSTATS                        = 0x4008426f
	BIOCIMMEDIATE                     = 0x80044270
	BIOCPROMISC                       = 0x20004269
	BIOCSBLEN                         = 0xc0044266
	BIOCSDLT                          = 0x80044278
	BIOCSETF                          = 0x80104267
	BIOCSETIF                         = 0x8020426c
	BIOCSHDRCMPLT                     = 0x80044275
	BIOCSRSIG                         = 0x80044273
	BIOCSRTIMEOUT                     = 0x8010426d
	BIOCSSEESENT                      = 0x80044277
	BIOCVERSION                       = 0x40044271
	BPF_A                             = 0x10
	BPF_ABS                           = 0x20
	BPF_ADD                           = 0x0
	BPF_ALIGNMENT                     = 0x4
	BPF_ALU                           = 0x4
	BPF_AND                           = 0x50
	BPF_B                             = 0x10
	BPF_DIV                           = 0x30
	BPF_H                             = 0x8
	BPF_IMM                           = 0x0
	BPF_IND                           = 0x40
	BPF_JA                            = 0x0
	BPF_JEQ                           = 0x10
	BPF_JGE                           = 0x30
	BPF_JGT                           = 0x20
	BPF_JMP                           = 0x5
	BPF_JSET                          = 0x40
	BPF_K                             = 0x0
	BPF_LD                            = 0x0
	BPF_LDX                           = 0x1
	BPF_LEN                           = 0x80
	BPF_LSH                           = 0x60
	BPF_MAJOR_VERSION                 = 0x1
	BPF_MAXBUFSIZE                    = 0x80000
	BPF_MAXINSNS                      = 0x200
	BPF_MEM                           = 0x60
	BPF_MEMWORDS                      = 0x10
	BPF_MINBUFSIZE                    = 0x20
	BPF_MINOR_VERSION                 = 0x1
	BPF_MISC                          = 0x7
	BPF_MSH                           = 0xa0
	BPF_MUL                           = 0x20
	BPF_NEG                           = 0x80
	BPF_OR                            = 0x40
	BPF_RELEASE                       = 0x30bb6
	BPF_RET                           = 0x6
	BPF_RSH                           = 0x70
	BPF_ST                            = 0x2
	BPF_STX                           = 0x3
	BPF_SUB                           = 0x10
	BPF_TAX                           = 0x0
	BPF_TXA                           = 0x80
	BPF_W                             = 0x0
	BPF_X                             = 0x8
	BRKINT                            = 0x2
	CFLUSH                            = 0xf
	CLOCAL                            = 0x8000
	CREAD                             = 0x800
	CS5                               = 0x0
	CS6                               = 0x100
	CS7                               = 0x200
	CS8                               = 0x300
	CSIZE                             = 0x300
	CSTART                            = 0x11
	CSTATUS                           = 0x14
	CSTOP                             = 0x13
	CSTOPB                            = 0x400
	CSUSP                             = 0x1a
	CTL_MAXNAME                       = 0xc
	CTL_NET                           = 0x4
	DLT_APPLE_IP_OVER_IEEE1394        = 0x8a
	DLT_ARCNET                        = 0x7
	DLT_ATM_CLIP                      = 0x13
	DLT_ATM_RFC1483                   = 0xb
	DLT_AX25                          = 0x3
	DLT_CHAOS                         = 0x5
	DLT_CHDLC                         = 0x68
	DLT_C_HDLC                        = 0x68
	DLT_EN10MB                        = 0x1
	DLT_EN3MB                         = 0x2
	DLT_FDDI                          = 0xa
	DLT_IEEE802                       = 0x6
	DLT_IEEE802_11                    = 0x69
	DLT_IEEE802_11_RADIO              = 0x7f
	DLT_IEEE802_11_RADIO_AVS          = 0xa3
	DLT_LINUX_SLL                     = 0x71
	DLT_LOOP                          = 0x6c
	DLT_NULL                          = 0x0
	DLT_PFLOG                         = 0x75
	DLT_PFSYNC                        = 0x12
	DLT_PPP                           = 0x9
	DLT_PPP_BSDOS                     = 0x10
	DLT_PPP_SERIAL                    = 0x32
	DLT_PRONET                        = 0x4
	DLT_RAW                           = 0xc
	DLT_SLIP                          = 0x8
	DLT_SLIP_BSDOS                    = 0xf
	DT_BLK                            = 0x6
	DT_CHR                            = 0x2
	DT_DIR                            = 0x4
	DT_FIFO                           = 0x1
	DT_LNK                            = 0xa
	DT_REG                            = 0x8
	DT_SOCK                           = 0xc
	DT_UNKNOWN                        = 0x0
	DT_WHT                            = 0xe
	ECHO                              = 0x8
	ECHOCTL                           = 0x40
	ECHOE                             = 0x2
	ECHOK                             = 0x4
	ECHOKE                            = 0x1
	ECHONL                            = 0x10
	ECHOPRT                           = 0x20
	EVFILT_AIO                        = -0x3
	EVFILT_FS                         = -0x9
	EVFILT_MACHPORT                   = -0x8
	EVFILT_PROC                       = -0x5
	EVFILT_READ                       = -0x1
	EVFILT_SIGNAL                     = -0x6
	EVFILT_SYSCOUNT                   = 0xe
	EVFILT_THREADMARKER               = 0xe
	EVFILT_TIMER                      = -0x7
	EVFILT_USER                       = -0xa
	EVFILT_VM                         = -0xc
	EVFILT_VNODE                      = -0x4
	EVFILT_WRITE                      = -0x2
	EV_ADD                            = 0x1
	EV_CLEAR                          = 0x20
	EV_DELETE                         = 0x2
	EV_DISABLE                        = 0x8
	EV_DISPATCH                       = 0x80
	EV_ENABLE                         = 0x4
	EV_EOF                            = 0x8000
	EV_ERROR                          = 0x4000
	EV_FLAG0                          = 0x1000
	EV_FLAG1                          = 0x2000
	EV_ONESHOT                        = 0x10
	EV_OOBAND                         = 0x2000
	EV_POLL                           = 0x1000
	EV_RECEIPT                        = 0x40
	EV_SYSFLAGS                       = 0xf000
	EXTA                              = 0x4b00
	EXTB                              = 0x9600
	EXTPROC                           = 0x800
	FD_CLOEXEC                        = 0x1
	FD_SETSIZE                        = 0x400
	FLUSHO                            = 0x800000
	F_ADDFILESIGS                     = 0x3d
	F_ADDSIGS                         = 0x3b
	F_ALLOCATEALL                     = 0x4
	F_ALLOCATECONTIG                  = 0x2
	F_CHKCLEAN                        = 0x29
	F_DUPFD                           = 0x0
	F_DUPFD_CLOEXEC                   = 0x43
	F_FINDSIGS                        = 0x4e
	F_FLUSH_DATA                      = 0x28
	F_FREEZE_FS                       = 0x35
	F_FULLFSYNC                       = 0x33
	F_GETCODEDIR                      = 0x48
	F_GETFD                           = 0x1
	F_GETFL                           = 0x3
	F_GETLK                           = 0x7
	F_GETLKPID                        = 0x42
	F_GETNOSIGPIPE                    = 0x4a
	F_GETOWN                          = 0x5
	F_GETPATH                         = 0x32
	F_GETPATH_MTMINFO                 = 0x47
	F_GETPROTECTIONCLASS              = 0x3f
	F_GETPROTECTIONLEVEL              = 0x4d
	F_GLOBAL_NOCACHE                  = 0x37
	F_LOG2PHYS                        = 0x31
	F_LOG2PHYS_EXT                    = 0x41
	F_NOCACHE                         = 0x30
	F_NODIRECT                        = 0x3e
	F_OK                              = 0x0
	F_PATHPKG_CHECK                   = 0x34
	F_PEOFPOSMODE                     = 0x3
	F_PREALLOCATE                     = 0x2a
	F_RDADVISE                        = 0x2c
	F_RDAHEAD                         = 0x2d
	F_RDLCK                           = 0x1
	F_SETBACKINGSTORE                 = 0x46
	F_SETFD                           = 0x2
	F_SETFL                           = 0x4
	F_SETLK                           = 0x8
	F_SETLKW                          = 0x9
	F_SETLKWTIMEOUT                   = 0xa
	F_SETNOSIGPIPE                    = 0x49
	F_SETOWN                          = 0x6
	F_SETPROTECTIONCLASS              = 0x40
	F_SETSIZE                         = 0x2b
	F_SINGLE_WRITER                   = 0x4c
	F_THAW_FS                         = 0x36
	F_TRANSCODEKEY                    = 0x4b
	F_UNLCK                           = 0x2
	F_VOLPOSMODE                      = 0x4
	F_WRLCK                           = 0x3
	HUPCL                             = 0x4000
	ICANON                            = 0x100
	ICMP6_FILTER                      = 0x12
	ICRNL                             = 0x100
	IEXTEN                            = 0x400
	IFF_ALLMULTI                      = 0x200
	IFF_ALTPHYS                       = 0x4000
	IFF_BROADCAST                     = 0x2
	IFF_DEBUG                         = 0x4
	IFF_LINK0                         = 0x1000
	IFF_LINK1                         = 0x2000
	IFF_LINK2                         = 0x4000
	IFF_LOOPBACK                      = 0x8
	IFF_MULTICAST                     = 0x8000
	IFF_NOARP                         = 0x80
	IFF_NOTRAILERS                    = 0x20
	IFF_OACTIVE                       = 0x400
	IFF_POINTOPOINT                   = 0x10
	IFF_PROMISC                       = 0x100
	IFF_RUNNING                       = 0x40
	IFF_SIMPLEX                       = 0x800
	IFF_UP                            = 0x1
	IFNAMSIZ                          = 0x10
	IFT_1822                          = 0x2
	IFT_AAL5                          = 0x31
	IFT_ARCNET                        = 0x23
	IFT_ARCNETPLUS                    = 0x24
	IFT_ATM                           = 0x25
	IFT_BRIDGE                        = 0xd1
	IFT_CARP                          = 0xf8
	IFT_CELLULAR                      = 0xff
	IFT_CEPT                          = 0x13
	IFT_DS3                           = 0x1e
	IFT_ENC                           = 0xf4
	IFT_EON                           = 0x19
	IFT_ETHER                         = 0x6
	IFT_FAITH                         = 0x38
	IFT_FDDI                          = 0xf
	IFT_FRELAY                        = 0x20
	IFT_FRELAYDCE                     = 0x2c
	IFT_GIF                           = 0x37
	IFT_HDH1822                       = 0x3
	IFT_HIPPI                         = 0x2f
	IFT_HSSI                          = 0x2e
	IFT_HY                            = 0xe
	IFT_IEEE1394                      = 0x90
	IFT_IEEE8023ADLAG                 = 0x88
	IFT_ISDNBASIC                     = 0x14
	IFT_ISDNPRIMARY                   = 0x15
	IFT_ISO88022LLC                   = 0x29
	IFT_ISO88023                      = 0x7
	IFT_ISO88024                      = 0x8
	IFT_ISO88025                      = 0x9
	IFT_ISO88026                      = 0xa
	IFT_L2VLAN                        = 0x87
	IFT_LAPB                          = 0x10
	IFT_LOCALTALK                     = 0x2a
	IFT_LOOP                          = 0x18
	IFT_MIOX25                        = 0x26
	IFT_MODEM                         = 0x30
	IFT_NSIP                          = 0x1b
	IFT_OTHER                         = 0x1
	IFT_P10                           = 0xc
	IFT_P80                           = 0xd
	IFT_PARA                          = 0x22
	IFT_PDP                           = 0xff
	IFT_PFLOG                         = 0xf5
	IFT_PFSYNC                        = 0xf6
	IFT_PPP                           = 0x17
	IFT_PROPMUX                       = 0x36
	IFT_PROPVIRTUAL                   = 0x35
	IFT_PTPSERIAL                     = 0x16
	IFT_RS232                         = 0x21
	IFT_SDLC                          = 0x11
	IFT_SIP                           = 0x1f
	IFT_SLIP                          = 0x1c
	IFT_SMDSDXI                       = 0x2b
	IFT_SMDSICIP                      = 0x34
	IFT_SONET                         = 0x27
	IFT_SONETPATH                     = 0x32
	IFT_SONETVT                       = 0x33
	IFT_STARLAN                       = 0xb
	IFT_STF                           = 0x39
	IFT_T1                            = 0x12
	IFT_ULTRA                         = 0x1d
	IFT_V35                           = 0x2d
	IFT_X25                           = 0x5
	IFT_X25DDN                        = 0x4
	IFT_X25PLE                        = 0x28
	IFT_XETHER                        = 0x1a
	IGNBRK                            = 0x1
	IGNCR                             = 0x80
	IGNPAR                            = 0x4
	IMAXBEL                           = 0x2000
	INLCR                             = 0x40
	INPCK                             = 0x10
	IN_CLASSA_HOST                    = 0xffffff
	IN_CLASSA_MAX                     = 0x80
	IN_CLASSA_NET                     = 0xff000000
	IN_CLASSA_NSHIFT                  = 0x18
	IN_CLASSB_HOST                    = 0xffff
	IN_CLASSB_MAX                     = 0x10000
	IN_CLASSB_NET                     = 0xffff0000
	IN_CLASSB_NSHIFT                  = 0x10
	IN_CLASSC_HOST                    = 0xff
	IN_CLASSC_NET                     = 0xffffff00
	IN_CLASSC_NSHIFT                  = 0x8
	IN_CLASSD_HOST                    = 0xfffffff
	IN_CLASSD_NET                     = 0xf0000000
	IN_CLASSD_NSHIFT                  = 0x1c
	IN_LINKLOCALNETNUM                = 0xa9fe0000
	IN_LOOPBACKNET                    = 0x7f
	IPPROTO_3PC                       = 0x22
	IPPROTO_ADFS                      = 0x44
	IPPROTO_AH                        = 0x33
	IPPROTO_AHIP                      = 0x3d
	IPPROTO_APES                      = 0x63
	IPPROTO_ARGUS                     = 0xd
	IPPROTO_AX25                      = 0x5d
	IPPROTO_BHA                       = 0x31
	IPPROTO_BLT                       = 0x1e
	IPPROTO_BRSATMON                  = 0x4c
	IPPROTO_CFTP                      = 0x3e
	IPPROTO_CHAOS                     = 0x10
	IPPROTO_CMTP                      = 0x26
	IPPROTO_CPHB                      = 0x49
	IPPROTO_CPNX                      = 0x48
	IPPROTO_DDP                       = 0x25
	IPPROTO_DGP                       = 0x56
	IPPROTO_DIVERT                    = 0xfe
	IPPROTO_DONE                      = 0x101
	IPPROTO_DSTOPTS                   = 0x3c
	IPPROTO_EGP                       = 0x8
	IPPROTO_EMCON                     = 0xe
	IPPROTO_ENCAP                     = 0x62
	IPPROTO_EON                       = 0x50
	IPPROTO_ESP                       = 0x32
	IPPROTO_ETHERIP                   = 0x61
	IPPROTO_FRAGMENT                  = 0x2c
	IPPROTO_GGP                       = 0x3
	IPPROTO_GMTP                      = 0x64
	IPPROTO_GRE                       = 0x2f
	IPPROTO_HELLO                     = 0x3f
	IPPROTO_HMP                       = 0x14
	IPPROTO_HOPOPTS                   = 0x0
	IPPROTO_ICMP                      = 0x1
	IPPROTO_ICMPV6                    = 0x3a
	IPPROTO_IDP                       = 0x16
	IPPROTO_IDPR                      = 0x23
	IPPROTO_IDRP                      = 0x2d
	IPPROTO_IGMP                      = 0x2
	IPPROTO_IGP                       = 0x55
	IPPROTO_IGRP                      = 0x58
	IPPROTO_IL                        = 0x28
	IPPROTO_INLSP                     = 0x34
	IPPROTO_INP                       = 0x20
	IPPROTO_IP                        = 0x0
	IPPROTO_IPCOMP                    = 0x6c
	IPPROTO_IPCV                      = 0x47
	IPPROTO_IPEIP                     = 0x5e
	IPPROTO_IPIP                      = 0x4
	IPPROTO_IPPC                      = 0x43
	IPPROTO_IPV4                      = 0x4
	IPPROTO_IPV6                      = 0x29
	IPPROTO_IRTP                      = 0x1c
	IPPROTO_KRYPTOLAN                 = 0x41
	IPPROTO_LARP                      = 0x5b
	IPPROTO_LEAF1                     = 0x19
	IPPROTO_LEAF2                     = 0x1a
	IPPROTO_MAX                       = 0x100
	IPPROTO_MAXID                     = 0x34
	IPPROTO_MEAS                      = 0x13
	IPPROTO_MHRP                      = 0x30
	IPPROTO_MICP                      = 0x5f
	IPPROTO_MTP                       = 0x5c
	IPPROTO_MUX                       = 0x12
	IPPROTO_ND                        = 0x4d
	IPPROTO_NHRP                      = 0x36
	IPPROTO_NONE                      = 0x3b
	IPPROTO_NSP                       = 0x1f
	IPPROTO_NVPII                     = 0xb
	IPPROTO_OSPFIGP                   = 0x59
	IPPROTO_PGM                       = 0x71
	IPPROTO_PIGP                      = 0x9
	IPPROTO_PIM                       = 0x67
	IPPROTO_PRM                       = 0x15
	IPPROTO_PUP                       = 0xc
	IPPROTO_PVP                       = 0x4b
	IPPROTO_RAW                       = 0xff
	IPPROTO_RCCMON                    = 0xa
	IPPROTO_RDP                       = 0x1b
	IPPROTO_ROUTING                   = 0x2b
	IPPROTO_RSVP                      = 0x2e
	IPPROTO_RVD                       = 0x42
	IPPROTO_SATEXPAK                  = 0x40
	IPPROTO_SATMON                    = 0x45
	IPPROTO_SCCSP                     = 0x60
	IPPROTO_SCTP                      = 0x84
	IPPROTO_SDRP                      = 0x2a
	IPPROTO_SEP                       = 0x21
	IPPROTO_SRPC                      = 0x5a
	IPPROTO_ST                        = 0x7
	IPPROTO_SVMTP                     = 0x52
	IPPROTO_SWIPE                     = 0x35
	IPPROTO_TCF                       = 0x57
	IPPROTO_TCP                       = 0x6
	IPPROTO_TP                        = 0x1d
	IPPROTO_TPXX                      = 0x27
	IPPROTO_TRUNK1                    = 0x17
	IPPROTO_TRUNK2                    = 0x18
	IPPROTO_TTP                       = 0x54
	IPPROTO_UDP                       = 0x11
	IPPROTO_VINES                     = 0x53
	IPPROTO_VISA                      = 0x46
	IPPROTO_VMTP                      = 0x51
	IPPROTO_WBEXPAK                   = 0x4f
	IPPROTO_WBMON                     = 0x4e
	IPPROTO_WSN                       = 0x4a
	IPPROTO_XNET                      = 0xf
	IPPROTO_XTP                       = 0x24
	IPV6_2292DSTOPTS                  = 0x17
	IPV6_2292HOPLIMIT                 = 0x14
	IPV6_2292HOPOPTS                  = 0x16
	IPV6_2292NEXTHOP                  = 0x15
	IPV6_2292PKTINFO                  = 0x13
	IPV6_2292PKTOPTIONS               = 0x19
	IPV6_2292RTHDR                    = 0x18
	IPV6_BINDV6ONLY                   = 0x1b
	IPV6_BOUND_IF                     = 0x7d
	IPV6_CHECKSUM                     = 0x1a
	IPV6_DEFAULT_MULTICAST_HOPS       = 0x1
	IPV6_DEFAULT_MULTICAST_LOOP       = 0x1
	IPV6_DEFHLIM                      = 0x40
	IPV6_FAITH                        = 0x1d
	IPV6_FLOWINFO_MASK                = 0xffffff0f
	IPV6_FLOWLABEL_MASK               = 0xffff0f00
	IPV6_FRAGTTL                      = 0x78
	IPV6_FW_ADD                       = 0x1e
	IPV6_FW_DEL                       = 0x1f
	IPV6_FW_FLUSH                     = 0x20
	IPV6_FW_GET                       = 0x22
	IPV6_FW_ZERO                      = 0x21
	IPV6_HLIMDEC                      = 0x1
	IPV6_IPSEC_POLICY                 = 0x1c
	IPV6_JOIN_GROUP                   = 0xc
	IPV6_LEAVE_GROUP                  = 0xd
	IPV6_MAXHLIM                      = 0xff
	IPV6_MAXOPTHDR                    = 0x800
	IPV6_MAXPACKET                    = 0xffff
	IPV6_MAX_GROUP_SRC_FILTER         = 0x200
	IPV6_MAX_MEMBERSHIPS              = 0xfff
	IPV6_MAX_SOCK_SRC_FILTER          = 0x80
	IPV6_MIN_MEMBERSHIPS              = 0x1f
	IPV6_MMTU                         = 0x500
	IPV6_MULTICAST_HOPS               = 0xa
	IPV6_MULTICAST_IF                 = 0x9
	IPV6_MULTICAST_LOOP               = 0xb
	IPV6_PORTRANGE                    = 0xe
	IPV6_PORTRANGE_DEFAULT            = 0x0
	IPV6_PORTRANGE_HIGH               = 0x1
	IPV6_PORTRANGE_LOW                = 0x2
	IPV6_RECVTCLASS                   = 0x23
	IPV6_RTHDR_LOOSE                  = 0x0
	IPV6_RTHDR_STRICT                 = 0x1
	IPV6_RTHDR_TYPE_0                 = 0x0
	IPV6_SOCKOPT_RESERVED1            = 0x3
	IPV6_TCLASS                       = 0x24
	IPV6_UNICAST_HOPS                 = 0x4
	IPV6_V6ONLY                       = 0x1b
	IPV6_VERSION                      = 0x60
	IPV6_VERSION_MASK                 = 0xf0
	IP_ADD_MEMBERSHIP                 = 0xc
	IP_ADD_SOURCE_MEMBERSHIP          = 0x46
	IP_BLOCK_SOURCE                   = 0x48
	IP_BOUND_IF                       = 0x19
	IP_DEFAULT_MULTICAST_LOOP         = 0x1
	IP_DEFAULT_MULTICAST_TTL          = 0x1
	IP_DF                             = 0x4000
	IP_DROP_MEMBERSHIP                = 0xd
	IP_DROP_SOURCE_MEMBERSHIP         = 0x47
	IP_DUMMYNET_CONFIGURE             = 0x3c
	IP_DUMMYNET_DEL                   = 0x3d
	IP_DUMMYNET_FLUSH                 = 0x3e
	IP_DUMMYNET_GET                   = 0x40
	IP_FAITH                          = 0x16
	IP_FW_ADD                         = 0x28
	IP_FW_DEL                         = 0x29
	IP_FW_FLUSH                       = 0x2a
	IP_FW_GET                         = 0x2c
	IP_FW_RESETLOG                    = 0x2d
	IP_FW_ZERO                        = 0x2b
	IP_HDRINCL                        = 0x2
	IP_IPSEC_POLICY                   = 0x15
	IP_MAXPACKET                      = 0xffff
	IP_MAX_GROUP_SRC_FILTER           = 0x200
	IP_MAX_MEMBERSHIPS                = 0xfff
	IP_MAX_SOCK_MUTE_FILTER           = 0x80
	IP_MAX_SOCK_SRC_FILTER            = 0x80
	IP_MF                             = 0x2000
	IP_MIN_MEMBERSHIPS                = 0x1f
	IP_MSFILTER                       = 0x4a
	IP_MSS                            = 0x240
	IP_MULTICAST_IF                   = 0x9
	IP_MULTICAST_IFINDEX              = 0x42
	IP_MULTICAST_LOOP                 = 0xb
	IP_MULTICAST_TTL                  = 0xa
	IP_MULTICAST_VIF                  = 0xe
	IP_NAT__XXX                       = 0x37
	IP_OFFMASK                        = 0x1fff
	IP_OLD_FW_ADD                     = 0x32
	IP_OLD_FW_DEL                     = 0x33
	IP_OLD_FW_FLUSH                   = 0x34
	IP_OLD_FW_GET                     = 0x36
	IP_OLD_FW_RESETLOG                = 0x38
	IP_OLD_FW_ZERO                    = 0x35
	IP_OPTIONS                        = 0x1
	IP_PKTINFO                        = 0x1a
	IP_PORTRANGE                      = 0x13
	IP_PORTRANGE_DEFAULT              = 0x0
	IP_PORTRANGE_HIGH                 = 0x1
	IP_PORTRANGE_LOW                  = 0x2
	IP_RECVDSTADDR                    = 0x7
	IP_RECVIF                         = 0x14
	IP_RECVOPTS                       = 0x5
	IP_RECVPKTINFO                    = 0x1a
	IP_RECVRETOPTS                    = 0x6
	IP_RECVTTL                        = 0x18
	IP_RETOPTS                        = 0x8
	IP_RF                             = 0x8000
	IP_RSVP_OFF                       = 0x10
	IP_RSVP_ON                        = 0xf
	IP_RSVP_VIF_OFF                   = 0x12
	IP_RSVP_VIF_ON                    = 0x11
	IP_STRIPHDR                       = 0x17
	IP_TOS                            = 0x3
	IP_TRAFFIC_MGT_BACKGROUND         = 0x41
	IP_TTL                            = 0x4
	IP_UNBLOCK_SOURCE                 = 0x49
	ISIG                              = 0x80
	ISTRIP                            = 0x20
	IUTF8                             = 0x4000
	IXANY                             = 0x800
	IXOFF                             = 0x400
	IXON                              = 0x200
	LOCK_EX                           = 0x2
	LOCK_NB                           = 0x4
	LOCK_SH                           = 0x1
	LOCK_UN                           = 0x8
	MADV_CAN_REUSE                    = 0x9
	MADV_DONTNEED                     = 0x4
	MADV_FREE                         = 0x5
	MADV_FREE_REUSABLE                = 0x7
	MADV_FREE_REUSE                   = 0x8
	MADV_NORMAL                       = 0x0
	MADV_RANDOM                       = 0x1
	MADV_SEQUENTIAL                   = 0x2
	MADV_WILLNEED                     = 0x3
	MADV_ZERO_WIRED_PAGES             = 0x6
	MAP_ANON                          = 0x1000
	MAP_COPY                          = 0x2
	MAP_FILE                          = 0x0
	MAP_FIXED                         = 0x10
	MAP_HASSEMAPHORE                  = 0x200
	MAP_JIT                           = 0x800
	MAP_NOCACHE                       = 0x400
	MAP_NOEXTEND                      = 0x100
	MAP_NORESERVE                     = 0x40
	MAP_PRIVATE                       = 0x2
	MAP_RENAME                        = 0x20
	MAP_RESERVED0080                  = 0x80
	MAP_SHARED                        = 0x1
	MCL_CURRENT                       = 0x1
	MCL_FUTURE                        = 0x2
	MSG_CTRUNC                        = 0x20
	MSG_DONTROUTE                     = 0x4
	MSG_DONTWAIT                      = 0x80
	MSG_EOF                           = 0x100
	MSG_EOR                           = 0x8
	MSG_FLUSH                         = 0x400
	MSG_HAVEMORE                      = 0x2000
	MSG_HOLD                          = 0x800
	MSG_NEEDSA                        = 0x10000
	MSG_OOB                           = 0x1
	MSG_PEEK                          = 0x2
	MSG_RCVMORE                       = 0x4000
	MSG_SEND                          = 0x1000
	MSG_TRUNC                         = 0x10
	MSG_WAITALL                       = 0x40
	MSG_WAITSTREAM                    = 0x200
	MS_ASYNC                          = 0x1
	MS_DEACTIVATE                     = 0x8
	MS_INVALIDATE                     = 0x2
	MS_KILLPAGES                      = 0x4
	MS_SYNC                           = 0x10
	NAME_MAX                          = 0xff
	NET_RT_DUMP                       = 0x1
	NET_RT_DUMP2                      = 0x7
	NET_RT_FLAGS                      = 0x2
	NET_RT_IFLIST                     = 0x3
	NET_RT_IFLIST2                    = 0x6
	NET_RT_MAXID                      = 0xa
	NET_RT_STAT                       = 0x4
	NET_RT_TRASH                      = 0x5
	NOFLSH                            = 0x80000000
	NOTE_ABSOLUTE                     = 0x8
	NOTE_ATTRIB                       = 0x8
	NOTE_BACKGROUND                   = 0x40
	NOTE_CHILD                        = 0x4
	NOTE_CRITICAL                     = 0x20
	NOTE_DELETE                       = 0x1
	NOTE_EXEC                         = 0x20000000
	NOTE_EXIT                         = 0x80000000
	NOTE_EXITSTATUS                   = 0x4000000
	NOTE_EXIT_CSERROR                 = 0x40000
	NOTE_EXIT_DECRYPTFAIL             = 0x10000
	NOTE_EXIT_DETAIL                  = 0x2000000
	NOTE_EXIT_DETAIL_MASK             = 0x70000
	NOTE_EXIT_MEMORY                  = 0x20000
	NOTE_EXIT_REPARENTED              = 0x80000
	NOTE_EXTEND                       = 0x4
	NOTE_FFAND                        = 0x40000000
	NOTE_FFCOPY                       = 0xc0000000
	NOTE_FFCTRLMASK                   = 0xc0000000
	NOTE_FFLAGSMASK                   = 0xffffff
	NOTE_FFNOP                        = 0x0
	NOTE_FFOR                         = 0x80000000
	NOTE_FORK                         = 0x40000000
	NOTE_LEEWAY                       = 0x10
	NOTE_LINK                         = 0x10
	NOTE_LOWAT                        = 0x1
	NOTE_NONE                         = 0x80
	NOTE_NSECONDS                     = 0x4
	NOTE_PCTRLMASK                    = -0x100000
	NOTE_PDATAMASK                    = 0xfffff
	NOTE_REAP                         = 0x10000000
	NOTE_RENAME                       = 0x20
	NOTE_REVOKE                       = 0x40
	NOTE_SECONDS                      = 0x1
	NOTE_SIGNAL                       = 0x8000000
	NOTE_TRACK                        = 0x1
	NOTE_TRACKERR                     = 0x2
	NOTE_TRIGGER                      = 0x1000000
	NOTE_USECONDS                     = 0x2
	NOTE_VM_ERROR                     = 0x10000000
	NOTE_VM_PRESSURE                  = 0x80000000
	NOTE_VM_PRESSURE_SUDDEN_TERMINATE = 0x20000000
	NOTE_VM_PRESSURE_TERMINATE        = 0x40000000
	NOTE_WRITE                        = 0x2
	OCRNL                             = 0x10
	OFDEL                             = 0x20000
	OFILL                             = 0x80
	ONLCR                             = 0x2
	ONLRET                            = 0x40
	ONOCR                             = 0x20
	ONOEOT                            = 0x8
	OPOST                             = 0x1
	O_ACCMODE                         = 0x3
	O_ALERT                           = 0x20000000
	O_APPEND                          = 0x8
	O_ASYNC                           = 0x40
	O_CLOEXEC                         = 0x1000000
	O_CREAT                           = 0x200
	O_DIRECTORY                       = 0x100000
	O_DP_GETRAWENCRYPTED              = 0x1
	O_DSYNC                           = 0x400000
	O_EVTONLY                         = 0x8000
	O_EXCL                            = 0x800
	O_EXLOCK                          = 0x20
	O_FSYNC                           = 0x80
	O_NDELAY                          = 0x4
	O_NOCTTY                          = 0x20000
	O_NOFOLLOW                        = 0x100
	O_NONBLOCK                        = 0x4
	O_POPUP                           = 0x80000000
	O_RDONLY                          = 0x0
	O_RDWR                            = 0x2
	O_SHLOCK                          = 0x10
	O_SYMLINK                         = 0x200000
	O_SYNC                            = 0x80
	O_TRUNC                           = 0x400
	O_WRONLY                          = 0x1
	PARENB                            = 0x1000
	PARMRK                            = 0x8
	PARODD                            = 0x2000
	PENDIN                            = 0x20000000
	PRIO_PGRP                         = 0x1
	PRIO_PROCESS                      = 0x0
	PRIO_USER                         = 0x2
	PROT_EXEC                         = 0x4
	PROT_NONE                         = 0x0
	PROT_READ                         = 0x1
	PROT_WRITE                        = 0x2
	PT_ATTACH                         = 0xa
	PT_ATTACHEXC                      = 0xe
	PT_CONTINUE                       = 0x7
	PT_DENY_ATTACH                    = 0x1f
	PT_DETACH                         = 0xb
	PT_FIRSTMACH                      = 0x20
	PT_FORCEQUOTA                     = 0x1e
	PT_KILL                           = 0x8
	PT_READ_D                         = 0x2
	PT_READ_I                         = 0x1
	PT_READ_U                         = 0x3
	PT_SIGEXC                         = 0xc
	PT_STEP                           = 0x9
	PT_THUPDATE                       = 0xd
	PT_TRACE_ME                       = 0x0
	PT_WRITE_D                        = 0x5
	PT_WRITE_I                        = 0x4
	PT_WRITE_U                        = 0x6
	RLIMIT_AS                         = 0x5
	RLIMIT_CORE                       = 0x4
	RLIMIT_CPU                        = 0x0
	RLIMIT_CPU_USAGE_MONITOR          = 0x2
	RLIMIT_DATA                       = 0x2
	RLIMIT_FSIZE                      = 0x1
	RLIMIT_NOFILE                     = 0x8
	RLIMIT_STACK                      = 0x3
	RLIM_INFINITY                     = 0x7fffffffffffffff
	RTAX_AUTHOR                       = 0x6
	RTAX_BRD                          = 0x7
	RTAX_DST                          = 0x0
	RTAX_GATEWAY                      = 0x1
	RTAX_GENMASK                      = 0x3
	RTAX_IFA                          = 0x5
	RTAX_IFP                          = 0x4
	RTAX_MAX                          = 0x8
	RTAX_NETMASK                      = 0x2
	RTA_AUTHOR                        = 0x40
	RTA_BRD                           = 0x80
	RTA_DST                           = 0x1
	RTA_GATEWAY                       = 0x2
	RTA_GENMASK                       = 0x8
	RTA_IFA                           = 0x20
	RTA_IFP                           = 0x10
	RTA_NETMASK                       = 0x4
	RTF_BLACKHOLE                     = 0x1000
	RTF_BROADCAST                     = 0x400000
	RTF_CLONING                       = 0x100
	RTF_CONDEMNED                     = 0x2000000
	RTF_DELCLONE                      = 0x80
	RTF_DONE                          = 0x40
	RTF_DYNAMIC                       = 0x10
	RTF_GATEWAY                       = 0x2
	RTF_HOST                          = 0x4
	RTF_IFREF                         = 0x4000000
	RTF_IFSCOPE                       = 0x1000000
	RTF_LLINFO                        = 0x400
	RTF_LOCAL                         = 0x200000
	RTF_MODIFIED                      = 0x20
	RTF_MULTICAST                     = 0x800000
	RTF_PINNED                        = 0x100000
	RTF_PRCLONING                     = 0x10000
	RTF_PROTO1                        = 0x8000
	RTF_PROTO2                        = 0x4000
	RTF_PROTO3                        = 0x40000
	RTF_PROXY                         = 0x8000000
	RTF_REJECT                        = 0x8
	RTF_ROUTER                        = 0x10000000
	RTF_STATIC                        = 0x800
	RTF_UP                            = 0x1
	RTF_WASCLONED                     = 0x20000
	RTF_XRESOLVE                      = 0x200
	RTM_ADD                           = 0x1
	RTM_CHANGE                        = 0x3
	RTM_DELADDR                       = 0xd
	RTM_DELETE                        = 0x2
	RTM_DELMADDR                      = 0x10
	RTM_GET                           = 0x4
	RTM_GET2                          = 0x14
	RTM_IFINFO                        = 0xe
	RTM_IFINFO2                       = 0x12
	RTM_LOCK                          = 0x8
	RTM_LOSING                        = 0x5
	RTM_MISS                          = 0x7
	RTM_NEWADDR                       = 0xc
	RTM_NEWMADDR                      = 0xf
	RTM_NEWMADDR2                     = 0x13
	RTM_OLDADD                        = 0x9
	RTM_OLDDEL                        = 0xa
	RTM_REDIRECT                      = 0x6
	RTM_RESOLVE                       = 0xb
	RTM_RTTUNIT                       = 0xf4240
	RTM_VERSION                       = 0x5
	RTV_EXPIRE                        = 0x4
	RTV_HOPCOUNT                      = 0x2
	RTV_MTU                           = 0x1
	RTV_RPIPE                         = 0x8
	RTV_RTT                           = 0x40
	RTV_RTTVAR                        = 0x80
	RTV_SPIPE                         = 0x10
	RTV_SSTHRESH                      = 0x20
	RUSAGE_CHILDREN                   = -0x1
	RUSAGE_SELF                       = 0x0
	SCM_CREDS                         = 0x3
	SCM_RIGHTS                        = 0x1
	SCM_TIMESTAMP                     = 0x2
	SCM_TIMESTAMP_MONOTONIC           = 0x4
	SHUT_RD                           = 0x0
	SHUT_RDWR                         = 0x2
	SHUT_WR                           = 0x1
	SIOCADDMULTI                      = 0x80206931
	SIOCAIFADDR                       = 0x8040691a
	SIOCARPIPLL                       = 0xc0206928
	SIOCATMARK                        = 0x40047307
	SIOCAUTOADDR                      = 0xc0206926
	SIOCAUTONETMASK                   = 0x80206927
	SIOCDELMULTI                      = 0x80206932
	SIOCDIFADDR                       = 0x80206919
	SIOCDIFPHYADDR                    = 0x80206941
	SIOCGDRVSPEC                      = 0xc028697b
	SIOCGETVLAN                       = 0xc020697f
	SIOCGHIWAT                        = 0x40047301
	SIOCGIFADDR                       = 0xc0206921
	SIOCGIFALTMTU                     = 0xc0206948
	SIOCGIFASYNCMAP                   = 0xc020697c
	SIOCGIFBOND                       = 0xc0206947
	SIOCGIFBRDADDR                    = 0xc0206923
	SIOCGIFCAP                        = 0xc020695b
	SIOCGIFCONF                       = 0xc00c6924
	SIOCGIFDEVMTU                     = 0xc0206944
	SIOCGIFDSTADDR                    = 0xc0206922
	SIOCGIFFLAGS                      = 0xc0206911
	SIOCGIFGENERIC                    = 0xc020693a
	SIOCGIFKPI                        = 0xc0206987
	SIOCGIFMAC                        = 0xc0206982
	SIOCGIFMEDIA                      = 0xc02c6938
	SIOCGIFMETRIC                     = 0xc0206917
	SIOCGIFMTU                        = 0xc0206933
	SIOCGIFNETMASK                    = 0xc0206925
	SIOCGIFPDSTADDR                   = 0xc0206940
	SIOCGIFPHYS                       = 0xc0206935
	SIOCGIFPSRCADDR                   = 0xc020693f
	SIOCGIFSTATUS                     = 0xc331693d
	SIOCGIFVLAN                       = 0xc020697f
	SIOCGIFWAKEFLAGS                  = 0xc0206988
	SIOCGLOWAT                        = 0x40047303
	SIOCGPGRP                         = 0x40047309
	SIOCIFCREATE                      = 0xc0206978
	SIOCIFCREATE2                     = 0xc020697a
	SIOCIFDESTROY                     = 0x80206979
	SIOCIFGCLONERS                    = 0xc0106981
	SIOCRSLVMULTI                     = 0xc010693b
	SIOCSDRVSPEC                      = 0x8028697b
	SIOCSETVLAN                       = 0x8020697e
	SIOCSHIWAT                        = 0x80047300
	SIOCSIFADDR                       = 0x8020690c
	SIOCSIFALTMTU                     = 0x80206945
	SIOCSIFASYNCMAP                   = 0x8020697d
	SIOCSIFBOND                       = 0x80206946
	SIOCSIFBRDADDR                    = 0x80206913
	SIOCSIFCAP                        = 0x8020695a
	SIOCSIFDSTADDR                    = 0x8020690e
	SIOCSIFFLAGS                      = 0x80206910
	SIOCSIFGENERIC                    = 0x80206939
	SIOCSIFKPI                        = 0x80206986
	SIOCSIFLLADDR                     = 0x8020693c
	SIOCSIFMAC                        = 0x80206983
	SIOCSIFMEDIA                      = 0xc0206937
	SIOCSIFMETRIC                     = 0x80206918
	SIOCSIFMTU                        = 0x80206934
	SIOCSIFNETMASK                    = 0x80206916
	SIOCSIFPHYADDR                    = 0x8040693e
	SIOCSIFPHYS                       = 0x80206936
	SIOCSIFVLAN                       = 0x8020697e
	SIOCSLOWAT                        = 0x80047302
	SIOCSPGRP                         = 0x80047308
	SOCK_DGRAM                        = 0x2
	SOCK_MAXADDRLEN                   = 0xff
	SOCK_RAW                          = 0x3
	SOCK_RDM                          = 0x4
	SOCK_SEQPACKET                    = 0x5
	SOCK_STREAM                       = 0x1
	SOL_SOCKET                        = 0xffff
	SOMAXCONN                         = 0x80
	SO_ACCEPTCONN                     = 0x2
	SO_BROADCAST                      = 0x20
	SO_DEBUG                          = 0x1
	SO_DONTROUTE                      = 0x10
	SO_DONTTRUNC                      = 0x2000
	SO_ERROR                          = 0x1007
	SO_KEEPALIVE                      = 0x8
	SO_LABEL                          = 0x1010
	SO_LINGER                         = 0x80
	SO_LINGER_SEC                     = 0x1080
	SO_NKE                            = 0x1021
	SO_NOADDRERR                      = 0x1023
	SO_NOSIGPIPE                      = 0x1022
	SO_NOTIFYCONFLICT                 = 0x1026
	SO_NP_EXTENSIONS                  = 0x1083
	SO_NREAD                          = 0x1020
	SO_NUMRCVPKT                      = 0x1112
	SO_NWRITE                         = 0x1024
	SO_OOBINLINE                      = 0x100
	SO_PEERLABEL                      = 0x1011
	SO_RANDOMPORT                     = 0x1082
	SO_RCVBUF                         = 0x1002
	SO_RCVLOWAT                       = 0x1004
	SO_RCVTIMEO                       = 0x1006
	SO_REUSEADDR                      = 0x4
	SO_REUSEPORT                      = 0x200
	SO_REUSESHAREUID                  = 0x1025
	SO_SNDBUF                         = 0x1001
	SO_SNDLOWAT                       = 0x1003
	SO_SNDTIMEO                       = 0x1005
	SO_TIMESTAMP                      = 0x400
	SO_TIMESTAMP_MONOTONIC            = 0x800
	SO_TYPE                           = 0x1008
	SO_UPCALLCLOSEWAIT                = 0x1027
	SO_USELOOPBACK                    = 0x40
	SO_WANTMORE                       = 0x4000
	SO_WANTOOBFLAG                    = 0x8000
	S_IEXEC                           = 0x40
	S_IFBLK                           = 0x6000
	S_IFCHR                           = 0x2000
	S_IFDIR                           = 0x4000
	S_IFIFO                           = 0x1000
	S_IFLNK                           = 0xa000
	S_IFMT                            = 0xf000
	S_IFREG                           = 0x8000
	S_IFSOCK                          = 0xc000
	S_IFWHT                           = 0xe000
	S_IREAD                           = 0x100
	S_IRGRP                           = 0x20
	S_IROTH                           = 0x4
	S_IRUSR                           = 0x100
	S_IRWXG                           = 0x38
	S_IRWXO                           = 0x7
	S_IRWXU                           = 0x1c0
	S_ISGID                           = 0x400
	S_ISTXT                           = 0x200
	S_ISUID                           = 0x800
	S_ISVTX                           = 0x200
	S_IWGRP                           = 0x10
	S_IWOTH                           = 0x2
	S_IWRITE                          = 0x80
	S_IWUSR                           = 0x80
	S_IXGRP                           = 0x8
	S_IXOTH                           = 0x1
	S_IXUSR                           = 0x40
	TCIFLUSH                          = 0x1
	TCIOFLUSH                         = 0x3
	TCOFLUSH                          = 0x2
	TCP_CONNECTIONTIMEOUT             = 0x20
	TCP_ENABLE_ECN                    = 0x104
	TCP_KEEPALIVE                     = 0x10
	TCP_KEEPCNT                       = 0x102
	TCP_KEEPINTVL                     = 0x101
	TCP_MAXHLEN                       = 0x3c
	TCP_MAXOLEN                       = 0x28
	TCP_MAXSEG                        = 0x2
	TCP_MAXWIN                        = 0xffff
	TCP_MAX_SACK                      = 0x4
	TCP_MAX_WINSHIFT                  = 0xe
	TCP_MINMSS                        = 0xd8
	TCP_MSS                           = 0x200
	TCP_NODELAY                       = 0x1
	TCP_NOOPT                         = 0x8
	TCP_NOPUSH                        = 0x4
	TCP_NOTSENT_LOWAT                 = 0x201
	TCP_RXT_CONNDROPTIME              = 0x80
	TCP_RXT_FINDROP                   = 0x100
	TCP_SENDMOREACKS                  = 0x103
	TCSAFLUSH                         = 0x2
	TIOCCBRK                          = 0x2000747a
	TIOCCDTR                          = 0x20007478
	TIOCCONS                          = 0x80047462
	TIOCDCDTIMESTAMP                  = 0x40107458
	TIOCDRAIN                         = 0x2000745e
	TIOCDSIMICROCODE                  = 0x20007455
	TIOCEXCL                          = 0x2000740d
	TIOCEXT                           = 0x80047460
	TIOCFLUSH                         = 0x80047410
	TIOCGDRAINWAIT                    = 0x40047456
	TIOCGETA                          = 0x40487413
	TIOCGETD                          = 0x4004741a
	TIOCGPGRP                         = 0x40047477
	TIOCGWINSZ                        = 0x40087468
	TIOCIXOFF                         = 0x20007480
	TIOCIXON                          = 0x20007481
	TIOCMBIC                          = 0x8004746b
	TIOCMBIS                          = 0x8004746c
	TIOCMGDTRWAIT                     = 0x4004745a
	TIOCMGET                          = 0x4004746a
	TIOCMODG                          = 0x40047403
	TIOCMODS                          = 0x80047404
	TIOCMSDTRWAIT                     = 0x8004745b
	TIOCMSET                          = 0x8004746d
	TIOCM_CAR                         = 0x40
	TIOCM_CD                          = 0x40
	TIOCM_CTS                         = 0x20
	TIOCM_DSR                         = 0x100
	TIOCM_DTR                         = 0x2
	TIOCM_LE                          = 0x1
	TIOCM_RI                          = 0x80
	TIOCM_RNG                         = 0x80
	TIOCM_RTS                         = 0x4
	TIOCM_SR                          = 0x10
	TIOCM_ST                          = 0x8
	TIOCNOTTY                         = 0x20007471
	TIOCNXCL                          = 0x2000740e
	TIOCOUTQ                          = 0x40047473
	TIOCPKT                           = 0x80047470
	TIOCPKT_DATA                      = 0x0
	TIOCPKT_DOSTOP                    = 0x20
	TIOCPKT_FLUSHREAD                 = 0x1
	TIOCPKT_FLUSHWRITE                = 0x2
	TIOCPKT_IOCTL                     = 0x40
	TIOCPKT_NOSTOP                    = 0x10
	TIOCPKT_START                     = 0x8
	TIOCPKT_STOP                      = 0x4
	TIOCPTYGNAME                      = 0x40807453
	TIOCPTYGRANT                      = 0x20007454
	TIOCPTYUNLK                       = 0x20007452
	TIOCREMOTE                        = 0x80047469
	TIOCSBRK                          = 0x2000747b
	TIOCSCONS                         = 0x20007463
	TIOCSCTTY                         = 0x20007461
	TIOCSDRAINWAIT                    = 0x80047457
	TIOCSDTR                          = 0x20007479
	TIOCSETA                          = 0x80487414
	TIOCSETAF                         = 0x80487416
	TIOCSETAW                         = 0x80487415
	TIOCSETD                          = 0x8004741b
	TIOCSIG                           = 0x2000745f
	TIOCSPGRP                         = 0x80047476
	TIOCSTART                         = 0x2000746e
	TIOCSTAT                          = 0x20007465
	TIOCSTI                           = 0x80017472
	TIOCSTOP                          = 0x2000746f
	TIOCSWINSZ                        = 0x80087467
	TIOCTIMESTAMP                     = 0x40107459
	TIOCUCNTL                         = 0x80047466
	TOSTOP                            = 0x400000
	VDISCARD                          = 0xf
	VDSUSP                            = 0xb
	VEOF                              = 0x0
	VEOL                              = 0x1
	VEOL2                             = 0x2
	VERASE                            = 0x3
	VINTR                             = 0x8
	VKILL                             = 0x5
	VLNEXT                            = 0xe
	VMIN                              = 0x10
	VQUIT                             = 0x9
	VREPRINT                          = 0x6
	VSTART                            = 0xc
	VSTATUS                           = 0x12
	VSTOP                             = 0xd
	VSUSP                             = 0xa
	VT0                               = 0x0
	VT1                               = 0x10000
	VTDLY                             = 0x10000
	VTIME                             = 0x11
	VWERASE                           = 0x4
	WCONTINUED                        = 0x10
	WCOREFLAG                         = 0x80
	WEXITED                           = 0x4
	WNOHANG                           = 0x1
	WNOWAIT                           = 0x20
	WORDSIZE                          = 0x40
	WSTOPPED                          = 0x8
	WUNTRACED                         = 0x2
)
const (
	E2BIG           = Errno(0x7)
	EACCES          = Errno(0xd)
	EADDRINUSE      = Errno(0x30)
	EADDRNOTAVAIL   = Errno(0x31)
	EAFNOSUPPORT    = Errno(0x2f)
	EAGAIN          = Errno(0x23)
	EALREADY        = Errno(0x25)
	EAUTH           = Errno(0x50)
	EBADARCH        = Errno(0x56)
	EBADEXEC        = Errno(0x55)
	EBADF           = Errno(0x9)
	EBADMACHO       = Errno(0x58)
	EBADMSG         = Errno(0x5e)
	EBADRPC         = Errno(0x48)
	EBUSY           = Errno(0x10)
	ECANCELED       = Errno(0x59)
	ECHILD          = Errno(0xa)
	ECONNABORTED    = Errno(0x35)
	ECONNREFUSED    = Errno(0x3d)
	ECONNRESET      = Errno(0x36)
	EDEADLK         = Errno(0xb)
	EDESTADDRREQ    = Errno(0x27)
	EDEVERR         = Errno(0x53)
	EDOM            = Errno(0x21)
	EDQUOT          = Errno(0x45)
	EEXIST          = Errno(0x11)
	EFAULT          = Errno(0xe)
	EFBIG           = Errno(0x1b)
	EFTYPE          = Errno(0x4f)
	EHOSTDOWN       = Errno(0x40)
	EHOSTUNREACH    = Errno(0x41)
	EIDRM           = Errno(0x5a)
	EILSEQ          = Errno(0x5c)
	EINPROGRESS     = Errno(0x24)
	EINTR           = Errno(0x4)
	EINVAL          = Errno(0x16)
	EIO             = Errno(0x5)
	EISCONN         = Errno(0x38)
	EISDIR          = Errno(0x15)
	ELAST           = Errno(0x6a)
	ELOOP           = Errno(0x3e)
	EMFILE          = Errno(0x18)
	EMLINK          = Errno(0x1f)
	EMSGSIZE        = Errno(0x28)
	EMULTIHOP       = Errno(0x5f)
	ENAMETOOLONG    = Errno(0x3f)
	ENEEDAUTH       = Errno(0x51)
	ENETDOWN        = Errno(0x32)
	ENETRESET       = Errno(0x34)
	ENETUNREACH     = Errno(0x33)
	ENFILE          = Errno(0x17)
	ENOATTR         = Errno(0x5d)
	ENOBUFS         = Errno(0x37)
	ENODATA         = Errno(0x60)
	ENODEV          = Errno(0x13)
	ENOENT          = Errno(0x2)
	ENOEXEC         = Errno(0x8)
	ENOLCK          = Errno(0x4d)
	ENOLINK         = Errno(0x61)
	ENOMEM          = Errno(0xc)
	ENOMSG          = Errno(0x5b)
	ENOPOLICY       = Errno(0x67)
	ENOPROTOOPT     = Errno(0x2a)
	ENOSPC          = Errno(0x1c)
	ENOSR           = Errno(0x62)
	ENOSTR          = Errno(0x63)
	ENOSYS          = Errno(0x4e)
	ENOTBLK         = Errno(0xf)
	ENOTCONN        = Errno(0x39)
	ENOTDIR         = Errno(0x14)
	ENOTEMPTY       = Errno(0x42)
	ENOTRECOVERABLE = Errno(0x68)
	ENOTSOCK        = Errno(0x26)
	ENOTSUP         = Errno(0x2d)
	ENOTTY          = Errno(0x19)
	ENXIO           = Errno(0x6)
	EOPNOTSUPP      = Errno(0x66)
	EOVERFLOW       = Errno(0x54)
	EOWNERDEAD      = Errno(0x69)
	EPERM           = Errno(0x1)
	EPFNOSUPPORT    = Errno(0x2e)
	EPIPE           = Errno(0x20)
	EPROCLIM        = Errno(0x43)
	EPROCUNAVAIL    = Errno(0x4c)
	EPROGMISMATCH   = Errno(0x4b)
	EPROGUNAVAIL    = Errno(0x4a)
	EPROTO          = Errno(0x64)
	EPROTONOSUPPORT = Errno(0x2b)
	EPROTOTYPE      = Errno(0x29)
	EPWROFF         = Errno(0x52)
	EQFULL          = Errno(0x6a)
	ERANGE          = Errno(0x22)
	EREMOTE         = Errno(0x47)
	EROFS           = Errno(0x1e)
	ERPCMISMATCH    = Errno(0x49)
	ESHLIBVERS      = Errno(0x57)
	ESHUTDOWN       = Errno(0x3a)
	ESOCKTNOSUPPORT = Errno(0x2c)
	ESPIPE          = Errno(0x1d)
	ESRCH           = Errno(0x3)
	ESTALE          = Errno(0x46)
	ETIME           = Errno(0x65)
	ETIMEDOUT       = Errno(0x3c)
	ETOOMANYREFS    = Errno(0x3b)
	ETXTBSY         = Errno(0x1a)
	EUSERS          = Errno(0x44)
	EWOULDBLOCK     = Errno(0x23)
	EXDEV           = Errno(0x12)
)
    Errors

const (
	SIGABRT   = Signal(0x6)
	SIGALRM   = Signal(0xe)
	SIGBUS    = Signal(0xa)
	SIGCHLD   = Signal(0x14)
	SIGCONT   = Signal(0x13)
	SIGEMT    = Signal(0x7)
	SIGFPE    = Signal(0x8)
	SIGHUP    = Signal(0x1)
	SIGILL    = Signal(0x4)
	SIGINFO   = Signal(0x1d)
	SIGINT    = Signal(0x2)
	SIGIO     = Signal(0x17)
	SIGIOT    = Signal(0x6)
	SIGKILL   = Signal(0x9)
	SIGPIPE   = Signal(0xd)
	SIGPROF   = Signal(0x1b)
	SIGQUIT   = Signal(0x3)
	SIGSEGV   = Signal(0xb)
	SIGSTOP   = Signal(0x11)
	SIGSYS    = Signal(0xc)
	SIGTERM   = Signal(0xf)
	SIGTRAP   = Signal(0x5)
	SIGTSTP   = Signal(0x12)
	SIGTTIN   = Signal(0x15)
	SIGTTOU   = Signal(0x16)
	SIGURG    = Signal(0x10)
	SIGUSR1   = Signal(0x1e)
	SIGUSR2   = Signal(0x1f)
	SIGVTALRM = Signal(0x1a)
	SIGWINCH  = Signal(0x1c)
	SIGXCPU   = Signal(0x18)
	SIGXFSZ   = Signal(0x19)
)
    Signals

const (
	SYS_SYSCALL                        = 0
	SYS_EXIT                           = 1
	SYS_FORK                           = 2
	SYS_READ                           = 3
	SYS_WRITE                          = 4
	SYS_OPEN                           = 5
	SYS_CLOSE                          = 6
	SYS_WAIT4                          = 7
	SYS_LINK                           = 9
	SYS_UNLINK                         = 10
	SYS_CHDIR                          = 12
	SYS_FCHDIR                         = 13
	SYS_MKNOD                          = 14
	SYS_CHMOD                          = 15
	SYS_CHOWN                          = 16
	SYS_GETFSSTAT                      = 18
	SYS_GETPID                         = 20
	SYS_SETUID                         = 23
	SYS_GETUID                         = 24
	SYS_GETEUID                        = 25
	SYS_PTRACE                         = 26
	SYS_RECVMSG                        = 27
	SYS_SENDMSG                        = 28
	SYS_RECVFROM                       = 29
	SYS_ACCEPT                         = 30
	SYS_GETPEERNAME                    = 31
	SYS_GETSOCKNAME                    = 32
	SYS_ACCESS                         = 33
	SYS_CHFLAGS                        = 34
	SYS_FCHFLAGS                       = 35
	SYS_SYNC                           = 36
	SYS_KILL                           = 37
	SYS_GETPPID                        = 39
	SYS_DUP                            = 41
	SYS_PIPE                           = 42
	SYS_GETEGID                        = 43
	SYS_SIGACTION                      = 46
	SYS_GETGID                         = 47
	SYS_SIGPROCMASK                    = 48
	SYS_GETLOGIN                       = 49
	SYS_SETLOGIN                       = 50
	SYS_ACCT                           = 51
	SYS_SIGPENDING                     = 52
	SYS_SIGALTSTACK                    = 53
	SYS_IOCTL                          = 54
	SYS_REBOOT                         = 55
	SYS_REVOKE                         = 56
	SYS_SYMLINK                        = 57
	SYS_READLINK                       = 58
	SYS_EXECVE                         = 59
	SYS_UMASK                          = 60
	SYS_CHROOT                         = 61
	SYS_MSYNC                          = 65
	SYS_VFORK                          = 66
	SYS_MUNMAP                         = 73
	SYS_MPROTECT                       = 74
	SYS_MADVISE                        = 75
	SYS_MINCORE                        = 78
	SYS_GETGROUPS                      = 79
	SYS_SETGROUPS                      = 80
	SYS_GETPGRP                        = 81
	SYS_SETPGID                        = 82
	SYS_SETITIMER                      = 83
	SYS_SWAPON                         = 85
	SYS_GETITIMER                      = 86
	SYS_GETDTABLESIZE                  = 89
	SYS_DUP2                           = 90
	SYS_FCNTL                          = 92
	SYS_SELECT                         = 93
	SYS_FSYNC                          = 95
	SYS_SETPRIORITY                    = 96
	SYS_SOCKET                         = 97
	SYS_CONNECT                        = 98
	SYS_GETPRIORITY                    = 100
	SYS_BIND                           = 104
	SYS_SETSOCKOPT                     = 105
	SYS_LISTEN                         = 106
	SYS_SIGSUSPEND                     = 111
	SYS_GETTIMEOFDAY                   = 116
	SYS_GETRUSAGE                      = 117
	SYS_GETSOCKOPT                     = 118
	SYS_READV                          = 120
	SYS_WRITEV                         = 121
	SYS_SETTIMEOFDAY                   = 122
	SYS_FCHOWN                         = 123
	SYS_FCHMOD                         = 124
	SYS_SETREUID                       = 126
	SYS_SETREGID                       = 127
	SYS_RENAME                         = 128
	SYS_FLOCK                          = 131
	SYS_MKFIFO                         = 132
	SYS_SENDTO                         = 133
	SYS_SHUTDOWN                       = 134
	SYS_SOCKETPAIR                     = 135
	SYS_MKDIR                          = 136
	SYS_RMDIR                          = 137
	SYS_UTIMES                         = 138
	SYS_FUTIMES                        = 139
	SYS_ADJTIME                        = 140
	SYS_GETHOSTUUID                    = 142
	SYS_SETSID                         = 147
	SYS_GETPGID                        = 151
	SYS_SETPRIVEXEC                    = 152
	SYS_PREAD                          = 153
	SYS_PWRITE                         = 154
	SYS_NFSSVC                         = 155
	SYS_STATFS                         = 157
	SYS_FSTATFS                        = 158
	SYS_UNMOUNT                        = 159
	SYS_GETFH                          = 161
	SYS_QUOTACTL                       = 165
	SYS_MOUNT                          = 167
	SYS_CSOPS                          = 169
	SYS_CSOPS_AUDITTOKEN               = 170
	SYS_WAITID                         = 173
	SYS_KDEBUG_TRACE                   = 180
	SYS_SETGID                         = 181
	SYS_SETEGID                        = 182
	SYS_SETEUID                        = 183
	SYS_SIGRETURN                      = 184
	SYS_CHUD                           = 185
	SYS_FDATASYNC                      = 187
	SYS_STAT                           = 188
	SYS_FSTAT                          = 189
	SYS_LSTAT                          = 190
	SYS_PATHCONF                       = 191
	SYS_FPATHCONF                      = 192
	SYS_GETRLIMIT                      = 194
	SYS_SETRLIMIT                      = 195
	SYS_GETDIRENTRIES                  = 196
	SYS_MMAP                           = 197
	SYS_LSEEK                          = 199
	SYS_TRUNCATE                       = 200
	SYS_FTRUNCATE                      = 201
	SYS___SYSCTL                       = 202
	SYS_MLOCK                          = 203
	SYS_MUNLOCK                        = 204
	SYS_UNDELETE                       = 205
	SYS_ATSOCKET                       = 206
	SYS_ATGETMSG                       = 207
	SYS_ATPUTMSG                       = 208
	SYS_ATPSNDREQ                      = 209
	SYS_ATPSNDRSP                      = 210
	SYS_ATPGETREQ                      = 211
	SYS_ATPGETRSP                      = 212
	SYS_OPEN_DPROTECTED_NP             = 216
	SYS_GETATTRLIST                    = 220
	SYS_SETATTRLIST                    = 221
	SYS_GETDIRENTRIESATTR              = 222
	SYS_EXCHANGEDATA                   = 223
	SYS_SEARCHFS                       = 225
	SYS_DELETE                         = 226
	SYS_COPYFILE                       = 227
	SYS_FGETATTRLIST                   = 228
	SYS_FSETATTRLIST                   = 229
	SYS_POLL                           = 230
	SYS_WATCHEVENT                     = 231
	SYS_WAITEVENT                      = 232
	SYS_MODWATCH                       = 233
	SYS_GETXATTR                       = 234
	SYS_FGETXATTR                      = 235
	SYS_SETXATTR                       = 236
	SYS_FSETXATTR                      = 237
	SYS_REMOVEXATTR                    = 238
	SYS_FREMOVEXATTR                   = 239
	SYS_LISTXATTR                      = 240
	SYS_FLISTXATTR                     = 241
	SYS_FSCTL                          = 242
	SYS_INITGROUPS                     = 243
	SYS_POSIX_SPAWN                    = 244
	SYS_FFSCTL                         = 245
	SYS_NFSCLNT                        = 247
	SYS_FHOPEN                         = 248
	SYS_MINHERIT                       = 250
	SYS_SEMSYS                         = 251
	SYS_MSGSYS                         = 252
	SYS_SHMSYS                         = 253
	SYS_SEMCTL                         = 254
	SYS_SEMGET                         = 255
	SYS_SEMOP                          = 256
	SYS_MSGCTL                         = 258
	SYS_MSGGET                         = 259
	SYS_MSGSND                         = 260
	SYS_MSGRCV                         = 261
	SYS_SHMAT                          = 262
	SYS_SHMCTL                         = 263
	SYS_SHMDT                          = 264
	SYS_SHMGET                         = 265
	SYS_SHM_OPEN                       = 266
	SYS_SHM_UNLINK                     = 267
	SYS_SEM_OPEN                       = 268
	SYS_SEM_CLOSE                      = 269
	SYS_SEM_UNLINK                     = 270
	SYS_SEM_WAIT                       = 271
	SYS_SEM_TRYWAIT                    = 272
	SYS_SEM_POST                       = 273
	SYS_SEM_GETVALUE                   = 274
	SYS_SEM_INIT                       = 275
	SYS_SEM_DESTROY                    = 276
	SYS_OPEN_EXTENDED                  = 277
	SYS_UMASK_EXTENDED                 = 278
	SYS_STAT_EXTENDED                  = 279
	SYS_LSTAT_EXTENDED                 = 280
	SYS_FSTAT_EXTENDED                 = 281
	SYS_CHMOD_EXTENDED                 = 282
	SYS_FCHMOD_EXTENDED                = 283
	SYS_ACCESS_EXTENDED                = 284
	SYS_SETTID                         = 285
	SYS_GETTID                         = 286
	SYS_SETSGROUPS                     = 287
	SYS_GETSGROUPS                     = 288
	SYS_SETWGROUPS                     = 289
	SYS_GETWGROUPS                     = 290
	SYS_MKFIFO_EXTENDED                = 291
	SYS_MKDIR_EXTENDED                 = 292
	SYS_IDENTITYSVC                    = 293
	SYS_SHARED_REGION_CHECK_NP         = 294
	SYS_VM_PRESSURE_MONITOR            = 296
	SYS_PSYNCH_RW_LONGRDLOCK           = 297
	SYS_PSYNCH_RW_YIELDWRLOCK          = 298
	SYS_PSYNCH_RW_DOWNGRADE            = 299
	SYS_PSYNCH_RW_UPGRADE              = 300
	SYS_PSYNCH_MUTEXWAIT               = 301
	SYS_PSYNCH_MUTEXDROP               = 302
	SYS_PSYNCH_CVBROAD                 = 303
	SYS_PSYNCH_CVSIGNAL                = 304
	SYS_PSYNCH_CVWAIT                  = 305
	SYS_PSYNCH_RW_RDLOCK               = 306
	SYS_PSYNCH_RW_WRLOCK               = 307
	SYS_PSYNCH_RW_UNLOCK               = 308
	SYS_PSYNCH_RW_UNLOCK2              = 309
	SYS_GETSID                         = 310
	SYS_SETTID_WITH_PID                = 311
	SYS_PSYNCH_CVCLRPREPOST            = 312
	SYS_AIO_FSYNC                      = 313
	SYS_AIO_RETURN                     = 314
	SYS_AIO_SUSPEND                    = 315
	SYS_AIO_CANCEL                     = 316
	SYS_AIO_ERROR                      = 317
	SYS_AIO_READ                       = 318
	SYS_AIO_WRITE                      = 319
	SYS_LIO_LISTIO                     = 320
	SYS_IOPOLICYSYS                    = 322
	SYS_PROCESS_POLICY                 = 323
	SYS_MLOCKALL                       = 324
	SYS_MUNLOCKALL                     = 325
	SYS_ISSETUGID                      = 327
	SYS___PTHREAD_KILL                 = 328
	SYS___PTHREAD_SIGMASK              = 329
	SYS___SIGWAIT                      = 330
	SYS___DISABLE_THREADSIGNAL         = 331
	SYS___PTHREAD_MARKCANCEL           = 332
	SYS___PTHREAD_CANCELED             = 333
	SYS___SEMWAIT_SIGNAL               = 334
	SYS_PROC_INFO                      = 336
	SYS_SENDFILE                       = 337
	SYS_STAT64                         = 338
	SYS_FSTAT64                        = 339
	SYS_LSTAT64                        = 340
	SYS_STAT64_EXTENDED                = 341
	SYS_LSTAT64_EXTENDED               = 342
	SYS_FSTAT64_EXTENDED               = 343
	SYS_GETDIRENTRIES64                = 344
	SYS_STATFS64                       = 345
	SYS_FSTATFS64                      = 346
	SYS_GETFSSTAT64                    = 347
	SYS___PTHREAD_CHDIR                = 348
	SYS___PTHREAD_FCHDIR               = 349
	SYS_AUDIT                          = 350
	SYS_AUDITON                        = 351
	SYS_GETAUID                        = 353
	SYS_SETAUID                        = 354
	SYS_GETAUDIT_ADDR                  = 357
	SYS_SETAUDIT_ADDR                  = 358
	SYS_AUDITCTL                       = 359
	SYS_BSDTHREAD_CREATE               = 360
	SYS_BSDTHREAD_TERMINATE            = 361
	SYS_KQUEUE                         = 362
	SYS_KEVENT                         = 363
	SYS_LCHOWN                         = 364
	SYS_STACK_SNAPSHOT                 = 365
	SYS_BSDTHREAD_REGISTER             = 366
	SYS_WORKQ_OPEN                     = 367
	SYS_WORKQ_KERNRETURN               = 368
	SYS_KEVENT64                       = 369
	SYS___OLD_SEMWAIT_SIGNAL           = 370
	SYS___OLD_SEMWAIT_SIGNAL_NOCANCEL  = 371
	SYS_THREAD_SELFID                  = 372
	SYS_LEDGER                         = 373
	SYS___MAC_EXECVE                   = 380
	SYS___MAC_SYSCALL                  = 381
	SYS___MAC_GET_FILE                 = 382
	SYS___MAC_SET_FILE                 = 383
	SYS___MAC_GET_LINK                 = 384
	SYS___MAC_SET_LINK                 = 385
	SYS___MAC_GET_PROC                 = 386
	SYS___MAC_SET_PROC                 = 387
	SYS___MAC_GET_FD                   = 388
	SYS___MAC_SET_FD                   = 389
	SYS___MAC_GET_PID                  = 390
	SYS___MAC_GET_LCID                 = 391
	SYS___MAC_GET_LCTX                 = 392
	SYS___MAC_SET_LCTX                 = 393
	SYS_SETLCID                        = 394
	SYS_GETLCID                        = 395
	SYS_READ_NOCANCEL                  = 396
	SYS_WRITE_NOCANCEL                 = 397
	SYS_OPEN_NOCANCEL                  = 398
	SYS_CLOSE_NOCANCEL                 = 399
	SYS_WAIT4_NOCANCEL                 = 400
	SYS_RECVMSG_NOCANCEL               = 401
	SYS_SENDMSG_NOCANCEL               = 402
	SYS_RECVFROM_NOCANCEL              = 403
	SYS_ACCEPT_NOCANCEL                = 404
	SYS_MSYNC_NOCANCEL                 = 405
	SYS_FCNTL_NOCANCEL                 = 406
	SYS_SELECT_NOCANCEL                = 407
	SYS_FSYNC_NOCANCEL                 = 408
	SYS_CONNECT_NOCANCEL               = 409
	SYS_SIGSUSPEND_NOCANCEL            = 410
	SYS_READV_NOCANCEL                 = 411
	SYS_WRITEV_NOCANCEL                = 412
	SYS_SENDTO_NOCANCEL                = 413
	SYS_PREAD_NOCANCEL                 = 414
	SYS_PWRITE_NOCANCEL                = 415
	SYS_WAITID_NOCANCEL                = 416
	SYS_POLL_NOCANCEL                  = 417
	SYS_MSGSND_NOCANCEL                = 418
	SYS_MSGRCV_NOCANCEL                = 419
	SYS_SEM_WAIT_NOCANCEL              = 420
	SYS_AIO_SUSPEND_NOCANCEL           = 421
	SYS___SIGWAIT_NOCANCEL             = 422
	SYS___SEMWAIT_SIGNAL_NOCANCEL      = 423
	SYS___MAC_MOUNT                    = 424
	SYS___MAC_GET_MOUNT                = 425
	SYS___MAC_GETFSSTAT                = 426
	SYS_FSGETPATH                      = 427
	SYS_AUDIT_SESSION_SELF             = 428
	SYS_AUDIT_SESSION_JOIN             = 429
	SYS_FILEPORT_MAKEPORT              = 430
	SYS_FILEPORT_MAKEFD                = 431
	SYS_AUDIT_SESSION_PORT             = 432
	SYS_PID_SUSPEND                    = 433
	SYS_PID_RESUME                     = 434
	SYS_PID_HIBERNATE                  = 435
	SYS_PID_SHUTDOWN_SOCKETS           = 436
	SYS_SHARED_REGION_MAP_AND_SLIDE_NP = 438
	SYS_KAS_INFO                       = 439
	SYS_MAXSYSCALL                     = 440
)
const (
	SizeofSockaddrInet4    = 0x10
	SizeofSockaddrInet6    = 0x1c
	SizeofSockaddrAny      = 0x6c
	SizeofSockaddrUnix     = 0x6a
	SizeofSockaddrDatalink = 0x14
	SizeofLinger           = 0x8
	SizeofIPMreq           = 0x8
	SizeofIPv6Mreq         = 0x14
	SizeofMsghdr           = 0x30
	SizeofCmsghdr          = 0xc
	SizeofInet4Pktinfo     = 0xc
	SizeofInet6Pktinfo     = 0x14
	SizeofIPv6MTUInfo      = 0x20
	SizeofICMPv6Filter     = 0x20
)
const (
	PTRACE_TRACEME = 0x0
	PTRACE_CONT    = 0x7
	PTRACE_KILL    = 0x8
)
const (
	SizeofIfMsghdr    = 0x70
	SizeofIfData      = 0x60
	SizeofIfaMsghdr   = 0x14
	SizeofIfmaMsghdr  = 0x10
	SizeofIfmaMsghdr2 = 0x14
	SizeofRtMsghdr    = 0x5c
	SizeofRtMetrics   = 0x38
)
const (
	SizeofBpfVersion = 0x4
	SizeofBpfStat    = 0x8
	SizeofBpfProgram = 0x10
	SizeofBpfInsn    = 0x8
	SizeofBpfHdr     = 0x14
)
const ImplementsGetwd = true

VARIABLES

var (
	Stdin  = 0
	Stdout = 1
	Stderr = 2
)
var ForkLock sync.RWMutex
    ForkLock is used to synchronize creation of new file descriptors with fork.

    We want the child in a fork/exec sequence to inherit only the file
    descriptors we intend. To do that, we mark all file descriptors
    close-on-exec and then, in the child, explicitly unmark the ones we want the
    exec'ed program to keep. Unix doesn't make this easy: there is, in general,
    no way to allocate a new file descriptor close-on-exec. Instead you have to
    allocate the descriptor and then mark it close-on-exec. If a fork happens
    between those two events, the child's exec will inherit an unwanted file
    descriptor.

    This lock solves that race: the create new fd/mark close-on-exec operation
    is done holding ForkLock for reading, and the fork itself is done
    holding ForkLock for writing. At least, that's the idea. There are some
    complications.

    Some system calls that create new file descriptors can block for arbitrarily
    long times: open on a hung NFS server or named pipe, accept on a socket,
    and so on. We can't reasonably grab the lock across those operations.

    It is worse to inherit some file descriptors than others. If a non-malicious
    child accidentally inherits an open ordinary file, that's not a big deal.
    On the other hand, if a long-lived child accidentally inherits the write end
    of a pipe, then the reader of that pipe will not see EOF until that child
    exits, potentially causing the parent program to hang. This is a common
    problem in threaded C programs that use popen.

    Luckily, the file descriptors that are most important not to inherit
    are not the ones that can take an arbitrarily long time to create: pipe
    returns instantly, and the net package uses non-blocking I/O to accept on a
    listening socket. The rules for which file descriptor-creating operations
    use the ForkLock are as follows:

      - Pipe. Use pipe2 if available. Otherwise, does not block, so use
        ForkLock.
      - Socket. Use SOCK_CLOEXEC if available. Otherwise, does not block,
        so use ForkLock.
      - Open. Use O_CLOEXEC if available. Otherwise, may block, so live with the
        race.
      - Dup. Use F_DUPFD_CLOEXEC or dup3 if available. Otherwise, does not
        block, so use ForkLock.

var SocketDisableIPv6 bool
    For testing: clients can set this flag to force creation of IPv6 sockets to
    return EAFNOSUPPORT.


FUNCTIONS

func Accept(fd int) (nfd int, sa Sockaddr, err error)
func Access(path string, mode uint32) (err error)
func Adjtime(delta *Timeval, olddelta *Timeval) (err error)
func Bind(fd int, sa Sockaddr) (err error)
func BpfBuflen(fd int) (int, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func BpfDatalink(fd int) (int, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func BpfHeadercmpl(fd int) (int, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func BpfInterface(fd int, name string) (string, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func BpfStats(fd int) (*BpfStat, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func BpfTimeout(fd int) (*Timeval, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func BytePtrFromString(s string) (*byte, error)
    BytePtrFromString returns a pointer to a NUL-terminated array of bytes
    containing the text of s. If s contains a NUL byte at any location,
    it returns (nil, EINVAL).

func ByteSliceFromString(s string) ([]byte, error)
    ByteSliceFromString returns a NUL-terminated slice of bytes containing
    the text of s. If s contains a NUL byte at any location, it returns (nil,
    EINVAL).

func Chdir(path string) (err error)
func CheckBpfVersion(fd int) error
    Deprecated: Use golang.org/x/net/bpf instead.

func Chflags(path string, flags int) (err error)
func Chmod(path string, mode uint32) (err error)
func Chown(path string, uid int, gid int) (err error)
func Chroot(path string) (err error)
func Clearenv()
func Close(fd int) (err error)
func CloseOnExec(fd int)
func CmsgLen(datalen int) int
    CmsgLen returns the value to store in the Len field of the Cmsghdr
    structure, taking into account any necessary alignment.

func CmsgSpace(datalen int) int
    CmsgSpace returns the number of bytes an ancillary element with payload of
    the passed data length occupies.

func Connect(fd int, sa Sockaddr) (err error)
func Dup(fd int) (nfd int, err error)
func Dup2(from int, to int) (err error)
func Environ() []string
func Exchangedata(path1 string, path2 string, options int) (err error)
func Exec(argv0 string, argv []string, envv []string) (err error)
    Exec invokes the execve(2) system call.

func Exit(code int)
func Fchdir(fd int) (err error)
func Fchflags(fd int, flags int) (err error)
func Fchmod(fd int, mode uint32) (err error)
func Fchown(fd int, uid int, gid int) (err error)
func FcntlFlock(fd uintptr, cmd int, lk *Flock_t) error
    FcntlFlock performs a fcntl syscall for the F_GETLK, F_SETLK or F_SETLKW
    command.

func Flock(fd int, how int) (err error)
func FlushBpf(fd int) error
    Deprecated: Use golang.org/x/net/bpf instead.

func ForkExec(argv0 string, argv []string, attr *ProcAttr) (pid int, err error)
    Combination of fork and exec, careful to be thread safe.

func Fpathconf(fd int, name int) (val int, err error)
func Fstat(fd int, stat *Stat_t) (err error)
func Fstatfs(fd int, stat *Statfs_t) (err error)
func Fsync(fd int) (err error)
func Ftruncate(fd int, length int64) (err error)
func Futimes(fd int, tv []Timeval) (err error)
func Getdirentries(fd int, buf []byte, basep *uintptr) (n int, err error)
func Getdtablesize() (size int)
func Getegid() (egid int)
func Getenv(key string) (value string, found bool)
func Geteuid() (uid int)
func Getfsstat(buf []Statfs_t, flags int) (n int, err error)
func Getgid() (gid int)
func Getgroups() (gids []int, err error)
func Getpagesize() int
func Getpeername(fd int) (sa Sockaddr, err error)
func Getpgid(pid int) (pgid int, err error)
func Getpgrp() (pgrp int)
func Getpid() (pid int)
func Getppid() (ppid int)
func Getpriority(which int, who int) (prio int, err error)
func Getrlimit(which int, lim *Rlimit) (err error)
func Getrusage(who int, rusage *Rusage) (err error)
func Getsid(pid int) (sid int, err error)
func Getsockname(fd int) (sa Sockaddr, err error)
func GetsockoptByte(fd, level, opt int) (value byte, err error)
func GetsockoptICMPv6Filter(fd, level, opt int) (*ICMPv6Filter, error)
func GetsockoptIPMreq(fd, level, opt int) (*IPMreq, error)
func GetsockoptIPv6MTUInfo(fd, level, opt int) (*IPv6MTUInfo, error)
func GetsockoptIPv6Mreq(fd, level, opt int) (*IPv6Mreq, error)
func GetsockoptInet4Addr(fd, level, opt int) (value [4]byte, err error)
func GetsockoptInt(fd, level, opt int) (value int, err error)
func Gettimeofday(tp *Timeval) (err error)
func Getuid() (uid int)
func Getwd() (string, error)
func Issetugid() (tainted bool)
func Kevent(kq int, changes, events []Kevent_t, timeout *Timespec) (n int, err error)
func Kill(pid int, signum Signal) (err error)
func Kqueue() (fd int, err error)
func Lchown(path string, uid int, gid int) (err error)
func Link(path string, link string) (err error)
func Listen(s int, backlog int) (err error)
func Lstat(path string, stat *Stat_t) (err error)
func Mkdir(path string, mode uint32) (err error)
func Mkfifo(path string, mode uint32) (err error)
func Mknod(path string, mode uint32, dev int) (err error)
func Mlock(b []byte) (err error)
func Mlockall(flags int) (err error)
func Mmap(fd int, offset int64, length int, prot int, flags int) (data []byte, err error)
func Mprotect(b []byte, prot int) (err error)
func Munlock(b []byte) (err error)
func Munlockall() (err error)
func Munmap(b []byte) (err error)
func Open(path string, mode int, perm uint32) (fd int, err error)
func ParseDirent(buf []byte, max int, names []string) (consumed int, count int, newnames []string)
    ParseDirent parses up to max directory entries in buf, appending the names
    to names. It returns the number of bytes consumed from buf, the number of
    entries added to names, and the new names slice.

func ParseRoutingMessage(b []byte) (msgs []RoutingMessage, err error)
    ParseRoutingMessage parses b as routing messages and returns the slice
    containing the RoutingMessage interfaces.

    Deprecated: Use golang.org/x/net/route instead.

func ParseRoutingSockaddr(msg RoutingMessage) ([]Sockaddr, error)
    ParseRoutingSockaddr parses msg's payload as raw sockaddrs and returns the
    slice containing the Sockaddr interfaces.

    Deprecated: Use golang.org/x/net/route instead.

func ParseSocketControlMessage(b []byte) ([]SocketControlMessage, error)
    ParseSocketControlMessage parses b as an array of socket control messages.

func ParseUnixRights(m *SocketControlMessage) ([]int, error)
    ParseUnixRights decodes a socket control message that contains an integer
    array of open file descriptors from another process.

func Pathconf(path string, name int) (val int, err error)
func Pipe(p []int) (err error)
func Pread(fd int, p []byte, offset int64) (n int, err error)
func PtraceAttach(pid int) (err error)
func PtraceDetach(pid int) (err error)
func Pwrite(fd int, p []byte, offset int64) (n int, err error)
func RawSyscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
func RawSyscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
func Read(fd int, p []byte) (n int, err error)
func ReadDirent(fd int, buf []byte) (n int, err error)
func Readlink(path string, buf []byte) (n int, err error)
func Recvfrom(fd int, p []byte, flags int) (n int, from Sockaddr, err error)
func Recvmsg(fd int, p, oob []byte, flags int) (n, oobn int, recvflags int, from Sockaddr, err error)
func Rename(from string, to string) (err error)
func Revoke(path string) (err error)
func Rmdir(path string) (err error)
func RouteRIB(facility, param int) ([]byte, error)
    RouteRIB returns routing information base, as known as RIB, which consists
    of network facility information, states and parameters.

    Deprecated: Use golang.org/x/net/route instead.

func Seek(fd int, offset int64, whence int) (newoffset int64, err error)
func Select(n int, r *FdSet, w *FdSet, e *FdSet, timeout *Timeval) (err error)
func Sendfile(outfd int, infd int, offset *int64, count int) (written int, err error)
func Sendmsg(fd int, p, oob []byte, to Sockaddr, flags int) (err error)
func SendmsgN(fd int, p, oob []byte, to Sockaddr, flags int) (n int, err error)
func Sendto(fd int, p []byte, flags int, to Sockaddr) (err error)
func SetBpf(fd int, i []BpfInsn) error
    Deprecated: Use golang.org/x/net/bpf instead.

func SetBpfBuflen(fd, l int) (int, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func SetBpfDatalink(fd, t int) (int, error)
    Deprecated: Use golang.org/x/net/bpf instead.

func SetBpfHeadercmpl(fd, f int) error
    Deprecated: Use golang.org/x/net/bpf instead.

func SetBpfImmediate(fd, m int) error
    Deprecated: Use golang.org/x/net/bpf instead.

func SetBpfInterface(fd int, name string) error
    Deprecated: Use golang.org/x/net/bpf instead.

func SetBpfPromisc(fd, m int) error
    Deprecated: Use golang.org/x/net/bpf instead.

func SetBpfTimeout(fd int, tv *Timeval) error
    Deprecated: Use golang.org/x/net/bpf instead.

func SetKevent(k *Kevent_t, fd, mode, flags int)
func SetNonblock(fd int, nonblocking bool) (err error)
func Setegid(egid int) (err error)
func Setenv(key, value string) error
func Seteuid(euid int) (err error)
func Setgid(gid int) (err error)
func Setgroups(gids []int) (err error)
func Setlogin(name string) (err error)
func Setpgid(pid int, pgid int) (err error)
func Setpriority(which int, who int, prio int) (err error)
func Setprivexec(flag int) (err error)
func Setregid(rgid int, egid int) (err error)
func Setreuid(ruid int, euid int) (err error)
func Setrlimit(resource int, rlim *Rlimit) error
func Setsid() (pid int, err error)
func SetsockoptByte(fd, level, opt int, value byte) (err error)
func SetsockoptICMPv6Filter(fd, level, opt int, filter *ICMPv6Filter) error
func SetsockoptIPMreq(fd, level, opt int, mreq *IPMreq) (err error)
func SetsockoptIPv6Mreq(fd, level, opt int, mreq *IPv6Mreq) (err error)
func SetsockoptInet4Addr(fd, level, opt int, value [4]byte) (err error)
func SetsockoptInt(fd, level, opt int, value int) (err error)
func SetsockoptLinger(fd, level, opt int, l *Linger) (err error)
func SetsockoptString(fd, level, opt int, s string) (err error)
func SetsockoptTimeval(fd, level, opt int, tv *Timeval) (err error)
func Settimeofday(tp *Timeval) (err error)
func Setuid(uid int) (err error)
func Shutdown(s int, how int) (err error)
func SlicePtrFromStrings(ss []string) ([]*byte, error)
    SlicePtrFromStrings converts a slice of strings to a slice of pointers to
    NUL-terminated byte arrays. If any string contains a NUL byte, it returns
    (nil, EINVAL).

func Socket(domain, typ, proto int) (fd int, err error)
func Socketpair(domain, typ, proto int) (fd [2]int, err error)
func StartProcess(argv0 string, argv []string, attr *ProcAttr) (pid int, handle uintptr, err error)
    StartProcess wraps ForkExec for package os.

func Stat(path string, stat *Stat_t) (err error)
func Statfs(path string, stat *Statfs_t) (err error)
func StringBytePtr(s string) *byte
    StringBytePtr returns a pointer to a NUL-terminated array of bytes. If s
    contains a NUL byte this function panics instead of returning an error.

    Deprecated: Use BytePtrFromString instead.

func StringByteSlice(s string) []byte
    StringByteSlice converts a string to a NUL-terminated []byte, If s contains
    a NUL byte this function panics instead of returning an error.

    Deprecated: Use ByteSliceFromString instead.

func StringSlicePtr(ss []string) []*byte
    StringSlicePtr converts a slice of strings to a slice of pointers to
    NUL-terminated byte arrays. If any string contains a NUL byte this function
    panics instead of returning an error.

    Deprecated: Use SlicePtrFromStrings instead.

func Symlink(path string, link string) (err error)
func Sync() (err error)
func Syscall(trap, a1, a2, a3 uintptr) (r1, r2 uintptr, err Errno)
func Syscall6(trap, a1, a2, a3, a4, a5, a6 uintptr) (r1, r2 uintptr, err Errno)
func Syscall9(num, a1, a2, a3, a4, a5, a6, a7, a8, a9 uintptr) (r1, r2 uintptr, err Errno)
func Sysctl(name string) (value string, err error)
func SysctlUint32(name string) (value uint32, err error)
func TimespecToNsec(ts Timespec) int64
    TimespecToNsec returns the time stored in ts as nanoseconds.

func TimevalToNsec(tv Timeval) int64
    TimevalToNsec returns the time stored in tv as nanoseconds.

func Truncate(path string, length int64) (err error)
func Umask(newmask int) (oldmask int)
func Undelete(path string) (err error)
func UnixRights(fds ...int) []byte
    UnixRights encodes a set of open file descriptors into a socket control
    message for sending to another process.

func Unlink(path string) (err error)
func Unmount(path string, flags int) (err error)
func Unsetenv(key string) error
func Utimes(path string, tv []Timeval) (err error)
func UtimesNano(path string, ts []Timespec) error
func Wait4(pid int, wstatus *WaitStatus, options int, rusage *Rusage) (wpid int, err error)
func Write(fd int, p []byte) (n int, err error)

TYPES

type BpfHdr struct {
	Tstamp    Timeval32
	Caplen    uint32
	Datalen   uint32
	Hdrlen    uint16
	Pad_cgo_0 [2]byte
}

type BpfInsn struct {
	Code uint16
	Jt   uint8
	Jf   uint8
	K    uint32
}

func BpfJump(code, k, jt, jf int) *BpfInsn
    Deprecated: Use golang.org/x/net/bpf instead.

func BpfStmt(code, k int) *BpfInsn
    Deprecated: Use golang.org/x/net/bpf instead.

type BpfProgram struct {
	Len       uint32
	Pad_cgo_0 [4]byte
	Insns     *BpfInsn
}

type BpfStat struct {
	Recv uint32
	Drop uint32
}

type BpfVersion struct {
	Major uint16
	Minor uint16
}

type Cmsghdr struct {
	Len   uint32
	Level int32
	Type  int32
}

func (cmsg *Cmsghdr) SetLen(length int)

type Conn interface {
	// SyscallConn returns a raw network connection.
	SyscallConn() (RawConn, error)
}
    Conn is implemented by some types in the net and os packages to provide
    access to the underlying file descriptor or handle.

type Credential struct {
	Uid         uint32   // User ID.
	Gid         uint32   // Group ID.
	Groups      []uint32 // Supplementary group IDs.
	NoSetGroups bool     // If true, don't set supplementary groups
}
    Credential holds user and group identities to be assumed by a child process
    started by StartProcess.

type Dirent struct {
	Ino       uint64
	Seekoff   uint64
	Reclen    uint16
	Namlen    uint16
	Type      uint8
	Name      [1024]int8
	Pad_cgo_0 [3]byte
}

type Errno uintptr
    An Errno is an unsigned number describing an error condition. It implements
    the error interface. The zero Errno is by convention a non-error, so code to
    convert from Errno to error should use:

        err = nil
        if errno != 0 {
        	err = errno
        }

    Errno values can be tested against error values using errors.Is. For
    example:

        _, _, err := syscall.Syscall(...)
        if errors.Is(err, fs.ErrNotExist) ...

func (e Errno) Error() string

func (e Errno) Is(target error) bool

func (e Errno) Temporary() bool

func (e Errno) Timeout() bool

type Fbootstraptransfer_t struct {
	Offset int64
	Length uint64
	Buffer *byte
}

type FdSet struct {
	Bits [32]int32
}

type Flock_t struct {
	Start  int64
	Len    int64
	Pid    int32
	Type   int16
	Whence int16
}

type Fsid struct {
	Val [2]int32
}

type Fstore_t struct {
	Flags      uint32
	Posmode    int32
	Offset     int64
	Length     int64
	Bytesalloc int64
}

type ICMPv6Filter struct {
	Filt [8]uint32
}

type IPMreq struct {
	Multiaddr [4]byte /* in_addr */
	Interface [4]byte /* in_addr */
}

type IPv6MTUInfo struct {
	Addr RawSockaddrInet6
	Mtu  uint32
}

type IPv6Mreq struct {
	Multiaddr [16]byte /* in6_addr */
	Interface uint32
}

type IfData struct {
	Type       uint8
	Typelen    uint8
	Physical   uint8
	Addrlen    uint8
	Hdrlen     uint8
	Recvquota  uint8
	Xmitquota  uint8
	Unused1    uint8
	Mtu        uint32
	Metric     uint32
	Baudrate   uint32
	Ipackets   uint32
	Ierrors    uint32
	Opackets   uint32
	Oerrors    uint32
	Collisions uint32
	Ibytes     uint32
	Obytes     uint32
	Imcasts    uint32
	Omcasts    uint32
	Iqdrops    uint32
	Noproto    uint32
	Recvtiming uint32
	Xmittiming uint32
	Lastchange Timeval32
	Unused2    uint32
	Hwassist   uint32
	Reserved1  uint32
	Reserved2  uint32
}

type IfMsghdr struct {
	Msglen    uint16
	Version   uint8
	Type      uint8
	Addrs     int32
	Flags     int32
	Index     uint16
	Pad_cgo_0 [2]byte
	Data      IfData
}

type IfaMsghdr struct {
	Msglen    uint16
	Version   uint8
	Type      uint8
	Addrs     int32
	Flags     int32
	Index     uint16
	Pad_cgo_0 [2]byte
	Metric    int32
}

type IfmaMsghdr struct {
	Msglen    uint16
	Version   uint8
	Type      uint8
	Addrs     int32
	Flags     int32
	Index     uint16
	Pad_cgo_0 [2]byte
}

type IfmaMsghdr2 struct {
	Msglen    uint16
	Version   uint8
	Type      uint8
	Addrs     int32
	Flags     int32
	Index     uint16
	Pad_cgo_0 [2]byte
	Refcount  int32
}

type Inet4Pktinfo struct {
	Ifindex  uint32
	Spec_dst [4]byte /* in_addr */
	Addr     [4]byte /* in_addr */
}

type Inet6Pktinfo struct {
	Addr    [16]byte /* in6_addr */
	Ifindex uint32
}

type InterfaceAddrMessage struct {
	Header IfaMsghdr
	Data   []byte
}
    InterfaceAddrMessage represents a routing message containing network
    interface address entries.

    Deprecated: Use golang.org/x/net/route instead.

type InterfaceMessage struct {
	Header IfMsghdr
	Data   []byte
}
    InterfaceMessage represents a routing message containing network interface
    entries.

    Deprecated: Use golang.org/x/net/route instead.

type InterfaceMulticastAddrMessage struct {
	Header IfmaMsghdr2
	Data   []byte
}
    InterfaceMulticastAddrMessage represents a routing message containing
    network interface address entries.

    Deprecated: Use golang.org/x/net/route instead.

type Iovec struct {
	Base *byte
	Len  uint64
}

func (iov *Iovec) SetLen(length int)

type Kevent_t struct {
	Ident  uint64
	Filter int16
	Flags  uint16
	Fflags uint32
	Data   int64
	Udata  *byte
}

type Linger struct {
	Onoff  int32
	Linger int32
}

type Log2phys_t struct {
	Flags       uint32
	Contigbytes int64
	Devoffset   int64
}

type Msghdr struct {
	Name       *byte
	Namelen    uint32
	Pad_cgo_0  [4]byte
	Iov        *Iovec
	Iovlen     int32
	Pad_cgo_1  [4]byte
	Control    *byte
	Controllen uint32
	Flags      int32
}

func (msghdr *Msghdr) SetControllen(length int)

type ProcAttr struct {
	Dir   string    // Current working directory.
	Env   []string  // Environment.
	Files []uintptr // File descriptors.
	Sys   *SysProcAttr
}
    ProcAttr holds attributes that will be applied to a new process started by
    StartProcess.

type Radvisory_t struct {
	Offset    int64
	Count     int32
	Pad_cgo_0 [4]byte
}

type RawConn interface {
	// Control invokes f on the underlying connection's file
	// descriptor or handle.
	// The file descriptor fd is guaranteed to remain valid while
	// f executes but not after f returns.
	Control(f func(fd uintptr)) error

	// Read invokes f on the underlying connection's file
	// descriptor or handle; f is expected to try to read from the
	// file descriptor.
	// If f returns true, Read returns. Otherwise Read blocks
	// waiting for the connection to be ready for reading and
	// tries again repeatedly.
	// The file descriptor is guaranteed to remain valid while f
	// executes but not after f returns.
	Read(f func(fd uintptr) (done bool)) error

	// Write is like Read but for writing.
	Write(f func(fd uintptr) (done bool)) error
}
    A RawConn is a raw network connection.

type RawSockaddr struct {
	Len    uint8
	Family uint8
	Data   [14]int8
}

type RawSockaddrAny struct {
	Addr RawSockaddr
	Pad  [92]int8
}

type RawSockaddrDatalink struct {
	Len    uint8
	Family uint8
	Index  uint16
	Type   uint8
	Nlen   uint8
	Alen   uint8
	Slen   uint8
	Data   [12]int8
}

type RawSockaddrInet4 struct {
	Len    uint8
	Family uint8
	Port   uint16
	Addr   [4]byte /* in_addr */
	Zero   [8]int8
}

type RawSockaddrInet6 struct {
	Len      uint8
	Family   uint8
	Port     uint16
	Flowinfo uint32
	Addr     [16]byte /* in6_addr */
	Scope_id uint32
}

type RawSockaddrUnix struct {
	Len    uint8
	Family uint8
	Path   [104]int8
}

type Rlimit struct {
	Cur uint64
	Max uint64
}

type RouteMessage struct {
	Header RtMsghdr
	Data   []byte
}
    RouteMessage represents a routing message containing routing entries.

    Deprecated: Use golang.org/x/net/route instead.

type RoutingMessage interface {
	// Has unexported methods.
}
    RoutingMessage represents a routing message.

    Deprecated: Use golang.org/x/net/route instead.

type RtMetrics struct {
	Locks    uint32
	Mtu      uint32
	Hopcount uint32
	Expire   int32
	Recvpipe uint32
	Sendpipe uint32
	Ssthresh uint32
	Rtt      uint32
	Rttvar   uint32
	Pksent   uint32
	Filler   [4]uint32
}

type RtMsghdr struct {
	Msglen    uint16
	Version   uint8
	Type      uint8
	Index     uint16
	Pad_cgo_0 [2]byte
	Flags     int32
	Addrs     int32
	Pid       int32
	Seq       int32
	Errno     int32
	Use       int32
	Inits     uint32
	Rmx       RtMetrics
}

type Rusage struct {
	Utime    Timeval
	Stime    Timeval
	Maxrss   int64
	Ixrss    int64
	Idrss    int64
	Isrss    int64
	Minflt   int64
	Majflt   int64
	Nswap    int64
	Inblock  int64
	Oublock  int64
	Msgsnd   int64
	Msgrcv   int64
	Nsignals int64
	Nvcsw    int64
	Nivcsw   int64
}

type Signal int
    A Signal is a number describing a process signal. It implements the
    os.Signal interface.

func (s Signal) Signal()

func (s Signal) String() string

type Sockaddr interface {
	// Has unexported methods.
}

type SockaddrDatalink struct {
	Len    uint8
	Family uint8
	Index  uint16
	Type   uint8
	Nlen   uint8
	Alen   uint8
	Slen   uint8
	Data   [12]int8
	// Has unexported fields.
}

type SockaddrInet4 struct {
	Port int
	Addr [4]byte
	// Has unexported fields.
}

type SockaddrInet6 struct {
	Port   int
	ZoneId uint32
	Addr   [16]byte
	// Has unexported fields.
}

type SockaddrUnix struct {
	Name string
	// Has unexported fields.
}

type SocketControlMessage struct {
	Header Cmsghdr
	Data   []byte
}
    SocketControlMessage represents a socket control message.

type Stat_t struct {
	Dev           int32
	Mode          uint16
	Nlink         uint16
	Ino           uint64
	Uid           uint32
	Gid           uint32
	Rdev          int32
	Pad_cgo_0     [4]byte
	Atimespec     Timespec
	Mtimespec     Timespec
	Ctimespec     Timespec
	Birthtimespec Timespec
	Size          int64
	Blocks        int64
	Blksize       int32
	Flags         uint32
	Gen           uint32
	Lspare        int32
	Qspare        [2]int64
}

type Statfs_t struct {
	Bsize       uint32
	Iosize      int32
	Blocks      uint64
	Bfree       uint64
	Bavail      uint64
	Files       uint64
	Ffree       uint64
	Fsid        Fsid
	Owner       uint32
	Type        uint32
	Flags       uint32
	Fssubtype   uint32
	Fstypename  [16]int8
	Mntonname   [1024]int8
	Mntfromname [1024]int8
	Reserved    [8]uint32
}

type SysProcAttr struct {
	Chroot     string      // Chroot.
	Credential *Credential // Credential.
	Ptrace     bool        // Enable tracing.
	Setsid     bool        // Create session.
	// Setpgid sets the process group ID of the child to Pgid,
	// or, if Pgid == 0, to the new child's process ID.
	Setpgid bool
	// Setctty sets the controlling terminal of the child to
	// file descriptor Ctty. Ctty must be a descriptor number
	// in the child process: an index into ProcAttr.Files.
	// This is only meaningful if Setsid is true.
	Setctty bool
	Noctty  bool // Detach fd 0 from controlling terminal
	Ctty    int  // Controlling TTY fd
	// Foreground places the child process group in the foreground.
	// This implies Setpgid. The Ctty field must be set to
	// the descriptor of the controlling TTY.
	// Unlike Setctty, in this case Ctty must be a descriptor
	// number in the parent process.
	Foreground bool
	Pgid       int // Child's process group ID if Setpgid.
}

type Termios struct {
	Iflag     uint64
	Oflag     uint64
	Cflag     uint64
	Lflag     uint64
	Cc        [20]uint8
	Pad_cgo_0 [4]byte
	Ispeed    uint64
	Ospeed    uint64
}

type Timespec struct {
	Sec  int64
	Nsec int64
}

func NsecToTimespec(nsec int64) Timespec
    NsecToTimespec converts a number of nanoseconds into a Timespec.

func (ts *Timespec) Nano() int64
    Nano returns the time stored in ts as nanoseconds.

func (ts *Timespec) Unix() (sec int64, nsec int64)
    Unix returns the time stored in ts as seconds plus nanoseconds.

type Timeval struct {
	Sec       int64
	Usec      int32
	Pad_cgo_0 [4]byte
}

func NsecToTimeval(nsec int64) Timeval
    NsecToTimeval converts a number of nanoseconds into a Timeval.

func (tv *Timeval) Nano() int64
    Nano returns the time stored in tv as nanoseconds.

func (tv *Timeval) Unix() (sec int64, nsec int64)
    Unix returns the time stored in tv as seconds plus nanoseconds.

type Timeval32 struct {
	Sec  int32
	Usec int32
}

type WaitStatus uint32

func (w WaitStatus) Continued() bool

func (w WaitStatus) CoreDump() bool

func (w WaitStatus) ExitStatus() int

func (w WaitStatus) Exited() bool

func (w WaitStatus) Signal() Signal

func (w WaitStatus) Signaled() bool

func (w WaitStatus) StopSignal() Signal

func (w WaitStatus) Stopped() bool

func (w WaitStatus) TrapCause() int

