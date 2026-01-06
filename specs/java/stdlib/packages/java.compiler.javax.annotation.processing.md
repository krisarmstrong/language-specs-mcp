Module[java.compiler](../../../module-summary.html)

# Package javax.annotation.processing

package javax.annotation.processingFacilities for declaring annotation processors and for allowing annotation processors to communicate with an annotation processing tool environment. 

 Unless otherwise specified in a particular implementation, the collections returned by methods in this package should be expected to be unmodifiable by the caller and unsafe for concurrent access. 

 Unless otherwise specified, methods in this package will throw a `NullPointerException` if given a `null` argument.

Since:1.6See Also:

- [JSR 269: Pluggable Annotation Processing API](https://jcp.org/en/jsr/detail?id=269)

- All Classes and InterfacesInterfacesClassesException ClassesAnnotation InterfacesClassDescription[AbstractProcessor](AbstractProcessor.html)An abstract annotation processor designed to be a convenient superclass for most concrete annotation processors.[Completion](Completion.html)A suggested [completion](Processor.html#getCompletions(javax.lang.model.element.Element,javax.lang.model.element.AnnotationMirror,javax.lang.model.element.ExecutableElement,java.lang.String)) for an annotation.[Completions](Completions.html)Utility class for assembling [Completion](Completion.html) objects.[Filer](Filer.html)This interface supports the creation of new files by an annotation processor.[FilerException](FilerException.html)Indicates a [Filer](Filer.html) detected an attempt to open a file that would violate the guarantees provided by the `Filer`.[Generated](Generated.html)The Generated annotation is used to mark source code that has been generated.[Messager](Messager.html)A `Messager` provides the way for an annotation processor to report error messages, warnings, and other notices.[ProcessingEnvironment](ProcessingEnvironment.html)An annotation processing tool framework will [provide an annotation processor with an object
 implementing this interface](Processor.html#init(javax.annotation.processing.ProcessingEnvironment)) so the processor can use facilities provided by the framework to write new files, report error messages, and find other utilities.[Processor](Processor.html)The interface for an annotation processor.[RoundEnvironment](RoundEnvironment.html)An annotation processing tool framework will [provide an annotation processor with an object
 implementing this interface](Processor.html#process(java.util.Set,javax.annotation.processing.RoundEnvironment)) so that the processor can query for information about a round of annotation processing.[SupportedAnnotationTypes](SupportedAnnotationTypes.html)An annotation used to indicate what annotation interfaces an annotation processor supports.[SupportedOptions](SupportedOptions.html)An annotation used to indicate what options an annotation processor supports.[SupportedSourceVersion](SupportedSourceVersion.html)An annotation used to indicate the latest source version an annotation processor supports.
