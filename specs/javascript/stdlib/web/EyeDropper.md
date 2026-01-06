# EyeDropper

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEyeDropper&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The `EyeDropper` interface represents an instance of an eyedropper tool that can be opened and used by the user to select colors from the screen.

## In this article

- [Constructor](#constructor)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Constructor](#constructor)

[EyeDropper()](/en-US/docs/Web/API/EyeDropper/EyeDropper)Experimental

Returns a new `EyeDropper` instance.

## [Instance methods](#instance_methods)

The `EyeDropper` interface doesn't inherit any methods.

[EyeDropper.open()](/en-US/docs/Web/API/EyeDropper/open)Experimental

Returns a promise that resolves to an object that gives access to the selected color.

## [Examples](#examples)

### [Opening the eyedropper tool and sampling a color](#opening_the_eyedropper_tool_and_sampling_a_color)

This example shows how to open an eyedropper tool and wait for the user to either select a pixel from the screen, or press Escape to cancel the eyedropper mode.

#### HTML

html

```
<button id="start-button">Open the eyedropper</button> <span id="result"></span>
```

#### JavaScript

js

```
document.getElementById("start-button").addEventListener("click", () => {
  const resultElement = document.getElementById("result");

  if (!window.EyeDropper) {
    resultElement.textContent =
      "Your browser does not support the EyeDropper API";
    return;
  }

  const eyeDropper = new EyeDropper();

  eyeDropper
    .open()
    .then((result) => {
      resultElement.textContent = result.sRGBHex;
      resultElement.style.backgroundColor = result.sRGBHex;
    })
    .catch((e) => {
      resultElement.textContent = e;
    });
});
```

#### Result

### [Aborting the eyedropper mode](#aborting_the_eyedropper_mode)

This example shows that the eyedropper mode can also be aborted before the user has selected a color or pressed Escape.

#### HTML

html

```
<button id="start-button">Open the eyedropper</button> <span id="result"></span>
```

#### JavaScript

js

```
document.getElementById("start-button").addEventListener("click", () => {
  const resultElement = document.getElementById("result");

  if (!window.EyeDropper) {
    resultElement.textContent =
      "Your browser does not support the EyeDropper API";
    return;
  }

  const eyeDropper = new EyeDropper();
  const abortController = new AbortController();

  eyeDropper
    .open({ signal: abortController.signal })
    .then((result) => {
      resultElement.textContent = result.sRGBHex;
      resultElement.style.backgroundColor = result.sRGBHex;
    })
    .catch((e) => {
      resultElement.textContent = e;
    });

  setTimeout(() => {
    abortController.abort();
  }, 2000);
});
```

#### Result

## [Specifications](#specifications)

Specification
[EyeDropper API# eyedropper-interface](https://wicg.github.io/eyedropper-api/#eyedropper-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 22, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/EyeDropper/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/eyedropper/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEyeDropper&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Feyedropper%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FEyeDropper%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Feyedropper%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9fb6c9e56c6db295967384730feeb941509ac743%0A*+Document+last+modified%3A+2023-02-22T10%3A15%3A21.000Z%0A%0A%3C%2Fdetails%3E)
