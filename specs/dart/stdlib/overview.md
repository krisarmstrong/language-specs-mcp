Dart - Dart API docsmenu

1. [Dart SDK](https://github.com/dart-lang/sdk)

Dart dark_mode  light_mode 

# Welcome!

Welcome to the Dart API reference documentation, covering the [Dart core libraries](https://dart.dev/guides/libraries). These include:

- [dart:core](dart-core/dart-core-library.html): Core functionality such as strings, numbers, collections, errors, dates, and URIs.
- [dart:io](dart-io/dart-io-library.html): I/O for non-web apps.
- [dart:async](dart-async/dart-async-library.html): Functionality for asynchronous programming with futures, streams, and zones.

You'll also find reference documentation covering Dart's various platform interoperability options, such as:

- [dart:js_interop](dart-js_interop/dart-js_interop-library.html): Library including a sound type hierarchy and helper functions for interoperability with JavaScript.
- [package:web](https://pub.dev/documentation/web): DOM manipulation for web apps.
- [dart:ffi](dart-ffi/dart-ffi-library.html): Foreign function interfaces for interoperability with the C language.

The core libraries - except for `dart:core` - must be imported before they're available for use:

```
import 'dart:math';
```

Additionally, you can find Dart packages at [pub.dev](https://pub.dev).

## Language docs

The main site for learning and using Dart is [dart.dev](https://dart.dev). Check out these pages:

- [Dart overview](https://dart.dev/overview)
- [Dart language documentation](https://dart.dev/language)
- [Library tour](https://dart.dev/libraries)
- [Tutorials](https://dart.dev/tutorials)

This API reference is generated from the SDK source at [dart-lang/sdk](https://github.com/dart-lang/sdk). If you'd like to give feedback on or edit this documentation, see [Contributing](https://github.com/dart-lang/sdk/blob/main/CONTRIBUTING.md).

## Libraries

### Core

[dart:async](dart-async/)Support for asynchronous programming, with classes such as Future and Stream. [dart:collection](dart-collection/)Classes and utilities that supplement the collection support in dart:core. [dart:convert](dart-convert/)Encoders and decoders for converting between different data representations, including JSON and UTF-8. [dart:core](dart-core/)Built-in types, collections, and other core functionality for every Dart program. [dart:developer](dart-developer/)Interact with developer tools such as the debugger and inspector. [dart:math](dart-math/)Mathematical constants and functions, plus a random number generator. [dart:typed_data](dart-typed_data/)Lists that efficiently handle fixed sized data (for example, unsigned 8 byte integers) and SIMD numeric types. 

### VM

[dart:ffi](dart-ffi/)Foreign Function Interface for interoperability with the C programming language. [dart:io](dart-io/)File, socket, HTTP, and other I/O support for non-web applications. [dart:isolate](dart-isolate/)Concurrent programming using isolates: independent workers that are similar to threads but don't share memory, communicating only via messages. [dart:mirrors](dart-mirrors/)Basic reflection in Dart, with support for introspection and dynamic invocation. 

### Web

[package:web
                  open_in_new](https://pub.dev/documentation/web/latest/)This package exposes browser APIs. It's intended to replace dart:html and similar Dart SDK libraries. It will support access to browser APIs from Dart code compiled to either JavaScript or WebAssembly.[dart:js_interop](dart-js_interop/)Interoperability, "interop" for short, with JavaScript and browser APIs. [dart:js_interop_unsafe](dart-js_interop_unsafe/)Utility methods to manipulate JavaScript objects dynamically. 

### Web (Legacy)

[dart:html](dart-html/)HTML elements and other resources for web-based applications that need to interact with the browser and the DOM (Document Object Model). [dart:indexed_db](dart-indexed_db/)A client-side key-value store with support for indexes. [dart:js](dart-js/)Low-level support for interoperating with JavaScript. [dart:js_util](dart-js_util/)Utility methods to manipulate `package:js` annotated JavaScript interop objects in cases where the name to call is not known at runtime. [dart:svg](dart-svg/)Scalable Vector Graphics: Two-dimensional vector graphics with support for events and animation. [dart:web_audio](dart-web_audio/)High-fidelity audio programming in the browser. [dart:web_gl](dart-web_gl/)3D programming in the browser. 

1. [Dart SDK](https://github.com/dart-lang/sdk)

##### DartSDK

1. Libraries
2. Core
3. [dart:async](dart-async/)
4. [dart:collection](dart-collection/)
5. [dart:convert](dart-convert/)
6. [dart:core](dart-core/)
7. [dart:developer](dart-developer/)
8. [dart:math](dart-math/)
9. [dart:typed_data](dart-typed_data/)
10. VM
11. [dart:ffi](dart-ffi/)
12. [dart:io](dart-io/)
13. [dart:isolate](dart-isolate/)
14. [dart:mirrors](dart-mirrors/)
15. Web
16. [package:web
            open_in_new](https://pub.dev/documentation/web/latest/)
17. [dart:js_interop](dart-js_interop/)
18. [dart:js_interop_unsafe](dart-js_interop_unsafe/)
19. Web (Legacy)
20. [dart:html](dart-html/)
21. [dart:indexed_db](dart-indexed_db/)
22. [dart:js](dart-js/)
23. [dart:js_util](dart-js_util/)
24. [dart:svg](dart-svg/)
25. [dart:web_audio](dart-web_audio/)
26. [dart:web_gl](dart-web_gl/)

 Dart 3.10.7  | [Terms](https://dart.dev/terms) | [Privacy](https://policies.google.com/privacy) | [Security](https://dart.dev/security) Except as otherwise noted, this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) and code samples are licensed under the [3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause) Cookies management controls
