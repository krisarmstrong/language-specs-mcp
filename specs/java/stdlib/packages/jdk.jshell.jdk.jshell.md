Module[jdk.jshell](../../module-summary.html)

# Package jdk.jshell

package jdk.jshellProvides interfaces for creating tools, such as a Read-Eval-Print Loop (REPL), which interactively evaluate "snippets" of Java programming language code. Where a "snippet" is a single expression, statement, or declaration. This functionality can be used to enhance tools such as IDEs or can be stand-alone. 

[JShell](JShell.html) is the central class. An instance of `JShell` holds the evaluation state, which is both the current set of source snippets and the execution state they have produced. 

 Each source snippet is represented by an instance of a subclass of [Snippet](Snippet.html). For example, a statement is represented by an instance of [StatementSnippet](StatementSnippet.html), and a method declaration is represented by an instance of [MethodSnippet](MethodSnippet.html). Snippets are created when [JShell.eval(String)](JShell.html#eval(java.lang.String)) is invoked with an input which includes one or more snippets of code. 

 Any change to the compilation status of a snippet is reported with a [SnippetEvent](SnippetEvent.html). There are three major kinds of changes to the status of a snippet: it can be created with `eval`, it can be dropped from the active source state with [JShell.drop(jdk.jshell.Snippet)](JShell.html#drop(jdk.jshell.Snippet)), and it can have its status updated as a result of a status change in another snippet. For example: given `js`, an instance of `JShell`, executing `js.eval("int x = 5;")` will add the variable `x` to the source state and will generate an event describing the creation of a [VarSnippet](VarSnippet.html) for `x`. Then executing `js.eval("int timesx(int val) { return val * x; }")` will add a method to the source state and will generate an event describing the creation of a [MethodSnippet](MethodSnippet.html) for `timesx`. Assume that `varx` holds the snippet created by the first call to `eval`, executing `js.drop(varx)` will generate two events: one for changing the status of the variable snippet to `DROPPED` and one for updating the method snippet (which now has an unresolved reference to `x`). 

 Of course, for any general application of the API, the input would not be fixed strings, but would come from the user. Below is a very simplified example of how the API might be used to implement a REPL. 

```

 
     import java.io.ByteArrayInputStream;
     import java.io.Console;
     import java.util.List;
     import jdk.jshell.*;
     import jdk.jshell.Snippet.Status;

     class ExampleJShell {
         public static void main(String[] args) {
             Console console = System.console();
             try (JShell js = JShell.create()) {
                 do {
                     System.out.print("Enter some Java code: ");
                     String input = console.readLine();
                     if (input == null) {
                         break;
                     }
                     List<SnippetEvent> events = js.eval(input);
                     for (SnippetEvent e : events) {
                         StringBuilder sb = new StringBuilder();
                         if (e.causeSnippet() == null) {
                             //  We have a snippet creation event
                             switch (e.status()) {
                                 case VALID:
                                     sb.append("Successful ");
                                     break;
                                 case RECOVERABLE_DEFINED:
                                     sb.append("With unresolved references ");
                                     break;
                                 case RECOVERABLE_NOT_DEFINED:
                                     sb.append("Possibly reparable, failed  ");
                                     break;
                                 case REJECTED:
                                     sb.append("Failed ");
                                     break;
                             }
                             if (e.previousStatus() == Status.NONEXISTENT) {
                                 sb.append("addition");
                             } else {
                                 sb.append("modification");
                             }
                             sb.append(" of ");
                             sb.append(e.snippet().source());
                             System.out.println(sb);
                             if (e.value() != null) {
                                 System.out.printf("Value is: %s\n", e.value());
                             }
                             System.out.flush();
                         }
                     }
                 } while (true);
             }
             System.out.println("\nGoodbye");
         }
     }
 
 
```

 To register for status change events use [JShell.onSnippetEvent(java.util.function.Consumer)](JShell.html#onSnippetEvent(java.util.function.Consumer)). These events are only generated by `eval` and `drop`, the return values of these methods are the list of events generated by that call. So, as in the example above, events can be used without registering to receive events. 

 If you experiment with this example, you will see that failing to terminate a statement or variable declaration with a semi-colon will simply fail. An unfinished entry (for example a desired multi-line method) will also just fail after one line. The utilities in [SourceCodeAnalysis](SourceCodeAnalysis.html) provide source boundary and completeness analysis to address cases like those. `SourceCodeAnalysis` also provides suggested completions of input, as might be used in tab-completion.

Since:9

- Related PackagesPackageDescription[jdk.jshell.execution](execution/package-summary.html)Provides implementation support for building JShell execution engines.[jdk.jshell.spi](spi/package-summary.html)Defines the Service Provider Interface for pluggable JShell execution engines.[jdk.jshell.tool](tool/package-summary.html)Provides a mechanism to launch an instance of a Java shell tool.
- All Classes and InterfacesInterfacesClassesEnum ClassesRecord ClassesException ClassesClassDescription[DeclarationSnippet](DeclarationSnippet.html)Grouping for all declaration Snippets: variable declarations ([VarSnippet](VarSnippet.html)), method declarations ([MethodSnippet](MethodSnippet.html)), and type declarations ([TypeDeclSnippet](TypeDeclSnippet.html)).[Diag](Diag.html)Diagnostic information for a Snippet.[ErroneousSnippet](ErroneousSnippet.html)A snippet of code that is not valid Java programming language code.[EvalException](EvalException.html)Wraps an throwable thrown in the executing client.[ExpressionSnippet](ExpressionSnippet.html)Snippet for an assignment or variable-value expression.[ImportSnippet](ImportSnippet.html)Snippet for an import declaration.[JShell](JShell.html)The JShell evaluation state engine.[JShell.Builder](JShell.Builder.html)Builder for `JShell` instances.[JShellConsole](JShellConsole.html)An interface providing functionality for [Console](../../../java.base/java/io/Console.html) in the user's snippet.[JShellException](JShellException.html)The superclass of JShell generated exceptions[MethodSnippet](MethodSnippet.html)Snippet for a method definition.[PersistentSnippet](PersistentSnippet.html)Grouping for Snippets which persist and influence future code.[Snippet](Snippet.html)A Snippet represents a snippet of Java source code as passed to [JShell.eval(java.lang.String)](JShell.html#eval(java.lang.String)).[Snippet.Kind](Snippet.Kind.html)Describes the general kind of snippet.[Snippet.Status](Snippet.Status.html)Describes the current state of a Snippet.[Snippet.SubKind](Snippet.SubKind.html)The detailed variety of a snippet.[SnippetEvent](SnippetEvent.html)A description of a change to a Snippet.[SourceCodeAnalysis](SourceCodeAnalysis.html)Provides analysis utilities for source code input.[SourceCodeAnalysis.Attribute](SourceCodeAnalysis.Attribute.html)A span attribute which can be used to derive a coloring.[SourceCodeAnalysis.Completeness](SourceCodeAnalysis.Completeness.html)Describes the completeness of the given input.[SourceCodeAnalysis.CompletionInfo](SourceCodeAnalysis.CompletionInfo.html)The result of `analyzeCompletion(String input)`.[SourceCodeAnalysis.Documentation](SourceCodeAnalysis.Documentation.html)A documentation for a candidate for continuation of the given user's input.[SourceCodeAnalysis.Highlight](SourceCodeAnalysis.Highlight.html)Assigns attributes usable for coloring to spans inside a snippet.[SourceCodeAnalysis.QualifiedNames](SourceCodeAnalysis.QualifiedNames.html)List of possible qualified names.[SourceCodeAnalysis.SnippetWrapper](SourceCodeAnalysis.SnippetWrapper.html)The wrapping of a snippet of Java source into valid top-level Java source.[SourceCodeAnalysis.Suggestion](SourceCodeAnalysis.Suggestion.html)A candidate for continuation of the given user's input.[StatementSnippet](StatementSnippet.html)Snippet for a statement.[TypeDeclSnippet](TypeDeclSnippet.html)Snippet for a type definition (a class, interface, enum, or annotation interface definition).[UnresolvedReferenceException](UnresolvedReferenceException.html)Exception reported on attempting to execute a [RECOVERABLE_DEFINED](Snippet.Status.html#RECOVERABLE_DEFINED) snippet.[VarSnippet](VarSnippet.html)Snippet for a variable definition.
