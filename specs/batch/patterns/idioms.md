# Batch Idioms

## Use SetLocal

```bat
@echo off
setlocal EnableExtensions EnableDelayedExpansion
```

## Quote paths

```bat
if exist "%~f0" echo Running
```

## Prefer CALL for subroutines

```bat
call :do_work
exit /b

:do_work
  echo Work
  exit /b
```
