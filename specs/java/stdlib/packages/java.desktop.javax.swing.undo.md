javax.swing.undo (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../index.html)
- [Module](../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../preview-list.html)
- [New](../../../../new-list.html)
- [Deprecated](../../../../deprecated-list.html)
- [Index](../../../../index-files/index-1.html)
- [Help](../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../search.html)Module[java.desktop](../../../module-summary.html)

# Package javax.swing.undo

package javax.swing.undoAllows developers to provide support for undo/redo in applications such as text editors. 

Note: Most of the Swing API is not thread safe. For details, see [Concurrency in Swing](https://docs.oracle.com/javase/tutorial/uiswing/concurrency/index.html), a section in [The Java Tutorial](https://docs.oracle.com/javase/tutorial/). 

## Related Documentation

 For overviews, tutorials, examples, guides, and tool documentation, please see: 

- [Implementing Undo and Redo](https://docs.oracle.com/javase/tutorial/uiswing/components/generaltext.html#undo), a section in The Java Tutorial

Since:1.2

- Related PackagesPackageDescription[javax.swing](../package-summary.html)Provides a set of "lightweight" (all-Java language) components that, to the maximum degree possible, work the same on all platforms.
- All Classes and InterfacesInterfacesClassesException ClassesClassDescription[AbstractUndoableEdit](AbstractUndoableEdit.html)An abstract implementation of `UndoableEdit`, implementing simple responses to all boolean methods in that interface.[CannotRedoException](CannotRedoException.html)Thrown when an UndoableEdit is told to `redo()` and can't.[CannotUndoException](CannotUndoException.html)Thrown when an UndoableEdit is told to `undo()` and can't.[CompoundEdit](CompoundEdit.html)A concrete subclass of AbstractUndoableEdit, used to assemble little UndoableEdits into great big ones.[StateEdit](StateEdit.html)StateEdit is a general edit for objects that change state.[StateEditable](StateEditable.html)StateEditable defines the interface for objects that can have their state undone/redone by a StateEdit.[UndoableEdit](UndoableEdit.html)An `UndoableEdit` represents an edit.[UndoableEditSupport](UndoableEditSupport.html)A support class used for managing `UndoableEdit` listeners.[UndoManager](UndoManager.html)`UndoManager` manages a list of `UndoableEdits`, providing a way to undo or redo the appropriate edits.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
