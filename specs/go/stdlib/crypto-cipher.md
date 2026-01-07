Authenticated encryption - Wikipedia[Jump to content](#bodyContent)Main menuMain menumove to sidebarhide Navigation 

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
- [Create account](/w/index.php?title=Special:CreateAccount&returnto=Authenticated+encryption)
- [Log in](/w/index.php?title=Special:UserLogin&returnto=Authenticated+encryption)

Personal tools

- [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
- [Create account](/w/index.php?title=Special:CreateAccount&returnto=Authenticated+encryption)
- [Log in](/w/index.php?title=Special:UserLogin&returnto=Authenticated+encryption)

## Contents

move to sidebarhide

- [(Top)](#)
- [1
				Programming interface](#Programming_interface)

- [2
				History](#History)

- [3
				Variants](#Variants)Toggle Variants subsection

  - [3.1
					Authenticated encryption with associated data](#Authenticated_encryption_with_associated_data)

  - [3.2
					Key-committing AEAD](#Key-committing_AEAD)

  - [3.3
					Misuse-resistant authenticated encryption](#Misuse-resistant_authenticated_encryption)

- [4
				Approaches to authenticated encryption](#Approaches_to_authenticated_encryption)Toggle Approaches to authenticated encryption subsection

  - [4.1
					Encrypt-then-MAC (EtM)](#Encrypt-then-MAC_(EtM))

  - [4.2
					Encrypt-and-MAC (E&M)](#Encrypt-and-MAC_(E&M))

  - [4.3
					MAC-then-Encrypt (MtE)](#MAC-then-Encrypt_(MtE))

- [5
				See also](#See_also)

- [6
				References](#References)

- [7
				Sources](#Sources)

Toggle the table of contents

# Authenticated encryption

13 languages

- [Català](https://ca.wikipedia.org/wiki/Xifratge_autenticat)
- [Čeština](https://cs.wikipedia.org/wiki/Autentizovan%C3%A9_%C5%A1ifrov%C3%A1n%C3%AD)
- [Deutsch](https://de.wikipedia.org/wiki/Authenticated_Encryption)
- [فارسی](https://fa.wikipedia.org/wiki/%D8%B1%D9%85%D8%B2%DA%AF%D8%B0%D8%A7%D8%B1%DB%8C_%D8%AA%D8%A3%DB%8C%DB%8C%D8%AF_%D9%87%D9%88%DB%8C%D8%AA)
- [Français](https://fr.wikipedia.org/wiki/Chiffrement_authentifi%C3%A9)
- [한국어](https://ko.wikipedia.org/wiki/%EC%9D%B8%EC%A6%9D%EB%90%9C_%EC%95%94%ED%98%B8_%EB%B0%A9%EC%8B%9D)
- [Italiano](https://it.wikipedia.org/wiki/Cifratura_autenticata)
- [עברית](https://he.wikipedia.org/wiki/%D7%94%D7%A6%D7%A4%D7%A0%D7%94_%D7%9E%D7%90%D7%95%D7%9E%D7%AA%D7%AA)
- [日本語](https://ja.wikipedia.org/wiki/%E8%AA%8D%E8%A8%BC%E4%BB%98%E3%81%8D%E6%9A%97%E5%8F%B7)
- [Русский](https://ru.wikipedia.org/wiki/AEAD-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC_%D0%B1%D0%BB%D0%BE%D1%87%D0%BD%D0%BE%D0%B3%D0%BE_%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F)
- [Српски / srpski](https://sr.wikipedia.org/wiki/%D0%90%D1%83%D1%82%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%BE%D0%B2%D0%B0%D0%BD%D0%BE_%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D1%9A%D0%B5)
- [Українська](https://uk.wikipedia.org/wiki/AEAD-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC_%D0%B1%D0%BB%D0%BE%D1%87%D0%BD%D0%BE%D0%B3%D0%BE_%D1%88%D0%B8%D1%84%D1%80%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F)
- [中文](https://zh.wikipedia.org/wiki/%E8%AE%A4%E8%AF%81%E5%8A%A0%E5%AF%86)

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q15263584#sitelinks-wikipedia)

- [Article](/wiki/Authenticated_encryption)
- [Talk](/wiki/Talk:Authenticated_encryption)

English

- [Read](/wiki/Authenticated_encryption)
- [Edit](/w/index.php?title=Authenticated_encryption&action=edit)
- [View history](/w/index.php?title=Authenticated_encryption&action=history)

ToolsToolsmove to sidebarhide Actions 

- [Read](/wiki/Authenticated_encryption)
- [Edit](/w/index.php?title=Authenticated_encryption&action=edit)
- [View history](/w/index.php?title=Authenticated_encryption&action=history)

 General 

- [What links here](/wiki/Special:WhatLinksHere/Authenticated_encryption)
- [Related changes](/wiki/Special:RecentChangesLinked/Authenticated_encryption)
- [Upload file](//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard)
- [Permanent link](/w/index.php?title=Authenticated_encryption&oldid=1323669885)
- [Page information](/w/index.php?title=Authenticated_encryption&action=info)
- [Cite this page](/w/index.php?title=Special:CiteThisPage&page=Authenticated_encryption&id=1323669885&wpFormIdentifier=titleform)
- [Get shortened URL](/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAuthenticated_encryption)
- [Download QR code](/w/index.php?title=Special:QrCode&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FAuthenticated_encryption)

 Print/export 

- [Download as PDF](/w/index.php?title=Special:DownloadAsPdf&page=Authenticated_encryption&action=show-download-screen)
- [Printable version](/w/index.php?title=Authenticated_encryption&printable=yes)

 In other projects 

- [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q15263584)

Appearancemove to sidebarhideFrom Wikipedia, the free encyclopediaEncryption method

Authenticated encryption (AE) is any [encryption](/wiki/Encryption) scheme which simultaneously assures the data confidentiality (also known as privacy: the encrypted message is impossible to understand without the knowledge of a secret [key](/wiki/Key_(cryptography))[[1]](#cite_note-FOOTNOTEBlack20051-1)) and [authenticity](/wiki/Message_authentication) (in other words, it is unforgeable:[[2]](#cite_note-FOOTNOTEKatzLindell2020116-2) the encrypted message includes an [authentication tag](/wiki/Authentication_tag) that the sender can calculate only while possessing the secret key[[1]](#cite_note-FOOTNOTEBlack20051-1)). Examples of [encryption modes](/wiki/Encryption_mode) that provide AE are [GCM](/wiki/Galois/Counter_Mode), [CCM](/wiki/CCM_mode).[[1]](#cite_note-FOOTNOTEBlack20051-1)

Many (but not all) AE schemes allow the message to contain "associated data" (AD) which is not made confidential, but is integrity protected (i.e., readable, but [tamperevident](/wiki/Tamper-evident_technology)). A typical example is the [header](/wiki/Header_(computing)) of a [network packet](/wiki/Network_packet) that contains its destination address. To properly [route](/wiki/Routing) the packet, all intermediate nodes in the message path need to know the destination, but for security reasons they cannot possess the secret key.[[3]](#cite_note-FOOTNOTEBlack20052-3) Schemes that allow associated data provide [authenticated encryption with associated data](#Authenticated_encryption_with_associated_data), or AEAD.[[3]](#cite_note-FOOTNOTEBlack20052-3)

## Programming interface

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=1)]

A typical [programming interface](/wiki/Application_programming_interface) for an AE implementation provides the following functions: 

- Encryption 

  - Input: plaintext, key, and optionally a header (also known as additional authenticated data, AAD, or associated data, AD) in plaintext that will not be encrypted, but will be covered by authenticity protection.
  - Output: ciphertext and authentication tag ([message authentication code](/wiki/Message_authentication_code) or MAC).

- Decryption 

  - Input: ciphertext, key, authentication tag, and optionally a header (if used during the encryption).
  - Output: plaintext, or an error if the authentication tag does not match the supplied ciphertext or header.

The header part is intended to provide authenticity and integrity protection for networking or storage metadata for which confidentiality is unnecessary, but authenticity is desired. 

## History

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=2)]

The need for authenticated encryption emerged from the observation that securely combining separate confidentiality and authentication block cipher operation modes could be error prone and difficult.[[4]](#cite_note-:1-4)[[5]](#cite_note-5) This was confirmed by a number of practical attacks introduced into production protocols and applications by incorrect implementation, or lack of authentication.[[6]](#cite_note-6)

Around the year 2000, a number of efforts evolved around the notion of standardizing modes that ensured correct implementation. In particular, strong interest in possibly secure modes was sparked by the publication of [Charanjit Jutla](/w/index.php?title=Charanjit_Jutla&action=edit&redlink=1)'s integrity-aware CBC and [integrity-aware parallelizable](/wiki/IAPM_(mode)), IAPM, modes[[7]](#cite_note-7) in 2000 (see [OCB](/wiki/OCB_mode) and chronology[[8]](#cite_note-8)). Six different authenticated encryption modes (namely [offset codebook mode 2.0](/wiki/OCB_mode), OCB2.0; [Key Wrap](/wiki/Key_Wrap); [counter with CBC-MAC](/wiki/CCM_mode), CCM; [encrypt then authenticate then translate](/wiki/EAX_mode), EAX; [encrypt-then-MAC](/wiki/Encrypt-then-MAC), EtM; and [Galois/counter mode](/wiki/Galois/counter_mode), GCM) have been standardized in ISO/IEC 19772:2009.[[9]](#cite_note-ISO19772-9) More authenticated encryption methods were developed in response to [NIST](/wiki/NIST) solicitation.[[10]](#cite_note-10)[Sponge functions](/wiki/Sponge_function) can be used in duplex mode to provide authenticated encryption.[[11]](#cite_note-11)

Bellare and Namprempre (2000) analyzed three compositions of encryption and MAC primitives, and demonstrated that encrypting a message and subsequently applying a MAC to the ciphertext (the [Encrypt-then-MAC](#Encrypt-then-MAC) approach) implies security against an [adaptive chosen ciphertext attack](/wiki/Adaptive_chosen_ciphertext_attack), provided that both functions meet minimum required properties. Katz and Yung investigated the notion under the name "unforgeable encryption" and proved it implies security against chosen ciphertext attacks.[[12]](#cite_note-12)

In 2013, the [CAESAR competition](/wiki/CAESAR_Competition) was announced to encourage design of authenticated encryption modes.[[13]](#cite_note-13)

In 2015, [ChaCha20-Poly1305](/wiki/ChaCha20-Poly1305) is added as an alternative AE construction to [GCM](/wiki/Galois/Counter_Mode) in [IETF](/wiki/Internet_Engineering_Task_Force) protocols. 

## Variants

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=3)]

### Authenticated encryption with associated data

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=4)]

Authenticated encryption with associated data (AEAD) is a variant of AE that allows the message to include "associated data" (AD, additional non-confidential information, a.k.a. "additional authenticated data", AAD). A recipient can check the integrity of both the associated data and the confidential information in a message. AD is useful, for example, in [network packets](/wiki/Network_packet) where the [header](/wiki/Header_(computing)) should be visible for [routing](/wiki/Routing), but the payload needs to be confidential, and both need [integrity](/wiki/Data_integrity) and [authenticity](/wiki/Message_authentication). The notion of AEAD was formalized by [Rogaway](/wiki/Phillip_Rogaway) (2002).[[3]](#cite_note-FOOTNOTEBlack20052-3)

### Key-committing AEAD

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=5)]

AE was originally designed primarily to provide the ciphertext integrity: successful validation of an authentication tag by [Alice](/wiki/Alice_and_Bob) using her symmetric key KA indicates that the message was not tampered with by an adversary [Mallory](/wiki/Alice_and_Bob) that does not possess the KA. The AE schemes usually do not provide the key commitment, a guarantee that the decryption would fail for any other key.[[14]](#cite_note-FOOTNOTEAlbertiniDuongGueronKölbl20201–2-14) As of 2021, most existing AE schemes (including the very popular GCM) allow some messages to be decrypted without an error using more than just the (correct) KA; while the plaintext decrypted using a second (wrong) key KM will be incorrect, the authentication tag would still match the new plaintext.[[15]](#cite_note-15) Since crafting a message with such property requires Mallory to already possess both KA and KM, the issue might appear to be one of a purely academic interest.[[16]](#cite_note-FOOTNOTEAlbertiniDuongGueronKölbl20202-16) However, under special circumstances, practical attacks can be mounted against vulnerable implementations. For example, if an identity authentication protocol is based on successful decryption of a message that uses a password-based key, Mallory's ability to craft a single message that would be successfully decrypted using 1000 different keys associated with [weak](/wiki/Weak_password), and thus known to her, potential passwords, can speed up her search for passwords by a factor of almost 1000. For this [dictionary attack](/wiki/Dictionary_attack) to succeed, Mallory also needs an ability to distinguish successful decryption by Alice from an unsuccessful one, due, for example, to a poor protocol design or implementation turning Alice's side into an [oracle](/wiki/Oracle_attack). Naturally, this attack cannot be mounted at all when the keys are generated randomly.[[17]](#cite_note-17)

Key commitment was originally studied in the 2010s by Abdalla et al.[[18]](#cite_note-FOOTNOTEAbdallaBellareNeven2010480–497-18) and Farshim et al.[[19]](#cite_note-FOOTNOTEFarshimLibertPatersonQuaglia2013352–368-19) under the name "robust encryption".[[16]](#cite_note-FOOTNOTEAlbertiniDuongGueronKölbl20202-16)[[20]](#cite_note-FOOTNOTEBellareHoang20225-20)

To mitigate the attack described above without removing the "oracle", a key-committing AEAD that does not allow this type of crafted messages to exist can be used. AEGIS is an example of fast (if the [AES instruction set](/wiki/AES_instruction_set) is present), key-committing AEAD.[[21]](#cite_note-21) It is possible to add key-commitment to an existing AEAD scheme.[[22]](#cite_note-22)[[23]](#cite_note-23)

### Misuse-resistant authenticated encryption

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=6)]

Misuse-resistant authenticated encryption (MRAE) has the additional property that reusing the same [nonce](/wiki/Cryptographic_nonce) for several messages does not allow an attacker to recover the plaintext. MRAE was formalized in 2006 by [Phillip Rogaway](/wiki/Phillip_Rogaway) and Thomas Shrimpton.[[24]](#cite_note-24) One example of a MRAE algorithm is [AES-GCM-SIV](/wiki/AES-GCM-SIV). 

## Approaches to authenticated encryption

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=7)]

### Encrypt-then-MAC (EtM) 

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=8)]/wiki/File:Authenticated_Encryption_EtM.pngEtM approach

The plaintext is first encrypted, then a MAC is produced based on the resulting ciphertext. The ciphertext and its MAC are sent together. ETM is the standard method according to ISO/IEC 19772:2009.[[9]](#cite_note-ISO19772-9) It is the only method which can reach the highest definition of security in AE, but this can only be achieved when the MAC used is "strongly unforgeable".[[25]](#cite_note-BN-25)

[IPSec](/wiki/IPsec) adopted EtM in 2005.[[26]](#cite_note-26) In November 2014, TLS and DTLS received extensions for EtM with [RFC](/wiki/RFC_(identifier))[7366](https://www.rfc-editor.org/rfc/rfc7366). Various EtM ciphersuites exist for SSHv2 as well (e.g., hmac-sha1-etm@openssh.com). 

### Encrypt-and-MAC (E&M) 

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=9)]/wiki/File:Authenticated_Encryption_EaM.pngE&M approach

A MAC is produced based on the plaintext, and the plaintext is encrypted without the MAC. The plaintext's MAC and the ciphertext are sent together. Used in, e.g., [SSH](/wiki/Secure_Shell).[[27]](#cite_note-27) Even though the E&M approach has not been proved to be strongly unforgeable in itself,[[25]](#cite_note-BN-25) it is possible to apply some minor modifications to [SSH](/wiki/Secure_Shell) to make it strongly unforgeable despite the approach.[[28]](#cite_note-28)

### MAC-then-Encrypt (MtE) 

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=10)]/wiki/File:Authenticated_Encryption_MtE.pngMtE approach

A MAC is produced based on the plaintext, then the plaintext and MAC are together encrypted to produce a ciphertext based on both. The ciphertext (containing an encrypted MAC) is sent. Until TLS 1.2, all available [SSL/TLS](/wiki/SSL/TLS) cipher suites were MtE.[[29]](#cite_note-29)

MtE has not been proven to be strongly unforgeable in itself.[[25]](#cite_note-BN-25) The [SSL/TLS](/wiki/SSL/TLS) implementation has been proven to be strongly unforgeable by [Krawczyk](/wiki/Hugo_Krawczyk) who showed that SSL/TLS was, in fact, secure because of the encoding used alongside the MtE mechanism.[[30]](#cite_note-:0-30) However, Krawczyk's proof contains flawed assumptions about the randomness of the [initialization vector](/wiki/Initialization_vector) (IV). The 2011 BEAST attack exploited the non-random chained IV and broke all CBC algorithms in TLS 1.0 and under.[[31]](#cite_note-31)

In addition, deeper analysis of SSL/TLS modeled the protection as MAC-then-pad-then-encrypt, i.e. the plaintext is first padded to the block size of the encryption function. Padding errors often result in the detectable errors on the recipient's side, which in turn lead to [padding oracle attacks](/wiki/Padding_oracle_attack), such as [Lucky Thirteen](/wiki/Lucky_Thirteen_attack). 

## See also

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=11)]

- [Block cipher mode of operation](/wiki/Block_cipher_mode_of_operation)
- [CCM mode](/wiki/CCM_mode)
- [CWC mode](/wiki/CWC_mode)
- [OCB mode](/wiki/OCB_mode)
- [EAX mode](/wiki/EAX_mode)
- [GCM](/wiki/Galois/Counter_Mode)
- [GCM-SIV](/wiki/AES-GCM-SIV)
- [ChaCha20-Poly1305](/wiki/ChaCha20-Poly1305)
- [SGCM](/wiki/Sophie_Germain_Counter_Mode)
- [Signcryption](/wiki/Signcryption)

## References

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=12)]

1. ^ [a](#cite_ref-FOOTNOTEBlack20051_1-0)[b](#cite_ref-FOOTNOTEBlack20051_1-1)[c](#cite_ref-FOOTNOTEBlack20051_1-2)[Black 2005](#CITEREFBlack2005), p. 1.
2. [^](#cite_ref-FOOTNOTEKatzLindell2020116_2-0)[Katz & Lindell 2020](#CITEREFKatzLindell2020), p. 116.
3. ^ [a](#cite_ref-FOOTNOTEBlack20052_3-0)[b](#cite_ref-FOOTNOTEBlack20052_3-1)[c](#cite_ref-FOOTNOTEBlack20052_3-2)[Black 2005](#CITEREFBlack2005), p. 2.
4. [^](#cite_ref-:1_4-0)M. Bellare; P. Rogaway; D. Wagner. ["A Conventional Authenticated-Encryption Mode"](http://csrc.nist.gov/groups/ST/toolkit/BCM/documents/proposedmodes/eax/eax-spec.pdf)(PDF). NIST. Retrieved March 12, 2013. people had been doing rather poorly when they tried to glue together a traditional (privacy-only) encryption scheme and a message authentication code (MAC)
5. [^](#cite_ref-5)T. Kohno; J. Viega & D. Whiting. ["The CWC Authenticated Encryption (Associated Data) Mode"](http://csrc.nist.gov/groups/ST/toolkit/BCM/documents/proposedmodes/cwc/cwc-spec.pdf)(PDF). NIST. Retrieved March 12, 2013. it is very easy to accidentally combine secure encryption schemes with secure MACs and still get insecure authenticated encryption schemes
6. [^](#cite_ref-6)["Failures of secret-key cryptography"](https://web.archive.org/web/20130418063008/http://cr.yp.to/talks/2013.03.12/slides.pdf)(PDF). Daniel J. Bernstein. Archived from [the original](https://cr.yp.to/talks/2013.03.12/slides.pdf)(PDF) on April 18, 2013. Retrieved March 12, 2013.
7. [^](#cite_ref-7)Jutl, Charanjit S. (2000-08-01). ["Encryption Modes with Almost Free Message Integrity"](https://eprint.iacr.org/2000/039). Cryptology ePrint Archive: Report 2000/039. Proceedings IACR EUROCRYPT 2001. [IACR](/wiki/International_Association_for_Cryptologic_Research). Retrieved 2013-03-16.
8. [^](#cite_ref-8)T. Krovetz; P. Rogaway (2011-03-01). ["The Software Performance of Authenticated-Encryption Modes"](https://web.cs.ucdavis.edu/~rogaway/papers/ae.pdf)(PDF). Fast Software Encryption 2011 (FSE 2011). [IACR](/wiki/International_Association_for_Cryptologic_Research).
9. ^ [a](#cite_ref-ISO19772_9-0)[b](#cite_ref-ISO19772_9-1)["Information technology -- Security techniques -- Authenticated encryption"](https://www.iso.org/iso/catalogue_detail.htm?csnumber=46345). 19772:2009. ISO/IEC. Retrieved March 12, 2013.
10. [^](#cite_ref-10)["Encryption modes development"](http://csrc.nist.gov/groups/ST/toolkit/BCM/modes_development.html). NIST. Retrieved April 17, 2013.
11. [^](#cite_ref-11)The Keccak Team. ["Duplexing The Sponge"](http://sponge.noekeon.org/SpongeDuplex.pdf)(PDF).
12. [^](#cite_ref-12)Katz, J.; Yung, M. (2001). "Unforgeable Encryption and Chosen Ciphertext Secure Modes of Operation". In B. Schneier (ed.). Fast Software Encryption (FSE): 2000 Proceedings. Lecture Notes in Computer Science. Vol. 1978. pp. 284–299. [doi](/wiki/Doi_(identifier)):[10.1007/3-540-44706-7_20](https://doi.org/10.1007%2F3-540-44706-7_20). [ISBN](/wiki/ISBN_(identifier))[978-3-540-41728-6](/wiki/Special:BookSources/978-3-540-41728-6).
13. [^](#cite_ref-13)["CAESAR: Competition for Authenticated Encryption: Security, Applicability, and Robustness"](https://competitions.cr.yp.to/caesar.html). Retrieved March 12, 2013.
14. [^](#cite_ref-FOOTNOTEAlbertiniDuongGueronKölbl20201–2_14-0)[Albertini et al. 2020](#CITEREFAlbertiniDuongGueronKölbl2020), pp. 1–2.
15. [^](#cite_ref-15)["Invisible Salamanders Are Not What You Think"](https://soatok.blog/2024/09/10/invisible-salamanders-are-not-what-you-think/). Dhole Moments. 2024-09-10. Retrieved 2025-02-21.
16. ^ [a](#cite_ref-FOOTNOTEAlbertiniDuongGueronKölbl20202_16-0)[b](#cite_ref-FOOTNOTEAlbertiniDuongGueronKölbl20202_16-1)[Albertini et al. 2020](#CITEREFAlbertiniDuongGueronKölbl2020), p. 2.
17. [^](#cite_ref-17)Len, Julia; Grubbs, Paul; Ristenpart, Thomas (2021). [Partitioning Oracle Attacks](https://www.usenix.org/conference/usenixsecurity21/presentation/len). USENET '21. pp. 195–212.
18. [^](#cite_ref-FOOTNOTEAbdallaBellareNeven2010480–497_18-0)[Abdalla, Bellare & Neven 2010](#CITEREFAbdallaBellareNeven2010), pp. 480–497.
19. [^](#cite_ref-FOOTNOTEFarshimLibertPatersonQuaglia2013352–368_19-0)[Farshim et al. 2013](#CITEREFFarshimLibertPatersonQuaglia2013), pp. 352–368.
20. [^](#cite_ref-FOOTNOTEBellareHoang20225_20-0)[Bellare & Hoang 2022](#CITEREFBellareHoang2022), p. 5.
21. [^](#cite_ref-21)Denis, Frank. ["The AEGIS Family of Authenticated Encryption Algorithms"](https://cfrg.github.io/draft-irtf-cfrg-aegis-aead/draft-irtf-cfrg-aegis-aead.html). cfrg.github.io.
22. [^](#cite_ref-22)Gueron, Shay (2020). ["Key Committing AEADs"](https://eprint.iacr.org/2020/1153.pdf)(PDF).
23. [^](#cite_ref-23)poncho. ["Key Committing AEADs"](https://crypto.stackexchange.com/a/87776). Cryptography Stack Exchange. Retrieved 21 February 2024. (See also the comment section discussing a revised [libsodium](/wiki/Libsodium) recommendation for adding key-commitment.)
24. [^](#cite_ref-24)[Rogaway, Phillip](/wiki/Phillip_Rogaway); Shrimpton, Thomas (2006). [Deterministic Authenticated-Encryption: A Provable-Security Treatment of the Key-Wrap Problem](https://www.cs.ucdavis.edu/~rogaway/papers/keywrap.pdf)(PDF). [EUROCRYPT](/wiki/EUROCRYPT). [Lecture Notes in Computer Science](/wiki/Lecture_Notes_in_Computer_Science). Vol. 4004. [Springer](/wiki/Springer_Science%2BBusiness_Media). pp. 373–390. [doi](/wiki/Doi_(identifier)):[10.1007/11761679_23](https://doi.org/10.1007%2F11761679_23). [Archived](https://web.archive.org/web/20241218124122/https://www.cs.ucdavis.edu/~rogaway/papers/keywrap.pdf)(PDF) from the original on 2024-12-18. Retrieved 2025-06-22.
25. ^ [a](#cite_ref-BN_25-0)[b](#cite_ref-BN_25-1)[c](#cite_ref-BN_25-2)["Authenticated Encryption: Relations among notions and analysis of the generic composition paradigm"](https://web.archive.org/web/20180123062226/http://cseweb.ucsd.edu/~mihir/papers/oem.html). M. Bellare and C. Namprempre. Archived from [the original](https://cseweb.ucsd.edu/~mihir/papers/oem.html) on January 23, 2018. Retrieved April 13, 2013.
26. [^](#cite_ref-26)Kent, Stephen (December 2005). ["Separate Confidentiality and Integrity Algorithms"](https://tools.ietf.org/html/rfc4303#section-3.3.2.1). RFC 4303 - IP Encapsulating Security Payload (ESP). Internet Engineering Task Force (IETF). Retrieved 2018-09-12.
27. [^](#cite_ref-27)Lonvick, Chris M.; Ylonen, Tatu (January 2006). ["Data Integrity"](https://tools.ietf.org/html/rfc4253#section-6.4). RFC 4253. Internet Engineering Task Force (IETF). Retrieved 2018-09-12.
28. [^](#cite_ref-28)Bellare, Mihir; Kohno, Tadayoshi; Namprempre, Chanathip. ["Breaking and Provably Repairing the SSH Authenticated Encryption Scheme: A Case Study of the Encode-then-Encrypt-and-MAC Paradigm"](https://homes.cs.washington.edu/~yoshi/papers/SSH/ssh.pdf)(PDF). ACM Transactions on Information and System Security. Retrieved 30 August 2021.
29. [^](#cite_ref-29)Rescorla, Eric; Dierks, Tim (August 2008). ["Record Payload Protection"](https://tools.ietf.org/html/rfc5246#section-6.2.3). RFC 5246. Internet Engineering Task Force (IETF). Retrieved 2018-09-12.
30. [^](#cite_ref-:0_30-0)["The Order of Encryption and Authentication for Protecting Communications (Or: How Secure is SSL?)"](https://www.iacr.org/archive/crypto2001/21390309.pdf)(PDF). H. Krawczyk. Retrieved April 13, 2013.
31. [^](#cite_ref-31)Duong, Thai; Rizzo, Juliano (May 13, 2011). ["Here Come The ⊕ Ninjas"](https://tlseminar.github.io/docs/beast.pdf)(PDF). – BEAST attack whitepaper

General

- Bellare, M.; Namprempre, C. (2000), "Authenticated Encryption: Relations among Notions and Analysis of the Generic Composition Paradigm", in T. Okamoto (ed.), [Advances in Cryptology — ASIACRYPT 2000](https://link.springer.com/content/pdf/10.1007/3-540-44448-3_41.pdf)(PDF), Lecture Notes in Computer Science, vol. 1976, Springer-Verlag, pp. 531–545, [doi](/wiki/Doi_(identifier)):[10.1007/3-540-44448-3_41](https://doi.org/10.1007%2F3-540-44448-3_41), [ISBN](/wiki/ISBN_(identifier))[978-3-540-41404-9](/wiki/Special:BookSources/978-3-540-41404-9)

## Sources

[[edit](/w/index.php?title=Authenticated_encryption&action=edit&section=13)]

- Katz, J.; Lindell, Y. (2020). [Introduction to Modern Cryptography](https://books.google.com/books?id=RsoOEAAAQBAJ&pg=PT116). Chapman & Hall/CRC Cryptography and Network Security Series. CRC Press. [ISBN](/wiki/ISBN_(identifier))[978-1-351-13301-2](/wiki/Special:BookSources/978-1-351-13301-2). Retrieved 2023-06-08.
- Black, J. (2005). ["Authenticated encryption"](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=2628d946bda9f3d3b087e5c4846e76ae0fb07b6b). Encyclopedia of Cryptography and Security. Springer US. pp. 11–21. [doi](/wiki/Doi_(identifier)):[10.1007/0-387-23483-7_15](https://doi.org/10.1007%2F0-387-23483-7_15). [ISBN](/wiki/ISBN_(identifier))[978-0-387-23473-1](/wiki/Special:BookSources/978-0-387-23473-1).
- Albertini, Ange; Duong, Thai; Gueron, Shay; Kölbl, Stefan; Luykx, Atul; Schmieg, Sophie (2020). ["How to Abuse and Fix Authenticated Encryption Without Key Commitment"](https://eprint.iacr.org/2020/1456.pdf)(PDF). USENIX.
- Bellare, Mihir; Hoang, Viet Tung (2022). ["Efficient Schemes for Committing Authenticated Encryption"](https://eprint.iacr.org/2022/268.pdf)(PDF). EUROCRYPT 2022.
- Abdalla, Michel; Bellare, Mihir; Neven, Gregory (2010). "Robust Encryption". Theory of Cryptography. Vol. 5978. Berlin, Heidelberg: Springer Berlin Heidelberg. [doi](/wiki/Doi_(identifier)):[10.1007/978-3-642-11799-2_28](https://doi.org/10.1007%2F978-3-642-11799-2_28). [ISBN](/wiki/ISBN_(identifier))[978-3-642-11798-5](/wiki/Special:BookSources/978-3-642-11798-5).
- Farshim, Pooya; Libert, Benoît; Paterson, Kenneth G.; Quaglia, Elizabeth A. (2013). "Robust Encryption, Revisited". Public-Key Cryptography – PKC 2013. Vol. 7778. Berlin, Heidelberg: Springer Berlin Heidelberg. [doi](/wiki/Doi_(identifier)):[10.1007/978-3-642-36362-7_22](https://doi.org/10.1007%2F978-3-642-36362-7_22). [ISBN](/wiki/ISBN_(identifier))[978-3-642-36361-0](/wiki/Special:BookSources/978-3-642-36361-0).
- Chan, John; Rogaway, Phillip (2022). "On Committing Authenticated-Encryption". Computer Security – ESORICS 2022. Vol. 13555. Cham: Springer Nature Switzerland. [doi](/wiki/Doi_(identifier)):[10.1007/978-3-031-17146-8_14](https://doi.org/10.1007%2F978-3-031-17146-8_14). [ISBN](/wiki/ISBN_(identifier))[978-3-031-17145-1](/wiki/Special:BookSources/978-3-031-17145-1).

- [v](/wiki/Template:Cryptography_hash)
- [t](/wiki/Template_talk:Cryptography_hash)
- [e](/wiki/Special:EditPage/Template:Cryptography_hash)

[Cryptographic hash functions](/wiki/Cryptographic_hash_function) and [message authentication codes](/wiki/Message_authentication_code)

- [List](/wiki/List_of_hash_functions)
- [Comparison](/wiki/Comparison_of_cryptographic_hash_functions)
- [Known attacks](/wiki/Hash_function_security_summary)

Common functions

- [MD5](/wiki/MD5) (compromised)
- [SHA-1](/wiki/SHA-1) (compromised)
- [SHA-2](/wiki/SHA-2)
- [SHA-3](/wiki/SHA-3)
- [BLAKE2](/wiki/BLAKE_(hash_function)#BLAKE2)

[SHA-3 finalists](/wiki/NIST_hash_function_competition)

- [BLAKE](/wiki/BLAKE_(hash_function))
- [Grøstl](/wiki/Gr%C3%B8stl)
- [JH](/wiki/JH_(hash_function))
- [Skein](/wiki/Skein_(hash_function))
- [Keccak](/wiki/SHA-3) (winner)

Other functions

- [BLAKE3](/wiki/BLAKE3)
- [CubeHash](/wiki/CubeHash)
- [ECOH](/wiki/Elliptic_curve_only_hash)
- [FSB](/wiki/Fast_syndrome-based_hash)
- [Fugue](/wiki/Fugue_(hash_function))
- [GOST](/wiki/GOST_(hash_function))
- [HAS-160](/wiki/HAS-160)
- [HAVAL](/wiki/HAVAL)
- [Kupyna](/wiki/Kupyna)
- [LSH](/wiki/LSH_(hash_function))
- [Lane](/wiki/Lane_(hash_function))
- [MASH-1](/wiki/MASH-1)
- [MASH-2](/wiki/MASH-1#MASH2)
- [MD2](/wiki/MD2_(hash_function))
- [MD4](/wiki/MD4)
- [MD6](/wiki/MD6)
- [MDC-2](/wiki/MDC-2)
- [N-hash](/wiki/N-hash)
- [RIPEMD](/wiki/RIPEMD)
- [RadioGatún](/wiki/RadioGat%C3%BAn)
- [SIMD](/wiki/SIMD_(hash_function))
- [SM3](/wiki/SM3_(hash_function))
- [SWIFFT](/wiki/SWIFFT)
- [Shabal](/wiki/Shabal)
- [Snefru](/wiki/Snefru)
- [Streebog](/wiki/Streebog)
- [Tiger](/wiki/Tiger_(hash_function))
- [VSH](/wiki/Very_smooth_hash)
- [Whirlpool](/wiki/Whirlpool_(hash_function))

Password hashing/
[key stretching](/wiki/Key_stretching) functions

- [Argon2](/wiki/Argon2)
- [Balloon](/wiki/Balloon_hashing)
- [bcrypt](/wiki/Bcrypt)
- [Catena](/wiki/Catena_(cryptography))
- [crypt](/wiki/Crypt_(C))
- [LM hash](/wiki/LAN_Manager#LM_hash_details)
- [Lyra2](/wiki/Lyra2)
- [Makwa](/wiki/Makwa_(cryptography))
- [PBKDF2](/wiki/PBKDF2)
- [scrypt](/wiki/Scrypt)
- [yescrypt](/wiki/Yescrypt)

General purpose
[key derivation functions](/wiki/Key_derivation_function)

- [HKDF](/wiki/HKDF)
- KDF1/KDF2

[MAC functions](/wiki/Message_authentication_code)

- [CBC-MAC](/wiki/CBC-MAC)
- [DAA](/wiki/Data_Authentication_Algorithm)
- [GMAC](/wiki/Galois_Message_Authentication_Code)
- [HMAC](/wiki/HMAC)
- [NMAC](/wiki/NMAC)
- [OMAC](/wiki/One-key_MAC)/[CMAC](/wiki/One-key_MAC)
- [PMAC](/wiki/PMAC_(cryptography))
- [Poly1305](/wiki/Poly1305)
- [SipHash](/wiki/SipHash)
- [UMAC](/wiki/UMAC_(cryptography))
- [VMAC](/wiki/VMAC)

Authenticated
encryption modes

- [CCM](/wiki/CCM_mode)
- [ChaCha20-Poly1305](/wiki/ChaCha20-Poly1305)
- [CWC](/wiki/CWC_mode)
- [EAX](/wiki/EAX_mode)
- [GCM](/wiki/Galois/Counter_Mode)
- [IAPM](/wiki/IAPM_(mode))
- [OCB](/wiki/OCB_mode)

Attacks

- [Collision attack](/wiki/Collision_attack)
- [Preimage attack](/wiki/Preimage_attack)
- [Birthday attack](/wiki/Birthday_attack)
- [Brute-force attack](/wiki/Brute-force_attack)
- [Rainbow table](/wiki/Rainbow_table)
- [Side-channel attack](/wiki/Side-channel_attack)
- [Length extension attack](/wiki/Length_extension_attack)

Design

- [Avalanche effect](/wiki/Avalanche_effect)
- [Hash collision](/wiki/Hash_collision)
- [Merkle–Damgård construction](/wiki/Merkle%E2%80%93Damg%C3%A5rd_construction)
- [Sponge function](/wiki/Sponge_function)
- [HAIFA construction](/wiki/HAIFA_construction)

Standardization

- [CAESAR Competition](/wiki/CAESAR_Competition)
- [CRYPTREC](/wiki/CRYPTREC)
- [NESSIE](/wiki/NESSIE)
- [NIST hash function competition](/wiki/NIST_hash_function_competition)
- [Password Hashing Competition](/wiki/Password_Hashing_Competition)
- [NSA Suite B](/wiki/NSA_Suite_B_Cryptography)
- [CNSA](/wiki/Commercial_National_Security_Algorithm_Suite)

Utilization

- [Hash-based cryptography](/wiki/Post-quantum_cryptography#Hash-based_cryptography)
- [Merkle tree](/wiki/Merkle_tree)
- [Message authentication](/wiki/Message_authentication)
- [Proof of work](/wiki/Proof_of_work)
- [Salt](/wiki/Salt_(cryptography))
- [Pepper](/wiki/Pepper_(cryptography))

- [v](/wiki/Template:Cryptography_navbox)
- [t](/wiki/Template_talk:Cryptography_navbox)
- [e](/wiki/Special:EditPage/Template:Cryptography_navbox)

[Cryptography](/wiki/Cryptography)General

- [History of cryptography](/wiki/History_of_cryptography)
- [Outline of cryptography](/wiki/Outline_of_cryptography)
- [Classical cipher](/wiki/Classical_cipher)
- [Cryptographic protocol](/wiki/Cryptographic_protocol)

  - [Authentication protocol](/wiki/Authentication_protocol)

- [Cryptographic primitive](/wiki/Cryptographic_primitive)
- [Cryptanalysis](/wiki/Cryptanalysis)
- [Cryptocurrency](/wiki/Cryptocurrency)
- [Cryptosystem](/wiki/Cryptosystem)
- [Cryptographic nonce](/wiki/Cryptographic_nonce)
- [Cryptovirology](/wiki/Cryptovirology)
- [Hash function](/wiki/Hash_function)

  - [Cryptographic hash function](/wiki/Cryptographic_hash_function)
  - [Key derivation function](/wiki/Key_derivation_function)
  - [Secure Hash Algorithms](/wiki/Secure_Hash_Algorithms)

- [Digital signature](/wiki/Digital_signature)
- [Kleptography](/wiki/Kleptography)
- [Key (cryptography)](/wiki/Key_(cryptography))
- [Key exchange](/wiki/Key_exchange)
- [Key generator](/wiki/Key_generator)
- [Key schedule](/wiki/Key_schedule)
- [Key stretching](/wiki/Key_stretching)
- [Keygen](/wiki/Keygen)
- [Machines](/wiki/Template:Cryptography_machines)
- [Ransomware](/wiki/Ransomware)
- [Random number generation](/wiki/Random_number_generation)

  - [Cryptographically secure pseudorandom number generator](/wiki/Cryptographically_secure_pseudorandom_number_generator) (CSPRNG)

- [Pseudorandom noise](/wiki/Pseudorandom_noise) (PRN)
- [Secure channel](/wiki/Secure_channel)
- [Insecure channel](/wiki/Insecure_channel)
- [Subliminal channel](/wiki/Subliminal_channel)
- [Encryption](/wiki/Encryption)
- [Decryption](/wiki/Decryption)
- [End-to-end encryption](/wiki/End-to-end_encryption)
- [Harvest now, decrypt later](/wiki/Harvest_now,_decrypt_later)
- [Information-theoretic security](/wiki/Information-theoretic_security)
- [Plaintext](/wiki/Plaintext)
- [Codetext](/wiki/Codetext)
- [Ciphertext](/wiki/Ciphertext)
- [Shared secret](/wiki/Shared_secret)
- [Trapdoor function](/wiki/Trapdoor_function)
- [Trusted timestamping](/wiki/Trusted_timestamping)
- [Key-based routing](/wiki/Key-based_routing)
- [Onion routing](/wiki/Onion_routing)
- [Garlic routing](/wiki/Garlic_routing)
- [Kademlia](/wiki/Kademlia)
- [Mix network](/wiki/Mix_network)

Mathematics

- [Cryptographic hash function](/wiki/Cryptographic_hash_function)
- [Block cipher](/wiki/Block_cipher)
- [Stream cipher](/wiki/Stream_cipher)
- [Symmetric-key algorithm](/wiki/Symmetric-key_algorithm)
- Authenticated encryption
- [Public-key cryptography](/wiki/Public-key_cryptography)
- [Quantum key distribution](/wiki/Quantum_key_distribution)
- [Quantum cryptography](/wiki/Quantum_cryptography)
- [Post-quantum cryptography](/wiki/Post-quantum_cryptography)
- [Message authentication code](/wiki/Message_authentication_code)
- [Random numbers](/wiki/Cryptographically_secure_pseudorandom_number_generator)
- [Steganography](/wiki/Steganography)

- [Category](/wiki/Category:Cryptography)

Retrieved from "[https://en.wikipedia.org/w/index.php?title=Authenticated_encryption&oldid=1323669885](https://en.wikipedia.org/w/index.php?title=Authenticated_encryption&oldid=1323669885)"[Categories](/wiki/Help:Category): 

- [Symmetric-key cryptography](/wiki/Category:Symmetric-key_cryptography)
- [Message authentication codes](/wiki/Category:Message_authentication_codes)

Hidden categories: 

- [Articles with short description](/wiki/Category:Articles_with_short_description)
- [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata)

-  This page was last edited on 23 November 2025, at 03:17 (UTC).
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
- [Mobile view](//en.wikipedia.org/w/index.php?title=Authenticated_encryption&mobileaction=toggle_view_mobile)

- https://www.wikimedia.org/
- https://www.mediawiki.org/

SearchSearchToggle the table of contentsAuthenticated encryption#######13 languages[Add topic](#)
