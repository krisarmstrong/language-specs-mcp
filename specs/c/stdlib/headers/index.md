C Standard Library headers - cppreference.com

##### [cppreference.com](../../index.html)

[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fheader&type=signup)

- [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fheader)

##### Namespaces

- [Page](header.html)
- [Discussion](../Talk%253Ac/header.html)

##### Variantsheader.html#

##### Views

- [View](header.html)
- [Edit](https://en.cppreference.com/mwiki/index.php?title=c/header&action=edit)
- [History](https://en.cppreference.com/mwiki/index.php?title=c/header&action=history)

##### Actionsheader.html#

# C Standard Library headers

From cppreference.com< [c](../c.html)[C](../c.html)[Compiler support](compiler_support.html)[Language](language.html)Headers[Type support](types.html)[Program utilities](program.html)[Variadic function support](variadic.html)[Error handling](error.html)[Dynamic memory management](memory.html)[Strings library](string.html)[Algorithms](algorithm.html)[Numerics](numeric.html)[Date and time utilities](chrono.html)[Input/output support](io.html)[Localization support](locale.html)[Concurrency support](thread.html)(C11)[Technical Specifications](experimental.html)[Symbol index](index.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit) Standard Library headers [<assert.h>](header/assert.html)[<complex.h>](header/complex.html)(C99)[<ctype.h>](header/ctype.html)[<errno.h>](header/errno.html)[<fenv.h>](header/fenv.html)(C99)[<float.h>](header/float.html)[<inttypes.h>](header/inttypes.html)(C99)[<iso646.h>](header/iso646.html)(C95)[<limits.h>](header/limits.html)[<locale.h>](header/locale.html)[<math.h>](header/math.html)[<setjmp.h>](header/setjmp.html)[<signal.h>](header/signal.html)[<stdalign.h>](header/stdalign.html)(C11*)[<stdarg.h>](header/stdarg.html)[<stdatomic.h>](header/stdatomic.html)(C11)[<stdbit.h>](header/stdbit.html)(C23)[<stdbool.h>](header/stdbool.html)(C99*)[<stdckdint.h>](header/stdckdint.html)(C23)[<stddef.h>](header/stddef.html)[<stdint.h>](header/stdint.html)(C99)[<stdio.h>](header/stdio.html)[<stdlib.h>](header/stdlib.html)[<stdmchar.h>](header/stdmchar.html)(C29)[<stdnoreturn.h>](header/stdnoreturn.html)(C11*)[<string.h>](header/string.html)[<tgmath.h>](header/tgmath.html)(C99)[<threads.h>](header/threads.html)(C11)[<time.h>](header/time.html)[<uchar.h>](header/uchar.html)(C11)[<wchar.h>](header/wchar.html)(C95)[<wctype.h>](header/wctype.html)(C95)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/navbar_content&action=edit)

The interface of C standard library is defined by the following collection of headers. 

[<assert.h>](header/assert.html)[Conditionally compiled macro that compares its argument to zero](error.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_assert&action=edit)[<complex.h>](header/complex.html)(C99)[Complex number arithmetic](numeric/complex.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_complex&action=edit)[<ctype.h>](header/ctype.html)[Functions to determine the type contained in character data](string/byte.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_ctype&action=edit)[<errno.h>](header/errno.html)[Macros reporting error conditions](error.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_errno&action=edit)[<fenv.h>](header/fenv.html)(C99)[Floating-point environment](numeric/fenv.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_fenv&action=edit)[<float.h>](header/float.html)[Limits of floating-point types](types/limits.html#Limits_of_floating-point_types)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_float&action=edit)[<inttypes.h>](header/inttypes.html)(C99)[Format conversion of integer types](types/integer.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_inttypes&action=edit)[<iso646.h>](header/iso646.html)(C95)[Alternative operator spellings](language/operator_alternative.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_iso646&action=edit)[<limits.h>](header/limits.html)[Ranges of integer types](types/limits.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_limits&action=edit)[<locale.h>](header/locale.html)[Localization utilities](locale.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_locale&action=edit)[<math.h>](header/math.html)[Common mathematics functions](numeric/math.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_math&action=edit)[<setjmp.h>](header/setjmp.html)[Nonlocal jumps](program.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_setjmp&action=edit)[<signal.h>](header/signal.html)[Signal handling](program.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_signal&action=edit)[<stdalign.h>](header/stdalign.html)(since C11)(deprecated in C23)[alignas and alignof](types.html) convenience macros[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdalign&action=edit)[<stdarg.h>](header/stdarg.html)[Variable arguments](variadic.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdarg&action=edit)[<stdatomic.h>](header/stdatomic.html)(C11)[Atomic operations](thread.html#Atomic_operations)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdatomic&action=edit)[<stdbit.h>](header/stdbit.html)(C23)[Macros to work with the byte and bit representations of types](numeric.html#Bit_manipulation)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdbit&action=edit)[<stdbool.h>](header/stdbool.html)(since C99)(deprecated in C23)[Macros for boolean type](types.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdbool&action=edit)[<stdckdint.h>](header/stdckdint.html)(C23)[Macros for performing checked integer arithmetic](numeric.html#Checked_integer_arithmetic)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdckdint&action=edit)[<stddef.h>](header/stddef.html)[Common macro definitions](types.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stddef&action=edit)[<stdint.h>](header/stdint.html)(C99)[Fixed-width integer types](types/integer.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdint&action=edit)[<stdio.h>](header/stdio.html)[Input/output](io.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdio&action=edit)[<stdlib.h>](header/stdlib.html) General utilities: [memory management](memory.html), [program utilities](program.html), [string conversions](string.html), [random numbers](numeric/random.html), [algorithms](algorithm.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdlib&action=edit)[<stdmchar.h>](header/stdmchar.html)(since C29) Text transcode[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdmchar&action=edit)[<stdnoreturn.h>](header/stdnoreturn.html)(since C11)(deprecated in C23)[noreturn](language/noreturn.html) convenience macro[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_stdnoreturn&action=edit)[<string.h>](header/string.html)[String handling](string/byte.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_string&action=edit)[<tgmath.h>](header/tgmath.html)(C99)[Type-generic math](numeric/tgmath.html) (macros wrapping [<math.h>](header/math.html) and [<complex.h>](header/complex.html))[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_tgmath&action=edit)[<threads.h>](header/threads.html)(C11)[Thread library](thread.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_threads&action=edit)[<time.h>](header/time.html)[Time/date utilities](chrono.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_time&action=edit)[<uchar.h>](header/uchar.html)(C11)[UTF-16 and UTF-32 character utilities](string/multibyte.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_uchar&action=edit)[<wchar.h>](header/wchar.html)(C95)[Extended multibyte and wide character utilities](string/wide.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_wchar&action=edit)[<wctype.h>](header/wctype.html)(C95)[Functions to determine the type contained in wide character data](string/wide.html)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/header/dsc_wctype&action=edit)

### [[edit](https://en.cppreference.com/mwiki/index.php?title=c/header&action=edit&section=1)]Feature test macros (since C23)

Feature test macros are defined in corresponding headers respectively since C23. Note that not all headers contain such a macro. 

# Header Macro name Value 1 [<assert.h>](header/assert.html)__STDC_VERSION_ASSERT_H__202311L2 [<complex.h>](header/complex.html)__STDC_VERSION_COMPLEX_H__202311L3 [<ctype.h>](header/ctype.html)N/A4 [<errno.h>](header/errno.html)N/A5 [<fenv.h>](header/fenv.html)__STDC_VERSION_FENV_H__202311L6 [<float.h>](header/float.html)__STDC_VERSION_FLOAT_H__202311L7 [<inttypes.h>](header/inttypes.html)__STDC_VERSION_INTTYPES_H__202311L8 [<iso646.h>](header/iso646.html)N/A9 [<limits.h>](header/limits.html)__STDC_VERSION_LIMITS_H__202311L10 [<locale.h>](header/locale.html)N/A11 [<math.h>](header/math.html)__STDC_VERSION_MATH_H__202311L12 [<setjmp.h>](header/setjmp.html)__STDC_VERSION_SETJMP_H__202311L13 [<signal.h>](header/signal.html)N/A14 [<stdalign.h>](header/stdalign.html)N/A15 [<stdarg.h>](header/stdarg.html)__STDC_VERSION_STDARG_H__202311L16 [<stdatomic.h>](header/stdatomic.html)__STDC_VERSION_STDATOMIC_H__202311L17 [<stdbit.h>](header/stdbit.html)__STDC_VERSION_STDBIT_H__202311L18 [<stdbool.h>](header/stdbool.html)N/A19 [<stdckdint.h>](header/stdckdint.html)__STDC_VERSION_STDCKDINT_H__202311L20 [<stddef.h>](header/stddef.html)__STDC_VERSION_STDDEF_H__202311L21 [<stdint.h>](header/stdint.html)__STDC_VERSION_STDINT_H__202311L22 [<stdio.h>](header/stdio.html)__STDC_VERSION_STDIO_H__202311L23 [<stdlib.h>](header/stdlib.html)__STDC_VERSION_STDLIB_H__202311L24 [<stdmchar.h>](header/stdmchar.html)__STDC_VERSION_STDMCHAR_H__2029??L25 [<stdnoreturn.h>](header/stdnoreturn.html)N/A26 [<string.h>](header/string.html)__STDC_VERSION_STRING_H__202311L27 [<tgmath.h>](header/tgmath.html)__STDC_VERSION_TGMATH_H__202311L28 [<threads.h>](header/threads.html)N/A29 [<time.h>](header/time.html)__STDC_VERSION_TIME_H__202311L30 [<uchar.h>](header/uchar.html)__STDC_VERSION_UCHAR_H__202311L31 [<wchar.h>](header/wchar.html)__STDC_VERSION_WCHAR_H__202311L32 [<wctype.h>](header/wctype.html)N/A

### [[edit](https://en.cppreference.com/mwiki/index.php?title=c/header&action=edit&section=2)]References

-  C23 standard (ISO/IEC 9899:2024): 

-  7.1.2 Standard headers (p: 191-192) 

-  C17 standard (ISO/IEC 9899:2018): 

-  7.1.2 Standard headers (p: 131-132) 

-  C11 standard (ISO/IEC 9899:2011): 

-  7.1.2 Standard headers (p: 181-182) 

-  C99 standard (ISO/IEC 9899:1999): 

-  7.1.2 Standard headers (p: 165) 

-  C89/C90 standard (ISO/IEC 9899:1990): 

-  4.1.2 Standard headers 

### [[edit](https://en.cppreference.com/mwiki/index.php?title=c/header&action=edit&section=3)]See also

[C++ documentation](../cpp/headers.html) for Standard Library headers Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/header&oldid=183293](https://en.cppreference.com/mwiki/index.php?title=c/header&oldid=183293)" 

##### Navigation

- [Support us](http://www.cppreference.com/support)
- [Recent changes](https://en.cppreference.com/w/Special:RecentChanges)
- [FAQ](../Cppreference%253AAbout.html)
- [Offline version](../Cppreference%253AArchives.html)

##### Toolboxheader.html#

- [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/header)
- [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/header)
- [Upload file](http://upload.cppreference.com/w/Special:Upload)
- [Special pages](https://en.cppreference.com/w/Special:SpecialPages)
- [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/header&printable=yes)
- [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/header&oldid=183293)
- [Page information](https://en.cppreference.com/mwiki/index.php?title=c/header&action=info)

- In other languages

- [العربية](http://ar.cppreference.com/w/c/header)
- [Česky](http://cs.cppreference.com/w/c/header)
- [Deutsch](http://de.cppreference.com/w/c/header)
- [Español](http://es.cppreference.com/w/c/header)
- [Français](http://fr.cppreference.com/w/c/header)
- [Italiano](http://it.cppreference.com/w/c/header)
- [日本語](http://ja.cppreference.com/w/c/header)
- [한국어](http://ko.cppreference.com/w/c/header)
- [Polski](http://pl.cppreference.com/w/c/header)
- [Português](http://pt.cppreference.com/w/c/header)
- [Русский](http://ru.cppreference.com/w/c/header)
- [Türkçe](http://tr.cppreference.com/w/c/header)
- [中文](http://zh.cppreference.com/w/c/header)

-  This page was last modified on 16 May 2025, at 16:55.

- [Privacy policy](../Cppreference%253APrivacy_policy.html)
- [About cppreference.com](../Cppreference%253AAbout.html)
- [Disclaimers](../Cppreference%253AGeneral_disclaimer.html)

- https://www.mediawiki.org/http://qbnz.com/highlighter/http://www.tigertech.net/referral/cppreference.com
