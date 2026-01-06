## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Rule reference

This is a list of all built-in rules.

Rules with  are enabled by `html-validate:recommended`.
 Rules with  are enabled by `html-validate:document`.

Additional presets can be found and compared in [Configuration presets](presets.html).

Third-party rules can be found in [Third-party rules](third-party.html).

## HTML syntax and concepts

Rules relating to the HTML syntax and concepts.

[attr-delimiter](/rules/attr-delimiter.html)Disallow whitespace between attribute key and value[attr-spacing](/rules/attr-spacing.html)Require attributes to be separated by whitespace[close-attr](/rules/close-attr.html)Disallow end tags from having attributes[close-order](/rules/close-order.html)Require elements to be closed in correct order[element-name](/rules/element-name.html)Disallow invalid element names[form-dup-name](/rules/form-dup-name.html)Require form controls to have a unique name[map-dup-name](/rules/map-dup-name.html)Require `<map name>` to be unique[map-id-name](/rules/map-id-name.html)Require name and id to match on <map> elements[no-dup-attr](/rules/no-dup-attr.html)Disallow duplicated attributes[no-dup-class](/rules/no-dup-class.html)Disallow duplicated classes[no-raw-characters](/rules/no-raw-characters.html)Disallow the use of unescaped special characters[no-redundant-for](/rules/no-redundant-for.html)Disallow usage of redundant label for attributes[script-type](/rules/script-type.html)Require valid type for `<script>` element[unrecognized-char-ref](/rules/unrecognized-char-ref.html)Disallow unrecognized character references[valid-autocomplete](/rules/valid-autocomplete.html)Require autocomplete attribute to be valid[valid-id](/rules/valid-id.html)Require `id` to be a valid identifier

## Content model

[attribute-allowed-values](/rules/attribute-allowed-values.html)Validate permitted attribute values[attribute-misuse](/rules/attribute-misuse.html)Require attribute to be used in correct context[element-permitted-content](/rules/element-permitted-content.html)Validate permitted content[element-permitted-occurrences](/rules/element-permitted-occurrences.html)Validate permitted number of element occurrences[element-permitted-order](/rules/element-permitted-order.html)Validate required element order[element-permitted-parent](/rules/element-permitted-parent.html)Validate permitted element parent[element-required-ancestor](/rules/element-required-ancestor.html)Validate required element ancestors[element-required-attributes](/rules/element-required-attributes.html)Ensure required attributes are set[element-required-content](/rules/element-required-content.html)Ensure required elements are present[input-attributes](/rules/input-attributes.html)Validates usage of input attributes[no-multiple-main](/rules/no-multiple-main.html)Disallow multiple `<main>`[script-element](/rules/script-element.html)Require end tag for `<script>`[void-content](/rules/void-content.html)Disallow void element with content

## Deprecated

Rules related to usage of deprecated or obsolete functionality.

[deprecated](/rules/deprecated.html)Disallow usage of deprecated elements[deprecated-rule](/rules/deprecated-rule.html)Disallow usage of deprecated rules[no-conditional-comment](/rules/no-conditional-comment.html)Disallow usage of conditional comments[no-deprecated-attr](/rules/no-deprecated-attr.html)Disallow usage of deprecated attributes

## Accessibility

