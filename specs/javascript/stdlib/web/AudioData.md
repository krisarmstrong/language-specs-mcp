# AudioData

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioData&level=not)

Note: This feature is available in [Dedicated Web Workers](/en-US/docs/Web/API/DedicatedWorkerGlobalScope).

The `AudioData` interface of the [WebCodecs API](/en-US/docs/Web/API/WebCodecs_API) represents an audio sample.

`AudioData` is a [transferable object](/en-US/docs/Web/API/Web_Workers_API/Transferable_objects).

## In this article

- [Description](#description)
- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Description](#description)

An audio track consists of a stream of audio samples, each sample representing a captured moment of sound. An `AudioData` object is a representation of such a sample. Working alongside the interfaces of the [Insertable Streams API](/en-US/docs/Web/API/Insertable_Streams_for_MediaStreamTrack_API), you can break a stream into individual `AudioData` objects with [MediaStreamTrackProcessor](/en-US/docs/Web/API/MediaStreamTrackProcessor), or construct an audio track from a stream of frames with [MediaStreamTrackGenerator](/en-US/docs/Web/API/MediaStreamTrackGenerator).

Note: Find out more about audio on the web in [Digital audio concepts](/en-US/docs/Web/Media/Guides/Formats/Audio_concepts).

### [The media resource](#the_media_resource)

An `AudioData` object contains a reference to an attached media resource. This media resource contains the actual audio sample data described by the object. A media resource is maintained by the user agent until it is no longer referenced by an `AudioData` object, for example when [AudioData.close()](/en-US/docs/Web/API/AudioData/close) is called.

### [Planes and audio format](#planes_and_audio_format)

To return the sample format of an `AudioData` use the [AudioData.format](/en-US/docs/Web/API/AudioData/format) property. The format may be described as interleaved or planar. In interleaved formats, the audio samples from the different channels are laid out in a single buffer, described as a plane. This plane contains a number of elements equal to [AudioData.numberOfFrames](/en-US/docs/Web/API/AudioData/numberOfFrames) * [AudioData.numberOfChannels](/en-US/docs/Web/API/AudioData/numberOfChannels).

In planar format, the number of planes is equal to [AudioData.numberOfChannels](/en-US/docs/Web/API/AudioData/numberOfChannels), and each plane is a buffer containing a number of elements equal to [AudioData.numberOfFrames](/en-US/docs/Web/API/AudioData/numberOfFrames).

## [Constructor](#constructor)

[AudioData()](/en-US/docs/Web/API/AudioData/AudioData)

Creates a new `AudioData` object.

## [Instance properties](#instance_properties)

[AudioData.format](/en-US/docs/Web/API/AudioData/format)Read only

Returns the sample format of the audio.

[AudioData.sampleRate](/en-US/docs/Web/API/AudioData/sampleRate)Read only

Returns the sample rate of the audio in Hz.

[AudioData.numberOfFrames](/en-US/docs/Web/API/AudioData/numberOfFrames)Read only

Returns the number of frames.

[AudioData.numberOfChannels](/en-US/docs/Web/API/AudioData/numberOfChannels)Read only

Returns the number of audio channels.

[AudioData.duration](/en-US/docs/Web/API/AudioData/duration)Read only

Returns the duration of the audio in microseconds.

[AudioData.timestamp](/en-US/docs/Web/API/AudioData/timestamp)Read only

Returns the timestamp of the audio in microseconds.

## [Instance methods](#instance_methods)

[AudioData.allocationSize()](/en-US/docs/Web/API/AudioData/allocationSize)

Returns the number of bytes required to hold the sample as filtered by options passed into the method.

[AudioData.copyTo()](/en-US/docs/Web/API/AudioData/copyTo)

Copies the samples from the specified plane of the `AudioData` object to the destination.

[AudioData.clone()](/en-US/docs/Web/API/AudioData/clone)

Creates a new `AudioData` object with reference to the same media resource as the original.

[AudioData.close()](/en-US/docs/Web/API/AudioData/close)

Clears all states and releases the reference to the media resource.

## [Specifications](#specifications)

Specification
[WebCodecs# audiodata-interface](https://w3c.github.io/webcodecs/#audiodata-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 3, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/AudioData/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/audiodata/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioData&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Faudiodata%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAudioData%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Faudiodata%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F27bceead8e9b1fe9c92df0fa5e418f81bd5b9fdf%0A*+Document+last+modified%3A+2025-02-03T15%3A11%3A02.000Z%0A%0A%3C%2Fdetails%3E)
