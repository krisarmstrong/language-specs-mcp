# ConstantSourceNode

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConstantSourceNode&level=high)

The `ConstantSourceNode` interface—part of the Web Audio API—represents an audio source (based upon [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode)) whose output is single unchanging value. This makes it useful for cases in which you need a constant value coming in from an audio source. In addition, it can be used like a constructible [AudioParam](/en-US/docs/Web/API/AudioParam) by automating the value of its [offset](/en-US/docs/Web/API/ConstantSourceNode/offset) or by connecting another node to it; see [Controlling multiple parameters with ConstantSourceNode](/en-US/docs/Web/API/Web_Audio_API/Controlling_multiple_parameters_with_ConstantSourceNode).

A `ConstantSourceNode` has no inputs and exactly one monaural (one-channel) output. The output's value is always the same as the value of the [offset](/en-US/docs/Web/API/ConstantSourceNode/offset) parameter.

Number of inputs`0`Number of outputs`1`

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[ConstantSourceNode()](/en-US/docs/Web/API/ConstantSourceNode/ConstantSourceNode)

Creates and returns a new `ConstantSourceNode` instance, optionally specifying an object which establishes initial values for the object's properties. As an alternative, you can use the [BaseAudioContext.createConstantSource()](/en-US/docs/Web/API/BaseAudioContext/createConstantSource) factory method; see [Creating an AudioNode](/en-US/docs/Web/API/AudioNode#creating_an_audionode).

## [Instance properties](#instance_properties)

Inherits properties from its parent interface, [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode), and adds the following properties:

[offset](/en-US/docs/Web/API/ConstantSourceNode/offset)

An [AudioParam](/en-US/docs/Web/API/AudioParam) which specifies the value that this source continuously outputs. The default value is 1.0.

### [Events](#events)

Inherits events from its parent interface, [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode).

Note: Some browsers' implementations of these events are part of the [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode) interface.

[ended](/en-US/docs/Web/API/AudioScheduledSourceNode/ended_event)

Fired whenever the `ConstantSourceNode` data has stopped playing.

## [Instance methods](#instance_methods)

Inherits methods from its parent interface, [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode).

Note: Some browsers' implementations of these methods are part of the [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode) interface.

[start()](/en-US/docs/Web/API/AudioScheduledSourceNode/start)

Schedules a sound to playback at an exact time.

[stop()](/en-US/docs/Web/API/AudioScheduledSourceNode/stop)

Schedules a sound to stop playback at an exact time.

## [Example](#example)

In the article [Controlling multiple parameters with ConstantSourceNode](/en-US/docs/Web/API/Web_Audio_API/Controlling_multiple_parameters_with_ConstantSourceNode), a `ConstantSourceNode` is created to allow one slider control to change the gain on two [GainNode](/en-US/docs/Web/API/GainNode)s. The three nodes are set up like this:

js

```
gainNode2 = context.createGain();
gainNode3 = context.createGain();
gainNode2.gain.value = gainNode3.gain.value = 0.5;
volumeSliderControl.value = gainNode2.gain.value;

constantNode = context.createConstantSource();
constantNode.connect(gainNode2.gain);
constantNode.connect(gainNode3.gain);
constantNode.start();

gainNode2.connect(context.destination);
gainNode3.connect(context.destination);
```

This code starts by creating the gain nodes and setting them and the volume control that will adjust their value all to 0.5. Then the `ConstantSourceNode` is created by calling [AudioContext.createConstantSource()](/en-US/docs/Web/API/BaseAudioContext/createConstantSource), and the gain parameters of each of the two gain nodes are connected to the `ConstantSourceNode`. After starting the constant source by calling its [start()](/en-US/docs/Web/API/AudioScheduledSourceNode/start) method. Finally, the two gain nodes are connected to the audio destination (typically speakers or headphones).

Now, whenever the value of [constantNode.offset](/en-US/docs/Web/API/ConstantSourceNode/offset) changes, the gain on both `gainNode2` and `gainNode3` will change to have that same value.

To see this example in action, as well as to read the rest of the code from which these snippets were derived, see [Controlling multiple parameters with ConstantSourceNode.](/en-US/docs/Web/API/Web_Audio_API/Controlling_multiple_parameters_with_ConstantSourceNode)

## [Specifications](#specifications)

Specification
[Web Audio API# ConstantSourceNode](https://webaudio.github.io/web-audio-api/#ConstantSourceNode)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the Web Audio API](/en-US/docs/Web/API/Web_Audio_API/Using_Web_Audio_API)
- [AudioScheduledSourceNode](/en-US/docs/Web/API/AudioScheduledSourceNode)
- [AudioNode](/en-US/docs/Web/API/AudioNode)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/ConstantSourceNode/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/constantsourcenode/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConstantSourceNode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fconstantsourcenode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FConstantSourceNode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fconstantsourcenode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc7edf2734fccb185c5e93ee114ea3d5edc0177b5%0A*+Document+last+modified%3A+2024-07-26T02%3A57%3A09.000Z%0A%0A%3C%2Fdetails%3E)
