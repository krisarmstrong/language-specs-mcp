# Media Session API

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Session_API&level=not)

The Media Session API provides a way to customize media notifications. It does this by providing metadata for display by the user agent for the media your web app is playing.

It also provides action handlers that the browser can use to access platform media keys such as hardware keys found on keyboards, headsets, remote controls, and software keys found in notification areas and on lock screens of mobile devices. So you can seamlessly control web-provided media via your device, even when not looking at the web page.

The aim is to allow users to know what's playing and to control it, without needing to open the specific page that launched it. To be able to support the Media Session API, a browser first needs a mechanism by which to access and be controlled by the OS-level media controls (such as Firefox's [MediaControl](https://bugzil.la/1648100)).

## In this article

- [Media Session concepts and usage](#media_session_concepts_and_usage)
- [Accessing the Media Session API](#accessing_the_media_session_api)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Media Session concepts and usage](#media_session_concepts_and_usage)

The [MediaMetadata](/en-US/docs/Web/API/MediaMetadata) interface lets a website provide rich metadata to the platform UI for media that is playing. This metadata includes the title, artist (creator) name, album (collection), artwork, and chapter information. The platform can show this metadata in media centers, notifications, device lock screens, and so on. For example, different devices might present the Media Session API data like so:

 Original image source: [Customize media notifications and playback controls with the Media Session API](https://web.dev/articles/media-session) on web.dev (2024)

The [MediaSession](/en-US/docs/Web/API/MediaSession) interface lets users control the playback of media through user-agent-defined interface elements. Interaction with these elements triggers action handlers on the web page playing the media. Since multiple pages may be simultaneously using this API, the user agent is responsible for calling the correct page's action handlers. The user agent provides default behaviors when no page-defined behavior is available.

## [Accessing the Media Session API](#accessing_the_media_session_api)

The primary interface for the Media Session API is the [MediaSession](/en-US/docs/Web/API/MediaSession) interface. Rather than creating your own `MediaSession` instance, you access the API using the [navigator.mediaSession](/en-US/docs/Web/API/Navigator/mediaSession) property. For example, to set the current state of the media session to `playing`:

js

```
navigator.mediaSession.playbackState = "playing";
```

## [Interfaces](#interfaces)

[ChapterInformation](/en-US/docs/Web/API/ChapterInformation)

Represents the metadata for an individual chapter of a media resource (i.e., a video or audio file).

[MediaMetadata](/en-US/docs/Web/API/MediaMetadata)

Allows a web page to provide rich media metadata for display in a platform UI.

[MediaSession](/en-US/docs/Web/API/MediaSession)

Allows a web page to provide custom behaviors for standard media playback interactions.

## [Examples](#examples)

### [Setting up action handlers for a music player](#setting_up_action_handlers_for_a_music_player)

The following example shows feature detection for the Media Session API. It then instantiates a metadata object for the session, and adds action handlers for the user control actions:

js

```
if ("mediaSession" in navigator) {
  navigator.mediaSession.metadata = new MediaMetadata({
    title: "Unforgettable",
    artist: "Nat King Cole",
    album: "The Ultimate Collection (Remastered)",
    artwork: [
      {
        src: "https://dummyimage.com/96x96",
        sizes: "96x96",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/128x128",
        sizes: "128x128",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/192x192",
        sizes: "192x192",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/256x256",
        sizes: "256x256",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/384x384",
        sizes: "384x384",
        type: "image/png",
      },
      {
        src: "https://dummyimage.com/512x512",
        sizes: "512x512",
        type: "image/png",
      },
    ],
  });

  navigator.mediaSession.setActionHandler("play", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("pause", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("stop", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("seekbackward", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("seekforward", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("seekto", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("previoustrack", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("nexttrack", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("skipad", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("togglecamera", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("togglemicrophone", () => {
    /* Code excerpted. */
  });
  navigator.mediaSession.setActionHandler("hangup", () => {
    /* Code excerpted. */
  });
}
```

Some user agents disable autoplay for media elements on mobile devices and require a user gesture to start media. The following example adds a `pointerup` event to an on-page play button, which is then used to kick off the media session code:

js

```
playButton.addEventListener("pointerup", (event) => {
  const audio = document.querySelector("audio");

  // User interacted with the page. Let's play audio!
  audio
    .play()
    .then(() => {
      /* Set up media session controls, as shown above. */
    })
    .catch((error) => {
      console.error(error);
    });
});
```

### [Using action handlers to control a slide presentation](#using_action_handlers_to_control_a_slide_presentation)

The `"previousslide"` and `"nextslide"` action handlers can be used to handle moving forward and backward through a slide presentation, for example when the user puts their presentation into a [Picture-in-Picture](/en-US/docs/Web/API/Picture-in-Picture_API) window, and presses the browser-supplied controls for navigating through slides.

js

```
try {
  navigator.mediaSession.setActionHandler("previousslide", () => {
    log('> User clicked "Previous Slide" icon.');
    if (slideNumber > 1) slideNumber--;
    updateSlide();
  });
} catch (error) {
  log('Warning! The "previousslide" media session action is not supported.');
}

try {
  navigator.mediaSession.setActionHandler("nextslide", () => {
    log('> User clicked "Next Slide" icon.');
    slideNumber++;
    updateSlide();
  });
} catch (error) {
  log('Warning! The "nextslide" media session action is not supported.');
}
```

See [Presenting Slides / Media Session Sample](https://googlechrome.github.io/samples/media-session/slides.html) for a working example.

## [Specifications](#specifications)

Specification
[Media Session# the-mediasession-interface](https://w3c.github.io/mediasession/#the-mediasession-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Customize media notifications and playback controls with the Media Session API](https://web.dev/articles/media-session) on web.dev (2024)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 7, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Media_Session_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/media_session_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Session_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmedia_session_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMedia_Session_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmedia_session_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F033bcb33784ef00e5c95c0333d51c771125f9f94%0A*+Document+last+modified%3A+2024-08-07T09%3A59%3A17.000Z%0A%0A%3C%2Fdetails%3E)
