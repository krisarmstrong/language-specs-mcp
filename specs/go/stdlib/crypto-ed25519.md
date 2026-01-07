Introduction 

# Ed25519: high-speed high-security signatures

Introduction[Software](software.html)[Papers](papers.html)

# Introduction

 Ed25519 is a public-key signature system with several attractive features: 

- Fast single-signature verification. The [software](software.html) takes only 273364 cycles to verify a signature on Intel's widely deployed Nehalem/Westmere lines of CPUs. (This performance measurement is for short messages; for very long messages, verification time is dominated by hashing time.) Nehalem and Westmere include all Core i7, i5, and i3 CPUs released between 2008 and 2010, and most Xeon CPUs released in the same period. 
- Even faster batch verification. The software performs a batch of 64 separate signature verifications (verifying 64 signatures of 64 messages under 64 public keys) in only 8.55 million cycles, i.e., under 134000 cycles per signature. The software fits easily into L1 cache, so contention between cores is negligible: a quad-core 2.4GHz Westmere verifies 71000 signatures per second, while keeping the maximum verification latency below 4 milliseconds. 
- Very fast signing. The software takes only 87548 cycles to sign a message. A quad-core 2.4GHz Westmere signs 109000 messages per second. 
- Fast key generation. Key generation is almost as fast as signing. There is a slight penalty for key generation to obtain a secure random number from the operating system; /dev/urandom under Linux costs about 6000 cycles. 
- High security level. This system has a 2^128 security target; breaking it has similar difficulty to breaking NIST P-256, RSA with ~3000-bit keys, strong 128-bit block ciphers, etc. The best attacks known actually cost more than 2^140 bit operations on average, and degrade quadratically in success probability as the number of bit operations drops. 
- Foolproof session keys. Signatures are generated deterministically; key generation consumes new randomness but new signatures do not. This is not only a speed feature but also a security feature, directly relevant to the recent collapse of the Sony PlayStation 3 security system. 
- Collision resilience. Hash-function collisions do not break this system. This adds a layer of defense against the possibility of weakness in the selected hash function. 
- No secret array indices. The software never reads or writes data from secret addresses in RAM; the pattern of addresses is completely predictable. The software is therefore immune to cache-timing attacks, hyperthreading attacks, and other side-channel attacks that rely on leakage of addresses through the CPU cache. 
- No secret branch conditions. The software never performs conditional branches based on secret data; the pattern of jumps is completely predictable. The software is therefore immune to side-channel attacks that rely on leakage of information through the branch-prediction unit. 
- Small signatures. Signatures fit into 64 bytes. These signatures are actually compressed versions of longer signatures; the times for compression and decompression are included in the cycle counts reported above. 
- Small keys. Public keys consume only 32 bytes. The times for compression and decompression are again included. 

 The numbers 87548 and 273364 shown above are official [eBATS](https://bench.cr.yp.to) reports for a Westmere CPU (Intel Xeon E5620, hydra2). 

 Ed25519 signatures are elliptic-curve signatures, carefully engineered at several levels of design and implementation to achieve very high speeds without compromising security. 

## Contributors (alphabetical order)

[Daniel J. Bernstein](https://cr.yp.to/djb.html), University of Illinois at Chicago 

[Niels Duif](http://www.nielsduif.nl/), Technische Universiteit Eindhoven 

[Tanja Lange](https://hyperelliptic.org/tanja), Technische Universiteit Eindhoven 

[Peter Schwabe](http://www.cryptojedi.org/users/peter/), National Taiwan University 

[Bo-Yin Yang](http://www.iis.sinica.edu.tw/pages/byyang/), Academia Sinica 

## Acknowledgments

 This work was supported by the U.S. National Science Foundation under grant 1018836. "Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation." 

 This work was supported by the European Commission under Contract ICT-2007-216676 ECRYPT II. 

 This work was supported by the National Science Council, National Taiwan University and Intel Corporation under Grants NSC99-2911-I-002-001 and 99-2218-E-001-007. 

 This work was supported by an Academia Sinica Career Award. 

 Part of this work was carried out when Peter Schwabe was employed by Academia Sinica, Taiwan. 

 Part of this work was carried out when Niels Duif was employed by Compumatica secure networks BV, the Netherlands. 

## Version

 This is version 2017.01.22 of the index.html web page.
