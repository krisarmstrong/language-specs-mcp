Module[jdk.jshell](../../../module-summary.html)

# Package jdk.jshell.tool

package jdk.jshell.toolProvides a mechanism to launch an instance of a Java shell tool. Allows configuration of the tool before launching. A builder is used to configure and launch the tool. 

 At the simplest, a builder is retrieved, and the builder is used to start the tool: 

```

 
       JavaShellToolBuilder
             .builder()
             .start();
 
 
```

 The builder can be configured and the start can have arguments: 

```

 
       JavaShellToolBuilder
             .builder()
             .out(myCommandPrintStream, myOutputPrintStream)
             .locale(Locale.CANADA)
             .start("--feedback", "silent", "MyStart");
 
 
```

Since:9

- Related PackagesPackageDescription[jdk.jshell](../package-summary.html)Provides interfaces for creating tools, such as a Read-Eval-Print Loop (REPL), which interactively evaluate "snippets" of Java programming language code.[jdk.jshell.execution](../execution/package-summary.html)Provides implementation support for building JShell execution engines.[jdk.jshell.spi](../spi/package-summary.html)Defines the Service Provider Interface for pluggable JShell execution engines.
- InterfacesClassDescription[JavaShellToolBuilder](JavaShellToolBuilder.html)Interface to configure and run a Java shell tool instance.
