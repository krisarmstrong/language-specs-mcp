# PowerShell Generation Checklist

**Read this BEFORE writing PowerShell code. Pipeline and error handling matter.**

## Critical: You Must Do These

### 1. Use Approved Verbs for Function Names
```powershell
# BAD - non-standard verbs
function GetUserData { }
function DeleteOldFiles { }
function Make-Report { }

# GOOD - approved verbs (see Get-Verb)
function Get-UserData { }
function Remove-OldFiles { }
function New-Report { }

# Standard verbs: Get, Set, New, Remove, Start, Stop, Invoke, etc.
Get-Verb | Sort-Object Verb
```

### 2. Use `[CmdletBinding()]` for Advanced Functions
```powershell
# BAD - basic function
function Get-Data {
    param($Path)
    # No -Verbose, -Debug, etc.
}

# GOOD - advanced function with CmdletBinding
function Get-Data {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Path,

        [switch]$Force
    )

    Write-Verbose "Reading from $Path"
    # Now supports -Verbose, -Debug, -ErrorAction, etc.
}
```

### 3. Handle Errors Properly
```powershell
# BAD - errors silently continue
Get-Content "nonexistent.txt"
# Script continues...

# GOOD - use try/catch with ErrorAction Stop
try {
    $content = Get-Content "config.txt" -ErrorAction Stop
}
catch {
    Write-Error "Failed to read config: $_"
    return
}

# GOOD - set preference at script level
$ErrorActionPreference = 'Stop'

# GOOD - use -ErrorAction per command
Get-Item $path -ErrorAction SilentlyContinue
```

### 4. Validate Parameters
```powershell
# GOOD - parameter validation attributes
function Set-Configuration {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [ValidateNotNullOrEmpty()]
        [string]$Name,

        [ValidateSet('Development', 'Staging', 'Production')]
        [string]$Environment = 'Development',

        [ValidateRange(1, 65535)]
        [int]$Port = 8080,

        [ValidateScript({ Test-Path $_ })]
        [string]$ConfigPath,

        [ValidatePattern('^[a-zA-Z0-9]+$')]
        [string]$AppId
    )
}
```

### 5. Use Pipeline Input Correctly
```powershell
# GOOD - support pipeline input
function Remove-OldFile {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory, ValueFromPipeline, ValueFromPipelineByPropertyName)]
        [Alias('FullName')]
        [string[]]$Path
    )

    process {
        foreach ($file in $Path) {
            if ($PSCmdlet.ShouldProcess($file, 'Remove')) {
                Remove-Item $file -Force
            }
        }
    }
}

# Usage
Get-ChildItem *.log | Remove-OldFile -WhatIf
```

## Important: Strong Recommendations

### 6. Use Meaningful Variable Names
```powershell
# BAD - unclear
$x = Get-Process
$a = $x | Where-Object { $_.CPU -gt 100 }

# GOOD - descriptive
$allProcesses = Get-Process
$highCpuProcesses = $allProcesses | Where-Object { $_.CPU -gt 100 }
```

### 7. Use Splatting for Long Commands
```powershell
# BAD - hard to read
Send-MailMessage -From "alerts@company.com" -To "admin@company.com" -Subject "Alert" -Body "Server down" -SmtpServer "mail.company.com" -Priority High

# GOOD - splatting
$mailParams = @{
    From       = "alerts@company.com"
    To         = "admin@company.com"
    Subject    = "Alert"
    Body       = "Server down"
    SmtpServer = "mail.company.com"
    Priority   = "High"
}
Send-MailMessage @mailParams
```

### 8. Use `ForEach-Object` vs `foreach` Statement Appropriately
```powershell
# foreach statement - faster for known collections
$results = foreach ($item in $collection) {
    Process-Item $item
}

# ForEach-Object - for pipeline streaming, memory efficient
Get-Content "largefile.txt" | ForEach-Object {
    Process-Line $_
}

# ForEach-Object with parallel (PowerShell 7+)
1..10 | ForEach-Object -Parallel {
    Start-Sleep 1
    "Processed $_"
} -ThrottleLimit 5
```

