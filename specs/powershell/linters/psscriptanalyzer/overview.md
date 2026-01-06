Table of contents Exit editor modeAsk LearnAsk LearnFocus modeTable of contents[Read in English](#)AddAdd to plan[Edit](https://github.com/MicrosoftDocs/PowerShell-Docs-Modules/blob/main/reference/docs-conceptual/PSScriptAnalyzer/overview.md)

#### Share via

[Facebook](#)[x.com](#)[LinkedIn](#)[Email](#)Print

Note

 Access to this page requires authorization. You can try [signing in](#) or changing directories. 

 Access to this page requires authorization. You can try changing directories. 

# PSScriptAnalyzer module

Feedback Summarize this article for me 

##  In this article 

PSScriptAnalyzer is a static code checker for PowerShell modules and scripts. PSScriptAnalyzer checks the quality of PowerShell code by running a set of rules. The rules are based on PowerShell best practices identified by PowerShell Team and the community. It generates DiagnosticResults (errors and warnings) to inform users about potential code defects and suggests possible solutions for improvements.

PSScriptAnalyzer ships with a collection of built-in rules that check various aspects of PowerShell code such as:

- The presence of uninitialized variables
- Use of PSCredential type
- Use of `Invoke-Expression`
- And many more

You can choose the rules to include or exclude for your modules and scripts. PSScriptAnalyzer can also fix the formatting of your code. This helps you produce code that conforms to a standard style, is easier to read, and is more maintainable.

## Installing PSScriptAnalyzer

Supported PowerShell Versions and Platforms

- Windows PowerShell 5.1 or greater
- PowerShell 7.2.11 or greater on Windows/Linux/macOS

Install using PowerShellGet 2.x:

```
Install-Module -Name PSScriptAnalyzer -Force
```

Install using PSResourceGet 1.x:

```
Install-PSResource -Name PSScriptAnalyzer -Reinstall
```

The `-Force` or `-Reinstall` parameters are only necessary when you have an older version of PSScriptAnalyzer installed. These parameters also work even when you don't have a previous version installed.

 Collaborate with us on GitHub  The source for this content can be found on GitHub, where you can also create and review issues and pull requests. For more information, see [our contributor guide](https://learn.microsoft.com/powershell/scripting/community/contributing/powershell-style-guide). 

 PowerShell 

[Open a documentation issue](#)[Provide product feedback](https://github.com/PowerShell/PSScriptAnalyzer/issues/new/choose)

## Feedback

 Was this page helpful? 

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix? 

##  Additional resources 

- Last updated on  2024-10-10
