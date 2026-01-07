List of warnings — luacheck 0.26.0 documentation[luacheck](index.html) stable 

- [List of warnings](#)

  - [Global variables (1xx)](#global-variables-1xx)

    - [Read-only globals](#read-only-globals)
    - [Implicitly defined globals](#implicitly-defined-globals)
    - [Modules](#modules-1)

  - [Unused variables (2xx) and values (3xx)](#unused-variables-2xx-and-values-3xx)

    - [“Unused hint” (214)](#unused-hint-214)
    - [Unused values and uninitialized variables](#unused-values-and-uninitialized-variables)
    - [Secondary values and variables](#secondary-values-and-variables)

  - [Shadowing declarations (4xx)](#shadowing-declarations-4xx)
  - [Control flow and data flow issues (5xx)](#control-flow-and-data-flow-issues-5xx)

    - [Unreachable code](#unreachable-code)
    - [Unused labels](#unused-labels)
    - [Unbalanced assignments](#unbalanced-assignments)
    - [Empty blocks](#empty-blocks)
    - [Empty statements](#empty-statements)
    - [Cyclomatic complexity](#cyclomatic-complexity)
    - [Reversed numeric for loops](#reversed-numeric-for-loops)
    - [Error-prone and Unnecessary Negations](#error-prone-and-unnecessary-negations)

  - [Formatting issues (6xx)](#formatting-issues-6xx)

    - [Whitespace issues](#whitespace-issues)
    - [Line length limits](#line-length-limits)

- [Command line interface](cli.html)
- [Configuration file](config.html)
- [Inline options](inline.html)
- [Luacheck module](module.html)

[luacheck](index.html)

- [Docs](index.html) »
- List of warnings
- [Edit on GitHub](https://github.com/lunarmodules/luacheck/blob/5784e3f906979abfd0b2bc7a004be64e07fe84b2/docsrc/warnings.rst)

# List of warnings[¶](#list-of-warnings)

Warnings produced by Luacheck are categorized using three-digit warning codes. Warning codes can be displayed in CLI output using `--codes` CLI option or `codes` config option. Errors also have codes starting with zero; unlike warnings, they can not be ignored.

CodeDescription011A syntax error.021An invalid inline option.022An unpaired inline push directive.023An unpaired inline pop directive.111Setting an undefined global variable.112Mutating an undefined global variable.113Accessing an undefined global variable.121Setting a read-only global variable.122Setting a read-only field of a global variable.131Unused implicitly defined global variable.142Setting an undefined field of a global variable.143Accessing an undefined field of a global variable.211Unused local variable.212Unused argument.213Unused loop variable.214Used variable.221Local variable is accessed but never set.231Local variable is set but never accessed.232An argument is set but never accessed.233Loop variable is set but never accessed.241Local variable is mutated but never accessed.311Value assigned to a local variable is unused.312Value of an argument is unused.313Value of a loop variable is unused.314Value of a field in a table literal is unused.321Accessing uninitialized local variable.331Value assigned to a local variable is mutated but never accessed.341Mutating uninitialized local variable.411Redefining a local variable.412Redefining an argument.413Redefining a loop variable.421Shadowing a local variable.422Shadowing an argument.423Shadowing a loop variable.431Shadowing an upvalue.432Shadowing an upvalue argument.433Shadowing an upvalue loop variable.511Unreachable code.512Loop can be executed at most once.521Unused label.531Left-hand side of an assignment is too short.532Left-hand side of an assignment is too long.541An empty `do``end` block.542An empty `if` branch.551An empty statement.561Cyclomatic complexity of a function is too high.571A numeric for loop goes from #(expr) down to 1 or less without negative step.581Negation of a relational operator- operator can be flipped.582Error prone negation: negation has a higher priority than equality.611A line consists of nothing but whitespace.612A line contains trailing whitespace.613Trailing whitespace in a string.614Trailing whitespace in a comment.621Inconsistent indentation (`SPACE` followed by `TAB`).631Line is too long.

## Global variables (1xx)[¶](#global-variables-1xx)

For each file, Luacheck builds list of defined globals and fields which can be used there. By default only globals from Lua standard library are defined; custom globals can be added using `--globals` CLI option or `globals` config option, and version of standard library can be selected using `--std` CLI option or `std` config option. When an undefined global or field is set, mutated or accessed, Luacheck produces a warning.

### Read-only globals[¶](#read-only-globals)

By default, most standard globals and fields are marked as read-only, so that setting them produces a warning. Custom read-only globals and fields can be added using `--read-globals` CLI option or `read_globals` config option, or using a custom set of globals. See [Custom sets of globals](config.html#custom-stds)

Globals and fields that are not read-only by default:

- `_G`
- `_ENV` (treated as a global by Luacheck)
- `package.path`
- `package.cpath`
- `package.loaded`
- `package.preload`
- `package.loaders`
- `package.searchers`

### Implicitly defined globals[¶](#implicitly-defined-globals)

Luacheck can be configured to consider globals assigned under some conditions to be defined implicitly. When `-d`/`--allow_defined` CLI option or `allow_defined` config option is used, all assignments to globals define them; when `-t`/`--allow_defined_top` CLI option or `allow_defined_top` config option is used, assignments to globals in the top level function scope (also known as main chunk) define them. A warning is produced when an implicitly defined global is not accessed anywhere.

### Modules[¶](#modules-1)

Files can be marked as modules using `-m`/`--module` CLI option or `module` config option to simulate semantics of the deprecated [module](http://www.lua.org/manual/5.1/manual.html#pdf-module) function. Globals implicitly defined inside a module are considired part of its interface, are not visible outside and are not reported as unused. Assignments to other globals are not allowed, even to defined ones.

## Unused variables (2xx) and values (3xx)[¶](#unused-variables-2xx-and-values-3xx)

Luacheck generates warnings for all unused local variables except one named `_`. It also detects variables which are set but never accessed or accessed but never set.

### “Unused hint” (214)[¶](#unused-hint-214)

If a function argument starts with an underscore `_`, it recevies an “unused hint”, meaning that it’s intended to be left unused. If it is used, a 214 warning is generated.

### Unused values and uninitialized variables[¶](#unused-values-and-uninitialized-variables)

For each value assigned to a local variable, Luacheck computes set of expressions where it could be used. Warnings are produced for unused values (when a value can’t be used anywhere) and for accessing uninitialized variables (when no values can reach an expression). E.g. in the following snippet value assigned to `foo` on line 1 is unused, and variable `bar` is uninitialized on line 9:

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
```

```
local foo = expr1()
local bar

if condition() then
   foo = expr2()
   bar = expr3()
else
   foo = expr4()
   print(bar)
end

return foo, bar
```

### Secondary values and variables[¶](#secondary-values-and-variables)

Unused value assigned to a local variable is secondary if its origin is the last item on the RHS of assignment, and another value from that item is used. Secondary values typically appear when result of a function call is put into locals, and only some of them are later used. For example, here value assigned to `b` is secondary, value assigned to `c` is used, and value assigned to `a` is simply unused:

```
1
2
3
```

```
local a, b, c = f(), g()

return c
```

A variable is secondary if all values assigned to it are secondary. In the snippet above, `b` is a secondary variable.

Warnings related to unused secondary values and variables can be removed using `-s`/`--no-unused-secondaries` CLI option or `unused_secondaries` config option.

## Shadowing declarations (4xx)[¶](#shadowing-declarations-4xx)

Luacheck detects declarations of local variables shadowing previous declarations, unless the variable is named `_`. If the previous declaration is in the same scope as the new one, it is called redefining.

Note that it is not necessary to define a new local variable when overwriting an argument:

```
1
2
3
4
5
6
7
```

```
local function f(x)
   local x = x or "default" -- bad
end

local function f(x)
   x = x or "default" -- good
end
```

## Control flow and data flow issues (5xx)[¶](#control-flow-and-data-flow-issues-5xx)

### Unreachable code[¶](#unreachable-code)

Luacheck detects unreachable code. It also detects it if end of a loop block is unreachable, which means that the loop can be executed at most once:

```
1
2
3
4
5
```

```
for i = 1, 100 do
   -- Break statement is outside the `if` block,
   -- so that the loop always stops after the first iteration.
   if cond(i) then f() end break
end
```

### Unused labels[¶](#unused-labels)

Labels that are not used by any `goto` statements are reported as unused.

### Unbalanced assignments[¶](#unbalanced-assignments)

If an assignment has left side and right side with different lengths, the assignment is unbalanced and Luacheck warns about it.

An exception is initializing several local variables in a single statement while leaving some uninitialized:

```
1
```

```
local a, b, c = nil -- Effectively sets `a`, `b`, and `c` to nil, no warning.
```

### Empty blocks[¶](#empty-blocks)

Luacheck warns about empty `do``end` blocks and empty `if` branches (`then``else`, `then``elseif`, and `then``end`).

### Empty statements[¶](#empty-statements)

In Lua 5.2+ semicolons are considered statements and can appear even when not following normal statements. Such semicolons produce Luacheck warnings as they are completely useless.

### Cyclomatic complexity[¶](#cyclomatic-complexity)

If a limit is set using `--max-cyclomatic-complexity` CLI option or corresponding config or inline options, Luacheck warns about functions with too high cyclomatic complexity.

### Reversed numeric for loops[¶](#reversed-numeric-for-loops)

Iterating a table in reverse using a numeric for loop going from `#t` to `1` requires a negative loop step. Luacheck warns about loops going from `#(some expression)` to `1` or a smaller constant when the loop step is not negative:

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
```

```
-- Warning for this loop:
-- numeric for loop goes from #(expr) down to 1 but loop step is not negative
for i = #t, 1 do
   print(t[i])
end

-- This loop is okay.
for i = #t, 1, -1 do
   print(t[i])
end
```

### Error-prone and Unnecessary Negations[¶](#error-prone-and-unnecessary-negations)

Negation has a higher priority than relational operators; (not x == 3) is interpreted as (not x) == 3, rather than not (x == 3).

Negating the output of a relational operator is unnecessary; each one has another operator that can be used directly:

not (x == y) => x ~= y not (x ~= y) => x == y not (x > y) => x <= y not (x >= y) => x < y not (x < y) => x >= y not (x <= y) => x > y

These replacements work for all numbers, but can fail with metatables or NaN’s.

## Formatting issues (6xx)[¶](#formatting-issues-6xx)

### Whitespace issues[¶](#whitespace-issues)

Luacheck warns about trailing whitespace and inconsistent indentation (`SPACE` followed by `TAB`).

Some examples of trailing whitespace Luacheck finds:

```
1
2
3
4
```

```
-- Whitespace example.
print("Hello")

print("World")
```

Here:

- Any tabs or spaces after either `)` would be considered trailing.
- Any tabs or spaces after the `.` in the comment would be considered trailing
- Any tabs or spaces on the empty line between the two `print` statements would also be considered a form of trailing whitespace.

Trailing whitespace in any of these forms is useless, can be a nuisance to developers navigating around a file, and is forbidden in many formatting styles.

### Line length limits[¶](#line-length-limits)

Luacheck warns about lines that are longer then some limit. Default limit is `120` characters. It’s possible to change this limit using `--max-line-length` CLI option or disable the check completely with `--no-max-line-length`; there are similar config and inline options.

Additionally, separate limits can be set for three different type of lines:

- “String” lines have their line ending inside a string, typically a long string using `[[...]]` syntax.
- “Comment” lines have their line ending inside a long comment (`--[[...]]`), or end with a short comment using normal `--...` syntax.
- “Code” lines are all other lines.

These types of lines are limited using CLI options named `--[no-]max-string-line-length`, `--[no-]max-comment-line-length`, and `--[no-]max-code-line-length`, with similar config and inline options.

[Next](cli.html)[Previous](index.html)

 © Copyright 2014 - 2018, Peter Melnichenko  Revision `5784e3f9`. 

 Built with [Sphinx](http://sphinx-doc.org/) using a [theme](https://github.com/rtfd/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).
