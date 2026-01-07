# Julia Generation Checklist

**Read this BEFORE writing Julia code. Type stability and performance matter.**

## Critical: You Must Do These

### 1. Write Type-Stable Functions
```julia
# BAD - type unstable (returns different types)
function bad_abs(x)
    if x > 0
        return x
    else
        return -x  # Could be different type if x is unsigned
    end
end

# GOOD - type stable
function good_abs(x::T) where T <: Number
    return x > zero(T) ? x : -x
end

# Check type stability with @code_warntype
@code_warntype good_abs(-5)
```

### 2. Avoid Global Variables in Performance-Critical Code
```julia
# BAD - global variable causes type instability
x = 10
function bad_compute()
    return x * 2  # x type unknown at compile time
end

# GOOD - pass as argument
function good_compute(x)
    return x * 2
end

# GOOD - const for truly constant globals
const CONFIG_VALUE = 10
function compute_with_const()
    return CONFIG_VALUE * 2  # OK - type is known
end
```

### 3. Pre-allocate Arrays
```julia
# BAD - growing array
function bad_squares(n)
    result = []
    for i in 1:n
        push!(result, i^2)
    end
    return result
end

# GOOD - pre-allocated with type
function good_squares(n)
    result = Vector{Int}(undef, n)
    for i in 1:n
        result[i] = i^2
    end
    return result
end

# BETTER - comprehension
squares(n) = [i^2 for i in 1:n]
```

### 4. Use Broadcasting with Dot Syntax
```julia
# BAD - explicit loop
function add_arrays_bad(a, b)
    result = similar(a)
    for i in eachindex(a)
        result[i] = a[i] + b[i]
    end
    return result
end

# GOOD - broadcasting
add_arrays(a, b) = a .+ b

# GOOD - fused broadcasting (single loop, no temporaries)
result = @. sin(x) + cos(y) * z
# Equivalent to: sin.(x) .+ cos.(y) .* z
```

### 5. Use Multiple Dispatch Properly
```julia
# GOOD - leverage Julia's strength
abstract type Shape end

struct Circle <: Shape
    radius::Float64
end

struct Rectangle <: Shape
    width::Float64
    height::Float64
end

# Method for each type
area(c::Circle) = π * c.radius^2
area(r::Rectangle) = r.width * r.height

# Generic function works with any Shape
total_area(shapes::Vector{<:Shape}) = sum(area, shapes)
```

## Important: Strong Recommendations

### 6. Use Concrete Types in Struct Fields
```julia
# BAD - abstract field type
struct BadContainer
    data::AbstractVector  # Type instability
end

# GOOD - parametric type
struct GoodContainer{T<:AbstractVector}
    data::T
end

# Or concrete type if known
struct IntContainer
    data::Vector{Int}
end
```

### 7. Use `@views` for Slicing Without Copies
```julia
# BAD - creates copy
function process_slice(A)
    B = A[1:100, :]  # Allocates new array
    return sum(B)
end

# GOOD - view (no allocation)
function process_slice_view(A)
    B = @view A[1:100, :]  # No copy
    return sum(B)
end

# GOOD - @views macro for block
function process_views(A)
    @views begin
        x = A[1:10]
        y = A[11:20]
        return x .+ y
    end
end
```

### 8. Use `eachindex` and `axes` for Iteration
```julia
# BAD - assumes 1-based indexing
for i in 1:length(A)
    A[i] = i
end

# GOOD - works with any array type
for i in eachindex(A)
    A[i] = i
end

# GOOD - multi-dimensional
for i in axes(A, 1), j in axes(A, 2)
    A[i, j] = i + j
end
```

### 9. Use Named Tuples and Keyword Arguments
```julia
# BAD - positional args hard to remember
function create_user(name, email, age, active, role)
    # What order?
end

# GOOD - keyword arguments
function create_user(; name, email, age=0, active=true, role="user")
    return (; name, email, age, active, role)  # Named tuple
end

user = create_user(name="Alice", email="a@b.com")
```

### 10. Use `nothing` and Union Types for Optional Values
```julia
# GOOD - explicit optional
function find_user(id::Int)::Union{User, Nothing}
    # Returns User or nothing
end

# Check with isnothing
user = find_user(123)
if !isnothing(user)
    println(user.name)
end

# Or with pattern
result = something(find_user(123), default_user)
```

## Performance

### 11. Use `@inbounds` for Hot Loops (Carefully)
```julia
# GOOD - when you've verified bounds are safe
function sum_array(A)
    s = zero(eltype(A))
    @inbounds for i in eachindex(A)
        s += A[i]
    end
    return s
end

# CAUTION: Only use when you're certain indices are valid
```

### 12. Use `@simd` for Vectorizable Loops
```julia
# GOOD - enables SIMD optimization
function dot_product(a, b)
    s = zero(eltype(a))
    @simd for i in eachindex(a)
        @inbounds s += a[i] * b[i]
    end
    return s
end
```

### 13. Profile Before Optimizing
```julia
# Use built-in profiling
using Profile

@profile my_function(args)
Profile.print()

# Use BenchmarkTools for timing
using BenchmarkTools

@btime my_function($args)  # $ interpolates to avoid globals
@benchmark my_function($args)
```

### 14. Use StaticArrays for Small Fixed-Size Arrays
```julia
using StaticArrays

# GOOD - stack-allocated, very fast for small arrays
function compute_3d(v::SVector{3, Float64})
    return v[1]^2 + v[2]^2 + v[3]^2
end

v = SVector(1.0, 2.0, 3.0)
```

## Best Practices

### 15. Use Modules for Code Organization
```julia
module MyModule

export public_function

# Private - not exported
function helper()
    # ...
end

# Public
function public_function(x)
    return helper() + x
end

end # module
```

### 16. Handle Errors with Exceptions
```julia
# GOOD - custom exception types
struct ValidationError <: Exception
    msg::String
end

function validate(x)
    x > 0 || throw(ValidationError("x must be positive"))
    return x
end

# Handle errors
try
    validate(-1)
catch e
    if e isa ValidationError
        println("Validation failed: ", e.msg)
    else
        rethrow()
    end
end
```

---

**Quick Reference - Copy This Mental Model:**
- Type-stable functions (check with @code_warntype)
- Avoid globals (or use `const`)
- Pre-allocate arrays with types
- Dot broadcasting (`.+`, `@.`)
- Multiple dispatch for polymorphism
- Concrete types in struct fields
- `@views` for slicing
- `eachindex` for iteration
- Keyword arguments for clarity
- `Union{T, Nothing}` for optionals
- `@inbounds` and `@simd` for hot loops
- BenchmarkTools for profiling
- StaticArrays for small fixed arrays
