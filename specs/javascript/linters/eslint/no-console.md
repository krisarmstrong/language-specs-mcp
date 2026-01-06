# no-console

Disallow the use of `console`

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)
3. [When Not To Use It](#when-not-to-use-it)
4. [Related Rules](#related-rules)
5. [Version](#version)
6. [Resources](#resources)

In JavaScript that is designed to be executed in the browser, it’s considered a best practice to avoid using methods on `console`. Such messages are considered to be for debugging purposes and therefore not suitable to ship to the client. In general, calls using `console` should be stripped before being pushed to production.

```
console.log("Made it here.");
console.error("That shouldn't have happened.");
1
2
```

Copy code to clipboard

## Rule Details

This rule disallows calls or assignments to methods of the `console` object.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWNvbnNvbGU6IFwiZXJyb3JcIiAqL1xuXG5jb25zb2xlLmxvZyhcIkxvZyBhIGRlYnVnIGxldmVsIG1lc3NhZ2UuXCIpO1xuY29uc29sZS53YXJuKFwiTG9nIGEgd2FybiBsZXZlbCBtZXNzYWdlLlwiKTtcbmNvbnNvbGUuZXJyb3IoXCJMb2cgYW4gZXJyb3IgbGV2ZWwgbWVzc2FnZS5cIik7XG5jb25zb2xlLmxvZyA9IGZvbygpOyJ9)

```
/* eslint no-console: "error" */

console.log("Log a debug level message.");
console.warn("Log a warn level message.");
console.error("Log an error level message.");
console.log = foo();
1
2
3
4
5
6
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWNvbnNvbGU6IFwiZXJyb3JcIiAqL1xuXG4vLyBjdXN0b20gY29uc29sZVxuQ29uc29sZS5sb2coXCJIZWxsbyB3b3JsZCFcIik7In0=)

```
/* eslint no-console: "error" */

// custom console
Console.log("Hello world!");
1
2
3
4
```

## Options

This rule has an object option for exceptions:

- `"allow"` has an array of strings which are allowed methods of the `console` object

Examples of additional correct code for this rule with a sample `{ "allow": ["warn", "error"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLWNvbnNvbGU6IFtcImVycm9yXCIsIHsgYWxsb3c6IFtcIndhcm5cIiwgXCJlcnJvclwiXSB9XSAqL1xuXG5jb25zb2xlLndhcm4oXCJMb2cgYSB3YXJuIGxldmVsIG1lc3NhZ2UuXCIpO1xuY29uc29sZS5lcnJvcihcIkxvZyBhbiBlcnJvciBsZXZlbCBtZXNzYWdlLlwiKTsifQ==)

```
/* eslint no-console: ["error", { allow: ["warn", "error"] }] */

console.warn("Log a warn level message.");
console.error("Log an error level message.");
1
2
3
4
```

## When Not To Use It

If you’re using Node.js, however, `console` is used to output information to the user and so is not strictly used for debugging purposes. If you are developing for Node.js then you most likely do not want this rule enabled.

Another case where you might not use this rule is if you want to enforce `console` calls and not `console` overwrites. For example:

```
/* eslint no-console: ["error", { allow: ["warn"] }] */
console.error = function (message) {
  throw new Error(message);
};
1
2
3
4
```

Copy code to clipboard

With the `no-console` rule in the above example, ESLint will report an error. For the above example, you can disable the rule:

```
// eslint-disable-next-line no-console
console.error = function (message) {
  throw new Error(message);
};

// or

console.error = function (message) {  // eslint-disable-line no-console
  throw new Error(message);
};
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
```

Copy code to clipboard

However, you might not want to manually add `eslint-disable-next-line` or `eslint-disable-line`. You can achieve the effect of only receiving errors for console calls with the `no-restricted-syntax` rule:

```
{
    "rules": {
        "no-console": "off",
        "no-restricted-syntax": [
            "error",
            {
                "selector": "CallExpression[callee.object.name='console'][callee.property.name!=/^(log|warn|error|info|trace)$/]",
                "message": "Unexpected property on console object was called"
            }
        ]
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
```

Copy code to clipboard

## Related Rules

- [no-alert](/docs/latest/rules/no-alert)
- [no-debugger](/docs/latest/rules/no-debugger)

## Version

This rule was introduced in ESLint v0.0.2.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-console.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-console.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-console.md
                    
                
                )
