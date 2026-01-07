# Dart Generation Checklist

**Read this BEFORE writing Dart code. Dart has strong null safety—use it properly.**

## Critical: You Must Do These

### 1. Use Null Safety Correctly
```dart
// BAD - disabling null safety
String? name;
print(name!.length);  // Force unwrap - crashes on null!

// GOOD - null-aware operators
String? name;
print(name?.length ?? 0);  // Safe - returns 0 if null

// GOOD - check first
if (name != null) {
  print(name.length);  // Dart knows it's non-null here
}
```

### 2. Use `final` and `const` Appropriately
```dart
// BAD - mutable when not needed
var name = 'Alice';
var pi = 3.14159;

// GOOD - final for runtime constants
final name = 'Alice';
final now = DateTime.now();  // Runtime value

// GOOD - const for compile-time constants
const pi = 3.14159;
const maxItems = 100;
```

### 3. Use Named Parameters for Clarity
```dart
// BAD - unclear positional parameters
createUser('Alice', 'alice@test.com', true, false, 30);

// GOOD - named parameters
void createUser({
  required String name,
  required String email,
  bool isAdmin = false,
  bool sendWelcome = true,
  int? age,
}) { }

createUser(
  name: 'Alice',
  email: 'alice@test.com',
  isAdmin: true,
);
```

### 4. Handle Async Operations Properly
```dart
// BAD - fire and forget
void loadData() {
  fetchData();  // Returns Future, but ignored!
}

// GOOD - await or handle Future
Future<void> loadData() async {
  try {
    final data = await fetchData();
    process(data);
  } catch (e) {
    handleError(e);
  }
}

// GOOD - if truly fire-and-forget, use unawaited
import 'dart:async';
void logAnalytics() {
  unawaited(sendAnalytics());  // Explicit intent
}
```

### 5. Use Type Annotations Where Not Obvious
```dart
// GOOD - type is obvious, can omit
final name = 'Alice';
final items = <String>[];

// GOOD - type not obvious, include annotation
final User user = getUserFromJson(json);
final Map<String, List<int>> groupedData = processData();
```

## Important: Strong Recommendations

### 6. Use Collection Literals
```dart
// BAD - verbose constructors
var list = List<String>();
var map = Map<String, int>();
var set = Set<int>();

// GOOD - collection literals
var list = <String>[];
var map = <String, int>{};
var set = <int>{};

// GOOD - with initial values
final names = ['Alice', 'Bob'];
final scores = {'Alice': 100, 'Bob': 95};
```

### 7. Use Cascade Notation
```dart
// BAD - repetitive
var paint = Paint();
paint.color = Colors.blue;
paint.strokeWidth = 2.0;
paint.style = PaintingStyle.stroke;

// GOOD - cascade
final paint = Paint()
  ..color = Colors.blue
  ..strokeWidth = 2.0
  ..style = PaintingStyle.stroke;
```

### 8. Use `late` Sparingly
```dart
// BAD - late everywhere
late String name;
late int count;

// GOOD - late only when truly necessary
late final Database db;  // Initialized once, before first use

void init() {
  db = Database.connect();
}

// PREFER - nullable with assertion
String? _name;
String get name => _name!;  // Clearly shows it can fail
```

### 9. Use Pattern Matching (Dart 3+)
```dart
// BAD - verbose type checking
if (shape is Circle) {
  return shape.radius * shape.radius * pi;
} else if (shape is Rectangle) {
  return shape.width * shape.height;
}

// GOOD - pattern matching
double area(Shape shape) => switch (shape) {
  Circle(radius: var r) => r * r * pi,
  Rectangle(width: var w, height: var h) => w * h,
};
```

### 10. Use Records for Multiple Returns (Dart 3+)
```dart
// BAD - custom class for simple grouping
class Point { final int x, y; Point(this.x, this.y); }

// GOOD - record
(int, int) getCoordinates() => (10, 20);

// GOOD - named fields
({int x, int y}) getCoordinates() => (x: 10, y: 20);

final coords = getCoordinates();
print('${coords.x}, ${coords.y}');
```

## Flutter-Specific

### 11. Use `const` Constructors
```dart
// BAD - rebuilds widget every time
Widget build(BuildContext context) {
  return Container(
    child: Text('Hello'),
  );
}

// GOOD - const prevents unnecessary rebuilds
Widget build(BuildContext context) {
  return const Text('Hello');
}
```

### 12. Extract Widgets Instead of Helper Methods
```dart
// BAD - helper method returns widget
Widget _buildHeader() {
  return Container(...);
}

// GOOD - separate widget class
class Header extends StatelessWidget {
  const Header({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(...);
  }
}
```

### 13. Use Keys Properly in Lists
```dart
// BAD - no keys in dynamic lists
ListView.builder(
  itemBuilder: (context, index) => ListTile(
    title: Text(items[index].name),
  ),
);

// GOOD - keys help Flutter track items
ListView.builder(
  itemBuilder: (context, index) => ListTile(
    key: ValueKey(items[index].id),
    title: Text(items[index].name),
  ),
);
```

## Error Handling

### 14. Use Specific Exception Types
```dart
// BAD - generic exception
throw Exception('User not found');

// GOOD - custom exception
class UserNotFoundException implements Exception {
  final String userId;
  UserNotFoundException(this.userId);

  @override
  String toString() => 'User not found: $userId';
}

throw UserNotFoundException(userId);
```

### 15. Use `rethrow` to Preserve Stack Trace
```dart
// BAD - loses original stack trace
try {
  riskyOperation();
} catch (e) {
  log(e);
  throw e;  // Stack trace lost!
}

// GOOD - preserves stack trace
try {
  riskyOperation();
} catch (e) {
  log(e);
  rethrow;  // Stack trace preserved
}
```

---

**Quick Reference - Copy This Mental Model:**
- Null-aware operators (`?.`, `??`, `!`)
- `final` for runtime, `const` for compile-time
- Named parameters for clarity
- `async`/`await` with try-catch
- Collection literals
- Cascade notation (`..`)
- `late` only when necessary
- Pattern matching (Dart 3+)
- Records for multiple returns
- `const` constructors in Flutter
- Extract widgets, not helper methods
- Keys in dynamic lists
- `rethrow` preserves stack trace
