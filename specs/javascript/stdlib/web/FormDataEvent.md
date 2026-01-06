# FormDataEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFormDataEvent&level=high)

The `FormDataEvent` interface represents a [formdata event](/en-US/docs/Web/API/HTMLFormElement/formdata_event) — such an event is fired on an [HTMLFormElement](/en-US/docs/Web/API/HTMLFormElement) object after the entry list representing the form's data is constructed. This happens when the form is submitted, but can also be triggered by the invocation of a [FormData()](/en-US/docs/Web/API/FormData/FormData) constructor.

This allows a [FormData](/en-US/docs/Web/API/FormData) object to be quickly obtained in response to a `formdata` event firing, rather than needing to put it together yourself when you wish to submit form data via a method like [fetch()](/en-US/docs/Web/API/Window/fetch) (see [Using FormData objects](/en-US/docs/Web/API/XMLHttpRequest_API/Using_FormData_Objects)).

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[FormDataEvent()](/en-US/docs/Web/API/FormDataEvent/FormDataEvent)

Creates a new `FormDataEvent` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent interface, [Event](/en-US/docs/Web/API/Event).

[FormDataEvent.formData](/en-US/docs/Web/API/FormDataEvent/formData)

Contains the [FormData](/en-US/docs/Web/API/FormData) object representing the data contained in the form when the event was fired.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

js

```
// grab reference to form

const formElem = document.querySelector("form");

// submit handler

formElem.addEventListener("submit", (e) => {
  // on form submission, prevent default
  e.preventDefault();

  console.log(form.querySelector('input[name="field1"]')); // FOO
  console.log(form.querySelector('input[name="field2"]')); // BAR

  // construct a FormData object, which fires the formdata event
  const formData = new FormData(formElem);
  // formdata gets modified by the formdata event
  console.log(formData.get("field1")); // foo
  console.log(formData.get("field2")); // bar
});

// formdata handler to retrieve data

formElem.addEventListener("formdata", (e) => {
  console.log("formdata fired");

  // modifies the form data
  const formData = e.formData;
  formData.set("field1", formData.get("field1").toLowerCase());
  formData.set("field2", formData.get("field2").toLowerCase());
});
```

## [Specifications](#specifications)

Specification
[HTML# the-formdataevent-interface](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-formdataevent-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [fetch()](/en-US/docs/Web/API/Window/fetch)
- [FormData](/en-US/docs/Web/API/FormData)
- [Using FormData objects](/en-US/docs/Web/API/XMLHttpRequest_API/Using_FormData_Objects)
- [<Form>](/en-US/docs/Web/HTML/Reference/Elements/form)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/FormDataEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/formdataevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFormDataEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fformdataevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FFormDataEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fformdataevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F58ad1df59f2ffb9ecab4e27fe1bdf1eb5a55f89b%0A*+Document+last+modified%3A+2024-07-24T01%3A12%3A06.000Z%0A%0A%3C%2Fdetails%3E)
