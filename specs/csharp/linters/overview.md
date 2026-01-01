# Roslyn Analyzers Overview

.NET compiler platform analyzers for C#.

## Built-in Analyzers

### Code Analysis (CA)

Design, globalization, performance, security rules.

```xml
<!-- .editorconfig -->
[*.cs]
dotnet_analyzer_diagnostic.category-Performance.severity = warning
dotnet_analyzer_diagnostic.category-Security.severity = error
```

### Code Style (IDE)

Formatting, naming, expression-level preferences.

```xml
[*.cs]
# Prefer var
csharp_style_var_for_built_in_types = true:suggestion
csharp_style_var_when_type_is_apparent = true:suggestion

# Prefer expression body
csharp_style_expression_bodied_methods = when_on_single_line:suggestion

# Prefer pattern matching
csharp_style_pattern_matching_over_is_with_cast_check = true:warning
```

## Configuration

### .editorconfig

```ini
root = true

[*.cs]
# Analyzer severity
dotnet_diagnostic.CA1000.severity = warning
dotnet_diagnostic.CA2000.severity = error

# Bulk configuration
dotnet_analyzer_diagnostic.severity = warning
dotnet_code_quality.severity = warning

# Code style
dotnet_style_qualification_for_field = false:suggestion
dotnet_style_qualification_for_property = false:suggestion
dotnet_style_predefined_type_for_locals_parameters_members = true:warning

# Naming
dotnet_naming_rule.private_fields_should_be_camel_case.severity = warning
dotnet_naming_rule.private_fields_should_be_camel_case.symbols = private_fields
dotnet_naming_rule.private_fields_should_be_camel_case.style = camel_case_style

dotnet_naming_symbols.private_fields.applicable_kinds = field
dotnet_naming_symbols.private_fields.applicable_accessibilities = private

dotnet_naming_style.camel_case_style.capitalization = camel_case
dotnet_naming_style.camel_case_style.required_prefix = _
```

### Project Configuration

```xml
<!-- .csproj -->
<PropertyGroup>
    <AnalysisLevel>latest</AnalysisLevel>
    <EnforceCodeStyleInBuild>true</EnforceCodeStyleInBuild>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    <Nullable>enable</Nullable>
</PropertyGroup>

<ItemGroup>
    <PackageReference Include="Microsoft.CodeAnalysis.NetAnalyzers" Version="8.0.0">
        <PrivateAssets>all</PrivateAssets>
        <IncludeAssets>runtime; build; native; contentfiles; analyzers</IncludeAssets>
    </PackageReference>
</ItemGroup>
```

## Suppression

```csharp
// Inline suppression
#pragma warning disable CA1000
public static void Method() { }
#pragma warning restore CA1000

// Attribute suppression
[SuppressMessage("Design", "CA1000:DoNotDeclareStaticMembersOnGenericTypes")]
public static void Method() { }

// Global suppression (GlobalSuppressions.cs)
[assembly: SuppressMessage("Design", "CA1000", Scope = "member", Target = "~M:MyClass.Method")]
```

## Rule Categories

| Category | Prefix | Description |
|----------|--------|-------------|
| Design | CA1xxx | API design |
| Globalization | CA1300-1399 | Culture issues |
| Performance | CA1800-1899 | Performance |
| Security | CA2xxx | Security |
| Usage | CA2200-2299 | Proper API usage |
| Reliability | CA2000-2099 | Reliability |
| Naming | CA1700-1799 | Naming |
