# JET.jl

JET.jl is a code analyzer for Julia that detects bugs and type instabilities.

Version: 0.9
Source: https://github.com/aviatesk/JET.jl

## Installation

```julia
using Pkg
Pkg.add("JET")
```

## Usage

```julia
using JET

# Analyze a function call
@report_call sum([1, 2, 3])

# Analyze with test inputs
report_call(sum, (Vector{Int},))

# Analyze a file
report_file("script.jl")

# Analyze a package
report_package("MyPackage")
```

## Analysis Types

### Error Analysis
Detects potential runtime errors:
- Method errors (no matching method)
- Undefined variable access
- Type assertion failures
- Bounds errors

### Optimization Analysis
Detects type instabilities:

```julia
@report_opt sum([1, 2, 3])
```

## Configuration

```julia
# Custom analysis
report_call(
    my_function,
    (Int, String);
    mode = :sound,           # :sound or :typo
    target_modules = (Main,)
)
```

### Analysis Modes

#### :sound
Stricter analysis, may report more issues.

#### :typo (default)
Balanced analysis, focuses on likely errors.

## Error Types Detected

### MethodError
No method matching the given types.

```julia
# Will detect
f(x::Int) = x
f("string")  # No method for String
```

### UndefVarError
Access to undefined variables.

### TypeError
Type assertion failures.

### BoundsError
Array index out of bounds (limited detection).

### DivideError
Division by zero (constant cases).

## Optimization Issues

### Type Instability
Function return type varies based on runtime values.

```julia
# Type unstable
function unstable(x)
    if x > 0
        return 1
    else
        return 1.0  # Returns Int or Float64
    end
end
```

### Runtime Dispatch
Dynamic dispatch due to unclear types.

## Integration

### VS Code
Julia extension shows JET diagnostics.

### CI/CD
```julia
using JET

# Fail CI on errors
result = report_package("MyPackage")
@assert isempty(get_reports(result))
```

## Suppressing Warnings

```julia
# JET.jl respects `@assume_effects` and other compiler hints
Base.@assume_effects :nothrow function safe_function()
    # ...
end
```

## StaticLint.jl

Another Julia linter focused on style:

```julia
using StaticLint
StaticLint.lint_file("script.jl")
```

### StaticLint Checks
- Unused variables
- Missing docstrings
- Style issues
- Import analysis
