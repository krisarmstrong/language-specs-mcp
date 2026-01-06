# Worklet

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨April 2021⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorklet&level=high)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

The `Worklet` interface is a lightweight version of [Web Workers](/en-US/docs/Web/API/Web_Workers_API) and gives developers access to low-level parts of the rendering pipeline.

With Worklets, you can run JavaScript and [WebAssembly](/en-US/docs/WebAssembly) code to do graphics rendering or audio processing where high performance is required.

Worklets allow static import of [ECMAScript modules](/en-US/docs/Web/JavaScript/Guide/Modules), if supported, using [import](/en-US/docs/Web/JavaScript/Reference/Statements/import). Dynamic import is disallowed by the specification — calling [import()](/en-US/docs/Web/JavaScript/Reference/Operators/import) will throw.

## In this article

- [Worklet types](#worklet_types)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Worklet types](#worklet_types)

Worklets are restricted to specific use cases; they cannot be used for arbitrary computations like Web Workers. The `Worklet` interface abstracts properties and methods common to all kind of worklets, and cannot be created directly. Instead, you can use one of the following classes:

NameDescriptionLocationSpecification[AudioWorklet](/en-US/docs/Web/API/AudioWorklet)For audio processing with custom AudioNodes.Web Audio render thread[Web Audio API](https://webaudio.github.io/web-audio-api/#AudioWorklet)`AnimationWorklet` For creating scroll-linked and other high performance procedural animations. Compositor thread[CSS Animation Worklet API](https://wicg.github.io/animation-worklet/)`LayoutWorklet`For defining the positioning and dimensions of custom elements.[CSS Layout API](https://drafts.css-houdini.org/css-layout-api-1/#layout-worklet)[SharedStorageWorklet](/en-US/docs/Web/API/SharedStorageWorklet)For running private operations on cross-site data, without risk of data leakage.Main thread[Shared Storage API](https://wicg.github.io/shared-storage/)

Note: Paint worklets, defined by the [CSS Painting API](/en-US/docs/Web/API/CSS_Painting_API), don't subclass `Worklet`. They are accessed through a regular `Worklet` object obtained using [CSS.paintWorklet](/en-US/docs/Web/API/CSS/paintWorklet_static).

For 3D rendering with [WebGL](/en-US/docs/Web/API/WebGL_API), you don't use worklets. Instead, you write vertex shaders and fragment shaders using GLSL code, and those shaders will then run on the graphics card.

## [Instance properties](#instance_properties)

The Worklet interface does not define any properties.

## [Instance methods](#instance_methods)

[Worklet.addModule()](/en-US/docs/Web/API/Worklet/addModule)

Adds the script module at the given URL to the current worklet.

## [Specifications](#specifications)

Specification
[HTML# worklets-worklet](https://html.spec.whatwg.org/multipage/worklets.html#worklets-worklet)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Houdini: Demystifying CSS](https://developer.chrome.com/docs/css-ui/houdini) on Google Developers (2016)
- [AudioWorklet :: What, Why, and How](https://www.youtube.com/watch?v=g1L4O1smMC0&t=1m33s) on YouTube (2017)
- [Enter AudioWorklet](https://developer.chrome.com/blog/audio-worklet/) on Google Developers (2017)
- [Animation Worklet - HTTP203 Advent](https://www.youtube.com/watch?v=ZPkMMShYxKU&t=0m19s) on YouTube (2017)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Aug 2, 2024⁩ by [MDN contributors](/en-US/docs/Web/API/Worklet/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/worklet/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorklet&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fworklet%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWorklet%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fworklet%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb065c09b79d18abf0f04778c9307e1c312b8c6f9%0A*+Document+last+modified%3A+2024-08-02T15%3A47%3A51.000Z%0A%0A%3C%2Fdetails%3E)
