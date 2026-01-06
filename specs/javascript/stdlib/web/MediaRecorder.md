# MediaRecorder

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaRecorder&level=high)

The `MediaRecorder` interface of the [MediaStream Recording API](/en-US/docs/Web/API/MediaStream_Recording_API) provides functionality to easily record media. It is created using the [MediaRecorder()](/en-US/docs/Web/API/MediaRecorder/MediaRecorder) constructor.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Static methods](#static_methods)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Example](#example)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[MediaRecorder()](/en-US/docs/Web/API/MediaRecorder/MediaRecorder)

Creates a new `MediaRecorder` object, given a [MediaStream](/en-US/docs/Web/API/MediaStream) to record. Options are available to do things like set the container's MIME type (such as `"video/webm"` or `"video/mp4"`) and the bit rates of the audio and video tracks or a single overall bit rate.

## [Instance properties](#instance_properties)

[MediaRecorder.mimeType](/en-US/docs/Web/API/MediaRecorder/mimeType)Read only

Returns the MIME type that was selected as the recording container for the `MediaRecorder` object when it was created.

[MediaRecorder.state](/en-US/docs/Web/API/MediaRecorder/state)Read only

Returns the current state of the `MediaRecorder` object (`inactive`, `recording`, or `paused`.)

[MediaRecorder.stream](/en-US/docs/Web/API/MediaRecorder/stream)Read only

Returns the stream that was passed into the constructor when the `MediaRecorder` was created.

[MediaRecorder.videoBitsPerSecond](/en-US/docs/Web/API/MediaRecorder/videoBitsPerSecond)Read only

Returns the video encoding bit rate in use. This may differ from the bit rate specified in the constructor (if it was provided).

[MediaRecorder.audioBitsPerSecond](/en-US/docs/Web/API/MediaRecorder/audioBitsPerSecond)Read only

Returns the audio encoding bit rate in use. This may differ from the bit rate specified in the constructor (if it was provided).

[MediaRecorder.audioBitrateMode](/en-US/docs/Web/API/MediaRecorder/audioBitrateMode)Read onlyExperimental

Returns the bitrate mode used to encode audio tracks.

## [Static methods](#static_methods)

[MediaRecorder.isTypeSupported()](/en-US/docs/Web/API/MediaRecorder/isTypeSupported_static)

A static method which returns a `true` or `false` value indicating if the given MIME media type is supported by the current user agent.

## [Instance methods](#instance_methods)

[MediaRecorder.pause()](/en-US/docs/Web/API/MediaRecorder/pause)

Pauses the recording of media.

[MediaRecorder.requestData()](/en-US/docs/Web/API/MediaRecorder/requestData)

Requests a [Blob](/en-US/docs/Web/API/Blob) containing the saved data received thus far (or since the last time `requestData()` was called. After calling this method, recording continues, but in a new `Blob`.

[MediaRecorder.resume()](/en-US/docs/Web/API/MediaRecorder/resume)

Resumes recording of media after having been paused.

[MediaRecorder.start()](/en-US/docs/Web/API/MediaRecorder/start)

Begins recording media; this method can optionally be passed a `timeslice` argument with a value in milliseconds. If this is specified, the media will be captured in separate chunks of that duration, rather than the default behavior of recording the media in a single large chunk.

[MediaRecorder.stop()](/en-US/docs/Web/API/MediaRecorder/stop)

Stops recording, at which point a [dataavailable](/en-US/docs/Web/API/MediaRecorder/dataavailable_event) event containing the final `Blob` of saved data is fired. No more recording occurs.

## [Events](#events)

Listen to these events using `addEventListener()` or by assigning an event listener to the `oneventname` property of this interface.

[dataavailable](/en-US/docs/Web/API/MediaRecorder/dataavailable_event)

Fires periodically each time `timeslice` milliseconds of media have been recorded (or when the entire media has been recorded, if `timeslice` wasn't specified). The event, of type [BlobEvent](/en-US/docs/Web/API/BlobEvent), contains the recorded media in its [data](/en-US/docs/Web/API/BlobEvent/data) property.

[error](/en-US/docs/Web/API/MediaRecorder/error_event)

Fired when there are fatal errors that stop recording. The received event is based on the [MediaRecorderErrorEvent](/en-US/docs/Web/API/MediaRecorderErrorEvent) interface, whose [error](/en-US/docs/Web/API/MediaRecorderErrorEvent/error) property contains a [DOMException](/en-US/docs/Web/API/DOMException) that describes the actual error that occurred.

[pause](/en-US/docs/Web/API/MediaRecorder/pause_event)

Fired when media recording is paused.

[resume](/en-US/docs/Web/API/MediaRecorder/resume_event)

Fired when media recording resumes after being paused.

[start](/en-US/docs/Web/API/MediaRecorder/start_event)

Fired when media recording starts.

[stop](/en-US/docs/Web/API/MediaRecorder/stop_event)

Fired when media recording ends, either when the [MediaStream](/en-US/docs/Web/API/MediaStream) ends, or after the [MediaRecorder.stop()](/en-US/docs/Web/API/MediaRecorder/stop) method is called.

## [Example](#example)

js

```
if (navigator.mediaDevices) {
  console.log("getUserMedia supported.");

  const constraints = { audio: true };
  let chunks = [];

  navigator.mediaDevices
    .getUserMedia(constraints)
    .then((stream) => {
      const mediaRecorder = new MediaRecorder(stream);

      record.onclick = () => {
        mediaRecorder.start();
        console.log(mediaRecorder.state);
        console.log("recorder started");
        record.style.background = "red";
        record.style.color = "black";
      };

      stop.onclick = () => {
        mediaRecorder.stop();
        console.log(mediaRecorder.state);
        console.log("recorder stopped");
        record.style.background = "";
        record.style.color = "";
      };

      mediaRecorder.onstop = (e) => {
        console.log("data available after MediaRecorder.stop() called.");

        const clipName = prompt("Enter a name for your sound clip");

        const clipContainer = document.createElement("article");
        const clipLabel = document.createElement("p");
        const audio = document.createElement("audio");
        const deleteButton = document.createElement("button");
        const mainContainer = document.querySelector("body");

        clipContainer.classList.add("clip");
        audio.setAttribute("controls", "");
        deleteButton.textContent = "Delete";
        clipLabel.textContent = clipName;

        clipContainer.appendChild(audio);
        clipContainer.appendChild(clipLabel);
        clipContainer.appendChild(deleteButton);
        mainContainer.appendChild(clipContainer);

        audio.controls = true;
        const blob = new Blob(chunks, { type: "audio/ogg; codecs=opus" });
        chunks = [];
        const audioURL = URL.createObjectURL(blob);
        audio.src = audioURL;
        console.log("recorder stopped");

        deleteButton.onclick = (e) => {
          const evtTgt = e.target;
          evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
        };
      };

      mediaRecorder.ondataavailable = (e) => {
        chunks.push(e.data);
      };
    })
    .catch((err) => {
      console.error(`The following error occurred: ${err}`);
    });
}
```

Note: This code sample is inspired by the Web Dictaphone demo. Some lines have been omitted for brevity; [refer to the source](https://github.com/mdn/dom-examples/tree/main/media/web-dictaphone) for the complete code.

## [Specifications](#specifications)

Specification
[MediaStream Recording# mediarecorder-api](https://w3c.github.io/mediacapture-record/#mediarecorder-api)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Using the MediaStream Recording API](/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API)
- [Web Dictaphone](https://mdn.github.io/dom-examples/media/web-dictaphone/): MediaRecorder + getUserMedia + Web Audio API visualization demo, by [Chris Mills](https://github.com/chrisdavidmills) ([source on GitHub](https://github.com/mdn/dom-examples/tree/main/media/web-dictaphone).)
- [Recording a media element](/en-US/docs/Web/API/MediaStream_Recording_API/Recording_a_media_element)
- [simpl.info MediaStream Recording demo](https://simpl.info/mediarecorder/), by [Sam Dutton](https://github.com/samdutton).
- [MediaDevices.getUserMedia()](/en-US/docs/Web/API/MediaDevices/getUserMedia)
- [OpenLang](https://github.com/chrisjohndigital/OpenLang): HTML video language lab web application using MediaDevices and the MediaStream Recording API for video recording ([source on GitHub](https://github.com/chrisjohndigital/OpenLang))

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 26, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaRecorder/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediarecorder/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaRecorder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediarecorder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaRecorder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediarecorder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcfb7587e3e3122630ad6cbd94d834ecadbe0a746%0A*+Document+last+modified%3A+2024-07-26T03%3A44%3A38.000Z%0A%0A%3C%2Fdetails%3E)
