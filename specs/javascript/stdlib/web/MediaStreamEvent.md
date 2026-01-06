# MediaStreamEvent

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `MediaStreamEvent` interface represents events that occurs in relation to a [MediaStream](/en-US/docs/Web/API/MediaStream). Two events of this type can be thrown: [addstream](/en-US/docs/Web/API/RTCPeerConnection/addstream_event) and [removestream](/en-US/docs/Web/API/RTCPeerConnection/removestream_event).

## In this article

- [Instance properties](#instance_properties)
- [Constructors](#constructors)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

A `MediaStreamEvent` being an [Event](/en-US/docs/Web/API/Event), this event also implements these properties.

[MediaStreamEvent.stream](/en-US/docs/Web/API/MediaStreamEvent/stream)Read onlyDeprecatedNon-standard

Contains the [MediaStream](/en-US/docs/Web/API/MediaStream) containing the stream associated with the event.

## [Constructors](#constructors)

[MediaStreamEvent()](/en-US/docs/Web/API/MediaStreamEvent/MediaStreamEvent)DeprecatedNon-standard

Returns a new `MediaStreamEvent`. It takes two parameters, the first being a string representing the type of the event; the second a dictionary containing the [MediaStream](/en-US/docs/Web/API/MediaStream) it refers to.

## [Instance methods](#instance_methods)

A `MediaStreamEvent` being an [Event](/en-US/docs/Web/API/Event), this event also implements these properties. There is no specific `MediaStreamEvent` method.

## [Examples](#examples)

js

```
pc.onaddstream = (ev) => {
  alert(`A stream (id: '${ev.stream.id}') has been added to this connection.`);
};
```

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebRTC](/en-US/docs/Web/API/WebRTC_API)
- Its usual target: [RTCPeerConnection](/en-US/docs/Web/API/RTCPeerConnection).

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 24, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/MediaStreamEvent/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/mediastreamevent/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamEvent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fmediastreamevent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FMediaStreamEvent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fmediastreamevent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32305cc3cf274fbfdcc73a296bbd400a26f38296%0A*+Document+last+modified%3A+2024-07-24T20%3A47%3A46.000Z%0A%0A%3C%2Fdetails%3E)