[area-alt](/rules/area-alt.html)Require alternative text on `<area>` elements[aria-hidden-body](/rules/aria-hidden-body.html)disallow `aria-hidden` from being set on `<body>`[aria-label-misuse](/rules/aria-label-misuse.html)Disallow `aria-label` and `aria-labelledby` misuse[empty-heading](/rules/empty-heading.html)Require headings to have textual content[empty-title](/rules/empty-title.html)Require title to have textual content[hidden-focusable](/rules/hidden-focusable.html)Disallows `aria-hidden` on focusable elements[input-missing-label](/rules/input-missing-label.html)Require input to have label[meta-refresh](/rules/meta-refresh.html)Require meta refresh to have 0 second delay[multiple-labeled-controls](/rules/multiple-labeled-controls.html)Disallow labels associated with multiple controls[no-abstract-role](/rules/no-abstract-role.html)Disallow usage of abstract WAI-ARIA roles[no-autoplay](/rules/no-autoplay.html)Disallow autoplaying media elements[no-implicit-button-type](/rules/no-implicit-button-type.html)Disallow implicit button type[no-redundant-aria-label](/rules/no-redundant-aria-label.html)Disallow aria-label and label with same text content[no-redundant-role](/rules/no-redundant-role.html)Disallow usage of redundant roles[prefer-native-element](/rules/prefer-native-element.html)Prefer to use native HTML element over roles[svg-focusable](/rules/svg-focusable.html)Require <svg> to have focusable attribute[tel-non-breaking](/rules/tel-non-breaking.html)Require non-breaking characters in telephone numbers[text-content](/rules/text-content.html)Require elements to have valid text content[unique-landmark](/rules/unique-landmark.html)Requires landmarks to have unique names[wcag/h30](/rules/wcag/h30.html)WCAG H30: Providing link text[wcag/h32](/rules/wcag/h32.html)WCAG H32: Providing submit buttons[wcag/h36](/rules/wcag/h36.html)WCAG H36: Require alt text on images used as submit buttons[wcag/h37](/rules/wcag/h37.html)WCAG H37: Using alt attributes on img elements[wcag/h63](/rules/wcag/h63.html)WCAG H63: Using the scope attribute to associate header cells and data cells[wcag/h67](/rules/wcag/h67.html)WCAG H67: Using null alt text and no title attribute on img elements[wcag/h71](/rules/wcag/h71.html)WCAG H71: Providing a description for groups of form controls

## Security

[require-csp-nonce](/rules/require-csp-nonce.html)Require CSP nonce for resources[require-sri](/rules/require-sri.html)Require SRI for resources

## SEO

[long-title](/rules/long-title.html)Require title not to have too long text

## Style

[attr-case](/rules/attr-case.html)Require a specific case for attribute names[attr-pattern](/rules/attr-pattern.html)Require attributes to match configured patterns[attr-quotes](/rules/attr-quotes.html)Require attribute quoting[attribute-boolean-style](/rules/attribute-boolean-style.html)Require a specific style for boolean attributes[attribute-empty-style](/rules/attribute-empty-style.html)Require a specific style for empty attributes[class-pattern](/rules/class-pattern.html)Require classes to match a specific pattern[doctype-style](/rules/doctype-style.html)Require a specific case for DOCTYPE[element-case](/rules/element-case.html)Require a specific case for element names[id-pattern](/rules/id-pattern.html)Require IDs to match a specific pattern[name-pattern](/rules/name-pattern.html)Require form control names to match a specific pattern[no-implicit-close](/rules/no-implicit-close.html)Require elements with optional end tags to be explicitly closed[no-implicit-input-type](/rules/no-implicit-input-type.html)Disallow implicit input type[no-inline-style](/rules/no-inline-style.html)Disallow inline style[no-self-closing](/rules/no-self-closing.html)Disallow self-closing elements[no-style-tag](/rules/no-style-tag.html)Disallow usage of <style> tag[no-trailing-whitespace](/rules/no-trailing-whitespace.html)Disallow trailing whitespace[prefer-button](/rules/prefer-button.html)Prefer to use <button> instead of <input> for buttons[prefer-tbody](/rules/prefer-tbody.html)Prefer to wrap <tr> inside <tbody>[void-style](/rules/void-style.html)Require a specific style for closing void elements

## Document

These rules is to be used on full documents.

[allowed-links](/rules/allowed-links.html)Disallow link types[doctype-html](/rules/doctype-html.html)Require usage of "html" doctype[heading-level](/rules/heading-level.html)Require headings to start at h1 and increment by one[missing-doctype](/rules/missing-doctype.html)Require document to have a doctype[no-dup-id](/rules/no-dup-id.html)Disallow duplicated IDs[no-missing-references](/rules/no-missing-references.html)Require all element references to exist[no-utf8-bom](/rules/no-utf8-bom.html)Disallow documents from having UTF-8 BOM

## Uncategorized

[no-unknown-elements](/rules/no-unknown-elements.html)Disallow usage of unknown elements[no-unused-disable](/rules/no-unused-disable.html)Disallow unused disable directives
