# Biome Correctness Rules

Rules that prevent bugs and incorrect behavior.

## noArrayIndexKey

Don't use array index as key in React.

```tsx
// BAD - index as key
items.map((item, index) => <li key={index}>{item}</li>)

// GOOD - unique id
items.map((item) => <li key={item.id}>{item.name}</li>)
```

**Why:** Reordering breaks component state.

## noChildrenProp

Don't pass children as props.

```tsx
// BAD
<Component children={<span />} />

// GOOD
<Component>
  <span />
</Component>
```

## noConstAssign

Prevent assignment to const variables.

```typescript
// BAD
const x = 1;
x = 2;  // Error!

// GOOD
let x = 1;
x = 2;
```

## noConstructorReturn

Don't return value from constructor.

```typescript
// BAD
class Foo {
  constructor() {
    return { bad: true };
  }
}

// GOOD
class Foo {
  bad: boolean;
  constructor() {
    this.bad = true;
  }
}
```

## noEmptyCharacterClassInRegex

Empty character class in regex is likely a bug.

```typescript
// BAD
const re = /[]/;  // matches nothing

// GOOD
const re = /./;
```

## noEmptyPattern

Prevent empty destructuring patterns.

```typescript
// BAD
const {} = obj;
const [] = arr;

// GOOD
const { a, b } = obj;
const [first] = arr;
```

## noGlobalObjectCalls

Don't call global objects as functions.

```typescript
// BAD
Math();
JSON();
Reflect();

// GOOD
Math.floor(1.5);
JSON.parse("{}");
```

## noInnerDeclarations

Prevent declarations in nested blocks.

```typescript
// BAD
if (condition) {
  function foo() {}  // hoisting confusion
}

// GOOD
function foo() {}
if (condition) {
  foo();
}
```

## noInvalidConstructorSuper

Validate super() calls in constructors.

```typescript
// BAD - missing super()
class Child extends Parent {
  constructor() {
    this.foo = 1;  // Error: must call super first
  }
}

// GOOD
class Child extends Parent {
  constructor() {
    super();
    this.foo = 1;
  }
}
```

## noInvalidNewBuiltin

Don't use new with Symbol or BigInt.

```typescript
// BAD
const s = new Symbol("foo");
const b = new BigInt(1);

// GOOD
const s = Symbol("foo");
const b = BigInt(1);
```

## noNewSymbol

Same as above - Symbol is not a constructor.

## noNonoctalDecimalEscape

Prevent deprecated octal escapes.

```typescript
// BAD
"\8";
"\9";

// GOOD
"8";
"9";
```

## noPrecisionLoss

Prevent number literals that lose precision.

```typescript
// BAD
const x = 9007199254740993;  // loses precision

// GOOD
const x = 9007199254740992n;  // BigInt
const x = 9007199254740992;   // safe integer
```

## noRenderReturnValue

Don't use return value of ReactDOM.render.

```tsx
// BAD
const app = ReactDOM.render(<App />, root);

// GOOD
ReactDOM.render(<App />, root);
```

## noSelfAssign

Prevent self-assignment.

```typescript
// BAD
x = x;
obj.a = obj.a;

// Remove the useless assignment
```

## noSetterReturn

Setters should not return values.

```typescript
// BAD
class Foo {
  set bar(value) {
    return value;  // useless
  }
}

// GOOD
class Foo {
  set bar(value) {
    this._bar = value;
  }
}
```

## noStringCaseMismatch

Prevent impossible string comparisons.

```typescript
// BAD
s.toLowerCase() === "ABC";  // always false

// GOOD
s.toLowerCase() === "abc";
```

## noSwitchDeclarations

Require block for declarations in switch cases.

```typescript
// BAD
switch (x) {
  case 0:
    let y = 1;  // leaks to other cases
    break;
}

// GOOD
switch (x) {
  case 0: {
    let y = 1;
    break;
  }
}
```

## noUndeclaredVariables

Catch undeclared variable usage.

```typescript
// BAD
console.log(undeclaredVar);

// GOOD
const declaredVar = 1;
console.log(declaredVar);
```

## noUnnecessaryContinue

Remove unnecessary continue statements.

```typescript
// BAD
for (const x of arr) {
  if (x) {
    doSomething();
  } else {
    continue;  // unnecessary
  }
}

// GOOD
for (const x of arr) {
  if (x) {
    doSomething();
  }
}
```

## noUnreachable

Detect unreachable code.

```typescript
// BAD
function foo() {
  return 1;
  console.log("never runs");  // unreachable
}
```

## noUnreachableSuper

Ensure super() is always called.

```typescript
// BAD
class Child extends Parent {
  constructor(cond) {
    if (cond) {
      super();
    }
    // super not called if !cond
  }
}
```

## noUnsafeFinally

Prevent control flow in finally blocks.

```typescript
// BAD
try {
  return 1;
} finally {
  return 2;  // overrides try's return
}

// GOOD
try {
  return 1;
} finally {
  cleanup();
}
```

## noUnsafeOptionalChaining

Prevent unsafe use after optional chain.

```typescript
// BAD
(obj?.foo)();  // might call undefined

// GOOD
obj?.foo?.();
```

## noUnusedImports

Remove unused imports.

```typescript
// BAD
import { unused } from "module";

// GOOD - remove it
```

## noUnusedLabels

Remove unused labels.

```typescript
// BAD
label: {
  break label;
}
unusedLabel: {}  // never referenced
```

## noUnusedPrivateClassMembers

Remove unused private members.

```typescript
// BAD
class Foo {
  #unused = 1;  // never read
}

// Remove it or use it
```

## noUnusedVariables

Remove unused variables.

```typescript
// BAD
const unused = 1;

// GOOD - use underscore for intentionally unused
const _intentionallyUnused = 1;
```

## noVoidElementsWithChildren

Void elements can't have children.

```tsx
// BAD
<img>content</img>
<br>content</br>

// GOOD
<img />
<br />
```

## noVoidTypeReturn

Void functions shouldn't have return value used.

```typescript
// BAD
const result = console.log("hi");

// console.log returns undefined
```

## useArrayLiterals

Use array literals instead of Array constructor.

```typescript
// BAD
new Array(1, 2, 3);

// GOOD
[1, 2, 3];
```

## useExhaustiveDependencies

React hooks must have correct dependencies.

```tsx
// BAD
useEffect(() => {
  doSomething(prop);
}, []);  // missing 'prop'

// GOOD
useEffect(() => {
  doSomething(prop);
}, [prop]);
```

## useHookAtTopLevel

Hooks must be at top level.

```tsx
// BAD
if (condition) {
  useEffect(() => {});
}

// GOOD
useEffect(() => {
  if (condition) {
    // ...
  }
});
```

## useIsNan

Use Number.isNaN() not === NaN.

```typescript
// BAD
if (x === NaN) {}  // always false!

// GOOD
if (Number.isNaN(x)) {}
```

## useJsxKeyInIterable

Elements in iterables need keys.

```tsx
// BAD
items.map(item => <div>{item}</div>);

// GOOD
items.map(item => <div key={item.id}>{item}</div>);
```

## useValidForDirection

Prevent infinite loops.

```typescript
// BAD
for (let i = 0; i < 10; i--) {}  // infinite!

// GOOD
for (let i = 0; i < 10; i++) {}
```

## useYield

Generators must yield.

```typescript
// BAD
function* gen() {
  return 1;  // no yield!
}

// GOOD
function* gen() {
  yield 1;
}
```
