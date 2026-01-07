Go FAQ | Protocol Buffers Documentation[Protocol Buffers Documentation](/)

- [Protocol Buffers](/)

  - [Overview](/overview/)
  - [Protoc Installation](/installation/)
  - [News](/news/)
  - [Programming Guides](/programming-guides/)

    - [Language Guide (editions)](/programming-guides/editions/)
    - [Language Guide (proto 2)](/programming-guides/proto2/)
    - [Language Guide (proto 3)](/programming-guides/proto3/)
    - [Proto Limits](/programming-guides/proto-limits/)
    - [Style Guide](/programming-guides/style/)
    - [Enum Behavior](/programming-guides/enum/)
    - [Encoding](/programming-guides/encoding/)
    - [ProtoJSON Format](/programming-guides/json/)
    - [Techniques](/programming-guides/techniques/)
    - [Add-ons](/programming-guides/addons/)
    - [Extension Declarations](/programming-guides/extension_declarations/)
    - [Field Presence](/programming-guides/field_presence/)
    - [Proto Serialization Is Not Canonical](/programming-guides/serialization-not-canonical/)
    - [Deserializing Debug Proto Representations](/programming-guides/deserialize-debug/)

  - [Protobuf Editions](/editions/)

    - [Overview](/editions/overview/)
    - [Feature Settings for Editions](/editions/features/)
    - [Implementing Editions Support](/editions/implementation/)

  - [Design Decisions](/design-decisions/)

    - [No Nullable Setters/Getters Support](/design-decisions/nullable-getters-setters/)

  - [Proto Best Practices](/best-practices/)

    - [Avoid Cargo Culting](/best-practices/no-cargo-cults/)
    - [Proto Best Practices](/best-practices/dos-donts/)
    - [1-1-1 Best Practice](/best-practices/1-1-1/)

  - [Tutorials](/getting-started/)

    - [C++](/getting-started/cpptutorial/)
    - [C#](/getting-started/csharptutorial/)
    - [Dart](/getting-started/darttutorial/)
    - [Go](/getting-started/gotutorial/)
    - [Java](/getting-started/javatutorial/)
    - [Kotlin](/getting-started/kotlintutorial/)
    - [Python](/getting-started/pythontutorial/)

  - [Reference Guides](/reference/)

    - [C++](/reference/cpp/)

      - [Generated Code Guide](/reference/cpp/cpp-generated/)
      - [String View APIs](/reference/cpp/string-view/)
      - [Arena Allocation Guide](/reference/cpp/arenas/)
      - [Abseil Support](/reference/cpp/abseil/)
      - [C++ API](/reference/cpp/api-docs/)

    - [C#](/reference/csharp/)

      - [Generated Code Guide](/reference/csharp/csharp-generated/)
      - [C# API](/reference/csharp/api-docs)

    - [Dart](/reference/dart/)

      - [Generated Code](/reference/dart/dart-generated/)
      - [Dart API](https://pub.dartlang.org/documentation/protobuf)

    - [Go](/reference/go/)

      - [Generated Code Guide (Open)](/reference/go/go-generated/)
      - [Generated Code Guide (Opaque)](/reference/go/go-generated-opaque/)
      - [FAQ](/reference/go/faq/)
      - [Size Semantics](/reference/go/size/)
      - [Go API](https://pkg.go.dev/google.golang.org/protobuf/proto)
      - [Opaque API Migration](/reference/go/opaque-migration/)
      - [Opaque API: Manual Migration](/reference/go/opaque-migration-manual/)
      - [Opaque API FAQ](/reference/go/opaque-faq/)

    - [Java](/reference/java/)

      - [Generated Code Guide](/reference/java/java-generated/)
      - [Generated Proto Names](/reference/java/java-proto-names/)
      - [Java API](/reference/java/api-docs/overview-summary.html)

    - [Kotlin](/reference/kotlin/)

      - [Kotlin](/reference/kotlin/api-docs/)
      - [Generated Code Guide](/reference/kotlin/kotlin-generated/)

    - [Objective-C](/reference/objective-c/)

      - [Generated Code Guide](/reference/objective-c/objective-c-generated/)

    - [PHP](/reference/php/)

      - [Generated Code Guide](/reference/php/php-generated/)
      - [PHP API](/reference/php/api-docs/)

    - [Python](/reference/python/)

      - [Generated Code Guide](/reference/python/python-generated/)
      - [Python Comparison](/reference/python/python-comparison/)
      - [Python API](https://googleapis.dev/python/protobuf/latest/)

    - [Ruby](/reference/ruby/)

      - [Generated Code Guide](/reference/ruby/ruby-generated/)

    - [Rust](/reference/rust/)

      - [Generated Code Guide](/reference/rust/rust-generated/)
      - [Redaction in Rust](/reference/rust/rust-redaction/)
      - [Building Rust Protos](/reference/rust/building-rust-protos/)
      - [Design Decisions](/reference/rust/rust-design-decisions/)

    - [Protocol Buffers](/reference/protobuf/)

      - [2023 Language Specification](/reference/protobuf/edition-2023-spec/)
      - [Language Specification (Proto2 Syntax)](/reference/protobuf/proto2-spec/)
      - [2024 Language Specification](/reference/protobuf/edition-2024-spec/)
      - [Language Specification (Proto3)](/reference/protobuf/proto3-spec/)
      - [Text Format Language Specification](/reference/protobuf/textformat-spec/)
      - [MIME Types](/reference/protobuf/mime-types/)
      - [Well-Known Types](/reference/protobuf/google.protobuf/)

    - [Other Languages](/reference/other/)

  - [Support](/support/)

    - [Version Support](/support/version-support/)
    - [Migration Guide](/support/migration/)
    - [Cross-Version Runtime Guarantee](/support/cross-version-runtime-guarantee/)

  - [Downloads](/downloads/)
  - [History](/history/)
  - [Forum](https://groups.google.com/g/protobuf)
  - /navbar/
  - [Search Results](/search/)

[View page source](https://github.com/protocolbuffers/protocolbuffers.github.io/tree/main/content/reference/go/faq.md)[Edit this page](https://github.com/protocolbuffers/protocolbuffers.github.io/edit/main/content/reference/go/faq.md)[Create child page](https://github.com/protocolbuffers/protocolbuffers.github.io/new/main/content/reference/go/faq.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create documentation issue](https://github.com/protocolbuffers/protocolbuffers.github.io/issues/new?title=Go%20FAQ)[Create project issue](https://github.com/protocolbuffers/protobuf/issues/new)

- [Versions](#versions)

  - [What’s the difference between github.com/golang/protobuf and google.golang.org/protobuf?](#modules)
  - [What are proto1, proto2, proto3, and editions?](#proto-versions)
  - [There are several different Message types. Which should I use?](#message-types)

- [Common problems](#common-problems)

  - [“go install”: working directory is not part of a module](#working-directory)
  - [constant -1 overflows protoimpl.EnforceVersion](#enforce-version)
  - [undefined: "github.com/golang/protobuf/proto".ProtoPackageIsVersion4](#enforce-version-apiv1)
  - [What is a protocol buffer namespace conflict?](#namespace-conflict)
  - [How do I fix a protocol buffer namespace conflict?](#fix-namespace-conflict)
  - [How do I use protocol buffer editions?](#using-editions)
  - [How do I control the behavior of my generated Go code?](#controlling-generated-code)
  - [Why does reflect.DeepEqual behave unexpectedly with protobuf messages?](#deepequal)

- [Hyrum’s Law](#hyrums-law)

  - [What is Hyrum’s Law, and why is it in this FAQ?](#hyrums-law)
  - [Why does the text of errors keep changing?](#unstable-errors)
  - [protojson](https://pkg.go.dev/google.golang.org/protobuf/encoding/protojson) keep changing?
  - [prototext](https://pkg.go.dev/google.golang.org/protobuf/encoding/prototext) keep changing?

- [Miscellaneous](#miscellaneous)

  - [How do I use a protocol buffer message as a hash key?](#hash)
  - [Can I add a new feature to the Go protocol buffer implementation?](#new-feature)
  - [Can I add an option to Marshal or Unmarshal to customize it?](#new-marshal-option)
  - [Can I customize the code generated by protoc-gen-go?](#custom-code)

1. [Reference Guides](/reference/)
2. [Go](/reference/go/)
3. FAQ

# Go FAQ

A list of frequently asked questions about implementing protocol buffers in Go, with answer for each.

## Versions

### What’s the difference between `github.com/golang/protobuf` and `google.golang.org/protobuf`?

The [github.com/golang/protobuf](https://pkg.go.dev/github.com/golang/protobuf?tab=overview) module is the original Go protocol buffer API.

The [google.golang.org/protobuf](https://pkg.go.dev/google.golang.org/protobuf?tab=overview) module is an updated version of this API designed for simplicity, ease of use, and safety. The flagship features of the updated API are support for reflection and a separation of the user-facing API from the underlying implementation.

We recommend that you use `google.golang.org/protobuf` in new code.

Version `v1.4.0` and higher of `github.com/golang/protobuf` wrap the new implementation and permit programs to adopt the new API incrementally. For example, the well-known types defined in `github.com/golang/protobuf/ptypes` are simply aliases of those defined in the newer module. Thus, [google.golang.org/protobuf/types/known/emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb) and [github.com/golang/protobuf/ptypes/empty](https://pkg.go.dev/github.com/golang/protobuf/ptypes/empty) may be used interchangeably.

### What are `proto1`, `proto2`, `proto3`, and editions?

These are revisions of the protocol buffer language. It is different from the Go implementation of protobufs.

- 

Editions are the newest and recommended way of writing Protocol Buffers. New features will be released as part of new editions. For more information, see [Protocol Buffer Editions](/editions).

- 

`proto3` is a legacy version of the language. We encourage new code to use editions.

- 

`proto2` is a legacy version of the language. Despite being superseded by proto3 and editions, proto2 is still fully supported.

- 

`proto1` is an obsolete version of the language. It was never released as open source.

### There are several different `Message` types. Which should I use?

- 

["google.golang.org/protobuf/proto".Message](https://pkg.go.dev/google.golang.org/protobuf/proto?tab=doc#Message) is an interface type implemented by all messages generated by the current version of the protocol buffer compiler. Functions that operate on arbitrary messages, such as [proto.Marshal](https://pkg.go.dev/google.golang.org/protobuf/proto?tab=doc#Marshal) or [proto.Clone](https://pkg.go.dev/google.golang.org/protobuf/proto?tab=doc#Clone), accept or return this type.

- 

["google.golang.org/protobuf/reflect/protoreflect".Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect?tab=doc#Message) is an interface type describing a reflection view of a message.

Call the `ProtoReflect` method on a `proto.Message` to get a `protoreflect.Message`.

- 

["google.golang.org/protobuf/reflect/protoreflect".ProtoMessage](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect?tab=doc#ProtoMessage) is an alias of `"google.golang.org/protobuf/proto".Message`. The two types are interchangeable.

- 

["github.com/golang/protobuf/proto".Message](https://pkg.go.dev/github.com/golang/protobuf/proto?tab=doc#Message) is an interface type defined by the legacy Go protocol buffer API. All generated message types implement this interface, but the interface does not describe the behavior expected from these messages. New code should avoid using this type.

## Common problems

### “`go install`”: `working directory is not part of a module`

On Go 1.15 and below, you have set the environment variable `GO111MODULE=on` and are running the `go install` command outside of a module directory. Set `GO111MODULE=auto`, or unset the environment variable.

On Go 1.16 and above, `go install` can be invoked outside of a module by specifying an explicit version: `go install google.golang.org/protobuf/cmd/protoc-gen-go@latest`

### `constant -1 overflows protoimpl.EnforceVersion`

You are using a generated `.pb.go` file which requires a newer version of the `"google.golang.org/protobuf"` module.

Update to a newer version with:

```
go get -u google.golang.org/protobuf/proto
```

### `undefined: "github.com/golang/protobuf/proto".ProtoPackageIsVersion4`

You are using a generated `.pb.go` file which requires a newer version of the `"github.com/golang/protobuf"` module.

Update to a newer version with:

```
go get -u github.com/golang/protobuf/proto
```

### What is a protocol buffer namespace conflict?

All protocol buffers declarations linked into a Go binary are inserted into a global registry.

Every protobuf declaration (for example, enums, enum values, or messages) has an absolute name, which is the concatenation of the [package name](/programming-guides/proto2#packages) with the relative name of the declaration in the `.proto` source file (for example, `my.proto.package.MyMessage.NestedMessage`). The protobuf language assumes that all declarations are universally unique.

If two protobuf declarations linked into a Go binary have the same name, then this leads to a namespace conflict, and it is impossible for the registry to properly resolve that declaration by name. Depending on which version of Go protobufs is being used, this will either panic at init-time or silently drop the conflict and lead to a potential bug later during runtime.

### How do I fix a protocol buffer namespace conflict?

The way to best fix a namespace conflict depends on the reason why a conflict is occurring.

Common ways that namespace conflicts occur:

- 

Vendored .proto files. When a single `.proto` file is generated into two or more Go packages and linked into the same Go binary, it conflicts on every protobuf declaration in the generated Go packages. This typically occurs when a `.proto` file is vendored and a Go package is generated from it, or the generated Go package itself is vendored. Users should avoid vendoring and instead depend on a centralized Go package for that `.proto` file.

  - If a `.proto` file is owned by an external party and is lacking a `go_package` option, then you should coordinate with the owner of that `.proto` file to specify a centralized Go package that a plurality of users can all depend on.

- 

Missing or generic proto package names. If a `.proto` file does not specify a package name or uses an overly generic package name (for example, “my_service”), then there is a high probability that declarations within that file will conflict with other declarations elsewhere in the universe. We recommend that every `.proto` file have a package name that is deliberately chosen to be universally unique (for example, prefixed with the name of a company).

#### Warning

Retroactively changing the package name on a `.proto` file is not backwards compatible for types used as extension fields, stored in `google.protobuf.Any`, or for gRPC Service definitions.

Starting with v1.26.0 of the `google.golang.org/protobuf` module, a hard error will be reported when a Go program starts up that has multiple conflicting protobuf names linked into it. While it is preferable that the source of the conflict be fixed, the fatal error can be immediately worked around in one of two ways:

1. 

At compile time. The default behavior for handling conflicts can be specified at compile time with a linker-initialized variable: `go build -ldflags "-X google.golang.org/protobuf/reflect/protoregistry.conflictPolicy=warn"`

2. 

At program execution. The behavior for handling conflicts when executing a particular Go binary can be set with an environment variable: `GOLANG_PROTOBUF_REGISTRATION_CONFLICT=warn ./main`

### How do I use protocol buffer editions?

To use a protobuf edition, you must specify the edition in your `.proto` file. For example, to use the 2023 edition, add the following to the top of your `.proto` file:

```
edition = "2023";
```

The protocol buffer compiler will then generate Go code that is compatible with the specified edition. With editions, you can also enable or disable specific features for your `.proto` file. For more information, see [Protocol Buffer Editions](/editions/overview).

### How do I control the behavior of my generated Go code?

With editions, you can control the behavior of the generated Go code by enabling or disabling specific features in your `.proto` file. For example, to set the API behavior for your implementation, you would add the following to your `.proto` file:

```
edition = "2023";

option features.(pb.go).api_level = API_OPAQUE;
```

When `api_level` is set to `API_OPAQUE`, the Go code generated by the protocol buffer compiler hides struct fields so they can no longer be directly accessed. Instead, new accessor methods are created for getting, setting, or clearing a field.

For a complete list of available features and their descriptions, see [Features for Editions](/editions/features).

### Why does `reflect.DeepEqual` behave unexpectedly with protobuf messages?

Generated protocol buffer message types include internal state which can vary even between equivalent messages.

In addition, the `reflect.DeepEqual` function is not aware of the semantics of protocol buffer messages, and can report differences where none exist. For example, a map field containing a `nil` map and one containing a zero-length, non-`nil` map are semantically equivalent, but will be reported as unequal by `reflect.DeepEqual`.

Use the [proto.Equal](https://pkg.go.dev/google.golang.org/protobuf/proto#Equal) function to compare message values.

In tests, you can also use the ["github.com/google/go-cmp/cmp"](https://pkg.go.dev/github.com/google/go-cmp/cmp?tab=doc) package with the [protocmp.Transform()](https://pkg.go.dev/google.golang.org/protobuf/testing/protocmp#Transform) option. The `cmp` package can compare arbitrary data structures, and [cmp.Diff](https://pkg.go.dev/github.com/google/go-cmp/cmp#Diff) produces human-readable reports of the differences between values.

```
if diff := cmp.Diff(a, b, protocmp.Transform()); diff != "" {
  t.Errorf("unexpected difference:\n%v", diff)
}
```

## Hyrum’s Law

### What is Hyrum’s Law, and why is it in this FAQ?

[Hyrum’s Law](https://www.hyrumslaw.com/) states:

With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.

A design goal of the latest version of the Go protocol buffer API is to avoid, where possible, providing observable behaviors that we cannot promise to keep stable in the future. It is our philosophy that deliberate instability in areas where we make no promises is better than giving the illusion of stability, only for that to change in the future after a project has potentially been long depending on that false assumption.

### Why does the text of errors keep changing?

Tests depending on the exact text of errors are brittle and break often when that text changes. To discourage unsafe use of error text in tests, the text of errors produced by this module is deliberately unstable.

If you need to identify whether an error is produced by the [protobuf](https://pkg.go.dev/mod/google.golang.org/protobuf) module, we guarantee that all errors will match [proto.Error](https://pkg.go.dev/google.golang.org/protobuf/proto?tab=doc#Error) according to [errors.Is](https://pkg.go.dev/errors?tab=doc#Is).

### Why does the output of [protojson](https://pkg.go.dev/google.golang.org/protobuf/encoding/protojson) keep changing?

We make no promises about the long-term stability of Go’s implementation of the [JSON format for protocol buffers](/programming-guides/proto3#json). The specification only specifies what is valid JSON, but provides no specification for a canonical format for how a marshaler ought to exactly format a given message. To avoid giving the illusion that the output is stable, we deliberately introduce minor differences so that byte-for-byte comparisons are likely to fail.

To gain some degree of output stability, we recommend running the output through a JSON formatter.

### Why does the output of [prototext](https://pkg.go.dev/google.golang.org/protobuf/encoding/prototext) keep changing?

We make no promises about the long-term stability of Go’s implementation of the text format. There is no canonical specification of the protobuf text format, and we would like to preserve the ability to make improvements in the `prototext` package output in the future. Since we don’t promise stability in the package’s output, we’ve deliberately introduced instability to discourage users from depending on it.

To obtain some degree of stability, we recommend passing the output of `prototext` through the [txtpbfmt](https://github.com/protocolbuffers/txtpbfmt) program. The formatter can be directly invoked in Go using [parser.Format](https://pkg.go.dev/github.com/protocolbuffers/txtpbfmt/parser?tab=doc#Format).

## Miscellaneous

### How do I use a protocol buffer message as a hash key?

You need canonical serialization, where the marshaled output of a protocol buffer message is guaranteed to be stable over time. Unfortunately, no specification for canonical serialization exists at this time. You’ll need to write your own or find a way to avoid needing one.

### Can I add a new feature to the Go protocol buffer implementation?

Maybe. We always like suggestions, but we’re very cautious about adding new things.

The Go implementation of protocol buffers strives to be consistent with the other language implementations. As such, we tend to shy away from feature that are overly specialized to just Go. Go-specific features hinder the goal of protocol buffers being a language-neutral data interchange format.

Unless your idea is specific to the Go implementation, you should join the [protobuf discussion group](http://groups.google.com/group/protobuf) and suggest it there.

If you have an idea for the Go implementation, file an issue on our issue tracker: [https://github.com/golang/protobuf/issues](https://github.com/golang/protobuf/issues)

### Can I add an option to `Marshal` or `Unmarshal` to customize it?

Only if that option exists in other implementations (e.g., C++, Java). The encoding of protocol buffers (binary, JSON, and text) must be consistent across implementations, so a program written in one language is able to read messages written by another one.

We will not add any options to the Go implementation that affect the data output by `Marshal` functions or read by `Unmarshal` functions unless an equivalent option exist in at least one other supported implementation.

### Can I customize the code generated by `protoc-gen-go`?

In general, no. Protocol buffers are intended to be a language-agnostic data interchange format, and implementation-specific customizations run counter to that intent.

- https://stackoverflow.com/questions/tagged/protocol-buffers

- https://github.com/protocolbuffers/protobuf
- https://groups.google.com/g/protobuf

© 2026 Google LLC All Rights Reserved[Privacy Policy](https://policies.google.com/privacy)Hosted by GitHub Pages.[GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
