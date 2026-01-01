# Checkstyle Rules

## Naming Conventions

### TypeName

Classes, interfaces, enums, records use PascalCase.

```java
// BAD
class myClass { }
interface myInterface { }

// GOOD
class MyClass { }
interface MyInterface { }
```

### MethodName

Methods use camelCase.

```java
// BAD
void DoSomething() { }
void do_something() { }

// GOOD
void doSomething() { }
```

### ConstantName

Constants use UPPER_SNAKE_CASE.

```java
// BAD
static final int maxSize = 100;
static final int MaxSize = 100;

// GOOD
static final int MAX_SIZE = 100;
```

### MemberName

Instance fields use camelCase.

```java
// BAD
private String Name;
private String _name;

// GOOD
private String name;
```

### ParameterName

Parameters use camelCase.

```java
// BAD
void process(String Name, int Value) { }

// GOOD
void process(String name, int value) { }
```

### LocalVariableName

Local variables use camelCase.

```java
// BAD
int Counter = 0;
int my_counter = 0;

// GOOD
int counter = 0;
```

### PackageName

Packages use lowercase.

```java
// BAD
package com.Example.MyApp;

// GOOD
package com.example.myapp;
```

## Import Checks

### AvoidStarImport

No wildcard imports.

```java
// BAD
import java.util.*;
import static org.junit.Assert.*;

// GOOD
import java.util.List;
import java.util.Map;
import static org.junit.Assert.assertEquals;
```

### UnusedImports

No unused imports.

```java
// BAD
import java.util.List;  // never used

public class Foo {
    private String name;
}
```

### RedundantImport

No redundant imports.

```java
// BAD
import java.lang.String;  // java.lang auto-imported
import java.util.List;
import java.util.List;    // duplicate

// GOOD
import java.util.List;
```

### IllegalImport

Block certain imports.

```java
// BAD (if sun.* is blocked)
import sun.misc.Unsafe;

// GOOD
// Use standard APIs instead
```

### ImportOrder

Enforce import ordering.

```java
// GOOD (typical ordering)
import java.io.File;       // java.*
import java.util.List;

import javax.servlet.*;     // javax.*

import org.apache.commons.*; // third-party

import com.mycompany.*;     // own packages

import static org.junit.Assert.*;  // static imports last
```

## Size Violations

### LineLength

Maximum line length.

```java
// BAD (if max is 120)
String message = "This is a very long line that exceeds the maximum allowed line length and should be wrapped";

// GOOD
String message = "This is a very long line that exceeds " +
    "the maximum allowed line length and should be wrapped";
```

### FileLength

Maximum file line count.

### MethodLength

Maximum method line count.

```java
// BAD - method too long (>150 lines default)
public void processEverything() {
    // 200 lines of code
}

// GOOD - break into smaller methods
public void processEverything() {
    validateInput();
    processData();
    generateOutput();
}
```

### ParameterNumber

Maximum parameters per method.

```java
// BAD - too many parameters
public void configure(String a, String b, int c, int d, 
                     boolean e, boolean f, String g, int h) { }

// GOOD - use parameter object
public void configure(Configuration config) { }
```

### AnonInnerLength

Maximum anonymous inner class length.

```java
// BAD - anonymous class too long
button.addActionListener(new ActionListener() {
    // 50 lines of code
});

// GOOD - extract to named class or lambda
button.addActionListener(e -> handleClick(e));
```

## Whitespace

### WhitespaceAround

Whitespace around tokens.

```java
// BAD
int x=1+2;
if(condition){

// GOOD
int x = 1 + 2;
if (condition) {
```

### WhitespaceAfter

Whitespace after comma, semicolon.

```java
// BAD
int a,b,c;
for(int i=0;i<10;i++)

// GOOD
int a, b, c;
for (int i = 0; i < 10; i++)
```

### NoWhitespaceBefore

No whitespace before comma, semicolon.

```java
// BAD
method(a , b) ;

// GOOD
method(a, b);
```

### NoWhitespaceAfter

No whitespace after certain tokens.

```java
// BAD
int [] array;
method( arg);
! condition;

// GOOD
int[] array;
method(arg);
!condition;
```

### GenericWhitespace

Whitespace around generic brackets.

```java
// BAD
List< String >list = new ArrayList <String>();

// GOOD
List<String> list = new ArrayList<String>();
```

### EmptyLineSeparator

Blank lines between sections.

