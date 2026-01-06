# no-restricted-properties

Disallow certain properties on certain objects

## Table of Contents

1. [Rule Details](#rule-details)

  1. [Options](#options)

2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Certain properties on objects may be disallowed in a codebase. This is useful for deprecating an API or restricting usage of a module’s methods. For example, you may want to disallow using `describe.only` when using Mocha or telling people to use `Object.assign` instead of `_.extend`.

## Rule Details

This rule looks for accessing a given property key on a given object name, either when reading the property’s value or invoking it as a function. You may specify an optional message to indicate an alternative API or a reason for the restriction. This rule applies to both properties accessed by dot notation and destructuring.

### Options

This rule takes a list of objects, where the object name and property names are specified:

```
{
    "rules": {
        "no-restricted-properties": [2, {
            "object": "disallowedObjectName",
            "property": "disallowedPropertyName"
        }]
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
```

Copy code to clipboard

Multiple object/property values can be disallowed, and you can specify an optional message:

```
{
    "rules": {
        "no-restricted-properties": [2, {
            "object": "disallowedObjectName",
            "property": "disallowedPropertyName"
        }, {
            "object": "disallowedObjectName",
            "property": "anotherDisallowedPropertyName",
            "message": "Please use allowedObjectName.allowedPropertyName."
        }]
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

If the object name is omitted, the property is disallowed for all objects:

```
{
    "rules": {
        "no-restricted-properties": [2, {
            "property": "__defineGetter__",
            "message": "Please use Object.defineProperty instead."
        }]
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
```

Copy code to clipboard

If the property name is omitted, accessing any property of the given object is disallowed:

```
{
    "rules": {
        "no-restricted-properties": [2, {
            "object": "require",
            "message": "Please call require() directly."
        }]
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
```

Copy code to clipboard

If you want to restrict a property globally but allow specific objects to use it, you can use the `allowObjects` option:

```
{
    "rules": {
        "no-restricted-properties": [2, {
            "property": "push",
            "allowObjects": ["router"],
            "message": "Prefer [...array, newValue] because it does not mutate the array in place."
        }]
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
```

Copy code to clipboard

If you want to restrict all properties on an object except for specific ones, you can use the `allowProperties` option:

```
{
    "rules": {
        "no-restricted-properties": [2, {
            "object": "config",
            "allowProperties": ["settings", "version"],
            "message": "Accessing other properties is restricted."
        }]
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
```

Copy code to clipboard

Note that the `allowObjects` option cannot be used together with the `object` option since they are mutually exclusive. Similarly, the `allowProperties` option cannot be used together with the `property` option since they are also mutually exclusive.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcIm9iamVjdFwiOiBcImRpc2FsbG93ZWRPYmplY3ROYW1lXCIsXG4gICAgXCJwcm9wZXJ0eVwiOiBcImRpc2FsbG93ZWRQcm9wZXJ0eU5hbWVcIlxufV0gKi9cblxuY29uc3QgZXhhbXBsZSA9IGRpc2FsbG93ZWRPYmplY3ROYW1lLmRpc2FsbG93ZWRQcm9wZXJ0eU5hbWU7IC8qZXJyb3IgRGlzYWxsb3dlZCBvYmplY3QgcHJvcGVydHk6IGRpc2FsbG93ZWRPYmplY3ROYW1lLmRpc2FsbG93ZWRQcm9wZXJ0eU5hbWUuKi9cblxuZGlzYWxsb3dlZE9iamVjdE5hbWUuZGlzYWxsb3dlZFByb3BlcnR5TmFtZSgpOyAvKmVycm9yIERpc2FsbG93ZWQgb2JqZWN0IHByb3BlcnR5OiBkaXNhbGxvd2VkT2JqZWN0TmFtZS5kaXNhbGxvd2VkUHJvcGVydHlOYW1lLiovIn0=)

```
/* eslint no-restricted-properties: [2, {
    "object": "disallowedObjectName",
    "property": "disallowedPropertyName"
}] */

const example = disallowedObjectName.disallowedPropertyName; /*error Disallowed object property: disallowedObjectName.disallowedPropertyName.*/

disallowedObjectName.disallowedPropertyName(); /*error Disallowed object property: disallowedObjectName.disallowedPropertyName.*/
1
2
3
4
5
6
7
8
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcInByb3BlcnR5XCI6IFwiX19kZWZpbmVHZXR0ZXJfX1wiXG59XSAqL1xuXG5mb28uX19kZWZpbmVHZXR0ZXJfXyhiYXIsIGJheik7XG5cbmNvbnN0IHsgX19kZWZpbmVHZXR0ZXJfXyB9ID0gcXV4KCk7XG5cbih7IF9fZGVmaW5lR2V0dGVyX18gfSkgPT4ge307In0=)

```
/* eslint no-restricted-properties: [2, {
    "property": "__defineGetter__"
}] */

foo.__defineGetter__(bar, baz);

const { __defineGetter__ } = qux();

({ __defineGetter__ }) => {};
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

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcIm9iamVjdFwiOiBcInJlcXVpcmVcIlxufV0gKi9cblxucmVxdWlyZS5yZXNvbHZlKCdmb28nKTsifQ==)

```
/* eslint no-restricted-properties: [2, {
    "object": "require"
}] */

require.resolve('foo');
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcInByb3BlcnR5XCI6IFwicHVzaFwiLFxuICAgIFwiYWxsb3dPYmplY3RzXCI6IFtcInJvdXRlclwiXSxcbn1dICovXG5cbm15QXJyYXkucHVzaCg1KTsifQ==)

```
/* eslint no-restricted-properties: [2, {
    "property": "push",
    "allowObjects": ["router"],
}] */

myArray.push(5);
1
2
3
4
5
6
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcIm9iamVjdFwiOiBcImNvbmZpZ1wiLFxuICAgIFwiYWxsb3dQcm9wZXJ0aWVzXCI6IFtcInNldHRpbmdzXCIsIFwidmVyc2lvblwiXVxufV0gKi9cblxuY29uZmlnLmFwaUtleSA9IFwiMTIzNDVcIjtcbmNvbmZpZy50aW1lb3V0ID0gNTAwMDsifQ==)

```
/* eslint no-restricted-properties: [2, {
    "object": "config",
    "allowProperties": ["settings", "version"]
}] */

config.apiKey = "12345";
config.timeout = 5000;
1
2
3
4
5
6
7
```

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcIm9iamVjdFwiOiBcImRpc2FsbG93ZWRPYmplY3ROYW1lXCIsXG4gICAgXCJwcm9wZXJ0eVwiOiBcImRpc2FsbG93ZWRQcm9wZXJ0eU5hbWVcIlxufV0gKi9cblxuY29uc3QgZXhhbXBsZSA9IGRpc2FsbG93ZWRPYmplY3ROYW1lLnNvbWVQcm9wZXJ0eU5hbWU7XG5cbmFsbG93ZWRPYmplY3ROYW1lLmRpc2FsbG93ZWRQcm9wZXJ0eU5hbWUoKTsifQ==)

```
/* eslint no-restricted-properties: [2, {
    "object": "disallowedObjectName",
    "property": "disallowedPropertyName"
}] */

const example = disallowedObjectName.somePropertyName;

allowedObjectName.disallowedPropertyName();
1
2
3
4
5
6
7
8
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcIm9iamVjdFwiOiBcInJlcXVpcmVcIlxufV0gKi9cblxucmVxdWlyZSgnZm9vJyk7In0=)

```
/* eslint no-restricted-properties: [2, {
    "object": "require"
}] */

require('foo');
1
2
3
4
5
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcInByb3BlcnR5XCI6IFwicHVzaFwiLFxuICAgIFwiYWxsb3dPYmplY3RzXCI6IFtcInJvdXRlclwiLCBcImhpc3RvcnlcIl0sXG59XSAqL1xuXG5yb3V0ZXIucHVzaCgnL2hvbWUnKTtcbmhpc3RvcnkucHVzaCgnL2Fib3V0Jyk7In0=)

```
/* eslint no-restricted-properties: [2, {
    "property": "push",
    "allowObjects": ["router", "history"],
}] */

router.push('/home');
history.push('/about');
1
2
3
4
5
6
7
```

[Open in Playground](/play#eyJ0ZXh0IjoiLyogZXNsaW50IG5vLXJlc3RyaWN0ZWQtcHJvcGVydGllczogWzIsIHtcbiAgICBcIm9iamVjdFwiOiBcImNvbmZpZ1wiLFxuICAgIFwiYWxsb3dQcm9wZXJ0aWVzXCI6IFtcInNldHRpbmdzXCIsIFwidmVyc2lvblwiXVxufV0gKi9cblxuY29uZmlnLnNldHRpbmdzID0geyB0aGVtZTogXCJkYXJrXCIgfTtcbmNvbmZpZy52ZXJzaW9uID0gXCIxLjAuMFwiOyAgIn0=)

```
/* eslint no-restricted-properties: [2, {
    "object": "config",
    "allowProperties": ["settings", "version"]
}] */

config.settings = { theme: "dark" };
config.version = "1.0.0";  
1
2
3
4
5
6
7
```

## When Not To Use It

If you don’t have any object/property combinations to restrict, you should not use this rule.

## Related Rules

- [no-restricted-globals](/docs/latest/rules/no-restricted-globals)
- [no-restricted-syntax](/docs/latest/rules/no-restricted-syntax)

## Version

This rule was introduced in ESLint v3.5.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-restricted-properties.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-restricted-properties.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-restricted-properties.md
                    
                
                )
