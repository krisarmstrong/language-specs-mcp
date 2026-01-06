Module[jdk.javadoc](../../../module-summary.html)

# Package jdk.javadoc.doclet

package jdk.javadoc.docletThe Doclet API provides an environment which, in conjunction with the Language Model API and Compiler Tree API, allows clients to inspect the source-level structures of programs and libraries, including API comments embedded in the source. 

 The [standard doclet](StandardDoclet.html) can be used to generate HTML-formatted documentation. It supports user-defined [taglets](Taglet.html), which can be used to generate customized output for user-defined tags in documentation comments. 

Note: The declarations in this package supersede those in the older package `com.sun.javadoc`. For details on the mapping of old types to new types, see the [Migration Guide](#migration). 

 Doclets are invoked by javadoc and this API can be used to write out program information to files. For example, the standard doclet is invoked by default, to generate HTML documentation. 

 The invocation is defined by the interface [Doclet](Doclet.html) -- the [run](Doclet.html#run(jdk.javadoc.doclet.DocletEnvironment)) interface method, defines the entry point. Copy

```
   public boolean run(DocletEnvironment environment)
```

 The [DocletEnvironment](DocletEnvironment.html) instance holds the environment that the doclet will be initialized with. From this environment all other information can be extracted, in the form of [elements](../../../../java.compiler/javax/lang/model/element/Element.html). One can further use the APIs and utilities described by [Language Model API](../../../../java.compiler/javax/lang/model/package-summary.html) to query Elements and Types. 

## Terminology

SelectedAn element is considered to be selected, if the selection controls[allow](#options) it to be documented. (Note that synthetic elements are never selected.) SpecifiedThe set of elements specified by the user are considered to be specified elements. Specified elements provide the starting points for determining the included elements to be documented. IncludedAn element is considered to be included, if it is selected and any of the following is true: 

- the element is specified, or 
- the element contains a specified element, or 
- the element is enclosed in a specified element. 

 Included elements will be documented. 

## Options

 Javadoc selection control can be specified with these options as follows: 

- `--show-members:value` and `--show-types:value` can be used to filter the members, with the following values: 

  -  public -- considers only public elements 
  -  protected -- considers public and protected elements 
  -  package -- considers public, protected and package private elements 
  -  private -- considers all elements 

- `--show-packages:value` "exported" or "all" can be used to consider only exported packages or all packages within a module. 
- `--show-module-contents:value` can be used to specify the level at module declarations could be documented. A value of "api" indicates API level documentation, and "all" indicates detailed documentation. 

 The following options can be used to specify the elements to be documented: 

- `--module` documents the specified modules. 
- `--expand-requires:value` expand the set of modules to be documented by including some or all of the modules dependencies. The value may be one of: 

  -  transitive -- each module specified explicitly on the command line is expanded to include the closure of its transitive dependencies 
  -  all -- each module specified explicitly on the command line is expanded to include the closure of its transitive dependencies, and also all of its direct dependencies 

 By default, only the specified modules will be considered, without expansion of the module dependencies. 
- `packagenames` can be used to specify packages. 
- `-subpackages` can be used to recursively load packages. 
- `-exclude` can be used exclude package directories. 
- `sourcefilenames` can be used to specify source file names. 

### Interactions with older options.

 The new `--show-*` options provide a more detailed replacement for the older options `-public`, `-protected`, `-package`, `-private`. Alternatively, the older options can continue to be used as shorter forms for combinations of the new options, as described below: Short form options mapping Older option  Equivalent to these values with the new option `--show-members``--show-types``--show-packages``--show-module-contents``-public`public public exported api `-protected`protected protected exported api `-package`package package all all `-private`private private all all 

 A qualified element name is one that has its package name prepended to it, such as `java.lang.String`. A non-qualified name has no package name, such as `String`. 

## Example

 The following is an example doclet that displays information of a class and its members, supporting an option. Copy

```
// Note: imports deleted for clarity

public class Example implements Doclet {
    private Reporter reporter;
    private PrintWriter stdout;

    @Override
    public void init(Locale locale, Reporter reporter) {
        reporter.print(Kind.NOTE, "Doclet using locale: " + locale);
        this.reporter = reporter;
        stdout = reporter.getStandardWriter();
    }

    public void printElement(DocTrees trees, Element e) {
        DocCommentTree docCommentTree = trees.getDocCommentTree(e);
        if (docCommentTree != null) {
            stdout.println("Element (" + e.getKind() + ": "
                    + e + ") has the following comments:");
            stdout.println("Entire body: " + docCommentTree.getFullBody());
            stdout.println("Block tags: " + docCommentTree.getBlockTags());
        }
    }

    @Override
    public boolean run(DocletEnvironment docEnv) {
        reporter.print(Kind.NOTE, "overviewFile: " + overviewFile);

        // get the DocTrees utility class to access document comments
        DocTrees docTrees = docEnv.getDocTrees();

        // location of an element in the same directory as overview.html
        try {
            Element e = ElementFilter.typesIn(docEnv.getSpecifiedElements()).iterator().next();
            DocCommentTree docCommentTree
                    = docTrees.getDocCommentTree(e, overviewFile);
            if (docCommentTree != null) {
                stdout.println("Overview html: " + docCommentTree.getFullBody());
            }
        } catch (IOException missing) {
            reporter.print(Kind.ERROR, "No overview.html found.");
        }

        for (TypeElement t : ElementFilter.typesIn(docEnv.getIncludedElements())) {
            stdout.println(t.getKind() + ":" + t);
            for (Element e : t.getEnclosedElements()) {
                printElement(docTrees, e);
            }
        }
        return true;
    }

    @Override
    public String getName() {
        return "Example";
    }

    private String overviewFile;

    @Override
    public Set<? extends Option> getSupportedOptions() {
        Option[] options = {
            new Option() {
                private final List<String> someOption = List.of(
                        "--overview-file",
                        "-overviewfile",
                        "-o"
                );

                @Override
                public int getArgumentCount() {
                    return 1;
                }

                @Override
                public String getDescription() {
                    return "an option with aliases";
                }

                @Override
                public Option.Kind getKind() {
                    return Option.Kind.STANDARD;
                }

                @Override
                public List<String> getNames() {
                    return someOption;
                }

                @Override
                public String getParameters() {
                    return "file";
                }

                @Override
                public boolean process(String opt, List<String> arguments) {
                    overviewFile = arguments.get(0);
                    return true;
                }
            }
        };

        return Set.of(options);
    }

    @Override
    public SourceVersion getSupportedSourceVersion() {
        // support the latest release
        return SourceVersion.latest();
    }
}
```

 This doclet can be invoked with a command line, such as: Copy

```
javadoc -docletpath doclet-classes \
  -doclet Example \
  --overview-file overview.html \
  --source-path source-location \
  source-location/Example.java
```

## Migration Guide

Many of the types in the old `com.sun.javadoc` API do not have equivalents in this package. Instead, types in the `javax.lang.model` and `com.sun.source` APIs are used instead. 

The following table gives a guide to the mapping from old types to their replacements. In some cases, there is no direct equivalent. Guide for mapping old types to new typesOld TypeNew Type `AnnotatedType`[javax.lang.model.type.TypeMirror](../../../../java.compiler/javax/lang/model/type/TypeMirror.html)`AnnotationDesc`[javax.lang.model.element.AnnotationMirror](../../../../java.compiler/javax/lang/model/element/AnnotationMirror.html)`AnnotationDesc.ElementValuePair`[javax.lang.model.element.AnnotationValue](../../../../java.compiler/javax/lang/model/element/AnnotationValue.html)`AnnotationTypeDoc`[javax.lang.model.element.TypeElement](../../../../java.compiler/javax/lang/model/element/TypeElement.html)`AnnotationTypeElementDoc`[javax.lang.model.element.ExecutableElement](../../../../java.compiler/javax/lang/model/element/ExecutableElement.html)`AnnotationValue`[javax.lang.model.element.AnnotationValue](../../../../java.compiler/javax/lang/model/element/AnnotationValue.html)`ClassDoc`[javax.lang.model.element.TypeElement](../../../../java.compiler/javax/lang/model/element/TypeElement.html)`ConstructorDoc`[javax.lang.model.element.ExecutableElement](../../../../java.compiler/javax/lang/model/element/ExecutableElement.html)`Doc`[javax.lang.model.element.Element](../../../../java.compiler/javax/lang/model/element/Element.html)`DocErrorReporter`[jdk.javadoc.doclet.Reporter](Reporter.html)`Doclet`[jdk.javadoc.doclet.Doclet](Doclet.html)`ExecutableMemberDoc`[javax.lang.model.element.ExecutableElement](../../../../java.compiler/javax/lang/model/element/ExecutableElement.html)`FieldDoc`[javax.lang.model.element.VariableElement](../../../../java.compiler/javax/lang/model/element/VariableElement.html)`LanguageVersion`[javax.lang.model.SourceVersion](../../../../java.compiler/javax/lang/model/SourceVersion.html)`MemberDoc`[javax.lang.model.element.Element](../../../../java.compiler/javax/lang/model/element/Element.html)`MethodDoc`[javax.lang.model.element.ExecutableElement](../../../../java.compiler/javax/lang/model/element/ExecutableElement.html)`PackageDoc`[javax.lang.model.element.PackageElement](../../../../java.compiler/javax/lang/model/element/PackageElement.html)`Parameter`[javax.lang.model.element.VariableElement](../../../../java.compiler/javax/lang/model/element/VariableElement.html)`ParameterizedType`[javax.lang.model.type.DeclaredType](../../../../java.compiler/javax/lang/model/type/DeclaredType.html)`ParamTag`[com.sun.source.doctree.ParamTree](../../../../jdk.compiler/com/sun/source/doctree/ParamTree.html)`ProgramElementDoc`[javax.lang.model.element.Element](../../../../java.compiler/javax/lang/model/element/Element.html)`RootDoc`[jdk.javadoc.doclet.DocletEnvironment](DocletEnvironment.html)`SeeTag`[com.sun.source.doctree.LinkTree](../../../../jdk.compiler/com/sun/source/doctree/LinkTree.html)
[com.sun.source.doctree.SeeTree](../../../../jdk.compiler/com/sun/source/doctree/SeeTree.html)`SerialFieldTag`[com.sun.source.doctree.SerialFieldTree](../../../../jdk.compiler/com/sun/source/doctree/SerialFieldTree.html)`SourcePosition`[com.sun.source.util.SourcePositions](../../../../jdk.compiler/com/sun/source/util/SourcePositions.html)`Tag`[com.sun.source.doctree.DocTree](../../../../jdk.compiler/com/sun/source/doctree/DocTree.html)`ThrowsTag`[com.sun.source.doctree.ThrowsTree](../../../../jdk.compiler/com/sun/source/doctree/ThrowsTree.html)`Type`[javax.lang.model.type.TypeMirror](../../../../java.compiler/javax/lang/model/type/TypeMirror.html)`TypeVariable`[javax.lang.model.type.TypeVariable](../../../../java.compiler/javax/lang/model/type/TypeVariable.html)`WildcardType`[javax.lang.model.type.WildcardType](../../../../java.compiler/javax/lang/model/type/WildcardType.html)

Since:9See Also:

- [Doclet](Doclet.html)
- [DocletEnvironment](DocletEnvironment.html)

- All Classes and InterfacesInterfacesClassesEnum ClassesClassDescription[Doclet](Doclet.html)The user doclet must implement this interface, as described in the [package description](package-summary.html#package-description).[Doclet.Option](Doclet.Option.html)An encapsulation of option name, aliases, parameters and descriptions as used by the Doclet.[Doclet.Option.Kind](Doclet.Option.Kind.html)The kind of an option.[DocletEnvironment](DocletEnvironment.html)Represents the operating environment of a single invocation of the doclet.[DocletEnvironment.ModuleMode](DocletEnvironment.ModuleMode.html)The mode specifying the level of detail of module documentation.[Reporter](Reporter.html)Interface for reporting diagnostics and other messages.[StandardDoclet](StandardDoclet.html)This doclet generates HTML-formatted documentation for the specified modules, packages and types.[Taglet](Taglet.html)The interface for a custom taglet supported by doclets such as the [standard doclet](StandardDoclet.html).[Taglet.Location](Taglet.Location.html)The kind of location in which a tag may be used.
