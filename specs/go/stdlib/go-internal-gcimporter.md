package gcimporter // import "go/internal/gcimporter"

Package gcimporter implements Import for gc-generated object files.

FUNCTIONS

func Import(fset *token.FileSet, packages map[string]*types.Package, path, srcDir string, lookup func(path string) (io.ReadCloser, error)) (pkg *types.Package, err error)
    Import imports a gc-generated package given its import path and srcDir,
    adds the corresponding package object to the packages map, and returns the
    object. The packages map must contain all packages already imported.