```java
// BAD
package com.example;
import java.util.List;
public class Foo {
    private int x;
    public void method() { }
}

// GOOD
package com.example;

import java.util.List;

public class Foo {

    private int x;

    public void method() { }
}
```

### OperatorWrap

Operator placement on line breaks.

```java
// BAD
String s = "a" +
           "b";

// GOOD (operator at end)
String s = "a"
         + "b";
```

## Block Checks

### NeedBraces

Require braces for control statements.

```java
// BAD
if (condition)
    doSomething();

for (int i = 0; i < 10; i++)
    process(i);

// GOOD
if (condition) {
    doSomething();
}

for (int i = 0; i < 10; i++) {
    process(i);
}
```

### LeftCurly

Opening brace placement.

```java
// BAD (if eol style)
if (condition)
{
    doSomething();
}

// GOOD (eol style)
if (condition) {
    doSomething();
}
```

### RightCurly

Closing brace placement.

```java
// BAD
if (condition) {
    doSomething();
}
else {
    doOther();
}

// GOOD
if (condition) {
    doSomething();
} else {
    doOther();
}
```

### EmptyBlock

No empty blocks.

```java
// BAD
if (condition) {
}

try {
    riskyOperation();
} catch (Exception e) {
}

// GOOD
if (condition) {
    // intentionally empty - explain why
}

try {
    riskyOperation();
} catch (Exception e) {
    log.error("Operation failed", e);
}
```

### AvoidNestedBlocks

Avoid unnecessary nested blocks.

```java
// BAD
{
    int x = 1;
    process(x);
}

// GOOD - remove unnecessary block
int x = 1;
process(x);
```

## Coding

### MagicNumber

No magic numbers.

```java
// BAD
if (status == 200) { }
double area = 3.14159 * r * r;

// GOOD
private static final int HTTP_OK = 200;
private static final double PI = Math.PI;

if (status == HTTP_OK) { }
double area = PI * r * r;
```

### MissingSwitchDefault

Switch needs default case.

```java
// BAD
switch (value) {
    case 1:
        break;
    case 2:
        break;
}

// GOOD
switch (value) {
    case 1:
        break;
    case 2:
        break;
    default:
        throw new IllegalArgumentException("Unknown value: " + value);
}
```

### FallThrough

No fall-through in switch.

```java
// BAD
switch (value) {
    case 1:
        doOne();
    case 2:  // falls through!
        doTwo();
        break;
}

// GOOD
switch (value) {
    case 1:
        doOne();
        // fall through - intentional
    case 2:
        doTwo();
        break;
}
```

### SimplifyBooleanExpression

Simplify boolean expressions.

```java
// BAD
if (condition == true) { }
if (condition == false) { }
return condition ? true : false;

// GOOD
if (condition) { }
if (!condition) { }
return condition;
```

### SimplifyBooleanReturn

Simplify boolean returns.

```java
// BAD
if (condition) {
    return true;
} else {
    return false;
}

// GOOD
return condition;
```

### StringLiteralEquality

Use equals for string comparison.

```java
// BAD
if (str == "value") { }

// GOOD
if ("value".equals(str)) { }
if (str.equals("value")) { }  // may NPE
```

### EqualsHashCode

equals and hashCode together.

```java
// BAD - only one implemented
@Override
public boolean equals(Object obj) { }
// missing hashCode!

// GOOD - both implemented
@Override
public boolean equals(Object obj) { }

@Override
public int hashCode() { }
```

### HiddenField

No hidden fields.

```java
// BAD
class Foo {
    private String name;
    
    public void setName(String name) {  // hides field
        name = name;  // assigns to parameter!
    }
}

// GOOD
public void setName(String name) {
    this.name = name;
}
```

### IllegalCatch

Don't catch generic exceptions.

```java
// BAD
try {
    process();
} catch (Exception e) { }

// VERY BAD
try {
    process();
} catch (Throwable t) { }

// GOOD
try {
    process();
} catch (IOException | SQLException e) {
    handle(e);
}
```

### IllegalThrows

Don't throw generic exceptions.

```java
// BAD
public void process() throws Exception { }
public void process() throws Throwable { }

// GOOD
public void process() throws IOException, SQLException { }
```

### InnerAssignment

No assignments in expressions.

```java
// BAD
if ((result = calculate()) > 0) { }
String line;
while ((line = reader.readLine()) != null) { }

// GOOD
result = calculate();
if (result > 0) { }

// Exception: while loop idiom often allowed
```

### ModifiedControlVariable

Don't modify loop variable.

