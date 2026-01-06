Table of contents Exit editor modeAsk LearnAsk LearnFocus modeTable of contents[Read in English](#)AddAdd to plan[Edit](https://github.com/MicrosoftDocs/PowerShell-Docs/blob/main/reference/7.4/PSReadLine/PSReadLine.md)

#### Share via

[Facebook](#)[x.com](#)[LinkedIn](#)[Email](#)Print

Note

 Access to this page requires authorization. You can try [signing in](#) or changing directories. 

 Access to this page requires authorization. You can try changing directories. 

 Summarize this article for me 

# PSReadLine Module

## 

The PSReadLine module contains cmdlets that let you customize the command-line editing environment in PowerShell.

There have been many updates to PSReadLine since the version that ships in Windows PowerShell 5.1.

- v2.3.6 first shipped in PowerShell 7.4.7 and 7.5.0
- v2.3.5 first shipped in PowerShell 7.4.2 and 7.5.0-preview.3
- v2.3.4 first shipped in PowerShell 7.4.0-rc.1
- v2.2.6 first shipped in PowerShell 7.3.0
- v2.1.0 first shipped in PowerShell 7.2.5
- v2.0.4 first shipped in PowerShell 7.0.11
- v2.0.0 ships in Windows PowerShell 5.1

For more information about version differences, see [about_PSReadLine_Release_Notes](about/about_psreadline_release_notes?view=powershell-7.4).

These articles document version 2.3.6 of PSReadLine.

Note

Beginning with PowerShell 7.0, PowerShell skips auto-loading PSReadLine on Windows if a screen reader program is detected. Currently, PSReadLine doesn't work well with the screen readers. The default rendering and formatting of PowerShell 7.0 on Windows works properly. You can manually load the module if necessary.

## PSReadLine Cmdlets

CmdletDescription[Get-PSReadLineKeyHandler](get-psreadlinekeyhandler?view=powershell-7.4)

Gets the key bindings for the PSReadLine module.

[Get-PSReadLineOption](get-psreadlineoption?view=powershell-7.4)

Gets values for the options that can be configured.

[PSConsoleHostReadLine](psconsolehostreadline?view=powershell-7.4)

This function is the main entry point for PSReadLine.

[Remove-PSReadLineKeyHandler](remove-psreadlinekeyhandler?view=powershell-7.4)

Removes a key binding.

[Set-PSReadLineKeyHandler](set-psreadlinekeyhandler?view=powershell-7.4)

Binds keys to user-defined or PSReadLine key handler functions.

[Set-PSReadLineOption](set-psreadlineoption?view=powershell-7.4)

Customizes the behavior of command line editing in PSReadLine.

 Collaborate with us on GitHub  The source for this content can be found on GitHub, where you can also create and review issues and pull requests. For more information, see [our contributor guide](https://learn.microsoft.com/powershell/scripting/community/contributing/powershell-style-guide). 

 PowerShell 

[Open a documentation issue](#)[Provide product feedback](https://github.com/PowerShell/PowerShell/issues/new/choose)

## Feedback

 Was this page helpful? 

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix?
