# no-eval

Disallow the use of `eval()`

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowIndirect](#allowindirect)

3. [Known Limitations](#known-limitations)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Further Reading](#further-reading)
7. [Resources](#resources)

JavaScript’s `eval()` function is potentially dangerous and is often misused. Using `eval()` on untrusted code can open a program up to several different injection attacks. The use of `eval()` in most contexts can be substituted for a better, alternative approach to a problem.

```
const obj = { x: "foo" },
    key = "x",
    value = eval("obj." + key);
1
2
3
```

Copy code to clipboard

## Rule Details

This rule is aimed at preventing potentially dangerous, unnecessary, and slow code by disallowing the use of the `eval()` function. As such, it will warn whenever the `eval()` function is used.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogXCJlcnJvclwiKi9cblxuY29uc3Qgb2JqID0geyB4OiBcImZvb1wiIH0sXG4gICAga2V5ID0gXCJ4XCIsXG4gICAgdmFsdWUgPSBldmFsKFwib2JqLlwiICsga2V5KTtcblxuKDAsIGV2YWwpKFwiY29uc3QgYSA9IDBcIik7XG5cbmNvbnN0IGZvbyA9IGV2YWw7XG5mb28oXCJjb25zdCBhID0gMFwiKTtcblxuLy8gVGhpcyBgdGhpc2AgaXMgdGhlIGdsb2JhbCBvYmplY3QuXG50aGlzLmV2YWwoXCJjb25zdCBhID0gMFwiKTsifQ==)

```
/*eslint no-eval: "error"*/

const obj = { x: "foo" },
    key = "x",
    value = eval("obj." + key);

(0, eval)("const a = 0");

const foo = eval;
foo("const a = 0");

// This `this` is the global object.
this.eval("const a = 0");
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
```

Example of additional incorrect code for this rule with `window` global variable:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogXCJlcnJvclwiKi9cbi8qZ2xvYmFsIHdpbmRvdyovXG5cbndpbmRvdy5ldmFsKFwiY29uc3QgYSA9IDBcIik7In0=)

```
/*eslint no-eval: "error"*/
/*global window*/

window.eval("const a = 0");
1
2
3
4
```

Example of additional incorrect code for this rule with `global` global variable:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogXCJlcnJvclwiKi9cbi8qZ2xvYmFsIGdsb2JhbCovXG5cbmdsb2JhbC5ldmFsKFwiY29uc3QgYSA9IDBcIik7In0=)

```
/*eslint no-eval: "error"*/
/*global global*/

global.eval("const a = 0");
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogXCJlcnJvclwiKi9cblxuY29uc3Qgb2JqID0geyB4OiBcImZvb1wiIH0sXG4gICAga2V5ID0gXCJ4XCIsXG4gICAgdmFsdWUgPSBvYmpba2V5XTtcblxuY2xhc3MgQSB7XG4gICAgZm9vKCkge1xuICAgICAgICAvLyBUaGlzIGlzIGEgdXNlci1kZWZpbmVkIG1ldGhvZC5cbiAgICAgICAgdGhpcy5ldmFsKFwiY29uc3QgYSA9IDBcIik7XG4gICAgfVxuXG4gICAgZXZhbCgpIHtcbiAgICB9XG5cbiAgICBzdGF0aWMge1xuICAgICAgICAvLyBUaGlzIGlzIGEgdXNlci1kZWZpbmVkIHN0YXRpYyBtZXRob2QuXG4gICAgICAgIHRoaXMuZXZhbChcImNvbnN0IGEgPSAwXCIpO1xuICAgIH1cblxuICAgIHN0YXRpYyBldmFsKCkge1xuICAgIH1cbn0ifQ==)

```
/*eslint no-eval: "error"*/

const obj = { x: "foo" },
    key = "x",
    value = obj[key];

class A {
    foo() {
        // This is a user-defined method.
        this.eval("const a = 0");
    }

    eval() {
    }

