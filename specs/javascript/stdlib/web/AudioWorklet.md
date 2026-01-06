# AudioWorklet

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorklet&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `AudioWorklet` interface of the [Web Audio API](/en-US/docs/Web/API/Web_Audio_API) is used to supply custom audio processing scripts that execute in a separate thread to provide very low latency audio processing.

The worklet's code is run in the [AudioWorkletGlobalScope](/en-US/docs/Web/API/AudioWorkletGlobalScope) global execution context, using a separate Web Audio thread which is shared by the worklet and other audio nodes.

Access the audio context's instance of `AudioWorklet` through the [BaseAudioContext.audioWorklet](/en-US/docs/Web/API/BaseAudioContext/audioWorklet) property.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

This interface also inherits properties defined on its parent interface, [Worklet](/en-US/docs/Web/API/Worklet).

[port](/en-US/docs/Web/API/AudioWorklet/port)Read onlyExperimental

Returns a [MessagePort](/en-US/docs/Web/API/MessagePort) for custom, asynchronous communication between code in the main thread and the global scope of an audio worklet. This allows for custom messages, such as sending and receiving control data or global settings.

## [Instance methods](#instance_methods)

This interface inherits methods from [Worklet](/en-US/docs/Web/API/Worklet). The `AudioWorklet` interface does not define any methods of its own.

## [Events](#events)

`AudioWorklet` has no events to which it responds.

## [Examples](#examples)

See [AudioWorkletNode](/en-US/docs/Web/API/AudioWorkletNode) for complete examples of custom audio node creation.

## [Specifications](#specifications)

Specification
[Web Audio API# AudioWorklet](https://webaudio.github.io/web-audio-api/#AudioWorklet)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [AudioWorkletGlobalScope](/en-US/docs/Web/API/AudioWorkletGlobalScope) — the global execution context of an `AudioWorklet`
- [Web Audio API](/en-US/docs/Web/API/Web_Audio_API)
- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [Using AudioWorklet](/en-US/docs/Web/API/Web_Audio_API/Using_AudioWorklet)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨May 9, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioWorklet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audioworklet/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorklet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudioworklet%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioWorklet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudioworklet%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa61be259435257328a25c462cb0f42bc91981a6f%0A*+Document+last+modified%3A+2025-05-09T10%3A10%3A27.000Z%0A%0A%3C%2Fdetails%3E)