### 9. Use Strong Typing When Appropriate
```powershell
# BAD - type issues at runtime
function Get-UserAge {
    param($birthDate)
    return (Get-Date) - $birthDate  # Fails if not DateTime
}

# GOOD - typed parameters
function Get-UserAge {
    param(
        [Parameter(Mandatory)]
        [datetime]$BirthDate
    )
    return ((Get-Date) - $BirthDate).Days / 365
}
```

### 10. Use `$PSScriptRoot` for Script-Relative Paths
```powershell
# BAD - assumes current directory
$config = Get-Content "config.json"
. ".\helpers.ps1"

# GOOD - relative to script location
$config = Get-Content (Join-Path $PSScriptRoot "config.json")
. (Join-Path $PSScriptRoot "helpers.ps1")
```

## Output and Formatting

### 11. Use Write-Output for Pipeline Output
```powershell
# BAD - Write-Host bypasses pipeline
function Get-Data {
    Write-Host "Found 10 items"  # Can't be captured!
    return $items
}

# GOOD - Write-Output for data (or implicit output)
function Get-Data {
    Write-Verbose "Finding items..."  # Goes to verbose stream
    $items  # Implicit Write-Output
}

# Use appropriate streams:
# Write-Output    - Pipeline output (stream 1)
# Write-Error     - Errors (stream 2)
# Write-Warning   - Warnings (stream 3)
# Write-Verbose   - Verbose info (stream 4)
# Write-Debug     - Debug info (stream 5)
# Write-Information - Info (stream 6)
```

### 12. Return Objects, Not Formatted Text
```powershell
# BAD - returns formatted string
function Get-DiskInfo {
    $disk = Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='C:'"
    return "Drive C: has $([math]::Round($disk.FreeSpace/1GB, 2)) GB free"
}

# GOOD - returns object
function Get-DiskInfo {
    [CmdletBinding()]
    param(
        [string]$DriveLetter = 'C'
    )

    $disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='${DriveLetter}:'"

    [PSCustomObject]@{
        DriveLetter = $DriveLetter
        FreeSpaceGB = [math]::Round($disk.FreeSpace / 1GB, 2)
        TotalSizeGB = [math]::Round($disk.Size / 1GB, 2)
        PercentFree = [math]::Round(($disk.FreeSpace / $disk.Size) * 100, 1)
    }
}
```

## Security

### 13. Avoid Invoke-Expression
```powershell
# DANGEROUS - code injection risk
$userInput = Read-Host "Enter command"
Invoke-Expression $userInput

# DANGEROUS - command in string
$cmd = "Get-Process -Name $processName"
Invoke-Expression $cmd

# GOOD - use direct commands with parameters
$process = Get-Process -Name $processName

# GOOD - use call operator if needed
$cmdName = "Get-Process"
& $cmdName -Name $processName
```

### 14. Use SecureString for Credentials
```powershell
# BAD - plain text password
$password = "MyPassword123"
$cred = New-Object PSCredential("user", (ConvertTo-SecureString $password -AsPlainText -Force))

# GOOD - prompt for credentials
$cred = Get-Credential

# GOOD - from secure storage
$cred = Import-Clixml "$env:USERPROFILE\mycred.xml"
```

### 15. Sanitize File Paths
```powershell
# BAD - path injection
$userPath = "..\..\..\etc\passwd"
Get-Content "C:\data\$userPath"

# GOOD - validate and sanitize
function Get-SafePath {
    param([string]$UserInput, [string]$BasePath)

    $fullPath = Join-Path $BasePath $UserInput
    $resolvedPath = [System.IO.Path]::GetFullPath($fullPath)

    if (-not $resolvedPath.StartsWith($BasePath)) {
        throw "Invalid path: outside allowed directory"
    }
    return $resolvedPath
}
```

---

**Quick Reference - Copy This Mental Model:**
- Approved verbs (Get-Verb)
- `[CmdletBinding()]` for all functions
- `try/catch` with `-ErrorAction Stop`
- Validate parameters (Mandatory, ValidateSet, etc.)
- Support pipeline with `ValueFromPipeline`
- Splatting for long commands
- `$PSScriptRoot` for paths
- Write-Verbose/Warning/Error (not Write-Host)
- Return objects, not strings
- Avoid Invoke-Expression
- SecureString for credentials
