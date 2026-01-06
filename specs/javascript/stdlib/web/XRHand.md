# XRHand

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRHand&level=not)

The `XRHand` interface is pair iterator (an ordered map) with the key being the hand joints and the value being an [XRJointSpace](/en-US/docs/Web/API/XRJointSpace).

`XRHand` is returned by [XRInputSource.hand](/en-US/docs/Web/API/XRInputSource/hand).

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Hand joints](#hand_joints)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[size Read only 
Experimental](#size)

Returns `25`, the size of the pair iterator.

## [Instance methods](#instance_methods)

The `XRHand` object is a pair iterator. It can directly be used in a [for...of](/en-US/docs/Web/JavaScript/Reference/Statements/for...of) structure. `for (const joint of myHand)` is equivalent to `for (const joint of myHand.entries())`. However, it's not a map-like object, so you don't have the `clear()`, `delete()`, `has()`, and `set()` methods.

[entries() 
Experimental](#entries)

Returns an iterator with the hand joints/[XRJointSpace](/en-US/docs/Web/API/XRJointSpace) pairs for each element. See [Map.prototype.entries()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/entries) for more details.

[forEach() 
Experimental](#foreach)

Runs a provided function once per each hand joint/[XRJointSpace](/en-US/docs/Web/API/XRJointSpace) pair. See [Map.prototype.forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/forEach) for more details.

[get() 
Experimental](#get)

Returns a [XRJointSpace](/en-US/docs/Web/API/XRJointSpace) for a given hand joint or [undefined](/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) if no such hand joint key is in the map. See [Map.prototype.get()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/get) for more details.

[keys() 
Experimental](#keys)

Returns an iterator with all the hand joint keys. See [Map.prototype.keys()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/keys) for more details.

[values() 
Experimental](#values)

Returns an iterator with all the [XRJointSpace](/en-US/docs/Web/API/XRJointSpace) values. See [Map.prototype.values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/values) for more details.

## [Hand joints](#hand_joints)

The `XRHand` object contains the following hand joints:

Hand jointIndexwrist0thumb-metacarpal1thumb-phalanx-proximal2thumb-phalanx-distal3thumb-tip4index-finger-metacarpal5index-finger-phalanx-proximal6index-finger-phalanx-intermediate7index-finger-phalanx-distal8index-finger-tip9middle-finger-metacarpal10middle-finger-phalanx-proximal11middle-finger-phalanx-intermediate12middle-finger-phalanx-distal13middle-finger-tip14ring-finger-metacarpal15ring-finger-phalanx-proximal16ring-finger-phalanx-intermediate17ring-finger-phalanx-distal18ring-finger-tip19pinky-finger-metacarpal20pinky-finger-phalanx-proximal21pinky-finger-phalanx-intermediate22pinky-finger-phalanx-distal23pinky-finger-tip24

## [Examples](#examples)

### [Using XRHand objects](#using_xrhand_objects)

js

```
const wristJoint = inputSource.hand.get("wrist");
const indexFingerTipJoint = inputSource.hand.get("index-finger-tip");

for (const [joint, jointSpace] of inputSource.hand) {
  console.log(joint);
  console.log(jointSpace);
}
```

## [Specifications](#specifications)

Specification
[WebXR Hand Input Module - Level 1# xrhand-interface](https://immersive-web.github.io/webxr-hand-input/#xrhand-interface)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [XRInputSource.hand](/en-US/docs/Web/API/XRInputSource/hand)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Apr 28, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/XRHand/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrhand/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRHand&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrhand%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRHand%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrhand%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbe1922d62a0d31e4e3441db0e943aed8df736481%0A*+Document+last+modified%3A+2025-04-28T14%3A28%3A26.000Z%0A%0A%3C%2Fdetails%3E)
