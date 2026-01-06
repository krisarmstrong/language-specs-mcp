# AudioParamDescriptor

The `AudioParamDescriptor` dictionary of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) specifies properties for [AudioParam](/en-US/docs/Web/API/AudioParam) objects.

It is used to create custom `AudioParam`s on an [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode). If the underlying [AudioWorkletProcessor](/en-US/docs/Web/API/AudioWorkletProcessor) has a [parameterDescriptors](/en-US/docs/Web/API/AudioWorkletProcessor/parameterDescriptors_static) static getter, then the returned array of objects based on this dictionary is used internally by `AudioWorkletNode` constructor to populate its [parameters](/en-US/docs/Web/API/AudioWorkletNode/parameters) property accordingly.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[name](#name)

The string which represents the name of the `AudioParam`. Under this name the `AudioParam` will be available in the [parameters](/en-US/docs/Web/API/AudioWorkletNode/parameters) property of the node, and under this name the [AudioWorkletProcessor.process](/en-US/docs/Web/API/AudioWorkletProcessor/process) method will acquire the calculated values of this `AudioParam`.

[automationRate Optional](#automationrate)

Either ["a-rate"](/en-US/docs/Web/API/AudioParam#a-rate), or ["k-rate"](/en-US/docs/Web/API/AudioParam#k-rate) string which represents an automation rate of this `AudioParam`. Defaults to `"a-rate"`.

[minValue Optional](#minvalue)

A `float` which represents minimum value of the `AudioParam`. Defaults to `-3.4028235e38`.

[maxValue Optional](#maxvalue)

A `float` which represents maximum value of the `AudioParam`. Defaults to `3.4028235e38`.

[defaultValue Optional](#defaultvalue)

A `float` which represents initial value of the `AudioParam`. Defaults to `0`.

## [Examples](#examples)

The code fragment below shows a descriptor of this type being returned by a static [parameterDescriptors](/en-US/docs/Web/API/AudioWorkletProcessor/parameterDescriptors_static) method defined in a custom `AudioWorkletProcessor` (this is part of the more complete example in [AudioWorkletNode.parameters](/en-US/docs/Web/API/AudioWorkletNode/parameters#examples)).

js

```
// white-noise-processor.js
class WhiteNoiseProcessor extends AudioWorkletProcessor {
  static get parameterDescriptors() {
    return [
      {
        name: "customGain",
        defaultValue: 1,
        minValue: 0,
        maxValue: 1,
        automationRate: "a-rate",
      },
    ];
  }

  // …
}
```

## [Specifications](#specifications)

Specification
[Web Audio API# AudioParamDescriptor](https://webaudio.github.io/web-audio-api/#AudioParamDescriptor)

## [See also](#see_also)

- [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)
- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Mar 25, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioParamDescriptor/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioparamdescriptor/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParamDescriptor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioparamdescriptor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioParamDescriptor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioparamdescriptor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46b0ecd3b5280fbff659d138e3a7eaaf0fd12a24%0A*+Document+last+modified%3A+2025-03-25T14%3A00%3A13.000Z%0A%0A%3C%2Fdetails%3E)
