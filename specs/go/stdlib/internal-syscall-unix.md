package unix // import "internal/syscall/unix"


CONSTANTS

const (
	AT_EACCESS          = 0x10
	AT_FDCWD            = -0x2
	AT_REMOVEDIR        = 0x80
	AT_SYMLINK_NOFOLLOW = 0x0020

	UTIME_OMIT = -0x2
)
const (
	R_OK = 0x4
	W_OK = 0x2
	X_OK = 0x1

	// NoFollowErrno is the error returned from open/openat called with
	// O_NOFOLLOW flag, when the trailing component (basename) of the path
	// is a symbolic link.
	NoFollowErrno = noFollowErrno
)
const (
	AI_CANONNAME = 0x2
	AI_ALL       = 0x100
	AI_V4MAPPED  = 0x800
	AI_MASK      = 0x1407

	EAI_ADDRFAMILY = 1
	EAI_AGAIN      = 2
	EAI_NODATA     = 7
	EAI_NONAME     = 8
	EAI_SERVICE    = 9
	EAI_SYSTEM     = 11
	EAI_OVERFLOW   = 14

	NI_NAMEREQD = 4
)
const (
	SC_GETGR_R_SIZE_MAX = 0x46
	SC_GETPW_R_SIZE_MAX = 0x47
)

FUNCTIONS

func ARC4Random(p []byte)
    ARC4Random calls the macOS arc4random_buf(3) function.

func Eaccess(path string, mode uint32) error
func Fchmodat(dirfd int, path string, mode uint32, flags int) error
func Fchownat(dirfd int, path string, uid, gid int, flags int) error
func Fcntl(fd int, cmd int, arg int) (int, error)
func Freeaddrinfo(ai *Addrinfo)
func Fstatat(dirfd int, path string, stat *syscall.Stat_t, flags int) error
func GaiStrerror(ecode int) string
func Getaddrinfo(hostname, servname *byte, hints *Addrinfo, res **Addrinfo) (int, error)
func Getgrgid(gid uint32, grp *Group, buf *byte, size uintptr, result **Group) syscall.Errno
func Getgrnam(name *byte, grp *Group, buf *byte, size uintptr, result **Group) syscall.Errno
func Getgrouplist(name *byte, gid uint32, gids *uint32, n *int32) error
func Getnameinfo(sa *syscall.RawSockaddr, salen int, host *byte, hostlen int, serv *byte, servlen int, flags int) (int, error)
func Getpwnam(name *byte, pwd *Passwd, buf *byte, size uintptr, result **Passwd) syscall.Errno
func Getpwuid(uid uint32, pwd *Passwd, buf *byte, size uintptr, result **Passwd) syscall.Errno
func GoString(p *byte) string
func Grantpt(fd int) error
func HasNonblockFlag(flag int) bool
func IsNonblock(fd int) (nonblocking bool, err error)
func KernelVersion() (major int, minor int)
func Linkat(olddirfd int, oldpath string, newdirfd int, newpath string, flag int) error
func Mkdirat(dirfd int, path string, mode uint32) error
func Openat(dirfd int, path string, flags int, perm uint32) (int, error)
func PosixOpenpt(flag int) (fd int, err error)
func Ptsname(fd int) (string, error)
func Readlinkat(dirfd int, path string, buf []byte) (int, error)
func RecvfromInet4(fd int, p []byte, flags int, from *syscall.SockaddrInet4) (int, error)
func RecvfromInet6(fd int, p []byte, flags int, from *syscall.SockaddrInet6) (n int, err error)
func RecvmsgInet4(fd int, p, oob []byte, flags int, from *syscall.SockaddrInet4) (n, oobn int, recvflags int, err error)
func RecvmsgInet6(fd int, p, oob []byte, flags int, from *syscall.SockaddrInet6) (n, oobn int, recvflags int, err error)
func Renameat(olddirfd int, oldpath string, newdirfd int, newpath string) error
func ResNclose(state *ResState)
func ResNinit(state *ResState) error
func ResNsearch(state *ResState, dname *byte, class, typ int, ans *byte, anslen int) (int, error)
func SendmsgNInet4(fd int, p, oob []byte, to *syscall.SockaddrInet4, flags int) (n int, err error)
func SendmsgNInet6(fd int, p, oob []byte, to *syscall.SockaddrInet6, flags int) (n int, err error)
func SendtoInet4(fd int, p []byte, flags int, to *syscall.SockaddrInet4) (err error)
func SendtoInet6(fd int, p []byte, flags int, to *syscall.SockaddrInet6) (err error)
func Symlinkat(oldpath string, newdirfd int, newpath string) error
func Sysconf(key int32) int64
func Tcsetpgrp(fd int, pgid int32) (err error)
func Unlinkat(dirfd int, path string, flags int) error
func Unlockpt(fd int) error
func Utimensat(dirfd int, path string, times *[2]syscall.Timespec, flag int) error

TYPES

type Addrinfo struct {
	Flags     int32
	Family    int32
	Socktype  int32
	Protocol  int32
	Addrlen   uint32
	Canonname *byte
	Addr      *syscall.RawSockaddr
	Next      *Addrinfo
}

type Group struct {
	Name   *byte
	Passwd *byte
	Gid    uint32 // gid_t
	Mem    **byte
}

type Passwd struct {
	Name   *byte
	Passwd *byte
	Uid    uint32 // uid_t
	Gid    uint32 // gid_t
	Change int64  // time_t
	Class  *byte
	Gecos  *byte
	Dir    *byte
	Shell  *byte
	Expire int64 // time_t
}

type ResState struct {
	// Has unexported fields.
}

