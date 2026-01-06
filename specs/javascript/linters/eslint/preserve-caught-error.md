# preserve-caught-error

Disallow losing originally caught error when re-throwing custom errors

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [requireCatchParameter](#requirecatchparameter)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Further Reading](#further-reading)
6. [Resources](#resources)

JavaScript developers often re-throw errors in `catch` blocks to add context but forget to preserve the original error, resulting in lost debugging information.

Using the `cause` option when throwing new errors helps retain the original error and maintain complete error chains, which improves debuggability and traceability.

```
try {
	await fetch("https://xyz.com/resource");
} catch(error) {
	// Throw a more specific error without losing original context
	throw new Error("Failed to fetch resource", {
		cause: error
	});
}
1
2
3
4
5
6
7
8
```

Copy code to clipboard

## Rule Details

This rule enforces the use of the `cause` property when throwing a new error inside a `catch` block.

Checks for all built-in `error types` that support passing a `cause`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZXNlcnZlLWNhdWdodC1lcnJvcjogXCJlcnJvclwiICovXG5cbi8vIE5vdCB1c2luZyB0aGUgYGNhdXNlYCBvcHRpb25cbnRyeSB7XG4gICAgLy8gLi4uXG59IGNhdGNoIChlcnJvcikge1xuICAgIHRocm93IG5ldyBFcnJvcihcIlNvbWV0aGluZyB3ZW50IHdyb25nOiBcIiArIGVycm9yLm1lc3NhZ2UpO1xufVxuXG4vLyBUaHJvd2luZyBhIG5ldyBFcnJvciB3aXRoIHVucmVsYXRlZCBjYXVzZVxudHJ5IHtcblx0ZG9Tb21ldGhpbmcoKTtcbn0gY2F0Y2ggKGVycikge1xuXHRjb25zdCB1bnJlbGF0ZWQgPSBuZXcgRXJyb3IoXCJvdGhlclwiKTtcblx0dGhyb3cgbmV3IEVycm9yKFwiU29tZXRoaW5nIGZhaWxlZFwiLCB7IGNhdXNlOiB1bnJlbGF0ZWQgfSk7XG59XG5cbi8vIENhdWdodCBlcnJvciBpcyBiZWluZyBsb3N0IHBhcnRpYWxseSBkdWUgdG8gZGVzdHJ1Y3R1cmluZ1xudHJ5IHtcblx0ZG9Tb21ldGhpbmcoKTtcbn0gY2F0Y2ggKHsgbWVzc2FnZSwgLi4ucmVzdCB9KSB7XG5cdHRocm93IG5ldyBFcnJvcihtZXNzYWdlKTtcbn1cblxuLy8gQ2F1c2UgZXJyb3IgaXMgYmVpbmcgc2hhZG93ZWQgYnkgYSBjbG9zZXIgc2NvcGVkIHJlZGVjbGFyYXRpb24uXG50cnkge1xuICAgIGRvU29tZXRoaW5nKCk7XG59IGNhdGNoIChlcnJvcikge1xuICAgIGlmICh3aGF0ZXZlcikge1xuICAgICAgICBjb25zdCBlcnJvciA9IGFub3RoZXJFcnJvcjsgLy8gVGhpcyBkZWNsYXJhdGlvbiBpcyB0aGUgcHJvYmxlbS5cbiAgICAgICAgdGhyb3cgbmV3IEVycm9yKFwiU29tZXRoaW5nIHdlbnQgd3JvbmdcIiwgeyBjYXVzZTogZXJyb3IgfSk7XG4gICAgfVxufSJ9)

```
/* eslint preserve-caught-error: "error" */

// Not using the `cause` option
try {
    // ...
} catch (error) {
    throw new Error("Something went wrong: " + error.message);
}

// Throwing a new Error with unrelated cause
try {
	doSomething();
} catch (err) {
	const unrelated = new Error("other");
	throw new Error("Something failed", { cause: unrelated });
}

// Caught error is being lost partially due to destructuring
try {
	doSomething();
} catch ({ message, ...rest }) {
	throw new Error(message);
}

// Cause error is being shadowed by a closer scoped redeclaration.
try {
    doSomething();
} catch (error) {
    if (whatever) {
        const error = anotherError; // This declaration is the problem.
        throw new Error("Something went wrong", { cause: error });
    }
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZXNlcnZlLWNhdWdodC1lcnJvcjogXCJlcnJvclwiICovXG5cbnRyeSB7XG4gICAgLy8gLi4uXG59IGNhdGNoIChlcnJvcikge1xuICAgIHRocm93IG5ldyBFcnJvcihcIlNvbWV0aGluZyB3ZW50IHdyb25nXCIsIHsgY2F1c2U6IGVycm9yIH0pO1xufVxuXG4vLyBXaGVuIHRoZSB0aHJvd24gZXJyb3IgaXMgbm90IGRpcmVjdGx5IHJlbGF0ZWQgdG8gdGhlIGNhdWdodCBlcnJvci5cbnRyeSB7XG59IGNhdGNoIChlcnJvcikge1xuXHRmb28gPSB7XG5cdFx0YmFyKCkge1xuXHRcdFx0Ly8gVGhpcyB0aHJvdyBpcyBub3QgZGlyZWN0bHkgcmVsYXRlZCB0byB0aGUgY2F1Z2h0IGVycm9yLlxuXHRcdFx0dGhyb3cgbmV3IEVycm9yKFwiU29tZXRoaW5nIHdlbnQgd3JvbmdcIik7XG5cdFx0fVxuXHR9O1xufVxuXG4vLyBObyB0aHJvdyBpbnNpZGUgY2F0Y2hcbnRyeSB7XG4gICAgZG9Tb21ldGhpbmcoKTtcbn0gY2F0Y2ggKGUpIHtcbiAgICBjb25zb2xlLmVycm9yKGUpO1xufVxuXG4vLyBJZ25vcmluZyB0aGUgY2F1Z2h0IGVycm9yIGF0IHRoZSBwYXJhbWV0ZXIgbGV2ZWxcbi8vIFRoaXMgaXMgdmFsaWQgYnkgZGVmYXVsdCwgYnV0IHRoaXMgYmVoYXZpb3IgY2FuIGJlIGNoYW5nZWRcbi8vIGJ5IHVzaW5nIHRoZSBgcmVxdWlyZUNhdGNoUGFyYW1ldGVyYCBvcHRpb24gZGlzY3Vzc2VkIGJlbG93LlxudHJ5IHtcblx0ZG9Tb21ldGhpbmcoKTtcbn0gY2F0Y2gge1xuXHR0aHJvdyBuZXcgVHlwZUVycm9yKFwiU29tZXRoaW5nIHdlbnQgd3JvbmdcIik7XG59In0=)

```
/* eslint preserve-caught-error: "error" */

try {
    // ...
} catch (error) {
    throw new Error("Something went wrong", { cause: error });
}

// When the thrown error is not directly related to the caught error.
try {
} catch (error) {
	foo = {
		bar() {
			// This throw is not directly related to the caught error.
			throw new Error("Something went wrong");
		}
	};
}

// No throw inside catch
try {
    doSomething();
} catch (e) {
    console.error(e);
}

// Ignoring the caught error at the parameter level
// This is valid by default, but this behavior can be changed
// by using the `requireCatchParameter` option discussed below.
try {
	doSomething();
} catch {
	throw new TypeError("Something went wrong");
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
```

## Options

This rule takes a single option — an object with the following optional property:

- `requireCatchParameter`: Requires the catch blocks to always have the caught error parameter when set to `true`. By default, this is `false`.

### requireCatchParameter

Enabling this option mandates for all the catch blocks to have a caught error parameter. This makes sure that the caught error is not discarded at the parameter level.

```
"preserve-caught-error": ["error", {
  "requireCatchParameter": true
}]
1
2
3
```

Copy code to clipboard

Example of incorrect code for the `{ "requireCatchParameter": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZXNlcnZlLWNhdWdodC1lcnJvcjogW1wiZXJyb3JcIiwgeyBcInJlcXVpcmVDYXRjaFBhcmFtZXRlclwiOiB0cnVlIH1dICovXG5cbnRyeSB7XG5cdGRvU29tZXRoaW5nKCk7XG59IGNhdGNoIHsgLy8gQ2FuJ3QgZGlzY2FyZCB0aGUgZXJyb3Ig4p2MXG5cdHRocm93IG5ldyBFcnJvcihcIlNvbWV0aGluZyB3ZW50IHdyb25nXCIpO1xufSJ9)

```
/* eslint preserve-caught-error: ["error", { "requireCatchParameter": true }] */

try {
	doSomething();
} catch { // Can't discard the error ❌
	throw new Error("Something went wrong");
}
1
2
3
4
5
6
7
```

Example of correct code for the `{ "requireCatchParameter": true }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IHByZXNlcnZlLWNhdWdodC1lcnJvcjogW1wiZXJyb3JcIiwgeyBcInJlcXVpcmVDYXRjaFBhcmFtZXRlclwiOiB0cnVlIH1dICovXG5cbnRyeSB7XG5cdGRvU29tZXRoaW5nKCk7XG59IGNhdGNoKGVycm9yKSB7IC8vIEVycm9yIGlzIGJlaW5nIHJlZmVyZW5jZWQg4pyFXG5cdC8vIEhhbmRsaW5nIGFuZCByZS10aHJvdyBsb2dpY1xufSJ9)

```
/* eslint preserve-caught-error: ["error", { "requireCatchParameter": true }] */

try {
	doSomething();
} catch(error) { // Error is being referenced ✅
	// Handling and re-throw logic
}
1
2
3
4
5
6
7
```

## When Not To Use It

You might not want to enable this rule if:

- 

You follow a custom error-handling approach where the original error is intentionally omitted from re-thrown errors (e.g., to avoid exposing internal details or to log the original error separately).

- 

You use a third-party or internal error-handling library that preserves error context using non-standard properties (e.g., [verror](https://www.npmjs.com/package/verror)) instead of the cause option.

- 

(In rare cases) you are targeting legacy environments where the cause option in `Error` constructors is not supported.

## Version

This rule was introduced in ESLint v9.35.0.

## Further Reading

[MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause)
 developer.mozilla.org[Errors | Node.js v24.3.0 Documentation](https://nodejs.org/api/errors.html#errorcause)
 nodejs.org[proposal-error-cause/README.md at main · tc39/proposal-error-cause](https://github.com/tc39/proposal-error-cause/blob/main/README.md)
 github.com[Never lose valuable error context in JavaScript - DEV Community](https://dev.to/amnish04/never-lose-valuable-error-context-in-javascript-3aco)
 dev.to[Error types that support `cause`](https://github.com/microsoft/TypeScript/blob/main/src/lib/es2022.error.d.ts)
 github.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/preserve-caught-error.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/preserve-caught-error.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/preserve-caught-error.md
                    
                
                )
