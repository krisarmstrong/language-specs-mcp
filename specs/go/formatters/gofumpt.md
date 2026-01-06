[mvdan](/mvdan)/[gofumpt](/mvdan/gofumpt)Public

- 

###  Uh oh! 

There was an error while loading. Please reload this page.

- [Notifications](/login?return_to=%2Fmvdan%2Fgofumpt)You must be signed in to change notification settings
- [Fork
    124](/login?return_to=%2Fmvdan%2Fgofumpt)
- [Star
          3.8k](/login?return_to=%2Fmvdan%2Fgofumpt)

 A stricter gofmt 

[pkg.go.dev/mvdan.cc/gofumpt](https://pkg.go.dev/mvdan.cc/gofumpt)

### License

 BSD-3-Clause, BSD-3-Clause licenses found 

### Licenses found

[BSD-3-Clause
              LICENSE](/mvdan/gofumpt/blob/master/./LICENSE)[BSD-3-Clause
              LICENSE.google](/mvdan/gofumpt/blob/master/./LICENSE.google)[3.8k
          stars](/mvdan/gofumpt/stargazers)[124
          forks](/mvdan/gofumpt/forks)[Branches](/mvdan/gofumpt/branches)[Tags](/mvdan/gofumpt/tags)[Activity](/mvdan/gofumpt/activity)[Star](/login?return_to=%2Fmvdan%2Fgofumpt)[Notifications](/login?return_to=%2Fmvdan%2Fgofumpt)You must be signed in to change notification settings

- [Code](/mvdan/gofumpt)
- [Issues
          28](/mvdan/gofumpt/issues)
- [Pull requests
          1](/mvdan/gofumpt/pulls)
- [Discussions](/mvdan/gofumpt/discussions)
- [Actions](/mvdan/gofumpt/actions)
- 

### 

[Security
          
  
  
    
  
    
      

              Uh oh!

              There was an error while loading. Please reload this page](/mvdan/gofumpt/security).

- [Insights](/mvdan/gofumpt/pulse)

Additional navigation options

- [Code](/mvdan/gofumpt)
- [Issues](/mvdan/gofumpt/issues)
- [Pull requests](/mvdan/gofumpt/pulls)
- [Discussions](/mvdan/gofumpt/discussions)
- [Actions](/mvdan/gofumpt/actions)
- [Security](/mvdan/gofumpt/security)
- [Insights](/mvdan/gofumpt/pulse)

# mvdan/gofumpt
Version: 0.9.2

Source: https://github.com/mvdan/gofumpt


master[Branches](/mvdan/gofumpt/branches)[Tags](/mvdan/gofumpt/tags)/mvdan/gofumpt/branches/mvdan/gofumpt/tagsGo to fileCodeOpen more actions menu

## Folders and files

NameNameLast commit messageLast commit date

## Latest commit

## History

[316 Commits](/mvdan/gofumpt/commits/master/)/mvdan/gofumpt/commits/master/[.github](/mvdan/gofumpt/tree/master/.github)[.github](/mvdan/gofumpt/tree/master/.github)[format](/mvdan/gofumpt/tree/master/format)[format](/mvdan/gofumpt/tree/master/format)[internal](/mvdan/gofumpt/tree/master/internal)[internal](/mvdan/gofumpt/tree/master/internal)[testdata](/mvdan/gofumpt/tree/master/testdata)[testdata](/mvdan/gofumpt/tree/master/testdata)[.gitattributes](/mvdan/gofumpt/blob/master/.gitattributes)[.gitattributes](/mvdan/gofumpt/blob/master/.gitattributes)[CHANGELOG.md](/mvdan/gofumpt/blob/master/CHANGELOG.md)[CHANGELOG.md](/mvdan/gofumpt/blob/master/CHANGELOG.md)[LICENSE](/mvdan/gofumpt/blob/master/LICENSE)[LICENSE](/mvdan/gofumpt/blob/master/LICENSE)[LICENSE.google](/mvdan/gofumpt/blob/master/LICENSE.google)[LICENSE.google](/mvdan/gofumpt/blob/master/LICENSE.google)[README.md](/mvdan/gofumpt/blob/master/README.md)[README.md](/mvdan/gofumpt/blob/master/README.md)[doc.go](/mvdan/gofumpt/blob/master/doc.go)[doc.go](/mvdan/gofumpt/blob/master/doc.go)[gen_govendor.go](/mvdan/gofumpt/blob/master/gen_govendor.go)[gen_govendor.go](/mvdan/gofumpt/blob/master/gen_govendor.go)[go.mod](/mvdan/gofumpt/blob/master/go.mod)[go.mod](/mvdan/gofumpt/blob/master/go.mod)[go.sum](/mvdan/gofumpt/blob/master/go.sum)[go.sum](/mvdan/gofumpt/blob/master/go.sum)[gofmt.go](/mvdan/gofumpt/blob/master/gofmt.go)[gofmt.go](/mvdan/gofumpt/blob/master/gofmt.go)[internal.go](/mvdan/gofumpt/blob/master/internal.go)[internal.go](/mvdan/gofumpt/blob/master/internal.go)[main_test.go](/mvdan/gofumpt/blob/master/main_test.go)[main_test.go](/mvdan/gofumpt/blob/master/main_test.go)[ulimit_linux_test.go](/mvdan/gofumpt/blob/master/ulimit_linux_test.go)[ulimit_linux_test.go](/mvdan/gofumpt/blob/master/ulimit_linux_test.go)View all files

## Repository files navigation

- [README](#)
- [BSD-3-Clause license](#)
- [BSD-3-Clause license](#)

# gofumpt

#gofumpt

https://pkg.go.dev/mvdan.cc/gofumpt/format

```
go install mvdan.cc/gofumpt@latest
```

Enforce a stricter format than `gofmt`, while being backwards compatible. That is, `gofumpt` is happy with a subset of the formats that `gofmt` is happy with.

The tool is a fork of `gofmt` as of Go 1.25.0, and requires Go 1.24 or later. It can be used as a drop-in replacement to format your Go code, and running `gofmt` after `gofumpt` should produce no changes. For example:

```
gofumpt -l -w .
```

Some of the Go source files in this repository belong to the Go project. The project includes copies of `go/printer` and `go/doc/comment` as of Go 1.25.0 to ensure consistent formatting independent of what Go version is being used. The [added formatting rules](#Added-rules) are implemented in the `format` package.

`vendor` and `testdata` directories are skipped unless given as explicit arguments. Similarly, the added rules do not apply to generated Go files unless they are given as explicit arguments.

[ignore directives](https://go.dev/ref/mod#go-mod-file-ignore) in `go.mod` files are obeyed as well, unless directories or files within them are given as explicit arguments.

Finally, note that the `-r` rewrite flag is removed in favor of `gofmt -r`, and the `-s` flag is hidden as it is always enabled.

### Added rules

#added-rules

No empty lines following an assignment operator

Example

```
func foo() {
    foo :=
        "bar"
}
```

```
func foo() {
	foo := "bar"
}
```

No empty lines around function bodies

Example

```
func foo() {

	println("bar")

}
```

```
func foo() {
	println("bar")
}
```

Functions should separate `) {` where the indentation helps readability

Example

```
func foo(s string,
	i int) {
	println("bar")
}

// With an empty line it's slightly better, but still not great.
func bar(s string,
	i int) {

	println("bar")
}
```

```
func foo(s string,
	i int,
) {
	println("bar")
}

// With an empty line it's slightly better, but still not great.
func bar(s string,
	i int,
) {
	println("bar")
}
```

No empty lines around a lone statement (or comment) in a block

Example

```
if err != nil {

	return err
}
```

```
if err != nil {
	return err
}
```

No empty lines before a simple error check

Example

```
foo, err := processFoo()

if err != nil {
	return err
}
```

```
foo, err := processFoo()
if err != nil {
	return err
}
```

Composite literals should use newlines consistently

Example

```
// A newline before or after an element requires newlines for the opening and
// closing braces.
var ints = []int{1, 2,
	3, 4}

// A newline between consecutive elements requires a newline between all
// elements.
var matrix = [][]int{
	{1},
	{2}, {
		3,
	},
}
```

```
var ints = []int{
	1, 2,
	3, 4,
}

var matrix = [][]int{
	{1},
	{2},
	{
		3,
	},
}
```

Empty field lists should use a single line

Example

```
var V interface {
} = 3

type T struct {
}

func F(
)
```

```
var V interface{} = 3

type T struct{}

func F()
```

`std` imports must be in a separate group at the top

Example

```
import (
	"foo.com/bar"

	"io"

	"io/ioutil"
)
```

```
import (
	"io"
	"io/ioutil"

	"foo.com/bar"
)
```

Short case clauses should take a single line

Example

```
switch c {
case 'a', 'b',
	'c', 'd':
}
```

```
switch c {
case 'a', 'b', 'c', 'd':
}
```

Multiline top-level declarations must be separated by empty lines

Example

```
func foo() {
	println("multiline foo")
}
func bar() {
	println("multiline bar")
}
```

```
func foo() {
	println("multiline foo")
}

func bar() {
	println("multiline bar")
}
```

Single var declarations should not be grouped with parentheses

Example

```
var (
	foo = "bar"
)
```

```
var foo = "bar"
```

Contiguous top-level declarations should be grouped together

Example

```
var nicer = "x"
var with = "y"
var alignment = "z"
```

```
var (
	nicer     = "x"
	with      = "y"
	alignment = "z"
)
```

Simple var-declaration statements should use short assignments

Example

```
var s = "somestring"
```

```
s := "somestring"
```

The `-s` code simplification flag is enabled by default

Example

```
var _ = [][]int{[]int{1}}
```

```
var _ = [][]int{{1}}
```

Octal integer literals should use the `0o` prefix on modules using Go 1.13 and later

Example

```
const perm = 0755
```

```
const perm = 0o755
```

Comments which aren't Go directives should start with a whitespace

Example

```
//go:noinline

//Foo is awesome.
func Foo() {}
```

```
//go:noinline

// Foo is awesome.
func Foo() {}
```

Composite literals should not have leading or trailing empty lines

Example

```
var _ = []string{

	"foo",

}

var _ = map[string]string{

	"foo": "bar",

}
```

```
var _ = []string{
	"foo",
}

var _ = map[string]string{
	"foo": "bar",
}
```

Field lists should not have leading or trailing empty lines

Example

```
type Person interface {

	Name() string

	Age() int

}

type ZeroFields struct {

	// No fields are needed here.

}
```

```
type Person interface {
	Name() string

	Age() int
}

type ZeroFields struct {
	// No fields are needed here.
}
```

### Extra rules behind `-extra`

#extra-rules-behind--extra

Adjacent parameters with the same type should be grouped together

Example

```
func Foo(bar string, baz string) {}
```

```
func Foo(bar, baz string) {}
```

Avoid naked returns for the sake of clarity

Example

```
func Foo() (err error) {
	return
}
```

```
func Foo() (err error) {
	return err
}
```

### Installation

#installation

`gofumpt` is a replacement for `gofmt`, so you can simply `go install` it as described at the top of this README and use it.

When using an IDE or editor with Go integration based on `gopls`, it's best to configure the editor to use the `gofumpt` support built into `gopls`.

The instructions below show how to set up `gofumpt` for some of the major editors out there.

#### Visual Studio Code

#visual-studio-code

Enable the language server following [the official docs](https://github.com/golang/vscode-go#readme), and then enable gopls's `gofumpt` option. Note that VS Code will complain about the `gopls` settings, but they will still work.

```
"go.useLanguageServer": true,
"gopls": {
	"formatting.gofumpt": true,
},
```

#### GoLand

#goland

GoLand doesn't use `gopls` so it should be configured to use `gofumpt` directly. Once `gofumpt` is installed, follow the steps below:

- Open Settings (File > Settings)
- Open the Tools section
- Find the File Watchers sub-section
- Click on the `+` on the right side to add a new file watcher
- Choose Custom Template

When a window asks for settings, you can enter the following:

- File Types: Select all .go files
- Scope: Project Files
- Program: Select your `gofumpt` executable
- Arguments: `-w $FilePath$`
- Output path to refresh: `$FilePath$`
- Working directory: `$ProjectFileDir$`
- Environment variables: `GOROOT=$GOROOT$;GOPATH=$GOPATH$;PATH=$GoBinDirs$`

To avoid unnecessary runs, you should disable all checkboxes in the Advanced section.

#### Vim

#vim

The configuration depends on the plugin you are using: [vim-go](https://github.com/fatih/vim-go) or [govim](https://github.com/govim/govim).

##### vim-go

#vim-go

To configure `gopls` to use `gofumpt`:

```
let g:go_fmt_command="gopls"
let g:go_gopls_gofumpt=1
```

##### govim

#govim

To configure `gopls` to use `gofumpt`:

```
call govim#config#Set("Gofumpt", 1)
```

#### Neovim

#neovim

When using [lspconfig](https://github.com/neovim/nvim-lspconfig), pass the `gofumpt` setting to `gopls`:

```
require('lspconfig').gopls.setup({
    settings = {
        gopls = {
            gofumpt = true
        }
    }
})
```

#### Emacs

#emacs

For [lsp-mode](https://emacs-lsp.github.io/lsp-mode/) users on version 8.0.0 or higher:

```
(setq lsp-go-use-gofumpt t)
```

For users of `lsp-mode` before `8.0.0`:

```
(lsp-register-custom-settings
 '(("gopls.gofumpt" t)))
```

For [eglot](https://github.com/joaotavora/eglot) users:

```
(setq-default eglot-workspace-configuration
 '((:gopls . ((gofumpt . t)))))
```

#### Helix

#helix

When using the `gopls` language server, modify the Go settings in `~/.config/helix/languages.toml`:

```
[language-server.gopls.config]
"formatting.gofumpt" = true
```

#### Sublime Text

#sublime-text

With ST4, install the Sublime Text LSP extension according to [the documentation](https://github.com/sublimelsp/LSP), and enable `gopls`'s `gofumpt` option in the LSP package settings, including setting `lsp_format_on_save` to `true`.

```
"lsp_format_on_save": true,
"clients":
{
	"gopls":
	{
		"enabled": true,
		"initializationOptions": {
			"gofumpt": true,
		}
	}
}
```

### Zed

#zed

For `gofumpt` to be used in Zed, you need to set the `gofumpt` option in the LSP settings. This is done by providing the `"gofumpt": true` in `initialization_options`.

```
"lsp": {
  "gopls": {
    "initialization_options": {
      "gofumpt": true
    }
  }
}
```

### Roadmap

#roadmap

This tool is a place to experiment. In the long term, the features that work well might be proposed for `gofmt` itself.

The tool is also compatible with `gofmt` and is aimed to be stable, so you can rely on it for your code as long as you pin a version of it.

### Frequently Asked Questions

#frequently-asked-questions

Why attempt to replace `gofmt` instead of building on top of it?

Our design is to build on top of `gofmt`, and we'll never add rules which disagree with its formatting. So we extend `gofmt` rather than compete with it.

The tool is a modified copy of `gofmt`, for the purpose of allowing its use as a drop-in replacement in editors and scripts.

Why are my module imports being grouped with standard library imports?

Any import paths that don't start with a domain name like `foo.com` are effectively [reserved by the Go toolchain](https://github.com/golang/go/issues/32819). Third party modules should either start with a domain name, even a local one like `foo.local`, or use [a reserved path prefix](https://github.com/golang/go/issues/37641).

For backwards compatibility with modules set up before these rules were clear, `gofumpt` will treat any import path sharing a prefix with the current module path as third party. For example, if the current module is `mycorp/mod1`, then all import paths in `mycorp/...` will be considered third party.

How can I use `gofumpt` if I already use `goimports` to replace `gofmt`?

Most editors have replaced the `goimports` program with the same functionality provided by a language server like `gopls`. This mechanism is significantly faster and more powerful, since the language server has more information that is kept up to date, necessary to add missing imports.

As such, the general recommendation is to let your editor fix your imports - either via `gopls`, such as VSCode or vim-go, or via their own custom implementation, such as GoLand. Then follow the install instructions above to enable the use of `gofumpt` instead of `gofmt`.

If you want to avoid integrating with `gopls`, and are OK with the overhead of calling `goimports` from scratch on each save, you should be able to call both tools; for example, `goimports file.go && gofumpt file.go`.

### Contributing

#contributing

Issues and pull requests are welcome! Please open an issue to discuss a feature before sending a pull request.

We also use the `#gofumpt` channel over at the [Gophers Slack](https://invite.slack.golangbridge.org/) to chat.

When reporting a formatting bug, insert a `//gofumpt:diagnose` comment. The comment will be rewritten to include useful debugging information. For instance:

```
$ cat f.go
package p

//gofumpt:diagnose
$ gofumpt f.go
package p

//gofumpt:diagnose v0.1.1-0.20211103104632-bdfa3b02e50a -lang=go1.16
```

### License

#license

Note that much of the code is copied from Go's `gofmt` command. You can tell which files originate from the Go repository from their copyright headers. Their license file is `LICENSE.google`.

`gofumpt`'s original source files are also under the 3-clause BSD license, with the separate file `LICENSE`.

## About

 A stricter gofmt 

[pkg.go.dev/mvdan.cc/gofumpt](https://pkg.go.dev/mvdan.cc/gofumpt)

### Topics

[go](/topics/go)[format](/topics/format)[style](/topics/style)[gofmt](/topics/gofmt)[goimports](/topics/goimports)[idiomatic](/topics/idiomatic)

### Resources

[Readme](#readme-ov-file)

### License

 BSD-3-Clause, BSD-3-Clause licenses found 

### Licenses found

[BSD-3-Clause
              LICENSE](/mvdan/gofumpt/blob/master/./LICENSE)[BSD-3-Clause
              LICENSE.google](/mvdan/gofumpt/blob/master/./LICENSE.google)

###  Uh oh! 

There was an error while loading. Please reload this page.

[Activity](/mvdan/gofumpt/activity)

### Stars

[3.8k
        stars](/mvdan/gofumpt/stargazers)

### Watchers

[12
        watching](/mvdan/gofumpt/watchers)

### Forks

[124
        forks](/mvdan/gofumpt/forks)[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fmvdan%2Fgofumpt&report=mvdan+%28user%29)

## [Releases
      14](/mvdan/gofumpt/releases)

[v0.9.2
        
          Latest
      
      Oct 21, 2025](/mvdan/gofumpt/releases/tag/v0.9.2)[+ 13 releases](/mvdan/gofumpt/releases)

## Sponsor this project

 Sponsor 

###  Uh oh! 

There was an error while loading. Please reload this page.

[Learn more about GitHub Sponsors](/sponsors)

## [Packages
      0](/users/mvdan/packages?repo_name=gofumpt)

 No packages published 

## [Used by 13.6k](/mvdan/gofumpt/network/dependents)

- 
- 
- 
- 
- 
- 
- 
- 

[+ 13,585](/mvdan/gofumpt/network/dependents)

## [Contributors
      42](/mvdan/gofumpt/graphs/contributors)

- https://github.com/mvdan
- https://github.com/tsnewaz
- https://github.com/twpayne
- https://github.com/scop
- https://github.com/tklauser
- https://github.com/jakebailey
- https://github.com/ebati
- https://github.com/adamroyjones
- https://github.com/AlekSi
- https://github.com/karelbilek
- https://github.com/moorereason
- https://github.com/muesli
- https://github.com/ravishi
- https://github.com/sbaildon

[+ 28 contributors](/mvdan/gofumpt/graphs/contributors)

## Languages

- [Go
          100.0%](/mvdan/gofumpt/search?l=go)
