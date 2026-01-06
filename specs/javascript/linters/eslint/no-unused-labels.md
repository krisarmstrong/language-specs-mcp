# no-unused-labels

Disallow unused labels

✅ Recommended

 Using the `recommended` config from `@eslint/js` in a [configuration file](../use/configure/configuration-files#using-predefined-configurations) enables this rule 

🔧 Fixable

 Some problems reported by this rule are automatically fixable by the `--fix`[command line](../use/command-line-interface#--fix) option 

## Table of Contents

1. [Rule Details](#rule-details)
2. [When Not To Use It](#when-not-to-use-it)
3. [Related Rules](#related-rules)
4. [Version](#version)
5. [Resources](#resources)

Labels that are declared and not used anywhere in the code are most likely an error due to incomplete refactoring.

```
OUTER_LOOP:
for (const student of students) {
    if (checkScores(student.scores)) {
        continue;
    }
    doSomething(student);
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

In this case, probably removing `OUTER_LOOP:` had been forgotten. Such labels take up space in the code and can lead to confusion by readers.

## Rule Details

This rule is aimed at eliminating unused labels.

Problems reported by this rule can be fixed automatically, except when there are any comments between the label and the following statement, or when removing a label would cause the following statement to become a directive such as `"use strict"`.

Examples of incorrect code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWxhYmVsczogXCJlcnJvclwiKi9cblxuQTogdmFyIGZvbyA9IDA7XG5cbkI6IHtcbiAgICBmb28oKTtcbn1cblxuQzpcbmZvciAobGV0IGkgPSAwOyBpIDwgMTA7ICsraSkge1xuICAgIGZvbygpO1xufSJ9)

```
/*eslint no-unused-labels: "error"*/

A: var foo = 0;

B: {
    foo();
}

C:
for (let i = 0; i < 10; ++i) {
    foo();
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

Examples of correct code for this rule:

[Open in Playground](/play#eyJ0ZXh0IjoiLyplc2xpbnQgbm8tdW51c2VkLWxhYmVsczogXCJlcnJvclwiKi9cblxuQToge1xuICAgIGlmIChmb28oKSkge1xuICAgICAgICBicmVhayBBO1xuICAgIH1cbiAgICBiYXIoKTtcbn1cblxuQjpcbmZvciAobGV0IGkgPSAwOyBpIDwgMTA7ICsraSkge1xuICAgIGlmIChmb28oKSkge1xuICAgICAgICBicmVhayBCO1xuICAgIH1cbiAgICBiYXIoKTtcbn0ifQ==)

```
/*eslint no-unused-labels: "error"*/

A: {
    if (foo()) {
        break A;
    }
    bar();
}

B:
for (let i = 0; i < 10; ++i) {
    if (foo()) {
        break B;
    }
    bar();
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
```

## When Not To Use It

If you don’t want to be notified about unused labels, then it’s safe to disable this rule.

## Related Rules

- [no-extra-label](/docs/latest/rules/no-extra-label)
- [no-labels](/docs/latest/rules/no-labels)
- [no-label-var](/docs/latest/rules/no-label-var)

## Version

This rule was introduced in ESLint v2.0.0-rc.0.

## Resources

- [Rule source](https://github.com/eslint/eslint/blob/main/lib/rules/no-unused-labels.js)
- [Tests source](https://github.com/eslint/eslint/blob/main/tests/lib/rules/no-unused-labels.js)

[Edit this page](
                
                    
                        https://github.com/eslint/eslint/edit/latest/docs/./src/rules/no-unused-labels.md
                    
                
                )
