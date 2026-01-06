# XRInputSourceArray

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourceArray&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The interface `XRInputSourceArray` represents a live list of WebXR input sources, and is used as the return value of the [XRSession](/en-US/docs/Web/API/XRSession) property [inputSources](/en-US/docs/Web/API/XRSession/inputSources). Each entry is an [XRInputSource](/en-US/docs/Web/API/XRInputSource) representing one input device connected to the WebXR system.

In addition to being able to access the input sources in the list using standard array notation (that is, with index numbers inside square brackets), methods are available to allow the use of iterators and the [forEach()](/en-US/docs/Web/API/XRInputSourceArray/forEach) method is also available.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

The following properties are available on `XRInputSourceArray` objects.

[length](/en-US/docs/Web/API/XRInputSourceArray/length)Read onlyExperimental

The number of [XRInputSource](/en-US/docs/Web/API/XRInputSource) objects in the list.

## [Instance methods](#instance_methods)

The following methods are available on `XRInputSourceArray` objects. You may also use the features of the [Symbol](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) type.

[entries()](/en-US/docs/Web/API/XRInputSourceArray/entries)Experimental

Returns an [iterator](/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) you can use to walk the list of key/value pairs in the list. Each item returned is an array whose first value is the index and whose second value is the [XRInputSource](/en-US/docs/Web/API/XRInputSource) at that index.

[forEach()](/en-US/docs/Web/API/XRInputSourceArray/forEach)Experimental

Iterates over each item in the list, in order from first to last.

[keys()](/en-US/docs/Web/API/XRInputSourceArray/keys)Experimental

A list of the keys corresponding to the entries in the input source list.

[values()](/en-US/docs/Web/API/XRInputSourceArray/values)Experimental

Returns an `iterator` you can use to go through all the values in the list. Each item is a single [XRInputSource](/en-US/docs/Web/API/XRInputSource) object.

In addition to these methods, you may use array notation to access items in the list by index For example, the snippet of code below calls a function `handleInput()`, passing into it the first item in the input source list, if the list isn't empty.

js

```
let sources = xrSession.inputSources;
if (sources.length > 0) {
  handleInput(sources[0]);
}
```

## [Specifications](#specifications)

Specification
[WebXR Device API# xrinputsourcearray-interface](https://immersive-web.github.io/webxr/#xrinputsourcearray-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 11, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XRInputSourceArray/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrinputsourcearray/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourceArray&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrinputsourcearray%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRInputSourceArray%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrinputsourcearray%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd666d5ed812b56cbc9c6cba853494976da1f1dd2%0A*+Document+last+modified%3A+2025-03-11T00%3A20%3A46.000Z%0A%0A%3C%2Fdetails%3E)
