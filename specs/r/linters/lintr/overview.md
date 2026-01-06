# lintr

lintr is a static code analysis tool for R.

Version: 3.3.0
Source: https://lintr.r-lib.org/

## Installation

```r
install.packages("lintr")
```

## Usage

```r
# Lint a file
lintr::lint("script.R")

# Lint a package
lintr::lint_package()

# Lint a directory
lintr::lint_dir("R/")
```

## Configuration

Create `.lintr` file:

```r
linters: linters_with_defaults(
  line_length_linter(120),
  commented_code_linter = NULL
)
exclusions: list(
  "R/generated.R",
  "tests/testthat/helper.R" = list(
    object_name_linter = Inf
  )
)
```

## Linter Categories

### Style & Formatting

#### assignment_linter
Checks assignment operator style (`<-` vs `=`).

#### brace_linter
Checks brace placement and style.

#### commas_linter
Ensures proper comma spacing.

#### indentation_linter
Checks consistent indentation.

#### infix_spaces_linter
Ensures spaces around infix operators.

#### line_length_linter
Enforces maximum line length.

#### quotes_linter
Checks quote style consistency.

#### semicolon_linter
Discourages semicolons.

#### spaces_inside_linter
Checks spacing inside brackets.

#### trailing_blank_lines_linter
Removes trailing blank lines.

#### trailing_whitespace_linter
Removes trailing whitespace.

### Code Quality

#### commented_code_linter
Detects commented-out code.

#### cyclocomp_linter
Checks cyclomatic complexity.

#### function_argument_linter
Checks function argument usage.

#### object_length_linter
Checks object name length.

#### object_name_linter
Ensures naming conventions.

#### object_usage_linter
Detects undefined variables.

#### return_linter
Checks return statement usage.

#### todo_comment_linter
Warns about TODO comments.

#### unreachable_code_linter
Detects unreachable code.

### Common Mistakes

#### all_equal_linter
Suggests `all.equal()` alternatives.

#### any_duplicated_linter
Suggests `anyDuplicated()`.

#### any_is_na_linter
Prefers `anyNA()` over `any(is.na())`.

#### comparison_negation_linter
Simplifies negated comparisons.

#### equals_na_linter
Warns about `== NA` (use `is.na()`).

#### if_not_else_linter
Simplifies `if (!x) else`.

#### nested_ifelse_linter
Warns about nested ifelse.

#### redundant_equals_linter
Removes redundant `== TRUE`.

#### redundant_ifelse_linter
Simplifies redundant ifelse.

#### vector_logic_linter
Uses `&&`/`||` vs `&`/`|` appropriately.

#### yoda_test_linter
Avoids Yoda conditions.

### Efficiency

#### inner_combine_linter
Suggests moving `c()` inside functions.

#### lengths_linter
Prefers `lengths()` over `sapply(x, length)`.

#### matrix_apply_linter
Suggests `colSums`/`rowSums`.

#### nrow_subset_linter
Avoids `nrow()` in subsetting.

#### seq_linter
Prefers `seq_len()`/`seq_along()`.

### Testing (testthat)

#### expect_comparison_linter
Uses comparison expectations properly.

#### expect_identical_linter
Prefers `expect_identical()`.

#### expect_length_linter
Uses `expect_length()`.

#### expect_named_linter
Uses `expect_named()`.

#### expect_not_linter
Uses `expect_false()`.

#### expect_null_linter
Uses `expect_null()`.

#### expect_s3_class_linter
Uses `expect_s3_class()`.

#### expect_s4_class_linter
Uses `expect_s4_class()`.

#### expect_true_false_linter
Uses `expect_true()`/`expect_false()`.

#### expect_type_linter
Uses `expect_type()`.

## Configuration Functions

```r
# Default linters with modifications
linters_with_defaults(
  line_length_linter = line_length_linter(120),
  object_name_linter = NULL  # disable
)

# Only specific tags
linters_with_tags(tags = c("correctness", "efficiency"))

# Exclude lines
# nolint
# nolint start
# nolint end
```

## IDE Integration

- RStudio: Built-in support
- VS Code: R extension support
- Emacs: flycheck-lintr
- Vim: ALE plugin