    static {
        // This is a user-defined static method.
        this.eval("const a = 0");
    }

    static eval() {
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
```

## Options

### allowIndirect

This rule has an option to allow [“indirect eval”](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#direct_and_indirect_eval). Indirect calls to `eval` are less dangerous than direct calls to `eval` because they cannot dynamically change the scope. Because of this, they also will not negatively impact performance to the degree of direct `eval`.

```
{
    "no-eval": ["error", {"allowIndirect": true}] // default is false
}
1
2
3
```

Copy code to clipboard

Example of incorrect code for this rule with the `{"allowIndirect": true}` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogW1wiZXJyb3JcIiwge1wiYWxsb3dJbmRpcmVjdFwiOiB0cnVlfSBdKi9cblxuY29uc3Qgb2JqID0geyB4OiBcImZvb1wiIH0sXG4gICAga2V5ID0gXCJ4XCIsXG4gICAgdmFsdWUgPSBldmFsKFwib2JqLlwiICsga2V5KTsifQ==)

```
/*eslint no-eval: ["error", {"allowIndirect": true} ]*/

const obj = { x: "foo" },
    key = "x",
    value = eval("obj." + key);
1
2
3
4
5
```

Examples of correct code for this rule with the `{"allowIndirect": true}` option:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogW1wiZXJyb3JcIiwge1wiYWxsb3dJbmRpcmVjdFwiOiB0cnVlfSBdKi9cblxuKDAsIGV2YWwpKFwiY29uc3QgYSA9IDBcIik7XG5cbmNvbnN0IGZvbyA9IGV2YWw7XG5mb28oXCJjb25zdCBhID0gMFwiKTtcblxudGhpcy5ldmFsKFwiY29uc3QgYSA9IDBcIik7In0=)

```
/*eslint no-eval: ["error", {"allowIndirect": true} ]*/

(0, eval)("const a = 0");

const foo = eval;
foo("const a = 0");

this.eval("const a = 0");
1
2
3
4
5
6
7
8
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogW1wiZXJyb3JcIiwge1wiYWxsb3dJbmRpcmVjdFwiOiB0cnVlfSBdKi9cbi8qZ2xvYmFsIHdpbmRvdyovXG5cbndpbmRvdy5ldmFsKFwiY29uc3QgYSA9IDBcIik7In0=)

```
/*eslint no-eval: ["error", {"allowIndirect": true} ]*/
/*global window*/

window.eval("const a = 0");
1
2
3
4
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tZXZhbDogW1wiZXJyb3JcIiwge1wiYWxsb3dJbmRpcmVjdFwiOiB0cnVlfSBdKi9cbi8qZ2xvYmFsIGdsb2JhbCovXG5cbmdsb2JhbC5ldmFsKFwiY29uc3QgYSA9IDBcIik7In0=)

```
/*eslint no-eval: ["error", {"allowIndirect": true} ]*/
/*global global*/

global.eval("const a = 0");
1
2
3
4
```

## Known Limitations

- 

This rule is warning every `eval()` even if the `eval` is not global’s. This behavior is in order to detect calls of direct `eval`. Such as:

```
module.exports = function(eval) {
    // If the value of this `eval` is built-in `eval` function, this is a
    // call of direct `eval`.
    eval("const a = 0");
};
1
2
3
4
5
```

Copy code to clipboard
- 

This rule cannot catch renaming the global object. Such as:

```
const foo = window;
foo.eval("const a = 0");
1
2
```

Copy code to clipboard

## Related Rules

- [no-implied-eval](/docs/latest/rules/no-implied-eval)

## Version

This rule was introduced in ESLint v0.0.2.

## Further Reading

[Eval is evil, part one](https://ericlippert.com/2003/11/01/eval-is-evil-part-one/)
 ericlippert.com[How evil is eval?](https://javascriptweblog.wordpress.com/2010/04/19/how-evil-is-eval/)
 javascriptweblog.wordpress.com

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-eval.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-eval.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-eval.md
                    
                
                )
