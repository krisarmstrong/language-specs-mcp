Table of contents Exit editor modeAsk LearnAsk LearnFocus modeTable of contents[Read in English](#)AddAdd to plan[Edit](https://github.com/MicrosoftDocs/PowerShell-Docs/blob/main/reference/7.4/Microsoft.PowerShell.Core/Microsoft.PowerShell.Core.md)

#### Share via

[Facebook](#)[x.com](#)[LinkedIn](#)[Email](#)Print

Note

 Access to this page requires authorization. You can try [signing in](#) or changing directories. 

 Access to this page requires authorization. You can try changing directories. 

 Summarize this article for me 

# Microsoft.PowerShell.Core Module

## 

The Microsoft.PowerShell.Core snap-in contains cmdlets and providers that manage the basic features of PowerShell. PowerShell loads Microsoft.PowerShell.Core snap-in automatically at startup. This is not a module. You can't import it using `Import-Module` or remove it using `Remove-Module`.

## Microsoft.PowerShell.Core Cmdlets

CmdletDescription[Add-History](add-history?view=powershell-7.4)

Appends entries to the session history.

[Clear-History](clear-history?view=powershell-7.4)

Deletes entries from the PowerShell session command history.

[Clear-Host](clear-host?view=powershell-7.4)

Clears the display in the host program.

[Connect-PSSession](connect-pssession?view=powershell-7.4)

Reconnects to disconnected sessions.

[Debug-Job](debug-job?view=powershell-7.4)

Debugs a running background or remote job.

[Disable-ExperimentalFeature](disable-experimentalfeature?view=powershell-7.4)

Disable an experimental feature on startup of new instance of PowerShell.

[Disable-PSRemoting](disable-psremoting?view=powershell-7.4)

Prevents PowerShell endpoints from receiving remote connections.

[Disable-PSSessionConfiguration](disable-pssessionconfiguration?view=powershell-7.4)

Disables session configurations on the local computer.

[Disconnect-PSSession](disconnect-pssession?view=powershell-7.4)

Disconnects from a session.

[Enable-ExperimentalFeature](enable-experimentalfeature?view=powershell-7.4)

Enable an experimental feature on startup of new instance of PowerShell.

[Enable-PSRemoting](enable-psremoting?view=powershell-7.4)

Configures the computer to receive remote commands.

[Enable-PSSessionConfiguration](enable-pssessionconfiguration?view=powershell-7.4)

Enables the session configurations on the local computer.

[Enter-PSHostProcess](enter-pshostprocess?view=powershell-7.4)

Connects to and enters into an interactive session with a local process.

[Enter-PSSession](enter-pssession?view=powershell-7.4)

Starts an interactive session with a remote computer.

[Exit-PSHostProcess](exit-pshostprocess?view=powershell-7.4)

Closes an interactive session with a local process.

[Exit-PSSession](exit-pssession?view=powershell-7.4)

Ends an interactive session with a remote computer.

[Export-ModuleMember](export-modulemember?view=powershell-7.4)

Specifies the module members that are exported.

[ForEach-Object](foreach-object?view=powershell-7.4)

Performs an operation against each item in a collection of input objects.

[Get-Command](get-command?view=powershell-7.4)

Gets all commands.

[Get-ExperimentalFeature](get-experimentalfeature?view=powershell-7.4)

Gets experimental features.

[Get-Help](get-help?view=powershell-7.4)

Displays information about PowerShell commands and concepts.

[Get-History](get-history?view=powershell-7.4)

Gets a list of the commands entered during the current session.

[Get-Job](get-job?view=powershell-7.4)

Gets PowerShell background jobs that are running in the current session.

[Get-Module](get-module?view=powershell-7.4)

List the modules imported in the current session or that can be imported from the PSModulePath.

[Get-PSHostProcessInfo](get-pshostprocessinfo?view=powershell-7.4)

Gets process information about the PowerShell host.

[Get-PSSession](get-pssession?view=powershell-7.4)

Gets the PowerShell sessions on local and remote computers.

[Get-PSSessionCapability](get-pssessioncapability?view=powershell-7.4)

Gets the capabilities of a specific user on a constrained session configuration.

[Get-PSSessionConfiguration](get-pssessionconfiguration?view=powershell-7.4)

Gets the registered session configurations on the computer.

[Get-PSSubsystem](get-pssubsystem?view=powershell-7.4)

Retrieves information about the subsystems registered in PowerShell.

[Import-Module](import-module?view=powershell-7.4)

Adds modules to the current session.

[Invoke-Command](invoke-command?view=powershell-7.4)

Runs commands on local and remote computers.

[Invoke-History](invoke-history?view=powershell-7.4)

Runs commands from the session history.

[New-Module](new-module?view=powershell-7.4)

Creates a new dynamic module that exists only in memory.

[New-ModuleManifest](new-modulemanifest?view=powershell-7.4)

Creates a new module manifest.

[New-PSRoleCapabilityFile](new-psrolecapabilityfile?view=powershell-7.4)

Creates a file that defines a set of capabilities to be exposed through a session configuration.

[New-PSSession](new-pssession?view=powershell-7.4)

Creates a persistent connection to a local or remote computer.

[New-PSSessionConfigurationFile](new-pssessionconfigurationfile?view=powershell-7.4)

Creates a file that defines a session configuration.

[New-PSSessionOption](new-pssessionoption?view=powershell-7.4)

Creates an object that contains advanced options for a PSSession.

[New-PSTransportOption](new-pstransportoption?view=powershell-7.4)

Creates an object that contains advanced options for a session configuration.

[Out-Default](out-default?view=powershell-7.4)

Sends the output to the default formatter and to the default output cmdlet.

[Out-Host](out-host?view=powershell-7.4)

Sends output to the command line.

[Out-Null](out-null?view=powershell-7.4)

Hides the output instead of sending it down the pipeline or displaying it.

[Receive-Job](receive-job?view=powershell-7.4)

Gets the results of the PowerShell background jobs in the current session.

[Receive-PSSession](receive-pssession?view=powershell-7.4)

Gets results of commands in disconnected sessions

[Register-ArgumentCompleter](register-argumentcompleter?view=powershell-7.4)

Registers a custom argument completer.

[Register-PSSessionConfiguration](register-pssessionconfiguration?view=powershell-7.4)

Creates and registers a new session configuration.

[Remove-Job](remove-job?view=powershell-7.4)

Deletes a PowerShell background job.

[Remove-Module](remove-module?view=powershell-7.4)

Removes modules from the current session.

[Remove-PSSession](remove-pssession?view=powershell-7.4)

Closes one or more PowerShell sessions (PSSessions).

[Save-Help](save-help?view=powershell-7.4)

Downloads and saves the newest help files to a file system directory.

[Set-PSDebug](set-psdebug?view=powershell-7.4)

Turns script debugging features on and off, sets the trace level, and toggles strict mode.

[Set-PSSessionConfiguration](set-pssessionconfiguration?view=powershell-7.4)

Changes the properties of a registered session configuration.

[Set-StrictMode](set-strictmode?view=powershell-7.4)

Establishes and enforces coding rules in expressions, scripts, and script blocks.

[Start-Job](start-job?view=powershell-7.4)

Starts a PowerShell background job.

[Stop-Job](stop-job?view=powershell-7.4)

Stops a PowerShell background job.

[Switch-Process](switch-process?view=powershell-7.4)

On Linux and macOS, the cmdlet calls the `execv()` function to provide similar behavior as POSIX shells.

[TabExpansion2](tabexpansion2?view=powershell-7.4)

A helper function that wraps the `CompleteInput()` method of the CommandCompletion class to provide tab completion for PowerShell scripts.

[Test-ModuleManifest](test-modulemanifest?view=powershell-7.4)

Verifies that a module manifest file accurately describes the contents of a module.

[Test-PSSessionConfigurationFile](test-pssessionconfigurationfile?view=powershell-7.4)

Verifies the keys and values in a session configuration file.

[Unregister-PSSessionConfiguration](unregister-pssessionconfiguration?view=powershell-7.4)

Deletes registered session configurations from the computer.

[Update-Help](update-help?view=powershell-7.4)

Downloads and installs the newest help files on your computer.

[Wait-Job](wait-job?view=powershell-7.4)

Waits until one or all of the PowerShell jobs running in the session are in a terminating state.

[Where-Object](where-object?view=powershell-7.4)

Selects objects from a collection based on their property values.

 Collaborate with us on GitHub  The source for this content can be found on GitHub, where you can also create and review issues and pull requests. For more information, see [our contributor guide](https://learn.microsoft.com/powershell/scripting/community/contributing/powershell-style-guide). 

 PowerShell 

[Open a documentation issue](#)[Provide product feedback](https://github.com/PowerShell/PowerShell/issues/new/choose)

## Feedback

 Was this page helpful? 

YesNoNo

 Need help with this topic? 

 Want to try using Ask Learn to clarify or guide you through this topic? 

Ask LearnAsk Learn Suggest a fix?
