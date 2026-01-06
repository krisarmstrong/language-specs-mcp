# MySQL Functions and Operators

Reference for MySQL 8.0 built-in functions and operators.

## Operators

### Arithmetic Operators
| Operator | Description |
|----------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `DIV` | Integer division |
| `%`, `MOD` | Modulo |

### Comparison Operators
| Operator | Description |
|----------|-------------|
| `=` | Equal |
| `<>`, `!=` | Not equal |
| `<` | Less than |
| `<=` | Less than or equal |
| `>` | Greater than |
| `>=` | Greater than or equal |
| `<=>` | NULL-safe equal |
| `BETWEEN ... AND ...` | Range check |
| `IN (...)` | Set membership |
| `IS NULL` | NULL check |
| `IS NOT NULL` | Not NULL check |
| `LIKE` | Pattern matching |
| `REGEXP`, `RLIKE` | Regular expression |

### Logical Operators
| Operator | Description |
|----------|-------------|
| `AND`, `&&` | Logical AND |
| `OR`, `\|\|` | Logical OR |
| `NOT`, `!` | Logical NOT |
| `XOR` | Logical XOR |

### Bitwise Operators
| Operator | Description |
|----------|-------------|
| `&` | Bitwise AND |
| `\|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left shift |
| `>>` | Right shift |

## String Functions

```sql
-- Length and position
CHAR_LENGTH(str), CHARACTER_LENGTH(str)  -- Character count
LENGTH(str)                               -- Byte length
LOCATE(substr, str [, pos])              -- Find position
POSITION(substr IN str)                   -- Find position
INSTR(str, substr)                       -- Find position

-- Substring
SUBSTRING(str, pos [, len])              -- Extract substring
SUBSTR(str, pos [, len])                 -- Alias for SUBSTRING
LEFT(str, len)                           -- Left characters
RIGHT(str, len)                          -- Right characters
MID(str, pos, len)                       -- Alias for SUBSTRING

-- Modification
CONCAT(str1, str2, ...)                  -- Concatenate strings
CONCAT_WS(sep, str1, str2, ...)          -- Concatenate with separator
INSERT(str, pos, len, newstr)            -- Insert/replace
REPLACE(str, from_str, to_str)           -- Replace occurrences
REVERSE(str)                             -- Reverse string

-- Case conversion
UPPER(str), UCASE(str)                   -- Uppercase
LOWER(str), LCASE(str)                   -- Lowercase

-- Trimming and padding
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM] str)
LTRIM(str)                               -- Left trim spaces
RTRIM(str)                               -- Right trim spaces
LPAD(str, len, padstr)                   -- Left pad
RPAD(str, len, padstr)                   -- Right pad

-- Other
REPEAT(str, count)                       -- Repeat string
SPACE(n)                                 -- Generate spaces
FORMAT(x, d [, locale])                  -- Format number
ASCII(str)                               -- ASCII value of first char
CHAR(n, ... [USING charset])             -- Char from ASCII
ORD(str)                                 -- Character code
HEX(str), UNHEX(str)                     -- Hex encoding
```

## Numeric Functions

```sql
-- Basic math
ABS(x)                    -- Absolute value
SIGN(x)                   -- Sign (-1, 0, 1)
MOD(n, m)                 -- Modulo
POW(x, y), POWER(x, y)    -- Exponentiation
SQRT(x)                   -- Square root
EXP(x)                    -- e^x
LN(x)                     -- Natural logarithm
LOG(x), LOG(b, x)         -- Logarithm
LOG10(x), LOG2(x)         -- Base 10/2 logarithm

-- Rounding
CEIL(x), CEILING(x)       -- Round up
FLOOR(x)                  -- Round down
ROUND(x [, d])            -- Round to d decimals
TRUNCATE(x, d)            -- Truncate to d decimals

-- Trigonometry
SIN(x), COS(x), TAN(x)
ASIN(x), ACOS(x), ATAN(x), ATAN2(y, x)
COT(x)
DEGREES(x), RADIANS(x)
PI()

-- Random
RAND([seed])              -- Random 0.0-1.0

-- Other
GREATEST(val1, val2, ...) -- Maximum value
LEAST(val1, val2, ...)    -- Minimum value
CONV(n, from_base, to_base) -- Base conversion
BIN(n), OCT(n)            -- Binary/octal representation
```

## Date and Time Functions

```sql
-- Current date/time
NOW()                     -- Current datetime
CURRENT_TIMESTAMP()       -- Alias for NOW()
SYSDATE()                 -- System time (differs in stored programs)
CURDATE(), CURRENT_DATE() -- Current date
CURTIME(), CURRENT_TIME() -- Current time
UTC_DATE(), UTC_TIME(), UTC_TIMESTAMP()

