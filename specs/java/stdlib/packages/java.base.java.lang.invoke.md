Module[java.base](../../../module-summary.html)

# Package java.lang.invoke

package java.lang.invokeThe `java.lang.invoke` package provides low-level primitives for interacting with the Java Virtual Machine. 

 As described in the Java Virtual Machine Specification, certain types in this package are given special treatment by the virtual machine: 

- The classes [MethodHandle](MethodHandle.html) and [VarHandle](VarHandle.html) contain [signature polymorphic methods](MethodHandle.html#sigpoly) which can be linked regardless of their type descriptor. Normally, method linkage requires exact matching of type descriptors. 
- The JVM bytecode format supports immediate constants of the classes [MethodHandle](MethodHandle.html) and [MethodType](MethodType.html). 
- The `invokedynamic` instruction makes use of bootstrap `MethodHandle` constants to dynamically resolve `CallSite` objects for custom method invocation behavior. 
- The `ldc` instruction makes use of bootstrap `MethodHandle` constants to dynamically resolve custom constant values. 

## Dynamic resolution of call sites and constants

 The following low-level information summarizes relevant parts of the Java Virtual Machine specification. For full details, please see the current version of that specification. 

### Dynamically-computed call sites

 An `invokedynamic` instruction is originally in an unlinked state. In this state, there is no target method for the instruction to invoke. 

 Before the JVM can execute an `invokedynamic` instruction, the instruction must first be linked. Linking is accomplished by calling a bootstrap method which is given the static information content of the call, and which must produce a [CallSite](CallSite.html) that gives the behavior of the invocation. 

 Each `invokedynamic` instruction statically specifies its own bootstrap method as a constant pool reference. The constant pool reference also specifies the invocation's name and method type descriptor, just like `invokestatic` and the other invoke instructions. 

### Dynamically-computed constants

 The constant pool may contain constants tagged `CONSTANT_Dynamic`, equipped with bootstrap methods which perform their resolution. Such a dynamic constant is originally in an unresolved state. Before the JVM can use a dynamically-computed constant, it must first be resolved. Dynamically-computed constant resolution is accomplished by calling a bootstrap method which is given the static information content of the constant, and which must produce a value of the constant's statically declared type. 

 Each dynamically-computed constant statically specifies its own bootstrap method as a constant pool reference. The constant pool reference also specifies the constant's name and field type descriptor, just like `getstatic` and the other field reference instructions. (Roughly speaking, a dynamically-computed constant is to a dynamically-computed call site as a `CONSTANT_Fieldref` is to a `CONSTANT_Methodref`.) 

### Execution of bootstrap methods

 Resolving a dynamically-computed call site or constant starts with resolving constants from the constant pool for the following items: 

- the bootstrap method, a `CONSTANT_MethodHandle`
- the `Class` or `MethodType` derived from type component of the `CONSTANT_NameAndType` descriptor
- static arguments, if any (note that static arguments can themselves be dynamically-computed constants)

 The bootstrap method is then invoked, as if by [MethodHandle.invoke](MethodHandle.html#invoke(java.lang.Object...)), with the following arguments: 

- a `MethodHandles.Lookup`, which is a lookup object on the caller class in which dynamically-computed constant or call site occurs
- a `String`, the name mentioned in the `CONSTANT_NameAndType`
- a `MethodType` or `Class`, the resolved type descriptor of the `CONSTANT_NameAndType`
- a `Class`, the resolved type descriptor of the constant, if it is a dynamic constant 
- the additional resolved static arguments, if any

 For a dynamically-computed call site, the returned result must be a non-null reference to a [CallSite](CallSite.html). The type of the call site's target must be exactly equal to the type derived from the invocation's type descriptor and passed to the bootstrap method. If these conditions are not met, a `BootstrapMethodError` is thrown. On success the call site then becomes permanently linked to the `invokedynamic` instruction. 

 For a dynamically-computed constant, the first parameter of the bootstrap method must be assignable to `MethodHandles.Lookup`. If this condition is not met, a `BootstrapMethodError` is thrown. On success the result of the bootstrap method is cached as the resolved constant value. 

 If an exception, `E` say, occurs during execution of the bootstrap method, then resolution fails and terminates abnormally. `E` is rethrown if the type of `E` is `Error` or a subclass, otherwise a `BootstrapMethodError` that wraps `E` is thrown. If this happens, the same error will be thrown for all subsequent attempts to execute the `invokedynamic` instruction or load the dynamically-computed constant. 

### Timing of resolution

 An `invokedynamic` instruction is linked just before its first execution. A dynamically-computed constant is resolved just before the first time it is used (by pushing it on the stack or linking it as a bootstrap method parameter). The bootstrap method call implementing the linkage occurs within a thread that is attempting a first execution or first use. 

 If there are several such threads, the bootstrap method may be invoked in several threads concurrently. Therefore, bootstrap methods which access global application data must take the usual precautions against race conditions. In any case, every `invokedynamic` instruction is either unlinked or linked to a unique `CallSite` object. 

 In an application which requires `invokedynamic` instructions with individually mutable behaviors, their bootstrap methods should produce distinct [CallSite](CallSite.html) objects, one for each linkage request. Alternatively, an application can link a single `CallSite` object to several `invokedynamic` instructions, in which case a change to the target method will become visible at each of the instructions. 

 If several threads simultaneously execute a bootstrap method for a single dynamically-computed call site or constant, the JVM must choose one bootstrap method result and install it visibly to all threads. Any other bootstrap method calls are allowed to complete, but their results are ignored. 

Discussion: These rules do not enable the JVM to share call sites, or to issue “causeless” bootstrap method calls. Every `invokedynamic` instruction transitions at most once from unlinked to linked, just before its first invocation. There is no way to undo the effect of a completed bootstrap method call. 

### Types of bootstrap methods

 For a dynamically-computed call site, the bootstrap method is invoked with parameter types `MethodHandles.Lookup`, `String`, `MethodType`, and the types of any static arguments; the return type is `CallSite`. 

 For a dynamically-computed constant, the bootstrap method is invoked with parameter types `MethodHandles.Lookup`, `String`, `Class`, and the types of any static arguments; the return type is the type represented by the `Class`. 

 Because [MethodHandle.invoke](MethodHandle.html#invoke(java.lang.Object...)) allows for adaptations between the invoked method type and the bootstrap method handle's method type, there is flexibility in the declaration of the bootstrap method. For a dynamically-computed constant the first parameter type of the bootstrap method handle must be assignable to `MethodHandles.Lookup`, other than that constraint the same degree of flexibility applies to bootstrap methods of dynamically-computed call sites and dynamically-computed constants. Note: this constraint allows for the future possibility where the bootstrap method is invoked with just the parameter types of static arguments, thereby supporting a wider range of methods compatible with the static arguments (such as methods that don't declare or require the lookup, name, and type meta-data parameters). 

 For example, for dynamically-computed call site, the first argument could be `Object` instead of `MethodHandles.Lookup`, and the return type could also be `Object` instead of `CallSite`. (Note that the types and number of the stacked arguments limit the legal kinds of bootstrap methods to appropriately typed static methods and constructors.) 

 If a pushed value is a primitive type, it may be converted to a reference by boxing conversion. If the bootstrap method is a variable arity method (its modifier bit `0x0080` is set), then some or all of the arguments specified here may be collected into a trailing array parameter. (This is not a special rule, but rather a useful consequence of the interaction between `CONSTANT_MethodHandle` constants, the modifier bit for variable arity methods, and the [asVarargsCollector](MethodHandle.html#asVarargsCollector(java.lang.Class)) transformation.) 

 Given these rules, here are examples of legal bootstrap method declarations for dynamically-computed call sites, given various numbers `N` of extra arguments. The first row (marked `*`) will work for any number of extra arguments. Static argument typesNSample bootstrap method*

- `CallSite bootstrap(Lookup caller, String name, MethodType type, Object... args)`
- `CallSite bootstrap(Object... args)`
- `CallSite bootstrap(Object caller, Object... nameAndTypeWithArgs)`

0

- `CallSite bootstrap(Lookup caller, String name, MethodType type)`
- `CallSite bootstrap(Lookup caller, Object... nameAndType)`

1`CallSite bootstrap(Lookup caller, String name, MethodType type, Object arg)`2

- `CallSite bootstrap(Lookup caller, String name, MethodType type, Object... args)`
- `CallSite bootstrap(Lookup caller, String name, MethodType type, String... args)`
- `CallSite bootstrap(Lookup caller, String name, MethodType type, String x, int y)`

 The last example assumes that the extra arguments are of type `String` and `Integer` (or `int`), respectively. The second-to-last example assumes that all extra arguments are of type `String`. The other examples work with all types of extra arguments. Note that all the examples except the second and third also work with dynamically-computed constants if the return type is changed to be compatible with the constant's declared type (such as `Object`, which is always compatible). 

 Since dynamically-computed constants can be provided as static arguments to bootstrap methods, there are no limitations on the types of bootstrap arguments. However, arguments of type `boolean`, `byte`, `short`, or `char` cannot be directly supplied by `CONSTANT_Integer` constant pool entries, since the `asType` conversions do not perform the necessary narrowing primitive conversions. 

 In the above examples, the return type is always `CallSite`, but that is not a necessary feature of bootstrap methods. In the case of a dynamically-computed call site, the only requirement is that the return type of the bootstrap method must be convertible (using the `asType` conversions) to `CallSite`, which means the bootstrap method return type might be `Object` or `ConstantCallSite`. In the case of a dynamically-resolved constant, the return type of the bootstrap method must be convertible to the type of the constant, as represented by its field type descriptor. For example, if the dynamic constant has a field type descriptor of `"C"` (`char`) then the bootstrap method return type could be `Object`, `Character`, or `char`, but not `int` or `Integer`.

Since:1.7

- Related PackagesPackageDescription[java.lang](../package-summary.html)Provides classes that are fundamental to the design of the Java programming language.
- All Classes and InterfacesInterfacesClassesEnum ClassesException ClassesClassDescription[CallSite](CallSite.html)A `CallSite` is a holder for a variable [MethodHandle](MethodHandle.html), which is called its `target`.[ConstantBootstraps](ConstantBootstraps.html)Bootstrap methods for dynamically-computed constants.[ConstantCallSite](ConstantCallSite.html)A `ConstantCallSite` is a [CallSite](CallSite.html) whose target is permanent, and can never be changed.[LambdaConversionException](LambdaConversionException.html)LambdaConversionException[LambdaMetafactory](LambdaMetafactory.html)Methods to facilitate the creation of simple "function objects" that implement one or more interfaces by delegation to a provided [MethodHandle](MethodHandle.html), possibly after type adaptation and partial evaluation of arguments.[MethodHandle](MethodHandle.html)A method handle is a typed, directly executable reference to an underlying method, constructor, field, or similar low-level operation, with optional transformations of arguments or return values.[MethodHandleInfo](MethodHandleInfo.html)A symbolic reference obtained by cracking a direct method handle into its constituent symbolic parts.[MethodHandleProxies](MethodHandleProxies.html)This class consists exclusively of static methods that help adapt method handles to other JVM types, such as interfaces.[MethodHandles](MethodHandles.html)This class consists exclusively of static methods that operate on or return method handles.[MethodHandles.Lookup](MethodHandles.Lookup.html)A lookup object is a factory for creating method handles, when the creation requires access checking.[MethodHandles.Lookup.ClassOption](MethodHandles.Lookup.ClassOption.html)The set of class options that specify whether a hidden class created by [Lookup::defineHiddenClass](MethodHandles.Lookup.html#defineHiddenClass(byte%5B%5D,boolean,java.lang.invoke.MethodHandles.Lookup.ClassOption...)) method is dynamically added as a new member to the nest of a lookup class and/or whether a hidden class has a strong relationship with the class loader marked as its defining loader.[MethodType](MethodType.html)A method type represents the arguments and return type accepted and returned by a method handle, or the arguments and return type passed and expected by a method handle caller.[MutableCallSite](MutableCallSite.html)A `MutableCallSite` is a [CallSite](CallSite.html) whose target variable behaves like an ordinary field.[SerializedLambda](SerializedLambda.html)Serialized form of a lambda expression.[StringConcatException](StringConcatException.html)StringConcatException is thrown by [StringConcatFactory](StringConcatFactory.html) when linkage invariants are violated.[StringConcatFactory](StringConcatFactory.html)Methods to facilitate the creation of String concatenation methods, that can be used to efficiently concatenate a known number of arguments of known types, possibly after type adaptation and partial evaluation of arguments.[SwitchPoint](SwitchPoint.html) A `SwitchPoint` is an object which can publish state transitions to other threads.[TypeDescriptor](TypeDescriptor.html)An entity that has a type descriptor.[TypeDescriptor.OfField](TypeDescriptor.OfField.html)<F extends [TypeDescriptor.OfField](TypeDescriptor.OfField.html)<F>>An entity that has a field type descriptor.[TypeDescriptor.OfMethod](TypeDescriptor.OfMethod.html)<F extends [TypeDescriptor.OfField](TypeDescriptor.OfField.html)<F>,M extends [TypeDescriptor.OfMethod](TypeDescriptor.OfMethod.html)<F,M>>An entity that has a method type descriptor Method descriptors conforming to JVMS [4.3.3](https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.3.3) can be described nominally via [MethodType::describeConstable](MethodType.html#describeConstable()); otherwise they cannot be described nominally.[VarHandle](VarHandle.html)A VarHandle is a dynamically strongly typed reference to a variable, or to a parametrically-defined family of variables, including static fields, non-static fields, array elements, or components of an off-heap data structure.[VarHandle.AccessMode](VarHandle.AccessMode.html)The set of access modes that specify how a variable, referenced by a VarHandle, is accessed.[VarHandle.VarHandleDesc](VarHandle.VarHandleDesc.html)A [nominal descriptor](../../../../java.base/java/lang/constant/package-summary.html#nominal) for a [VarHandle](VarHandle.html) constant.[VolatileCallSite](VolatileCallSite.html)A `VolatileCallSite` is a [CallSite](CallSite.html) whose target acts like a volatile variable.[WrongMethodTypeException](WrongMethodTypeException.html)Thrown to indicate that code has attempted to call a method handle via the wrong method type.
