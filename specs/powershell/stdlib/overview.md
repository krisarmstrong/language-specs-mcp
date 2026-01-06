Table of contents Exit editor modeAsk LearnAsk LearnFocus modeTable of contents[Read in English](#)AddAdd to plan[Edit](https://github.com/MicrosoftDocs/PowerShell-Docs/blob/main/reference/docs-conceptual/overview.md)

#### Share via

[Facebook](#)[x.com](#)[LinkedIn](#)[Email](#)Print

Note

 Access to this page requires authorization. You can try [signing in](#) or changing directories. 

 Access to this page requires authorization. You can try changing directories. 

# What is PowerShell?

Feedback Summarize this article for me 

##  In this article 

PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. PowerShell runs on Windows, Linux, and macOS.

## Command-line Shell

PowerShell is a modern command shell that includes the best features of other popular shells. Unlike most shells that only accept and return text, PowerShell accepts and returns .NET objects. The shell includes the following features:

- Robust command-line [history](/en-us/powershell/module/microsoft.powershell.core/about/about_history)
- Tab completion and command prediction (See [about_PSReadLine](/en-us/powershell/module/psreadline/about/about_psreadline))
- Supports command and parameter [aliases](/en-us/powershell/module/microsoft.powershell.core/about/about_aliases)
- [Pipeline](/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines) for chaining commands
- In-console [help](/en-us/powershell/module/microsoft.powershell.core/get-help) system, similar to Unix `man` pages

## Scripting language

As a scripting language, PowerShell is commonly used for automating the management of systems. It's also used to build, test, and deploy solutions, often in CI/CD environments. PowerShell is built on the .NET Common Language Runtime (CLR). All inputs and outputs are .NET objects. No need to parse text output to extract information from output. The PowerShell scripting language includes the following features:

- Extensible through [functions](/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced), [classes](/en-us/powershell/module/microsoft.powershell.core/about/about_classes), [scripts](/en-us/powershell/module/microsoft.powershell.core/about/about_scripts), and [modules](/en-us/powershell/module/microsoft.powershell.core/about/about_modules)
- Extensible [formatting system](/en-us/powershell/module/microsoft.powershell.core/about/about_format.ps1xml) for easy output
- Extensible [type system](/en-us/powershell/module/microsoft.powershell.core/about/about_types.ps1xml) for creating dynamic types
- Built-in support for common data formats like [CSV](/en-us/powershell/module/microsoft.powershell.utility/convertfrom-csv), [JSON](/en-us/powershell/module/microsoft.powershell.utility/convertfrom-json), and [XML](/en-us/powershell/module/microsoft.powershell.utility/convertto-xml)

## Automation platform

The extensible nature of PowerShell provides an ecosystem of PowerShell modules to deploy and manage almost any technology you work with. For example:

Microsoft modules

- [Azure](/en-us/powershell/azure)
- [Windows](/en-us/powershell/windows/get-started)
- [Exchange](/en-us/powershell/exchange/exchange-management-shell)
- [SQL](/en-us/sql/powershell/sql-server-powershell)

Third-party modules

- [AWS](https://aws.amazon.com/powershell/)
- [VMware](https://developer.broadcom.com/powercli)
- [Google Cloud](https://cloud.google.com/powershell/)

### Configuration management

PowerShell Desired State Configuration ([DSC](/en-us/powershell/scripting/dsc/overview/dscforengineers)) is a management framework in PowerShell that enables you to manage your enterprise infrastructure with configuration as code. With DSC, you can:

- Create declarative [configurations](/en-us/powershell/scripting/dsc/configurations/configurations) and custom scripts for repeatable deployments
- Enforce configuration settings and report on configuration drift
- Deploy configuration using [push or pull](/en-us/powershell/scripting/dsc/pull-server/enactingconfigurations) models

## Monad Manifesto

Jeffrey Snover, the inventor of PowerShell, wrote the Monad Manifesto to explain his vision for PowerShell and how it would change the way we manage systems. Use the following link to download a copy of the [Monad Manifesto](https://github.com/MicrosoftDocs/PowerShell-Docs/blob/main/assets/MonadManifesto.pdf).

This PDF file is a version of the original Monad Manifesto, which articulated the long-term vision and started the development effort that became PowerShell. PowerShell has delivered on many of the elements described in this document.

## Next steps

### Getting started

Are you new to PowerShell and don't know where to start? Take a look at these resources.

- [Install PowerShell](/en-us/powershell/scripting/install/installing-powershell)
- [Discover PowerShell](discover-powershell?view=powershell-7.4)
- [PowerShell 101](/en-us/powershell/scripting/learn/ps101/00-introduction)
- [Microsoft Virtual Academy videos](/en-us/shows/browse?terms=powershell)
- [PowerShell Learn modules](/en-us/training/browse/?terms=PowerShell)

### PowerShell in action

Take a look at how PowerShell is being used in different scenarios and on different platforms.

- [PowerShell remoting over SSH](/en-us/powershell/scripting/learn/remoting/ssh-remoting-in-powershell-core)
- [Getting started with Azure PowerShell](/en-us/powershell/azure/get-started-azureps)
- [Building a CI/CD pipeline with DSC](/en-us/azure/devops/pipelines/release/dsc-cicd)
- [Managing Microsoft Exchange](/en-us/powershell/exchange/exchange-management-shell)

 Collaborate with us on GitHub  The source for this content can be found on GitHub, where you can also create and review issues and pull requests. For more information, see [our contributor guide](https://learn.microsoft.com/powershell/scripting/community/contributing/powershell-style-guide). 

 PowerShell 

[Open a documentation issue](#)[Provide product feedback](https://github.com/powershell/powershell/issues/new)

## Feedback

 Was this page helpful? 

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix? 

##  Additional resources 

- Last updated on  2025-07-07
