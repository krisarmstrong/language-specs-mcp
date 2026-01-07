Code analysis in .NET | Microsoft Learn[Skip to main content](#main)[Skip to Ask Learn chat experience](#)

This browser is no longer supported.

 Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support. 

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881 )[More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge) Table of contents Exit editor modeAsk LearnAsk LearnFocus modeTable of contents[Read in English](#)AddAdd to plan[Edit](https://github.com/dotnet/docs/blob/main/docs/fundamentals/code-analysis/overview.md)

#### Share via

[Facebook](#)[x.com](#)[LinkedIn](#)[Email](#)Print

Note

 Access to this page requires authorization. You can try [signing in](#) or changing directories. 

 Access to this page requires authorization. You can try changing directories. 

# Overview of .NET source code analysis

Feedback Summarize this article for me 

##  In this article 

.NET compiler platform (Roslyn) analyzers inspect your C# or Visual Basic code for code quality and style issues. These analyzers are included with the .NET SDK and you don't need to install them separately. If your project targets .NET 5 or later, code analysis is enabled by default. (For information about enabling code analysis in projects that target .NET Framework, see [Enable code analysis in legacy projects](#enable-code-analysis-in-legacy-projects).)

If rule violations are found by an analyzer, they're reported as a suggestion, warning, or error, depending on how each rule is [configured](configuration-options). Code analysis violations appear with the prefix "CA" or "IDE" to differentiate them from compiler errors.

## Code quality analysis

Code quality analysis ("CAxxxx") rules inspect your C# or Visual Basic code for security, performance, design and other issues. Analysis is enabled, by default, for projects that target .NET 5 or later. You can enable code analysis on projects that target earlier .NET versions by setting the [EnableNETAnalyzers](../../core/project-sdk/msbuild-props#enablenetanalyzers) property to `true`. You can also disable code analysis for your project by setting `EnableNETAnalyzers` to `false`.

Tip

If you're using Visual Studio, many analyzer rules have associated code fixes that you can apply to automatically correct the problem. Code fixes are shown in the light bulb icon menu.

### Enabled rules

- [.NET 10](#tabpanel_1_net-10)
- [.NET 9](#tabpanel_1_net-9)
- [.NET 8](#tabpanel_1_net-8)

The following rules are enabled, by default, as errors or warnings in .NET 10. Additional rules are enabled as suggestions.

Diagnostic IDCategorySeverityVersion addedDescription[CA1416](quality-rules/ca1416)InteroperabilityWarning.NET 5Validate platform compatibility[CA1417](quality-rules/ca1417)InteroperabilityWarning.NET 5Do not use `OutAttribute` on string parameters for P/Invokes[CA1418](quality-rules/ca1418)InteroperabilityWarning.NET 6Use valid platform string[CA1420](quality-rules/ca1420)InteroperabilityWarning.NET 7Using features that require runtime marshalling when it's disabled will result in runtime exceptions[CA1422](quality-rules/ca1422)InteroperabilityWarning.NET 7Validate platform compatibility[CA1831](quality-rules/ca1831)PerformanceWarning.NET 5Use `AsSpan` instead of range-based indexers for string when appropriate[CA1856](quality-rules/ca1856)PerformanceError.NET 8Incorrect usage of `ConstantExpected` attribute[CA1857](quality-rules/ca1857)PerformanceWarning.NET 8A constant is expected for the parameter[CA2013](quality-rules/ca2013)ReliabilityWarning.NET 5Do not use `ReferenceEquals` with value types[CA2014](quality-rules/ca2014)ReliabilityWarning.NET 5Do not use `stackalloc` in loops[CA2015](quality-rules/ca2015)ReliabilityWarning.NET 5Do not define finalizers for types derived from [MemoryManager<T>](/en-us/dotnet/api/system.buffers.memorymanager-1)[CA2017](quality-rules/ca2017)ReliabilityWarning.NET 6Parameter count mismatch[CA2018](quality-rules/ca2018)ReliabilityWarning.NET 6The `count` argument to `Buffer.BlockCopy` should specify the number of bytes to copy[CA2021](quality-rules/ca2021)ReliabilityWarning.NET 8Do not call `Enumerable.Cast<T>` or `Enumerable.OfType<T>` with incompatible types[CA2022](quality-rules/ca2022)ReliabilityWarning.NET 9Avoid inexact read with `Stream.Read`[CA2023](quality-rules/ca2023)ReliabilityWarning.NET 10Invalid braces in message template[CA2200](quality-rules/ca2200)UsageWarning.NET 5Rethrow to preserve stack details[CA2247](quality-rules/ca2247)UsageWarning.NET 5Argument passed to `TaskCompletionSource` constructor should be [TaskCreationOptions](/en-us/dotnet/api/system.threading.tasks.taskcreationoptions) enum instead of [TaskContinuationOptions](/en-us/dotnet/api/system.threading.tasks.taskcontinuationoptions)[CA2252](quality-rules/ca2252)UsageError.NET 6Opt in to preview features[CA2255](quality-rules/ca2255)UsageWarning.NET 6The `ModuleInitializer` attribute should not be used in libraries[CA2256](quality-rules/ca2256)UsageWarning.NET 6All members declared in parent interfaces must have an implementation in a `DynamicInterfaceCastableImplementation`-attributed interface[CA2257](quality-rules/ca2257)UsageWarning.NET 6Members defined on an interface with the `DynamicInterfaceCastableImplementationAttribute` should be `static`[CA2258](quality-rules/ca2258)UsageWarning.NET 6Providing a `DynamicInterfaceCastableImplementation` interface in Visual Basic is unsupported[CA2259](quality-rules/ca2259)UsageWarning.NET 7`ThreadStatic` only affects static fields[CA2260](quality-rules/ca2260)UsageWarning.NET 7Use correct type parameter[CA2261](quality-rules/ca2261)UsageWarning.NET 8Do not use `ConfigureAwaitOptions.SuppressThrowing` with `Task<TResult>`[CA2264](quality-rules/ca2264)UsageWarning.NET 9Do not pass a non-nullable value to `ArgumentNullException.ThrowIfNull`[CA2265](quality-rules/ca2265)UsageWarning.NET 9Do not compare `Span<T>` to `null` or `default`

The following rules are enabled, by default, as errors or warnings in .NET 9. Additional rules are enabled as suggestions.

Diagnostic IDCategorySeverityVersion addedDescription[CA1416](quality-rules/ca1416)InteroperabilityWarning.NET 5Validate platform compatibility[CA1417](quality-rules/ca1417)InteroperabilityWarning.NET 5Do not use `OutAttribute` on string parameters for P/Invokes[CA1418](quality-rules/ca1418)InteroperabilityWarning.NET 6Use valid platform string[CA1420](quality-rules/ca1420)InteroperabilityWarning.NET 7Using features that require runtime marshalling when it's disabled will result in runtime exceptions[CA1422](quality-rules/ca1422)InteroperabilityWarning.NET 7Validate platform compatibility[CA1831](quality-rules/ca1831)PerformanceWarning.NET 5Use `AsSpan` instead of range-based indexers for string when appropriate[CA1856](quality-rules/ca1856)PerformanceError.NET 8Incorrect usage of `ConstantExpected` attribute[CA1857](quality-rules/ca1857)PerformanceWarning.NET 8A constant is expected for the parameter[CA2013](quality-rules/ca2013)ReliabilityWarning.NET 5Do not use `ReferenceEquals` with value types[CA2014](quality-rules/ca2014)ReliabilityWarning.NET 5Do not use `stackalloc` in loops[CA2015](quality-rules/ca2015)ReliabilityWarning.NET 5Do not define finalizers for types derived from [MemoryManager<T>](/en-us/dotnet/api/system.buffers.memorymanager-1)[CA2017](quality-rules/ca2017)ReliabilityWarning.NET 6Parameter count mismatch[CA2018](quality-rules/ca2018)ReliabilityWarning.NET 6The `count` argument to `Buffer.BlockCopy` should specify the number of bytes to copy[CA2021](quality-rules/ca2021)ReliabilityWarning.NET 8Do not call `Enumerable.Cast<T>` or `Enumerable.OfType<T>` with incompatible types[CA2022](quality-rules/ca2022)ReliabilityWarning.NET 9Avoid inexact read with `Stream.Read`[CA2200](quality-rules/ca2200)UsageWarning.NET 5Rethrow to preserve stack details[CA2247](quality-rules/ca2247)UsageWarning.NET 5Argument passed to `TaskCompletionSource` constructor should be [TaskCreationOptions](/en-us/dotnet/api/system.threading.tasks.taskcreationoptions) enum instead of [TaskContinuationOptions](/en-us/dotnet/api/system.threading.tasks.taskcontinuationoptions)[CA2252](quality-rules/ca2252)UsageError.NET 6Opt in to preview features[CA2255](quality-rules/ca2255)UsageWarning.NET 6The `ModuleInitializer` attribute should not be used in libraries[CA2256](quality-rules/ca2256)UsageWarning.NET 6All members declared in parent interfaces must have an implementation in a `DynamicInterfaceCastableImplementation`-attributed interface[CA2257](quality-rules/ca2257)UsageWarning.NET 6Members defined on an interface with the `DynamicInterfaceCastableImplementationAttribute` should be `static`[CA2258](quality-rules/ca2258)UsageWarning.NET 6Providing a `DynamicInterfaceCastableImplementation` interface in Visual Basic is unsupported[CA2259](quality-rules/ca2259)UsageWarning.NET 7`ThreadStatic` only affects static fields[CA2260](quality-rules/ca2260)UsageWarning.NET 7Use correct type parameter[CA2261](quality-rules/ca2261)UsageWarning.NET 8Do not use `ConfigureAwaitOptions.SuppressThrowing` with `Task<TResult>`[CA2264](quality-rules/ca2264)UsageWarning.NET 9Do not pass a non-nullable value to `ArgumentNullException.ThrowIfNull`[CA2265](quality-rules/ca2265)UsageWarning.NET 9Do not compare `Span<T>` to `null` or `default`

The following rules are enabled, by default, as errors or warnings in .NET 8. Additional rules are enabled as suggestions.

Diagnostic IDCategorySeverityVersion addedDescription[CA1416](quality-rules/ca1416)InteroperabilityWarning.NET 5Validate platform compatibility[CA1417](quality-rules/ca1417)InteroperabilityWarning.NET 5Do not use `OutAttribute` on string parameters for P/Invokes[CA1418](quality-rules/ca1418)InteroperabilityWarning.NET 6Use valid platform string[CA1420](quality-rules/ca1420)InteroperabilityWarning.NET 7Using features that require runtime marshalling when it's disabled will result in runtime exceptions[CA1422](quality-rules/ca1422)InteroperabilityWarning.NET 7Validate platform compatibility[CA1831](quality-rules/ca1831)PerformanceWarning.NET 5Use `AsSpan` instead of range-based indexers for string when appropriate[CA1856](quality-rules/ca1856)PerformanceError.NET 8Incorrect usage of `ConstantExpected` attribute[CA1857](quality-rules/ca1857)PerformanceWarning.NET 8A constant is expected for the parameter[CA2013](quality-rules/ca2013)ReliabilityWarning.NET 5Do not use `ReferenceEquals` with value types[CA2014](quality-rules/ca2014)ReliabilityWarning.NET 5Do not use `stackalloc` in loops[CA2015](quality-rules/ca2015)ReliabilityWarning.NET 5Do not define finalizers for types derived from [MemoryManager<T>](/en-us/dotnet/api/system.buffers.memorymanager-1)[CA2017](quality-rules/ca2017)ReliabilityWarning.NET 6Parameter count mismatch[CA2018](quality-rules/ca2018)ReliabilityWarning.NET 6The `count` argument to `Buffer.BlockCopy` should specify the number of bytes to copy[CA2021](quality-rules/ca2021)ReliabilityWarning.NET 8Do not call `Enumerable.Cast<T>` or `Enumerable.OfType<T>` with incompatible types[CA2200](quality-rules/ca2200)UsageWarning.NET 5Rethrow to preserve stack details[CA2247](quality-rules/ca2247)UsageWarning.NET 5Argument passed to `TaskCompletionSource` constructor should be [TaskCreationOptions](/en-us/dotnet/api/system.threading.tasks.taskcreationoptions) enum instead of [TaskContinuationOptions](/en-us/dotnet/api/system.threading.tasks.taskcontinuationoptions)[CA2252](quality-rules/ca2252)UsageError.NET 6Opt in to preview features[CA2255](quality-rules/ca2255)UsageWarning.NET 6The `ModuleInitializer` attribute should not be used in libraries[CA2256](quality-rules/ca2256)UsageWarning.NET 6All members declared in parent interfaces must have an implementation in a `DynamicInterfaceCastableImplementation`-attributed interface[CA2257](quality-rules/ca2257)UsageWarning.NET 6Members defined on an interface with the `DynamicInterfaceCastableImplementationAttribute` should be `static`[CA2258](quality-rules/ca2258)UsageWarning.NET 6Providing a `DynamicInterfaceCastableImplementation` interface in Visual Basic is unsupported[CA2259](quality-rules/ca2259)UsageWarning.NET 7`ThreadStatic` only affects static fields[CA2260](quality-rules/ca2260)UsageWarning.NET 7Use correct type parameter[CA2261](quality-rules/ca2261)UsageWarning.NET 8Do not use `ConfigureAwaitOptions.SuppressThrowing` with `Task<TResult>`

You can change the severity of these rules to disable them or elevate them to errors. You can also [enable more rules](#enable-additional-rules).

- For a list of rules that are included with each .NET SDK version, see [Analyzer releases](https://github.com/dotnet/sdk/blob/main/src/Microsoft.CodeAnalysis.NetAnalyzers/src/Microsoft.CodeAnalysis.NetAnalyzers/AnalyzerReleases.Shipped.md).
- For a list of all the code quality rules, see [Code quality rules](quality-rules/).

### Enable additional rules

Analysis mode refers to a predefined code analysis configuration where none, some, or all rules are enabled. In the default analysis mode (`Default`), only a small number of rules are [enabled as build warnings](#enabled-rules). You can change the analysis mode for your project by setting the [<AnalysisMode>](../../core/project-sdk/msbuild-props#analysismode) property in the project file. The allowable values are:

ValueDescription`None`All rules are disabled. You can selectively [opt in to](configuration-options) individual rules to enable them.`Default`Default mode, where certain rules are enabled as build warnings, certain rules are enabled as Visual Studio IDE suggestions, and the remainder are disabled.`Minimum`More aggressive mode than `Default` mode. Certain suggestions that are highly recommended for build enforcement are enabled as build warnings. To see which rules this includes, inspect the %ProgramFiles%/dotnet/sdk/[version]/Sdks/Microsoft.NET.Sdk/analyzers/build/config/analysislevel_[level]_minimum.globalconfig file. (For .NET 7 and earlier versions, the file extension is .editorconfig.)`Recommended`More aggressive mode than `Minimum` mode, where more rules are enabled as build warnings. To see which rules this includes, inspect the %ProgramFiles%/dotnet/sdk/[version]/Sdks/Microsoft.NET.Sdk/analyzers/build/config/analysislevel_[level]_recommended.globalconfig file. (For .NET 7 and earlier versions, the file extension is .editorconfig.)`All`All rules are enabled as build warnings*. You can selectively [opt out](configuration-options) of individual rules to disable them.

* The following rules are not enabled by setting `AnalysisMode` to `All` or by setting `AnalysisLevel` to `latest-all`: CA1017, CA1045, CA1005, CA1014, CA1060, CA1021, and the code metrics analyzer rules (CA1501, CA1502, CA1505, CA1506, and CA1509). These legacy rules might be deprecated in a future version. However, you can still enable them individually using a `dotnet_diagnostic.CAxxxx.severity = <severity>` entry.

You can also omit [<AnalysisMode>](../../core/project-sdk/msbuild-props#analysismode) in favor of a compound value for the `<AnalysisLevel>` property. For example, the following value enables the recommended set of rules for the latest release: `<AnalysisLevel>latest-Recommended</AnalysisLevel>`. For more information, see [AnalysisLevel](../../core/project-sdk/msbuild-props#analysislevel).

To find the default severity for each available rule and whether or not the rule is enabled in `Default` analysis mode, see the [full list of rules](https://github.com/dotnet/roslyn-analyzers/blob/main/src/NetAnalyzers/Core/AnalyzerReleases.Shipped.md).

### Treat warnings as errors

If you use the `-warnaserror` flag when you build your projects, all code analysis warnings are also treated as errors. If you do not want code quality warnings (CAxxxx) to be treated as errors in presence of `-warnaserror`, you can set the `CodeAnalysisTreatWarningsAsErrors` MSBuild property to `false` in your project file.

```
<PropertyGroup>
  <CodeAnalysisTreatWarningsAsErrors>false</CodeAnalysisTreatWarningsAsErrors>
</PropertyGroup>
```

You'll still see any code analysis warnings, but they won't break your build.

### Latest updates

By default, you'll get the latest code analysis rules and default rule severities as you upgrade to newer versions of the .NET SDK. If you don't want this behavior, for example, if you want to ensure that no new rules are enabled or disabled, you can override it in one of the following ways:

- 

Set the `AnalysisLevel` MSBuild property to a specific value to lock the warnings to that set. When you upgrade to a newer SDK, you'll still get bug fixes for those warnings, but no new warnings will be enabled and no existing warnings will be disabled. For example, to lock the set of rules to those that ship with version 8.0 of the .NET SDK, add the following entry to your project file.

```
<PropertyGroup>
  <AnalysisLevel>8.0</AnalysisLevel>
</PropertyGroup>
```

Tip

The default value for the `AnalysisLevel` property is `latest`, which means you always get the latest code analysis rules as you move to newer versions of the .NET SDK.

For more information, and to see a list of possible values, see [AnalysisLevel](../../core/project-sdk/msbuild-props#analysislevel).

- 

Install the [Microsoft.CodeAnalysis.NetAnalyzers NuGet package](https://github.com/dotnet/roslyn-analyzers#microsoftcodeanalysisnetanalyzers) to decouple rule updates from .NET SDK updates. For projects that target .NET 5+, installing the package turns off the built-in SDK analyzers. You'll get a build warning if the SDK contains a newer analyzer assembly version than that of the NuGet package. To disable the warning, set the `_SkipUpgradeNetAnalyzersNuGetWarning` property to `true`.

Note

If you install the Microsoft.CodeAnalysis.NetAnalyzers NuGet package, you should not add the [EnableNETAnalyzers](../../core/project-sdk/msbuild-props#enablenetanalyzers) property to either your project file or a Directory.Build.props file. When the NuGet package is installed and the `EnableNETAnalyzers` property is set to `true`, a build warning is generated.

## Code-style analysis

Code-style analysis ("IDExxxx") rules enable you to define and maintain consistent code style in your codebase. The default enablement settings are:

- 

Command-line build: Code-style analysis is disabled, by default, for all .NET projects on command-line builds.

You can [enable code-style analysis on build](#enable-on-build), both at the command line and inside Visual Studio. Code style violations appear as warnings or errors with an "IDE" prefix. This enables you to enforce consistent code styles at build time.

- 

Visual Studio: Code-style analysis is enabled, by default, for all .NET projects inside Visual Studio as [code refactoring quick actions](/en-us/visualstudio/ide/code-generation-in-visual-studio).

For a full list of code-style analysis rules, see [Code style rules](style-rules/).

### Enable on build

You can enable code-style analysis when building from the command-line and in Visual Studio. (However, for performance reasons, [a handful of code-style rules](https://github.com/dotnet/roslyn/blob/9f87b444da9c48a4d492b19f8337339056bf2b95/src/Analyzers/Core/Analyzers/EnforceOnBuildValues.cs#L95) will still apply only in the Visual Studio IDE.)

Follow these steps to enable code-style analysis on build:

1. 

Set the MSBuild property [EnforceCodeStyleInBuild](../../core/project-sdk/msbuild-props#enforcecodestyleinbuild) to `true`.

2. 

In an .editorconfig file, [configure](configuration-options) each "IDE" code style rule that you wish to run on build as a warning or an error. For example:

```
[*.{cs,vb}]
# IDE0040: Accessibility modifiers required (escalated to a build warning)
dotnet_diagnostic.IDE0040.severity = warning
```

Tip

Starting in .NET 9, you can also use the [option format](style-rules/language-rules#option-format) to specify a severity and have it be respected at build time. For example:

```
[*.{cs,vb}]
# IDE0040: Accessibility modifiers required (escalated to a build warning)
dotnet_style_require_accessibility_modifiers = always:warning
```

Alternatively, you can configure an entire category to be a warning or error, by default, and then selectively turn off rules in that category that you don't want to run on build. For example:

```
[*.{cs,vb}]

# Default severity for analyzer diagnostics with category 'Style' (escalated to build warnings)
dotnet_analyzer_diagnostic.category-Style.severity = warning

# IDE0040: Accessibility modifiers required (disabled on build)
dotnet_diagnostic.IDE0040.severity = silent
```

## Suppress a warning

One way to suppress a rule violation is to set the severity option for that rule ID to `none` in an EditorConfig file. For example:

```
dotnet_diagnostic.CA1822.severity = none
```

For more information and other ways to suppress warnings, see [How to suppress code analysis warnings](suppress-warnings).

## Enable code analysis in legacy projects

If your project targets .NET 5 or later, code analysis is enabled by default. If your project targets .NET Standard or .NET Framework, you must manually enable code analysis by setting the [EnableNETAnalyzers](../../core/project-sdk/msbuild-props#enablenetanalyzers) property to `true`.

If your project uses the legacy project file format, that is, it doesn't reference a [project SDK](../../core/project-sdk/overview), there are some additional steps you must take to enable code analysis:

1. Add a reference to the [📦 Microsoft.CodeAnalysis.NetAnalyzers NuGet package](https://www.nuget.org/packages/Microsoft.CodeAnalysis.NetAnalyzers).
2. Instead of setting [AnalysisLevel](../../core/project-sdk/msbuild-props#analysislevel), which isn't understood by non-SDK-style projects, add the following properties to your project file:

```
  <EffectiveAnalysisLevel>9</EffectiveAnalysisLevel>
  <AnalysisMode>Recommended</AnalysisMode>
```

## Third-party analyzers

In addition to the official .NET analyzers, you can also install third party analyzers, such as [StyleCop](https://www.nuget.org/packages/StyleCop.Analyzers/), [Roslynator](https://www.nuget.org/packages/Roslynator.Analyzers/), [Meziantou.Analyzer](https://www.nuget.org/packages/Meziantou.Analyzer/), [XUnit Analyzers](https://www.nuget.org/packages/xunit.analyzers/), and [Sonar Analyzer](https://www.nuget.org/packages/SonarAnalyzer.CSharp/).

## See also

- [Code quality analysis rule reference](quality-rules/)
- [Code style analysis rule reference](style-rules/)
- [Code analysis in Visual Studio](/en-us/visualstudio/code-quality/roslyn-analyzers-overview)
- [.NET Compiler Platform SDK](../../csharp/roslyn-sdk/)
- [Tutorial: Write your first analyzer and code fix](../../csharp/roslyn-sdk/tutorials/how-to-write-csharp-analyzer-code-fix)
- [Code analysis in ASP.NET Core apps](/en-us/aspnet/core/diagnostics/code-analysis)

 Collaborate with us on GitHub  The source for this content can be found on GitHub, where you can also create and review issues and pull requests. For more information, see [our contributor guide](https://learn.microsoft.com/contribute/content/dotnet/dotnet-contribute). 

 .NET 

[Open a documentation issue](#)[Provide product feedback](https://aka.ms/feedback/report?space=61)

## Feedback

 Was this page helpful? 

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix? 

##  Additional resources 

- Last updated on  2025-11-11 

### In this article

Was this page helpful?

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix? [en-us](#)[Your Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)Theme

-  Light 
-  Dark 
-  High contrast 

- 
- [AI Disclaimer](https://learn.microsoft.com/en-us/principles-for-ai-generated-content)
- [Previous Versions](https://learn.microsoft.com/en-us/previous-versions/)
- [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
- [Contribute](https://learn.microsoft.com/en-us/contribute)
- [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
- [Terms of Use](https://learn.microsoft.com/en-us/legal/termsofuse)
- [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
- © Microsoft 2025
