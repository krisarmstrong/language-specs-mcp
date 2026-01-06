# PannerNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPannerNode&level=high)

The `PannerNode` interface defines an audio-processing object that represents the location, direction, and behavior of an audio source signal in a simulated physical space. This [AudioNode](/en-US/docs/Web/API/AudioNode) uses right-hand Cartesian coordinates to describe the source's position as a vector and its orientation as a 3D directional cone.

A `PannerNode` always has exactly one input and one output: the input can be mono or stereo but the output is always stereo (2 channels); you can't have panning effects without at least two audio channels!

Number of inputs`1`Number of outputs`1`Channel count mode`"clamped-max"`Channel count`2`Channel interpretation`"speakers"`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[PannerNode()](/en-US/docs/Web/API/PannerNode/PannerNode)

Creates a new `PannerNode` object instance.

## [Instance properties](#instance_properties)

Inherits properties from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

Note: The orientation and position value are set and retrieved using different syntaxes, since they're stored as [AudioParam](/en-US/docs/Web/API/AudioParam) values. Retrieval is done by accessing, for example, `PannerNode.positionX`. While setting the same property is done with `PannerNode.positionX.value`. This is why these values are not marked read only, which is how they appear in the WebIDL.

[PannerNode.coneInnerAngle](/en-US/docs/Web/API/PannerNode/coneInnerAngle)

A double value describing the angle, in degrees, of a cone inside of which there will be no volume reduction.

[PannerNode.coneOuterAngle](/en-US/docs/Web/API/PannerNode/coneOuterAngle)

A double value describing the angle, in degrees, of a cone outside of which the volume will be reduced by a constant value, defined by the `coneOuterGain` property.

[PannerNode.coneOuterGain](/en-US/docs/Web/API/PannerNode/coneOuterGain)

A double value describing the amount of volume reduction outside the cone defined by the `coneOuterAngle` attribute. Its default value is `0`, meaning that no sound can be heard.

[PannerNode.distanceModel](/en-US/docs/Web/API/PannerNode/distanceModel)

An enumerated value determining which algorithm to use to reduce the volume of the audio source as it moves away from the listener. Possible values are `"linear"`, `"inverse"` and `"exponential"`. The default value is `"inverse"`.

[PannerNode.maxDistance](/en-US/docs/Web/API/PannerNode/maxDistance)

A double value representing the maximum distance between the audio source and the listener, after which the volume is not reduced any further.

[PannerNode.orientationX](/en-US/docs/Web/API/PannerNode/orientationX)

Represents the horizontal position of the audio source's vector in a right-hand Cartesian coordinate system. While this [AudioParam](/en-US/docs/Web/API/AudioParam) cannot be directly changed, its value can be altered using its [value](/en-US/docs/Web/API/AudioParam/value) property. The default is value is 1.

[PannerNode.orientationY](/en-US/docs/Web/API/PannerNode/orientationY)

Represents the vertical position of the audio source's vector in a right-hand Cartesian coordinate system. The default is 0. While this [AudioParam](/en-US/docs/Web/API/AudioParam) cannot be directly changed, its value can be altered using its [value](/en-US/docs/Web/API/AudioParam/value) property. The default is value is 0.

[PannerNode.orientationZ](/en-US/docs/Web/API/PannerNode/orientationZ)

Represents the longitudinal (back and forth) position of the audio source's vector in a right-hand Cartesian coordinate system. The default is 0. While this [AudioParam](/en-US/docs/Web/API/AudioParam) cannot be directly changed, its value can be altered using its [value](/en-US/docs/Web/API/AudioParam/value) property. The default is value is 0.

[PannerNode.panningModel](/en-US/docs/Web/API/PannerNode/panningModel)

An enumerated value determining which spatialization algorithm to use to position the audio in 3D space.

[PannerNode.positionX](/en-US/docs/Web/API/PannerNode/positionX)

Represents the horizontal position of the audio in a right-hand Cartesian coordinate system. The default is 0. While this [AudioParam](/en-US/docs/Web/API/AudioParam) cannot be directly changed, its value can be altered using its [value](/en-US/docs/Web/API/AudioParam/value) property. The default is value is 0.

[PannerNode.positionY](/en-US/docs/Web/API/PannerNode/positionY)

Represents the vertical position of the audio in a right-hand Cartesian coordinate system. The default is 0. While this [AudioParam](/en-US/docs/Web/API/AudioParam) cannot be directly changed, its value can be altered using its [value](/en-US/docs/Web/API/AudioParam/value) property. The default is value is 0.

[PannerNode.positionZ](/en-US/docs/Web/API/PannerNode/positionZ)

Represents the longitudinal (back and forth) position of the audio in a right-hand Cartesian coordinate system. The default is 0. While this [AudioParam](/en-US/docs/Web/API/AudioParam) cannot be directly changed, its value can be altered using its [value](/en-US/docs/Web/API/AudioParam/value) property. The default is value is 0.

[PannerNode.refDistance](/en-US/docs/Web/API/PannerNode/refDistance)

A double value representing the reference distance for reducing volume as the audio source moves further from the listener. For distances greater than this the volume will be reduced based on `rolloffFactor` and `distanceModel`.

[PannerNode.rolloffFactor](/en-US/docs/Web/API/PannerNode/rolloffFactor)

A double value describing how quickly the volume is reduced as the source moves away from the listener. This value is used by all distance models.

## [Instance methods](#instance_methods)

Inherits methods from its parent, [AudioNode](/en-US/docs/Web/API/AudioNode).

[PannerNode.setPosition()](/en-US/docs/Web/API/PannerNode/setPosition)Deprecated

Defines the position of the audio source relative to the listener (represented by an [AudioListener](/en-US/docs/Web/API/AudioListener) object stored in the [BaseAudioContext.listener](/en-US/docs/Web/API/BaseAudioContext/listener) attribute.)

[PannerNode.setOrientation()](/en-US/docs/Web/API/PannerNode/setOrientation)Deprecated

Defines the direction the audio source is playing in.

## [Examples](#examples)

See [BaseAudioContext.createPanner()](/en-US/docs/Web/API/BaseAudioContext/createPanner#examples) for example code.

## [Specifications](#specifications)

Specification
[Web Audio API# PannerNode](https://webaudio.github.io/web-audio-api/#PannerNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/PannerNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/pannernode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPannerNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fpannernode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FPannerNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fpannernode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faa8fa82a902746b0bd97839180fc2b5397088140%0A*+Document+last+modified%3A+2024-07-26T02%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E)