```java
// BAD
for (int i = 0; i < 10; i++) {
    if (condition) {
        i = i + 2;  // modifying loop variable
    }
}

// GOOD
for (int i = 0; i < 10; i++) {
    // don't modify i in loop body
}
```

### MultipleVariableDeclarations

One variable per declaration.

```java
// BAD
int x, y, z;
int a = 1, b = 2;

// GOOD
int x;
int y;
int z;
int a = 1;
int b = 2;
```

### OneStatementPerLine

One statement per line.

```java
// BAD
int a = 1; int b = 2;
if (x) doA(); else doB();

// GOOD
int a = 1;
int b = 2;

if (x) {
    doA();
} else {
    doB();
}
```

### OverloadMethodsDeclarationOrder

Group overloaded methods.

```java
// BAD
void process(String s) { }
void other() { }
void process(int i) { }  // separated

// GOOD
void process(String s) { }
void process(int i) { }
void other() { }
```

### PackageDeclaration

Package statement required.

```java
// BAD - no package
public class Foo { }

// GOOD
package com.example;

public class Foo { }
```

### ParameterAssignment

Don't assign to parameters.

```java
// BAD
public void process(String input) {
    input = input.trim();
}

// GOOD
public void process(String input) {
    String trimmed = input.trim();
}
```

### RequireThis

Require this for instance members.

```java
// BAD (if requireThis enabled)
class Foo {
    private String name;
    public String getName() {
        return name;
    }
}

// GOOD
class Foo {
    private String name;
    public String getName() {
        return this.name;
    }
}
```

### UnnecessaryParentheses

No unnecessary parentheses.

```java
// BAD
return (x);
int y = (x + 1);
if ((x == 1)) { }

// GOOD
return x;
int y = x + 1;
if (x == 1) { }
```

### VariableDeclarationUsageDistance

Declare variables close to use.

```java
// BAD
String name = getName();
// 20 lines of unrelated code
process(name);

// GOOD
// do unrelated work
String name = getName();
process(name);
```

## Design

### FinalClass

Classes with private constructors should be final.

```java
// BAD
public class Utility {
    private Utility() { }  // private constructor
    // but class not final
}

// GOOD
public final class Utility {
    private Utility() { }
}
```

### HideUtilityClassConstructor

Utility classes need private constructor.

```java
// BAD
public class StringUtils {
    public static String trim(String s) { }
}

// GOOD
public final class StringUtils {
    private StringUtils() { }  // prevent instantiation
    public static String trim(String s) { }
}
```

### InterfaceIsType

Interfaces shouldn't be constant-only.

```java
// BAD
public interface Constants {
    int MAX_SIZE = 100;
    String PREFIX = "app";
}

// GOOD
public final class Constants {
    public static final int MAX_SIZE = 100;
    public static final String PREFIX = "app";
    private Constants() { }
}
```

### VisibilityModifier

Fields should be private.

```java
// BAD
public class Foo {
    public String name;
}

// GOOD
public class Foo {
    private String name;
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

### MutableException

Exceptions should be immutable.

```java
// BAD
public class MyException extends Exception {
    private String details;  // mutable!
    public void setDetails(String d) { details = d; }
}

// GOOD
public class MyException extends Exception {
    private final String details;
    public MyException(String message, String details) {
        super(message);
        this.details = details;
    }
}
```

## Javadoc

### JavadocType

Classes need Javadoc.

```java
// BAD
public class Service { }

// GOOD
/**
 * Service for processing orders.
 */
public class Service { }
```

### JavadocMethod

Public methods need Javadoc.

```java
// BAD
public void process(String input) { }

// GOOD
/**
 * Processes the input string.
 *
 * @param input the string to process
 * @throws IllegalArgumentException if input is null
 */
public void process(String input) { }
```

### JavadocVariable

Public fields need Javadoc.

```java
// BAD
public static final int MAX_SIZE = 100;

// GOOD
/** Maximum allowed size in bytes. */
public static final int MAX_SIZE = 100;
```

### MissingJavadocMethod

Missing Javadoc on public methods.

### MissingJavadocType

Missing Javadoc on public types.

### InvalidJavadocPosition

Javadoc must be before annotations.

```java
// BAD
@Override
/** Bad position. */
public void method() { }

// GOOD
/** Good position. */
@Override
public void method() { }
```

### NonEmptyAtclauseDescription

Javadoc tags need descriptions.

```java
// BAD
/**
 * @param input
 * @return
 */

// GOOD
/**
 * @param input the input to process
 * @return the processed result
 */
```
