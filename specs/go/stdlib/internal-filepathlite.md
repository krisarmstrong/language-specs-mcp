package filepathlite // import "internal/filepathlite"

Package filepathlite implements a subset of path/filepath, only using packages
which may be imported by "os".

Tests for these functions are in path/filepath.

CONSTANTS

const (
	Separator     = '/' // OS-specific path separator
	ListSeparator = ':' // OS-specific path list separator
)

FUNCTIONS

func Base(path string) string
    Base is filepath.Base.

func Clean(path string) string
    Clean is filepath.Clean.

func Dir(path string) string
    Dir is filepath.Dir.

func Ext(path string) string
    Ext is filepath.Ext.

func FromSlash(path string) string
    FromSlash is filepath.FromSlash.

func IsAbs(path string) bool
    IsAbs reports whether the path is absolute.

func IsLocal(path string) bool
    IsLocal is filepath.IsLocal.

func IsPathSeparator(c uint8) bool
func Localize(path string) (string, error)
    Localize is filepath.Localize.

func Split(path string) (dir, file string)
    Split is filepath.Split.

func ToSlash(path string) string
    ToSlash is filepath.ToSlash.

func VolumeName(path string) string
    VolumeName is filepath.VolumeName.

func VolumeNameLen(path string) int
    VolumeNameLen returns the length of the leading volume name on Windows.
    It returns 0 elsewhere.

