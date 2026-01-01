package srcimporter // import "go/internal/srcimporter"

Package srcimporter implements importing directly from source files rather than
installed packages.

TYPES

type Importer struct {
	// Has unexported fields.
}
    An Importer provides the context for importing packages from source code.

func New(ctxt *build.Context, fset *token.FileSet, packages map[string]*types.Package) *Importer
    New returns a new Importer for the given context, file set, and map of
    packages. The context is used to resolve import paths to package paths,
    and identifying the files belonging to the package. If the context provides
    non-nil file system functions, they are used instead of the regular package
    os functions. The file set is used to track position information of package
    files; and imported packages are added to the packages map.

func (p *Importer) Import(path string) (*types.Package, error)
    Import(path) is a shortcut for ImportFrom(path, ".", 0).

func (p *Importer) ImportFrom(path, srcDir string, mode types.ImportMode) (*types.Package, error)
    ImportFrom imports the package with the given import path resolved from the
    given srcDir, adds the new package to the set of packages maintained by the
    importer, and returns the package. Package path resolution and file system
    operations are controlled by the context maintained with the importer.
    The import mode must be zero but is otherwise ignored. Packages that are
    not comprised entirely of pure Go files may fail to import because the type
    checker may not be able to determine all exported entities (e.g. due to cgo
    dependencies).

