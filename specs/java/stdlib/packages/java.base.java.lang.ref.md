java.lang.ref (Java SE 21 & JDK 21)[Skip navigation links](#skip-navbar-top)Java SE 21 & JDK 21

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

[SEARCH](../../../../search.html)Module[java.base](../../../module-summary.html)

# Package java.lang.ref

package java.lang.refProvides reference-object classes, which support a limited degree of interaction with the garbage collector. A program may use a reference object to maintain a reference to some other object in such a way that the latter object may still be reclaimed by the collector. A program may also arrange to be notified some time after the collector has determined that the reachability of a given object has changed. 

## Package Specification

 A reference object encapsulates a reference to some other object so that the reference itself may be examined and manipulated like any other object. Three types of reference objects are provided, each weaker than the last: soft, weak, and phantom. Each type corresponds to a different level of reachability, as defined below. Soft references are for implementing memory-sensitive caches, weak references are for implementing canonicalizing mappings that do not prevent their keys (or values) from being reclaimed, and phantom references are for scheduling post-mortem cleanup actions. Post-mortem cleanup actions can be registered and managed by a [Cleaner](Cleaner.html). 

 Each reference-object type is implemented by a subclass of the abstract base [Reference](Reference.html) class. An instance of one of these subclasses encapsulates a single reference to a particular object, called the referent. Every reference object provides methods for getting and clearing the reference. Aside from the clearing operation reference objects are otherwise immutable, so no `set` operation is provided. A program may further subclass these subclasses, adding whatever fields and methods are required for its purposes, or it may use these subclasses without change. 

### Notification

 A program may request to be notified of changes in an object's reachability by registering an appropriate reference object with a reference queue at the time the reference object is created. Some time after the garbage collector determines that the reachability of the referent has changed to the value corresponding to the type of the reference, it will clear the reference and add it to the associated queue. At this point, the reference is considered to be enqueued. The program may remove references from a queue either by polling or by blocking until a reference becomes available. Reference queues are implemented by the [ReferenceQueue](ReferenceQueue.html) class. 

 The relationship between a registered reference object and its queue is one-sided. That is, a queue does not keep track of the references that are registered with it. If a registered reference becomes unreachable itself, then it will never be enqueued. It is the responsibility of the program using reference objects to ensure that the objects remain reachable for as long as the program is interested in their referents. 

 While some programs will choose to dedicate a thread to removing reference objects from one or more queues and processing them, this is by no means necessary. A tactic that often works well is to examine a reference queue in the course of performing some other fairly-frequent action. For example, a hashtable that uses weak references to implement weak keys could poll its reference queue each time the table is accessed. This is how the [WeakHashMap](../../util/WeakHashMap.html) class works. Because the [ReferenceQueue.poll](ReferenceQueue.html#poll()) method simply checks an internal data structure, this check will add little overhead to the hashtable access methods. 

### Reachability

 Going from strongest to weakest, the different levels of reachability reflect the life cycle of an object. They are operationally defined as follows: 

-  An object is strongly reachable if it can be reached by some thread without traversing any reference objects. A newly-created object is strongly reachable by the thread that created it. 
-  An object is softly reachable if it is not strongly reachable but can be reached by traversing a soft reference. 
-  An object is weakly reachable if it is neither strongly nor softly reachable but can be reached by traversing a weak reference. When the weak references to a weakly-reachable object are cleared, the object becomes eligible for finalization. 
-  An object is phantom reachable if it is neither strongly, softly, nor weakly reachable, it has been finalized, and some phantom reference refers to it. 
-  Finally, an object is unreachable, and therefore eligible for reclamation, when it is not reachable in any of the above ways. 

Since:1.2

- Related PackagesPackageDescription[java.lang](../package-summary.html)Provides classes that are fundamental to the design of the Java programming language.
- All Classes and InterfacesInterfacesClassesClassDescription[Cleaner](Cleaner.html)`Cleaner` manages a set of object references and corresponding cleaning actions.[Cleaner.Cleanable](Cleaner.Cleanable.html)`Cleanable` represents an object and a cleaning action registered in a `Cleaner`.[PhantomReference](PhantomReference.html)<T>Phantom reference objects, which are enqueued after the collector determines that their referents may otherwise be reclaimed.[Reference](Reference.html)<T>Abstract base class for reference objects.[ReferenceQueue](ReferenceQueue.html)<T>Reference queues, to which registered reference objects are appended by the garbage collector after the appropriate reachability changes are detected.[SoftReference](SoftReference.html)<T>Soft reference objects, which are cleared at the discretion of the garbage collector in response to memory demand.[WeakReference](WeakReference.html)<T>Weak reference objects, which do not prevent their referents from being made finalizable, finalized, and then reclaimed.

[Report a bug or suggest an enhancement](https://bugreport.java.com/bugreport/)
 For further API reference and developer documentation see the [Java SE Documentation](https://docs.oracle.com/pls/topic/lookup?ctx=javase21&id=homepage), which contains more detailed, developer-targeted descriptions with conceptual overviews, definitions of terms, workarounds, and working code examples. [Other versions.](https://docs.oracle.com/en/java/javase/index.html)
 Java is a trademark or registered trademark of Oracle and/or its affiliates in the US and other countries.
[Copyright](../../../../../legal/copyright.html) © 1993, 2025, Oracle and/or its affiliates, 500 Oracle Parkway, Redwood Shores, CA 94065 USA.
All rights reserved. Use is subject to [license terms](https://www.oracle.com/java/javase/terms/license/java21speclicense.html) and the [documentation redistribution policy](https://www.oracle.com/technetwork/java/redist-137594.html).
