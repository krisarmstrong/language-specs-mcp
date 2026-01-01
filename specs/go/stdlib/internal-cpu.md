package cpu // import "internal/cpu"

Package cpu implements processor feature detection used by the Go standard
library.

CONSTANTS

const CacheLinePadSize = 128
    CacheLinePadSize is used to prevent false sharing of cache lines. We
    choose 128 because Apple Silicon, a.k.a. M1, has 128-byte cache line size.
    It doesn't cost much and is much more future-proof.


VARIABLES

var ARM struct {
	_            CacheLinePad
	HasVFPv4     bool
	HasIDIVA     bool
	HasV7Atomics bool
	_            CacheLinePad
}
    The booleans in ARM contain the correspondingly named cpu feature bit.
    The struct is padded to avoid false sharing.

var ARM64 struct {
	_          CacheLinePad
	HasAES     bool
	HasPMULL   bool
	HasSHA1    bool
	HasSHA2    bool
	HasSHA512  bool
	HasSHA3    bool
	HasCRC32   bool
	HasATOMICS bool
	HasCPUID   bool
	HasDIT     bool
	IsNeoverse bool
	_          CacheLinePad
}
    The booleans in ARM64 contain the correspondingly named cpu feature bit.
    The struct is padded to avoid false sharing.

var CacheLineSize uintptr = CacheLinePadSize
    CacheLineSize is the CPU's assumed cache line size. There is currently no
    runtime detection of the real cache line size so we use the constant per
    GOARCH CacheLinePadSize as an approximation.

var DebugOptions bool
    DebugOptions is set to true by the runtime if the OS supports reading
    GODEBUG early in runtime startup. This should not be changed after it is
    initialized.

var Loong64 struct {
	_         CacheLinePad
	HasLSX    bool // support 128-bit vector extension
	HasLASX   bool // support 256-bit vector extension
	HasCRC32  bool // support CRC instruction
	HasLAMCAS bool // support AMCAS[_DB].{B/H/W/D}
	HasLAM_BH bool // support AM{SWAP/ADD}[_DB].{B/H} instruction
	_         CacheLinePad
}
    The booleans in Loong64 contain the correspondingly named cpu feature bit.
    The struct is padded to avoid false sharing.

var MIPS64X struct {
	_      CacheLinePad
	HasMSA bool // MIPS SIMD architecture
	_      CacheLinePad
}
var PPC64 struct {
	_         CacheLinePad
	HasDARN   bool // Hardware random number generator (requires kernel enablement)
	HasSCV    bool // Syscall vectored (requires kernel enablement)
	IsPOWER8  bool // ISA v2.07 (POWER8)
	IsPOWER9  bool // ISA v3.00 (POWER9)
	IsPOWER10 bool // ISA v3.1  (POWER10)
	_         CacheLinePad
}
    For ppc64(le), it is safe to check only for ISA level starting on ISA v3.00,
    since there are no optional categories. There are some exceptions that
    also require kernel support to work (darn, scv), so there are feature bits
    for those as well. The minimum processor requirement is POWER8 (ISA 2.07).
    The struct is padded to avoid false sharing.

var RISCV64 struct {
	_                 CacheLinePad
	HasFastMisaligned bool // Fast misaligned accesses
	HasV              bool // Vector extension compatible with RVV 1.0
	HasZbb            bool // Basic bit-manipulation extension
	_                 CacheLinePad
}
    RISCV64 contains the supported CPU features and performance characteristics
    for riscv64 platforms. The booleans in RISCV64, with the exception of
    HasFastMisaligned, indicate the presence of RISC-V extensions. The struct is
    padded to avoid false sharing.

var S390X struct {
	_         CacheLinePad
	HasZARCH  bool // z architecture mode is active [mandatory]
	HasSTFLE  bool // store facility list extended [mandatory]
	HasLDISP  bool // long (20-bit) displacements [mandatory]
	HasEIMM   bool // 32-bit immediates [mandatory]
	HasDFP    bool // decimal floating point
	HasETF3EH bool // ETF-3 enhanced
	HasMSA    bool // message security assist (CPACF)
	HasAES    bool // KM-AES{128,192,256} functions
	HasAESCBC bool // KMC-AES{128,192,256} functions
	HasAESCTR bool // KMCTR-AES{128,192,256} functions
	HasAESGCM bool // KMA-GCM-AES{128,192,256} functions
	HasGHASH  bool // KIMD-GHASH function
	HasSHA1   bool // K{I,L}MD-SHA-1 functions
	HasSHA256 bool // K{I,L}MD-SHA-256 functions
	HasSHA512 bool // K{I,L}MD-SHA-512 functions
	HasSHA3   bool // K{I,L}MD-SHA3-{224,256,384,512} and K{I,L}MD-SHAKE-{128,256} functions
	HasVX     bool // vector facility. Note: the runtime sets this when it processes auxv records.
	HasVXE    bool // vector-enhancements facility 1
	HasKDSA   bool // elliptic curve functions
	HasECDSA  bool // NIST curves
	HasEDDSA  bool // Edwards curves
	_         CacheLinePad
}
var X86 struct {
	_            CacheLinePad
	HasAES       bool
	HasADX       bool
	HasAVX       bool
	HasAVX2      bool
	HasAVX512F   bool
	HasAVX512BW  bool
	HasAVX512VL  bool
	HasBMI1      bool
	HasBMI2      bool
	HasERMS      bool
	HasFSRM      bool
	HasFMA       bool
	HasOSXSAVE   bool
	HasPCLMULQDQ bool
	HasPOPCNT    bool
	HasRDTSCP    bool
	HasSHA       bool
	HasSSE3      bool
	HasSSSE3     bool
	HasSSE41     bool
	HasSSE42     bool
	_            CacheLinePad
}
    The booleans in X86 contain the correspondingly named cpuid feature bit.
    HasAVX and HasAVX2 are only set if the OS does support XMM and YMM registers
    in addition to the cpuid feature bit being set. The struct is padded to
    avoid false sharing.


FUNCTIONS

func Initialize(env string)
    Initialize examines the processor and sets the relevant variables above.
    This is called by the runtime package early in program initialization,
    before normal init functions are run. env is set by runtime if the OS
    supports cpu feature options in GODEBUG.

func Name() string
    Name returns the CPU name given by the vendor if it can be read directly
    from memory or by CPU instructions. If the CPU name can not be determined an
    empty string is returned.

    Implementations that use the Operating System (e.g. sysctl or /sys/) to
    gather CPU information for display should be placed in internal/sysinfo.


TYPES

type CacheLinePad struct {
	// Has unexported fields.
}
    CacheLinePad is used to pad structs to avoid false sharing.

