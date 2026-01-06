# TextMetrics

 Baseline  Widely available  * 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

* Some parts of this feature may have varying levels of support.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextMetrics&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `TextMetrics` interface represents the dimensions of a piece of text in the canvas; a `TextMetrics` instance can be retrieved using the [CanvasRenderingContext2D.measureText()](/en-US/docs/Web/API/CanvasRenderingContext2D/measureText) method.

## In this article

- [Instance properties](#instance_properties)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance properties](#instance_properties)

[TextMetrics.width](/en-US/docs/Web/API/TextMetrics/width)Read only

Returns the width of a segment of inline text in CSS pixels. It takes into account the current font of the context.

[TextMetrics.actualBoundingBoxLeft](/en-US/docs/Web/API/TextMetrics/actualBoundingBoxLeft)Read only

Distance parallel to the baseline from the alignment point given by the [CanvasRenderingContext2D.textAlign](/en-US/docs/Web/API/CanvasRenderingContext2D/textAlign) property to the left side of the bounding rectangle of the given text, in CSS pixels; positive numbers indicating a distance going left from the given alignment point.

[TextMetrics.actualBoundingBoxRight](/en-US/docs/Web/API/TextMetrics/actualBoundingBoxRight)Read only

Returns the distance from the alignment point given by the [CanvasRenderingContext2D.textAlign](/en-US/docs/Web/API/CanvasRenderingContext2D/textAlign) property to the right side of the bounding rectangle of the given text, in CSS pixels. The distance is measured parallel to the baseline.

[TextMetrics.fontBoundingBoxAscent](/en-US/docs/Web/API/TextMetrics/fontBoundingBoxAscent)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) attribute to the top of the highest bounding rectangle of all the fonts used to render the text, in CSS pixels.

[TextMetrics.fontBoundingBoxDescent](/en-US/docs/Web/API/TextMetrics/fontBoundingBoxDescent)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) attribute to the bottom of the bounding rectangle of all the fonts used to render the text, in CSS pixels.

[TextMetrics.actualBoundingBoxAscent](/en-US/docs/Web/API/TextMetrics/actualBoundingBoxAscent)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) attribute to the top of the bounding rectangle used to render the text, in CSS pixels.

[TextMetrics.actualBoundingBoxDescent](/en-US/docs/Web/API/TextMetrics/actualBoundingBoxDescent)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) attribute to the bottom of the bounding rectangle used to render the text, in CSS pixels.

[TextMetrics.emHeightAscent](/en-US/docs/Web/API/TextMetrics/emHeightAscent)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) property to the top of the em square in the line box, in CSS pixels.

[TextMetrics.emHeightDescent](/en-US/docs/Web/API/TextMetrics/emHeightDescent)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) property to the bottom of the em square in the line box, in CSS pixels.

[TextMetrics.hangingBaseline](/en-US/docs/Web/API/TextMetrics/hangingBaseline)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) property to the hanging baseline of the line box, in CSS pixels.

[TextMetrics.alphabeticBaseline](/en-US/docs/Web/API/TextMetrics/alphabeticBaseline)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) property to the [alphabetic baseline](/en-US/docs/Glossary/Baseline/Typography) of the line box, in CSS pixels.

[TextMetrics.ideographicBaseline](/en-US/docs/Web/API/TextMetrics/ideographicBaseline)Read only

Returns the distance from the horizontal line indicated by the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) property to the ideographic baseline of the line box, in CSS pixels.

## [Examples](#examples)

### [Baselines illustrated](#baselines_illustrated)

This example demonstrates the baselines the `TextMetrics` object holds. The default baseline is the `alphabeticBaseline`. See also the [CanvasRenderingContext2D.textBaseline](/en-US/docs/Web/API/CanvasRenderingContext2D/textBaseline) property.

#### HTML

html

```
<canvas id="canvas" width="550" height="500"></canvas>
```

#### JavaScript

js

```
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const baselinesAboveAlphabetic = [
  "fontBoundingBoxAscent",
  "actualBoundingBoxAscent",
  "emHeightAscent",
  "hangingBaseline",
];
const baselinesBelowAlphabetic = [
  "ideographicBaseline",
  "emHeightDescent",
  "actualBoundingBoxDescent",
  "fontBoundingBoxDescent",
];
const baselines = [...baselinesAboveAlphabetic, ...baselinesBelowAlphabetic];
ctx.font = "25px serif";
ctx.strokeStyle = "red";

baselines.forEach((baseline, index) => {
  const text = `Abcdefghijklmnop (${baseline})`;
  const textMetrics = ctx.measureText(text);
  const y = 50 + index * 50;
  ctx.beginPath();
  ctx.fillText(text, 0, y);

  const baselineMetricValue = textMetrics[baseline];
  if (baselineMetricValue === undefined) {
    return;
  }

  const lineY = baselinesBelowAlphabetic.includes(baseline)
    ? y + Math.abs(baselineMetricValue)
    : y - Math.abs(baselineMetricValue);
  ctx.moveTo(0, lineY);
  ctx.lineTo(550, lineY);
  ctx.stroke();
});
```

#### Result

### [Measuring text width](#measuring_text_width)

When measuring the x-direction of a piece of text, the sum of `actualBoundingBoxLeft` and `actualBoundingBoxRight` can be wider than the width of the inline box (`width`), due to slanted/italic fonts where characters overhang their advance width.

It can therefore be useful to use the sum of `actualBoundingBoxLeft` and `actualBoundingBoxRight` as a more accurate way to get the absolute text width:

js

```
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const text = "Abcdefghijklmnop";
ctx.font = "italic 50px serif";
const textMetrics = ctx.measureText(text);

console.log(textMetrics.width);
// 459.8833312988281

console.log(
  textMetrics.actualBoundingBoxRight + textMetrics.actualBoundingBoxLeft,
);
// 462.8833333333333
```

## [Specifications](#specifications)

Specification
[HTML# textmetrics](https://html.spec.whatwg.org/multipage/canvas.html#textmetrics)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- Creator method in [CanvasRenderingContext2D](/en-US/docs/Web/API/CanvasRenderingContext2D)
- The [<canvas>](/en-US/docs/Web/HTML/Reference/Elements/canvas) element and its associated interface, [HTMLCanvasElement](/en-US/docs/Web/API/HTMLCanvasElement)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 4, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/TextMetrics/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/textmetrics/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextMetrics&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Ftextmetrics%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FTextMetrics%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Ftextmetrics%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0a4d5b451cc54599ed2b99cef4fdd39c3fd96a3d%0A*+Document+last+modified%3A+2025-02-04T21%3A56%3A27.000Z%0A%0A%3C%2Fdetails%3E)
