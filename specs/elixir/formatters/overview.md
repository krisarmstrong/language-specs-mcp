mix format — Mix v1.19.4https://elixir-lang.org/docs.html[Mix](https://elixir-lang.org/docs.html) v1.19.4 

Search documentation of MixDefaultDefaultIn-browser searchSettings

# mix format(Mix v1.19.4)

[View Source](https://github.com/elixir-lang/elixir/blob/v1.19.4/lib/mix/lib/mix/tasks/format.ex#L5)

Formats the given files and patterns.

```
$ mix format mix.exs "lib/**/*.{ex,exs}" "test/**/*.{ex,exs}"
```

If any of the files is `-`, then the input is read from stdin and the output is written to stdout.

## #module-formatting-optionsFormatting options

The formatter will read a `.formatter.exs` file in the current directory for formatter configuration. Evaluating this file should return a keyword list.

Here is an example of a `.formatter.exs` file that works as a starting point:

```
[
  inputs: ["{mix,.formatter}.exs", "{config,lib,test}/**/*.{ex,exs}"]
]
```

Besides the options listed in [Code.format_string!/2](https://hexdocs.pm/elixir/Code.html#format_string!/2), the `.formatter.exs` file supports the following options:

- 

`:inputs` (a list of paths and patterns) - specifies the default inputs to be used by this task. For example, `["mix.exs", "{config,lib,test}/**/*.{ex,exs}"]`. Patterns are expanded with [Path.wildcard/2](https://hexdocs.pm/elixir/Path.html#wildcard/2).

- 

`:excludes` (a list of paths and patterns) (since v1.19.0) - specifies the files to exclude from the list of inputs to this task. For example, `["config/runtime.exs", "test/**/*.{ex,exs}"]`. Patterns are expanded with [Path.wildcard/2](https://hexdocs.pm/elixir/Path.html#wildcard/2).

- 

`:plugins` (a list of modules) (since v1.13.0) - specifies a list of modules to customize how the formatter works. See the "Plugins" section below for more information.

- 

`:subdirectories` (a list of paths and patterns) - specifies subdirectories that have their own formatting rules. Each subdirectory should have a `.formatter.exs` that configures how entries in that subdirectory should be formatted as. Configuration between `.formatter.exs` are not shared nor inherited. If a `.formatter.exs` lists "lib/app" as a subdirectory, the rules in `.formatter.exs` won't be available in `lib/app/.formatter.exs`. Note that the parent `.formatter.exs` must not specify files inside the "lib/app" subdirectory in its `:inputs` configuration. If this happens, the behaviour of which formatter configuration will be picked is unspecified.

- 

`:import_deps` (a list of dependencies as atoms) - specifies a list of dependencies whose formatter configuration will be imported. See the "Importing dependencies configuration" section below for more information.

- 

`:export` (a keyword list) - specifies formatter configuration to be exported. See the "Importing dependencies configuration" section below.

## #module-task-specific-optionsTask-specific options

- 

`--force` - force formatting to happen on all files, instead of relying on cache.

- 

`--check-formatted` - checks that the file is already formatted. This is useful in pre-commit hooks and CI scripts if you want to reject contributions with unformatted code. If the check fails, the formatted contents are not written to disk. Keep in mind that the formatted output may differ between Elixir versions as improvements and fixes are applied to the formatter.

- 

`--no-exit` - only valid when used with `--check-formatted`. Pass this if you don't want this Mix task to fail (and return a non-zero exit code), but still want to check for format errors and print them to the console.

- 

`--dry-run` - does not save files after formatting.

- 

`--dot-formatter` - path to the file with formatter configuration. Defaults to `.formatter.exs` if one is available. See the "Formatting options" section above for more information.

- 

`--stdin-filename` - path to the file being formatted on stdin. This is useful if you are using plugins to support custom filetypes such as `.heex`. Without passing this flag, it is assumed that the code being passed via stdin is valid Elixir code. Defaults to `stdin.exs`.

- 

`--migrate` - enables the `:migrate` option, which should be able to automatically fix some deprecation warnings but changes the AST. This should be safe in typical projects, but there is a non-zero risk of breaking code for meta-programming heavy projects that relied on a specific AST. We recommend running this task in its separate commit and reviewing its output before committing. See the "Migration formatting" section in [Code.format_string!/2](https://hexdocs.pm/elixir/Code.html#format_string!/2) for more information.

## #module-when-to-format-codeWhen to format code

We recommend developers to format code directly in their editors, either automatically when saving a file or via an explicit command or key binding. If such option is not available in your editor of choice, adding the required integration is usually a matter of invoking:

```
$ cd $project && mix format $file
```

where `$file` refers to the current file and `$project` is the root of your project.

It is also possible to format code across the whole project by passing a list of patterns and files to [mix format](Mix.Tasks.Format.html), as shown at the top of this task documentation. This list can also be set in the `.formatter.exs` file under the `:inputs` key.

## #module-pluginsPlugins

It is possible to customize how the formatter behaves. Plugins must implement the [Mix.Tasks.Format](Mix.Tasks.Format.html) behaviour. For example, imagine that your project uses Markdown in two distinct ways: via a custom `~M` sigil and via files with the `.md` and `.markdown` extensions. A custom plugin would look like this:

```
defmodule MixMarkdownFormatter do
  @behaviour Mix.Tasks.Format

  def features(_opts) do
    [sigils: [:M], extensions: [".md", ".markdown"]]
  end

  def format(contents, opts) do
    # logic that formats markdown
  end
end
```

The `opts` passed to `format/2` contains all the formatting options and either:

- 

`:sigil` (atom) - the sigil being formatted, e.g. `:M`.

- 

`:modifiers` (charlist) - list of sigil modifiers.

- 

`:extension` (string) - the extension of the file being formatted, e.g. `".md"`.

Now any application can use your formatter as follows:

```
# .formatter.exs
[
  # Define the desired plugins
  plugins: [MixMarkdownFormatter, AnotherMarkdownFormatter],
  # Remember to update the inputs list to include the new extensions
  inputs: ["{mix,.formatter}.exs", "{config,lib,test}/**/*.{ex,exs}", "posts/*.{md,markdown}"]
]
```

Notice that, when running the formatter with plugins, your code will be compiled first.

In addition, the order by which you input your plugins is the format order. So, in the above `.formatter.exs`, the `MixMarkdownFormatter` will format the markdown files and sigils before `AnotherMarkdownFormatter`.

## #module-importing-dependencies-configurationImporting dependencies configuration

This task supports importing formatter configuration from dependencies.

A dependency that wants to export formatter configuration needs to have a `.formatter.exs` file at the root of the project. In this file, the dependency can list an `:export` option with configuration to export. For now, only one option is supported under `:export`: `:locals_without_parens` (whose value has the same shape as the value of the `:locals_without_parens` in [Code.format_string!/2](https://hexdocs.pm/elixir/Code.html#format_string!/2)).

The functions listed under `:locals_without_parens` in the `:export` option of a dependency can be imported in a project by listing that dependency in the `:import_deps` option of the formatter configuration file of the project.

For example, consider you have a project called `my_app` that depends on another one called `my_dep`. `my_dep` wants to export some configuration, so `my_dep/.formatter.exs` would look like this:

```
# my_dep/.formatter.exs
[
  # Regular formatter configuration for my_dep
  # ...

  export: [
    locals_without_parens: [some_dsl_call: 2, some_dsl_call: 3]
  ]
]
```

In order to import configuration, `my_app`'s `.formatter.exs` would look like this:

```
# my_app/.formatter.exs
[
  import_deps: [:my_dep]
]
```

# #summarySummary

## [Types](#types)

[formatter_for_file_opts()](#t:formatter_for_file_opts/0)

Options for `formatter_for_file/2`.

## [Callbacks](#callbacks)

[features(keyword)](#c:features/1)

Returns which features this plugin should plug into.

[format(t, keyword)](#c:format/2)

Receives a string to be formatted with options and returns said string.

## [Functions](#functions)

[formatter_for_file(file, opts \\ [])](#formatter_for_file/2)

Returns a formatter function and the formatter options to be used for the given file.

# #typesTypes

#t:formatter_for_file_opts/0

# formatter_for_file_opts()

https://github.com/elixir-lang/elixir/blob/v1.19.4/lib/mix/lib/mix/tasks/format.ex#L370

```
@type formatter_for_file_opts() :: [
  deps_paths: %{required(atomhttps://hexdocs.pm/elixir/typespecs.html#basic-types()) => String.thttps://hexdocs.pm/elixir/String.html#t:t/0()},
  dot_formatter: String.thttps://hexdocs.pm/elixir/String.html#t:t/0(),
  plugin_loader: ([modulehttps://hexdocs.pm/elixir/typespecs.html#built-in-types()] -> [modulehttps://hexdocs.pm/elixir/typespecs.html#built-in-types()]),
  root: String.thttps://hexdocs.pm/elixir/String.html#t:t/0()
]
```

Options for [formatter_for_file/2](#formatter_for_file/2).

# #callbacksCallbacks

#c:features/1

# features(keyword)

https://github.com/elixir-lang/elixir/blob/v1.19.4/lib/mix/lib/mix/tasks/format.ex#L235

```
@callback features(keywordhttps://hexdocs.pm/elixir/typespecs.html#built-in-types()) :: [sigils: [atomhttps://hexdocs.pm/elixir/typespecs.html#basic-types()], extensions: [binaryhttps://hexdocs.pm/elixir/typespecs.html#built-in-types()]]
```

Returns which features this plugin should plug into.

It receives all options specified in `.formatter.exs`.

#c:format/2

# format(t, keyword)

https://github.com/elixir-lang/elixir/blob/v1.19.4/lib/mix/lib/mix/tasks/format.ex#L242

```
@callback format(
  String.thttps://hexdocs.pm/elixir/String.html#t:t/0(),
  keywordhttps://hexdocs.pm/elixir/typespecs.html#built-in-types()
) :: String.thttps://hexdocs.pm/elixir/String.html#t:t/0()
```

Receives a string to be formatted with options and returns said string.

It receives all options specified in `.formatter.exs`.

# #functionsFunctions

#formatter_for_file/2

# formatter_for_file(file, opts \\ [])

(since 1.13.0)https://github.com/elixir-lang/elixir/blob/v1.19.4/lib/mix/lib/mix/tasks/format.ex#L412

```
@spec formatter_for_file(String.thttps://hexdocs.pm/elixir/String.html#t:t/0(), formatter_for_file_opts#t:formatter_for_file_opts/0()) ::
  {(String.thttps://hexdocs.pm/elixir/String.html#t:t/0() -> String.thttps://hexdocs.pm/elixir/String.html#t:t/0()), keywordhttps://hexdocs.pm/elixir/typespecs.html#built-in-types()}
```

Returns a formatter function and the formatter options to be used for the given file.

The function must be called with the contents of the file to be formatted. Keep in mind that a function is always returned, even if it doesn't match any of the inputs specified in the `formatter.exs`. You can retrieve the `:inputs` from the returned options, alongside the `:root` option, to validate if the returned file matches the given `:root` and `:inputs`.

## #formatter_for_file/2-optionsOptions

- 

`:deps_paths` (since v1.18.0) - the dependencies path to be used to resolve `import_deps`. It defaults to `Mix.Project.deps_paths`.

- 

`:dot_formatter` - use the given file as the `dot_formatter` root. If this option is not specified, it uses the default one. The default one is cached, so use this option only if necessary.

- 

`:plugin_loader` (since v1.18.0) - a function that receives a list of plugins, which may or may not yet be loaded, and ensures all of them are loaded. It must return a list of plugins, which is recommended to be the exact same list given as argument. You may choose to skip plugins, but then it means the code will be partially formatted (as in the plugins will be skipped). By default, this function calls [mix loadpaths](Mix.Tasks.Loadpaths.html) and then, if not enough, [mix compile](Mix.Tasks.Compile.html).

- 

`:root` - use the given root as the current working directory.

 Search HexDocs [Download ePub version](Mix.epub)

 Built using [ExDoc](https://github.com/elixir-lang/ex_doc) (v0.39.1) for the [Elixir programming language](https://elixir-lang.org)
