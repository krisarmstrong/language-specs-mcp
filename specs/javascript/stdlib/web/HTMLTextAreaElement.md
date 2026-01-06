# HTMLTextAreaElement

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTextAreaElement&level=high)

The `HTMLTextAreaElement` interface provides properties and methods for manipulating the layout and presentation of [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea) elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

Also inherits properties from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[autocomplete](/en-US/docs/Web/API/HTMLTextAreaElement/autocomplete)

A string that represents the element's [autocomplete](/en-US/docs/Web/HTML/Reference/Elements/textarea#autocomplete) attribute.

[cols](/en-US/docs/Web/API/HTMLTextAreaElement/cols)

A number that represents the element's [cols](/en-US/docs/Web/HTML/Reference/Elements/textarea#cols) attribute, indicating the visible width of the text area.

[defaultValue](/en-US/docs/Web/API/HTMLTextAreaElement/defaultValue)

A string that represents the control's default value, which behaves like the [Node.textContent](/en-US/docs/Web/API/Node/textContent) property.

[dirName](/en-US/docs/Web/API/HTMLTextAreaElement/dirName)

A string that represents the directionality of the element.

[disabled](/en-US/docs/Web/API/HTMLTextAreaElement/disabled)

A boolean that represents the element's [disabled](/en-US/docs/Web/HTML/Reference/Elements/textarea#disabled) attribute, indicating that the control is not available for interaction.

[form](/en-US/docs/Web/API/HTMLTextAreaElement/form)Read only

