# [Linear Algebra](#man-linalg)#man-linalg

In addition to (and as part of) its support for multi-dimensional arrays, Julia provides native implementations of many common and useful linear algebra operations which can be loaded with `using LinearAlgebra`. Basic operations, such as [tr](#LinearAlgebra.tr), [det](#LinearAlgebra.det), and [inv](../../base/math/#Base.inv-Tuple{Number}) are all supported:

```
julia> A = [1 2 3; 4 1 6; 7 8 1]
3×3 Matrix{Int64}:
 1  2  3
 4  1  6
 7  8  1

julia> tr(A)
3

julia> det(A)
104.0

julia> inv(A)
3×3 Matrix{Float64}:
 -0.451923   0.211538    0.0865385
  0.365385  -0.192308    0.0576923
  0.240385   0.0576923  -0.0673077
```

As well as other useful operations, such as finding eigenvalues or eigenvectors:

```
julia> A = [-4. -17.; 2. 2.]
2×2 Matrix{Float64}:
 -4.0  -17.0
  2.0    2.0

julia> eigvals(A)
2-element Vector{ComplexF64}:
 -1.0 - 5.0im
 -1.0 + 5.0im

julia> eigvecs(A)
2×2 Matrix{ComplexF64}:
  0.945905-0.0im        0.945905+0.0im
 -0.166924+0.278207im  -0.166924-0.278207im
```

In addition, Julia provides many [factorizations](#man-linalg-factorizations) which can be used to speed up problems such as linear solve or matrix exponentiation by pre-factorizing a matrix into a form more amenable (for performance or memory reasons) to the problem. See the documentation on [factorize](#LinearAlgebra.factorize) for more information. As an example:

```
julia> A = [1.5 2 -4; 3 -1 -6; -10 2.3 4]
3×3 Matrix{Float64}:
   1.5   2.0  -4.0
   3.0  -1.0  -6.0
 -10.0   2.3   4.0

julia> factorize(A)
LU{Float64, Matrix{Float64}, Vector{Int64}}
L factor:
3×3 Matrix{Float64}:
  1.0    0.0       0.0
 -0.15   1.0       0.0
 -0.3   -0.132196  1.0
U factor:
3×3 Matrix{Float64}:
 -10.0  2.3     4.0
   0.0  2.345  -3.4
   0.0  0.0    -5.24947
```

Since `A` is not Hermitian, symmetric, triangular, tridiagonal, or bidiagonal, an LU factorization may be the best we can do. Compare with:

```
julia> B = [1.5 2 -4; 2 -1 -3; -4 -3 5]
3×3 Matrix{Float64}:
  1.5   2.0  -4.0
  2.0  -1.0  -3.0
 -4.0  -3.0   5.0

julia> factorize(B)
BunchKaufman{Float64, Matrix{Float64}, Vector{Int64}}
D factor:
3×3 Tridiagonal{Float64, Vector{Float64}}:
 -1.64286   0.0   ⋅
  0.0      -2.8  0.0
   ⋅        0.0  5.0
U factor:
3×3 UnitUpperTriangular{Float64, Matrix{Float64}}:
 1.0  0.142857  -0.8
  ⋅   1.0       -0.6
  ⋅    ⋅         1.0
permutation:
3-element Vector{Int64}:
 1
 2
 3
```

Here, Julia was able to detect that `B` is in fact symmetric, and used a more appropriate factorization. Often it's possible to write more efficient code for a matrix that is known to have certain properties e.g. it is symmetric, or tridiagonal. Julia provides some special types so that you can "tag" matrices as having these properties. For instance:

```
julia> B = [1.5 2 -4; 2 -1 -3; -4 -3 5]
3×3 Matrix{Float64}:
  1.5   2.0  -4.0
  2.0  -1.0  -3.0
 -4.0  -3.0   5.0

julia> sB = Symmetric(B)
3×3 Symmetric{Float64, Matrix{Float64}}:
  1.5   2.0  -4.0
  2.0  -1.0  -3.0
 -4.0  -3.0   5.0
```

`sB` has been tagged as a matrix that's (real) symmetric, so for later operations we might perform on it, such as eigenfactorization or computing matrix-vector products, efficiencies can be found by only referencing half of it. For example:

```
julia> B = [1.5 2 -4; 2 -1 -3; -4 -3 5]
3×3 Matrix{Float64}:
  1.5   2.0  -4.0
  2.0  -1.0  -3.0
 -4.0  -3.0   5.0

julia> sB = Symmetric(B)
3×3 Symmetric{Float64, Matrix{Float64}}:
  1.5   2.0  -4.0
  2.0  -1.0  -3.0
 -4.0  -3.0   5.0

julia> x = [1; 2; 3]
3-element Vector{Int64}:
 1
 2
 3

julia> sB\x
3-element Vector{Float64}:
 -1.7391304347826084
 -1.1086956521739126
 -1.4565217391304346
```

The `\` operation here performs the linear solution. The left-division operator is pretty powerful and it's easy to write compact, readable code that is flexible enough to solve all sorts of systems of linear equations.

## [Special matrices](#Special-matrices)#Special-matrices

[Matrices with special symmetries and structures](https://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=3274) arise often in linear algebra and are frequently associated with various matrix factorizations. Julia features a rich collection of special matrix types, which allow for fast computation with specialized routines that are specially developed for particular matrix types.

The following tables summarize the types of special matrices that have been implemented in Julia, as well as whether hooks to various optimized methods for them in LAPACK are available.

TypeDescription[Symmetric](#LinearAlgebra.Symmetric)[Symmetric matrix](https://en.wikipedia.org/wiki/Symmetric_matrix)[Hermitian](#LinearAlgebra.Hermitian)[Hermitian matrix](https://en.wikipedia.org/wiki/Hermitian_matrix)[UpperTriangular](#LinearAlgebra.UpperTriangular)Upper [triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix)[UnitUpperTriangular](#LinearAlgebra.UnitUpperTriangular)Upper [triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix) with unit diagonal[LowerTriangular](#LinearAlgebra.LowerTriangular)Lower [triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix)[UnitLowerTriangular](#LinearAlgebra.UnitLowerTriangular)Lower [triangular matrix](https://en.wikipedia.org/wiki/Triangular_matrix) with unit diagonal[UpperHessenberg](#LinearAlgebra.UpperHessenberg)Upper [Hessenberg matrix](https://en.wikipedia.org/wiki/Hessenberg_matrix)[Tridiagonal](#LinearAlgebra.Tridiagonal)[Tridiagonal matrix](https://en.wikipedia.org/wiki/Tridiagonal_matrix)[SymTridiagonal](#LinearAlgebra.SymTridiagonal)Symmetric tridiagonal matrix[Bidiagonal](#LinearAlgebra.Bidiagonal)Upper/lower [bidiagonal matrix](https://en.wikipedia.org/wiki/Bidiagonal_matrix)[Diagonal](#LinearAlgebra.Diagonal)[Diagonal matrix](https://en.wikipedia.org/wiki/Diagonal_matrix)[UniformScaling](#LinearAlgebra.UniformScaling)[Uniform scaling operator](https://en.wikipedia.org/wiki/Uniform_scaling)

### [Elementary operations](#Elementary-operations)#Elementary-operations

Matrix type`+``-``*``\`Other functions with optimized methods[Symmetric](#LinearAlgebra.Symmetric)MV[inv](../../base/math/#Base.inv-Tuple{Number}), [sqrt](../../base/math/#Base.sqrt-Tuple{Number}), [cbrt](../../base/math/#Base.Math.cbrt-Tuple{AbstractFloat}), [exp](../../base/math/#Base.exp-Tuple{Float64})[Hermitian](#LinearAlgebra.Hermitian)MV[inv](../../base/math/#Base.inv-Tuple{Number}), [sqrt](../../base/math/#Base.sqrt-Tuple{Number}), [cbrt](../../base/math/#Base.Math.cbrt-Tuple{AbstractFloat}), [exp](../../base/math/#Base.exp-Tuple{Float64})[UpperTriangular](#LinearAlgebra.UpperTriangular)MVMV[inv](../../base/math/#Base.inv-Tuple{Number}), [det](#LinearAlgebra.det), [logdet](#LinearAlgebra.logdet)[UnitUpperTriangular](#LinearAlgebra.UnitUpperTriangular)MVMV[inv](../../base/math/#Base.inv-Tuple{Number}), [det](#LinearAlgebra.det), [logdet](#LinearAlgebra.logdet)[LowerTriangular](#LinearAlgebra.LowerTriangular)MVMV[inv](../../base/math/#Base.inv-Tuple{Number}), [det](#LinearAlgebra.det), [logdet](#LinearAlgebra.logdet)[UnitLowerTriangular](#LinearAlgebra.UnitLowerTriangular)MVMV[inv](../../base/math/#Base.inv-Tuple{Number}), [det](#LinearAlgebra.det), [logdet](#LinearAlgebra.logdet)[UpperHessenberg](#LinearAlgebra.UpperHessenberg)MM[inv](../../base/math/#Base.inv-Tuple{Number}), [det](#LinearAlgebra.det)[SymTridiagonal](#LinearAlgebra.SymTridiagonal)MMMSMV[eigmax](#LinearAlgebra.eigmax), [eigmin](#LinearAlgebra.eigmin)[Tridiagonal](#LinearAlgebra.Tridiagonal)MMMSMV[Bidiagonal](#LinearAlgebra.Bidiagonal)MMMSMV[Diagonal](#LinearAlgebra.Diagonal)MMMVMV[inv](../../base/math/#Base.inv-Tuple{Number}), [det](#LinearAlgebra.det), [logdet](#LinearAlgebra.logdet), [/](../../base/math/#Base.:/)[UniformScaling](#LinearAlgebra.UniformScaling)MMMVSMVS[/](../../base/math/#Base.:/)

Legend:

KeyDescriptionM (matrix)An optimized method for matrix-matrix operations is availableV (vector)An optimized method for matrix-vector operations is availableS (scalar)An optimized method for matrix-scalar operations is available

### [Matrix factorizations](#Matrix-factorizations)#Matrix-factorizations

Matrix typeLAPACK[eigen](#LinearAlgebra.eigen)[eigvals](#LinearAlgebra.eigvals)[eigvecs](#LinearAlgebra.eigvecs)[svd](#LinearAlgebra.svd)[svdvals](#LinearAlgebra.svdvals)[Symmetric](#LinearAlgebra.Symmetric)SYARI[Hermitian](#LinearAlgebra.Hermitian)HEARI[UpperTriangular](#LinearAlgebra.UpperTriangular)TRAAA[UnitUpperTriangular](#LinearAlgebra.UnitUpperTriangular)TRAAA[LowerTriangular](#LinearAlgebra.LowerTriangular)TRAAA[UnitLowerTriangular](#LinearAlgebra.UnitLowerTriangular)TRAAA[SymTridiagonal](#LinearAlgebra.SymTridiagonal)STAARIAV[Tridiagonal](#LinearAlgebra.Tridiagonal)GT[Bidiagonal](#LinearAlgebra.Bidiagonal)BDAA[Diagonal](#LinearAlgebra.Diagonal)DIA

Legend:

KeyDescriptionExampleA (all)An optimized method to find all the characteristic values and/or vectors is availablee.g. `eigvals(M)`R (range)An optimized method to find the `il`th through the `ih`th characteristic values are available`eigvals(M, il, ih)`I (interval)An optimized method to find the characteristic values in the interval [`vl`, `vh`] is available`eigvals(M, vl, vh)`V (vectors)An optimized method to find the characteristic vectors corresponding to the characteristic values `x=[x1, x2,...]` is available`eigvecs(M, x)`

### [The uniform scaling operator](#The-uniform-scaling-operator)#The-uniform-scaling-operator

A [UniformScaling](#LinearAlgebra.UniformScaling) operator represents a scalar times the identity operator, `λ*I`. The identity operator `I` is defined as a constant and is an instance of `UniformScaling`. The size of these operators are generic and match the other matrix in the binary operations [+](../../base/math/#Base.:+), [-](../../base/math/#Base.:--Tuple{Any}), [*](../../base/math/#Base.:*-Tuple{Any, Vararg{Any}}) and [\](../../base/math/#Base.:\\-Tuple{Any, Any}). For `A+I` and `A-I` this means that `A` must be square. Multiplication with the identity operator `I` is a noop (except for checking that the scaling factor is one) and therefore almost without overhead.

To see the `UniformScaling` operator in action:

```
julia> U = UniformScaling(2);

julia> a = [1 2; 3 4]
2×2 Matrix{Int64}:
 1  2
 3  4

julia> a + U
2×2 Matrix{Int64}:
 3  2
 3  6

julia> a * U
2×2 Matrix{Int64}:
 2  4
 6  8

julia> [a U]
2×4 Matrix{Int64}:
 1  2  2  0
 3  4  0  2

julia> b = [1 2 3; 4 5 6]
2×3 Matrix{Int64}:
 1  2  3
 4  5  6

julia> b - U
ERROR: DimensionMismatch: matrix is not square: dimensions are (2, 3)
Stacktrace:
[...]
```

If you need to solve many systems of the form `(A+μI)x = b` for the same `A` and different `μ`, it might be beneficial to first compute the Hessenberg factorization `F` of `A` via the [hessenberg](#LinearAlgebra.hessenberg) function. Given `F`, Julia employs an efficient algorithm for `(F+μ*I) \ b` (equivalent to `(A+μ*I)x \ b`) and related operations like determinants.

## [Matrix factorizations](#man-linalg-factorizations)#man-linalg-factorizations

[Matrix factorizations (a.k.a. matrix decompositions)](https://en.wikipedia.org/wiki/Matrix_decomposition) compute the factorization of a matrix into a product of matrices, and are one of the central concepts in (numerical) linear algebra.

The following table summarizes the types of matrix factorizations that have been implemented in Julia. Details of their associated methods can be found in the [Standard functions](#Standard-functions) section of the Linear Algebra documentation.

TypeDescription`BunchKaufman`Bunch-Kaufman factorization`Cholesky`[Cholesky factorization](https://en.wikipedia.org/wiki/Cholesky_decomposition)`CholeskyPivoted`[Pivoted](https://en.wikipedia.org/wiki/Pivot_element) Cholesky factorization`LDLt`[LDL(T) factorization](https://en.wikipedia.org/wiki/Cholesky_decomposition#LDL_decomposition)`LU`[LU factorization](https://en.wikipedia.org/wiki/LU_decomposition)`QR`[QR factorization](https://en.wikipedia.org/wiki/QR_decomposition)`QRCompactWY`Compact WY form of the QR factorization`QRPivoted`Pivoted [QR factorization](https://en.wikipedia.org/wiki/QR_decomposition)`LQ`[QR factorization](https://en.wikipedia.org/wiki/QR_decomposition) of `transpose(A)``Hessenberg`[Hessenberg decomposition](https://mathworld.wolfram.com/HessenbergDecomposition.html)`Eigen`[Spectral decomposition](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix)`GeneralizedEigen`[Generalized spectral decomposition](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix#Generalized_eigenvalue_problem)`SVD`[Singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition)`GeneralizedSVD`[Generalized SVD](https://en.wikipedia.org/wiki/Generalized_singular_value_decomposition#Higher_order_version)`Schur`[Schur decomposition](https://en.wikipedia.org/wiki/Schur_decomposition)`GeneralizedSchur`[Generalized Schur decomposition](https://en.wikipedia.org/wiki/Schur_decomposition#Generalized_Schur_decomposition)

Adjoints and transposes of [Factorization](#LinearAlgebra.Factorization) objects are lazily wrapped in `AdjointFactorization` and `TransposeFactorization` objects, respectively. Generically, transpose of real `Factorization`s are wrapped as `AdjointFactorization`.

## [Orthogonal matrices (AbstractQ)](#man-linalg-abstractq)#man-linalg-abstractq

Some matrix factorizations generate orthogonal/unitary "matrix" factors. These factorizations include QR-related factorizations obtained from calls to [qr](#LinearAlgebra.qr), i.e., `QR`, `QRCompactWY` and `QRPivoted`, the Hessenberg factorization obtained from calls to [hessenberg](#LinearAlgebra.hessenberg), and the LQ factorization obtained from [lq](#LinearAlgebra.lq). While these orthogonal/unitary factors admit a matrix representation, their internal representation is, for performance and memory reasons, different. Hence, they should be rather viewed as matrix-backed, function-based linear operators. In particular, reading, for instance, a column of its matrix representation requires running "matrix"-vector multiplication code, rather than simply reading out data from memory (possibly filling parts of the vector with structural zeros). Another clear distinction from other, non-triangular matrix types is that the underlying multiplication code allows for in-place modification during multiplication. Furthermore, objects of specific `AbstractQ` subtypes as those created via [qr](#LinearAlgebra.qr), [hessenberg](#LinearAlgebra.hessenberg) and [lq](#LinearAlgebra.lq) can behave like a square or a rectangular matrix depending on context:

```
julia> using LinearAlgebra

julia> Q = qr(rand(3,2)).Q
3×3 LinearAlgebra.QRCompactWYQ{Float64, Matrix{Float64}, Matrix{Float64}}

julia> Matrix(Q)
3×2 Matrix{Float64}:
 -0.320597   0.865734
 -0.765834  -0.475694
 -0.557419   0.155628

julia> Q*I
3×3 Matrix{Float64}:
 -0.320597   0.865734  -0.384346
 -0.765834  -0.475694  -0.432683
 -0.557419   0.155628   0.815514

julia> Q*ones(2)
3-element Vector{Float64}:
  0.5451367118802273
 -1.241527373086654
 -0.40179067589600226

julia> Q*ones(3)
3-element Vector{Float64}:
  0.16079054743832022
 -1.674209978965636
  0.41372375588835797

julia> ones(1,2) * Q'
1×3 Matrix{Float64}:
 0.545137  -1.24153  -0.401791

julia> ones(1,3) * Q'
1×3 Matrix{Float64}:
 0.160791  -1.67421  0.413724
```

Due to this distinction from dense or structured matrices, the abstract `AbstractQ` type does not subtype `AbstractMatrix`, but instead has its own type hierarchy. Custom types that subtype `AbstractQ` can rely on generic fallbacks if the following interface is satisfied. For example, for

```
struct MyQ{T} <: LinearAlgebra.AbstractQ{T}
    # required fields
end
```

provide overloads for

```
Base.size(Q::MyQ) # size of corresponding square matrix representation
Base.convert(::Type{AbstractQ{T}}, Q::MyQ) # eltype promotion [optional]
LinearAlgebra.lmul!(Q::MyQ, x::AbstractVecOrMat) # left-multiplication
LinearAlgebra.rmul!(A::AbstractMatrix, Q::MyQ) # right-multiplication
```

If `eltype` promotion is not of interest, the `convert` method is unnecessary, since by default `convert(::Type{AbstractQ{T}}, Q::AbstractQ{T})` returns `Q` itself. Adjoints of `AbstractQ`-typed objects are lazily wrapped in an `AdjointQ` wrapper type, which requires its own `LinearAlgebra.lmul!` and `LinearAlgebra.rmul!` methods. Given this set of methods, any `Q::MyQ` can be used like a matrix, preferably in a multiplicative context: multiplication via `*` with scalars, vectors and matrices from left and right, obtaining a matrix representation of `Q` via `Matrix(Q)` (or `Q*I`) and indexing into the matrix representation all work. In contrast, addition and subtraction as well as more generally broadcasting over elements in the matrix representation fail because that would be highly inefficient. For such use cases, consider computing the matrix representation up front and cache it for future reuse.

## [Pivoting Strategies](#man-linalg-pivoting-strategies)#man-linalg-pivoting-strategies

Several of Julia's [matrix factorizations](#man-linalg-factorizations) support [pivoting](https://en.wikipedia.org/wiki/Pivot_element), which can be used to improve their numerical stability. In fact, some matrix factorizations, such as the LU factorization, may fail without pivoting.

In pivoting, first, a [pivot element](https://en.wikipedia.org/wiki/Pivot_element) with good numerical properties is chosen based on a pivoting strategy. Next, the rows and columns of the original matrix are permuted to bring the chosen element in place for subsequent computation. Furthermore, the process is repeated for each stage of the factorization.

Consequently, besides the conventional matrix factors, the outputs of pivoted factorization schemes also include permutation matrices.

In the following, the pivoting strategies implemented in Julia are briefly described. Note that not all matrix factorizations may support them. Consult the documentation of the respective [matrix factorization](#man-linalg-factorizations) for details on the supported pivoting strategies.

See also [LinearAlgebra.ZeroPivotException](#LinearAlgebra.ZeroPivotException).

[LinearAlgebra.NoPivot](#LinearAlgebra.NoPivot) — Type

```
NoPivot
```

Pivoting is not performed. This is the default strategy for [cholesky](#LinearAlgebra.cholesky) and [qr](#LinearAlgebra.qr) factorizations. Note, however, that other matrix factorizations such as the LU factorization may fail without pivoting, and may also be numerically unstable for floating-point matrices in the face of roundoff error. In such cases, this pivot strategy is mainly useful for pedagogical purposes.
