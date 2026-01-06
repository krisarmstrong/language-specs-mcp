# The basics[¶](#the-basics)
Version: 25.12.0

Source: https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html


Foundational knowledge on using and configuring Black.

Black is a well-behaved Unix-style command-line tool:

- 

it does nothing if it finds no sources to format;

- 

it will read from standard input and write to standard output if `-` is used as the filename;

- 

it only outputs messages to users on standard error;

- 

exits with code 0 unless an internal error occurred or a CLI option prompted it.

## Usage[¶](#usage)

Black will reformat entire files in place. To get started right away with sensible defaults:

```
black {source_file_or_directory}
```

You can run Black as a package if running it as a script doesn’t work:

```
python -m black {source_file_or_directory}
```

### Ignoring sections[¶](#ignoring-sections)

Black will not reformat lines that contain `# fmt: skip` or blocks that start with `# fmt: off` and end with `# fmt: on`. `# fmt: skip` can be mixed with other pragmas/comments either with multiple comments (e.g. `# fmt: skip # pylint # noqa`) or as a semicolon separated list (e.g. `# fmt: skip; pylint; noqa`). `# fmt: on/off` must be on the same level of indentation and in the same block, meaning no unindents beyond the initial indentation level between them. Black also recognizes [YAPF](https://github.com/google/yapf)’s block comments to the same effect, as a courtesy for straddling code.

### Command line options[¶](#command-line-options)

The CLI options of Black can be displayed by running `black --help`. All options are also covered in more detail below.

While Black has quite a few knobs these days, it is still opinionated so style options are deliberately limited and rarely added.

Note that all command-line options listed above can also be configured using a `pyproject.toml` file (more on that below).

#### `-h`, `--help`[¶](#h-help)

Show available command-line options and exit.

#### `-c`, `--code`[¶](#c-code)

Format the code passed in as a string.

```
$ black --code "print ( 'hello, world' )"
print("hello, world")
```

#### `-l`, `--line-length`[¶](#l-line-length)

How many characters per line to allow. The default is 88.

See also [the style documentation](../the_black_code_style/current_style.html#labels-line-length).

#### `-t`, `--target-version`[¶](#t-target-version)

Python versions that should be supported by Black’s output. You can run `black --help` and look for the `--target-version` option to see the full list of supported versions. You should include all versions that your code supports. If you support Python 3.11 through 3.13, you should write:

```
$ black -t py311 -t py312 -t py313
```

In a [configuration file](#configuration-via-a-file), you can write:

```
target-version = ["py311", "py312", "py313"]
```

By default, Black will infer target versions from the project metadata in `pyproject.toml`, specifically the `[project.requires-python]` field. If this does not yield conclusive results, Black will use per-file auto-detection.

Black uses this option to decide what grammar to use to parse your code. In addition, it may use it to decide what style to use. For example, support for a trailing comma after `*args` in a function call was added in Python 3.5, so Black will add this comma only if the target versions are all Python 3.5 or higher:

```
$ black --line-length=10 --target-version=py35 -c 'f(a, *args)'
f(
    a,
    *args,
)
$ black --line-length=10 --target-version=py34 -c 'f(a, *args)'
f(
    a,
    *args
)
$ black --line-length=10 --target-version=py34 --target-version=py35 -c 'f(a, *args)'
f(
    a,
    *args
)
```

#### `--pyi`[¶](#pyi)

Format all input files like typing stubs regardless of file extension. This is useful when piping source on standard input.

#### `--ipynb`[¶](#ipynb)

Format all input files like Jupyter Notebooks regardless of file extension. This is useful when piping source on standard input.

#### `--python-cell-magics`[¶](#python-cell-magics)

When processing Jupyter Notebooks, add the given magic to the list of known python- magics. Useful for formatting cells with custom python magics.

#### `-x, --skip-source-first-line`[¶](#x-skip-source-first-line)

Skip the first line of the source code.

#### `-S, --skip-string-normalization`[¶](#s-skip-string-normalization)

By default, Black uses double quotes for all strings and normalizes string prefixes, as described in [the style documentation](../the_black_code_style/current_style.html#labels-strings). If this option is given, strings are left unchanged instead.

#### `-C, --skip-magic-trailing-comma`[¶](#c-skip-magic-trailing-comma)

By default, Black uses existing trailing commas as an indication that short lines should be left separate, as described in [the style documentation](../the_black_code_style/current_style.html#labels-magic-trailing-comma). If this option is given, the magic trailing comma is ignored.

#### `--preview`[¶](#preview)

Enable potentially disruptive style changes that we expect to add to Black’s main functionality in the next major release. Use this if you want a taste of what next year’s style will look like.

Read more about [our preview style](../the_black_code_style/future_style.html#labels-preview-style).

There is no guarantee on the code style produced by this flag across releases.

#### `--unstable`[¶](#unstable)

Enable all style changes in `--preview`, plus additional changes that we would like to make eventually, but that have known issues that need to be fixed before they can move back to the `--preview` style. Use this if you want to experiment with these changes and help fix issues with them.

There is no guarantee on the code style produced by this flag across releases.

#### `--enable-unstable-feature`[¶](#enable-unstable-feature)

Enable specific features from the `--unstable` style. See [the preview style documentation](../the_black_code_style/future_style.html#labels-unstable-features) for the list of supported features. This flag can only be used when `--preview` is enabled. Users are encouraged to use this flag if they use `--preview` style and a feature that affects their code is moved from the `--preview` to the `--unstable` style, but they want to avoid the thrash from undoing this change.

There are no guarantees on the behavior of these features, or even their existence, across releases.

#### `--check`[¶](#check)

Don’t write the files back, just return the status. Black will exit with:

- 

code 0 if nothing would change;

- 

code 1 if some files would be reformatted; or

- 

code 123 if there was an internal error

If used in combination with `--quiet` then only the exit code will be returned, unless there was an internal error.

```
$ black test.py --check
All done! ✨ 🍰 ✨
1 file would be left unchanged.
$ echo $?
0

$ black test.py --check
would reformat test.py
Oh no! 💥 💔 💥
1 file would be reformatted.
$ echo $?
1

$ black test.py --check
error: cannot format test.py: INTERNAL ERROR: Black produced code that is not equivalent to the source.  Please report a bug on https://github.com/psf/black/issues.  This diff might be helpful: /tmp/blk_kjdr1oog.log
Oh no! 💥 💔 💥
1 file would fail to reformat.
$ echo $?
123
```

#### `--diff`[¶](#diff)

Don’t write the files back, just output a diff to indicate what changes Black would’ve made. They are printed to stdout so capturing them is simple.

If you’d like colored diffs, you can enable them with `--color`.

```
$ black test.py --diff
--- test.py     2021-03-08 22:23:40.848954+00:00
+++ test.py     2021-03-08 22:23:47.126319+00:00
@@ -1 +1 @@
-print ( 'hello, world' )
+print("hello, world")
would reformat test.py
All done! ✨ 🍰 ✨
1 file would be reformatted.
```

#### `--no-cache`[¶](#no-cache)

Do not consult or update Black’s per-user cache during this run. When `--no-cache` is specified, Black will perform fresh analysis for all files and will neither read from nor write to the cache. This is helpful for reproducing formatting results from a clean run, debugging cache-related issues, or ensuring CI executes a fresh formatting analysis every time.

#### `--color` / `--no-color`[¶](#color-no-color)

Show (or do not show) colored diff. Only applies when `--diff` is given.

#### `--line-ranges`[¶](#line-ranges)

When specified, Black will try its best to only format these lines.

This option can be specified multiple times, and a union of the lines will be formatted. Each range must be specified as two integers connected by a `-`: `<START>-<END>`. The `<START>` and `<END>` integer indices are 1-based and inclusive on both ends.

Black may still format lines outside of the ranges for multi-line statements. Formatting more than one file or any ipynb files with this option is not supported. This option cannot be specified in the `pyproject.toml` config.

Example: `black --line-ranges=1-10 --line-ranges=21-30 test.py` will format lines from `1` to `10` and `21` to `30`.

This option is mainly for editor integrations, such as “Format Selection”.

Note

Due to [#4052](https://github.com/psf/black/issues/4052), `--line-ranges` might format extra lines outside of the ranges when there are unformatted lines with the exact formatted content next to the requested lines. It also disables Black’s formatting stability check in `--safe` mode.

#### `--fast` / `--safe`[¶](#fast-safe)

By default, Black performs [an AST safety check](../the_black_code_style/current_style.html#labels-ast-changes) after formatting your code. The `--fast` flag turns off this check and the `--safe` flag explicitly enables it.

#### `--required-version`[¶](#required-version)

Require a specific version of Black to be running. This is useful for ensuring that all contributors to your project are using the same version, because different versions of Black may format code a little differently. This option can be set in a configuration file for consistent results across environments.

```
$ black --version
black, 25.12.0 (compiled: yes)
$ black --required-version 25.12.0 -c "format = 'this'"
format = "this"
$ black --required-version 31.5b2 -c "still = 'beta?!'"
Oh no! 💥 💔 💥 The required version does not match the running version!
```

You can also pass just the major version:

```
$ black --required-version 22 -c "format = 'this'"
format = "this"
$ black --required-version 31 -c "still = 'beta?!'"
Oh no! 💥 💔 💥 The required version does not match the running version!
```

Because of our [stability policy](../the_black_code_style/index.html), this will guarantee stable formatting, but still allow you to take advantage of improvements that do not affect formatting.

#### `--exclude`[¶](#exclude)

A regular expression that matches files and directories that should be excluded on recursive searches. An empty value means no paths are excluded. Use forward slashes for directories on all platforms (Windows, too). By default, Black also ignores all paths listed in `.gitignore`. Changing this value will override all default exclusions.

Default Exclusions: `['.direnv', '.eggs', '.git', '.hg', '.ipynb_checkpoints',  '.mypy_cache', '.nox', '.pytest_cache', '.ruff_cache', '.tox', '.svn', '.venv', '.vscode',  '__pypackages__', '_build', 'buck-out', 'build', 'dist', 'venv']`

If the regular expression contains newlines, it is treated as a [verbose regular expression](https://docs.python.org/3/library/re.html#re.VERBOSE). This is typically useful when setting these options in a `pyproject.toml` configuration file; see [Configuration format](#configuration-format) for more information.

#### `--extend-exclude`[¶](#extend-exclude)

Like `--exclude`, but adds additional files and directories on top of the default values instead of overriding them.

#### `--force-exclude`[¶](#force-exclude)

Like `--exclude`, but files and directories matching this regex will be excluded even when they are passed explicitly as arguments. This is useful when invoking Black programmatically on changed files, such as in a pre-commit hook or editor plugin.

#### `--stdin-filename`[¶](#stdin-filename)

The name of the file when passing it through stdin. Useful to make sure Black will respect the `--force-exclude` option on some editors that rely on using stdin.

#### `--include`[¶](#include)

A regular expression that matches files and directories that should be included on recursive searches. An empty value means all files are included regardless of the name. Use forward slashes for directories on all platforms (Windows, too). Overrides all exclusions, including from `.gitignore` and command line options.

Default Inclusions: `['.pyi', '.ipynb']`

#### `-W`, `--workers`[¶](#w-workers)

When Black formats multiple files, it may use a process pool to speed up formatting. This option controls the number of parallel workers. This can also be specified via the `BLACK_NUM_WORKERS` environment variable. Defaults to the number of CPUs in the system.

#### `-q`, `--quiet`[¶](#q-quiet)

Stop emitting all non-critical output. Error messages will still be emitted (which can silenced by `2>/dev/null`).

```
$ black src/ -q
error: cannot format src/black_primer/cli.py: Cannot parse: 5:6: mport asyncio
```

#### `-v`, `--verbose`[¶](#v-verbose)

Emit messages about files that were not changed or were ignored due to exclusion patterns. If Black is using a configuration file, a message detailing which one it is using will be emitted.

```
$ black src/ -v
Using configuration from /tmp/pyproject.toml.
src/blib2to3 ignored: matches the --extend-exclude regular expression
src/_black_version.py wasn't modified on disk since last run.
src/black/__main__.py wasn't modified on disk since last run.
error: cannot format src/black_primer/cli.py: Cannot parse: 5:6: mport asyncio
reformatted src/black_primer/lib.py
reformatted src/blackd/__init__.py
reformatted src/black/__init__.py
Oh no! 💥 💔 💥
3 files reformatted, 2 files left unchanged, 1 file failed to reformat
```

#### `--version`[¶](#version)

You can check the version of Black you have installed using the `--version` flag.

```
$ black --version
black, 25.12.0
```

#### `--config`[¶](#config)

Read configuration options from a configuration file. See [below](#configuration-via-a-file) for more details on the configuration file.

### Environment variable options[¶](#environment-variable-options)

Black supports the following configuration via environment variables.

#### `BLACK_CACHE_DIR`[¶](#black-cache-dir)

The directory where Black should store its cache.

#### `BLACK_NUM_WORKERS`[¶](#black-num-workers)

The number of parallel workers Black should use. The command line option `-W` / `--workers` takes precedence over this environment variable.

### Code input alternatives[¶](#code-input-alternatives)

Black supports formatting code via stdin, with the result being printed to stdout. Just let Black know with `-` as the path.

```
$ echo "print ( 'hello, world' )" | black -
print("hello, world")
reformatted -
All done! ✨ 🍰 ✨
1 file reformatted.
```

Tip: if you need Black to treat stdin input as a file passed directly via the CLI, use `--stdin-filename`. Useful to make sure Black will respect the `--force-exclude` option on some editors that rely on using stdin.

You can also pass code as a string using the `--code` option.

### Writeback and reporting[¶](#writeback-and-reporting)

By default Black reformats the files given and/or found in place. Sometimes you need Black to just tell you what it would do without actually rewriting the Python files.

There’s two variations to this mode that are independently enabled by their respective flags:

- 

`--check` (exit with code 1 if any file would be reformatted)

- 

`--diff` (print a diff instead of reformatting files)

Both variations can be enabled at once.

### Output verbosity[¶](#output-verbosity)

Black in general tries to produce the right amount of output, balancing between usefulness and conciseness. By default, Black emits files modified and error messages, plus a short summary.

```
$ black src/
error: cannot format src/black_primer/cli.py: Cannot parse: 5:6: mport asyncio
reformatted src/black_primer/lib.py
reformatted src/blackd/__init__.py
reformatted src/black/__init__.py
Oh no! 💥 💔 💥
3 files reformatted, 2 files left unchanged, 1 file failed to reformat.
```

The `--quiet` and `--verbose` flags control output verbosity.

## Configuration via a file[¶](#configuration-via-a-file)

Black is able to read project-specific default values for its command line options from a `pyproject.toml` file. This is especially useful for specifying custom `--include` and `--exclude`/`--force-exclude`/`--extend-exclude` patterns for your project.

Pro-tip: If you’re asking yourself “Do I need to configure anything?” the answer is “No”. Black is all about sensible defaults. Applying those defaults will have your code in compliance with many other Black formatted projects.

### What on Earth is a `pyproject.toml` file?[¶](#what-on-earth-is-a-pyproject-toml-file)

[PEP 518](https://www.python.org/dev/peps/pep-0518/) defines `pyproject.toml` as a configuration file to store build system requirements for Python projects. With the help of tools like [Poetry](https://python-poetry.org/), [Flit](https://flit.readthedocs.io/en/latest/), or [Hatch](https://hatch.pypa.io/latest/) it can fully replace the need for `setup.py` and `setup.cfg` files.

### Where Black looks for the file[¶](#where-black-looks-for-the-file)

By default Black looks for `pyproject.toml` containing a `[tool.black]` section starting from the common base directory of all files and directories passed on the command line. If it’s not there, it looks in parent directories. It stops looking when it finds the file, or a `.git` directory, or a `.hg` directory, or the root of the file system, whichever comes first.

If you’re formatting standard input, Black will look for configuration starting from the current working directory.

You can use a “global” configuration, stored in a specific location in your home directory. This will be used as a fallback configuration, that is, it will be used if and only if Black doesn’t find any configuration as mentioned above. Depending on your operating system, this configuration file should be stored as:

- 

Windows: `~\.black`

- 

Unix-like (Linux, MacOS, etc.): `$XDG_CONFIG_HOME/black` (`~/.config/black` if the `XDG_CONFIG_HOME` environment variable is not set)

Note that these are paths to the TOML file itself (meaning that they shouldn’t be named as `pyproject.toml`), not directories where you store the configuration (i.e., `black`/`.black` is the file to create and add your configuration options to, in the `~/.config/` directory). Here, `~` refers to the path to your home directory. On Windows, this will be something like `C:\\Users\UserName`.

You can also explicitly specify the path to a particular file that you want with `--config`. In this situation Black will not look for any other file.

If you’re running with `--verbose`, you will see a message if a file was found and used.

Please note `blackd` will not use `pyproject.toml` configuration.

### Configuration format[¶](#configuration-format)

As the file extension suggests, `pyproject.toml` is a [TOML](https://github.com/toml-lang/toml) file. It contains separate sections for different tools. Black is using the `[tool.black]` section. The option keys are the same as long names of options on the command line.

Note that you have to use single-quoted strings in TOML for regular expressions. It’s the equivalent of r-strings in Python. Multiline strings are treated as verbose regular expressions by Black. Use `[ ]` to denote a significant space character.

Example `pyproject.toml`

```
[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
# 'extend-exclude' excludes files or directories in addition to the defaults
extend-exclude = '''
# A regex preceded with ^/ will apply only to files and directories
# in the root of the project.
(
  ^/foo.py    # exclude a file named foo.py in the root of the project
  | .*_pb2.py  # exclude autogenerated Protocol Buffer files anywhere in the project
)
'''
```

### Lookup hierarchy[¶](#lookup-hierarchy)

Command-line options have defaults that you can see in `--help`. A `pyproject.toml` can override those defaults. Finally, options provided by the user on the command line override both.

Black will only ever use one `pyproject.toml` file during an entire run. It doesn’t look for multiple files, and doesn’t compose configuration from different levels of the file hierarchy.

## Next steps[¶](#next-steps)

A good next step would be configuring auto-discovery so `black .` is all you need instead of laborously listing every file or directory. You can get started by heading over to [File collection and discovery](file_collection_and_discovery.html).

Another good choice would be setting up an [integration with your editor](../integrations/editors.html) of choice or with [pre-commit for source version control](../integrations/source_version_control.html).