Returns a reference to the parent form element. If this element is not contained in a form element, it can be the [id](/en-US/docs/Web/HTML/Reference/Global_attributes/id) attribute of any [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element in the same document or the value `null`.

[labels](/en-US/docs/Web/API/HTMLTextAreaElement/labels)Read only

Returns a [NodeList](/en-US/docs/Web/API/NodeList) of the [<label>](/en-US/docs/Web/HTML/Reference/Elements/label) elements associated with this element.

[maxLength](/en-US/docs/Web/API/HTMLTextAreaElement/maxLength)

A number that represents the element's [maxlength](/en-US/docs/Web/HTML/Reference/Elements/textarea#maxlength) attribute, indicating the maximum number of characters the user can enter. This constraint is evaluated only when the value changes.

[minLength](/en-US/docs/Web/API/HTMLTextAreaElement/minLength)

A number that represents the element's [minlength](/en-US/docs/Web/HTML/Reference/Elements/textarea#minlength) attribute, indicating the minimum number of characters the user can enter. This constraint is evaluated only when the value changes.

[name](/en-US/docs/Web/API/HTMLTextAreaElement/name)

A string that represents the element's [name](/en-US/docs/Web/HTML/Reference/Elements/textarea#name) attribute, containing the name of the control.

[placeholder](/en-US/docs/Web/API/HTMLTextAreaElement/placeholder)

A string that represents the element's [placeholder](/en-US/docs/Web/HTML/Reference/Elements/textarea#placeholder) attribute, containing a hint to the user about what to enter in the control.

[readOnly](/en-US/docs/Web/API/HTMLTextAreaElement/readOnly)

A boolean that represents the element's [readonly](/en-US/docs/Web/HTML/Reference/Elements/textarea#readonly) attribute, indicating that the user cannot modify the value of the control.

[required](/en-US/docs/Web/API/HTMLTextAreaElement/required)

A boolean that represents the element's [required](/en-US/docs/Web/HTML/Reference/Elements/textarea#required) attribute, indicating that the user must specify a value before submitting the form.

[rows](/en-US/docs/Web/API/HTMLTextAreaElement/rows)

A number that represents the element's [rows](/en-US/docs/Web/HTML/Reference/Elements/textarea#rows) attribute, indicating the number of visible text lines for the control.

[selectionDirection](/en-US/docs/Web/API/HTMLTextAreaElement/selectionDirection)

A string that represents the direction in which selection occurred. This is `forward` if selection was performed in the start-to-end direction of the current locale, or `backward` for the opposite direction. This can also be `none` if the direction is unknown.

[selectionEnd](/en-US/docs/Web/API/HTMLTextAreaElement/selectionEnd)

A number that represents the index of the end of selected text. If no text is selected, it contains the index of the character that follows the input cursor. On being set, the control behaves as if `setSelectionRange()` had been called with this as the second argument, and `selectionStart` as the first argument.

[selectionStart](/en-US/docs/Web/API/HTMLTextAreaElement/selectionStart)

A number that represents the index of the beginning of selected text. If no text is selected, it contains the index of the character that follows the input cursor. On being set, the control behaves as if `setSelectionRange()` had been called with this as the first argument and `selectionEnd` as the second argument.

[textLength](/en-US/docs/Web/API/HTMLTextAreaElement/textLength)Read only

Returns the code point length of the control's `value`. Same as reading `value.length`.

[type](/en-US/docs/Web/API/HTMLTextAreaElement/type)Read only

Returns the string `textarea`.

[validationMessage](/en-US/docs/Web/API/HTMLTextAreaElement/validationMessage)Read only

Returns a localized message that describes the validation constraints that the control does not satisfy (if any). This is the empty string if the control is not a candidate for constraint validation (`willValidate` is `false`), or it satisfies its constraints.

[validity](/en-US/docs/Web/API/HTMLTextAreaElement/validity)Read only

Returns the validity state that this element is in.

[value](/en-US/docs/Web/API/HTMLTextAreaElement/value)

A string that represents the raw value contained in the control.

[willValidate](/en-US/docs/Web/API/HTMLTextAreaElement/willValidate)Read only

Returns whether the element is a candidate for constraint validation. `false` if any conditions bar it from constraint validation, including its `readOnly` or `disabled` property is `true`.

[wrap](/en-US/docs/Web/API/HTMLTextAreaElement/wrap)

A string that represents the element's [wrap](/en-US/docs/Web/HTML/Reference/Elements/textarea#wrap) attribute, indicating how the control wraps text.

## [Instance methods](#instance_methods)

Also inherits methods from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[checkValidity()](/en-US/docs/Web/API/HTMLTextAreaElement/checkValidity)

Returns `false` if the element is a candidate for constraint validation, and it does not satisfy its constraints. In this case, it also fires a cancelable `invalid` event at the control. It returns `true` if the control is not a candidate for constraint validation, or if it satisfies its constraints.

[reportValidity()](/en-US/docs/Web/API/HTMLTextAreaElement/reportValidity)

This method reports the problems with the constraints on the element, if any, to the user. If there are problems, it fires a cancelable `invalid` event at the element, and returns `false`; if there are no problems, it returns `true`.

[select()](/en-US/docs/Web/API/HTMLTextAreaElement/select)

Selects the contents of the control.

[setCustomValidity()](/en-US/docs/Web/API/HTMLTextAreaElement/setCustomValidity)

Sets a custom validity message for the element. If this message is not the empty string, then the element is suffering from a custom validity error, and does not validate.

[setRangeText()](/en-US/docs/Web/API/HTMLTextAreaElement/setRangeText)

Replaces a range of text in the element with new text.

[setSelectionRange()](/en-US/docs/Web/API/HTMLTextAreaElement/setSelectionRange)

Selects a range of text in the element (but does not focus it).

## [Events](#events)

Also inherits events from its parent interface, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

Listen to these events using [addEventListener()](/en-US/docs/Web/API/EventTarget/addEventListener) or by assigning an event listener to the `oneventname` property of this interface:

[select](/en-US/docs/Web/API/HTMLTextAreaElement/select_event) event

Fires when some text has been selected.

[selectionchange](/en-US/docs/Web/API/HTMLTextAreaElement/selectionchange_event) event

Fires when the text selection in a [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea) element has been changed.

## [Examples](#examples)

### [Autogrowing textarea example](#autogrowing_textarea_example)

Make a textarea autogrow while typing:

#### JavaScript

js

```
function autoGrow(field) {
  if (field.scrollHeight > field.clientHeight) {
    field.style.height = `${field.scrollHeight}px`;
  }
}

document.querySelector("textarea").addEventListener("keyup", (e) => {
  autoGrow(e.target);
});
```

#### CSS

css

```
textarea.no-scrollbars {
  overflow: hidden;
  width: 300px;
  height: 100px;
}
```

#### HTML

html

```
<form>
  <fieldset>
    <legend>Your comments</legend>
    <p><textarea class="no-scrollbars"></textarea></p>
    <p><input type="submit" value="Send" /></p>
  </fieldset>
</form>
```

### [Insert HTML tags example](#insert_html_tags_example)

Insert some HTML tags in a textarea:

js

```
function insert(startTag, endTag) {
  const textArea = document.myForm.myTextArea;
  const start = textArea.selectionStart;
  const end = textArea.selectionEnd;
  const oldText = textArea.value;

  const prefix = oldText.substring(0, start);
  const inserted = startTag + oldText.substring(start, end) + endTag;
  const suffix = oldText.substring(end);

  textArea.value = `${prefix}${inserted}${suffix}`;

  const newStart = start + startTag.length;
  const newEnd = end + startTag.length;

  textArea.setSelectionRange(newStart, newEnd);
  textArea.focus();
}

function insertURL() {
  const newURL = prompt("Enter the full URL for the link");
  if (newURL) {
    insert(`<a href="${newURL}">`, "</a>");
  } else {
    document.myForm.myTextArea.focus();
  }
}

const strong = document.querySelector("#format-strong");
const em = document.querySelector("#format-em");
const link = document.querySelector("#format-link");
const code = document.querySelector("#format-code");

strong.addEventListener("click", (e) => insert("<strong>", "</strong>"));
em.addEventListener("click", (e) => insert("<em>", "</em>"));
link.addEventListener("click", (e) => insertURL());
code.addEventListener("click", (e) => insert("<code>", "</code>"));
```

Decorate the span to behave like a link:

css

```
.intLink {
  cursor: pointer;
  text-decoration: underline;
  color: blue;
}
```

html

```
<form name="myForm">
  <p>
    [
    <span class="intLink" id="format-strong"><strong>Bold</strong></span> |
    <span class="intLink" id="format-em"><em>Italic</em></span> |
    <span class="intLink" id="format-link">URL</span> |
    <span class="intLink" id="format-code">code</span> ]
  </p>

  <p>
    <textarea name="myTextArea" rows="10" cols="50">
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut facilisis, arcu vitae adipiscing placerat, nisl lectus accumsan nisi, vitae iaculis sem neque vel lectus. Praesent tristique commodo lorem quis fringilla. Sed ac tellus eros. 
    </textarea>
  </p>
</form>
```

## [Specifications](#specifications)

Specification
[HTML# htmltextareaelement](https://html.spec.whatwg.org/multipage/form-elements.html#htmltextareaelement)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 8, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLTextAreaElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmltextareaelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTextAreaElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmltextareaelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLTextAreaElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmltextareaelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5f2a755c4fa7d126f85b56fbca90b15c5f039eff%0A*+Document+last+modified%3A+2025-08-08T16%3A55%3A34.000Z%0A%0A%3C%2Fdetails%3E)
