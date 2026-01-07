# Batch (Windows CMD) Generation Checklist

**Read this BEFORE writing batch scripts. These rules prevent common issues.**

## Critical: You Must Do These

### 1. Use `@echo off` and `setlocal`
```batch
:: BAD - echoes every command, pollutes environment
set myvar=value
echo %myvar%

:: GOOD - clean execution, local variables
@echo off
setlocal enabledelayedexpansion

set "myvar=value"
echo %myvar%

endlocal
```

### 2. Always Quote Variable Assignments and Usage
```batch
:: BAD - breaks with spaces or special chars
set myvar=C:\Program Files\App
set myvar=%userpath%

:: GOOD - quoted assignment
set "myvar=C:\Program Files\App"
set "mypath=%userpath%"

:: Also quote in comparisons
if "%myvar%"=="expected" (
    echo Match
)
```

### 3. Use Delayed Expansion Inside Loops
```batch
:: BAD - variable doesn't update in loop
@echo off
set count=0
for %%f in (*.txt) do (
    set /a count=%count%+1
    echo Count is %count%  :: Always shows 0!
)

:: GOOD - delayed expansion
@echo off
setlocal enabledelayedexpansion
set count=0
for %%f in (*.txt) do (
    set /a count=!count!+1
    echo Count is !count!
)
```

### 4. Check If Files/Directories Exist
```batch
:: BAD - assumes file exists
copy "%sourcefile%" "%dest%"

:: GOOD - check first
if not exist "%sourcefile%" (
    echo Error: Source file not found
    exit /b 1
)
copy "%sourcefile%" "%dest%"

:: Check directory
if not exist "%targetdir%\" (
    mkdir "%targetdir%"
)
```

### 5. Use `exit /b` Not Just `exit`
```batch
:: BAD - exits entire command prompt
exit 1

:: GOOD - exits script with return code
exit /b 1

:: GOOD - with meaningful return codes
if errorlevel 1 (
    echo Operation failed
    exit /b 1
)
exit /b 0
```

## Important: Strong Recommendations

### 6. Check `%errorlevel%` After Commands
```batch
:: GOOD - check for errors
xcopy "%source%" "%dest%" /E /I /Y
if errorlevel 1 (
    echo Copy failed with error %errorlevel%
    exit /b 1
)

:: Or use && for chaining on success
mkdir "%newdir%" && echo Directory created

:: Use || for handling failure
mkdir "%newdir%" || echo Failed to create directory
```

### 7. Use Proper FOR Loop Syntax
```batch
:: Loop through files
for %%f in (*.txt) do (
    echo Processing %%f
)

:: Loop through directories
for /d %%d in (*) do (
    echo Directory: %%d
)

:: Recursive file processing
for /r "%startdir%" %%f in (*.log) do (
    echo Found: %%f
)

:: Loop through numbers
for /l %%i in (1,1,10) do (
    echo Number: %%i
)

:: Process command output
for /f "tokens=*" %%a in ('dir /b *.txt') do (
    echo File: %%a
)
```

### 8. Handle Paths with Spaces Correctly
```batch
:: BAD - breaks on spaces
cd %programfiles%\MyApp
copy %filepath% %dest%

:: GOOD - quoted paths
cd "%programfiles%\MyApp"
copy "%filepath%" "%dest%"

:: GOOD - use short names if needed
cd "%~dp0"  :: Script's directory
```

### 9. Use `%~dp0` for Script Location
```batch
:: BAD - assumes current directory
set "config=config.ini"

:: GOOD - relative to script location
set "scriptdir=%~dp0"
set "config=%scriptdir%config.ini"

:: Common path modifiers:
:: %~d0 - Drive letter only
:: %~p0 - Path only
:: %~n0 - File name only
:: %~x0 - Extension only
:: %~f0 - Full path
:: %~dp0 - Drive + path (script directory)
```

### 10. Create Robust Parameter Handling
```batch
@echo off
setlocal

:: Check for required parameters
if "%~1"=="" (
    echo Usage: %~nx0 ^<source^> ^<destination^>
    exit /b 1
)

:: Assign to named variables
set "source=%~1"
set "dest=%~2"

:: Validate parameters
if not exist "%source%" (
    echo Error: Source not found: %source%
    exit /b 1
)
```

## Common Patterns

### 11. Create Functions with Labels
```batch
@echo off
setlocal

:: Main script
call :log "Starting process"
call :process_file "data.txt"
call :log "Process complete"
exit /b 0

:: Function: log message
:log
echo [%date% %time%] %~1
goto :eof

:: Function: process a file
:process_file
echo Processing: %~1
:: ... processing logic ...
goto :eof
```

### 12. Use Temporary Files Safely
```batch
:: Create unique temp file
set "tempfile=%temp%\myapp_%random%.tmp"

:: Use it
echo data > "%tempfile%"

:: Clean up (even on error)
if exist "%tempfile%" del "%tempfile%"
```

### 13. Prompt for User Input
```batch
:: Simple yes/no prompt
set /p "confirm=Are you sure? (Y/N): "
if /i "%confirm%" neq "Y" (
    echo Cancelled
    exit /b 0
)

:: Choice command (better for simple choices)
choice /c YN /m "Continue?"
if errorlevel 2 exit /b 0
```

## Security

### 14. Don't Echo Sensitive Data
```batch
:: BAD - password visible in logs
echo Password is %password%
set password

:: GOOD - hide sensitive operations
@echo off
:: Don't echo password-related commands
set "password=" & set /p "password=Enter password: "
:: Use immediately, clear after
call :authenticate "%password%"
set "password="
```

### 15. Validate User Input
```batch
:: BAD - blindly uses input
set /p "filename=Enter filename: "
del "%filename%"

:: GOOD - validate input
set /p "filename=Enter filename: "

:: Check for path traversal
echo "%filename%" | findstr /r "\.\.[\\/]" >nul && (
    echo Error: Invalid path
    exit /b 1
)

:: Check file exists and is in allowed directory
if not exist "%alloweddir%\%filename%" (
    echo Error: File not found in allowed directory
    exit /b 1
)
```

### 16. Use Full Paths for System Commands
```batch
:: Potentially unsafe - could run malicious program
dir
copy

:: Safer - use full path (when security critical)
%SystemRoot%\System32\cmd.exe /c dir
%SystemRoot%\System32\xcopy.exe
```

---

**Quick Reference - Copy This Mental Model:**
- `@echo off` and `setlocal` at start
- Quote all variable assignments `set "var=value"`
- Delayed expansion `!var!` inside loops
- Check file existence before operations
- `exit /b` not `exit`
- Check `%errorlevel%` after commands
- Quote paths with spaces
- `%~dp0` for script directory
- Handle missing parameters gracefully
- Functions with `:label` and `goto :eof`
- Clean up temp files
- Validate user input
