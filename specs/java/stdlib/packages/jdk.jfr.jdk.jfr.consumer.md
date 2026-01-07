jdk.jfr.consumer (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[jdk.jfr](../../../module-summary.html)

# Package jdk.jfr.consumer

package jdk.jfr.consumerThis package contains classes for consuming Flight Recorder data. 

 In the following example, the program prints a histogram of all method samples in a recording. Copy

```
public static void main(String[] args) throws IOException {
    if (args.length != 1) {
        System.err.println("Must specify a recording file.");
        return;
    }

    RecordingFile.readAllEvents(Path.of(args[0])).stream()
        .filter(e -> e.getEventType().getName().equals("jdk.ExecutionSample"))
        .map(e -> e.getStackTrace())
        .filter(s -> s != null)
        .map(s -> s.getFrames().get(0))
        .filter(f -> f.isJavaFrame())
        .map(f -> f.getMethod())
        .collect(
            Collectors.groupingBy(m -> m.getType().getName() + "." + m.getName() + " " + m.getDescriptor(),
            Collectors.counting()))
        .entrySet()
        .stream()
        .sorted((a, b) -> b.getValue().compareTo(a.getValue()))
        .forEach(e -> System.out.printf("%8d %s\n", e.getValue(), e.getKey()));
}
```

Null-handling

 All methods define whether they accept or return `null` in the Javadoc. Typically this is expressed as `"not null"`. If a `null` parameter is used where it is not allowed, a `java.lang.NullPointerException` is thrown. If a `null` parameters is passed to a method that throws other exceptions, such as `java.io.IOException`, the `java.lang.NullPointerException` takes precedence, unless the Javadoc for the method explicitly states how `null` is handled, i.e. by throwing `java.lang.IllegalArgumentException`.

Since:9

- Related PackagesPackageDescription[jdk.jfr](../package-summary.html)This package provides classes to create events and control Flight Recorder.
- All Classes and InterfacesInterfacesClassesClassDescription[EventStream](EventStream.html)Represents a stream of events.[MetadataEvent](MetadataEvent.html)Event that contains information about event types and configurations.[RecordedClass](RecordedClass.html)A recorded Java type, such as a class or an interface.[RecordedClassLoader](RecordedClassLoader.html)A recorded Java class loader.[RecordedEvent](RecordedEvent.html)A recorded event.[RecordedFrame](RecordedFrame.html)A recorded frame in a stack trace.[RecordedMethod](RecordedMethod.html)A recorded method.[RecordedObject](RecordedObject.html)A complex data type that consists of one or more fields.[RecordedStackTrace](RecordedStackTrace.html)A recorded stack trace.[RecordedThread](RecordedThread.html)A recorded thread.[RecordedThreadGroup](RecordedThreadGroup.html)A recorded Java thread group.[RecordingFile](RecordingFile.html)A recording file.[RecordingStream](RecordingStream.html)A recording stream produces events from the current JVM (Java Virtual Machine).

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
