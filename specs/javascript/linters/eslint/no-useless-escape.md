# no-useless-escape

Disallow unnecessary escape characters

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

💡 hasSuggestions

 Some problems reported by this rule are manually fixable by editor [suggestions](../use/core-concepts#rule-suggestions)

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [allowRegexCharacters](#allowregexcharacters)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

Escaping non-special characters in strings, template literals, and regular expressions doesn’t have any effect, as demonstrated in the following example:

```
let foo = "hol\a"; // > foo = "hola"
let bar = `${foo}\!`; // > bar = "hola!"
let baz = /\:/ // same functionality with /:/
1
2
3
```

Copy code to clipboard

## Rule Details

This rule flags escapes that can be safely removed without changing behavior.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1lc2NhcGU6IFwiZXJyb3JcIiovXG5cblwiXFwnXCI7XG4nXFxcIic7XG5cIlxcI1wiO1xuXCJcXGVcIjtcbmBcXFwiYDtcbmBcXFwiJHtmb299XFxcImA7XG5gXFwje2Zvb31gO1xuL1xcIS87XG4vXFxALztcbi9bXFxbXS87XG4vW2EtelxcLV0vOyJ9)

```
/*eslint no-useless-escape: "error"*/

"\'";
'\"';
"\#";
"\e";
`\"`;
`\"${foo}\"`;
`\#{foo}`;
/\!/;
/\@/;
/[\[]/;
/[a-z\-]/;
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJvcHRpb25zIjp7Imxhbmd1YWdlT3B0aW9ucyI6eyJzb3VyY2VUeXBlIjoic2NyaXB0In19LCJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1lc2NhcGU6IFwiZXJyb3JcIiovXG5cblwiXFxcIlwiO1xuJ1xcJyc7XG5cIlxceDEyXCI7XG5cIlxcdTAwYTlcIjtcblwiXFwzNzFcIjtcblwieHNcXHUyMTExXCI7XG5gXFxgYDtcbmBcXCR7JHtmb299fWA7XG5gJFxceyR7Zm9vfX1gO1xuL1xcXFwvZztcbi9cXHQvZztcbi9cXHdcXCRcXCpcXF5cXC4vO1xuL1tbXS87XG4vW1xcXV0vO1xuL1thLXotXS87In0=)

```
/*eslint no-useless-escape: "error"*/

"\"";
'\'';
"\x12";
"\u00a9";
"\371";
"xs\u2111";
`\``;
`\${${foo}}`;
`$\{${foo}}`;
/\\/g;
/\t/g;
/\w\$\*\^\./;
/[[]/;
/[\]]/;
/[a-z-]/;
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
```

## Options

This rule has an object option:

- `allowRegexCharacters` - An array of characters that should be allowed to have unnecessary escapes in regular expressions. This is useful for characters like `-` where escaping can prevent accidental character ranges. For example, in `/[0\-]/`, the escape is technically unnecessary but helps prevent the pattern from becoming a range if another character is added later (e.g., `/[0\-9]/` vs `/[0-9]/`).

### allowRegexCharacters

Examples of incorrect code for the `{ "allowRegexCharacters": ["-"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1lc2NhcGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd1JlZ2V4Q2hhcmFjdGVyc1wiOiBbXCItXCJdIH1dKi9cblxuL1xcIS87XG4vXFxALztcbi9bYS16XFxeXS87In0=)

```
/*eslint no-useless-escape: ["error", { "allowRegexCharacters": ["-"] }]*/

/\!/;
/\@/;
/[a-z\^]/;
1
2
3
4
5
```

Examples of correct code for the `{ "allowRegexCharacters": ["-"] }` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdXNlbGVzcy1lc2NhcGU6IFtcImVycm9yXCIsIHsgXCJhbGxvd1JlZ2V4Q2hhcmFjdGVyc1wiOiBbXCItXCJdIH1dKi9cblxuL1swXFwtXS87XG4vW1xcLTldLztcbi9hXFwtYi87In0=)

```
/*eslint no-useless-escape: ["error", { "allowRegexCharacters": ["-"] }]*/

/[0\-]/;
/[\-9]/;
/a\-b/;
1
2
3
4
5
```

## When Not To Use It

If you don’t want to be notified about unnecessary escapes, you can safely disable this rule.

## Version

This rule was introduced in ESLint v2.5.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-useless-escape.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-useless-escape.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-useless-escape.md
                    
                
                )
