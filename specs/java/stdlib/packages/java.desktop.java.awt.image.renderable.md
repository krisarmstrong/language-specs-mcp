java.awt.image.renderable (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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
  - [Related Packages](#related-package-summary)
  - [Classes and Interfaces](#class-summary)

- Package: 
- [Description](#package-description) | 
- [Related Packages](#related-package-summary) | 
- [Classes and Interfaces](#class-summary)

[SEARCH](../../../../../search.html)Module[java.desktop](../../../../module-summary.html)

# Package java.awt.image.renderable

package java.awt.image.renderableProvides classes and interfaces for producing rendering-independent images.Since:1.2

- Related PackagesPackageDescription[java.awt.image](../package-summary.html)Provides classes for creating and modifying images.
- All Classes and InterfacesInterfacesClassesClassDescription[ContextualRenderedImageFactory](ContextualRenderedImageFactory.html)ContextualRenderedImageFactory provides an interface for the functionality that may differ between instances of RenderableImageOp.[ParameterBlock](ParameterBlock.html)A `ParameterBlock` encapsulates all the information about sources and parameters (Objects) required by a RenderableImageOp, or other classes that process images.[RenderableImage](RenderableImage.html)A RenderableImage is a common interface for rendering-independent images (a notion which subsumes resolution independence).[RenderableImageOp](RenderableImageOp.html)This class handles the renderable aspects of an operation with help from its associated instance of a ContextualRenderedImageFactory.[RenderableImageProducer](RenderableImageProducer.html)An adapter class that implements ImageProducer to allow the asynchronous production of a RenderableImage.[RenderContext](RenderContext.html)A RenderContext encapsulates the information needed to produce a specific rendering from a RenderableImage.[RenderedImageFactory](RenderedImageFactory.html)The RenderedImageFactory interface (often abbreviated RIF) is intended to be implemented by classes that wish to act as factories to produce different renderings, for example by executing a series of BufferedImageOps on a set of sources, depending on a specific set of parameters, properties, and rendering hints.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
