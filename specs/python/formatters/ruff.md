.. Ruff [ruff](https://github.com/astral-sh/ruff)

- [Overview](..)
- [Tutorial](../tutorial/)
- [Installing Ruff](../installation/)
- [The Ruff Linter](../linter/)
-  The Ruff Formatter [The Ruff Formatter](./) Table of contents 

  - [ruff format](#ruff-format)
  - [Philosophy](#philosophy)
  - [Configuration](#configuration)
  - [Docstring formatting](#docstring-formatting)
  - [Format suppression](#format-suppression)
  - [Conflicting lint rules](#conflicting-lint-rules)
  - [Exit codes](#exit-codes)
  - [Style Guide](#style-guide)

    - [Intentional deviations](#intentional-deviations)
    - [Preview style](#preview-style)
    - [F-string formatting](#f-string-formatting)

      - [Quotes](#quotes)
      - [Line breaks](#line-breaks)
      - [Fluent layout for method chains](#fluent-layout-for-method-chains)

  - [Sorting imports](#sorting-imports)

-  Editors  Editors 

  - [Editor Integration](../editors/)
  - [Setup](../editors/setup/)
  - [Features](../editors/features/)
  - [Settings](../editors/settings/)
  - [Migrating from ruff-lsp](../editors/migration/)

- [Configuring Ruff](../configuration/)
- [Preview](../preview/)
- [Rules](../rules/)
- [Settings](../settings/)
- [Versioning](../versioning/)
- [Integrations](../integrations/)
- [FAQ](../faq/)
- [Contributing](../contributing/)

# [The Ruff Formatter](#the-ruff-formatter)

The Ruff formatter is an extremely fast Python code formatter designed as a drop-in replacement for [Black](https://pypi.org/project/black/), available as part of the `ruff` CLI via `ruff format`.

## [ruff format](#ruff-format)

`ruff format` is the primary entrypoint to the formatter. It accepts a list of files or directories, and formats all discovered Python files:

```
#__codelineno-0-1ruff format                   # Format all files in the current directory.
#__codelineno-0-2ruff format path/to/code/     # Format all files in `path/to/code` (and any subdirectories).
#__codelineno-0-3ruff format path/to/file.py   # Format a single file.
```

Similar to Black, running `ruff format /path/to/file.py` will format the given file or directory in-place, while `ruff format --check /path/to/file.py` will avoid writing any formatted files back, and instead exit with a non-zero status code upon detecting any unformatted files.

For the full list of supported options, run `ruff format --help`.

## [Philosophy](#philosophy)

The initial goal of the Ruff formatter is not to innovate on code style, but rather, to innovate on performance, and provide a unified toolchain across Ruff's linter, formatter, and any and all future tools.

As such, the formatter is designed as a drop-in replacement for [Black](https://github.com/psf/black), but with an excessive focus on performance and direct integration with Ruff. Given Black's popularity within the Python ecosystem, targeting Black compatibility ensures that formatter adoption is minimally disruptive for the vast majority of projects.

Specifically, the formatter is intended to emit near-identical output when run over existing Black-formatted code. When run over extensive Black-formatted projects like Django and Zulip, > 99.9% of lines are formatted identically. (See: [Style Guide](#style-guide).)

Given this focus on Black compatibility, the formatter thus adheres to [Black's (stable) code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html), which aims for "consistency, generality, readability and reducing git diffs". To give you a sense for the enforced code style, here's an example:

```
#__codelineno-1-1# Input
#__codelineno-1-2def _make_ssl_transport(
#__codelineno-1-3    rawsock, protocol, sslcontext, waiter=None,
#__codelineno-1-4    *, server_side=False, server_hostname=None,
#__codelineno-1-5    extra=None, server=None,
#__codelineno-1-6    ssl_handshake_timeout=None,
#__codelineno-1-7    call_connection_made=True):
#__codelineno-1-8    '''Make an SSL transport.'''
#__codelineno-1-9    if waiter is None:
#__codelineno-1-10      waiter = Future(loop=loop)
#__codelineno-1-11
#__codelineno-1-12    if extra is None:
#__codelineno-1-13      extra = {}
#__codelineno-1-14
#__codelineno-1-15    ...
#__codelineno-1-16
#__codelineno-1-17# Ruff
#__codelineno-1-18def _make_ssl_transport(
#__codelineno-1-19    rawsock,
#__codelineno-1-20    protocol,
#__codelineno-1-21    sslcontext,
#__codelineno-1-22    waiter=None,
#__codelineno-1-23    *,
#__codelineno-1-24    server_side=False,
#__codelineno-1-25    server_hostname=None,
#__codelineno-1-26    extra=None,
#__codelineno-1-27    server=None,
#__codelineno-1-28    ssl_handshake_timeout=None,
#__codelineno-1-29    call_connection_made=True,
#__codelineno-1-30):
#__codelineno-1-31    """Make an SSL transport."""
#__codelineno-1-32    if waiter is None:
#__codelineno-1-33        waiter = Future(loop=loop)
#__codelineno-1-34
#__codelineno-1-35    if extra is None:
#__codelineno-1-36        extra = {}
#__codelineno-1-37
#__codelineno-1-38    ...
```

Like Black, the Ruff formatter does not support extensive code style configuration; however, unlike Black, it does support configuring the desired quote style, indent style, line endings, and more. (See: [Configuration](#configuration).)

While the formatter is designed to be a drop-in replacement for Black, it is not intended to be used interchangeably with Black on an ongoing basis, as the formatter does differ from Black in a few conscious ways (see: [Known deviations](black/)). In general, deviations are limited to cases in which Ruff's behavior was deemed more consistent, or significantly simpler to support (with negligible end-user impact) given the differences in the underlying implementations between Black and Ruff.

Going forward, the Ruff Formatter will support Black's preview style under Ruff's own [preview](../preview/) mode.

## [Configuration](#configuration)

The Ruff Formatter exposes a small set of configuration options, some of which are also supported by Black (like line width), some of which are unique to Ruff (like quote, indentation style and formatting code examples in docstrings).

For example, to configure the formatter to use single quotes, format code examples in docstrings, a line width of 100, and tab indentation, add the following to your configuration file:

pyproject.tomlruff.toml

```
#__codelineno-2-1[tool.ruff]
#__codelineno-2-2line-length = 100
#__codelineno-2-3
#__codelineno-2-4[tool.ruff.format]
#__codelineno-2-5quote-style = "single"
#__codelineno-2-6indent-style = "tab"
#__codelineno-2-7docstring-code-format = true
```

```
#__codelineno-3-1line-length = 100
#__codelineno-3-2
#__codelineno-3-3[format]
#__codelineno-3-4quote-style = "single"
#__codelineno-3-5indent-style = "tab"
#__codelineno-3-6docstring-code-format = true
```

For the full list of supported settings, see [Settings](../settings/#format). For more on configuring Ruff via `pyproject.toml`, see [Configuring Ruff](../configuration/).

Given the focus on Black compatibility (and unlike formatters like [YAPF](https://github.com/google/yapf)), Ruff does not currently expose any other configuration options.

## [Docstring formatting](#docstring-formatting)

The Ruff formatter provides an opt-in feature for automatically formatting Python code examples in docstrings. The Ruff formatter currently recognizes code examples in the following formats:

- The Python [doctest](https://docs.python.org/3/library/doctest.html) format.
- CommonMark [fenced code blocks](https://spec.commonmark.org/0.30/#fenced-code-blocks) with the following info strings: `python`, `py`, `python3`, or `py3`. Fenced code blocks without an info string are assumed to be Python code examples and also formatted.
- reStructuredText [literal blocks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#literal-blocks). While literal blocks may contain things other than Python, this is meant to reflect a long-standing convention in the Python ecosystem where literal blocks often contain Python code.
- reStructuredText [`code-block` and `sourcecode` directives]. As with Markdown, the language names recognized for Python are `python`, `py`, `python3`, or `py3`.

If a code example is recognized and treated as Python, the Ruff formatter will automatically skip it if the code does not parse as valid Python or if the reformatted code would produce an invalid Python program.

Users may also configure the line length limit used for reformatting Python code examples in docstrings. The default is a special value, `dynamic`, which instructs the formatter to respect the line length limit setting for the surrounding Python code. The `dynamic` setting ensures that even when code examples are found inside indented docstrings, the line length limit configured for the surrounding Python code will not be exceeded. Users may also configure a fixed line length limit for code examples in docstrings.

For example, this configuration shows how to enable docstring code formatting with a fixed line length limit:

pyproject.tomlruff.toml

```
#__codelineno-4-1[tool.ruff.format]
#__codelineno-4-2docstring-code-format = true
#__codelineno-4-3docstring-code-line-length = 20
```

```
#__codelineno-5-1[format]
#__codelineno-5-2docstring-code-format = true
#__codelineno-5-3docstring-code-line-length = 20
```

With the above configuration, this code:

```
#__codelineno-6-1def f(x):
#__codelineno-6-2    '''
#__codelineno-6-3    Something about `f`. And an example:
#__codelineno-6-4
#__codelineno-6-5    .. code-block:: python
#__codelineno-6-6
#__codelineno-6-7        foo, bar, quux = this_is_a_long_line(lion, hippo, lemur, bear)
#__codelineno-6-8    '''
#__codelineno-6-9    pass
```

... will be reformatted (assuming the rest of the options are set to their defaults) as:

```
#__codelineno-7-1def f(x):
#__codelineno-7-2    """
#__codelineno-7-3    Something about `f`. And an example:
#__codelineno-7-4
#__codelineno-7-5    .. code-block:: python
#__codelineno-7-6
#__codelineno-7-7        (
#__codelineno-7-8            foo,
#__codelineno-7-9            bar,
#__codelineno-7-10            quux,
#__codelineno-7-11        ) = this_is_a_long_line(
#__codelineno-7-12            lion,
#__codelineno-7-13            hippo,
#__codelineno-7-14            lemur,
#__codelineno-7-15            bear,
#__codelineno-7-16        )
#__codelineno-7-17    """
#__codelineno-7-18    pass
```

## [Format suppression](#format-suppression)

Like Black, Ruff supports `# fmt: on`, `# fmt: off`, and `# fmt: skip` pragma comments, which can be used to temporarily disable formatting for a given code block.

`# fmt: on` and `# fmt: off` comments are enforced at the statement level:

```
#__codelineno-8-1# fmt: off
#__codelineno-8-2not_formatted=3
#__codelineno-8-3also_not_formatted=4
#__codelineno-8-4# fmt: on
```

As such, adding `# fmt: on` and `# fmt: off` comments within expressions will have no effect. In the following example, both list entries will be formatted, despite the `# fmt: off`:

```
#__codelineno-9-1[
#__codelineno-9-2    # fmt: off
#__codelineno-9-3    '1',
#__codelineno-9-4    # fmt: on
#__codelineno-9-5    '2',
#__codelineno-9-6]
```

Instead, apply the `# fmt: off` comment to the entire statement:

```
#__codelineno-10-1# fmt: off
#__codelineno-10-2[
#__codelineno-10-3    '1',
#__codelineno-10-4    '2',
#__codelineno-10-5]
#__codelineno-10-6# fmt: on
```

Like Black, Ruff will also recognize [YAPF](https://github.com/google/yapf)'s `# yapf: disable` and `# yapf: enable` pragma comments, which are treated equivalently to `# fmt: off` and `# fmt: on`, respectively.

`# fmt: skip` comments suppress formatting for a preceding statement, case header, decorator, function definition, or class definition:

```
#__codelineno-11-1if True:
#__codelineno-11-2    pass
#__codelineno-11-3elif False: # fmt: skip
#__codelineno-11-4    pass
#__codelineno-11-5
#__codelineno-11-6@Test
#__codelineno-11-7@Test2 # fmt: skip
#__codelineno-11-8def test(): ...
#__codelineno-11-9
#__codelineno-11-10a = [1, 2, 3, 4, 5] # fmt: skip
#__codelineno-11-11
#__codelineno-11-12def test(a, b, c, d, e, f) -> int: # fmt: skip
#__codelineno-11-13    pass
```

As such, adding an `# fmt: skip` comment at the end of an expression will have no effect. In the following example, the list entry `'1'` will be formatted, despite the `# fmt: skip`:

```
#__codelineno-12-1a = call(
#__codelineno-12-2    [
#__codelineno-12-3        '1',  # fmt: skip
#__codelineno-12-4        '2',
#__codelineno-12-5    ],
#__codelineno-12-6    b
#__codelineno-12-7)
```

Instead, apply the `# fmt: skip` comment to the entire statement:

```
#__codelineno-13-1a = call(
#__codelineno-13-2  [
#__codelineno-13-3    '1',
#__codelineno-13-4    '2',
#__codelineno-13-5  ],
#__codelineno-13-6  b
#__codelineno-13-7)  # fmt: skip
```

## [Conflicting lint rules](#conflicting-lint-rules)

Ruff's formatter is designed to be used alongside the linter. However, the linter includes some rules that, when enabled, can cause conflicts with the formatter, leading to unexpected behavior. When configured appropriately, the goal of Ruff's formatter-linter compatibility is such that running the formatter should never introduce new lint errors.

When using Ruff as a formatter, we recommend avoiding the following lint rules:

- [tab-indentation](../rules/tab-indentation/) (`W191`)
- [indentation-with-invalid-multiple](../rules/indentation-with-invalid-multiple/) (`E111`)
- [indentation-with-invalid-multiple-comment](../rules/indentation-with-invalid-multiple-comment/) (`E114`)
- [over-indented](../rules/over-indented/) (`E117`)
- [docstring-tab-indentation](../rules/docstring-tab-indentation/) (`D206`)
- [triple-single-quotes](../rules/triple-single-quotes/) (`D300`)
- [bad-quotes-inline-string](../rules/bad-quotes-inline-string/) (`Q000`)
- [bad-quotes-multiline-string](../rules/bad-quotes-multiline-string/) (`Q001`)
- [bad-quotes-docstring](../rules/bad-quotes-docstring/) (`Q002`)
- [avoidable-escaped-quote](../rules/avoidable-escaped-quote/) (`Q003`)
- [missing-trailing-comma](../rules/missing-trailing-comma/) (`COM812`)
- [prohibited-trailing-comma](../rules/prohibited-trailing-comma/) (`COM819`)
- [multi-line-implicit-string-concatenation](../rules/multi-line-implicit-string-concatenation/) (`ISC002`) if used without `ISC001` and `flake8-implicit-str-concat.allow-multiline = false`

While the [line-too-long](../rules/line-too-long/) (`E501`) rule can be used alongside the formatter, the formatter only makes a best-effort attempt to wrap lines at the configured [line-length](../settings/#line-length). As such, formatted code may exceed the line length, leading to [line-too-long](../rules/line-too-long/) (`E501`) errors.

None of the above are included in Ruff's default configuration. However, if you've enabled any of these rules or their parent categories (like `Q`), we recommend disabling them via the linter's [lint.ignore](../settings/#lint_ignore) setting.

Similarly, we recommend avoiding the following isort settings, which are incompatible with the formatter's treatment of import statements when set to non-default values:

- [force-single-line](../settings/#lint_isort_force-single-line)
- [force-wrap-aliases](../settings/#lint_isort_force-wrap-aliases)
- [lines-after-imports](../settings/#lint_isort_lines-after-imports)
- [lines-between-types](../settings/#lint_isort_lines-between-types)
- [split-on-trailing-comma](../settings/#lint_isort_split-on-trailing-comma)

If you've configured any of these settings to take on non-default values, we recommend removing them from your Ruff configuration.

When an incompatible lint rule or setting is enabled, `ruff format` will emit a warning. If your `ruff format` is free of warnings, you're good to go!

## [Exit codes](#exit-codes)

`ruff format` exits with the following status codes:

- `0` if Ruff terminates successfully, regardless of whether any files were formatted.
- `2` if Ruff terminates abnormally due to invalid configuration, invalid CLI options, or an internal error.

Meanwhile, `ruff format --check` exits with the following status codes:

- `0` if Ruff terminates successfully, and no files would be formatted if `--check` were not specified.
- `1` if Ruff terminates successfully, and one or more files would be formatted if `--check` were not specified.
- `2` if Ruff terminates abnormally due to invalid configuration, invalid CLI options, or an internal error.

## [Style Guide](#style-guide)

The formatter is designed to be a drop-in replacement for [Black](https://github.com/psf/black). This section documents the areas where the Ruff formatter goes beyond Black in terms of code style.

### [Intentional deviations](#intentional-deviations)

While the Ruff formatter aims to be a drop-in replacement for Black, it does differ from Black in a few known ways. Some of these differences emerge from conscious attempts to improve upon Black's code style, while others fall out of differences in the underlying implementations.

For a complete enumeration of these intentional deviations, see [Known deviations](black/).

Unintentional deviations from Black are tracked in the [issue tracker](https://github.com/astral-sh/ruff/issues?q=is%3Aopen+is%3Aissue+label%3Aformatter). If you've identified a new deviation, please [file an issue](https://github.com/astral-sh/ruff/issues/new).

### [Preview style](#preview-style)

Similar to [Black](https://black.readthedocs.io/en/stable/the_black_code_style/future_style.html#preview-style), Ruff implements formatting changes under the [preview](https://docs.astral.sh/ruff/settings/#format_preview) flag, promoting them to stable through minor releases, in accordance with our [versioning policy](https://github.com/astral-sh/ruff/discussions/6998#discussioncomment-7016766).

### [F-string formatting](#f-string-formatting)

Stabilized in Ruff 0.9.0

Unlike Black, Ruff formats the expression parts of f-strings which are the parts inside the curly braces `{...}`. This is a [known deviation](black/#f-strings) from Black.

Ruff employs several heuristics to determine how an f-string should be formatted which are detailed below.

#### [Quotes](#quotes)

Ruff will use the [configured quote style](../settings/#format_quote-style) for the f-string expression unless doing so would result in invalid syntax for the target Python version or requires more backslash escapes than the original expression. Specifically, Ruff will preserve the original quote style for the following cases:

When the target Python version is < 3.12 and a [self-documenting f-string](https://realpython.com/python-f-strings/#self-documenting-expressions-for-debugging) contains a string literal with the [configured quote style](../settings/#format_quote-style):

```
#__codelineno-14-1# format.quote-style = "double"
#__codelineno-14-2
#__codelineno-14-3f'{10 + len("hello")=}'
#__codelineno-14-4# This f-string cannot be formatted as follows when targeting Python < 3.12
#__codelineno-14-5f"{10 + len("hello")=}"
```

When the target Python version is < 3.12 and an f-string contains any triple-quoted string, byte or f-string literal that contains the [configured quote style](../settings/#format_quote-style):

```
#__codelineno-15-1# format.quote-style = "double"
#__codelineno-15-2
#__codelineno-15-3f'{"""nested " """}'
#__codelineno-15-4# This f-string cannot be formatted as follows when targeting Python < 3.12
#__codelineno-15-5f"{'''nested " '''}"
```

For all target Python versions, when a [self-documenting f-string](https://realpython.com/python-f-strings/#self-documenting-expressions-for-debugging) contains an expression between the curly braces (`{...}`) with a format specifier containing the [configured quote style](../settings/#format_quote-style):

```
#__codelineno-16-1# format.quote-style = "double"
#__codelineno-16-2
#__codelineno-16-3f'{1=:"foo}'
#__codelineno-16-4# This f-string cannot be formatted as follows for all target Python versions
#__codelineno-16-5f"{1=:"foo}"
```

For nested f-strings, Ruff alternates quote styles, starting with the [configured quote style](../settings/#format_quote-style) for the outermost f-string. For example, consider the following f-string:

```
#__codelineno-17-1# format.quote-style = "double"
#__codelineno-17-2
#__codelineno-17-3f"outer f-string {f"nested f-string {f"another nested f-string"} end"} end"
```

Ruff formats it as:

```
#__codelineno-18-1f"outer f-string {f'nested f-string {f"another nested f-string"} end'} end"
```

#### [Line breaks](#line-breaks)

Starting with Python 3.12 ([PEP 701](https://peps.python.org/pep-0701/)), the expression parts of an f-string can span multiple lines. Ruff needs to decide when to introduce a line break in an f-string expression. This depends on the semantic content of the expression parts of an f-string - for example, introducing a line break in the middle of a natural-language sentence is undesirable. Since Ruff doesn't have enough information to make that decision, it adopts a heuristic similar to [Prettier](https://prettier.io/docs/en/next/rationale.html#template-literals): it will only split the expression parts of an f-string across multiple lines if there was already a line break within any of the expression parts.

For example, the following code:

```
#__codelineno-19-1f"this f-string has a multiline expression {
#__codelineno-19-2  ['red', 'green', 'blue', 'yellow',]} and does not fit within the line length"
```

... is formatted as:

```
#__codelineno-20-1# The list expression is split across multiple lines because of the trailing comma
#__codelineno-20-2f"this f-string has a multiline expression {
#__codelineno-20-3    [
#__codelineno-20-4        'red',
#__codelineno-20-5        'green',
#__codelineno-20-6        'blue',
#__codelineno-20-7        'yellow',
#__codelineno-20-8    ]
#__codelineno-20-9} and does not fit within the line length"
```

But, the following will not be split across multiple lines even though it exceeds the line length:

```
#__codelineno-21-1f"this f-string has a multiline expression {['red', 'green', 'blue', 'yellow']} and does not fit within the line length"
```

If you want Ruff to split an f-string across multiple lines, ensure there's a linebreak somewhere within the `{...}` parts of an f-string.

#### [Fluent layout for method chains](#fluent-layout-for-method-chains)

At times, when developers write long chains of methods on an object, such as

```
#__codelineno-22-1x = df.filter(cond).agg(func).merge(other)
```

the intent is to perform a sequence of transformations or operations on a fixed object of interest - in this example, the object `df`. Assuming the assigned expression exceeds the `line-length`, this preview style will format the above as:

```
#__codelineno-23-1x = (
#__codelineno-23-2    df
#__codelineno-23-3    .filter(cond)
#__codelineno-23-4    .agg(func)
#__codelineno-23-5    .merge(other)
#__codelineno-23-6)
```

This deviates from the stable formatting, and also from Black, both of which would produce:

```
#__codelineno-24-1x = (
#__codelineno-24-2    df.filter(cond)
#__codelineno-24-3    .agg(func)
#__codelineno-24-4    .merge(other)
#__codelineno-24-5)
```

Both the stable and preview formatting are variants of something called a fluent layout.

In general, this preview style differs from the stable style only at the first attribute that precedes a call or subscript. The preview formatting breaks before this attribute, while the stable formatting breaks after the call or subscript.

## [Sorting imports](#sorting-imports)

Currently, the Ruff formatter does not sort imports. In order to both sort imports and format, call the Ruff linter and then the formatter:

```
#__codelineno-25-1ruff check --select I --fix
#__codelineno-25-2ruff format
```

A unified command for both linting and formatting is [planned](https://github.com/astral-sh/ruff/issues/8232).

 Back to top
