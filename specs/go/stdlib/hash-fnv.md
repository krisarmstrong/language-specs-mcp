Fowler–Noll–Vo hash function - Wikipedia[Jump to content](#bodyContent)Main menuMain menumove to sidebarhide Navigation 

- [Main page](/wiki/Main_Page)
- [Contents](/wiki/Wikipedia:Contents)
- [Current events](/wiki/Portal:Current_events)
- [Random article](/wiki/Special:Random)
- [About Wikipedia](/wiki/Wikipedia:About)
- [Contact us](//en.wikipedia.org/wiki/Wikipedia:Contact_us)

 Contribute 

- [Help](/wiki/Help:Contents)
- [Learn to edit](/wiki/Help:Introduction)
- [Community portal](/wiki/Wikipedia:Community_portal)
- [Recent changes](/wiki/Special:RecentChanges)
- [Upload file](/wiki/Wikipedia:File_upload_wizard)
- [Special pages](/wiki/Special:SpecialPages)

/wiki/Main_Page[Search](/wiki/Special:Search)Search

Appearance

- [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
- [Create account](/w/index.php?title=Special:CreateAccount&returnto=Fowler%E2%80%93Noll%E2%80%93Vo+hash+function)
- [Log in](/w/index.php?title=Special:UserLogin&returnto=Fowler%E2%80%93Noll%E2%80%93Vo+hash+function)

Personal tools

- [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
- [Create account](/w/index.php?title=Special:CreateAccount&returnto=Fowler%E2%80%93Noll%E2%80%93Vo+hash+function)
- [Log in](/w/index.php?title=Special:UserLogin&returnto=Fowler%E2%80%93Noll%E2%80%93Vo+hash+function)

## Contents

move to sidebarhide

- [(Top)](#)
- [1
				Overview](#Overview)

- [2
				The hash](#The_hash)Toggle The hash subsection

  - [2.1
					FNV-1 hash](#FNV-1_hash)

  - [2.2
					FNV-1a hash](#FNV-1a_hash)

  - [2.3
					FNV-0 hash (deprecated)](#FNV-0_hash_(deprecated))

  - [2.4
					FNV offset basis](#FNV_offset_basis)

  - [2.5
					FNV prime](#FNV_prime)

  - [2.6
					FNV hash parameters](#FNV_hash_parameters)

- [3
				Non-cryptographic hash](#Non-cryptographic_hash)

- [4
				See also](#See_also)

- [5
				References](#References)

- [6
				External links](#External_links)

Toggle the table of contents

# Fowler–Noll–Vo hash function

3 languages

- [Deutsch](https://de.wikipedia.org/wiki/FNV_(Informatik))
- [Русский](https://ru.wikipedia.org/wiki/FNV)
- [Српски / srpski](https://sr.wikipedia.org/wiki/Fauler%E2%80%93Nol%E2%80%93Vo_he%C5%A1_funkcija)

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q1389328#sitelinks-wikipedia)

- [Article](/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
- [Talk](/wiki/Talk:Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)

English

- [Read](/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
- [Edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit)
- [View history](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=history)

ToolsToolsmove to sidebarhide Actions 

- [Read](/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
- [Edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit)
- [View history](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=history)

 General 

- [What links here](/wiki/Special:WhatLinksHere/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
- [Related changes](/wiki/Special:RecentChangesLinked/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
- [Upload file](//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard)
- [Permanent link](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&oldid=1312413750)
- [Page information](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=info)
- [Cite this page](/w/index.php?title=Special:CiteThisPage&page=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&id=1312413750&wpFormIdentifier=titleform)
- [Get shortened URL](/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFowler%25E2%2580%2593Noll%25E2%2580%2593Vo_hash_function)
- [Download QR code](/w/index.php?title=Special:QrCode&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFowler%25E2%2580%2593Noll%25E2%2580%2593Vo_hash_function)

 Print/export 

- [Download as PDF](/w/index.php?title=Special:DownloadAsPdf&page=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=show-download-screen)
- [Printable version](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&printable=yes)

 In other projects 

- [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q1389328)

Appearancemove to sidebarhideFrom Wikipedia, the free encyclopedia(Redirected from [Fowler-Noll-Vo hash function](/w/index.php?title=Fowler-Noll-Vo_hash_function&redirect=no))Non-cryptographic hash function

Fowler–Noll–Vo (or FNV) is a [non-cryptographic hash function](/wiki/Non-cryptographic_hash_function) created by Glenn Fowler, [Landon Curt Noll](/wiki/Landon_Curt_Noll), and Kiem-Phong Vo. 

The basis of the FNV hash algorithm was taken from an idea sent as reviewer comments to the [IEEE POSIX P1003.2](/wiki/POSIX) committee by Glenn Fowler and Phong Vo in 1991. In a subsequent ballot round, Landon Curt Noll improved on their algorithm. In an email message to Noll, they named it the Fowler/Noll/Vo or FNV hash.[[1]](#cite_note-1)

## Overview

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=1)]

The current versions are FNV-1 and FNV-1a, which supply a means of creating non-zero FNV offset basis. FNV currently[[as of?](/wiki/Wikipedia:Manual_of_Style/Dates_and_numbers#Chronological_items)] comes in 32-, 64-, 128-, 256-, 512-, and 1024-bit variants. For pure FNV implementations, this is determined solely by the availability of FNV primes for the desired bit length; however, the FNV webpage discusses methods of adapting one of the above versions to a smaller length that may or may not be a power of two.[[2]](#cite_note-2)[[3]](#cite_note-3)

The FNV hash algorithms and reference FNV [source code](/wiki/Source_code)[[4]](#cite_note-FNV_prime-4)[[5]](#cite_note-5) have been released into the [public domain](/wiki/Public_domain).[[6]](#cite_note-6)

The [Python programming language](/wiki/Python_programming_language) previously used a modified version of the FNV scheme for its default `hash` function. From Python 3.4, FNV has been replaced with [SipHash](/wiki/SipHash) to resist "[hash flooding](/wiki/Collision_attack#Hash_flooding)" [denial-of-service attacks](/wiki/Denial-of-service_attack).[[7]](#cite_note-7)

FNV is not a [cryptographic hash](/wiki/Cryptographic_hash).[[4]](#cite_note-FNV_prime-4)

## The hash

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=2)]

One of FNV's key advantages is that it is very simple to implement. Start with an initial hash value of FNV offset basis. For each byte in the input, [multiply](/wiki/Multiply)hash by the FNV prime, then [XOR](/wiki/XOR) it with the byte from the input. The alternate algorithm, FNV-1a, reverses the multiply and XOR steps. 

### FNV-1 hash

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=3)]

The FNV-1 hash algorithm is as follows:[[8]](#cite_note-FNV_basics-8)[[9]](#cite_note-9)

```
algorithm fnv-1 is
    hash := FNV_offset_basis

    for each byte_of_data to be hashed do
        hash := hash × FNV_prime
        hash := hash XOR/wiki/XOR byte_of_data

    return hash 
```

In the above [pseudocode](/wiki/Pseudocode), all variables are [unsigned](/wiki/Signedness)[integers](/wiki/Integers). All variables, except for byte_of_data, have the same number of [bits](/wiki/Bit) as the FNV hash. The variable, byte_of_data, is an 8-[bit](/wiki/Bit) unsigned [integer](/wiki/Integer). 

As an example, consider the 64-[bit](/wiki/Bit) FNV-1 hash: 

- All variables, except for byte_of_data, are 64-[bit](/wiki/Bit) unsigned [integers](/wiki/Integers).
- The variable, byte_of_data, is an 8-[bit](/wiki/Bit) unsigned [integer](/wiki/Integer).
- The FNV_offset_basis is the 64-[bit](/wiki/Bit) value: 14695981039346656037 (in hex, 0xcbf29ce484222325).
- The FNV_prime is the 64-[bit](/wiki/Bit) value 1099511628211 (in hex, 0x100000001b3).
- The [multiply](/wiki/Multiply) returns the lower 64 [bits](/wiki/Bit) of the [product](/wiki/Product_(mathematics)).
- The [XOR](/wiki/XOR) is an 8-[bit](/wiki/Bit) operation that modifies only the lower 8-[bits](/wiki/Bit) of the hash value.
- The hash value returned is a 64-[bit](/wiki/Bit)[unsigned](/wiki/Signedness)[integer](/wiki/Integer_(computer_science)).

### FNV-1a hash

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=4)]

The FNV-1a hash differs from the FNV-1 hash only by the order in which the [multiply](/wiki/Multiply) and [XOR](/wiki/XOR) is performed:[[8]](#cite_note-FNV_basics-8)[[10]](#cite_note-10)

```
algorithm fnv-1a is
    hash := FNV_offset_basis

    for each byte_of_data to be hashed do
        hash := hash XOR/wiki/XOR byte_of_data
        hash := hash × FNV_prime

    return hash 
```

The above pseudocode has the same assumptions that were noted for the FNV-1 pseudocode. The change in order leads to slightly better [avalanche characteristics](/wiki/Avalanche_effect).[[8]](#cite_note-FNV_basics-8)[[11]](#cite_note-11)

### FNV-0 hash (deprecated)

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=5)]

The FNV-0 hash differs from the FNV-1 hash only by the initialisation value of the hash variable:[[8]](#cite_note-FNV_basics-8)[[12]](#cite_note-FNV0-12)

```
algorithm fnv-0 is
    hash := 0

    for each byte_of_data to be hashed do
        hash := hash × FNV_prime
        hash := hash XOR/wiki/XOR byte_of_data

    return hash
```

The above pseudocode has the same assumptions that were noted for the FNV-1 pseudocode. 

A consequence of the initialisation of the hash to 0 is that empty messages and all messages consisting of only the byte 0, regardless of their length, hash to 0.[[12]](#cite_note-FNV0-12)

Use of the FNV-0 hash is [deprecated](/wiki/Deprecated) except for the computing of the FNV offset basis for use as the FNV-1 and FNV-1a hash parameters.[[8]](#cite_note-FNV_basics-8)[[12]](#cite_note-FNV0-12)

### FNV offset basis

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=6)]

There are several different FNV offset bases for various bit lengths. These offset bases are computed by computing the FNV-0 from the following 32 [octets](/wiki/Octet_(computing)) when expressed in [ASCII](/wiki/ASCII): 

```
chongo <Landon Curt Noll> /\../\
```

This is one of [Landon Curt Noll](/wiki/Landon_Curt_Noll)'s [signature lines](/wiki/Signature_block). This is the only current practical use for the [deprecated](/wiki/Deprecated) FNV-0.[[8]](#cite_note-FNV_basics-8)[[12]](#cite_note-FNV0-12)

### FNV prime

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=7)]

An FNV prime is a [prime number](/wiki/Prime_number) and is determined as follows:[[4]](#cite_note-FNV_prime-4)[[13]](#cite_note-FNV_prime_remarks-13)

For a given integer s such that 4 < s < 11, let n = 2s and t = ⌊(5 + n) / 12⌋; then the n-[bit](/wiki/Bit) FNV prime is the smallest [prime number](/wiki/Prime_number)p that is of the form 

256t+28+b{\displaystyle 256^{t}+2^{8}+\mathrm {b} \,}

such that: 

- 0 < b < 28,
- the number of one-bits in the [binary](/wiki/Binary_number) representation of b is either 4 or 5, and
- p mod (240 − 224 − 1) > 224 + 28 + 27.

Experimentally, FNV primes matching the above constraints tend to have better dispersion properties. They improve the polynomial feedback characteristic when an FNV prime multiplies an intermediate hash value. As such, the hash values produced are more scattered throughout the n-[bit](/wiki/Bit) hash space.[[4]](#cite_note-FNV_prime-4)[[13]](#cite_note-FNV_prime_remarks-13)

### FNV hash parameters

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=8)]

The above FNV prime constraints and the definition of the FNV offset basis yield the following table of FNV hash parameters: 

FNV parameters [[4]](#cite_note-FNV_prime-4)[[14]](#cite_note-14)Size in bits 

n=2s{\displaystyle n=2^{s}}

Representation FNV primeFNV offset basis32 Expression 224 + 28 + 0x93 Decimal 16777619 2166136261 [Hexadecimal](/wiki/Hexadecimal)0x01000193 0x811c9dc5 64 Expression 240 + 28 + 0xb3 Decimal 1099511628211 14695981039346656037 Hexadecimal 0x00000100000001b3 0xcbf29ce484222325 128 Representation 288 + 28 + 0x3b Decimal 309485009821345068724781371 144066263297769815596495629667062367629 Hexadecimal 0x0000000001000000000000000000013b 0x6c62272e07bb014262b821756295c58d 256 Representation 2168 + 28 + 0x63 Decimal 

374144419156711147060143317
 175368453031918731002211 

100029257958052580907070968620625704837
 092796014241193945225284501741471925557 

Hexadecimal 

0x00000000000000000000010000000000
 00000000000000000000000000000163 

0xdd268dbcaac550362d98c384c4e576ccc8b153
 6847b6bbb31023b4c8caee0535 

512 Representation 2344 + 28 + 0x57 Decimal 

358359158748448673689190764
 890951084499463279557543925
 583998256154206699388825751
 26094039892345713852759 

965930312949666949800943540071631046609
 041874567263789610837432943446265799458
 293219771643844981305189220653980578449
 5328239340083876191928701583869517785 

Hexadecimal 

0x0000000000000000 0000000000000000
 0000000001000000 0000000000000000
 0000000000000000 0000000000000000
 0000000000000000 0000000000000157 

0xb86db0b1171f4416 dca1e50f309990ac
 ac87d059c9000000 0000000000000d21
 e948f68a34c192f6 2ea79bc942dbe7ce
 182036415f56e34b ac982aac4afe9fd9 

1024 Representation 2680 + 28 + 0x8d Decimal 

501645651011311865543459881103
 527895503076534540479074430301
 752383111205510814745150915769
 222029538271616265187852689524
 938529229181652437508374669137
 180409427187316048473796672026
 0389217684476157468082573 

14197795064947621068722070641403218320
 88062279544193396087847491461758272325
 22967323037177221508640965212023555493
 65628174669108571814760471015076148029
 75596980407732015769245856300321530495
 71501574036444603635505054127112859663
 61610267868082893823963790439336411086
 884584107735010676915 

Hexadecimal 

0x0000000000000000 0000000000000000
 0000000000000000 0000000000000000
 0000000000000000 0000010000000000
 0000000000000000 0000000000000000
 0000000000000000 0000000000000000
 0000000000000000 0000000000000000
 0000000000000000 0000000000000000
 0000000000000000 000000000000018d 

0x0000000000000000 005f7a76758ecc4d
 32e56d5a591028b7 4b29fc4223fdada1
 6c3bf34eda3674da 9a21d90000000000
 0000000000000000 0000000000000000
 0000000000000000 0000000000000000
 0000000000000000 000000000004c6d7
 eb6e73802734510a 555f256cc005ae55
 6bde8cc9c6a93b21 aff4b16c71ee90b3 

## Non-cryptographic hash

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=9)]

The FNV hash was designed for fast [hash table](/wiki/Hash_table) and [checksum](/wiki/Checksum) use, not [cryptography](/wiki/Cryptography). The authors have identified the following properties as making the algorithm unsuitable as a [cryptographic hash function](/wiki/Cryptographic_hash_function):[[15]](#cite_note-15)

- Speed of computation – As a hash designed primarily for hashtable and checksum use, FNV-1 and FNV-1a were designed to be fast to compute. However, this same speed makes finding specific hash values (collisions) by brute force faster.
- Sticky state – Being an iterative hash based primarily on multiplication and XOR, the algorithm is sensitive to the number zero. Specifically, if the hash value were to become zero at any point during calculation, and the next byte hashed were also all zeroes, then the hash would not change. This makes colliding messages trivial to create given a message that results in a hash value of zero at some point in its calculation. Additional operations, such as the addition of a third constant prime on each step, can mitigate this but may have detrimental effects on [avalanche effect](/wiki/Avalanche_effect) or random distribution of hash values.
- Diffusion – The ideal secure hash function is one in which each byte of input has an equally-complex effect on every bit of the hash. In the FNV hash, the ones place (the rightmost bit) is always the XOR of the rightmost bit of every input byte. This can be mitigated by XOR-folding (computing a hash twice the desired length, and then XORing the bits in the "upper half" with the bits in the "lower half").[[4]](#cite_note-FNV_prime-4)

A structural weakness of FNV-1a arises from its use of XOR before multiplication, which can cause predictable relationships between hashes of related inputs. For example, the following identity holds in both the 32-bit and 64-bit variants: 

```
fnv1a("some-string-a") XOR/wiki/XOR fnv1a("some-id-1231") = fnv1a("some-string-b") XOR/wiki/XOR fnv1a("some-id-1232")
```

because the differing characters ('a' vs 'b', and '1' vs '2') differ by the same bit pattern. This illustrates how certain bitwise symmetries in input can lead to unintended hash correlations. XOR-folding does not remove this weakness. 

## See also

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=10)]

- [Bloom filter](/wiki/Bloom_filter) (application for fast hashes)
- [Non-cryptographic hash functions](/wiki/Non-cryptographic_hash_functions)

## References

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=11)]

1. [^](#cite_ref-1)["FNV Hash - FNV hash history"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#history). www.isthe.com.
2. [^](#cite_ref-2)["FNV Hash - Changing the FNV hash size - xor-folding"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#xor-fold). www.isthe.com.
3. [^](#cite_ref-3)["FNV Hash - Changing the FNV hash size - non-powers of 2"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#other-folding). www.isthe.com.
4. ^ [a](#cite_ref-FNV_prime_4-0)[b](#cite_ref-FNV_prime_4-1)[c](#cite_ref-FNV_prime_4-2)[d](#cite_ref-FNV_prime_4-3)[e](#cite_ref-FNV_prime_4-4)[f](#cite_ref-FNV_prime_4-5)Eastlake, Donald; Hansen, Tony; Fowler, Glenn; Vo, Kiem-Phong; Noll, Landon (29 May 2019). ["The FNV Non-Cryptographic Hash Algorithm"](https://tools.ietf.org/html/draft-eastlake-fnv-17.html). tools.ietf.org.
5. [^](#cite_ref-5)["FNV Hash - FNV source"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-source). www.isthe.com.
6. [^](#cite_ref-6)[FNV put into the public domain](http://www.isthe.com/chongo/tech/comp/fnv/index.html#public_domain) on isthe.com
7. [^](#cite_ref-7)["PEP 456 -- Secure and interchangeable hash algorithm"](https://www.python.org/dev/peps/pep-0456/). Python.org.
8. ^ [a](#cite_ref-FNV_basics_8-0)[b](#cite_ref-FNV_basics_8-1)[c](#cite_ref-FNV_basics_8-2)[d](#cite_ref-FNV_basics_8-3)[e](#cite_ref-FNV_basics_8-4)[f](#cite_ref-FNV_basics_8-5)Eastlake, Donald; Hansen, Tony; Fowler, Glenn; Vo, Kiem-Phong; <unknown-email-Landon-Noll>, Landon Noll (June 4, 2020). ["The FNV Non-Cryptographic Hash Algorithm"](https://tools.ietf.org/html/draft-eastlake-fnv-17.html). tools.ietf.org. Retrieved 2020-06-04.[cite journal](/wiki/Template:Cite_journal)`{{}}`: `|last5=` has generic name ([help](/wiki/Help:CS1_errors#generic_name))
9. [^](#cite_ref-9)["FNV Hash - The core of the FNV hash"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-1). www.isthe.com. Retrieved 2020-06-04.
10. [^](#cite_ref-10)["FNV Hash - FNV-1a alternate algorithm"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-1a). www.isthe.com.
11. [^](#cite_ref-11)["avalanche - murmurhash"](https://sites.google.com/site/murmurhash/avalanche). sites.google.com.
12. ^ [a](#cite_ref-FNV0_12-0)[b](#cite_ref-FNV0_12-1)[c](#cite_ref-FNV0_12-2)[d](#cite_ref-FNV0_12-3)["FNV Hash - FNV-0 Historic not"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-0). www.isthe.com.
13. ^ [a](#cite_ref-FNV_prime_remarks_13-0)[b](#cite_ref-FNV_prime_remarks_13-1)["FNV Hash - A few remarks on FNV primes"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#fnv-prime). www.isthe.com.
14. [^](#cite_ref-14)["FNV Hash - Parameters of the FNV-1/FNV-1a hash"](http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-param). www.isthe.com.
15. [^](#cite_ref-15)Eastlake, Donald; Hansen, Tony; Fowler, Glenn; Vo, Kiem-Phong; Noll, Landon (29 May 2019). ["The FNV Non-Cryptographic Hash Algorithm"](https://tools.ietf.org/html/draft-eastlake-fnv-17.html). tools.ietf.org. Retrieved 2021-01-12.

## External links

[[edit](/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&action=edit&section=12)]

- [Landon Curt Noll's webpage on FNV](http://www.isthe.com/chongo/tech/comp/fnv/index.html) (with table of base & prime parameters)
- [Internet draft by Fowler, Noll, Vo, and Eastlake](https://datatracker.ietf.org/doc/html/draft-eastlake-fnv-17) (IETF Informational Internet Draft)

Retrieved from "[https://en.wikipedia.org/w/index.php?title=Fowler–Noll–Vo_hash_function&oldid=1312413750](https://en.wikipedia.org/w/index.php?title=Fowler–Noll–Vo_hash_function&oldid=1312413750)"[Categories](/wiki/Help:Category): 

- [Hash function (non-cryptographic)](/wiki/Category:Hash_function_(non-cryptographic))
- [Public-domain software with source code](/wiki/Category:Public-domain_software_with_source_code)

Hidden categories: 

- [CS1 errors: generic name](/wiki/Category:CS1_errors:_generic_name)
- [Articles with short description](/wiki/Category:Articles_with_short_description)
- [Short description matches Wikidata](/wiki/Category:Short_description_matches_Wikidata)
- [All articles with vague or ambiguous time](/wiki/Category:All_articles_with_vague_or_ambiguous_time)
- [Vague or ambiguous time from August 2024](/wiki/Category:Vague_or_ambiguous_time_from_August_2024)

-  This page was last edited on 20 September 2025, at 14:20 (UTC).
- Text is available under the [Creative Commons Attribution-ShareAlike 4.0 License](/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License); additional terms may apply. By using this site, you agree to the [Terms of Use](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use) and [Privacy Policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy). Wikipedia® is a registered trademark of the [Wikimedia Foundation, Inc.](https://wikimediafoundation.org/), a non-profit organization.

- [Privacy policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy)
- [About Wikipedia](/wiki/Wikipedia:About)
- [Disclaimers](/wiki/Wikipedia:General_disclaimer)
- [Contact Wikipedia](//en.wikipedia.org/wiki/Wikipedia:Contact_us)
- [Legal & safety contacts](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Legal:Wikimedia_Foundation_Legal_and_Safety_Contact_Information)
- [Code of Conduct](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct)
- [Developers](https://developer.wikimedia.org)
- [Statistics](https://stats.wikimedia.org/#/en.wikipedia.org)
- [Cookie statement](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement)
- [Mobile view](//en.wikipedia.org/w/index.php?title=Fowler%E2%80%93Noll%E2%80%93Vo_hash_function&mobileaction=toggle_view_mobile)

- https://www.wikimedia.org/
- https://www.mediawiki.org/

SearchSearchToggle the table of contentsFowler–Noll–Vo hash function#######3 languages[Add topic](#)
