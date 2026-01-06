# GPUSupportedFeatures

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUSupportedFeatures&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `GPUSupportedFeatures` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) is a [Set-like object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis) that describes additional functionality supported by a [GPUAdapter](/en-US/docs/Web/API/GPUAdapter).

The `GPUSupportedFeatures` object for the current adapter is accessed via the [GPUAdapter.features](/en-US/docs/Web/API/GPUAdapter/features) property — use this to test what features your current setup supports. To create a [GPUDevice](/en-US/docs/Web/API/GPUDevice) with a specific feature enabled, you need to specify it in the [requiredFeatures](/en-US/docs/Web/API/GPUAdapter/requestDevice#requiredfeatures) array of the [GPUAdapter.requestDevice()](/en-US/docs/Web/API/GPUAdapter/requestDevice) descriptor.

You should note that not all features will be available to WebGPU in all browsers that support it, even if the features are supported by the underlying hardware. This could be due to constraints in the underlying system, browser, or adapter. For example:

- The underlying system might not be able to guarantee exposure of a feature in a way that is compatible with a certain browser.
- The browser vendor might not have found a secure way to implement support for that feature, or might just not have gotten round to it yet.

If you are hoping to take advantage of a specific additional feature in a WebGPU app, thorough testing is advised.

## In this article

- [Available features](#available_features)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Available features](#available_features)

The following additional features are defined in WebGPU. Bear in mind that the exact set of features available will vary across implementations and physical devices and will change over time.

Feature nameDescription`bgra8unorm-storage`When enabled, allows `STORAGE_BINDING`[usage](/en-US/docs/Web/API/GPUDevice/createTexture#usage) of `bgra8unorm`-[format](/en-US/docs/Web/API/GPUDevice/createTexture#format)[GPUTexture](/en-US/docs/Web/API/GPUTexture)s.`clip-distances`When enabled, allows the use of [clip_distances](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-clip_distances) in WGSL.`core-features-and-limits`When enabled, signifies that the [GPUAdapter](/en-US/docs/Web/API/GPUAdapter) / [GPUDevice](/en-US/docs/Web/API/GPUDevice) is able to use all core WebGPU features and limits, which allows applications to support devices with the Direct 3D 12, Metal, and Vulkan platform graphics APIs (note that Safari only supports Metal). This is also referred to as "core" WebGPU. Currently, all adapters have "core" WebGPU available, and it is enabled automatically on all devices even if not requested. This feature will enable adapters and devices to differentiate between "core" WebGPU and "compatibility mode", which will provide support for older graphics APIs (such as Direct 3D 11 and OpenGL ES) at the expense of performance and feature set.`depth-clip-control`When enabled, allows [depth-clipping](https://gpuweb.github.io/gpuweb/#depth-clipping) to be disabled. If `depth-clip-control` is enabled, the [unclippedDepth](/en-US/docs/Web/API/GPUDevice/createRenderPipeline#unclippeddepth) property is available on the `primitive` object included as part of the [createRenderPipeline()](/en-US/docs/Web/API/GPUDevice/createRenderPipeline) or [createRenderPipelineAsync()](/en-US/docs/Web/API/GPUDevice/createRenderPipelineAsync) descriptor when creating a [GPURenderPipeline](/en-US/docs/Web/API/GPURenderPipeline). `primitive` describes how a pipeline constructs and rasterizes primitives from its vertex inputs. Set `unclipped-depth` to `true` to disable depth-clipping.`depth32float-stencil8`When enabled, allows creation of textures with the format `depth32float-stencil8`. If `depth32float-stencil8` is enabled, the `depth32float-stencil8` value can be used for the [format](/en-US/docs/Web/API/GPUDevice/createTexture#format) property of the [createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture) descriptor when creating a [GPUTexture](/en-US/docs/Web/API/GPUTexture).`dual-source-blending`When enabled, allows the use of [dual_source_blending](https://gpuweb.github.io/gpuweb/wgsl/#extension-dual_source_blending) in WGSL, which uses both pixel shader outputs (`@blend_src(0)` and `@blend_src(1)`) as inputs to a blending operation with the single color attachment at `@location(0)`. Over in WebGPU, `dual-source-blending` enables the following blend factor operations (specified in the [dstFactor](/en-US/docs/Web/API/GPUDevice/createRenderPipeline#dstfactor) and [srcFactor](/en-US/docs/Web/API/GPUDevice/createRenderPipeline#srcfactor) properties of [createRenderPipeline()](/en-US/docs/Web/API/GPUDevice/createRenderPipeline) and [createRenderPipelineAsync()](/en-US/docs/Web/API/GPUDevice/createRenderPipelineAsync) descriptors): `src1`, `one-minus-src1`, `src1-alpha`, and `one-minus-src1-alpha`.`float32-blendable`When enabled, allows [blending](/en-US/docs/Web/API/GPUDevice/createRenderPipeline#blend) of `r32float`-, `rg32float`-, and `rgba32float`-[format](/en-US/docs/Web/API/GPUDevice/createTexture#format)[GPUTexture](/en-US/docs/Web/API/GPUTexture)s.`float32-filterable`When enabled, allows [filtering](/en-US/docs/Web/API/GPUDevice/createSampler#magfilter) of `r32float`-, `rg32float`-, and `rgba32float`-[format](/en-US/docs/Web/API/GPUDevice/createTexture#format)[GPUTexture](/en-US/docs/Web/API/GPUTexture)s.`indirect-first-instance`When enabled, allows the use of non-zero `firstInstance` values in the `indirectBuffer` property of the `drawIndirect()` and `drawIndexedIndirect()` methods available on [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder) and [GPURenderBundleEncoder](/en-US/docs/Web/API/GPURenderBundleEncoder) instances.`primitive-index`When enabled, allows the use of the [primitive_index](https://gpuweb.github.io/gpuweb/wgsl/#built-in-values-primitive_index) built-in variable in WGSL. This built-in input value provides a per-primitive index to fragment shaders on supported hardware, similar to the existing [vertex_index](https://gpuweb.github.io/gpuweb/wgsl/#vertex-index-builtin-value) and [instance_index](https://gpuweb.github.io/gpuweb/wgsl/#instance-index-builtin-value) built-ins. The `primitive_index` built-in variable is useful for advanced graphical techniques, such as virtualized geometry.`rg11b10ufloat-renderable`When enabled, allows `RENDER_ATTACHMENT`[usage](/en-US/docs/Web/API/GPUDevice/createTexture#usage) of `rg11b10ufloat`-[format](/en-US/docs/Web/API/GPUDevice/createTexture#format)[GPUTexture](/en-US/docs/Web/API/GPUTexture)s, as well as their blending and multisampling.`shader-f16`When enabled, allows the use of the half-precision floating-point type [f16](https://gpuweb.github.io/gpuweb/wgsl/#extension-f16) in WGSL.`subgroups`When enabled, allows the use of [subgroups](https://gpuweb.github.io/gpuweb/wgsl/#extension-subgroups) in WGSL. Subgroups enable SIMD-level parallelism, allowing threads in a workgroup to communicate and execute collective math operations such as calculating a sum of numbers, and offering an efficient method for cross-thread data sharing. Note that the [subgroupMinSize](/en-US/docs/Web/API/GPUAdapterInfo/subgroupMinSize) and [subgroupMaxSize](/en-US/docs/Web/API/GPUAdapterInfo/subgroupMaxSize) properties can be useful to check if, for example, you have a hardcoded algorithm that requires a subgroup of a certain size. You can use f16 values with subgroups when you request a GPUDevice with both the `shader-f16` and `subgroups` features.`texture-component-swizzle`When enabled, allows the [swizzle](/en-US/docs/Web/API/GPUTexture/createView#swizzle) property to be set when calling `GPUTexture.createView()`. This feature allows a texture's red, green, blue, and alpha channel values to be rearranged or replaced in a texture view when accessed by a shader.`texture-compression-bc`When enabled, allows creation of two-dimensional BC compressed textures. If `texture-compression-bc` is enabled, the following values can be used for the [format](/en-US/docs/Web/API/GPUDevice/createTexture#format) property of the [createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture) descriptor when creating a [GPUTexture](/en-US/docs/Web/API/GPUTexture): `bc1-rgba-unorm`, `bc1-rgba-unorm-srgb`, `bc2-rgba-unorm`, `bc2-rgba-unorm-srgb`, `bc3-rgba-unorm`, `bc3-rgba-unorm-srgb`, `bc4-r-unorm`, `bc4-r-snorm`, `bc5-rg-unorm`, `bc5-rg-snorm`, `bc6h-rgb-ufloat`, `bc6h-rgb-float`, `bc7-rgba-unorm`, and `bc7-rgba-unorm-srgb`.`texture-compression-bc-sliced-3d`When enabled, allows creation of three-dimensional BC compressed textures. If `texture-compression-bc-sliced-3d` is enabled, `texture-compression-bc` must also be enabled, as it enables the BC texture formats to be used (see `texture-compression-bc`, above) in the first two dimensions. `texture-compression-bc-sliced-3d` enables those same textures to be used in the third dimension.`texture-compression-astc`When enabled, allows creation of two-dimensional ASTC compressed textures. If `texture-compression-astc` is enabled, the following values can be used for the [format](/en-US/docs/Web/API/GPUDevice/createTexture#format) property of the [createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture) descriptor when creating a [GPUTexture](/en-US/docs/Web/API/GPUTexture): `astc-4x4-unorm`, `astc-4x4-unorm-srgb`, `astc-5x4-unorm`, `astc-5x4-unorm-srgb`, `astc-5x5-unorm`, `astc-5x5-unorm-srgb`, `astc-6x5-unorm`, `astc-6x5-unorm-srgb`, `astc-6x6-unorm`, `astc-6x6-unorm-srgb`, `astc-8x5-unorm`, `astc-8x5-unorm-srgb`, `astc-8x6-unorm`, `astc-8x6-unorm-srgb`, `astc-8x8-unorm`, `astc-8x8-unorm-srgb`, `astc-10x5-unorm`, `astc-10x5-unorm-srgb`, `astc-10x6-unorm`, `astc-10x6-unorm-srgb`, `astc-10x8-unorm`, `astc-10x8-unorm-srgb`, `astc-10x10-unorm`, `astc-10x10-unorm-srgb`, `astc-12x10-unorm`, `astc-12x10-unorm-srgb`, and `astc-12x12-unorm``astc-12x12-unorm-srgb`.`texture-compression-astc-sliced-3d`When enabled, allows creation of three-dimensional ASTC compressed textures. If `texture-compression-astc-sliced-3d` is enabled, `texture-compression-astc` must also be enabled, as it enables the ASTC texture formats to be used (see `texture-compression-astc`, above) in the first two dimensions. `texture-compression-astc-sliced-3d` enables those same textures to be used in the third dimension.`texture-compression-etc2`When enabled, allows creation of two-dimensional ETC2 compressed textures. If `texture-compression-etc2` is enabled, the following values can be used for the [format](/en-US/docs/Web/API/GPUDevice/createTexture#format) property of the [createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture) descriptor when creating a [GPUTexture](/en-US/docs/Web/API/GPUTexture): `etc2-rgb8unorm`, `etc2-rgb8unorm-srgb`, `etc2-rgb8a1unorm`, `etc2-rgb8a1unorm-srgb`, `etc2-rgba8unorm`, `etc2-rgba8unorm-srgb`, `eac-r11unorm`, `eac-r11snorm`, `eac-rg11unorm`, and `eac-rg11snorm`.`texture-formats-tier1`When enabled, automatically enables the `rg11b10ufloat-renderable` feature, and allows creation of [GPUTexture](/en-US/docs/Web/API/GPUTexture)s (via [GPUDevice.createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture)) with the formats specified in [Tier 1](/en-US/docs/Web/API/GPUDevice/createTexture#tier_1). The Tier 1 set of texture formats is designed to allow developers to port existing content to the web without needing to rewrite it to use WebGPU's lower capabilities.`texture-formats-tier2`When enabled, automatically enables the `rg11b10ufloat-renderable` and `texture-formats-tier1` features, and allows creation of [GPUTexture](/en-US/docs/Web/API/GPUTexture)s (via [GPUDevice.createTexture()](/en-US/docs/Web/API/GPUDevice/createTexture)) with the formats specified in [Tier 2](/en-US/docs/Web/API/GPUDevice/createTexture#tier2). The Tier 2 set of texture formats supports storage texture formats that don't have support in "core" WebGPU, and are required for advanced usage.`timestamp-query`When enabled, allows timestamp queries to be run, which measure the time taken to run compute and render passes. If `timestamp-query` is enabled, the `timestamp` value can be set for the [type](/en-US/docs/Web/API/GPUDevice/createQuerySet#type) property of the [createQuerySet()](/en-US/docs/Web/API/GPUDevice/createQuerySet) descriptor when creating a [GPUQuerySet](/en-US/docs/Web/API/GPUQuerySet). In addition, the `timestampWrites` property can be set on the [beginComputePass()](/en-US/docs/Web/API/GPUCommandEncoder/beginComputePass) and [beginRenderPass()](/en-US/docs/Web/API/GPUCommandEncoder/beginRenderPass) descriptor when creating a [GPUComputePassEncoder](/en-US/docs/Web/API/GPUComputePassEncoder) and [GPURenderPassEncoder](/en-US/docs/Web/API/GPURenderPassEncoder), respectively. `GPUQuerySet` objects are referenced within the objects included in the `timestampWrites` property, to specify where timestamps should be written to.

## [Instance properties](#instance_properties)

The following properties are available to all read-only [Set-like objects](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis) (the links below are to the [Set](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) global object reference page).

[size](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/size)

Returns the number of values in the set.

## [Instance methods](#instance_methods)

The following methods are available to all read-only [Set-like objects](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set-like_browser_apis) (the below links are to the [Set](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) global object reference page).

[has()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)

Returns a boolean asserting whether an element is present with the given value in the set or not.

[values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values)

Returns a new iterator object that yields the values for each element in the set in insertion order.

[keys()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/keys)

An alias for [values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values).

[entries()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries)

Returns a new iterator object that contains an array of `[value, value]` for each element in the set, in insertion order.

[forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)

Calls a provided callback function once for each value present in the set, in insertion order.

## [Examples](#examples)

js

```
async function init() {
  if (!navigator.gpu) {
    throw Error("WebGPU not supported.");
  }

  const adapter = await navigator.gpu.requestAdapter();
  if (!adapter) {
    throw Error("Couldn't request WebGPU adapter.");
  }

  const adapterFeatures = adapter.features;

  // Return the size of the set
  console.log(adapterFeatures.size);

  // Check whether a feature is supported by the adapter
  console.log(adapterFeatures.has("texture-compression-astc"));

  // Iterate through all the set values using values()
  const valueIterator = adapterFeatures.values();
  for (const value of valueIterator) {
    console.log(value);
  }

  // Iterate through all the set values using keys()
  const keyIterator = adapterFeatures.keys();
  for (const value of keyIterator) {
    console.log(value);
  }

  // Iterate through all the set values using entries()
  const entryIterator = adapterFeatures.entries();
  for (const entry of entryIterator) {
    console.log(entry[0]);
  }

  // Iterate through all the set values using forEach()
  adapterFeatures.forEach((value) => {
    console.log(value);
  });

  // …
}
```

## [Specifications](#specifications)

Specification
[WebGPU# gpusupportedfeatures](https://gpuweb.github.io/gpuweb/#gpusupportedfeatures)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- The [WebGPU API](/en-US/docs/Web/API/WebGPU_API)
- The specification [Feature Index](https://gpuweb.github.io/gpuweb/#feature-index)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Nov 21, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/GPUSupportedFeatures/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/gpusupportedfeatures/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUSupportedFeatures&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fgpusupportedfeatures%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FGPUSupportedFeatures%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fgpusupportedfeatures%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8d8030c3bc728b1318b5147bc99bf5e6c24c75b9%0A*+Document+last+modified%3A+2025-11-21T19%3A03%3A12.000Z%0A%0A%3C%2Fdetails%3E)
