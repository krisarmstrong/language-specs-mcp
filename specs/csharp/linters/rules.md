# Roslyn Analyzer Rules

## Design Rules (CA1xxx)

### CA1000: Do not declare static members on generic types

```csharp
// BAD
public class Cache<T>
{
    public static void Clear() { }  // confusing: Cache<int>.Clear() vs Cache<string>.Clear()
}

// GOOD
public class Cache<T>
{
    public void Clear() { }
}

// Or non-generic companion
public static class Cache
{
    public static void ClearAll() { }
}
```

### CA1002: Do not expose generic lists

```csharp
// BAD
public class Order
{
    public List<Item> Items { get; } = new();
}

// GOOD
public class Order
{
    public IReadOnlyList<Item> Items => _items;
    private readonly List<Item> _items = new();
}
```

### CA1010: Collections should implement generic interface

```csharp
// BAD
public class ItemCollection : IEnumerable
{
    public IEnumerator GetEnumerator() { }
}

// GOOD
public class ItemCollection : IEnumerable<Item>
{
    public IEnumerator<Item> GetEnumerator() { }
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}
```

### CA1018: Mark attributes with AttributeUsageAttribute

```csharp
// BAD
public class MyAttribute : Attribute { }

// GOOD
[AttributeUsage(AttributeTargets.Method, AllowMultiple = false)]
public class MyAttribute : Attribute { }
```

### CA1028: Enum storage should be Int32

```csharp
// BAD - without justification
public enum Status : byte { }

// GOOD - default
public enum Status { }

// OK - when memory/interop matters
[Flags]
public enum Permissions : byte { }
```

### CA1031: Do not catch general exception types

```csharp
// BAD
try { Process(); }
catch (Exception) { }

// GOOD
try { Process(); }
catch (IOException ex)
{
    _logger.LogError(ex, "IO error");
}
catch (InvalidOperationException ex)
{
    _logger.LogError(ex, "Invalid operation");
}
```

### CA1051: Do not declare visible instance fields

```csharp
// BAD
public class Person
{
    public string Name;
}

// GOOD
public class Person
{
    public string Name { get; set; }
}
```

### CA1052: Static holder types should be sealed/static

```csharp
// BAD
public class StringHelper
{
    public static string Trim(string s) => s?.Trim();
}

// GOOD
public static class StringHelper
{
    public static string Trim(string s) => s?.Trim();
}
```

## Globalization Rules (CA13xx)

### CA1303: Do not pass literals as localized parameters

```csharp
// BAD
MessageBox.Show("Operation failed");

// GOOD
MessageBox.Show(Resources.OperationFailed);
```

### CA1304: Specify CultureInfo

```csharp
// BAD
string lower = text.ToLower();

// GOOD
string lower = text.ToLower(CultureInfo.CurrentCulture);
// Or for invariant
string lower = text.ToLowerInvariant();
```

### CA1305: Specify IFormatProvider

```csharp
// BAD
string formatted = number.ToString();

// GOOD
string formatted = number.ToString(CultureInfo.InvariantCulture);
```

### CA1310: Specify StringComparison for correctness

```csharp
// BAD
if (text.StartsWith("prefix")) { }

// GOOD
if (text.StartsWith("prefix", StringComparison.Ordinal)) { }
if (text.StartsWith("prefix", StringComparison.OrdinalIgnoreCase)) { }
```

## Performance Rules (CA18xx)

### CA1802: Use literals where appropriate

```csharp
// BAD
private static readonly string Prefix = "app_";

// GOOD - compile-time constant
private const string Prefix = "app_";
```

### CA1805: Do not initialize unnecessarily

```csharp
// BAD
private int _count = 0;  // default value
private bool _flag = false;
private string? _name = null;

// GOOD
private int _count;
private bool _flag;
private string? _name;
```

### CA1806: Do not ignore method results

```csharp
// BAD
"hello".ToUpper();  // result ignored

// GOOD
string upper = "hello".ToUpper();
```

### CA1812: Avoid uninstantiated internal classes

```csharp
// BAD - never instantiated
internal class Helper
{
    public static void DoWork() { }
}

// GOOD - make static
internal static class Helper
{
    public static void DoWork() { }
}
```

### CA1822: Mark members as static

```csharp
// BAD
public class Calculator
{
    public int Add(int a, int b) => a + b;  // doesn't use 'this'
}

// GOOD
public class Calculator
{
    public static int Add(int a, int b) => a + b;
}
```

### CA1825: Avoid zero-length array allocations

```csharp
// BAD
return new string[0];

// GOOD
return Array.Empty<string>();
```

### CA1826: Use property instead of Linq Enumerable method

```csharp
// BAD
if (array.Count() > 0) { }
var first = list.First();

// GOOD
if (array.Length > 0) { }
var first = list[0];
```

### CA1829: Use Length/Count property instead of Enumerable.Count method

```csharp
// BAD
if (list.Count() > 0) { }

// GOOD
if (list.Count > 0) { }
```

### CA1834: Consider using StringBuilder.Append(char) for single-character strings

