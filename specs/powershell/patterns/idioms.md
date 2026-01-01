# PowerShell Idioms

## Prefer cmdlets over aliases

```powershell
Get-ChildItem
```

## Use splatting for readability

```powershell
$params = @{ Path = $path; Recurse = $true }
Get-ChildItem @params
```
