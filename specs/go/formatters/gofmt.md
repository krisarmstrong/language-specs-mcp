1. [Discover Packages](/)
2. [Standard library](/std)
3. [cmd](/cmd)
4. [gofmt](/cmd/gofmt@go1.25.5)

https://go.dev/

# gofmt

commandstandard library[Version: 
        go1.25.5](?tab=versions) Opens a new window with list of versions in this module. Latest Latest 

This package is not in the latest version of its module.

[Go to latest](/cmd/gofmt) Published: Dec 2, 2025  License: [BSD-3-Clause](/cmd/gofmt?tab=licenses) Opens a new window with license information. [Imports: 24](/cmd/gofmt?tab=imports) Opens a new window with list of imports. [Imported by: 0](/cmd/gofmt?tab=importedby) Opens a new window with list of known importers. Main Versions  Licenses  Imports  Imported By 

## Details

-  Valid [go.mod](https://cs.opensource.google/go/go/+/go1.25.5:src/go.mod) file 

 The Go module system was introduced in Go 1.11 and is the official dependency management solution for Go. 

-  Redistributable license 

 Redistributable licenses place minimal restrictions on how software can be used, modified, and redistributed. 

-  Tagged version 

Modules with tagged versions give importers more predictable builds.

-  Stable version 

When a project reaches major version v1 it is considered stable.

- [Learn more about best practices](/about#best-practices)

## Repository

[cs.opensource.google/go/go](https://cs.opensource.google/go/go)

## Links

- [Report a Vulnerability](https://go.dev/security/policy)
- [Open Source Insights](https://deps.dev/go/std/go1.25.5)

 Jump to ... 

- [Documentation](#section-documentation)

  - [Overview](#pkg-overview)
  - [Notes](#pkg-notes)

    - [Bugs](#pkg-note-BUG)

- [Source Files](#section-sourcefiles)

Documentation

##  Documentation [¶](#section-documentation)

[Rendered for](https://go.dev/about#build-context)linux/amd64windows/amd64darwin/amd64js/wasm

### Overview [¶](#pkg-overview)

- [Examples](#hdr-Examples)
- [The simplify command](#hdr-The_simplify_command)

Gofmt formats Go programs. It uses tabs for indentation and blanks for alignment. Alignment assumes that an editor is using a fixed-width font. 

Without an explicit path, it processes the standard input. Given a file, it operates on that file; given a directory, it operates on all .go files in that directory, recursively. (Files starting with a period are ignored.) By default, gofmt prints the reformatted sources to standard output. 

Usage: 

```
gofmt [flags] [path ...]
```

The flags are: 

```
-d
	Do not print reformatted sources to standard output.
	If a file's formatting is different than gofmt's, print diffs
	to standard output.
-e
	Print all (including spurious) errors.
-l
	Do not print reformatted sources to standard output.
	If a file's formatting is different from gofmt's, print its name
	to standard output.
-r rule
	Apply the rewrite rule to the source before reformatting.
-s
	Try to simplify code (after applying the rewrite rule, if any).
-w
	Do not print reformatted sources to standard output.
	If a file's formatting is different from gofmt's, overwrite it
	with gofmt's version. If an error occurred during overwriting,
	the original file is restored from an automatic backup.
```

Debugging support: 

```
-cpuprofile filename
	Write cpu profile to the specified file.
```

The rewrite rule specified with the -r flag must be a string of the form: 

```
pattern -> replacement
```

Both pattern and replacement must be valid Go expressions. In the pattern, single-character lowercase identifiers serve as wildcards matching arbitrary sub-expressions; those expressions will be substituted for the same identifiers in the replacement. 

When gofmt reads from standard input, it accepts either a full Go program or a program fragment. A program fragment must be a syntactically valid declaration list, statement list, or expression. When formatting such a fragment, gofmt preserves leading indentation as well as leading and trailing spaces, so that individual sections of a Go program can be formatted by piping them through gofmt. 

#### Examples [¶](#hdr-Examples)

To check files for unnecessary parentheses: 

```
gofmt -r '(a) -> a' -l *.go
```

To remove the parentheses: 

```
gofmt -r '(a) -> a' -w *.go
```

To convert the package tree from explicit slice upper bounds to implicit ones: 

```
gofmt -r 'α[β:len(α)] -> α[β:]' -w $GOROOT/src
```

#### The simplify command [¶](#hdr-The_simplify_command)

When invoked with -s gofmt will make the following source transformations where possible. 

```
An array, slice, or map composite literal of the form:
	[]T{T{}, T{}}
will be simplified to:
	[]T{{}, {}}

A slice expression of the form:
	s[a:len(s)]
will be simplified to:
	s[a:]

A range of the form:
	for x, _ = range v {...}
will be simplified to:
	for x = range v {...}

A range of the form:
	for _ = range v {...}
will be simplified to:
	for range v {...}
```

This may result in changes that are incompatible with earlier versions of Go. 

### Notes [¶](#pkg-notes)

### Bugs [¶](#pkg-note-BUG)

- 

The implementation of -r is a bit slow. 

- 

If -w fails, the restored original file may not have some of the original file attributes. 

##  Source Files [¶](#section-sourcefiles)

[View all Source files](https://cs.opensource.google/go/go/+/go1.25.5:src/cmd/gofmt)

- [doc.go](https://cs.opensource.google/go/go/+/go1.25.5:src/cmd/gofmt/doc.go)
- [gofmt.go](https://cs.opensource.google/go/go/+/go1.25.5:src/cmd/gofmt/gofmt.go)
- [internal.go](https://cs.opensource.google/go/go/+/go1.25.5:src/cmd/gofmt/internal.go)
- [rewrite.go](https://cs.opensource.google/go/go/+/go1.25.5:src/cmd/gofmt/rewrite.go)
- [simplify.go](https://cs.opensource.google/go/go/+/go1.25.5:src/cmd/gofmt/simplify.go)

 Click to show internal directories.  Click to hide internal directories.
