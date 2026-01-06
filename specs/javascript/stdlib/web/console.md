# console

 Baseline  Widely available 

 This feature is well established and works across many devices and browser versions. It’s been available across browsers since ⁨July 2015⁩. 

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2Fconsole&level=high)

Note: This feature is available in [Web Workers](/en-US/docs/Web/API/Web_Workers_API).

The `console` object provides access to the debugging console (e.g., the [Web console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html) in Firefox).

Implementations of the console API may differ between runtimes. In particular, some console methods may work differently or not work at all in some online editors and IDEs. To see the behavior described in this documentation, try the methods in your browser's developer tools, although even here, there are some differences between browsers.

The `console` object is available in any global scope. For example:

js

```
console.log("Failed to open the specified link");
```

## In this article

- [Instance methods](#instance_methods)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)
- [See also](#see_also)

## [Instance methods](#instance_methods)

[console.assert()](/en-US/docs/Web/API/console/assert_static)

Log an error message to console if the first argument is `false`.

[console.clear()](/en-US/docs/Web/API/console/clear_static)

Clear the console.

[console.count()](/en-US/docs/Web/API/console/count_static)

Log the number of times this line has been called with the given label.

[console.countReset()](/en-US/docs/Web/API/console/countReset_static)

Resets the value of the counter with the given label.

[console.debug()](/en-US/docs/Web/API/console/debug_static)

Outputs a message to the console with the debug log level.

[console.dir()](/en-US/docs/Web/API/console/dir_static)

Displays an interactive listing of the properties of a specified JavaScript object. This listing lets you use disclosure triangles to examine the contents of child objects.

[console.dirxml()](/en-US/docs/Web/API/console/dirxml_static)

Displays an XML/HTML Element representation of the specified object if possible or the JavaScript Object view if it is not possible.

[console.error()](/en-US/docs/Web/API/console/error_static)

Outputs a message to the console with the error log level.

[console.exception() 
Non-standard
 
Deprecated](#console.exception)

An alias for `console.error()`.

[console.group()](/en-US/docs/Web/API/console/group_static)

Creates a new inline [group](#using_groups_in_the_console), indenting all following output by another level. To move back out a level, call `console.groupEnd()`.

[console.groupCollapsed()](/en-US/docs/Web/API/console/groupCollapsed_static)

Creates a new inline [group](#using_groups_in_the_console), indenting all following output by another level. However, unlike `console.group()` this starts with the inline group collapsed requiring the use of a disclosure button to expand it. To move back out a level, call `console.groupEnd()`.

[console.groupEnd()](/en-US/docs/Web/API/console/groupEnd_static)

Exits the current inline [group](#using_groups_in_the_console).

[console.info()](/en-US/docs/Web/API/console/info_static)

Outputs a message to the console with the info log level.

[console.log()](/en-US/docs/Web/API/console/log_static)

Outputs a message to the console.

[console.profile()](/en-US/docs/Web/API/console/profile_static)Non-standard

Starts the browser's built-in profiler (for example, the [Firefox performance tool](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html)). You can specify an optional name for the profile.

[console.profileEnd()](/en-US/docs/Web/API/console/profileEnd_static)Non-standard

Stops the profiler. You can see the resulting profile in the browser's performance tool (for example, the [Firefox performance tool](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html)).

[console.table()](/en-US/docs/Web/API/console/table_static)

Displays tabular data as a table.

[console.time()](/en-US/docs/Web/API/console/time_static)

Starts a [timer](#timers) with a name specified as an input parameter. Up to 10,000 simultaneous timers can run on a given page.

[console.timeEnd()](/en-US/docs/Web/API/console/timeEnd_static)

Stops the specified [timer](#timers) and logs the elapsed time in milliseconds since it started.

[console.timeLog()](/en-US/docs/Web/API/console/timeLog_static)

Logs the value of the specified [timer](#timers) to the console.

[console.timeStamp()](/en-US/docs/Web/API/console/timeStamp_static)Non-standard

Adds a marker to the browser performance tool's timeline ([Chrome](https://developer.chrome.com/docs/devtools/performance/reference) or [Firefox](https://profiler.firefox.com/docs/#/./guide-ui-tour-timeline)).

[console.trace()](/en-US/docs/Web/API/console/trace_static)

Outputs a [stack trace](#stack_traces).

[console.warn()](/en-US/docs/Web/API/console/warn_static)

Outputs a message to the console with the warning log level.

## [Examples](#examples)

### [Outputting text to the console](#outputting_text_to_the_console)

The console's most frequently used feature is logging text and other data. There are several categories of output you can generate using the [console.log()](/en-US/docs/Web/API/console/log_static), [console.info()](/en-US/docs/Web/API/console/info_static), [console.warn()](/en-US/docs/Web/API/console/warn_static), [console.error()](/en-US/docs/Web/API/console/error_static), or [console.debug()](/en-US/docs/Web/API/console/debug_static) methods. Each of these results in output styled differently in the log, and you can use the filtering controls provided by your browser to view only the kinds of output that interest you.

There are two ways to use each of the output methods:

- Pass in a variable number of arguments whose string representations get concatenated into one string, then output to the console.
- Pass in a string containing zero or more substitution strings followed by a variable number of arguments to replace them.

#### Outputting a single object

The simplest way to use the logging methods is to output a single object:

js

```
const someObject = { str: "Some text", id: 5 };
console.log(someObject);
```

The output looks something like this:

```
{str:"Some text", id:5}
```

The browser will display as much information about the object as it can and wishes to. For example, private state of the object may be displayed too. Certain types of objects, such as DOM elements or functions, may also be displayed in a special way.

#### Snapshotting objects

Information about an object is lazily retrieved. This means that the log message shows the content of an object at the time when it's first viewed, not when it was logged. For example:

js

```
const obj = {};
console.log(obj);
obj.prop = 123;
```

This will output `{}`. However, if you expand the object's details, you will see `prop: 123`.

If you are going to mutate your object and you want to prevent the logged information from being updated, you can [deep-clone](/en-US/docs/Glossary/Deep_copy) the object before logging it. A common way is to [JSON.stringify()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) and then [JSON.parse()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) it:

js

```
console.log(JSON.parse(JSON.stringify(obj)));
```

There are other alternatives that work in browsers, such as [structuredClone()](/en-US/docs/Web/API/Window/structuredClone), which are more effective at cloning different types of objects.

#### Outputting multiple objects

You can also output multiple objects by listing them when calling the logging method, like this:

js

```
const car = "Dodge Charger";
const someObject = { str: "Some text", id: 5 };
console.info("My first car was a", car, ". The object is:", someObject);
```

The output will look like this:

```
My first car was a Dodge Charger . The object is: {str:"Some text", id:5}
```

#### Using string substitutions

The first parameter to the logging methods can be a string containing zero or more substitution strings. Each substitution string is replaced by the corresponding argument value.

[%o](#o)

Outputs a JavaScript object in the "optimally useful formatting" style, for example DOM elements may be displayed the same way as they would appear in the element inspector.

[%O](#o_2)

Outputs a JavaScript object in the "generic JavaScript object formatting" style, usually in the form of an expandable tree. This is similar to [console.dir()](/en-US/docs/Web/API/console/dir_static).

[%d or %i](#d)

Outputs an integer.

[%s](#s)

Outputs a string.

[%f](#f)

Outputs a floating-point value.

[%c](#c)

Applies CSS style rules to all following text. See [Styling console output](#styling_console_output).

Some browsers may implement additional format specifiers. For example, Safari and Firefox support the C-style precision formatting `%.<precision>f`. For example `console.log("Foo %.2f", 1.1)` will output the number to 2 decimal places: `Foo 1.10`, while `console.log("Foo %.2d", 1.1)` will output the number as two significant figures with a leading 0: `Foo 01`.

Each of these pulls the next argument after the format string off the parameter list. For example:

js

```
for (let i = 0; i < 5; i++) {
  console.log("Hello, %s. You've called me %d times.", "Bob", i + 1);
}
```

The output looks like this:

```
Hello, Bob. You've called me 1 times.
Hello, Bob. You've called me 2 times.
Hello, Bob. You've called me 3 times.
Hello, Bob. You've called me 4 times.
Hello, Bob. You've called me 5 times.
```

#### Styling console output

You can use the `%c` directive to apply a CSS style to console output:

js

```
console.log(
  "This is %cMy stylish message",
  "color: yellow; font-style: italic; background-color: blue;padding: 2px",
);
```

The text before the directive will not be affected, but the text after the directive will be styled using the CSS declarations in the parameter.

You may use `%c` multiple times:

js

```
console.log(
  "Multiple styles: %cred %corange",
  "color: red",
  "color: orange",
  "Additional unformatted message",
);
```

The properties usable along with the `%c` syntax are as follows (at least, in Firefox — they may differ in other browsers):

- [background](/en-US/docs/Web/CSS/Reference/Properties/background) and its longhand equivalents
- [border](/en-US/docs/Web/CSS/Reference/Properties/border) and its longhand equivalents
- [border-radius](/en-US/docs/Web/CSS/Reference/Properties/border-radius)
- [box-decoration-break](/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
- [box-shadow](/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
- [clear](/en-US/docs/Web/CSS/Reference/Properties/clear) and [float](/en-US/docs/Web/CSS/Reference/Properties/float)
- [color](/en-US/docs/Web/CSS/Reference/Properties/color)
- [cursor](/en-US/docs/Web/CSS/Reference/Properties/cursor)
- [display](/en-US/docs/Web/CSS/Reference/Properties/display)
- [font](/en-US/docs/Web/CSS/Reference/Properties/font) and its longhand equivalents
- [line-height](/en-US/docs/Web/CSS/Reference/Properties/line-height)
- [margin](/en-US/docs/Web/CSS/Reference/Properties/margin)
- [outline](/en-US/docs/Web/CSS/Reference/Properties/outline) and its longhand equivalents
- [padding](/en-US/docs/Web/CSS/Reference/Properties/padding)
- `text-*` properties such as [text-transform](/en-US/docs/Web/CSS/Reference/Properties/text-transform)
- [white-space](/en-US/docs/Web/CSS/Reference/Properties/white-space)
- [word-spacing](/en-US/docs/Web/CSS/Reference/Properties/word-spacing) and [word-break](/en-US/docs/Web/CSS/Reference/Properties/word-break)
- [writing-mode](/en-US/docs/Web/CSS/Reference/Properties/writing-mode)

Note: Each console message behaves like an inline element by default. If you want properties such as `padding`, `margin`, and so on to have any effect, you can set the `display` property to `display: inline-block`.

Note: In order to support both light and dark color schemes, [light-dark()](/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark) can be used when specifying colors; for example: `color: light-dark(#D00000, #FF4040);`

### [Using groups in the console](#using_groups_in_the_console)

You can use nested groups to help organize your output by visually combining related material. To create a new nested block, call `console.group()`. The `console.groupCollapsed()` method is similar but creates the new block collapsed, requiring the use of a disclosure button to open it for reading.

To exit the current group, call `console.groupEnd()`. For example, given this code:

js

```
console.log("This is the outer level");
console.group("First group");
console.log("In the first group");
console.group("Second group");
console.log("In the second group");
console.warn("Still in the second group");
console.groupEnd();
console.log("Back to the first group");
console.groupEnd();
console.debug("Back to the outer level");
```

The output looks like this:

### [Timers](#timers)

You can start a timer to calculate the duration of a specific operation. To start one, call the `console.time()` method, giving it a name as the only parameter. To stop the timer, and to get the elapsed time in milliseconds, just call the `console.timeEnd()` method, again passing the timer's name as the parameter. Up to 10,000 timers can run simultaneously on a given page.

For example, given this code:

js

```
console.time("answer time");
alert("Click to continue");
console.timeLog("answer time");
alert("Do a bunch of other stuff…");
console.timeEnd("answer time");
```

Will log the time needed by the user to dismiss the alert box, log the time to the console, wait for the user to dismiss the second alert, and then log the ending time to the console:

Notice that the timer's name is displayed both when the timer is started and when it's stopped.

### [Stack traces](#stack_traces)

The console object also supports outputting a stack trace; this will show you the call path taken to reach the point at which you call [console.trace()](/en-US/docs/Web/API/console/trace_static). Given code like this:

js

```
function foo() {
  function bar() {
    console.trace();
  }
  bar();
}

foo();
```

The output in the console looks something like this:

## [Specifications](#specifications)

Specification
[Console# console-namespace](https://console.spec.whatwg.org/#console-namespace)

## [Browser compatibility](#browser_compatibility)

## [See also](#see_also)

- [Firefox Developer Tools](https://firefox-source-docs.mozilla.org/devtools-user/index.html)
- [Web console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html) — how the Web console in Firefox handles console API calls
- [about:debugging](https://firefox-source-docs.mozilla.org/devtools-user/about_colon_debugging/index.html) — how to see console output when the debugging target is a mobile device
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/console/api/)
- [Microsoft Edge DevTools](https://learn.microsoft.com/en-us/archive/microsoft-edge/legacy/developer/)
- [Safari Web Inspector](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/Console/Console.html)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Feb 13, 2025⁩ by [MDN contributors](/en-US/docs/Web/API/console/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/console/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2Fconsole&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fconsole%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2Fconsole%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fconsole%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff19387e11b429473d515019a0b8d9ba4e615f88f%0A*+Document+last+modified%3A+2025-02-13T10%3A41%3A00.000Z%0A%0A%3C%2Fdetails%3E)
