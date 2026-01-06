# ValidityState

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FValidityState&level=high)

The `ValidityState` interface represents the validity states that an element can be in, with respect to constraint validation. Together, they help explain why an element's value fails to validate, if it's not valid.

## In this article

- [Instance properties](#instance_properties)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Each validity state is represented by a Boolean property. A value of `true` indicates that the corresponding validation constraint has failed, except for the `valid` property, which is `true` when the element's value obeys all constraints.

[badInput](/en-US/docs/Web/API/ValidityState/badInput)Read only

A boolean value that is `true` if the user has provided input that the browser is unable to convert.

[customError](/en-US/docs/Web/API/ValidityState/customError)Read only

A boolean value indicating whether the element's custom validity message has been set to a non-empty string by calling the element's [setCustomValidity()](/en-US/docs/Web/API/HTMLInputElement/setCustomValidity) method.

[patternMismatch](/en-US/docs/Web/API/ValidityState/patternMismatch)Read only

A boolean value that is `true` if the value does not match the specified [pattern](/en-US/docs/Web/HTML/Reference/Elements/input#pattern), and `false` if it does match. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) CSS pseudo-class.

[rangeOverflow](/en-US/docs/Web/API/ValidityState/rangeOverflow)Read only

A boolean value that is `true` if the value is greater than the maximum specified by the [max](/en-US/docs/Web/HTML/Reference/Elements/input#max) attribute, or `false` if it is less than or equal to the maximum. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) and [:out-of-range](/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range) and CSS pseudo-classes.

[rangeUnderflow](/en-US/docs/Web/API/ValidityState/rangeUnderflow)Read only

A boolean value that is `true` if the value is less than the minimum specified by the [min](/en-US/docs/Web/HTML/Reference/Elements/input#min) attribute, or `false` if it is greater than or equal to the minimum. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) and [:out-of-range](/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range) CSS pseudo-classes.

[stepMismatch](/en-US/docs/Web/API/ValidityState/stepMismatch)Read only

A boolean value that is `true` if the value does not fit the rules determined by the [step](/en-US/docs/Web/HTML/Reference/Elements/input#step) attribute (that is, it's not evenly divisible by the step value), or `false` if it does fit the step rule. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) CSS pseudo-class.

[tooLong](/en-US/docs/Web/API/ValidityState/tooLong)Read only

A boolean value that is `true` if the value exceeds the specified `maxlength` for [HTMLInputElement](/en-US/docs/Web/API/HTMLInputElement) or [HTMLTextAreaElement](/en-US/docs/Web/API/HTMLTextAreaElement) objects, or `false` if its length is less than or equal to the maximum length. Note: This property is never `true` in Gecko, because elements' values are prevented from being longer than `maxlength`. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) and [:out-of-range](/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range) CSS pseudo-classes.

[tooShort](/en-US/docs/Web/API/ValidityState/tooShort)Read only

A boolean value that is `true` if the value fails to meet the specified `minlength` for [HTMLInputElement](/en-US/docs/Web/API/HTMLInputElement) or [HTMLTextAreaElement](/en-US/docs/Web/API/HTMLTextAreaElement) objects, or `false` if its length is greater than or equal to the minimum length. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) and [:out-of-range](/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range) CSS pseudo-classes.

[typeMismatch](/en-US/docs/Web/API/ValidityState/typeMismatch)Read only

A boolean value that is `true` if the value is not in the required syntax (when [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) is `email` or `url`), or `false` if the syntax is correct. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) CSS pseudo-class.

[valid](/en-US/docs/Web/API/ValidityState/valid)Read only

A boolean value that is `true` if the element meets all its validation constraints, and is therefore considered to be valid, or `false` if it fails any constraint. If `true`, the element matches the [:valid](/en-US/docs/Web/CSS/Reference/Selectors/:valid) CSS pseudo-class; the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) CSS pseudo-class otherwise.

[valueMissing](/en-US/docs/Web/API/ValidityState/valueMissing)Read only

A boolean value that is `true` if the element has a [required](/en-US/docs/Web/HTML/Reference/Elements/input#required) attribute, but no value, or `false` otherwise. If `true`, the element matches the [:invalid](/en-US/docs/Web/CSS/Reference/Selectors/:invalid) CSS pseudo-class.

## [Specifications](#specifications)

Specification
[HTML# validitystate](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#validitystate)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Guide: Constraint validation](/en-US/docs/Web/HTML/Guides/Constraint_validation)
- [Tutorial: Form data validation](/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jan 2, 2026⁩ by [MDN contributors](/en-US/docs/Web/API/ValidityState/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/validitystate/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FValidityState&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fvaliditystate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FValidityState%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fvaliditystate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F69cbda2568b49348e40e9fbae887cdabe1533038%0A*+Document+last+modified%3A+2026-01-02T03%3A55%3A19.000Z%0A%0A%3C%2Fdetails%3E)
