javax.lang.model.type (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../../search.html)Module[java.compiler](../../../../module-summary.html)

# Package javax.lang.model.type

package javax.lang.model.typeInterfaces used to model Java programming language types. 

 Unless otherwise specified in a particular implementation, the collections returned by methods in this package should be expected to be unmodifiable by the caller and unsafe for concurrent access. 

 Unless otherwise specified, methods in this package will throw a `NullPointerException` if given a `null` argument.

See Java Language Specification:[4.1 The Kinds of Types and Values](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.1)
[4.2 Primitive Types and Values](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.2)
[4.3 Reference Types and Values](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.3)
[4.4 Type Variables](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.4)
[4.5 Parameterized Types](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.5)
[4.8 Raw Types](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.8)
[4.9 Intersection Types](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.9)
[10.1 Array Types](https://docs.oracle.com/javase/specs/jls/se21/html/jls-10.html#jls-10.1)
Since:1.6See Also:

- [Types](../util/Types.html)
- [JSR 269: Pluggable Annotation Processing API](https://jcp.org/en/jsr/detail?id=269)

- Related PackagesPackageDescription[javax.lang.model](../package-summary.html)Types and hierarchies of packages comprising a Java language model, a model of the declarations and types of the Java programming language.[javax.lang.model.element](../element/package-summary.html)Interfaces used to model elements of the Java programming language.[javax.lang.model.util](../util/package-summary.html)Utilities to assist in the processing of [program elements](../element/package-summary.html) and [types](package-summary.html).
- All Classes and InterfacesInterfacesEnum ClassesException ClassesClassDescription[ArrayType](ArrayType.html)Represents an array type.[DeclaredType](DeclaredType.html)Represents a declared type, either a class type or an interface type.[ErrorType](ErrorType.html)Represents a class or interface type that cannot be properly modeled.[ExecutableType](ExecutableType.html)Represents the type of an executable.[IntersectionType](IntersectionType.html)Represents an intersection type.[MirroredTypeException](MirroredTypeException.html)Thrown when an application attempts to access the [Class](../../../../../java.base/java/lang/Class.html) object corresponding to a [TypeMirror](TypeMirror.html).[MirroredTypesException](MirroredTypesException.html)Thrown when an application attempts to access a sequence of [Class](../../../../../java.base/java/lang/Class.html) objects each corresponding to a [TypeMirror](TypeMirror.html).[NoType](NoType.html)A pseudo-type used where no actual type is appropriate.[NullType](NullType.html)Represents the null type.[PrimitiveType](PrimitiveType.html)Represents a primitive type.[ReferenceType](ReferenceType.html)Represents a reference type.[TypeKind](TypeKind.html)The kind of a type mirror.[TypeMirror](TypeMirror.html)Represents a type in the Java programming language.[TypeVariable](TypeVariable.html)Represents a type variable.[TypeVisitor](TypeVisitor.html)<R,P>A visitor of types, in the style of the visitor design pattern.[UnionType](UnionType.html)Represents a union type.[UnknownTypeException](UnknownTypeException.html)Indicates that an unknown kind of type was encountered.[WildcardType](WildcardType.html)Represents a wildcard type argument.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
