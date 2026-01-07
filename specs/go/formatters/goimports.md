Michael Whatcott on "GoSublime + GoImports = :)"

# [🏠  Michael Whatcott](/)

## GoSublime + GoImports = :)

## Had enough? -- build failed: imported and not used: 'fmt' --

25 December 2013[programming](/topics/#programming)[golang](/topics/#golang)[dev-tools](/topics/#dev-tools)[sublime-text](/topics/#sublime-text)[goland](/topics/#goland)[jetbrains](/topics/#jetbrains)

# TL;DR

[JetBrains](https://www.jetbrains.com) now has an IDE for Go (called [GoLand](https://www.jetbrains.com/go/)) which resolves missing imports on the fly and will remove superfluous imports as well, all out-of-the-box. If you're already on the JetBrains bandwagon, just install GoLand and you're off to the races. Otherwise, read on...

It bothers me to no end that the go compiler throws a fit when an extra import statement is left around. I realize that the go authors had important reasons for this and I don't mean to start a flame war but I still wish that another tool (go vet?) did the job of warning us of extra stuff (imports, variables, etc...) being left around in the code and allow us to go on our merry (read: sloppy) way.

[Brad Fitz](https://github.com/bradfitz) has come to our rescue by creating a tool that does everything `go fmt` does and it also helps with adding/removing imports: [goimports](https://github.com/bradfitz/goimports). This tool can be invoked from [GoSublime](https://github.com/DisposaBoy/GoSublime), a plugin for [Sublime Text](http://www.sublimetext.com/3). I’ve anxiously awaited this addition to GoSublime for a [little while now](https://github.com/DisposaBoy/GoSublime/issues/362). Here’s how to get it working:

1. Make sure `$GOPATH/bin` is in your `$PATH` (Windows: `%GOPATH%\bin` goes in your `%PATH%`).
2. Run `go get -u golang.org/x/tools/cmd/goimports` (you may have to install [mercurial](http://mercurial.selenic.com/)).
3. Install Sublime Text and GoSublime (or make sure you've got the latest update if it's already installed).
4. Open the gosublime user config/preference file (Mac: `⌘. ⌘5` Windows: `Ctrl+. Ctrl+5`). Make sure you keep the command button down for the whole shortcut sequence.
5. Make it look like this:

```
{
	"fmt_cmd": ["goimports"]
}
```

Now, when you save, imports from the standard library will be resolved/removed as necessary. No more build errors related to package imports!

NOTE: If Sublime Text isn't seeing your configured GOPATH or PATH (and is therefore not seeing `goimports` as a result), try using this as the contents of your gosublime config/preference file:

```
{
    "fmt_cmd": ["goimports"],
    "env": {
        "GOPATH": "/your/gopath/here"
    }
}
```