-- Date/time creation
DATE(expr)                -- Extract date
TIME(expr)                -- Extract time
TIMESTAMP(expr)           -- Datetime from expression
MAKEDATE(year, dayofyear) -- Create date
MAKETIME(hour, min, sec)  -- Create time
STR_TO_DATE(str, format)  -- Parse date string

-- Date/time extraction
YEAR(date), MONTH(date), DAY(date), DAYOFMONTH(date)
HOUR(time), MINUTE(time), SECOND(time), MICROSECOND(time)
DAYOFWEEK(date)           -- 1=Sunday, 7=Saturday
DAYOFYEAR(date)           -- 1-366
WEEK(date [, mode])       -- Week number
WEEKDAY(date)             -- 0=Monday, 6=Sunday
QUARTER(date)             -- 1-4
EXTRACT(unit FROM datetime)

-- Date/time formatting
DATE_FORMAT(date, format) -- Format date
TIME_FORMAT(time, format) -- Format time
GET_FORMAT(date|time|datetime, 'EUR'|'USA'|'ISO'|...) -- Get format string

-- Format specifiers: %Y (4-digit year), %y (2-digit), %m (month 01-12),
-- %d (day 01-31), %H (hour 00-23), %i (minute), %s (second),
-- %W (weekday name), %M (month name), %j (day of year)

-- Date arithmetic
DATE_ADD(date, INTERVAL expr unit)
DATE_SUB(date, INTERVAL expr unit)
ADDDATE(date, INTERVAL expr unit)
SUBDATE(date, INTERVAL expr unit)
ADDTIME(expr1, expr2)
SUBTIME(expr1, expr2)
TIMESTAMPADD(unit, interval, datetime)
DATEDIFF(date1, date2)    -- Days between dates
TIMEDIFF(time1, time2)    -- Time difference
TIMESTAMPDIFF(unit, datetime1, datetime2)

-- Units: MICROSECOND, SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR

-- Other
LAST_DAY(date)            -- Last day of month
DAYNAME(date)             -- Weekday name
MONTHNAME(date)           -- Month name
FROM_UNIXTIME(timestamp)  -- From Unix timestamp
UNIX_TIMESTAMP([date])    -- To Unix timestamp
CONVERT_TZ(dt, from_tz, to_tz)
```

## Aggregate Functions

```sql
COUNT(*)                  -- Count all rows
COUNT(expr)               -- Count non-NULL
COUNT(DISTINCT expr)      -- Count distinct values
SUM(expr)                 -- Sum
AVG(expr)                 -- Average
MIN(expr)                 -- Minimum
MAX(expr)                 -- Maximum

GROUP_CONCAT([DISTINCT] expr [ORDER BY ...] [SEPARATOR str])
JSON_ARRAYAGG(expr)       -- Aggregate to JSON array
JSON_OBJECTAGG(key, value) -- Aggregate to JSON object

-- Statistical
STD(expr), STDDEV(expr), STDDEV_POP(expr)  -- Population std dev
STDDEV_SAMP(expr)         -- Sample std dev
VAR_POP(expr), VARIANCE(expr)  -- Population variance
VAR_SAMP(expr)            -- Sample variance
BIT_AND(expr), BIT_OR(expr), BIT_XOR(expr)  -- Bitwise aggregates
```

## Window Functions

```sql
-- Ranking
ROW_NUMBER() OVER (...)   -- Sequential row number
RANK() OVER (...)         -- Rank with gaps
DENSE_RANK() OVER (...)   -- Rank without gaps
NTILE(n) OVER (...)       -- Divide into n groups
PERCENT_RANK() OVER (...) -- Relative rank (0-1)
CUME_DIST() OVER (...)    -- Cumulative distribution

-- Value access
LAG(expr [, n [, default]]) OVER (...)   -- Previous row value
LEAD(expr [, n [, default]]) OVER (...)  -- Next row value
FIRST_VALUE(expr) OVER (...)  -- First value in frame
LAST_VALUE(expr) OVER (...)   -- Last value in frame
NTH_VALUE(expr, n) OVER (...) -- Nth value in frame

-- Window specification
OVER (
    [PARTITION BY expr, ...]
    [ORDER BY expr [ASC|DESC], ...]
    [frame_clause]
)

-- Frame clause
{ROWS | RANGE | GROUPS} BETWEEN
    {UNBOUNDED PRECEDING | n PRECEDING | CURRENT ROW}
    AND
    {CURRENT ROW | n FOLLOWING | UNBOUNDED FOLLOWING}
```

## Flow Control Functions

```sql
IF(expr, val_if_true, val_if_false)
IFNULL(expr, alt_value)   -- Return alt if expr is NULL
NULLIF(expr1, expr2)      -- Return NULL if equal
COALESCE(val1, val2, ...) -- First non-NULL value

CASE expr
    WHEN val1 THEN result1
    WHEN val2 THEN result2
    ELSE default_result
END

CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result
END
```

## JSON Functions

```sql
-- Creation
JSON_ARRAY(val1, val2, ...)
JSON_OBJECT(key1, val1, key2, val2, ...)
JSON_QUOTE(str)

-- Extraction
JSON_EXTRACT(doc, path, ...)
doc->'$.path'             -- Shorthand for JSON_EXTRACT
doc->>'$.path'            -- Extract and unquote
JSON_KEYS(doc [, path])
JSON_VALUE(doc, path)

-- Modification
JSON_SET(doc, path, val, ...)     -- Set (insert or update)
JSON_INSERT(doc, path, val, ...)  -- Insert only
JSON_REPLACE(doc, path, val, ...) -- Update only
JSON_REMOVE(doc, path, ...)
JSON_ARRAY_APPEND(doc, path, val, ...)
JSON_ARRAY_INSERT(doc, path, val, ...)
JSON_MERGE_PATCH(doc1, doc2, ...)
JSON_MERGE_PRESERVE(doc1, doc2, ...)

-- Search
JSON_CONTAINS(doc, val [, path])
JSON_CONTAINS_PATH(doc, 'one'|'all', path, ...)
JSON_SEARCH(doc, 'one'|'all', search_str [, escape [, path, ...]])
MEMBER OF(val MEMBER OF(json_array))

-- Attributes
JSON_TYPE(doc)
JSON_VALID(val)
JSON_LENGTH(doc [, path])
JSON_DEPTH(doc)

-- Table functions
JSON_TABLE(doc, path COLUMNS(...)) -- Convert JSON to relational
```

## Encryption and Compression Functions

```sql
-- Hashing
MD5(str)                  -- MD5 hash
SHA1(str), SHA(str)       -- SHA-1 hash
SHA2(str, hash_length)    -- SHA-2 (224, 256, 384, 512)

-- Encryption (deprecated, use SSL/TLS instead)
AES_ENCRYPT(str, key_str [, init_vector [, kdf_name [, salt [, iterations]]]])
AES_DECRYPT(crypt_str, key_str [, ...])
RANDOM_BYTES(len)

-- Compression
COMPRESS(str)
UNCOMPRESS(compressed_str)
UNCOMPRESSED_LENGTH(compressed_str)
```

## Information Functions

```sql
DATABASE(), SCHEMA()      -- Current database
USER(), CURRENT_USER()    -- Current user
SESSION_USER(), SYSTEM_USER()
VERSION()                 -- MySQL version
CONNECTION_ID()           -- Connection ID
LAST_INSERT_ID()          -- Last AUTO_INCREMENT value
ROW_COUNT()               -- Rows affected by last statement
FOUND_ROWS()              -- Rows found (with SQL_CALC_FOUND_ROWS)
BENCHMARK(count, expr)    -- Performance testing
CHARSET(str)              -- Character set
COLLATION(str)            -- Collation
COERCIBILITY(str)         -- Collation coercibility
```

## Cast Functions

```sql
CAST(expr AS type)
CONVERT(expr, type)
CONVERT(expr USING charset)

-- Types: BINARY, CHAR, DATE, DATETIME, DECIMAL, DOUBLE, FLOAT,
--        JSON, NCHAR, SIGNED, TIME, UNSIGNED, YEAR
```

## Full-Text Search Functions

```sql
-- Natural language search
MATCH(col1, col2, ...) AGAINST('search terms')
MATCH(col1, col2, ...) AGAINST('search terms' IN NATURAL LANGUAGE MODE)

-- Boolean search
MATCH(col1, col2, ...) AGAINST('+required -excluded' IN BOOLEAN MODE)
-- Operators: + (must include), - (must exclude), > (increase relevance),
--           < (decrease relevance), () (grouping), ~ (negate relevance),
--           * (wildcard), "" (phrase)

-- Query expansion
MATCH(col1, col2, ...) AGAINST('search' WITH QUERY EXPANSION)
```

## Miscellaneous Functions

```sql
UUID()                    -- Generate UUID
UUID_SHORT()              -- Short UUID (64-bit)
UUID_TO_BIN(uuid [, swap_flag])
BIN_TO_UUID(binary_uuid [, swap_flag])
IS_UUID(string_uuid)

SLEEP(seconds)            -- Pause execution
GET_LOCK(str, timeout)    -- Named lock
IS_FREE_LOCK(str)
IS_USED_LOCK(str)
RELEASE_LOCK(str)
RELEASE_ALL_LOCKS()

INET_ATON(addr)           -- IPv4 to integer
INET_NTOA(num)            -- Integer to IPv4
INET6_ATON(addr)          -- IPv6 to binary
INET6_NTOA(binary)        -- Binary to IPv6
IS_IPV4(expr), IS_IPV6(expr)

VALUES(col)               -- Inserted value (in ON DUPLICATE KEY)
DEFAULT(col)              -- Default value of column
```

See: https://dev.mysql.com/doc/refman/8.0/en/functions.html
