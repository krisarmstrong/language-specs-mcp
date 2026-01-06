# AudioParamMap

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParamMap&level=high)

The `AudioParamMap` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) represents an iterable and read-only set of multiple audio parameters.

An `AudioParamMap` instance is a read-only [Map-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis), in which each key is the name string for a parameter, and the corresponding value is an [AudioParam](/en-US/docs/Web/API/AudioParam) containing the value of that parameter.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

The following methods are available to all read-only [Map-like objects](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis) (the below links are to the [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) global object reference page).

[size](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/size)

Returns the number of entries in the map.

## [Instance methods](#instance_methods)

The following methods are available to all read-only [Map-like objects](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#map-like_browser_apis) (the below links are to the [Map](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) global object reference page).

[entries()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/entries)

Returns a new [iterator object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) that yields entries in `[key, value]` pairs in the map in insertion order.

[forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach)

Calls a provided [callback function](/en-US/docs/Glossary/Callback_function) once for each value and key present in the map, in insertion order.

[get()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/get)

Returns the [AudioParam](/en-US/docs/Web/API/AudioParam) value associated with the string key, or `undefined` if there is none.

[has()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/has)

Returns a [boolean](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean) indicating whether a key is present in the map or not.

[keys()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/keys)

Returns a new iterator object that yields the string keys in the map in insertion order.

[values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/values)

Returns a new iterator object that yields the [AudioParam](/en-US/docs/Web/API/AudioParam) values in the map in insertion order.

## [Specifications](#specifications)

Specification
[Web Audio API# audioparammap](https://webaudio.github.io/web-audio-api/#audioparammap)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 8, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/AudioParamMap/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioparammap/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParamMap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioparammap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParamMap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioparammap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc99afd3cafe73c93831bd73ad1dac285c3c713b1%0A*+Document+last+modified%3A+2024-08-08T21%3A58%3A24.000Z%0A%0A%3C%2Fdetails%3E)
