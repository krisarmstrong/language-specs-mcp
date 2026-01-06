# Credo

Credo is a static code analysis tool for Elixir focusing on teaching and code consistency.

Version: 1.7.10
Source: https://hexdocs.pm/credo/

## Installation

Add to `mix.exs`:

```elixir
defp deps do
  [{:credo, "~> 1.7", only: [:dev, :test], runtime: false}]
end
```

## Usage

```bash
# Run analysis
mix credo

# Strict mode
mix credo --strict

# Focus on specific file
mix credo lib/my_app/module.ex

# Generate config
mix credo gen.config
```

## Configuration

Create `.credo.exs`:

```elixir
%{
  configs: [
    %{
      name: "default",
      files: %{
        included: ["lib/", "src/", "test/"],
        excluded: [~r"/_build/", ~r"/deps/"]
      },
      checks: %{
        enabled: [
          {Credo.Check.Consistency.TabsOrSpaces, []},
          {Credo.Check.Readability.ModuleDoc, []},
          {Credo.Check.Refactor.Nesting, [max_nesting: 2]}
        ],
        disabled: [
          {Credo.Check.Design.TagTODO, []}
        ]
      }
    }
  ]
}
```

## Check Categories

### Consistency
Ensures consistent coding style across the codebase.

### Design
Checks for software design issues.

### Readability
Improves code readability.

### Refactor
Identifies refactoring opportunities.

### Warning
Catches potential bugs and issues.

## Priority Levels

- `:higher` - Critical issues
- `:high` - Important issues
- `:normal` - Standard checks
- `:low` - Minor suggestions
- `:ignore` - Disabled

## Inline Configuration

```elixir
# Disable for line
# credo:disable-for-this-file
# credo:disable-for-next-line
# credo:disable-for-lines:3

defmodule MyModule do
  # credo:disable-for-this-file Credo.Check.Readability.ModuleDoc
end
```
