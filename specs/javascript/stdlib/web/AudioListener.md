# AudioListener

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioListener&level=high)

The `AudioListener` interface represents the position and orientation of the unique person listening to the audio scene, and is used in [audio spatialization](/en-US/docs/Web/API/Web_Audio_API/Web_audio_spatialization_basics). All [PannerNode](/en-US/docs/Web/API/PannerNode)s spatialize in relation to the `AudioListener` stored in the [BaseAudioContext.listener](/en-US/docs/Web/API/BaseAudioContext/listener) attribute.

It is important to note that there is only one listener per context and that it isn't an [AudioNode](/en-US/docs/Web/API/AudioNode).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Deprecated features](#deprecated_features)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

Note: The position, forward, and up value are set and retrieved using different syntaxes. Retrieval is done by accessing, for example, `AudioListener.positionX`, while setting the same property is done with `AudioListener.positionX.value`. This is why these values are not marked read only, which is how they appear in the specification's IDL.

[AudioListener.positionX](/en-US/docs/Web/API/AudioListener/positionX)

Represents the horizontal position of the listener in a right-hand cartesian coordinate system. The default is 0.

[AudioListener.positionY](/en-US/docs/Web/API/AudioListener/positionY)

Represents the vertical position of the listener in a right-hand cartesian coordinate system. The default is 0.

[AudioListener.positionZ](/en-US/docs/Web/API/AudioListener/positionZ)

Represents the longitudinal (back and forth) position of the listener in a right-hand cartesian coordinate system. The default is 0.

[AudioListener.forwardX](/en-US/docs/Web/API/AudioListener/forwardX)

Represents the horizontal position of the listener's forward direction in the same cartesian coordinate system as the position (`positionX`, `positionY`, and `positionZ`) values. The forward and up values are linearly independent of each other. The default is 0.

[AudioListener.forwardY](/en-US/docs/Web/API/AudioListener/forwardY)

Represents the vertical position of the listener's forward direction in the same cartesian coordinate system as the position (`positionX`, `positionY`, and `positionZ`) values. The forward and up values are linearly independent of each other. The default is 0.

[AudioListener.forwardZ](/en-US/docs/Web/API/AudioListener/forwardZ)

Represents the longitudinal (back and forth) position of the listener's forward direction in the same cartesian coordinate system as the position (`positionX`, `positionY`, and `positionZ`) values. The forward and up values are linearly independent of each other. The default is -1.

[AudioListener.upX](/en-US/docs/Web/API/AudioListener/upX)

Represents the horizontal position of the top of the listener's head in the same cartesian coordinate system as the position (`positionX`, `positionY`, and `positionZ`) values. The forward and up values are linearly independent of each other. The default is 0.

[AudioListener.upY](/en-US/docs/Web/API/AudioListener/upY)

Represents the vertical position of the top of the listener's head in the same cartesian coordinate system as the position (`positionX`, `positionY`, and `positionZ`) values. The forward and up values are linearly independent of each other. The default is 1.

[AudioListener.upZ](/en-US/docs/Web/API/AudioListener/upZ)

Represents the longitudinal (back and forth) position of the top of the listener's head in the same cartesian coordinate system as the position (`positionX`, `positionY`, and `positionZ`) values. The forward and up values are linearly independent of each other. The default is 0.

## [Instance methods](#instance_methods)

[AudioListener.setOrientation()](/en-US/docs/Web/API/AudioListener/setOrientation)Deprecated

Sets the orientation of the listener.

[AudioListener.setPosition()](/en-US/docs/Web/API/AudioListener/setPosition)Deprecated

Sets the position of the listener.

Note: Although these methods are deprecated they are currently the only way to set the orientation and position in Firefox (see [Firefox bug 1283029](https://bugzil.la/1283029)).

## [Deprecated features](#deprecated_features)

The `setOrientation()` and `setPosition()` methods have been replaced by setting their property value equivalents. For example `setPosition(x, y, z)` can be achieved by setting `positionX.value`, `positionY.value`, and `positionZ.value` respectively.

## [Example](#example)

See [BaseAudioContext.createPanner()](/en-US/docs/Web/API/BaseAudioContext/createPanner#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# AudioListener](https://webaudio.github.io/web-audio-api/#AudioListener)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Oct 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/AudioListener/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiolistener/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioListener&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiolistener%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioListener%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiolistener%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fed9ebd794add41de1f2e759502b73e8650afe56b%0A*+Document+last+modified%3A+2024-10-02T13%3A58%3A44.000Z%0A%0A%3C%2Fdetails%3E)
