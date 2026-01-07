Clang C Language Family Frontend for LLVM[LLVM Home](http://llvm.org/)Clang Info[Download](http://llvm.org/releases/download.html)[About](/index.html)[Features](/features.html)[Related Projects](/related.html)[User's Manual](/docs/UsersManual.html)[Language Compatibility](/compatibility.html)[Language Extensions](/docs/LanguageExtensions.html)[C Status](/c_status.html)[C++ Status](/cxx_status.html)Clang Development[Get Started](/get_started.html)[Get Involved](/get_involved.html)[Open Projects](/OpenProjects.html)[Clang Internals](/docs/InternalsManual.html)[Hacking on Clang](/hacking.html)Clang Tools[Automatic Bug-Finding](http://clang-analyzer.llvm.org)[Writing Clang Tools](/docs/Tooling.html)Communication[Clang Forum](https://discourse.llvm.org/c/clang)[cfe-commits List](http://lists.llvm.org/mailman/listinfo/cfe-commits)[Bug Reports](https://github.com/llvm/llvm-project/issues)[Discord](https://discord.gg/2kQU7PCuys)The Code[Check Out Sources](/get_started.html#build)[Browse Sources](https://github.com/llvm/llvm-project/tree/main/clang/)[doxygen](http://clang.llvm.org/doxygen/)Clang Events[LLVM Meeting](http://llvm.org/devmtg/)

# Clang: a C language family frontend for LLVM

The Clang project provides a language front-end and tooling infrastructure for languages in the C language family (C, C++, Objective C/C++, OpenCL, and CUDA) for the [LLVM](https://www.llvm.org/) project. Both a GCC-compatible compiler driver (clang) and an MSVC-compatible compiler driver (clang-cl.exe) are provided. You can [get and build](get_started.html) the source today.

## Features and Goals

Some of the goals for the project include the following:

[End-User Features](features.html#enduser):

- Fast compiles and low memory use
- Expressive diagnostics ([examples](diagnostics.html))
- GCC & MSVC compatibility

[Utility and
     Applications](features.html#applications):

- Modular library based architecture
- Support diverse clients (refactoring, static analysis, code generation, etc.)
- Allow tight integration with IDEs
- Use the LLVM 'Apache 2' [License](https://github.com/llvm/llvm-project/blob/main/LICENSE.TXT)

[Internal Design and
     Implementation](features.html#design):

- A real-world, production quality compiler
- A simple and hackable code base
- A single unified parser for C, Objective C, C++, and Objective C++
- Conformance with C/C++/ObjC and their variants

Of course this is only a rough outline of the goals and features of Clang. To get a true sense of what it is all about, see the [Features](features.html) section, which breaks each of these down and explains them in more detail.

## Why?

Development of the new front-end was started out of a need for a compiler that allows better diagnostics, better integration with IDEs, a license that is compatible with commercial products, and a nimble compiler that is easy to develop and maintain. All of these were motivations for starting work on a new front-end that could meet these needs.

## Current Status

Clang is considered to be a production quality C, Objective-C, C++ and Objective-C++ compiler when targeting any target supported by LLVM. As example, Clang is used in production to build performance-critical software like Chrome or Firefox. 
 If you are looking for source analysis or source-to-source transformation tools, Clang is probably a great solution for you. Please see the [C++ status](cxx_status.html) page or the [C status](c_status.html) page for more information about what standard modes and features are supported.

## Get it and get involved!

Start by [getting the code, building it, and
     playing with it](get_started.html). This will show you the sorts of things we can do today and will let you have the "Clang experience" first hand: hopefully it will "resonate" with you. :)

Once you've done that, please consider [getting
     involved in the Clang community](get_involved.html). The Clang developers include numerous volunteer contributors with a variety of backgrounds. If you're interested in following the development of Clang, signing up for a mailing list is a good way to learn about how the project works.
