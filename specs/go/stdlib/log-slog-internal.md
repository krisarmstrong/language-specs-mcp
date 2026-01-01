package internal // import "log/slog/internal"


VARIABLES

var IgnorePC = false
    If IgnorePC is true, do not invoke runtime.Callers to get the pc. This is
    solely for benchmarking the slowdown from runtime.Callers.

