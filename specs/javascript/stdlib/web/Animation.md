# Animation

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨March 2020⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimation&level=high)

The `Animation` interface of the [Web Animations API](/en-US/docs/Web/API/Web_Animations_API) represents a single animation player and provides playback controls and a timeline for an animation node or source.

## In this article

- [Constructor](#constructor)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Events](#events)
- [Accessibility concerns](#accessibility_concerns)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Constructor](#constructor)

[Animation()](/en-US/docs/Web/API/Animation/Animation)

Creates a new `Animation` object instance.

## [Instance properties](#instance_properties)

[Animation.currentTime](/en-US/docs/Web/API/Animation/currentTime)

The current time value of the animation in milliseconds, whether running or paused. If the animation lacks a [timeline](/en-US/docs/Web/API/AnimationTimeline), is inactive or hasn't been played yet, its value is `null`.

[Animation.effect](/en-US/docs/Web/API/Animation/effect)

Gets and sets the [AnimationEffect](/en-US/docs/Web/API/AnimationEffect) associated with this animation. This will usually be a [KeyframeEffect](/en-US/docs/Web/API/KeyframeEffect) object.

[Animation.finished](/en-US/docs/Web/API/Animation/finished)Read only

Returns the current finished Promise for this animation.

[Animation.id](/en-US/docs/Web/API/Animation/id)

Gets and sets the `String` used to identify the animation.

[Animation.overallProgress](/en-US/docs/Web/API/Animation/overallProgress)Read only

Returns a number between `0` and `1` indicating the animation's overall progress towards its finished state.

[Animation.pending](/en-US/docs/Web/API/Animation/pending)Read only

Indicates whether the animation is currently waiting for an asynchronous operation such as initiating playback or pausing a running animation.

[Animation.playState](/en-US/docs/Web/API/Animation/playState)Read only

Returns an enumerated value describing the playback state of an animation.

[Animation.playbackRate](/en-US/docs/Web/API/Animation/playbackRate)

Gets or sets the playback rate of the animation.

[Animation.ready](/en-US/docs/Web/API/Animation/ready)Read only

Returns the current ready Promise for this animation.

[Animation.replaceState](/en-US/docs/Web/API/Animation/replaceState)Read only

Indicates whether the animation is active, has been automatically removed after being replaced by another animation, or has been explicitly persisted by a call to [Animation.persist()](/en-US/docs/Web/API/Animation/persist).

[Animation.startTime](/en-US/docs/Web/API/Animation/startTime)

Gets or sets the scheduled time when an animation's playback should begin.

[Animation.timeline](/en-US/docs/Web/API/Animation/timeline)

Gets or sets the [timeline](/en-US/docs/Web/API/AnimationTimeline) associated with this animation.

## [Instance methods](#instance_methods)

[Animation.cancel()](/en-US/docs/Web/API/Animation/cancel)

Clears all [keyframeEffects](/en-US/docs/Web/API/KeyframeEffect) caused by this animation and aborts its playback.

[Animation.commitStyles()](/en-US/docs/Web/API/Animation/commitStyles)

Commits the current styling state of an animation to the element being animated, even after that animation has been removed. It will cause the current styling state to be written to the element being animated, in the form of properties inside a `style` attribute.

[Animation.finish()](/en-US/docs/Web/API/Animation/finish)

Seeks either end of an animation, depending on whether the animation is playing or reversing.

[Animation.pause()](/en-US/docs/Web/API/Animation/pause)

Suspends playing of an animation.

[Animation.persist()](/en-US/docs/Web/API/Animation/persist)

Explicitly persists an animation, preventing it from being [automatically removed](/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API#automatically_removing_filling_animations) when another animation replaces it.

[Animation.play()](/en-US/docs/Web/API/Animation/play)

Starts or resumes playing of an animation, or begins the animation again if it previously finished.

[Animation.reverse()](/en-US/docs/Web/API/Animation/reverse)

Reverses playback direction, stopping at the start of the animation. If the animation is finished or unplayed, it will play from end to beginning.

[Animation.updatePlaybackRate()](/en-US/docs/Web/API/Animation/updatePlaybackRate)

Sets the speed of an animation after first synchronizing its playback position.

## [Events](#events)

[cancel](/en-US/docs/Web/API/Animation/cancel_event)

Fires when the [Animation.cancel()](/en-US/docs/Web/API/Animation/cancel) method is called or when the animation enters the `"idle"` play state from another state.

[finish](/en-US/docs/Web/API/Animation/finish_event)

Fires when the animation finishes playing.

[remove](/en-US/docs/Web/API/Animation/remove_event)

Fires when the animation is [automatically removed](/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API#automatically_removing_filling_animations) by the browser.

## [Accessibility concerns](#accessibility_concerns)

Blinking and flashing animation can be problematic for people with cognitive concerns such as Attention Deficit Hyperactivity Disorder (ADHD). Additionally, certain kinds of motion can be a trigger for Vestibular disorders, epilepsy, and migraine, and Scotopic sensitivity.

Consider providing a mechanism for pausing or disabling animation, as well as using the [Reduced Motion Media Query](/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion) (or equivalent [user agent client hint](/en-US/docs/Web/HTTP/Guides/Client_hints#user_agent_client_hints)[Sec-CH-Prefers-Reduced-Motion](/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Prefers-Reduced-Motion)) to create a complimentary experience for users who have expressed a preference for no animated experiences.

- [Designing Safer Web Animation For Motion Sensitivity · An A List Apart Article](https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/)
- [An Introduction to the Reduced Motion Media Query | CSS-Tricks](https://css-tricks.com/introduction-reduced-motion-media-query/)
- [Responsive Design for Motion | WebKit](https://webkit.org/blog/7551/responsive-design-for-motion/)
- [MDN Understanding WCAG, Guideline 2.2 explanations](/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.2_%e2%80%94_enough_time_provide_users_enough_time_to_read_and_use_content)
- [Understanding Success Criterion 2.2.2 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/time-limits-pause.html)

## [Specifications](#specifications)

Specification
[Web Animations# the-animation-interface](https://drafts.csswg.org/web-animations-1/#the-animation-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Web Animations API](/en-US/docs/Web/API/Web_Animations_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/Animation/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/animation/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fanimation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FAnimation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fanimation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fad9776a6cf53eaf570ac0515402247e82ecefcfe%0A*+Document+last+modified%3A+2025-11-04T17%3A21%3A06.000Z%0A%0A%3C%2Fdetails%3E)
