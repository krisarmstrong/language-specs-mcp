# WGSLLanguageFeatures

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWGSLLanguageFeatures&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `WGSLLanguageFeatures` interface of the [WebGPU API](/en-US/docs/Web/API/WebGPU_API) is a [setlike](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) object that reports the [WGSL language extensions](https://gpuweb.github.io/gpuweb/wgsl/#language-extension) supported by the WebGPU implementation.

The `WGSLLanguageFeatures` object is accessed via the [GPU.wgslLanguageFeatures](/en-US/docs/Web/API/GPU/wgslLanguageFeatures) property.

Note: Not all WGSL language extensions are available to WebGPU in all browsers that support the API. We recommend you thoroughly test any extensions you choose to use.

## In this article

- [Available features](#available_features)
- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Available features](#available_features)

The following WGSL language extensions are defined at [WGSL language extensions](https://gpuweb.github.io/gpuweb/wgsl/#language-extension) in the WGSL specification. Bear in mind that the exact set of features available will vary across implementations and physical devices, and may change over time.

[packed_4x8_integer_dot_product](#packed_4x8_integer_dot_product)

Allows DP4a (Dot Product of 4 Elements and Accumulate) GPU instructions to be used via your WGSL code. These efficiently perform 8-bit integer dot products to accelerate computation, saving memory and network bandwidth and improving performance compared with the equivalent `f32` versions. They are commonly used in machine learning models in inferencing, within AI frameworks.

Specifically, when `packed_4x8_integer_dot_product` is available, WGSL code can use:

- 32-bit integer scalars packing 4-component vectors of 8-bit integers to be used as inputs to dot product instructions (via the `dot4U8Packed()` and `dot4I8Packed()` built-in functions).
- Packing and unpacking instructions with packed 4-component vectors of 8-bit integers (via built-in functions such as `pack4xI8()` and `pack4xI8Clamp()`).

[pointer_composite_access](#pointer_composite_access)

Enables WGSL shader code to access components of complex data types using the same dot (`.`) syntax whether you're working directly with the data or with a pointer to it.

When `pointer_composite_access` is available:

- If `foo` is a pointer: `foo.bar` is available as a more convenient way to write `(*foo).bar`. The asterisk (`*`) would normally be needed to turn the pointer into a "reference" that can be dereferenced, but now both pointers and references are almost interchangeable.
- If `foo` is not a pointer: The dot (`.`) operator works exactly as you're used to for directly accessing members.
- if `pa` is a pointer that stores the starting address of an array, then `pa[i]` gives you direct access to the memory location where the `i`th element of that array is stored.

See [Syntax sugar for dereferencing composites in WGSL](https://developer.chrome.com/blog/new-in-webgpu-123#syntax_sugar_for_dereferencing_composites_in_wgsl) for further details and an example.

[readonly_and_readwrite_storage_textures](#readonly_and_readwrite_storage_textures)

When available, allows the `"read-only"` and `"read-write"`[storageTexture.access](/en-US/docs/Web/API/GPUDevice/createBindGroupLayout#access) values to be set when specifying storage texture bind group entry types in a bind group layout. These enable WGSL code to read storage textures, and read/write storage textures, respectively.

[unrestricted_pointer_parameters](#unrestricted_pointer_parameters)

Loosens restrictions on pointers being passed to WGSL functions. When available, the following are allowed:

- 

Parameter pointers to storage, uniform, and workgroup address spaces being passed to user-declared functions.

- 

Pointers to structure members and array elements being passed to user-declared functions.

See [Pointers As Function Parameters](https://google.github.io/tour-of-wgsl/types/pointers/passing_pointers/) for more details.

## [Instance properties](#instance_properties)

The following property is available to all read-only [setlike](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) objects:

[size](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/size)

Returns the number of values in the set.

## [Instance methods](#instance_methods)

The following methods are available to all read-only [setlike](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) objects:

[has()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)

Returns a boolean asserting whether or not an element with the given value is present in the set.

[values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values)

Returns a new iterator object that yields values for each element in the set in insertion order.

[keys()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/keys)

An alias for [values()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/values).

[entries()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/entries)

Returns a new iterator object that contains an array of `[value, value]` for each element in the set in insertion order.

[forEach()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)

Calls the provided callback function once for each value present in the set in insertion order.

## [Examples](#examples)

### [Check whether an extension is available](#check_whether_an_extension_is_available)

js

```
if (
  navigator.gpu.wgslLanguageFeatures.has(
    "readonly_and_readwrite_storage_textures",
  )
) {
  console.log("Read-only and read-write storage textures are available");
}
```

### [Return set size and iterate through values](#return_set_size_and_iterate_through_values)

js

```
const wgslFeatures = navigator.gpu.wgslLanguageFeatures;

// Return the size of the set
console.log(wgslFeatures.size);

// Iterate through all the set values using values()
const valueIterator = wgslFeatures.values();
for (const value of valueIterator) {
  console.log(value);
}

// …
```

## [Specifications](#specifications)

Specification
[WebGPU# gpuwgsllanguagefeatures](https://gpuweb.github.io/gpuweb/#gpuwgsllanguagefeatures)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [WebGPU API](/en-US/docs/Web/API/WebGPU_API)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 1, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/WGSLLanguageFeatures/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/wgsllanguagefeatures/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWGSLLanguageFeatures&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fwgsllanguagefeatures%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWGSLLanguageFeatures%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fwgsllanguagefeatures%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F84ba257fb5e776926bb6dda340b0aa88300246b3%0A*+Document+last+modified%3A+2025-07-01T12%3A37%3A02.000Z%0A%0A%3C%2Fdetails%3E)
