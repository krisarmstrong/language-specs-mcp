# HMDVRDevice

Deprecated: This feature is no longer recommended. Though some browsers might still support it, it may have already been removed from the relevant web standards, may be in the process of being dropped, or may only be kept for compatibility purposes. Avoid using it, and update existing code if possible; see the [compatibility table](#browser_compatibility) at the bottom of this page to guide your decision. Be aware that this feature may cease to work at any time.

Non-standard: This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The `HMDVRDevice` interface of the [WebVR API](/en-US/docs/Web/API/WebVR_API) represents a head mounted display, providing access to information about each eye, and allowing us to modify the current field of view.

## In this article

- [Instance methods](#instance_methods)
- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[HMDVRDevice.getEyeParameters()](/en-US/docs/Web/API/HMDVRDevice/getEyeParameters)DeprecatedNon-standard

Returns current parameters for the eye specified as its argument ("left" or "right") — such as field of view information — stored in a [VREyeParameters](/en-US/docs/Web/API/VREyeParameters) object.

[HMDVRDevice.setFieldOfView()](/en-US/docs/Web/API/HMDVRDevice/setFieldOfView)DeprecatedNon-standard

Sets the field of view for both eyes.

## [Instance properties](#instance_properties)

This interface doesn't define any properties of its own, but it does inherit the properties of its parent interface, [VRDisplay](/en-US/docs/Web/API/VRDisplay).

[VRDisplay.hardwareUnitId Read only](#vrdisplay.hardwareunitid)

Returns the distinct hardware ID for the overall hardware unit that this `VRDevice` is a part of. All devices that are part of the same physical piece of hardware will have the same `hardwareUnitId`.

[VRDisplay.displayId](/en-US/docs/Web/API/VRDisplay/displayId)Read only

Returns the ID for this specific `VRDevice`. The ID shouldn't change across browser restarts, allowing configuration data to be saved based on it.

[VRDisplay.displayName](/en-US/docs/Web/API/VRDisplay/displayName)Read only

A human-readable name to identify the `VRDevice`.

## [Examples](#examples)

The following example, taken from the WebVR spec, finds the first available `HMDVRDevice` and its associated [PositionSensorVRDevice](/en-US/docs/Web/API/PositionSensorVRDevice), if it has one.

js

```
navigator.getVRDevices().then((devices) => {
  for (const device of devices) {
    if (device instanceof HMDVRDevice) {
      gHMD = device;
      break;
    }
  }

  if (gHMD) {
    for (const device of devices) {
      if (
        device instanceof PositionSensorVRDevice &&
        device.hardwareUnitId === gHMD.hardwareUnitId
      ) {
        gPositionSensor = devices[i];
        break;
      }
    }
  }
});
```

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebVR API](/en-US/docs/Web/API/WebVR_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Dec 18, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/HMDVRDevice/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/hmdvrdevice/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHMDVRDevice&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fhmdvrdevice%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FHMDVRDevice%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fhmdvrdevice%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fccbc5d4100e0a5de844e060b025883ef1611d7b8%0A*+Document+last+modified%3A+2023-12-18T13%3A22%3A57.000Z%0A%0A%3C%2Fdetails%3E)
