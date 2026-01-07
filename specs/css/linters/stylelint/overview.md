Rules | Stylelint[Skip to main content](#__docusaurus_skipToContent_fallback)/[Home](/)[Rules](/user-guide/rules)[Demo](/demo)[GitHub](https://github.com/stylelint/stylelint)Search/

- [Home](/)
- [User guide](/user-guide/get-started)

  - [Getting started](/user-guide/get-started)
  - [Customizing](/user-guide/customize)
  - [Configuring](/user-guide/configure)
  - [Rules](/user-guide/rules)
  - [Rules](/user-guide/rules/alpha-value-notation)
  - [Ignoring code](/user-guide/ignore-code)
  - [Command Line Interface (CLI)](/user-guide/cli)
  - [Node.js API](/user-guide/node-api)
  - [PostCSS plugin](/user-guide/postcss-plugin)
  - [Options](/user-guide/options)
  - [Errors & warnings](/user-guide/errors)

- [Developer guide](/developer-guide/rules)
- [Migration guide](/migration-guide/to-16)
- [Maintainer guide](/maintainer-guide/issues)
- [About](/about/vision)
- [Awesome](/awesome-stylelint)

On this page

# Rules

There are over one hundred built-in rules to help you:

- [avoid errors](#avoid-errors)
- [enforce conventions](#enforce-conventions)

We turn on most of the rules in our [standard config](https://www.npmjs.com/package/stylelint-config-standard) (✅) and many can be autofixed (🔧).

## Avoid errors[​](#avoid-errors)

You can avoid errors with these `no` rules.

### Deprecated[​](#deprecated)

Disallow deprecated things with these `no-deprecated` rules.

[at-rule-no-deprecated](/user-guide/rules/at-rule-no-deprecated)
Disallow deprecated at-rules.✅🔧[declaration-property-value-keyword-no-deprecated](/user-guide/rules/declaration-property-value-keyword-no-deprecated)
Disallow deprecated keywords for properties within declarations.✅🔧[media-type-no-deprecated](/user-guide/rules/media-type-no-deprecated)
Disallow deprecated media types.✅[property-no-deprecated](/user-guide/rules/property-no-deprecated)
Disallow deprecated properties.✅🔧

### Descending[​](#descending)

Disallow descending things with these `no-descending` rules.

[no-descending-specificity](/user-guide/rules/no-descending-specificity)
Disallow selectors of lower specificity from coming after overriding selectors of higher specificity.✅

### Duplicate[​](#duplicate)

Disallow duplicates with these `no-duplicate` rules.

[declaration-block-no-duplicate-custom-properties](/user-guide/rules/declaration-block-no-duplicate-custom-properties)
Disallow duplicate custom properties within declaration blocks.✅[declaration-block-no-duplicate-properties](/user-guide/rules/declaration-block-no-duplicate-properties)
Disallow duplicate properties within declaration blocks.✅🔧[font-family-no-duplicate-names](/user-guide/rules/font-family-no-duplicate-names)
Disallow duplicate names within font families.✅[keyframe-block-no-duplicate-selectors](/user-guide/rules/keyframe-block-no-duplicate-selectors)
Disallow duplicate selectors within keyframe blocks.✅[no-duplicate-at-import-rules](/user-guide/rules/no-duplicate-at-import-rules)
Disallow duplicate `@import` rules.✅[no-duplicate-selectors](/user-guide/rules/no-duplicate-selectors)
Disallow duplicate selectors.✅

### Empty[​](#empty)

Disallow empty things with these `no-empty` rules.

[block-no-empty](/user-guide/rules/block-no-empty)
Disallow empty blocks.✅[comment-no-empty](/user-guide/rules/comment-no-empty)
Disallow empty comments.✅[no-empty-source](/user-guide/rules/no-empty-source)
Disallow empty sources.✅

### Invalid[​](#invalid)

Disallow invalid syntax with these (sometimes implicit) `no-invalid` rules.

[at-rule-prelude-no-invalid](/user-guide/rules/at-rule-prelude-no-invalid)
Disallow invalid preludes for at-rules.✅[color-no-invalid-hex](/user-guide/rules/color-no-invalid-hex)
Disallow invalid hex colors.[function-calc-no-unspaced-operator](/user-guide/rules/function-calc-no-unspaced-operator)
Disallow invalid unspaced operator within `calc` functions.✅🔧[keyframe-declaration-no-important](/user-guide/rules/keyframe-declaration-no-important)
Disallow invalid `!important` within keyframe declarations.✅[media-query-no-invalid](/user-guide/rules/media-query-no-invalid)
Disallow invalid media queries.✅[named-grid-areas-no-invalid](/user-guide/rules/named-grid-areas-no-invalid)
Disallow invalid named grid areas.✅[no-invalid-double-slash-comments](/user-guide/rules/no-invalid-double-slash-comments)
Disallow invalid double-slash comments.✅[no-invalid-position-at-import-rule](/user-guide/rules/no-invalid-position-at-import-rule)
Disallow invalid position `@import` rules.✅[no-invalid-position-declaration](/user-guide/rules/no-invalid-position-declaration)
Disallow invalid position declarations.✅[string-no-newline](/user-guide/rules/string-no-newline)
Disallow invalid newlines within strings.✅[syntax-string-no-invalid](/user-guide/rules/syntax-string-no-invalid)
Disallow invalid syntax strings.✅

### Irregular[​](#irregular)

Disallow irregular things with these `no-irregular` rules.

[no-irregular-whitespace](/user-guide/rules/no-irregular-whitespace)
Disallow irregular whitespace.✅

### Missing[​](#missing)

Disallow missing things with these `no-missing` rules.

[custom-property-no-missing-var-function](/user-guide/rules/custom-property-no-missing-var-function)
Disallow missing `var` function for custom properties.✅[font-family-no-missing-generic-family-keyword](/user-guide/rules/font-family-no-missing-generic-family-keyword)
Disallow a missing generic family keyword within font families.✅[nesting-selector-no-missing-scoping-root](/user-guide/rules/nesting-selector-no-missing-scoping-root)
Disallow missing scoping root for nesting selectors.✅

### Non-standard[​](#non-standard)

Disallow non-standard things with these `no-nonstandard` rules.

[function-linear-gradient-no-nonstandard-direction](/user-guide/rules/function-linear-gradient-no-nonstandard-direction)
Disallow non-standard direction values for linear gradient functions.

### Overrides[​](#overrides)

Disallow overrides with these `no-overrides` rules.

[declaration-block-no-shorthand-property-overrides](/user-guide/rules/declaration-block-no-shorthand-property-overrides)
Disallow shorthand properties that override related longhand properties.✅

### Unmatchable[​](#unmatchable)

Disallow unmatchable things with these `no-unmatchable` rules.

[selector-anb-no-unmatchable](/user-guide/rules/selector-anb-no-unmatchable)
Disallow unmatchable An+B selectors.✅

### Unknown[​](#unknown)

Disallow unknown things with these `no-unknown` rules.

[annotation-no-unknown](/user-guide/rules/annotation-no-unknown)
Disallow unknown annotations.✅[at-rule-descriptor-no-unknown](/user-guide/rules/at-rule-descriptor-no-unknown)
Disallow unknown at-rule descriptors.✅[at-rule-descriptor-value-no-unknown](/user-guide/rules/at-rule-descriptor-value-no-unknown)
Disallow unknown values for descriptors within at-rules.✅[at-rule-no-unknown](/user-guide/rules/at-rule-no-unknown)
Disallow unknown at-rules.✅[declaration-property-value-no-unknown](/user-guide/rules/declaration-property-value-no-unknown)
Disallow unknown values for properties within declarations.✅[function-no-unknown](/user-guide/rules/function-no-unknown)
Disallow unknown functions.[media-feature-name-no-unknown](/user-guide/rules/media-feature-name-no-unknown)
Disallow unknown media feature names.✅[media-feature-name-value-no-unknown](/user-guide/rules/media-feature-name-value-no-unknown)
Disallow unknown values for media features.✅[no-unknown-animations](/user-guide/rules/no-unknown-animations)
Disallow unknown animations.[no-unknown-custom-media](/user-guide/rules/no-unknown-custom-media)
Disallow unknown custom media queries.[no-unknown-custom-properties](/user-guide/rules/no-unknown-custom-properties)
Disallow unknown custom properties.[property-no-unknown](/user-guide/rules/property-no-unknown)
Disallow unknown properties.✅[selector-pseudo-class-no-unknown](/user-guide/rules/selector-pseudo-class-no-unknown)
Disallow unknown pseudo-class selectors.✅[selector-pseudo-element-no-unknown](/user-guide/rules/selector-pseudo-element-no-unknown)
Disallow unknown pseudo-element selectors.✅[selector-type-no-unknown](/user-guide/rules/selector-type-no-unknown)
Disallow unknown type selectors.✅[unit-no-unknown](/user-guide/rules/unit-no-unknown)
Disallow unknown units.

## Enforce conventions[​](#enforce-conventions)

You can enforce conventions with these `no` and `list` rules. They are powerful rules for making your code consistent. You'll need to configure most of them to suit your needs.

### Allowed, disallowed & required[​](#allowed-disallowed--required)

Allow, disallow or require things with these `allowed-list`, `disallowed-list`, `required-list` and `no` rules.

#### At-rule[​](#at-rule)

[at-rule-allowed-list](/user-guide/rules/at-rule-allowed-list)
Specify a list of allowed at-rules.[at-rule-disallowed-list](/user-guide/rules/at-rule-disallowed-list)
Specify a list of disallowed at-rules.[at-rule-no-vendor-prefix](/user-guide/rules/at-rule-no-vendor-prefix)
Disallow vendor prefixes for at-rules.✅🔧[at-rule-property-required-list](/user-guide/rules/at-rule-property-required-list)
Specify a list of required properties (or descriptors) for an at-rule.

#### Color[​](#color)

[color-hex-alpha](/user-guide/rules/color-hex-alpha)
Require or disallow alpha channel for hex colors.[color-named](/user-guide/rules/color-named)
Require (where possible) or disallow named colors.[color-no-hex](/user-guide/rules/color-no-hex)
Disallow hex colors.

#### Comment[​](#comment)

[comment-word-disallowed-list](/user-guide/rules/comment-word-disallowed-list)
Specify a list of disallowed words within comments.

#### Declaration[​](#declaration)

[declaration-no-important](/user-guide/rules/declaration-no-important)
Disallow `!important` within declarations.[declaration-property-unit-allowed-list](/user-guide/rules/declaration-property-unit-allowed-list)
Specify a list of allowed property and unit pairs within declarations.[declaration-property-unit-disallowed-list](/user-guide/rules/declaration-property-unit-disallowed-list)
Specify a list of disallowed property and unit pairs within declarations.[declaration-property-value-allowed-list](/user-guide/rules/declaration-property-value-allowed-list)
Specify a list of allowed property and value pairs within declarations.[declaration-property-value-disallowed-list](/user-guide/rules/declaration-property-value-disallowed-list)
Specify a list of disallowed property and value pairs within declarations.

#### Function[​](#function)

[function-allowed-list](/user-guide/rules/function-allowed-list)
Specify a list of allowed functions.[function-disallowed-list](/user-guide/rules/function-disallowed-list)
Specify a list of disallowed functions.[function-url-no-scheme-relative](/user-guide/rules/function-url-no-scheme-relative)
Disallow scheme-relative URLs.[function-url-scheme-allowed-list](/user-guide/rules/function-url-scheme-allowed-list)
Specify a list of allowed URL schemes.[function-url-scheme-disallowed-list](/user-guide/rules/function-url-scheme-disallowed-list)
Specify a list of disallowed URL schemes.

#### Length[​](#length)

[length-zero-no-unit](/user-guide/rules/length-zero-no-unit)
Disallow units for zero lengths.✅🔧

#### Media feature[​](#media-feature)

[media-feature-name-allowed-list](/user-guide/rules/media-feature-name-allowed-list)
Specify a list of allowed media feature names.[media-feature-name-disallowed-list](/user-guide/rules/media-feature-name-disallowed-list)
Specify a list of disallowed media feature names.[media-feature-name-no-vendor-prefix](/user-guide/rules/media-feature-name-no-vendor-prefix)
Disallow vendor prefixes for media feature names.✅🔧[media-feature-name-unit-allowed-list](/user-guide/rules/media-feature-name-unit-allowed-list)
Specify a list of allowed name and unit pairs within media features.[media-feature-name-value-allowed-list](/user-guide/rules/media-feature-name-value-allowed-list)
Specify a list of allowed media feature name and value pairs.

#### Property[​](#property)

[property-allowed-list](/user-guide/rules/property-allowed-list)
Specify a list of allowed properties.[property-disallowed-list](/user-guide/rules/property-disallowed-list)
Specify a list of disallowed properties.[property-no-vendor-prefix](/user-guide/rules/property-no-vendor-prefix)
Disallow vendor prefixes for properties.✅🔧

#### Rule[​](#rule)

[rule-nesting-at-rule-required-list](/user-guide/rules/rule-nesting-at-rule-required-list)
Require rules to be nested in specific at-rules.[rule-selector-property-disallowed-list](/user-guide/rules/rule-selector-property-disallowed-list)
Specify a list of disallowed properties for selectors within rules.

#### Selector[​](#selector)

[selector-attribute-name-disallowed-list](/user-guide/rules/selector-attribute-name-disallowed-list)
Specify a list of disallowed attribute names.[selector-attribute-operator-allowed-list](/user-guide/rules/selector-attribute-operator-allowed-list)
Specify a list of allowed attribute operators.[selector-attribute-operator-disallowed-list](/user-guide/rules/selector-attribute-operator-disallowed-list)
Specify a list of disallowed attribute operators.[selector-combinator-allowed-list](/user-guide/rules/selector-combinator-allowed-list)
Specify a list of allowed combinators.[selector-combinator-disallowed-list](/user-guide/rules/selector-combinator-disallowed-list)
Specify a list of disallowed combinators.[selector-disallowed-list](/user-guide/rules/selector-disallowed-list)
Specify a list of disallowed selectors.[selector-no-qualifying-type](/user-guide/rules/selector-no-qualifying-type)
Disallow qualifying a selector by type.[selector-no-vendor-prefix](/user-guide/rules/selector-no-vendor-prefix)
Disallow vendor prefixes for selectors.✅🔧[selector-pseudo-class-allowed-list](/user-guide/rules/selector-pseudo-class-allowed-list)
Specify a list of allowed pseudo-class selectors.[selector-pseudo-class-disallowed-list](/user-guide/rules/selector-pseudo-class-disallowed-list)
Specify a list of disallowed pseudo-class selectors.[selector-pseudo-element-allowed-list](/user-guide/rules/selector-pseudo-element-allowed-list)
Specify a list of allowed pseudo-element selectors.[selector-pseudo-element-disallowed-list](/user-guide/rules/selector-pseudo-element-disallowed-list)
Specify a list of disallowed pseudo-element selectors.

#### Unit[​](#unit)

[unit-allowed-list](/user-guide/rules/unit-allowed-list)
Specify a list of allowed units.[unit-disallowed-list](/user-guide/rules/unit-disallowed-list)
Specify a list of disallowed units.

#### Value[​](#value)

[value-no-vendor-prefix](/user-guide/rules/value-no-vendor-prefix)
Disallow vendor prefixes for values.✅🔧

### Case[​](#case)

Specify lowercase or uppercase for words with these `case` rules.

[function-name-case](/user-guide/rules/function-name-case)
Specify lowercase or uppercase for function names.✅🔧[selector-type-case](/user-guide/rules/selector-type-case)
Specify lowercase or uppercase for type selectors.✅🔧[value-keyword-case](/user-guide/rules/value-keyword-case)
Specify lowercase or uppercase for keywords values.✅🔧

### Empty lines[​](#empty-lines)

Enforce or disallow empty lines before constructs with these `empty-line-before` rules.

[at-rule-empty-line-before](/user-guide/rules/at-rule-empty-line-before)
Require or disallow an empty line before at-rules.✅🔧[comment-empty-line-before](/user-guide/rules/comment-empty-line-before)
Require or disallow an empty line before comments.✅🔧[custom-property-empty-line-before](/user-guide/rules/custom-property-empty-line-before)
Require or disallow an empty line before custom properties.✅🔧[declaration-empty-line-before](/user-guide/rules/declaration-empty-line-before)
Require or disallow an empty line before declarations.✅🔧[rule-empty-line-before](/user-guide/rules/rule-empty-line-before)
Require or disallow an empty line before rules.✅🔧

### Max & min[​](#max--min)

Apply limits with these `max` and `min` rules.

[declaration-block-single-line-max-declarations](/user-guide/rules/declaration-block-single-line-max-declarations)
Limit the number of declarations within a single-line declaration block.✅[declaration-property-max-values](/user-guide/rules/declaration-property-max-values)
Limit the number of values for a list of properties within declarations.[max-nesting-depth](/user-guide/rules/max-nesting-depth)
Limit the depth of nesting.[number-max-precision](/user-guide/rules/number-max-precision)
Limit the number of decimal places allowed in numbers.✅[selector-max-attribute](/user-guide/rules/selector-max-attribute)
Limit the number of attribute selectors in a selector.[selector-max-class](/user-guide/rules/selector-max-class)
Limit the number of classes in a selector.[selector-max-combinators](/user-guide/rules/selector-max-combinators)
Limit the number of combinators in a selector.[selector-max-compound-selectors](/user-guide/rules/selector-max-compound-selectors)
Limit the number of compound selectors in a selector.[selector-max-id](/user-guide/rules/selector-max-id)
Limit the number of ID selectors in a selector.[selector-max-pseudo-class](/user-guide/rules/selector-max-pseudo-class)
Limit the number of pseudo-classes in a selector.[selector-max-specificity](/user-guide/rules/selector-max-specificity)
Limit the specificity of selectors.[selector-max-type](/user-guide/rules/selector-max-type)
Limit the number of type selectors in a selector.[selector-max-universal](/user-guide/rules/selector-max-universal)
Limit the number of universal selectors in a selector.[time-min-milliseconds](/user-guide/rules/time-min-milliseconds)
Limit the minimum number of milliseconds for time values.

### Notation[​](#notation)

Enforce one representation of things that have multiple with these `notation` (sometimes implicit) rules.

[alpha-value-notation](/user-guide/rules/alpha-value-notation)
Specify percentage or number notation for alpha-values.✅🔧[color-function-alias-notation](/user-guide/rules/color-function-alias-notation)
Specify alias notation for color-functions.✅🔧[color-function-notation](/user-guide/rules/color-function-notation)
Specify modern or legacy notation for color-functions.✅🔧[color-hex-length](/user-guide/rules/color-hex-length)
Specify short or long notation for hex colors.✅🔧[font-weight-notation](/user-guide/rules/font-weight-notation)
Specify numeric or named notation for font weights.🔧[hue-degree-notation](/user-guide/rules/hue-degree-notation)
Specify number or angle notation for degree hues.✅🔧[import-notation](/user-guide/rules/import-notation)
Specify string or URL notation for `@import` rules.✅🔧[keyframe-selector-notation](/user-guide/rules/keyframe-selector-notation)
Specify keyword or percentage notation for keyframe selectors.✅🔧[lightness-notation](/user-guide/rules/lightness-notation)
Specify number or percentage notation for lightness.✅🔧[media-feature-range-notation](/user-guide/rules/media-feature-range-notation)
Specify context or prefix notation for media feature ranges.✅🔧[selector-not-notation](/user-guide/rules/selector-not-notation)
Specify simple or complex notation for `:not()` pseudo-class selectors.✅🔧[selector-pseudo-element-colon-notation](/user-guide/rules/selector-pseudo-element-colon-notation)
Specify single or double colon notation for applicable pseudo-element selectors.✅🔧

### Pattern[​](#pattern)

Enforce naming conventions with these `pattern` rules.

[comment-pattern](/user-guide/rules/comment-pattern)
Specify a pattern for comments.[container-name-pattern](/user-guide/rules/container-name-pattern)
Specify a pattern for container names.✅[custom-media-pattern](/user-guide/rules/custom-media-pattern)
Specify a pattern for custom media query names.✅[custom-property-pattern](/user-guide/rules/custom-property-pattern)
Specify a pattern for custom properties.✅[keyframes-name-pattern](/user-guide/rules/keyframes-name-pattern)
Specify a pattern for keyframe names.✅[layer-name-pattern](/user-guide/rules/layer-name-pattern)
Specify a pattern for layer names.✅[selector-class-pattern](/user-guide/rules/selector-class-pattern)
Specify a pattern for class selectors.✅[selector-id-pattern](/user-guide/rules/selector-id-pattern)
Specify a pattern for ID selectors.✅[selector-nested-pattern](/user-guide/rules/selector-nested-pattern)
Specify a pattern for the selectors of rules nested within rules.

### Quotes[​](#quotes)

Require or disallow quotes with these `quotes` rules.

[font-family-name-quotes](/user-guide/rules/font-family-name-quotes)
Require or disallow quotes for font family names.✅🔧[function-url-quotes](/user-guide/rules/function-url-quotes)
Require or disallow quotes for urls.✅🔧[selector-attribute-quotes](/user-guide/rules/selector-attribute-quotes)
Require or disallow quotes for attribute values.✅🔧

### Redundant[​](#redundant)

Disallow redundancy with these `no-redundant` rules.

[block-no-redundant-nested-style-rules](/user-guide/rules/block-no-redundant-nested-style-rules)
Disallow redundant nested style rules within blocks.✅[declaration-block-no-redundant-longhand-properties](/user-guide/rules/declaration-block-no-redundant-longhand-properties)
Disallow redundant longhand properties within declaration-block.✅🔧[shorthand-property-no-redundant-values](/user-guide/rules/shorthand-property-no-redundant-values)
Disallow redundant values within shorthand properties.✅🔧

### Whitespace inside[​](#whitespace-inside)

Require or disallow whitespace on the inside with this `whitespace-inside` rule.

[comment-whitespace-inside](/user-guide/rules/comment-whitespace-inside)
Require or disallow whitespace on the inside of comment markers.✅🔧[PreviousConfiguring](/user-guide/configure)[Nextalpha-value-notation](/user-guide/rules/alpha-value-notation)

- [Avoid errors](#avoid-errors)

  - [Deprecated](#deprecated)
  - [Descending](#descending)
  - [Duplicate](#duplicate)
  - [Empty](#empty)
  - [Invalid](#invalid)
  - [Irregular](#irregular)
  - [Missing](#missing)
  - [Non-standard](#non-standard)
  - [Overrides](#overrides)
  - [Unmatchable](#unmatchable)
  - [Unknown](#unknown)

- [Enforce conventions](#enforce-conventions)

  - [Allowed, disallowed & required](#allowed-disallowed--required)
  - [Case](#case)
  - [Empty lines](#empty-lines)
  - [Max & min](#max--min)
  - [Notation](#notation)
  - [Pattern](#pattern)
  - [Quotes](#quotes)
  - [Redundant](#redundant)
  - [Whitespace inside](#whitespace-inside)
