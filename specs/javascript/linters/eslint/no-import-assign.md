# no-import-assign

Disallow assigning to imported bindings

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Handled by TypeScript](#handled_by_typescript)
4. [Version](#version)
5. [Resources](#resources)

The updates of imported bindings by ES Modules cause runtime errors.

## Rule Details

This rule warns the assignments, increments, and decrements of imported bindings.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wb3J0LWFzc2lnbjogXCJlcnJvclwiKi9cblxuaW1wb3J0IG1vZCwgeyBuYW1lZCB9IGZyb20gXCIuL21vZC5tanNcIlxuaW1wb3J0ICogYXMgbW9kX25zIGZyb20gXCIuL21vZC5tanNcIlxuXG5tb2QgPSAxICAgICAgICAgIC8vIEVSUk9SOiAnbW9kJyBpcyByZWFkb25seS5cbm5hbWVkID0gMiAgICAgICAgLy8gRVJST1I6ICduYW1lZCcgaXMgcmVhZG9ubHkuXG5tb2RfbnMubmFtZWQgPSAzIC8vIEVSUk9SOiBUaGUgbWVtYmVycyBvZiAnbW9kX25zJyBhcmUgcmVhZG9ubHkuXG5tb2RfbnMgPSB7fSAgICAgIC8vIEVSUk9SOiAnbW9kX25zJyBpcyByZWFkb25seS5cbi8vIENhbid0IGV4dGVuZCAnbW9kX25zJ1xuT2JqZWN0LmFzc2lnbihtb2RfbnMsIHsgZm9vOiBcImZvb1wiIH0pIC8vIEVSUk9SOiBUaGUgbWVtYmVycyBvZiAnbW9kX25zJyBhcmUgcmVhZG9ubHkuIn0=)

```
/*eslint no-import-assign: "error"*/

import mod, { named } from "./mod.mjs"
import * as mod_ns from "./mod.mjs"

mod = 1          // ERROR: 'mod' is readonly.
named = 2        // ERROR: 'named' is readonly.
mod_ns.named = 3 // ERROR: The members of 'mod_ns' are readonly.
mod_ns = {}      // ERROR: 'mod_ns' is readonly.
// Can't extend 'mod_ns'
Object.assign(mod_ns, { foo: "foo" }) // ERROR: The members of 'mod_ns' are readonly.
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
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8taW1wb3J0LWFzc2lnbjogXCJlcnJvclwiKi9cblxuaW1wb3J0IG1vZCwgeyBuYW1lZCB9IGZyb20gXCIuL21vZC5tanNcIlxuaW1wb3J0ICogYXMgbW9kX25zIGZyb20gXCIuL21vZC5tanNcIlxuXG5tb2QucHJvcCA9IDFcbm5hbWVkLnByb3AgPSAyXG5tb2RfbnMubmFtZWQucHJvcCA9IDNcblxuLy8gS25vd24gTGltaXRhdGlvblxuZnVuY3Rpb24gdGVzdChvYmopIHtcbiAgICBvYmoubmFtZWQgPSA0IC8vIE5vdCBlcnJvcmVkIGJlY2F1c2UgJ29iaicgaXMgbm90IG5hbWVzcGFjZSBvYmplY3RzLlxufVxudGVzdChtb2RfbnMpIC8vIE5vdCBlcnJvcmVkIGJlY2F1c2UgaXQgZG9lc24ndCBrbm93IHRoYXQgJ3Rlc3QnIHVwZGF0ZXMgdGhlIG1lbWJlciBvZiB0aGUgYXJndW1lbnQuIn0=)

```
/*eslint no-import-assign: "error"*/

import mod, { named } from "./mod.mjs"
import * as mod_ns from "./mod.mjs"

mod.prop = 1
named.prop = 2
mod_ns.named.prop = 3

// Known Limitation
function test(obj) {
    obj.named = 4 // Not errored because 'obj' is not namespace objects.
}
test(mod_ns) // Not errored because it doesn't know that 'test' updates the member of the argument.
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
```

## When Not To Use It

If you don’t want to be notified about modifying imported bindings, you can disable this rule.

## Handled by TypeScript

 It is safe to disable this rule when using TypeScript because TypeScript's compiler enforces this check. 

Note that the compiler will not catch the `Object.assign()` case. Thus, if you use `Object.assign()` in your codebase, this rule will still provide some value.

## Version

This rule was introduced in ESLint v6.4.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-import-assign.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-import-assign.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-import-assign.md
                    
                
                )
