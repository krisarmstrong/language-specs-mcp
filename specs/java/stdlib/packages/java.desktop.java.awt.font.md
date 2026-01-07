java.awt.font (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

# Package java.awt.font

package java.awt.fontProvides classes and interface relating to fonts. It contains support for representing Type 1, Type 1 Multiple Master fonts, OpenType fonts, and TrueType fonts.Since:1.2

- Related PackagesPackageDescription[java.awt](../package-summary.html)Contains all of the classes for creating user interfaces and for painting graphics and images.
- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[FontRenderContext](FontRenderContext.html)The `FontRenderContext` class is a container for the information needed to correctly measure text.[GlyphJustificationInfo](GlyphJustificationInfo.html)The `GlyphJustificationInfo` class represents information about the justification properties of a glyph.[GlyphMetrics](GlyphMetrics.html)The `GlyphMetrics` class represents information for a single glyph.[GlyphVector](GlyphVector.html)A `GlyphVector` object is a collection of glyphs containing geometric information for the placement of each glyph in a transformed coordinate space which corresponds to the device on which the `GlyphVector` is ultimately displayed.[GraphicAttribute](GraphicAttribute.html)This class is used with the CHAR_REPLACEMENT attribute.[ImageGraphicAttribute](ImageGraphicAttribute.html)The `ImageGraphicAttribute` class is an implementation of [GraphicAttribute](GraphicAttribute.html) which draws images in a [TextLayout](TextLayout.html).[LayoutPath](LayoutPath.html)LayoutPath provides a mapping between locations relative to the baseline and points in user space.[LineBreakMeasurer](LineBreakMeasurer.html)The `LineBreakMeasurer` class allows styled text to be broken into lines (or segments) that fit within a particular visual advance.[LineMetrics](LineMetrics.html)The `LineMetrics` class allows access to the metrics needed to layout characters along a line and to layout of a set of lines.[MultipleMaster](MultipleMaster.html)The `MultipleMaster` interface represents Type 1 Multiple Master fonts.[NumericShaper](NumericShaper.html)The `NumericShaper` class is used to convert Latin-1 (European) digits to other Unicode decimal digits.[NumericShaper.Range](NumericShaper.Range.html)A `NumericShaper.Range` represents a Unicode range of a script having its own decimal digits.[OpenType](OpenType.html)The `OpenType` interface represents OpenType and TrueType fonts.[ShapeGraphicAttribute](ShapeGraphicAttribute.html)The `ShapeGraphicAttribute` class is an implementation of [GraphicAttribute](GraphicAttribute.html) that draws shapes in a [TextLayout](TextLayout.html).[TextAttribute](TextAttribute.html)The `TextAttribute` class defines attribute keys and attribute values used for text rendering.[TextHitInfo](TextHitInfo.html)The `TextHitInfo` class represents a character position in a text model, and a bias, or "side," of the character.[TextLayout](TextLayout.html)`TextLayout` is an immutable graphical representation of styled character data.[TextLayout.CaretPolicy](TextLayout.CaretPolicy.html)Defines a policy for determining the strong caret location.[TextMeasurer](TextMeasurer.html)The `TextMeasurer` class provides the primitive operations needed for line break: measuring up to a given advance, determining the advance of a range of characters, and generating a `TextLayout` for a range of characters.[TransformAttribute](TransformAttribute.html)The `TransformAttribute` class provides an immutable wrapper for a transform so that it is safe to use as an attribute.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
