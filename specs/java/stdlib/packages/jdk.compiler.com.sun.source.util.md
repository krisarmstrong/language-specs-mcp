com.sun.source.util (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

- [Overview](../../../../../index.html)
- [Module](../../../../module-summary.html)
- Package
- Class
- [Use](package-use.html)
- [Tree](package-tree.html)
- [Preview](../../../../../preview-list.html)
- [New](../../../../../new-list.html)
- [Deprecated](../../../../../deprecated-list.html)
- [Index](../../../../../index-files/index-1.html)
- [Help](../../../../../help-doc.html#package)

- 

Package:

  - [Description](#package-description)
  - Related Packages
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- Related Packages | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../../search.html)Module[jdk.compiler](../../../../module-summary.html)

# Package com.sun.source.util

package com.sun.source.utilProvides utilities for operations on abstract syntax trees (AST).Since:1.6

- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[DocSourcePositions](DocSourcePositions.html)Provides methods to obtain the position of a DocTree within a javadoc comment.[DocTreeFactory](DocTreeFactory.html)Factory for creating `DocTree` nodes.[DocTreePath](DocTreePath.html)A path of tree nodes, typically used to represent the sequence of ancestor nodes of a tree node up to the top-level `DocCommentTree` node.[DocTreePathScanner](DocTreePathScanner.html)<R,P>A DocTreeVisitor that visits all the child tree nodes, and provides support for maintaining a path for the parent nodes.[DocTrees](DocTrees.html)Provides access to syntax trees for doc comments.[DocTreeScanner](DocTreeScanner.html)<R,P>A DocTreeVisitor that visits all the child tree nodes.[JavacTask](JavacTask.html)Provides access to functionality specific to the JDK Java Compiler, javac.[ParameterNameProvider](ParameterNameProvider.html)A provider for parameter names when the parameter names are not determined from a reliable source, like a classfile.[Plugin](Plugin.html)The interface for a javac plug-in.[SimpleDocTreeVisitor](SimpleDocTreeVisitor.html)<R,P>A simple visitor for tree nodes.[SimpleTreeVisitor](SimpleTreeVisitor.html)<R,P>A simple visitor for tree nodes.[SourcePositions](SourcePositions.html)Provides methods to obtain the position of a Tree within a CompilationUnit.[TaskEvent](TaskEvent.html)Provides details about work that has been done by the JDK Java Compiler, javac.[TaskEvent.Kind](TaskEvent.Kind.html)Kind of task event.[TaskListener](TaskListener.html)Provides a listener to monitor the activity of the JDK Java Compiler, javac.[TreePath](TreePath.html)A path of tree nodes, typically used to represent the sequence of ancestor nodes of a tree node up to the top-level `CompilationUnitTree` node.[TreePathScanner](TreePathScanner.html)<R,P>A TreeVisitor that visits all the child tree nodes, and provides support for maintaining a path for the parent nodes.[Trees](Trees.html)Bridges JSR 199, JSR 269, and the Tree API.[TreeScanner](TreeScanner.html)<R,P>A TreeVisitor that visits all the child tree nodes.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
