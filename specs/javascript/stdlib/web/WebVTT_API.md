# WebVTT API

Web Video Text Tracks (WebVTT) are text tracks providing specific text "cues" that are time-aligned with other media, such as video or audio tracks. The WebVTT API provides functionality to define and manipulate these text tracks. The WebVTT API is primarily used for displaying subtitles or captions that overlay with video content, but it has other uses: providing chapter information for easier navigation and generic metadata that needs to be time-aligned with audio or video content.

## In this article

- [Concepts and usage](#concepts_and_usage)
- [Interfaces](#interfaces)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Concepts and usage](#concepts_and_usage)

A text track is a container for time-aligned text data that can be played in parallel with a video or audio track to provide a translation, transcription, or overview of the content. A video or audio media element may define tracks of different kinds or in different languages, allowing users to display appropriate tracks based on their preferences or needs.

The different kinds of text data that can be specified are `captions`, `descriptions`, `chapters`, `subtitles` or `metadata`; the [<track>](/en-US/docs/Web/HTML/Reference/Elements/track#kind) documentation has more information about what they mean. Note that browsers do not necessarily support all kinds of text tracks.

The individual time-aligned units of text data within a track are referred to as "cues". Each cue has a start time, end time, and textual payload. It may also have "cue settings", which affect its display region, position, alignment, and/or size. Lastly, a cue may have a label, which can be used to select it for CSS styling.

A text track and cues can be defined in a file using the [WebVTT File Format](/en-US/docs/Web/API/WebVTT_API/Web_Video_Text_Tracks_Format), and then associated with a particular [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element using the [<track>](/en-US/docs/Web/HTML/Reference/Elements/track) element.

Alternatively you can add a [TextTrack](/en-US/docs/Web/API/TextTrack) to a media element in JavaScript using [HTMLMediaElement.addTextTrack()](/en-US/docs/Web/API/HTMLMediaElement/addTextTrack), and then add individual [VTTCue](/en-US/docs/Web/API/VTTCue) objects to the track with [TextTrack.addCue()](/en-US/docs/Web/API/TextTrack/addCue).

The [::cue](/en-US/docs/Web/CSS/Reference/Selectors/::cue)[CSS](/en-US/docs/Web/CSS)[pseudo-element](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) can be used both in HTML and in a WebVTT file to style the cues for a particular element, for a particular tag within a cue, for a VTT class, or for a cue with a particular label. The `::cue-region` pseudo-element is intended for styling cues in a particular region, but is not supported in any browser.

Most important WebVTT features can be accessed using either the file format or Web API.

## [Interfaces](#interfaces)

[VTTCue](/en-US/docs/Web/API/VTTCue)

Represents a cue, the text displayed in a particular timeslice of the text track associated with a media element.

[VTTRegion](/en-US/docs/Web/API/VTTRegion)

Represents a portion of a video element onto which a [VTTCue](/en-US/docs/Web/API/VTTCue) can be rendered.

[TextTrack](/en-US/docs/Web/API/TextTrack)

Represents a text track, which holds the list of cues to display along with an associated media element at various points while it plays.

[TextTrackCue](/en-US/docs/Web/API/TextTrackCue)

An abstract base class for various cue types, such as [VTTCue](/en-US/docs/Web/API/VTTCue).

[TextTrackCueList](/en-US/docs/Web/API/TextTrackCueList)

An array-like object that represents a dynamically updating list of [TextTrackCue](/en-US/docs/Web/API/TextTrackCue) objects. An instance of this type is obtained from [TextTrack.cues](/en-US/docs/Web/API/TextTrack/cues) in order to get all the cues in the [TextTrack](/en-US/docs/Web/API/TextTrack) object.

[TextTrackList](/en-US/docs/Web/API/TextTrackList)

Represents a list of the text tracks defined for a media element, with each track represented by a separate [TextTrack](/en-US/docs/Web/API/TextTrack) instance in the list.

### [Related interfaces](#related_interfaces)

[TrackEvent](/en-US/docs/Web/API/TrackEvent)

Part of the HTML DOM API, this is the interface for the `addtrack` and `removetrack` events that are fired when a track is added or removed from [TextTrackList](/en-US/docs/Web/API/TextTrackList) (or more generally, when a track is added/removed from an HTML media element).

### [Related CSS extensions](#related_css_extensions)

These [CSS](/en-US/docs/Web/CSS)[pseudo-element](/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) are used to style cues in media with VTT tracks.

[::cue](/en-US/docs/Web/CSS/Reference/Selectors/::cue)

Matches cues within a selected element in media with VTT tracks.

Note: The specification defines another pseudo-element, `::cue-region`, but this is not supported by any browsers.

## [Examples](#examples)

### [Using the WebVTT API to add captions](#using_the_webvtt_api_to_add_captions)

#### HTML

The following example adds a new [TextTrack](/en-US/docs/Web/API/TextTrack) to the video, then adds cues using [TextTrack.addCue()](/en-US/docs/Web/API/TextTrack/addCue) method calls, with constructed `VTTCue` objects as arguments.

html

```
<video controls src="/shared-assets/videos/friday.mp4"></video>
```

#### CSS

css

```
video {
  width: 420px;
  height: 300px;
}
```

#### JavaScript

js

```
let video = document.querySelector("video");
let track = video.addTextTrack("captions", "Captions", "en");
track.mode = "showing";
track.addCue(new VTTCue(0, 0.9, "Hildy!"));
track.addCue(new VTTCue(1, 1.4, "How are you?"));
track.addCue(new VTTCue(1.5, 2.9, "Tell me, is the lord of the universe in?"));
track.addCue(new VTTCue(3, 4.2, "Yes, he's in - in a bad humor"));
track.addCue(new VTTCue(4.3, 6, "Somebody must've stolen the crown jewels"));
console.log(track.cues);
```

#### Result

### [Displaying VTT content defined in a file](#displaying_vtt_content_defined_in_a_file)

This example demonstrates how to add the same set of captions to the video seen in the above [Using the WebVTT API to add captions](#using_the_webvtt_api_to_add_captions) example. This time, however, we will do it declaratively using a [<track>](/en-US/docs/Web/HTML/Reference/Elements/track) element.

First, let's define the captions inside a "captions.vtt" file:

```
WEBVTT

00:00.000 --> 00:00.900
Hildy!

00:01.000 --> 00:01.400
How are you?

00:01.500 --> 00:02.900
Tell me, is the lord of the universe in?

00:03.000 --> 00:04.200
Yes, he's in - in a bad humor

00:04.300 --> 00:06.000
Somebody must've stolen the crown jewels
```

We can then add this to a [<video>](/en-US/docs/Web/HTML/Reference/Elements/video) element using the [<track>](/en-US/docs/Web/HTML/Reference/Elements/track) element. The following HTML would result in the same text track as the previous example:

html

```
<video controls src="video.webm">
  <track default kind="captions" src="captions.vtt" srclang="en" />
</video>
```

We can add multiple [<track>](/en-US/docs/Web/HTML/Reference/Elements/track) elements to specify different kinds of tracks in multiple languages, using the `kind` and `srclang` attributes. Note that, if `kind` is specified, `srclang`must be set too. The `default` attribute may be added to just one `<track>`: this is the one that will be played if user preferences don't specify a particular language or kind.

html

```
<video controls src="video.webm">
  <track default kind="captions" src="captions.vtt" srclang="en" />
  <track kind="subtitles" src="subtitles.vtt" srclang="en" />
  <track kind="descriptions" src="descriptions.vtt" srclang="en" />
  <track kind="chapters" src="chapters_de.vtt" srclang="de" />
  <track kind="subtitles" src="subtitles_en.vtt" srclang="en" />
</video>
```

### [Styling WebVTT in HTML or a stylesheet](#styling_webvtt_in_html_or_a_stylesheet)

You can style WebVTT cues by matching elements using the [::cue](/en-US/docs/Web/CSS/Reference/Selectors/::cue) pseudo-element. This allows you to modify the appearance of all cue text, or just specific elements. In this example, we'll add some styling to the [first example above](#using_the_webvtt_api_to_add_captions).

Note: It is also possible to define styles in the [WebVTT File Format](/en-US/docs/Web/API/WebVTT_API/Web_Video_Text_Tracks_Format).

#### HTML

The HTML for the video itself is the same as we saw previously:

```
video {
  width: 420px;
  height: 300px;
}
```

html

```
<video controls src="/shared-assets/videos/friday.mp4"></video>
```

#### CSS

First, we use the [::cue](/en-US/docs/Web/CSS/Reference/Selectors/::cue) pseudo-element to select all video text cues, giving them larger red and a gradient background.

css

```
video::cue {
  font-size: 1.5rem;
  background-image: linear-gradient(to bottom, yellow, lightyellow);
  color: red;
}
```

We then use [::cue](/en-US/docs/Web/CSS/Reference/Selectors/::cue) to select text that has been marked up using the `u` and `b` elements and style them green and yellow, respectively.

css

```
video::cue(u) {
  color: green;
}

video::cue(b) {
  color: purple;
}
```

#### JavaScript

The JavaScript is the same as in the first example, except that we have marked up some of the cue text using `<b>` (bold) and `<u>` (underline) tags. By default the marked text would be displayed as bold or underlined (depending on the tag) but we have used the [::cue](/en-US/docs/Web/CSS/Reference/Selectors/::cue) in the previous section to also style the text to be green and purple, respectively.

js

```
let video = document.querySelector("video");
let track = video.addTextTrack("captions", "Captions", "en");
track.mode = "showing";
track.addCue(new VTTCue(0, 0.9, "Hildy!"));
track.addCue(new VTTCue(1, 1.4, "How are you?"));
track.addCue(
  new VTTCue(1.5, 2.9, "Tell me, is the <u>lord of the universe</u> in?"),
);
track.addCue(new VTTCue(3, 4.2, "Yes, he's in - in a bad humor"));
track.addCue(
  new VTTCue(4.3, 6, "Somebody must've <b>stolen</b> the crown jewels"),
);
console.log(track.cues);
```

#### Result

### [More cue styling examples](#more_cue_styling_examples)

This example shows more examples of how you can mark up cue text with tags and then style them. The same markup and styles can be used in the [WebVTT File Format](/en-US/docs/Web/API/WebVTT_API/Web_Video_Text_Tracks_Format).

The HTML and CSS for displaying the video itself is the same as for the [first example above](#using_the_webvtt_api_to_add_captions) so here we only show the specific code for marking up and styling the text.

```
video {
  width: 420px;
  height: 300px;
}
```

```
<video controls src="/shared-assets/videos/friday.mp4"></video>
```

#### Styling by tag type

The first cue we create will be displayed for all 6 seconds of the video and display text marked up with `b`, `u`, `i` and `c` tags.

js

```
let video = document.querySelector("video");

let track = video.addTextTrack("captions", "Captions", "en");
track.mode = "showing";

track.addCue(
  new VTTCue(
    0,
    6,
    "Styles: Normal <b>bold</b> <u>underlined</u> <i>italic</i> <c>class</c>",
  ),
);
```

First, we'll add a rule to make all cues 1.2 times bigger than normal.

css

```
video::cue {
  font-size: 1.2rem;
}
```

Then we style each of the tags above with a different color.

css

```
video::cue(u) {
  color: green;
}

video::cue(b) {
  color: purple;
}

video::cue(i) {
  color: red;
}

video::cue(c) {
  color: lavender;
}
```

#### Styling by class

The second cue is displayed right after the first one and includes the same tags. However, they all have a class of `myclass` applied to them.

js

```
track.addCue(
  new VTTCue(
    1,
    6,
    "Styles: Class markup: <b.myclass>bold</b> <u.myclass>underlined</u> <i.myclass>italic</i> <c.myclass>class</c>",
  ),
);
```

We style all items with the `.myclass` class with a light blue text color, except for the specific case of `c.myclass`, which is given a blue text color.

css

```
video::cue(.myclass) {
  color: lightblue;
}

video::cue(c.myclass) {
  color: blue;
}
```

#### Styling using attributes

The next two cues are displayed after two and then three seconds. The first displays text marked up with the `lang` tag for three locales of English, while the second displays a `<v>` (voice) tag with the "Bob" attribute.

js

```
track.addCue(
  new VTTCue(
    2,
    6,
    "<lang en>Lang markup: 'en'</lang>  <lang en-GB>Text: 'en-GB'</lang> <lang en-US>Text: 'en-US'</lang>",
  ),
);

track.addCue(new VTTCue(3, 6, "<v Bob>Bob's voice</v>"));
```

We use the `lang` attribute selector to give each language variant a different text color.

css

```
video::cue([lang="en"]) {
  color: lightgreen;
}

video::cue([lang="en-GB"]) {
  color: darkgreen;
}

video::cue(:lang(en-US)) {
  color: #6082b6;
}
```

Then we use the `v` tag and attribute selector for `voice` to color text in "Bob's voice" orange.

css

```
video::cue(v[voice="Bob"]) {
  color: orange;
}
```

#### Result

The example should the cues with color coding that matches the styling above (if the text is not colored, then `::cue` is not supported on your browser).

## [Specifications](#specifications)

Specification
[WebVTT: The Web Video Text Tracks Format# the-vttcue-interface](https://w3c.github.io/webvtt/#the-vttcue-interface)
[WebVTT: The Web Video Text Tracks Format# the-vttregion-interface](https://w3c.github.io/webvtt/#the-vttregion-interface)
[HTML# texttrack](https://html.spec.whatwg.org/multipage/media.html#texttrack)

## [Browser compatibility](#browser_compatibility)

### [api.VTTCue](#api.VTTCue)

### [api.TextTrack](#api.TextTrack)

### [api.VTTRegion](#api.VTTRegion)

## [See also](#see_also)

- The CSS [::cue and ::cue()](/en-US/docs/Web/CSS/Reference/Selectors/::cue) pseudo-elements

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WebVTT_API/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/webvtt_api/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebVTT_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwebvtt_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWebVTT_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwebvtt_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4cb9d89a204a9532370693b982e8a3b274a874b1%0A*+Document+last+modified%3A+2025-11-04T01%3A20%3A56.000Z%0A%0A%3C%2Fdetails%3E)
