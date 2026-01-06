Module[java.desktop](../../../module-summary.html)

# Package javax.swing.undo

package javax.swing.undoAllows developers to provide support for undo/redo in applications such as text editors. 

Note: Most of the Swing API is not thread safe. For details, see [Concurrency in Swing](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html), a section in [The Java Tutorial](https://docs.oracle.com/javase/tutorial/). 

## Related Documentation

 For overviews, tutorials, examples, guides, and tool documentation, please see: 

- [Implementing Undo and Redo](https://docs.oracle.com/javase/tutorial/uiswing/components/generaltext.html#undo), a section in The Java Tutorial

Since:1.2

- Related PackagesPackageDescription[javax.swing](../package-summary.html)Provides a set of "lightweight" (all-Java language) components that, to the maximum degree possible, work the same on all platforms.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[AbstractUndoableEdit](AbstractUndoableEdit.html)An abstract implementation of `UndoableEdit`, implementing simple responses to all boolean methods in that interface.[CannotRedoException](CannotRedoException.html)Thrown when an UndoableEdit is told to `redo()` and can't.[CannotUndoException](CannotUndoException.html)Thrown when an UndoableEdit is told to `undo()` and can't.[CompoundEdit](CompoundEdit.html)A concrete subclass of AbstractUndoableEdit, used to assemble little UndoableEdits into great big ones.[StateEdit](StateEdit.html)StateEdit is a general edit for objects that change state.[StateEditable](StateEditable.html)StateEditable defines the interface for objects that can have their state undone/redone by a StateEdit.[UndoableEdit](UndoableEdit.html)An `UndoableEdit` represents an edit.[UndoableEditSupport](UndoableEditSupport.html)A support class used for managing `UndoableEdit` listeners.[UndoManager](UndoManager.html)`UndoManager` manages a list of `UndoableEdits`, providing a way to undo or redo the appropriate edits.
