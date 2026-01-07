Encoding | Protocol Buffers Documentation[Protocol Buffers Documentation](/)

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

[View page source](https://github.com/protocolbuffers/protocolbuffers.github.io/tree/main/content/programming-guides/encoding.md)[Edit this page](https://github.com/protocolbuffers/protocolbuffers.github.io/edit/main/content/programming-guides/encoding.md)[Create child page](https://github.com/protocolbuffers/protocolbuffers.github.io/new/main/content/programming-guides/encoding.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)[Create documentation issue](https://github.com/protocolbuffers/protocolbuffers.github.io/issues/new?title=Encoding)[Create project issue](https://github.com/protocolbuffers/protobuf/issues/new)

- [A Simple Message](#simple)
- [Base 128 Varints](#varints)
- [Message Structure](#structure)
- [More Integer Types](#int-types)

  - [Bools and Enums](#bools-and-enums)
  - [Signed Integers](#signed-ints)
  - [Non-varint Numbers](#non-varints)

- [Length-Delimited Records](#length-types)

  - [Submessages](#embedded)

- [Missing Elements](#optional)
- [Repeated Elements](#repeated)

  - [Oneofs](#oneofs)
  - [Last One Wins](#last-one-wins)
  - [Maps](#maps)

- [Groups](#groups)
- [Field Order](#order)

  - [Implications](#implications)

- [Encoded Proto Size Limitations](#size-limit)
- [Condensed Reference Card](#cheat-sheet)

  - [Key](#cheat-sheet-key)

1. [Programming Guides](/programming-guides/)
2. Encoding

# Encoding

Explains how Protocol Buffers encodes data to files or to the wire.

This document describes the protocol buffer wire format, which defines the details of how your message is sent on the wire and how much space it consumes on disk. You probably don’t need to understand this to use protocol buffers in your application, but it’s useful information for doing optimizations.

If you already know the concepts but want a reference, skip to the [Condensed reference card](#cheat-sheet) section.

[Protoscope](https://github.com/protocolbuffers/protoscope) is a very simple language for describing snippets of the low-level wire format, which we’ll use to provide a visual reference for the encoding of various messages. Protoscope’s syntax consists of a sequence of tokens that each encode down to a specific byte sequence.

For example, backticks denote a raw hex literal, like ``70726f746f6275660a``. This encodes into the exact bytes denoted as hex in the literal. Quotes denote UTF-8 strings, like `"Hello, Protobuf!"`. This literal is synonymous with ``48656c6c6f2c2050726f746f62756621`` (which, if you observe closely, is composed of ASCII bytes). We’ll introduce more of the Protoscope language as we discuss aspects of the wire format.

The Protoscope tool can also dump encoded protocol buffers as text. See [https://github.com/protocolbuffers/protoscope/tree/main/testdata](https://github.com/protocolbuffers/protoscope/tree/main/testdata) for examples.

All examples in this topic assume that you are using Edition 2023 or later.

## A Simple Message

Let’s say you have the following very simple message definition:

```
message Test1 {
  int32 a = 1;
}
```

In an application, you create a `Test1` message and set `a` to 150. You then serialize the message to an output stream. If you were able to examine the encoded message, you’d see three bytes:

```
08 96 01
```

So far, so small and numeric – but what does it mean? If you use the Protoscope tool to dump those bytes, you’d get something like `1: 150`. How does it know this is the contents of the message?

## Base 128 Varints

Variable-width integers, or varints, are at the core of the wire format. They allow encoding unsigned 64-bit integers using anywhere between one and ten bytes, with small values using fewer bytes.

Each byte in the varint has a continuation bit that indicates if the byte that follows it is part of the varint. This is the most significant bit (MSB) of the byte (sometimes also called the sign bit). The lower 7 bits are a payload; the resulting integer is built by appending together the 7-bit payloads of its constituent bytes.

So, for example, here is the number 1, encoded as ``01`` – it’s a single byte, so the MSB is not set:

```
0000 0001
^ msb
```

And here is 150, encoded as ``9601`` – this is a bit more complicated:

```
10010110 00000001
^ msb    ^ msb
```

How do you figure out that this is 150? First you drop the MSB from each byte, as this is just there to tell us whether we’ve reached the end of the number (as you can see, it’s set in the first byte as there is more than one byte in the varint). These 7-bit payloads are in little-endian order. Convert to big-endian order, concatenate, and interpret as an unsigned 64-bit integer:

```
10010110 00000001        // Original inputs.
 0010110  0000001        // Drop continuation bits.
 0000001  0010110        // Convert to big-endian.
   00000010010110        // Concatenate.
 128 + 16 + 4 + 2 = 150  // Interpret as an unsigned 64-bit integer.
```

Because varints are so crucial to protocol buffers, in protoscope syntax, we refer to them as plain integers. `150` is the same as ``9601``.

## Message Structure

A protocol buffer message is a series of key-value pairs. The binary version of a message just uses the field’s number as the key – the name and declared type for each field can only be determined on the decoding end by referencing the message type’s definition (i.e. the `.proto` file). Protoscope does not have access to this information, so it can only provide the field numbers.

When a message is encoded, each key-value pair is turned into a record consisting of the field number, a wire type and a payload. The wire type tells the parser how big the payload after it is. This allows old parsers to skip over new fields they don’t understand. This type of scheme is sometimes called [Tag-Length-Value](https://en.wikipedia.org/wiki/Type%E2%80%93length%E2%80%93value), or TLV.

There are six wire types: `VARINT`, `I64`, `LEN`, `SGROUP`, `EGROUP`, and `I32`

IDNameUsed For0VARINTint32, int64, uint32, uint64, sint32, sint64, bool, enum1I64fixed64, sfixed64, double2LENstring, bytes, embedded messages, packed repeated fields3SGROUPgroup start (deprecated)4EGROUPgroup end (deprecated)5I32fixed32, sfixed32, float

The “tag” of a record is encoded as a varint formed from the field number and the wire type via the formula `(field_number << 3) | wire_type`. In other words, after decoding the varint representing a field, the low 3 bits tell us the wire type, and the rest of the integer tells us the field number.

Now let’s look at our simple example again. You now know that the first number in the stream is always a varint key, and here it’s ``08``, or (dropping the MSB):

```
000 1000
```

You take the last three bits to get the wire type (0) and then right-shift by three to get the field number (1). Protoscope represents a tag as an integer followed by a colon and the wire type, so we can write the above bytes as `1:VARINT`.

Because the wire type is 0, or `VARINT`, we know that we need to decode a varint to get the payload. As we saw above, the bytes ``9601`` varint-decode to 150, giving us our record. We can write it in Protoscope as `1:VARINT 150`.

Protoscope can infer the type for a tag if there is whitespace after the `:`. It does so by looking ahead at the next token and guessing what you meant (the rules are documented in detail in [Protoscope’s language.txt](https://github.com/protocolbuffers/protoscope/blob/main/language.txt)). For example, in `1: 150`, there is a varint immediately after the untyped tag, so Protoscope infers its type to be `VARINT`. If you wrote `2: {}`, it would see the `{` and guess `LEN`; if you wrote `3: 5i32` it would guess `I32`, and so on.

## More Integer Types

### Bools and Enums

Bools and enums are both encoded as if they were `int32`s. Bools, in particular, always encode as either ``00`` or ``01``. In Protoscope, `false` and `true` are aliases for these byte strings.

### Signed Integers

As you saw in the previous section, all the protocol buffer types associated with wire type 0 are encoded as varints. However, varints are unsigned, so the different signed types, `sint32` and `sint64` vs `int32` or `int64`, encode negative integers differently.

The `intN` types encode negative numbers as two’s complement, which means that, as unsigned, 64-bit integers, they have their highest bit set. As a result, this means that all ten bytes must be used. For example, `-2` is converted by protoscope into

```
11111110 11111111 11111111 11111111 11111111
11111111 11111111 11111111 11111111 00000001
```

This is the two’s complement of 2, defined in unsigned arithmetic as `~0 - 2 + 1`, where `~0` is the all-ones 64-bit integer. It is a useful exercise to understand why this produces so many ones.

`sintN` uses the “ZigZag” encoding instead of two’s complement to encode negative integers. Positive integers `p` are encoded as `2 * p` (the even numbers), while negative integers `n` are encoded as `2 * |n| - 1` (the odd numbers). The encoding thus “zig-zags” between positive and negative numbers. For example:

Signed OriginalEncoded As00-1112-23……0x7fffffff0xfffffffe-0x800000000xffffffff

In other words, each value `n` is encoded using

```
(n << 1) ^ (n >> 31)
```

for `sint32`s, or

```
(n << 1) ^ (n >> 63)
```

for the 64-bit version.

When the `sint32` or `sint64` is parsed, its value is decoded back to the original, signed version.

In protoscope, suffixing an integer with a `z` will make it encode as ZigZag. For example, `-500z` is the same as the varint `999`.

### Non-varint Numbers

Non-varint numeric types are simple. `double` and `fixed64` have wire type `I64`, which tells the parser to expect a fixed eight-byte lump of data. `double` values are encoded in IEEE 754 double-precision format. We can specify a `double` record by writing `5: 25.4`, or a `fixed64` record with `6: 200i64`.

Similarly `float` and `fixed32` have wire type `I32`, which tells it to expect four bytes instead. `float` values are encoded in IEEE 754 single-precision format. The syntax for these consists of adding an `i32` suffix. `25.4i32` will emit four bytes, as will `200i32`. Tag types are inferred as `I32`.

## Length-Delimited Records

Length prefixes are another major concept in the wire format. The `LEN` wire type has a dynamic length, specified by a varint immediately after the tag, which is followed by the payload as usual.

Consider this message schema:

```
message Test2 {
  string b = 2;
}
```

A record for the field `b` is a string, and strings are `LEN`-encoded. If we set `b` to `"testing"`, we encoded as a `LEN` record with field number 2 containing the ASCII string `"testing"`. The result is ``120774657374696e67``. Breaking up the bytes,

```
12 07 [74 65 73 74 69 6e 67]
```

we see that the tag, ``12``, is `00010 010`, or `2:LEN`. The byte that follows is the int32 varint `7`, and the next seven bytes are the UTF-8 encoding of `"testing"`. The int32 varint means that the max length of a string is 2GB.

In Protoscope, this is written as `2:LEN 7 "testing"`. However, it can be inconvenient to repeat the length of the string (which, in Protoscope text, is already quote-delimited). Wrapping Protoscope content in braces will generate a length prefix for it: `{"testing"}` is a shorthand for `7 "testing"`. `{}` is always inferred by fields to be a `LEN` record, so we can write this record simply as `2: {"testing"}`.

`bytes` fields are encoded in the same way.

### Submessages

Submessage fields also use the `LEN` wire type. Here’s a message definition with an embedded message of our original example message, `Test1`:

```
message Test3 {
  Test1 c = 3;
}
```

If `Test1`’s `a` field (i.e., `Test3`’s `c.a` field) is set to 150, we get ```1a03089601```. Breaking it up:

```
 1a 03 [08 96 01]
```

The last three bytes (in `[]`) are exactly the same ones from our [very first example](#simple). These bytes are preceded by a `LEN`-typed tag, and a length of 3, exactly the same way as strings are encoded.

In Protoscope, submessages are quite succinct. ```1a03089601``` can be written as `3: {1: 150}`.

## Missing Elements

Missing fields are easy to encode: we just leave out the record if it’s not present. This means that “huge” protos with only a few fields set are quite sparse.

## Repeated Elements

Starting in Edition 2023, `repeated` fields of a primitive type (any [scalar type](/programming-guides/proto2#scalar) that is not `string` or `bytes`) are [“packed”](/editions/features#repeated_field_encoding) by default.

Packed `repeated` fields, instead of being encoded as one record per entry, are encoded as a single `LEN` record that contains each element concatenated. To decode, elements are decoded from the `LEN` record one by one until the payload is exhausted. The start of the next element is determined by the length of the previous, which itself depends on the type of the field. Thus, if we have:

```
message Test4 {
  string d = 4;
  repeated int32 e = 6;
}
```

and we construct a `Test4` message with `d` set to `"hello"`, and `e` set to `1`, `2`, and `3`, this could be encoded as ``3206038e029ea705``, or written out as Protoscope,

```
4: {"hello"}
6: {3 270 86942}
```

However, if the repeated field is set to expanded (overriding the default packed state) or is not packable (strings and messages) then an entry for each individual value is encoded. Also, records for `e` do not need to appear consecutively, and can be interleaved with other fields; only the order of records for the same field with respect to each other is preserved. Thus, this could look like the following:

```
6: 1
6: 2
4: {"hello"}
6: 3
```

Only repeated fields of primitive numeric types can be declared “packed”. These are types that would normally use the `VARINT`, `I32`, or `I64` wire types.

Note that although there’s usually no reason to encode more than one key-value pair for a packed repeated field, parsers must be prepared to accept multiple key-value pairs. In this case, the payloads should be concatenated. Each pair must contain a whole number of elements. The following is a valid encoding of the same message above that parsers must accept:

```
6: {3 270}
6: {86942}
```

Protocol buffer parsers must be able to parse repeated fields that were compiled as `packed` as if they were not packed, and vice versa. This permits adding `[packed=true]` to existing fields in a forward- and backward-compatible way.

### Oneofs

[Oneof fields](/programming-guides/proto2#oneof) are encoded the same as if the fields were not in a `oneof`. The rules that apply to `oneofs` are independent of how they are represented on the wire.

### Last One Wins

Normally, an encoded message would never have more than one instance of a non-`repeated` field. However, parsers are expected to handle the case in which they do. For numeric types and strings, if the same field appears multiple times, the parser accepts the last value it sees. For embedded message fields, the parser merges multiple instances of the same field, as if with the `Message::MergeFrom` method – that is, all singular scalar fields in the latter instance replace those in the former, singular embedded messages are merged, and `repeated` fields are concatenated. The effect of these rules is that parsing the concatenation of two encoded messages produces exactly the same result as if you had parsed the two messages separately and merged the resulting objects. That is, this:

```
MyMessage message;
message.ParseFromString(str1 + str2);
```

is equivalent to this:

```
MyMessage message, message2;
message.ParseFromString(str1);
message2.ParseFromString(str2);
message.MergeFrom(message2);
```

This property is occasionally useful, as it allows you to merge two messages (by concatenation) even if you do not know their types.

### Maps

Map fields are just a shorthand for a special kind of repeated field. If we have

```
message Test6 {
  map<string, int32> g = 7;
}
```

this is actually the same as

```
message Test6 {
  message g_Entry {
    string key = 1;
    int32 value = 2;
  }
  repeated g_Entry g = 7;
}
```

Thus, maps are encoded almost exactly like a `repeated` message field: as a sequence of `LEN`-typed records, with two fields each. The exception is that order is not guaranteed to be preserved with maps during serialization.

## Groups

Groups are a deprecated feature that should not be used, but they remain in the wire format, and deserve a passing mention.

A group is a bit like a submessage, but it is delimited by special tags rather than by a `LEN` prefix. Each group in a message has a field number, which is used on these special tags.

A group with field number `8` begins with an `8:SGROUP` tag. `SGROUP` records have empty payloads, so all this does is denote the start of the group. Once all the fields in the group are listed, a corresponding `8:EGROUP` tag denotes its end. `EGROUP` records also have no payload, so `8:EGROUP` is the entire record. Group field numbers need to match up. If we encounter `7:EGROUP` where we expect `8:EGROUP`, the message is mal-formed.

Protoscope provides a convenient syntax for writing groups. Instead of writing

```
8:SGROUP
  1: 2
  3: {"foo"}
8:EGROUP
```

Protoscope allows

```
8: !{
  1: 2
  3: {"foo"}
}
```

This will generate the appropriate start and end group markers. The `!{}` syntax can only occur immediately after an un-typed tag expression, like `8:`.

## Field Order

Field numbers may be declared in any order in a `.proto` file. The order chosen has no effect on how the messages are serialized.

When a message is serialized, there is no guaranteed order for how its known or [unknown fields](/programming-guides/proto2#updating) will be written. Serialization order is an implementation detail, and the details of any particular implementation may change in the future. Therefore, protocol buffer parsers must be able to parse fields in any order.

### Implications

- Do not assume the byte output of a serialized message is stable. This is especially true for messages with transitive bytes fields representing other serialized protocol buffer messages.
- By default, repeated invocations of serialization methods on the same protocol buffer message instance may not produce the same byte output. That is, the default serialization is not deterministic.

  - Deterministic serialization only guarantees the same byte output for a particular binary. The byte output may change across different versions of the binary.

- The following checks may fail for a protocol buffer message instance `foo`:

  - `foo.SerializeAsString() == foo.SerializeAsString()`
  - `Hash(foo.SerializeAsString()) == Hash(foo.SerializeAsString())`
  - `CRC(foo.SerializeAsString()) == CRC(foo.SerializeAsString())`
  - `FingerPrint(foo.SerializeAsString()) == FingerPrint(foo.SerializeAsString())`

- Here are a few example scenarios where logically equivalent protocol buffer messages `foo` and `bar` may serialize to different byte outputs:

  - `bar` is serialized by an old server that treats some fields as unknown.
  - `bar` is serialized by a server that is implemented in a different programming language and serializes fields in different order.
  - `bar` has a field that serializes in a non-deterministic manner.
  - `bar` has a field that stores a serialized byte output of a protocol buffer message which is serialized differently.
  - `bar` is serialized by a new server that serializes fields in a different order due to an implementation change.
  - `foo` and `bar` are concatenations of the same individual messages in a different order.

## Encoded Proto Size Limitations

Protos must be smaller than 2 GiB when serialized. Many proto implementations will refuse to serialize or parse messages that exceed this limit.

## Condensed Reference Card

The following provides the most prominent parts of the wire format in an easy-to-reference format.

```
message    := (tag value)*

tag        := (field << 3) bit-or wire_type;
                encoded as uint32 varint
value      := varint      for wire_type == VARINT,
              i32         for wire_type == I32,
              i64         for wire_type == I64,
              len-prefix  for wire_type == LEN,
              <empty>     for wire_type == SGROUP or EGROUP

varint     := int32 | int64 | uint32 | uint64 | bool | enum | sint32 | sint64;
                encoded as varints (sintN are ZigZag-encoded first)
i32        := sfixed32 | fixed32 | float;
                encoded as 4-byte little-endian (float is IEEE 754
                single-precision); memcpy of the equivalent C types (u?int32_t,
                float)
i64        := sfixed64 | fixed64 | double;
                encoded as 8-byte little-endian (double is IEEE 754
                double-precision); memcpy of the equivalent C types (u?int64_t,
                double)

len-prefix := size (message | string | bytes | packed);
                size encoded as int32 varint
string     := valid UTF-8 string (e.g. ASCII);
                max 2GB of bytes
bytes      := any sequence of 8-bit bytes;
                max 2GB of bytes
packed     := varint* | i32* | i64*,
                consecutive values of the type specified in `.proto`
```

See also the [Protoscope Language Reference](https://github.com/protocolbuffers/protoscope/blob/main/language.txt).

### Key

`message := (tag value)*`A message is encoded as a sequence of zero or more pairs of tags and values.`tag := (field << 3) bit-or wire_type`A tag is a combination of a `wire_type`, stored in the least significant three bits, and the field number that is defined in the `.proto` file.`value := varint for wire_type == VARINT, ...`A value is stored differently depending on the `wire_type` specified in the tag.`varint := int32 | int64 | uint32 | uint64 | bool | enum | sint32 | sint64`You can use varint to store any of the listed data types.`i32 := sfixed32 | fixed32 | float`You can use fixed32 to store any of the listed data types.`i64 := sfixed64 | fixed64 | double`You can use fixed64 to store any of the listed data types.`len-prefix := size (message | string | bytes | packed)`A length-prefixed value is stored as a length (encoded as a varint), and then one of the listed data types.`string := valid UTF-8 string (e.g. ASCII)`As described, a string must use UTF-8 character encoding. A string cannot exceed 2GB.`bytes := any sequence of 8-bit bytes`As described, bytes can store custom data types, up to 2GB in size.`packed := varint* | i32* | i64*`Use the `packed` data type when you are storing consecutive values of the type described in the protocol definition. The tag is dropped for values after the first, which amortizes the costs of tags to one per field, rather than per element.

- https://stackoverflow.com/questions/tagged/protocol-buffers

- https://github.com/protocolbuffers/protobuf
- https://groups.google.com/g/protobuf

© 2026 Google LLC All Rights Reserved[Privacy Policy](https://policies.google.com/privacy)Hosted by GitHub Pages.[GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
