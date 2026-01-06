# TypeScript Language Specification
Version: 5.9.3

Source: https://www.typescriptlang.org/docs/handbook/


## Basic Types

```typescript
// Primitives
let isDone: boolean = false;
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
let big: bigint = 100n;
let color: string = "blue";
let sym: symbol = Symbol("key");

// Arrays
let list: number[] = [1, 2, 3];
let list: Array<number> = [1, 2, 3];
let tuple: [string, number] = ["hello", 10];

// Special types
let notSure: unknown = 4;
let nothing: void = undefined;
let u: undefined = undefined;
let n: null = null;
let neverReturns: never;  // function that never returns
```

## Type Annotations

```typescript
// Variables
let name: string = "Alice";

// Functions
function greet(name: string): string {
    return `Hello, ${name}`;
}

// Arrow functions
const add = (a: number, b: number): number => a + b;

// Optional parameters
function greet(name: string, greeting?: string): string {
    return `${greeting ?? "Hello"}, ${name}`;
}

// Default parameters
function greet(name: string, greeting: string = "Hello"): string {
    return `${greeting}, ${name}`;
}

// Rest parameters
function sum(...numbers: number[]): number {
    return numbers.reduce((a, b) => a + b, 0);
}
```

## Interfaces

```typescript
interface User {
    id: number;
    name: string;
    email: string;
    age?: number;  // optional
    readonly createdAt: Date;  // readonly
}

// Extending interfaces
interface Admin extends User {
    permissions: string[];
}

// Function types
interface SearchFunc {
    (source: string, subString: string): boolean;
}

// Index signatures
interface StringMap {
    [key: string]: string;
}

// Callable
interface Callable {
    (arg: string): void;
    property: string;
}
```

## Type Aliases

```typescript
type ID = string | number;
type Point = { x: number; y: number };
type Callback = (data: string) => void;

// Generic type alias
type Container<T> = { value: T };
type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };
```

## Union and Intersection Types

```typescript
// Union - either type
type StringOrNumber = string | number;
type Status = "pending" | "approved" | "rejected";

function format(value: string | number): string {
    if (typeof value === "string") {
        return value.toUpperCase();
    }
    return value.toFixed(2);
}

// Intersection - both types
type Employee = Person & { employeeId: number };

interface Colorful {
    color: string;
}
interface Circle {
    radius: number;
}
type ColorfulCircle = Colorful & Circle;
```

## Literal Types

```typescript
// String literals
type Direction = "north" | "south" | "east" | "west";

// Numeric literals
type DiceRoll = 1 | 2 | 3 | 4 | 5 | 6;

// Boolean literal
type True = true;

// Template literal types
type EventName = `on${string}`;
type PropName = `get${Capitalize<string>}`;
```

## Generics

```typescript
// Generic function
function identity<T>(arg: T): T {
    return arg;
}

// Generic interface
interface Box<T> {
    contents: T;
}

// Generic class
class Queue<T> {
    private data: T[] = [];
    
    push(item: T): void {
        this.data.push(item);
    }
    
    pop(): T | undefined {
        return this.data.shift();
    }
}

// Generic constraints
interface HasLength {
    length: number;
}

function logLength<T extends HasLength>(arg: T): number {
    return arg.length;
}

// Multiple type parameters
function pair<T, U>(first: T, second: U): [T, U] {
    return [first, second];
}

// Default type parameters
type Container<T = string> = { value: T };
```

## Utility Types

```typescript
// Partial - all properties optional
type PartialUser = Partial<User>;

// Required - all properties required
type RequiredUser = Required<User>;

// Readonly - all properties readonly
type ReadonlyUser = Readonly<User>;

// Pick - select properties
type UserPreview = Pick<User, "id" | "name">;

// Omit - exclude properties
type UserWithoutEmail = Omit<User, "email">;

// Record - construct object type
type UserMap = Record<string, User>;

// Exclude - exclude from union
type NotNull = Exclude<string | null | undefined, null | undefined>;

// Extract - extract from union
type JustStrings = Extract<string | number | boolean, string>;

// NonNullable - remove null/undefined
type NotNullable = NonNullable<string | null>;

// ReturnType - get function return type
type Returned = ReturnType<typeof someFunction>;

// Parameters - get function parameters as tuple
type Params = Parameters<typeof someFunction>;

// Awaited - unwrap Promise
type Data = Awaited<Promise<string>>;  // string
```

## Type Guards

```typescript
// typeof guard
function process(value: string | number) {
    if (typeof value === "string") {
        // value is string here
        return value.toUpperCase();
    }
    // value is number here
    return value * 2;
}

// instanceof guard
function logDate(value: Date | string) {
    if (value instanceof Date) {
        console.log(value.toISOString());
    } else {
        console.log(value);
    }
}

// in guard
interface Fish {
    swim: () => void;
}
interface Bird {
    fly: () => void;
}

function move(animal: Fish | Bird) {
    if ("swim" in animal) {
        animal.swim();
    } else {
        animal.fly();
    }
}

// Custom type guard
function isString(value: unknown): value is string {
    return typeof value === "string";
}

function isUser(value: unknown): value is User {
    return (
        typeof value === "object" &&
        value !== null &&
        "id" in value &&
        "name" in value
    );
}
```