```csharp
// BAD
sb.Append(",");

// GOOD
sb.Append(',');
```

### CA1845: Use span-based 'string.Concat'

```csharp
// BAD
string result = s.Substring(0, 5) + s.Substring(10, 5);

// GOOD
string result = string.Concat(s.AsSpan(0, 5), s.AsSpan(10, 5));
```

### CA1846: Prefer AsSpan over Substring

```csharp
// BAD
int.Parse(text.Substring(0, 5));

// GOOD
int.Parse(text.AsSpan(0, 5));
```

## Security Rules (CA2xxx)

### CA2000: Dispose objects before losing scope

```csharp
// BAD
public void Process()
{
    var stream = new FileStream(path, FileMode.Open);
    // might throw before disposal
}

// GOOD
public void Process()
{
    using var stream = new FileStream(path, FileMode.Open);
    // disposed automatically
}
```

### CA2007: Do not directly await a Task

```csharp
// BAD (in library code)
await SomeAsync();

// GOOD
await SomeAsync().ConfigureAwait(false);
```

### CA2012: Use ValueTasks correctly

```csharp
// BAD - awaiting twice
var task = GetValueTaskAsync();
await task;
await task;  // undefined behavior!

// GOOD - await once
var result = await GetValueTaskAsync();
```

### CA2016: Forward the CancellationToken parameter

```csharp
// BAD
public async Task ProcessAsync(CancellationToken cancellationToken)
{
    await DoWorkAsync();  // doesn't pass token
}

// GOOD
public async Task ProcessAsync(CancellationToken cancellationToken)
{
    await DoWorkAsync(cancellationToken);
}
```

### CA2200: Rethrow to preserve stack details

```csharp
// BAD - loses stack trace
catch (Exception ex)
{
    throw ex;
}

// GOOD - preserves stack trace
catch (Exception ex)
{
    // log or handle
    throw;
}
```

### CA2208: Instantiate argument exceptions correctly

```csharp
// BAD - wrong parameter order
throw new ArgumentNullException("Value cannot be null", nameof(value));

// GOOD
throw new ArgumentNullException(nameof(value), "Value cannot be null");

// Better
throw new ArgumentNullException(nameof(value));
```

## Usage Rules (CA22xx)

### CA2211: Non-constant fields should not be visible

```csharp
// BAD
public static int Counter;

// GOOD
private static int _counter;
public static int Counter => _counter;
```

### CA2213: Disposable fields should be disposed

```csharp
// BAD
public class Service : IDisposable
{
    private readonly Stream _stream = new MemoryStream();
    
    public void Dispose() { }  // doesn't dispose _stream
}

// GOOD
public void Dispose()
{
    _stream?.Dispose();
}
```

### CA2214: Do not call overridable methods in constructors

```csharp
// BAD
public class Base
{
    public Base()
    {
        Initialize();  // virtual call
    }
    
    protected virtual void Initialize() { }
}

// GOOD
public class Base
{
    protected virtual void Initialize() { }
}

public class Derived : Base
{
    public Derived()
    {
        Initialize();  // called in derived class
    }
}
```

### CA2225: Operator overloads have named alternates

```csharp
// Provide named method for languages without operator overloading
public static Money operator +(Money a, Money b) => a.Add(b);

public Money Add(Money other) => new(Amount + other.Amount);
```

### CA2227: Collection properties should be read only

```csharp
// BAD
public List<Item> Items { get; set; }

// GOOD
public List<Item> Items { get; } = new();

// Or
public IReadOnlyList<Item> Items => _items;
```

### CA2234: Pass System.Uri objects instead of strings

```csharp
// BAD
client.GetAsync("https://api.example.com");

// GOOD
client.GetAsync(new Uri("https://api.example.com"));
```

### CA2245: Do not assign a property to itself

```csharp
// BAD
this.Name = Name;  // assigns parameter to itself

// GOOD
this.Name = name;
```

### CA2246: Do not assign a symbol and its member in the same statement

```csharp
// BAD
obj = obj.Something;  // confusing

// GOOD
var result = obj.Something;
obj = result;
```

## Code Style Rules (IDE)

### IDE0001-0004: Simplify names

```csharp
// BAD
System.Console.WriteLine();
this.field = value;

// GOOD
Console.WriteLine();  // with using
field = value;        // when unambiguous
```

### IDE0017: Use object initializers

```csharp
// BAD
var person = new Person();
person.Name = "Alice";
person.Age = 30;

// GOOD
var person = new Person
{
    Name = "Alice",
    Age = 30
};
```

### IDE0028: Use collection initializers

```csharp
// BAD
var list = new List<int>();
list.Add(1);
list.Add(2);

// GOOD
var list = new List<int> { 1, 2 };
```

### IDE0057: Use range operator

```csharp
// BAD
var sub = text.Substring(1, text.Length - 1);

// GOOD
var sub = text[1..];
```

### IDE0090: Simplify new expression

```csharp
// BAD
List<int> list = new List<int>();

// GOOD
List<int> list = new();
```
