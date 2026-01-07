# R Generation Checklist

**Read this BEFORE writing R code. Vectorization and tidyverse patterns matter.**

## Critical: You Must Do These

### 1. Use Vectorized Operations, Not Loops
```r
# BAD - explicit loop
result <- c()
for (i in 1:length(x)) {
  result <- c(result, x[i] * 2)  # Also: growing vectors is slow!
}

# GOOD - vectorized
result <- x * 2

# BAD - loop for conditional
for (i in 1:length(x)) {
  if (x[i] > 0) x[i] <- x[i] * 2
}

# GOOD - vectorized conditional
x <- ifelse(x > 0, x * 2, x)
```

### 2. Use `<-` for Assignment, Not `=`
```r
# Not recommended - can be confused with function args
x = 5

# GOOD - standard R assignment
x <- 5

# Function arguments use =
mean(x = c(1, 2, 3), na.rm = TRUE)
```

### 3. Always Handle NA Values Explicitly
```r
# BAD - ignores NA problem
mean(data$value)  # Returns NA if any NA present

# GOOD - explicit NA handling
mean(data$value, na.rm = TRUE)

# GOOD - check for NAs
if (any(is.na(data$value))) {
  warning("Data contains NA values")
}

# GOOD - filter NAs
data_clean <- data[!is.na(data$value), ]
# Or with tidyverse
data_clean <- data %>% filter(!is.na(value))
```

### 4. Use Tidyverse for Data Manipulation
```r
# BAD - base R, hard to read
subset(df[order(df$date), ], status == "active")[, c("name", "value")]

# GOOD - tidyverse pipe chain
df %>%
  filter(status == "active") %>%
  arrange(date) %>%
  select(name, value)
```

### 5. Pre-allocate Vectors for Loops
```r
# BAD - growing vector (O(n²) complexity)
result <- c()
for (i in 1:n) {
  result <- c(result, compute(i))
}

# GOOD - pre-allocate
result <- vector("numeric", n)
for (i in 1:n) {
  result[i] <- compute(i)
}

# BETTER - use vapply (type-safe)
result <- vapply(1:n, compute, numeric(1))
```

## Important: Strong Recommendations

### 6. Use `vapply` Over `sapply`
```r
# BAD - sapply can return unexpected types
sapply(list(), function(x) x)  # Returns list()
sapply(1:3, function(x) x)     # Returns integer vector

# GOOD - vapply is type-safe
vapply(1:3, function(x) x, integer(1))

# For lists, use map functions from purrr
map_int(1:3, ~ .x * 2)
```

### 7. Use Meaningful Variable Names
```r
# BAD - unclear
df <- read_csv("data.csv")
x <- df$col1
y <- lm(x ~ df$col2)

# GOOD - descriptive
sales_data <- read_csv("sales.csv")
monthly_revenue <- sales_data$revenue
revenue_model <- lm(monthly_revenue ~ sales_data$marketing_spend)
```

### 8. Use Double Brackets for Single Element Extraction
```r
# Returns a list (probably not what you want)
my_list["element"]
df["column"]

# Returns the actual element/vector
my_list[["element"]]
df[["column"]]
df$column  # Equivalent for data frames
```

### 9. Use `dplyr::case_when` for Multiple Conditions
```r
# BAD - nested ifelse
data$grade <- ifelse(data$score >= 90, "A",
                ifelse(data$score >= 80, "B",
                  ifelse(data$score >= 70, "C", "F")))

# GOOD - case_when
data <- data %>%
  mutate(grade = case_when(
    score >= 90 ~ "A",
    score >= 80 ~ "B",
    score >= 70 ~ "C",
    TRUE ~ "F"
  ))
```

### 10. Use `here::here()` for File Paths
```r
# BAD - fragile paths
data <- read_csv("C:/Users/alice/project/data/sales.csv")
data <- read_csv("../data/sales.csv")

# GOOD - project-relative paths
library(here)
data <- read_csv(here("data", "sales.csv"))
```

## Data Analysis Patterns

### 11. Use `group_by` + `summarize` for Aggregations
```r
# GOOD - grouped summaries
sales_summary <- sales_data %>%
  group_by(region, year) %>%
  summarize(
    total_sales = sum(amount),
    avg_sale = mean(amount),
    n_transactions = n(),
    .groups = "drop"
  )
```

### 12. Use `pivot_longer` and `pivot_wider` for Reshaping
```r
# Wide to long (tidy)
tidy_data <- wide_data %>%
  pivot_longer(
    cols = starts_with("year_"),
    names_to = "year",
    values_to = "value"
  )

# Long to wide
wide_data <- tidy_data %>%
  pivot_wider(
    names_from = year,
    values_from = value
  )
```

### 13. Use `across()` for Multiple Column Operations
```r
# GOOD - apply function across multiple columns
data %>%
  mutate(across(where(is.numeric), scale))

data %>%
  summarize(across(starts_with("score"), mean, na.rm = TRUE))
```

## Best Practices

### 14. Use Functions for Repeated Code
```r
# BAD - copy-paste code
df1 <- df1 %>% filter(x > 0) %>% mutate(y = log(x)) %>% ...
df2 <- df2 %>% filter(x > 0) %>% mutate(y = log(x)) %>% ...

# GOOD - create function
transform_data <- function(df) {
  df %>%
    filter(x > 0) %>%
    mutate(y = log(x))
}

df1 <- transform_data(df1)
df2 <- transform_data(df2)
```

### 15. Document with roxygen2
```r
#' Calculate summary statistics
#'
#' @param data A data frame containing numeric columns
#' @param group_var Column name to group by (character)
#' @param value_var Column name to summarize (character)
#' @return A tibble with summary statistics
#' @export
#' @examples
#' calc_summary(mtcars, "cyl", "mpg")
calc_summary <- function(data, group_var, value_var) {
  data %>%
    group_by(.data[[group_var]]) %>%
    summarize(
      mean = mean(.data[[value_var]], na.rm = TRUE),
      sd = sd(.data[[value_var]], na.rm = TRUE)
    )
}
```

### 16. Use Set Seed for Reproducibility
```r
# GOOD - reproducible random operations
set.seed(42)
sample_data <- sample(data, 100)

# GOOD - within a function
my_bootstrap <- function(data, n = 1000, seed = NULL) {
  if (!is.null(seed)) set.seed(seed)
  # ... bootstrap logic
}
```

---

**Quick Reference - Copy This Mental Model:**
- Vectorize, don't loop
- `<-` for assignment
- Handle NAs explicitly (`na.rm = TRUE`)
- Tidyverse for data manipulation
- Pre-allocate vectors
- `vapply` over `sapply`
- `[[]]` for single element extraction
- `case_when` for multiple conditions
- `here::here()` for paths
- `group_by` + `summarize` for aggregations
- `pivot_longer/wider` for reshaping
- `across()` for multiple columns
- Functions for repeated code
- `set.seed()` for reproducibility
