# HTMLFormElement

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFormElement&level=high)

The `HTMLFormElement` interface represents a [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) element in the DOM. It allows access to—and, in some cases, modification of—aspects of the form, as well as access to its component elements.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Usage notes](#usage_notes)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[HTMLFormElement.acceptCharset](/en-US/docs/Web/API/HTMLFormElement/acceptCharset)

A string reflecting the value of the form's [accept-charset](/en-US/docs/Web/HTML/Reference/Elements/form#accept-charset) HTML attribute.

[HTMLFormElement.action](/en-US/docs/Web/API/HTMLFormElement/action)

A string reflecting the value of the form's [action](/en-US/docs/Web/HTML/Reference/Elements/form#action) HTML attribute, containing the URI of a program that processes the information submitted by the form.

[HTMLFormElement.autocomplete](/en-US/docs/Web/API/HTMLFormElement/autocomplete)

A string reflecting the value of the form's [autocomplete](/en-US/docs/Web/HTML/Reference/Attributes/autocomplete) HTML attribute, indicating whether the controls in this form can have their values automatically populated by the browser.

[HTMLFormElement.encoding](/en-US/docs/Web/API/HTMLFormElement/encoding) or [HTMLFormElement.enctype](/en-US/docs/Web/API/HTMLFormElement/enctype)

A string reflecting the value of the form's [enctype](/en-US/docs/Web/HTML/Reference/Elements/form#enctype) HTML attribute, indicating the type of content that is used to transmit the form to the server. Only specified values can be set. The two properties are synonyms.

[HTMLFormElement.elements](/en-US/docs/Web/API/HTMLFormElement/elements)Read only

A [HTMLFormControlsCollection](/en-US/docs/Web/API/HTMLFormControlsCollection) holding all form controls belonging to this form element.

[HTMLFormElement.length](/en-US/docs/Web/API/HTMLFormElement/length)Read only

A `long` reflecting the number of controls in the form.

[HTMLFormElement.name](/en-US/docs/Web/API/HTMLFormElement/name)

A string reflecting the value of the form's [name](/en-US/docs/Web/HTML/Reference/Elements/form#name) HTML attribute, containing the name of the form.

[HTMLFormElement.noValidate](/en-US/docs/Web/API/HTMLFormElement/noValidate)

A boolean value reflecting the value of the form's [novalidate](/en-US/docs/Web/HTML/Reference/Elements/form#novalidate) HTML attribute, indicating whether the form should not be validated.

[HTMLFormElement.method](/en-US/docs/Web/API/HTMLFormElement/method)

A string reflecting the value of the form's [method](/en-US/docs/Web/HTML/Reference/Elements/form#method) HTML attribute, indicating the HTTP method used to submit the form. Only specified values can be set.

[HTMLFormElement.rel](/en-US/docs/Web/API/HTMLFormElement/rel)

A string reflecting the value of the form's [rel](/en-US/docs/Web/HTML/Reference/Attributes/rel) HTML attribute, which represents what kinds of links the form creates as a space-separated list of enumerated values.

[HTMLFormElement.relList](/en-US/docs/Web/API/HTMLFormElement/relList)Read only

A [DOMTokenList](/en-US/docs/Web/API/DOMTokenList) that reflects the [rel](/en-US/docs/Web/HTML/Reference/Attributes/rel) HTML attribute, as a list of tokens.

[HTMLFormElement.target](/en-US/docs/Web/API/HTMLFormElement/target)

A string reflecting the value of the form's [target](/en-US/docs/Web/HTML/Reference/Elements/form#target) HTML attribute, indicating where to display the results received from submitting the form.

Named inputs are added to their owner form instance as properties, and can overwrite native properties if they share the same name (e.g., a form with an input named `action` will have its `action` property return that input instead of the form's [action](/en-US/docs/Web/HTML/Reference/Elements/form#action) HTML attribute).

## [Instance methods](#instance_methods)

This interface also inherits methods from its parent, [HTMLElement](/en-US/docs/Web/API/HTMLElement).

[checkValidity()](/en-US/docs/Web/API/HTMLFormElement/checkValidity)

Returns `true` if the element's child controls are subject to [constraint validation](/en-US/docs/Web/HTML/Guides/Constraint_validation) and satisfy those constraints; returns `false` if some controls do not satisfy their constraints. Fires an event named [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event) at any control that does not satisfy its constraints; such controls are considered invalid if the event is not canceled. It is up to the programmer to decide how to respond to `false`.

[reportValidity()](/en-US/docs/Web/API/HTMLFormElement/reportValidity)

Returns `true` if the element's child controls satisfy their [validation constraints](/en-US/docs/Web/HTML/Guides/Constraint_validation). When `false` is returned, cancelable [invalid](/en-US/docs/Web/API/HTMLInputElement/invalid_event) events are fired for each invalid child and validation problems are reported to the user.

[requestSubmit()](/en-US/docs/Web/API/HTMLFormElement/requestSubmit)

Requests that the form be submitted using the specified submit button and its corresponding configuration.

[reset()](/en-US/docs/Web/API/HTMLFormElement/reset)

Resets the form to its initial state.

[submit()](/en-US/docs/Web/API/HTMLFormElement/submit)

Submits the form to the server.

## [Events](#events)

Listen to these events using `addEventListener()`, or by assigning an event listener to the `oneventname` property of this interface.

[formdata](/en-US/docs/Web/API/HTMLFormElement/formdata_event)

The `formdata` event fires after the entry list representing the form's data is constructed.

[reset](/en-US/docs/Web/API/HTMLFormElement/reset_event)

The `reset` event fires when a form is reset.

[submit](/en-US/docs/Web/API/HTMLFormElement/submit_event)

The `submit` event fires when a form is submitted.

## [Usage notes](#usage_notes)

### [Obtaining a form element object](#obtaining_a_form_element_object)

To obtain an `HTMLFormElement` object, you can use a [CSS selector](/en-US/docs/Web/CSS/Guides/Selectors) with [querySelector()](/en-US/docs/Web/API/Document/querySelector), or you can get a list of all of the forms in the document using its [forms](/en-US/docs/Web/API/Document/forms) property.

[Document.forms](/en-US/docs/Web/API/Document/forms) returns an array of `HTMLFormElement` objects listing each of the forms on the page. You can then use any of the following syntaxes to get an individual form:

[document.forms[index]](#document.formsindex)

Returns the form at the specified `index` into the array of forms.

[document.forms[id]](#document.formsid)

Returns the form whose ID is `id`.

[document.forms[name]](#document.formsname)

Returns the form whose `name` attribute's value is `name`.

### [Accessing the form's elements](#accessing_the_forms_elements)

You can access the list of the form's data-containing elements by examining the form's [elements](/en-US/docs/Web/API/HTMLFormElement/elements) property. This returns an [HTMLFormControlsCollection](/en-US/docs/Web/API/HTMLFormControlsCollection) listing all of the form's user data entry elements, both those which are descendants of the `<form>` and those which are made members of the form using their `form` attributes.

You can also get the form's element by using its `name` attribute as a key of the `form`, but using `elements` is a better approach—it contains only the form's elements, and it cannot be mixed with other attributes of the `form`.

### [Issues with Naming Elements](#issues_with_naming_elements)

Some names will interfere with JavaScript access to the form's properties and elements.

For example:

- `<input name="id">` will take precedence over `<form id="…">`. This means that `form.id` will not refer to the form's id, but to the element whose name is `"id"`. This will be the case with any other form properties, such as `<input name="action">` or `<input name="post">`.
- `<input name="elements">` will render the form's `elements` collection inaccessible. The reference `form.elements` will now refer to the individual element.

To avoid such problems with element names:

- Always use the `elements` collection to avoid ambiguity between an element name and a form property.
- Never use `"elements"` as an element name.

If you are not using JavaScript, this will not cause a problem.

### [Elements that are considered form controls](#elements_that_are_considered_form_controls)

The elements included by `HTMLFormElement.elements` and `HTMLFormElement.length` are the following:

- [<button>](/en-US/docs/Web/HTML/Reference/Elements/button)
- [<fieldset>](/en-US/docs/Web/HTML/Reference/Elements/fieldset)
- [<input>](/en-US/docs/Web/HTML/Reference/Elements/input) (with the exception that any whose [type](/en-US/docs/Web/HTML/Reference/Elements/input#type) is `"image"` are omitted for historical reasons)
- [<object>](/en-US/docs/Web/HTML/Reference/Elements/object)
- [<output>](/en-US/docs/Web/HTML/Reference/Elements/output)
- [<select>](/en-US/docs/Web/HTML/Reference/Elements/select)
- [<textarea>](/en-US/docs/Web/HTML/Reference/Elements/textarea)

No other elements are included in the list returned by `elements`, which makes it an excellent way to get at the most important elements when processing forms.

## [Examples](#examples)

Creating a new form element, modifying its attributes, then submitting it:

js

```
const f = document.createElement("form"); // Create a form
document.body.appendChild(f); // Add it to the document body
f.action = "/cgi-bin/some.cgi"; // Add action and method attributes
f.method = "POST";
f.submit(); // Call the form's submit() method
```

Extract information from a `<form>` element and set some of its attributes:

html

```
<form name="formA" action="/cgi-bin/test" method="post">
  <p>Press "Info" for form details, or "Set" to change those details.</p>
  <p>
    <button type="button" id="info">Info</button>
    <button type="button" id="set-info">Set</button>
    <button type="reset">Reset</button>
  </p>

  <textarea id="form-info" rows="15" cols="20"></textarea>
</form>
```

js

```
document.getElementById("info").addEventListener("click", () => {
  // Get a reference to the form via its name
  const f = document.forms["formA"];
  // The form properties we're interested in
  const properties = [
    "elements",
    "length",
    "name",
    "charset",
    "action",
    "acceptCharset",
    "action",
    "enctype",
    "method",
    "target",
  ];
  // Iterate over the properties, turning them into a string that we can display to the user
  const info = properties
    .map((property) => `${property}: ${f[property]}`)
    .join("\n");

  // Set the form's <textarea> to display the form's properties
  document.forms["formA"].elements["form-info"].value = info; // document.forms["formA"]['form-info'].value would also work
});

document.getElementById("set-info").addEventListener("click", (e) => {
  // Get a reference to the form via the event target
  // e.target is the button, and .form is the form it belongs to
  const f = e.target.form;
  // Argument should be a form element reference.
  f.action = "a-different-url.cgi";
  f.name = "a-different-name";
});
```

Submit a `<form>` into a new window:

html

```
<form action="test.php" target="_blank">
  <p>
    <label>First name: <input type="text" name="first-name" /></label>
  </p>
  <p>
    <label>Last name: <input type="text" name="last-name" /></label>
  </p>
  <p>
    <label><input type="password" name="pwd" /></label>
  </p>

  <fieldset>
    <legend>Pet preference</legend>

    <p>
      <label><input type="radio" name="pet" value="cat" /> Cat</label>
    </p>
    <p>
      <label><input type="radio" name="pet" value="dog" /> Dog</label>
    </p>
  </fieldset>

  <fieldset>
    <legend>Owned vehicles</legend>

    <p>
      <label
        ><input type="checkbox" name="vehicle" value="Bike" />I have a
        bike</label
      >
    </p>
    <p>
      <label
        ><input type="checkbox" name="vehicle" value="Car" />I have a car</label
      >
    </p>
  </fieldset>

  <p><button>Submit</button></p>
</form>
```

## [Specifications](#specifications)

Specification
[HTML# htmlformelement](https://html.spec.whatwg.org/multipage/forms.html#htmlformelement)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The HTML element implementing this interface: [<form>](/en-US/docs/Web/HTML/Reference/Elements/form).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 7, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/HTMLFormElement/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/htmlformelement/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFormElement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhtmlformelement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHTMLFormElement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhtmlformelement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E)