## Discriminated Unions

```typescript
interface Circle {
    kind: "circle";
    radius: number;
}

interface Square {
    kind: "square";
    sideLength: number;
}

interface Rectangle {
    kind: "rectangle";
    width: number;
    height: number;
}

type Shape = Circle | Square | Rectangle;

function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2;
        case "square":
            return shape.sideLength ** 2;
        case "rectangle":
            return shape.width * shape.height;
    }
}
```

## Classes

```typescript
class Animal {
    // Properties
    public name: string;
    protected age: number;
    private secret: string;
    readonly species: string;
    
    // Static
    static count = 0;
    
    // Constructor
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
        this.secret = "hidden";
        this.species = "unknown";
        Animal.count++;
    }
    
    // Methods
    speak(): void {
        console.log(`${this.name} makes a sound`);
    }
    
    // Getters/setters
    get info(): string {
        return `${this.name}, age ${this.age}`;
    }
    
    set nickname(value: string) {
        this.name = value;
    }
}

// Inheritance
class Dog extends Animal {
    constructor(name: string, age: number) {
        super(name, age);
    }
    
    override speak(): void {
        console.log(`${this.name} barks`);
    }
}

// Abstract classes
abstract class Shape {
    abstract area(): number;
    
    describe(): string {
        return `Area: ${this.area()}`;
    }
}

// Implementing interfaces
interface Printable {
    print(): void;
}

class Document implements Printable {
    print(): void {
        console.log("Printing...");
    }
}
```

## Enums

```typescript
// Numeric enum
enum Direction {
    Up,      // 0
    Down,    // 1
    Left,    // 2
    Right,   // 3
}

// String enum
enum Status {
    Pending = "PENDING",
    Approved = "APPROVED",
    Rejected = "REJECTED",
}

// Const enum (inlined at compile time)
const enum Color {
    Red,
    Green,
    Blue,
}

// Usage
let dir: Direction = Direction.Up;
let status: Status = Status.Pending;
```

## Modules

```typescript
// Export
export const PI = 3.14159;
export function add(a: number, b: number): number {
    return a + b;
}
export class Calculator {}
export type Result = { value: number };
export interface Config {}

// Default export
export default class MyClass {}

// Import
import { add, PI } from "./math";
import type { Result } from "./math";
import MyClass from "./myclass";
import * as math from "./math";

// Re-export
export { add } from "./math";
export * from "./utils";
export type { Config } from "./config";
```

## Decorators

```typescript
// Class decorator
function logged(constructor: Function) {
    console.log(`Creating: ${constructor.name}`);
}

@logged
class MyClass {}

// Method decorator
function log(target: any, key: string, descriptor: PropertyDescriptor) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.log(`Calling ${key}`);
        return original.apply(this, args);
    };
}

class Calculator {
    @log
    add(a: number, b: number) {
        return a + b;
    }
}

// Property decorator
function required(target: any, key: string) {
    // validation logic
}
```

## Conditional Types

```typescript
// Basic conditional
type IsString<T> = T extends string ? true : false;

// Infer keyword
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type ElementType<T> = T extends (infer E)[] ? E : never;

// Distributive conditional types
type ToArray<T> = T extends any ? T[] : never;
type StrOrNumArray = ToArray<string | number>;  // string[] | number[]
```

## Mapped Types

```typescript
// Make all properties optional
type Partial<T> = {
    [P in keyof T]?: T[P];
};

// Make all properties required
type Required<T> = {
    [P in keyof T]-?: T[P];
};

// Make all properties readonly
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};

// Custom mapped type
type Getters<T> = {
    [P in keyof T as `get${Capitalize<string & P>}`]: () => T[P];
};
```

## Template Literal Types

```typescript
type World = "world";
type Greeting = `hello ${World}`;  // "hello world"

type EmailLocale = "welcome_email" | "email_heading";
type FooterLocale = "footer_title" | "footer_sendoff";
type AllLocale = `${EmailLocale | FooterLocale}_id`;

// With mapped types
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
```

## Satisfies Operator (4.9+)

```typescript
// Type-check without widening
const config = {
    width: 100,
    height: 200,
} satisfies Record<string, number>;

// config.width is still number, not string | number

// Useful for complex object literals
type Colors = "red" | "green" | "blue";
const palette = {
    red: [255, 0, 0],
    green: "#00ff00",
    blue: [0, 0, 255],
} satisfies Record<Colors, string | number[]>;

// palette.green is string, not string | number[]
```

## Const Assertions

```typescript
// as const makes everything readonly and literal
const config = {
    endpoint: "https://api.example.com",
    retries: 3,
} as const;

// config.endpoint is "https://api.example.com", not string
// config.retries is 3, not number

const directions = ["up", "down"] as const;
// directions is readonly ["up", "down"]
type Direction = (typeof directions)[number];  // "up" | "down"
```
