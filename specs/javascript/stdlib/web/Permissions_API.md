Using the Permissions API to Detect How Often Users Allow or Deny Camera Accesshttps://addpipe.com/

https://addpipe.com/
- Product[Audio Recorder](https://addpipe.com/audio-recorder)[Video Recorder](https://addpipe.com/video-recorder)[Screen Recorder](https://addpipe.com/screen-recorder)[Recording Client](https://addpipe.com/recording-client)[Infrastructure](https://addpipe.com/infrastructure)[Security & Privacy](https://addpipe.com/security-and-privacy/)
- Use Cases[Legal and Compliance Recordings](https://addpipe.com/use-cases/legal-and-compliance-recordings)[Online Proctoring](https://addpipe.com/use-cases/online-proctored-exams)[Remote Identity Verification (KYC)](https://addpipe.com/use-cases/remote-identity-verification-kyc)[User-Generated Content (UGC) for Marketing](https://addpipe.com/use-cases/user-generated-content-ugc-for-marketing)[Video Interviews Resumes](https://addpipe.com/use-cases/video-interviews-resumes)
- [Pricing](https://addpipe.com/pricing)
- [About](https://addpipe.com/about)
- [Blog](https://blog.addpipe.com/)
- [Integrations](https://addpipe.com/integrations)
- [Sign in](https://dashboard.addpipe.com/signin)
- [Get Started](https://dashboard.addpipe.com/signup)

2 May 2019 / [getUserMedia](/tag/getusermedia/)

# Using the Permissions API to Detect How Often Users Allow or Deny Camera Access

9 May update: we've updated the TTA & Permission API numbers to reflect the same 100k getUserMedia() calls dataset. The updated numbers result in the same conclusions.

While building our new [getUserMedia() Logs section](https://blog.addpipe.com/getusermedia-recorder-logs/) two questions came up:

1. How often is the permissions dialog shown in Chrome and Firefox?
2. When it IS shown, how often do users deny/allow access or dismiss it altogether?

To calculate the above stats we knew exactly how many of the `getUserMedia()` attempts were denied or allowed but we did not know whether the response was the result of human interaction with the permissions dialog or an automatic response as a result of a previously given persistent permission.

The browsers (Chrome & Firefox) did not give us any obvious information so we decided to use the time passed between calling `getUserMedia()` and receiving a success or failure promise. We called this interval Time To Action.

## Using `getUserMedia()` response times to detect whether or not the permission dialog is shown

With this measurement in place, the next question was where do automatic responses end and manual interactions start? On a scale from 0 ms to 20.000 ms where do we draw the line in the sand between them?

Our first attempt at setting a limit was pretty simple: in our testing 1000ms was about the fastest we could interact with the permission dialog so we decided to consider everything below 1000ms an automatic response based on a previous allow/deny permission and consider everything above... a manual human interaction with the Chrome/Firefox permission dialog. 

But the data did not suggest such a limit existed:

This chart plots the time it takes for a `getUserMedia()`call to return any kind of response.

When plotting the response times of our last 100k `getUserMedia()` calls there's no obvious line in the sand. We hoped to see a big dip between 200-300ms (where we imagined automatic responses would end) and 1.2-1.5 seconds (where we expected manual interactions to start) but no such dip exists.

Venturing to use a 1000ms limit to distinguish between who gets the prompt and who doesn't results in the following conclusions when using the data in the graph above.

Chrome:

- 67% of the responses are under 1000ms => they're not getting the prompt. 
- 33% of the responses are above 1000ms => they're getting the prompt.

Firefox:

- 35% of the responses are under 1000ms => they're not getting the prompt. 
- 65% of the responses are above 1000ms => they're getting the prompt.

As we'll see these percentages are relatively far from the real ones.

The data does confirm the differences between Chrome's and Firefox's respective permission persistence. Chrome's permissions are persistent while Firefox's Allow permission is not persistent by default. This is why Firefox responses are heavily distributed more to the right with about 50% requests taking more than 2 seconds to resolve.

PermissionChromeFirefoxAllowpersistentnot persistentDenypersistenttemporarily persistentDismissnot persistentyou can't dismiss in Firefox

## The Permissions API

Uncertain that we could present reliable numbers we've looked for other solutions, that's when we discovered the [Permissions API](https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API).

As opposed to the binary info (prompt/no prompt) we tried to deduct above, the Permissions API gives us accurate granular information about the state of both the microphone and camera permissions BEFORE calling `getUserMedia()`. 

More exactly it gives us 3 values for each permission (camera/microphone):

- prompt: the browser has no record of a persistent permission having been given so the user will be shown a permissions dialogue
- granted: the user has previously given permission and the answer is persistent
- denied: the user has previously denied permission and the answer is persistent

On top of that the camera and microphone parts of the Permissions API [have been implemented since Chrome 64 (January 2018)](https://developer.mozilla.org/en-US/docs/Web/API/Permissions_API#Browser_compatibility) so they are now widely supported by the Chrome user base.

Here's some sample code to run in the Chrome console:

```
navigator.permissions.query({name:'camera'}).then(function(result) {
    alert(result.state);
    if (result.state === 'granted') {
        //permission has already been granted, no prompt is shown
    } else if (result.state === 'prompt') {
       //there's no peristent permission registered, will be showing the prompt
    } else if (result.state === 'denied') {
       //permission has been denied
    }
});
```

Looking at the Permissions API data from Chrome from the same 100k `getUserMedia()` calls we can confidently say that:

- only about 21% of the `getUserMedia()` calls on Chrome on our platform resulted in a prompt.This number will strongly depend on your use case. Our platform does video recordings and our clients' use case favors repeat video recordings during a session (and thus repeat `getUserMedia()` calls). End users will only be prompted for permission to access the camera and microphone once - the 1st time they use the recorder - as Chrome's permissions are persistent. 
- of those who did get the permissions prompt 10% denied access or dismissed the dialog (dismissing is possible in Chrome) resulting in a 2.3% percentage across our last 100k `getUserMedia()` calls. This number is more steady between use cases.

The 21% number we now got on Chrome is very different than the 33% we got by drawing a line in the sand at 1000ms. Big difference! The cause? Camera & microphone initialization times vary a lot as we'll see in a blog post I'm preparing.

Since launching the new [getUserMedia() Logs section](https://blog.addpipe.com/getusermedia-recorder-logs/) we've made these stats available to our users. The Pipe platform will show [in the account area](https://addpipe.com/logs):

- how often your Chrome users get to see the prompt
- how often they dismiss the dialog
- how often they deny access

Here's an example where in 12.1% of cases the dialog is shown and in 9.15% of those cases the user denies access or dismisses the dialog (1.1% out of 26799):

`getUserMedia()` stats shown in the Pipe account area

#### [Octavian](/author/octavn/)

Read [more posts](/author/octavn/) by this author.

[Read More](/author/octavn/)/webcam-tester-library/

## 

[Introducing the Webcam Tester Library: Test Webcams and Microphones
            
                Testing camera and microphone functionality in web browsers has always been a challenge for developers building video recording applications, video conferencing tools, or any web app that relies on getUserMedia. How many times](/webcam-tester-library/)

7 min read

## 

[Significant Updates to Pipe’s Terms of Service [2025]
            
                Important Update: We're Launching New, Comprehensive Terms of Service

At Pipe, we believe in clear, transparent communication. That also applies to the legal terms that govern your use of our video,](/pipe-terms-of-service-october-30th-2025/)

3 min read

## 

[Switch Your Screen Share Source Without Restarting
            
                We’ve introduced two changes to the Pipe Recording Client to make screen recording even more reliable, flexible and easier to use.

Change Shared Surface

You can now change the shared surface after](/switch-your-screen-share-source-without-restarting/)

1 min read[Deconstruct - A Blog From the Makers of Pipe](https://blog.addpipe.com)—Using the Permissions API to Detect How Often Users Allow or Deny Camera AccessShare this https://twitter.com/share?text=Using%20the%20Permissions%20API%20to%20Detect%20How%20Often%20Users%20Allow%20or%20Deny%20Camera%20Access&url=https://blog.addpipe.com/using-permissions-api-to-detect-getusermedia-responses/https://www.facebook.com/sharer/sharer.php?u=https://blog.addpipe.com/using-permissions-api-to-detect-getusermedia-responses/IT TAKES 1 MINUTESign up for a 14 Day Trial

With our 14 days (336 hours) trial you can add audio, video and screen + camera recording to your website today and explore Pipe for 2 weeks

[Get Started](https://dashboard.addpipe.com/signup)https://addpipe.com/
- 

### Main

- [Home](https://addpipe.com/)
- [Audio Recorder](https://addpipe.com/audio-recorder)
- [Video Recorder](https://addpipe.com/video-recorder)
- [Screen Recorder](https://addpipe.com/screen-recorder)
- [Recording Client](https://addpipe.com/recording-client)
- [Infrastructure](https://addpipe.com/infrastructure)
- [Security & Privacy](https://addpipe.com/security-and-privacy/)
- [Custom Development](https://addpipe.com/custom-development/)
- [Pricing](https://addpipe.com/pricing)
- 

### Account

- [Get Started](https://dashboard.addpipe.com/signup)
- [Sign In](https://dashboard.addpipe.com/signin)
- [Reset Password](https://dashboard.addpipe.com/reset-password)
- 

### Tools

- [Online Audio Recorder](https://addpipe.com/online-audio-recorder)
- [Online Video Recorder](https://addpipe.com/online-video-recorder)
- [Online Screen Recorder](https://addpipe.com/online-screen-recorder)
- [Webcam Tester](https://addpipe.com/webcam-tester/)
- [Webcam Resolution Tester](https://addpipe.com/webcam-resolution-tester/)
- 

### Developers

- [Documentation](https://addpipe.com/docs)
- [Changelog](https://changelog.addpipe.com/)
- [React Demo Integration](https://addpipe.com/react-demo/)
- [Custom UI Demo HTML](https://addpipe.com/embed-code-v2-demos/embed-html.html)
- [Custom UI Demo JavaScript](https://addpipe.com/embed-code-v2-demos/embed-javascript.html)
- [Simple Form With Video Recorder](https://addpipe.com/embed-code-v2-demos/custom-form.html)
- [Platform Status](https://addpipe.instatus.com/)
- 

### Tech Demos

- [getUserMedia Examples](https://addpipe.com/getusermedia-examples/)
- [HTML Media Capture](https://addpipe.com/html-media-capture-demo/)
- [Media Recorder API](https://addpipe.com/media-recorder-api-demo/)
- [Media Recorder API Audio](https://addpipe.com/media-recorder-api-demo-audio/)
- [getDisplayMedia Demo](https://addpipe.com/getdisplaymedia-demo/)
- [Screen + Camera Recording](https://addpipe.com/get-display-media-with-cam/)
- [Recorder.js Demo](https://addpipe.com/simple-recorderjs-demo)
- [VMSG Demo](https://addpipe.com/simple-vmsg-demo)
- [WebAudioRecorder.js Demo](https://addpipe.com/webaudiorecorder-demo/)
- [Speech to Text Demo](https://addpipe.com/web-speech-api-demo/)
- [Text to Speech Demo](https://addpipe.com/web-speech-api-text-to-speech-demo/)
- 

### Integrations

- [React NPM Package](https://www.npmjs.com/package/@addpipe/react-pipe-media-recorder)
- [WordPress](https://addpipe.com/integrations/cms/wordpress/)
- [Gravity Forms](https://addpipe.com/integrations/forms/gravity/)
- [Ninja Forms](https://addpipe.com/integrations/forms/ninjaforms3/)
- [Formstack](https://addpipe.com/integrations/forms/formstack/)
- [Alchemer](https://addpipe.com/integrations/forms/alchemer/)
- [Formsite](https://addpipe.com/integrations/forms/formsite/)
- [Squarespace](https://addpipe.com/integrations/cms/squarespace/)
- [Qualtrics](https://addpipe.com/integrations/forms/qualtrics/)
- [Wix](https://addpipe.com/integrations/cms/wix/)
- [Webflow](https://addpipe.com/integrations/cms/webflow/)
- [Bubble](https://addpipe.com/integrations/cms/bubble/)
- [OttoKit](https://ottokit.com/integrations/Pipe_Video_Recorder)
- [Zapier](https://addpipe.com/integrations/other/zapier/)
- [Nfield by Nipo](https://addpipe.com/integrations/forms/nfield/)
- 

### Transcriptions

- [Amazon Transcribe](https://addpipe.com/integrations/transcriptions/amazon/)
- [11ElevenLabs Scribe](https://addpipe.com/integrations/transcriptions/elevenlabs/)
- [OpenAI's Whisper via Replicate](https://addpipe.com/integrations/transcriptions/replicate-and-whisper/)
- 

### Company

- [Blog](https://blog.addpipe.com)
- [Privacy Policy](https://addpipe.com/03.03.2022_Privacy-PolicyEN_final.pdf)
- [Terms of Service](https://addpipe.com/terms)
- [GDPR](https://addpipe.com/gdpr)
- [Contact](https://addpipe.com/contact)
- 

### Compare

- [Ziggeo](https://addpipe.com/vs/ziggeo)
- [CameraTag](https://addpipe.com/vs/cameratag)
- 

### Get In Touch

https://x.com/piperecorderhttps://github.com/addpipehttps://www.linkedin.com/company/addpipe/ Pipe Services S.R.L. 2015-2026
