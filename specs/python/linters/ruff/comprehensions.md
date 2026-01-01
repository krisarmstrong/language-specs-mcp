# Ruff - flake8-comprehensions Rules (C4)

Write better comprehensions.

## C400: Unnecessary generator - use list comprehension

```python
# BAD
list(x for x in iterable)

# GOOD
[x for x in iterable]
```

## C401: Unnecessary generator - use set comprehension

```python
# BAD
set(x for x in iterable)

# GOOD
{x for x in iterable}
```

## C402: Unnecessary generator - use dict comprehension

```python
# BAD
dict((k, v) for k, v in items)

# GOOD
{k: v for k, v in items}
```

## C403: Unnecessary list comprehension - use set

```python
# BAD
set([x for x in iterable])

# GOOD
{x for x in iterable}
```

## C404: Unnecessary list comprehension - use dict

```python
# BAD
dict([pair for pair in items])

# GOOD
{k: v for k, v in items}
```

## C405: Unnecessary literal - use set literal

```python
# BAD
set([1, 2, 3])
set((1, 2, 3))

# GOOD
{1, 2, 3}
```

## C406: Unnecessary literal - use dict literal

```python
# BAD
dict([(1, 2), (3, 4)])
dict(((1, 2), (3, 4)))

# GOOD
{1: 2, 3: 4}
```

## C408: Unnecessary dict/list/tuple call

```python
# BAD
dict()
list()
tuple()

# GOOD
{}
[]
()
```

## C409: Unnecessary list passed to tuple()

```python
# BAD
tuple([1, 2, 3])

# GOOD
(1, 2, 3)
```

## C410: Unnecessary list passed to list()

```python
# BAD
list([1, 2, 3])

# GOOD
[1, 2, 3]
```

## C411: Unnecessary list call - use list literal

```python
# BAD
list([])

# GOOD
[]
```

## C413: Unnecessary list/reversed call around sorted()

```python
# BAD
list(sorted(iterable))
reversed(sorted(iterable))

# GOOD
sorted(iterable)
sorted(iterable, reverse=True)
```

## C414: Unnecessary double list/set/tuple/reversed/sorted

```python
# BAD
list(list(iterable))
set(set(iterable))
sorted(sorted(iterable))

# GOOD
list(iterable)
set(iterable)
sorted(iterable)
```

## C415: Unnecessary subscript reversal

```python
# BAD
set(iterable[::-1])
sorted(iterable)[::-1]

# GOOD
set(iterable)
sorted(iterable, reverse=True)
```

## C416: Unnecessary comprehension - use list/set/dict

```python
# BAD
[x for x in iterable]  # identity comprehension
{x for x in iterable}
{k: v for k, v in items}

# GOOD
list(iterable)
set(iterable)
dict(items)
```

## C417: Unnecessary map - use generator/comprehension

```python
# BAD
map(lambda x: x * 2, iterable)
map(str, numbers)

# GOOD
(x * 2 for x in iterable)
[x * 2 for x in iterable]
(str(n) for n in numbers)
```

## C418: Unnecessary dict passed to dict()

```python
# BAD
dict({"a": 1})

# GOOD
{"a": 1}
```

## C419: Unnecessary comprehension in any/all

```python
# BAD
any([x > 0 for x in items])
all([x > 0 for x in items])

# GOOD - use generator
any(x > 0 for x in items)
all(x > 0 for x in items)
```
