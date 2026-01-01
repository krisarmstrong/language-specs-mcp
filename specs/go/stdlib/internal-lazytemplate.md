package lazytemplate // import "internal/lazytemplate"

Package lazytemplate is a thin wrapper over text/template, allowing the use of
global template variables without forcing them to be parsed at init.

TYPES

type Template struct {
	// Has unexported fields.
}
    Template is a wrapper around text/template.Template, where the underlying
    template will be parsed the first time it is needed.

func New(name, text string) *Template
    New creates a new lazy template, delaying the parsing work until it is first
    needed. If the code is being run as part of tests, the template parsing will
    happen immediately.

func (r *Template) Execute(w io.Writer, data any) error

