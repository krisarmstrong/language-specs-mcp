# unicode-bom

Require or disallow Unicode byte order mark (BOM)

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [Options](#options)

  1. [always](#always)
  2. [never](#never)

3. [When Not To Use It](#when-not-to-use-it)
4. [Version](#version)
5. [Resources](#resources)

The Unicode Byte Order Mark (BOM) is used to specify whether code units are big endian or little endian. That is, whether the most significant or least significant bytes come first. UTF-8 does not require a BOM because byte ordering does not matter when characters are a single byte. Since UTF-8 is the dominant encoding of the web, we make `"never"` the default option.

## Rule Details

If the `"always"` option is used, this rule requires that files always begin with the Unicode BOM character U+FEFF. If `"never"` is used, files must never begin with U+FEFF.

## Options

This rule has a string option:

- `"always"` files must begin with the Unicode BOM
- `"never"` (default) files must not begin with the Unicode BOM

### always

Example of correct code for this rule with the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0Ijoi77u/Ly8gVStGRUZGIGF0IHRoZSBiZWdpbm5pbmdcblxuLyplc2xpbnQgdW5pY29kZS1ib206IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdKi9cblxubGV0IGFiYzsifQ==)

```
﻿// U+FEFF at the beginning

/*eslint unicode-bom: ["error", "always"]*/

let abc;
1
2
3
4
5
```

Example of incorrect code for this rule with the `"always"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdW5pY29kZS1ib206IFtcImVycm9yXCIsIFwiYWx3YXlzXCJdKi9cblxubGV0IGFiYzsifQ==)

```
/*eslint unicode-bom: ["error", "always"]*/

let abc;
1
2
3
```

### never

Example of correct code for this rule with the default `"never"` option:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgdW5pY29kZS1ib206IFtcImVycm9yXCIsIFwibmV2ZXJcIl0qL1xuXG5sZXQgYWJjOyJ9)

```
/*eslint unicode-bom: ["error", "never"]*/

let abc;
1
2
3
```

Example of incorrect code for this rule with the `"never"` option:

[Open in Playground](/play#eyJ0ZXh0Ijoi77u/Ly8gVStGRUZGIGF0IHRoZSBiZWdpbm5pbmdcblxuLyplc2xpbnQgdW5pY29kZS1ib206IFtcImVycm9yXCIsIFwibmV2ZXJcIl0qL1xuXG5sZXQgYWJjOyJ9)

```
﻿// U+FEFF at the beginning

/*eslint unicode-bom: ["error", "never"]*/

let abc;
1
2
3
4
5
```

## When Not To Use It

If you use some UTF-16 or UTF-32 files and you want to allow a file to optionally begin with a Unicode BOM, you should turn this rule off.

## Version

This rule was introduced in ESLint v2.11.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/unicode-bom.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/unicode-bom.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/unicode-bom.md
                    
                
                )
