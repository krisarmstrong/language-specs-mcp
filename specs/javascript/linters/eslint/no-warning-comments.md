# no-warning-comments

Disallow specified warning terms in comments

❄️ Frozen

 This rule is currently [frozen](../contribute/core-rules#frozen-rules) and is not accepting feature requests. 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [terms and location](#terms-and-location)
  2. [Decoration Characters](#decoration-characters)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

Developers often add comments to code which is not complete or needs review. Most likely you want to fix or review the code, and then remove the comment, before you consider the code to be production ready.

```
// TODO: do something
// FIXME: this is not a good idea
1
2
```

Copy code to clipboard

## Rule Details

This rule reports comments that include any of the predefined terms specified in its configuration.

## Options

This rule has an options object literal:

- `"terms"`: optional array of terms to match. Defaults to `["todo", "fixme", "xxx"]`. Terms are matched case-insensitively and as whole words: `fix` would match `FIX` but not `fixing`. Terms can consist of multiple words: `really bad idea`.
- `"location"`: optional string that configures where in your comments to check for matches. Defaults to `"start"`. The start is from the first non-decorative character, ignoring whitespace, new lines and characters specified in `decoration`. The other value is match `anywhere` in comments.
- `"decoration"`: optional array of characters that are ignored at the start of a comment, when location is `"start"`. Defaults to `[]`. Any sequence of whitespace or the characters from this property are ignored. This option is ignored when location is `"anywhere"`.

Example of incorrect code for the default `{ "terms": ["todo", "fixme", "xxx"], "location": "start" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8td2FybmluZy1jb21tZW50czogXCJlcnJvclwiKi9cblxuLypcbkZJWE1FXG4qL1xuZnVuY3Rpb24gY2FsbGJhY2soZXJyLCByZXN1bHRzKSB7XG4gIGlmIChlcnIpIHtcbiAgICBjb25zb2xlLmVycm9yKGVycik7XG4gICAgcmV0dXJuO1xuICB9XG4gIC8vIFRPRE9cbn0ifQ==)

```
/*eslint no-warning-comments: "error"*/

/*
FIXME
*/
function callback(err, results) {
  if (err) {
    console.error(err);
    return;
  }
  // TODO
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

Example of correct code for the default `{ "terms": ["todo", "fixme", "xxx"], "location": "start" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8td2FybmluZy1jb21tZW50czogXCJlcnJvclwiKi9cblxuZnVuY3Rpb24gY2FsbGJhY2soZXJyLCByZXN1bHRzKSB7XG4gIGlmIChlcnIpIHtcbiAgICBjb25zb2xlLmVycm9yKGVycik7XG4gICAgcmV0dXJuO1xuICB9XG4gIC8vIE5PVCBSRUFEWSBGT1IgUFJJTUUgVElNRVxuICAvLyBidXQgdG9vIGJhZCwgaXQgaXMgbm90IGEgcHJlZGVmaW5lZCB3YXJuaW5nIHRlcm1cbn0ifQ==)

```
/*eslint no-warning-comments: "error"*/

function callback(err, results) {
  if (err) {
    console.error(err);
    return;
  }
  // NOT READY FOR PRIME TIME
  // but too bad, it is not a predefined warning term
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
```

### terms and location

Examples of incorrect code for the `{ "terms": ["todo", "fixme", "any other term"], "location": "anywhere" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8td2FybmluZy1jb21tZW50czogW1wiZXJyb3JcIiwgeyBcInRlcm1zXCI6IFtcInRvZG9cIiwgXCJmaXhtZVwiLCBcImFueSBvdGhlciB0ZXJtXCJdLCBcImxvY2F0aW9uXCI6IFwiYW55d2hlcmVcIiB9XSovXG5cbi8vIFRPRE86IHRoaXNcbi8vIHRvZG86IHRoaXMgdG9vXG4vLyBFdmVuIHRoaXM6IFRPRE9cbi8qXG4gKiBUaGUgc2FtZSBnb2VzIGZvciB0aGlzIFRPRE8gY29tbWVudFxuICogT3IgYSBmaXhtZVxuICogYXMgd2VsbCBhcyBhbnkgb3RoZXIgdGVybVxuICovIn0=)

```
/*eslint no-warning-comments: ["error", { "terms": ["todo", "fixme", "any other term"], "location": "anywhere" }]*/

// TODO: this
// todo: this too
// Even this: TODO
/*
 * The same goes for this TODO comment
 * Or a fixme
 * as well as any other term
 */
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

Examples of correct code for the `{ "terms": ["todo", "fixme", "any other term"], "location": "anywhere" }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8td2FybmluZy1jb21tZW50czogW1wiZXJyb3JcIiwgeyBcInRlcm1zXCI6IFtcInRvZG9cIiwgXCJmaXhtZVwiLCBcImFueSBvdGhlciB0ZXJtXCJdLCBcImxvY2F0aW9uXCI6IFwiYW55d2hlcmVcIiB9XSovXG5cbi8vIFRoaXMgaXMgdG8gZG9cbi8vIGV2ZW4gbm90IGFueSBvdGhlciAgICB0ZXJtXG4vLyBhbnkgb3RoZXIgdGVybWluYWxcbi8qXG4gKiBUaGUgc2FtZSBnb2VzIGZvciBibG9jayBjb21tZW50c1xuICogd2l0aCBhbnkgb3RoZXIgaW50ZXJlc3RpbmcgdGVybVxuICogb3IgZml4IG1lIHRoaXNcbiAqLyJ9)

```
/*eslint no-warning-comments: ["error", { "terms": ["todo", "fixme", "any other term"], "location": "anywhere" }]*/

// This is to do
// even not any other    term
// any other terminal
/*
 * The same goes for block comments
 * with any other interesting term
 * or fix me this
 */
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

### Decoration Characters

Examples of incorrect code for the `{ "decoration": ["*"] }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8td2FybmluZy1jb21tZW50czogW1wiZXJyb3JcIiwgeyBcImRlY29yYXRpb25cIjogW1wiKlwiXSB9XSovXG5cbi8vKioqKiogdG9kbyBkZWNvcmF0aXZlIGFzdGVyaXNrcyBhcmUgaWdub3JlZCAqKioqKi8vXG4vKipcbiAqIFRPRE8gbmV3IGxpbmVzIGFuZCBhc3Rlcmlza3MgYXJlIGFsc28gaWdub3JlZCBpbiBibG9jayBjb21tZW50cy5cbiAqLyJ9)

```
/*eslint no-warning-comments: ["error", { "decoration": ["*"] }]*/

//***** todo decorative asterisks are ignored *****//
/**
 * TODO new lines and asterisks are also ignored in block comments.
 */
1
2
3
4
5
6
```

Examples of incorrect code for the `{ "decoration": ["/", "*"] }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8td2FybmluZy1jb21tZW50czogW1wiZXJyb3JcIiwgeyBcImRlY29yYXRpb25cIjogW1wiL1wiLCBcIipcIl0gfV0qL1xuXG4vLy8vLy8gVE9ETyBkZWNvcmF0aXZlIHNsYXNoZXMgYW5kIHdoaXRlc3BhY2UgYXJlIGlnbm9yZWQgLy8vLy8vXG4vLyoqKioqIHRvZG8gZGVjb3JhdGl2ZSBhc3Rlcmlza3MgYXJlIGFsc28gaWdub3JlZCAqKioqKi8vXG4vKipcbiAqIFRPRE8gbmV3IGxpbmVzIGFyZSBhbHNvIGlnbm9yZWQgaW4gYmxvY2sgY29tbWVudHMuXG4gKi8ifQ==)

```
/*eslint no-warning-comments: ["error", { "decoration": ["/", "*"] }]*/

////// TODO decorative slashes and whitespace are ignored //////
//***** todo decorative asterisks are also ignored *****//
/**
 * TODO new lines are also ignored in block comments.
 */
1
2
3
4
5
6
7
```

Examples of correct code for the `{ "decoration": ["/", "*"] }` options:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8td2FybmluZy1jb21tZW50czogW1wiZXJyb3JcIiwgeyBcImRlY29yYXRpb25cIjogW1wiL1wiLCBcIipcIl0gfV0qL1xuXG4vLyFUT0RPIHByZWNlZGVkIGJ5IG5vbi1kZWNvcmF0aW9uIGNoYXJhY3RlclxuLyoqXG4gKiFUT0RPIHByZWNlZGVkIGJ5IG5vbi1kZWNvcmF0aW9uIGNoYXJhY3RlciBpbiBhIGJsb2NrIGNvbW1lbnRcbiAqLyJ9)

```
/*eslint no-warning-comments: ["error", { "decoration": ["/", "*"] }]*/

//!TODO preceded by non-decoration character
/**
 *!TODO preceded by non-decoration character in a block comment
 */
1
2
3
4
5
6
```

## When Not To Use It

- If you have a large code base that was not developed with a policy to not use such warning terms, you might get hundreds of warnings / errors which might be counter-productive if you can’t fix all of them (e.g. if you don’t get the time to do it) as you might overlook other warnings / errors or get used to many of them and don’t pay attention on it anymore.
- Same reason as the point above: You shouldn’t configure terms that are used very often (e.g. central parts of the native language used in your comments).

## Version

This rule was introduced in ESLint v0.4.4.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-warning-comments.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-warning-comments.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-warning-comments.md
                    
                
                )
