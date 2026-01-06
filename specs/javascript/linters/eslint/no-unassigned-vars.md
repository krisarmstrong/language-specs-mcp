# no-unassigned-vars

Disallow `let` or `var` variables that are read but never assigned

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

This rule flags `let` or `var` declarations that are never assigned a value but are still read or used in the code. Since these variables will always be `undefined`, their usage is likely a programming mistake.

For example, if you check the value of a `status` variable, but it was never given a value, it will always be `undefined`:

```
let status;

// ...forgot to assign a value to status...

if (status === 'ready') {
  console.log('Ready!');
}
1
2
3
4
5
6
7
```

Copy code to clipboard

## Rule Details

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5hc3NpZ25lZC12YXJzOiBcImVycm9yXCIqL1xuXG5sZXQgc3RhdHVzO1xuaWYgKHN0YXR1cyA9PT0gJ3JlYWR5Jykge1xuICBjb25zb2xlLmxvZygnUmVhZHkhJyk7XG59XG5cbmxldCB1c2VyO1xuZ3JlZXQodXNlcik7XG5cbmZ1bmN0aW9uIHRlc3QoKSB7XG4gIGxldCBlcnJvcjtcbiAgcmV0dXJuIGVycm9yIHx8IFwiVW5rbm93biBlcnJvclwiO1xufVxuXG5sZXQgb3B0aW9ucztcbmNvbnN0IHsgZGVidWcgfSA9IG9wdGlvbnMgfHwge307XG5cbmxldCBmbGFnO1xud2hpbGUgKCFmbGFnKSB7XG4gIC8vIERvIHNvbWV0aGluZy4uLlxufVxuXG5sZXQgY29uZmlnO1xuZnVuY3Rpb24gaW5pdCgpIHtcbiAgcmV0dXJuIGNvbmZpZz8uZW5hYmxlZDtcbn0ifQ==)

```
/*eslint no-unassigned-vars: "error"*/

let status;
if (status === 'ready') {
  console.log('Ready!');
}

let user;
greet(user);

function test() {
  let error;
  return error || "Unknown error";
}

let options;
const { debug } = options || {};

let flag;
while (!flag) {
  // Do something...
}

let config;
function init() {
  return config?.enabled;
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
```

In TypeScript:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11bmFzc2lnbmVkLXZhcnM6IFwiZXJyb3JcIiovXG5cbmxldCB2YWx1ZTogbnVtYmVyIHwgdW5kZWZpbmVkO1xuY29uc29sZS5sb2codmFsdWUpOyJ9)

```
/*eslint no-unassigned-vars: "error"*/

let value: number | undefined;
console.log(value);
1
2
3
4
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW5hc3NpZ25lZC12YXJzOiBcImVycm9yXCIqL1xuXG5sZXQgbWVzc2FnZSA9IFwiaGVsbG9cIjtcbmNvbnNvbGUubG9nKG1lc3NhZ2UpO1xuXG5sZXQgdXNlcjtcbnVzZXIgPSBnZXRVc2VyKCk7XG5jb25zb2xlLmxvZyh1c2VyLm5hbWUpO1xuXG5sZXQgY291bnQ7XG5jb3VudCA9IDE7XG5jb3VudCsrO1xuXG4vLyBWYXJpYWJsZSBpcyB1bnVzZWQgKHNob3VsZCBiZSByZXBvcnRlZCBieSBgbm8tdW51c2VkLXZhcnNgIG9ubHkpXG5sZXQgdGVtcDtcblxubGV0IGVycm9yO1xuaWYgKHNvbWV0aGluZ1dlbnRXcm9uZykge1xuICBlcnJvciA9IFwiU29tZXRoaW5nIHdlbnQgd3JvbmdcIjtcbn1cbmNvbnNvbGUubG9nKGVycm9yKTtcblxubGV0IGl0ZW07XG5mb3IgKGl0ZW0gb2YgaXRlbXMpIHtcbiAgcHJvY2VzcyhpdGVtKTtcbn1cblxubGV0IGNvbmZpZztcbmZ1bmN0aW9uIHNldHVwKCkge1xuICBjb25maWcgPSB7IGRlYnVnOiB0cnVlIH07XG59XG5zZXR1cCgpO1xuY29uc29sZS5sb2coY29uZmlnKTtcblxubGV0IG9uZSA9IHVuZGVmaW5lZDtcbmlmIChvbmUgPT09IHR3bykge1xuICAvLyBOb29wXG59In0=)

```
/*eslint no-unassigned-vars: "error"*/

let message = "hello";
console.log(message);

let user;
user = getUser();
console.log(user.name);

let count;
count = 1;
count++;

// Variable is unused (should be reported by `no-unused-vars` only)
let temp;

let error;
if (somethingWentWrong) {
  error = "Something went wrong";
}
console.log(error);

let item;
for (item of items) {
  process(item);
}

let config;
function setup() {
  config = { debug: true };
}
setup();
console.log(config);

let one = undefined;
if (one === two) {
  // Noop
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
35
36
37
38
```

In TypeScript:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJwYXJzZXIiOiJAdHlwZXNjcmlwdC1lc2xpbnQvcGFyc2VyIiwicGFyc2VyT3B0aW9ucyI6eyJlY21hRmVhdHVyZXMiOnsianN4Ijp0cnVlfSwic291cmNlVHlwZSI6Im1vZHVsZSJ9fX0sInRleHQiOiIvKmVzbGludCBuby11bmFzc2lnbmVkLXZhcnM6IFwiZXJyb3JcIiovXG5cbmRlY2xhcmUgbGV0IHZhbHVlOiBudW1iZXIgfCB1bmRlZmluZWQ7XG5jb25zb2xlLmxvZyh2YWx1ZSk7XG5cbmRlY2xhcmUgbW9kdWxlIFwibXktbW9kdWxlXCIge1xuICBsZXQgdmFsdWU6IHN0cmluZztcbiAgZXhwb3J0ID0gdmFsdWU7XG59In0=)

```
/*eslint no-unassigned-vars: "error"*/

declare let value: number | undefined;
console.log(value);

declare module "my-module" {
  let value: string;
  export = value;
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
```

## When Not To Use It

You can disable this rule if your code intentionally uses variables that are declared and used, but are never assigned a value. This might be the case in:

- Legacy codebases where uninitialized variables are used as placeholders.
- Certain TypeScript use cases where variables are declared with a type and intentionally left unassigned (though using `declare` is preferred).

## Related Rules

- [init-declarations](/docs/latest/rules/init-declarations)
- [no-unused-vars](/docs/latest/rules/no-unused-vars)
- [prefer-const](/docs/latest/rules/prefer-const)

## Version

This rule was introduced in ESLint v9.27.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unassigned-vars.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unassigned-vars.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unassigned-vars.md
                    
                
                )
