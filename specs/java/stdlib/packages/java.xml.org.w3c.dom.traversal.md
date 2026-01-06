Module[java.xml](../../../../module-summary.html)

# Package org.w3c.dom.traversal

package org.w3c.dom.traversal

 Provides interfaces for DOM Level 2 Traversal. Refer to the [Document Object Model (DOM) Level 2 Traversal and Range Specification](http://www.w3.org/TR/2000/REC-DOM-Level-2-Traversal-Range-20001113), the Traversal module contains specialized interfaces dedicated to traversing the document structure.

Since:1.5

- Related PackagesPackageDescription[org.w3c.dom](../package-summary.html)Provides the interfaces for the Document Object Model (DOM).
- InterfacesClassDescription[DocumentTraversal](DocumentTraversal.html)`DocumentTraversal` contains methods that create `NodeIterators` and `TreeWalkers` to traverse a node and its children in document order (depth first, pre-order traversal, which is equivalent to the order in which the start tags occur in the text representation of the document).[NodeFilter](NodeFilter.html)Filters are objects that know how to "filter out" nodes.[NodeIterator](NodeIterator.html)`NodeIterators` are used to step through a set of nodes, e.g.[TreeWalker](TreeWalker.html)`TreeWalker` objects are used to navigate a document tree or subtree using the view of the document defined by their `whatToShow` flags and filter (if any).
