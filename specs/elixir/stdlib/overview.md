Search documentation of ElixirDefaultDefaultIn-browser searchSettings

# API Reference Elixir v#1.19.4

[View Source](https://github.com/elixir-lang/elixir)

## Modules

[Access](Access.html)

Key-based access to data structures.

[Agent](Agent.html)

Agents are a simple abstraction around state.

[Application](Application.html)

A module for working with applications and defining application callbacks.

[ArgumentError](ArgumentError.html)

An exception raised when an argument to a function is invalid.

[ArithmeticError](ArithmeticError.html)

An exception raised on invalid arithmetic operations.

[Atom](Atom.html)

Atoms are constants whose values are their own name.

[BadArityError](BadArityError.html)

An exception raised when a function is called with the wrong number of arguments.

[BadBooleanError](BadBooleanError.html)

An exception raised when a boolean is expected, but something else was given.

[BadFunctionError](BadFunctionError.html)

An exception raised when a function is expected, but something else was given.

[BadMapError](BadMapError.html)

An exception raised when a map is expected, but something else was given.

[BadStructError](BadStructError.html)deprecated[Base](Base.html)

This module provides data encoding and decoding functions according to RFC 4648.

[Behaviour](Behaviour.html)deprecated

Mechanism for handling behaviours.

[Bitwise](Bitwise.html)

A set of functions that perform calculations on bits.

[Calendar](Calendar.html)

This module defines the responsibilities for working with calendars, dates, times and datetimes in Elixir.

[Calendar.ISO](Calendar.ISO.html)

The default calendar implementation, a Gregorian calendar following ISO 8601.

[Calendar.TimeZoneDatabase](Calendar.TimeZoneDatabase.html)

This module defines a behaviour for providing time zone data.

[Calendar.UTCOnlyTimeZoneDatabase](Calendar.UTCOnlyTimeZoneDatabase.html)

Built-in time zone database that works only in the `Etc/UTC` timezone.

[CaseClauseError](CaseClauseError.html)

An exception raised when a term in a `case/2` expression does not match any of the defined `->` clauses.

[Code](Code.html)

Utilities for managing code compilation, code evaluation, and code loading.

[Code.Fragment](Code.Fragment.html)

This module provides conveniences for analyzing fragments of textual code and extract available information whenever possible.

[Code.LoadError](Code.LoadError.html)

An exception raised when a file cannot be loaded.

[Collectable](Collectable.html)

A protocol to traverse data structures.

[CompileError](CompileError.html)

An exception raised when there's an error when compiling code.

[CondClauseError](CondClauseError.html)

An exception raised when no clauses in a `cond/1` expression evaluate to a truthy value.

[Config](Config.html)

A simple keyword-based configuration API.

[Config.Provider](Config.Provider.html)

Specifies a provider API that loads configuration during boot.

[Config.Reader](Config.Reader.html)

API for reading config files defined with `Config`.

[Date](Date.html)

A Date struct and functions.

[Date.Range](Date.Range.html)

Returns an inclusive range between dates.

[DateTime](DateTime.html)

A datetime implementation with a time zone.

[Dict](Dict.html)deprecated

Generic API for dictionaries.

[Duration](Duration.html)

Struct and functions for handling durations.

[DynamicSupervisor](DynamicSupervisor.html)

A supervisor optimized to only start children dynamically.

[Enum](Enum.html)

Functions for working with collections (known as enumerables).

[Enum.EmptyError](Enum.EmptyError.html)

An exception that is raised when something expects a non-empty enumerable but finds an empty one.

[Enum.OutOfBoundsError](Enum.OutOfBoundsError.html)

An exception that is raised when a function expects an enumerable to have a certain size but finds that it is too small.

[Enumerable](Enumerable.html)

Enumerable protocol used by `Enum` and `Stream` modules.

[ErlangError](ErlangError.html)

An exception raised when invoking an Erlang code that errors with a value not handled by Elixir.

[Exception](Exception.html)

Functions for dealing with throw/catch/exit and exceptions.

[File](File.html)

This module contains functions to manipulate files.

[File.CopyError](File.CopyError.html)

An exception that is raised when copying a file fails.

[File.Error](File.Error.html)

An exception that is raised when a file operation fails.

[File.LinkError](File.LinkError.html)

An exception that is raised when linking a file fails.

[File.RenameError](File.RenameError.html)

An exception that is raised when renaming a file fails.

[File.Stat](File.Stat.html)

A struct that holds file information.

[File.Stream](File.Stream.html)

Defines a `File.Stream` struct returned by `File.stream!/3`.

[Float](Float.html)

Functions for working with floating-point numbers.

[Function](Function.html)

A set of functions for working with functions.

[FunctionClauseError](FunctionClauseError.html)

An exception raised when a function call doesn't match any defined clause.

[GenEvent](GenEvent.html)deprecated

An event manager with event handlers behaviour.

[GenServer](GenServer.html)

A behaviour module for implementing the server of a client-server relation.

[HashDict](HashDict.html)deprecated

Tuple-based HashDict implementation.

[HashSet](HashSet.html)deprecated

Tuple-based HashSet implementation.

[IO](IO.html)

Functions handling input/output (IO).

[IO.ANSI](IO.ANSI.html)

Functionality to render ANSI escape sequences.

[IO.Stream](IO.Stream.html)

Defines an `IO.Stream` struct returned by `IO.stream/2` and `IO.binstream/2`.

[IO.StreamError](IO.StreamError.html)[Inspect](Inspect.html)

The `Inspect` protocol converts an Elixir data structure into an algebra document.

[Inspect.Algebra](Inspect.Algebra.html)

A set of functions for creating and manipulating algebra documents.

[Inspect.Error](Inspect.Error.html)

Raised when a struct cannot be inspected.

[Inspect.Opts](Inspect.Opts.html)

Defines the options used by the `Inspect` protocol.

[Integer](Integer.html)

Functions for working with integers.

[JSON](JSON.html)

JSON encoding and decoding.

[JSON.DecodeError](JSON.DecodeError.html)

The exception raised by `JSON.decode!/1`.

[JSON.Encoder](JSON.Encoder.html)

A protocol for custom JSON encoding of data structures.

[Kernel](Kernel.html)

`Kernel` is Elixir's default environment.

[Kernel.ParallelCompiler](Kernel.ParallelCompiler.html)

A module responsible for compiling and requiring files in parallel.

[Kernel.SpecialForms](Kernel.SpecialForms.html)

Special forms are the basic building blocks of Elixir, and therefore cannot be overridden by the developer.

[Kernel.TypespecError](Kernel.TypespecError.html)

An exception raised when there's an error in a typespec.

[KeyError](KeyError.html)

An exception raised when a key is not found in a data structure.

[Keyword](Keyword.html)

A keyword list is a list that consists exclusively of two-element tuples.

[List](List.html)

Linked lists hold zero, one, or more elements in the chosen order.

[List.Chars](List.Chars.html)

The `List.Chars` protocol is responsible for converting a structure to a charlist (only if applicable).

[Macro](Macro.html)

Functions for manipulating AST and implementing macros.

[Macro.Env](Macro.Env.html)

A struct that holds compile time environment information.

[Map](Map.html)

Maps are the "go to" key-value data structure in Elixir.

[MapSet](MapSet.html)

Functions that work on sets.

[MatchError](MatchError.html)

An exception raised when a pattern match (`=/2`) fails.

[MismatchedDelimiterError](MismatchedDelimiterError.html)

An exception raised when a mismatched delimiter is found when parsing code.

[MissingApplicationsError](MissingApplicationsError.html)

An exception that is raised when an application depends on one or more missing applications.

[Module](Module.html)

Provides functions to deal with modules during compilation time.

[NaiveDateTime](NaiveDateTime.html)

A NaiveDateTime struct (without a time zone) and functions.

[Node](Node.html)

Functions related to VM nodes.

[OptionParser](OptionParser.html)

Functions for parsing command line arguments.

[OptionParser.ParseError](OptionParser.ParseError.html)

An exception raised when parsing option fails.

[PartitionSupervisor](PartitionSupervisor.html)

A supervisor that starts multiple partitions of the same child.

[Path](Path.html)

This module provides conveniences for manipulating or retrieving file system paths.

[Port](Port.html)

Functions for interacting with the external world through ports.

[Process](Process.html)

Conveniences for working with processes and the process dictionary.

[Protocol](Protocol.html)

Reference and functions for working with protocols.

[Protocol.UndefinedError](Protocol.UndefinedError.html)

An exception raised when a protocol is not implemented for a given value.

[Range](Range.html)

Ranges represent a sequence of zero, one or many, ascending or descending integers with a common difference called step.

[Record](Record.html)

Module to work with, define, and import records.

[Regex](Regex.html)

Provides regular expressions for Elixir.

[Regex.CompileError](Regex.CompileError.html)

An exception raised when a regular expression could not be compiled.

[Registry](Registry.html)

A local, decentralized and scalable key-value process storage.

[RuntimeError](RuntimeError.html)

An exception for a generic runtime error.

[Set](Set.html)deprecated

Generic API for sets.

[Stream](Stream.html)

Functions for creating and composing streams.

[String](String.html)

Strings in Elixir are UTF-8 encoded binaries.

[String.Chars](String.Chars.html)

The `String.Chars` protocol is responsible for converting a structure to a binary (only if applicable).

[StringIO](StringIO.html)

Controls an IO device process that wraps a string.

[Supervisor](Supervisor.html)

A behaviour module for implementing supervisors.

[Supervisor.Spec](Supervisor.Spec.html)deprecated

Outdated functions for building child specifications.

[SyntaxError](SyntaxError.html)

An exception raised when there's a syntax error when parsing code.

[System](System.html)

The `System` module provides functions that interact directly with the VM or the host system.

[System.EnvError](System.EnvError.html)

An exception raised when a system environment variable is not set.

[SystemLimitError](SystemLimitError.html)

An exception raised when a system limit has been reached.

[Task](Task.html)

Conveniences for spawning and awaiting tasks.

[Task.Supervisor](Task.Supervisor.html)

A task supervisor.

[Time](Time.html)

A Time struct and functions.

[TokenMissingError](TokenMissingError.html)

An exception raised when a token is missing when parsing code.

[TryClauseError](TryClauseError.html)

An exception raised when none of the `else` clauses in a `try/1` match.

[Tuple](Tuple.html)

Functions for working with tuples.

[URI](URI.html)

Utilities for working with URIs.

[URI.Error](URI.Error.html)

An exception raised when an error occurs when a `URI` is invalid.

[UndefinedFunctionError](UndefinedFunctionError.html)

An exception raised when a function is invoked that is not defined.

[UnicodeConversionError](UnicodeConversionError.html)

An exception raised when converting data to or from Unicode.

[Version](Version.html)

Functions for parsing and matching versions against requirements.

[Version.InvalidRequirementError](Version.InvalidRequirementError.html)

An exception raised when a version requirement is invalid.

[Version.InvalidVersionError](Version.InvalidVersionError.html)

An exception raised when a version is invalid.

[Version.Requirement](Version.Requirement.html)

A struct that holds version requirement information.

[WithClauseError](WithClauseError.html)

An exception raised when a term in a `with/1` expression does not match any of the defined `->` clauses in its `else`.

 Search HexDocs [Download ePub version](Elixir.epub)

 Built using [ExDoc](https://github.com/elixir-lang/ex_doc) (v0.39.1) for the [Elixir programming language](https://elixir-lang.org)
