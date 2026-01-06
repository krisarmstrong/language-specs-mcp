# SubmitEvent

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨September 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSubmitEvent&level=high)

The `SubmitEvent` interface defines the object used to represent an [HTML](/en-US/docs/Glossary/HTML) form's [submit](/en-US/docs/Web/API/HTMLFormElement/submit_event) event. This event is fired at the [<form>](/en-US/docs/Web/HTML/Reference/Elements/form) when the form's submit action is invoked.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[SubmitEvent()](/en-US/docs/Web/API/SubmitEvent/SubmitEvent)

Creates and returns a new `SubmitEvent` object whose [type](/en-US/docs/Web/API/Event/type) and other options are configured as specified. Note that currently the only valid `type` for a `SubmitEvent` is `submit`.

## [Instance properties](#instance_properties)

In addition to the properties listed below, this interface inherits the properties of its parent interface, [Event](/en-US/docs/Web/API/Event).

[submitter](/en-US/docs/Web/API/SubmitEvent/submitter)Read only

An [HTMLElement](/en-US/docs/Web/API/HTMLElement) object which identifies the button or other element which was invoked to trigger the form being submitted.

## [Instance methods](#instance_methods)

While `SubmitEvent` offers no methods of its own, it inherits any specified by its parent interface, [Event](/en-US/docs/Web/API/Event).

## [Examples](#examples)

In this example, a shopping cart may have an assortment of different submit buttons depending on factors such as the user's settings, the shop's settings, and any minimum or maximum shopping card totals established by the payment processors. Each of the submit elements' [id](/en-US/docs/Web/API/Element/id) is used to identify which payment processor the button corresponds to.

js

```
let form = document.querySelector("form");
form.addEventListener("submit", (event) => {
  let submitter = event.submitter;
  let handler = submitter.id;

  if (handler) {
    processOrder(form, handler);
  } else {
    showAlertMessage(
      "An unknown or unaccepted payment type was selected. Please try again.",
      "OK",
    );
  }
});
```

The handler ID is obtained by using the `submit` event's [submitter](/en-US/docs/Web/API/SubmitEvent/submitter) property to get the submit button, from which we then get the ID. With that in hand, we can call a `processOrder()` function to handle the order, passing along the form and the handler ID.

## [Specifications](#specifications)

Specification
[HTML# the-submitevent-interface](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-submitevent-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/SubmitEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/submitevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSubmitEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fsubmitevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FSubmitEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fsubmitevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
