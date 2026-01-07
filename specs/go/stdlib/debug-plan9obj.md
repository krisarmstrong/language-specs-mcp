Go Security Policy - The Go Programming Language/[Skip to Main Content](#main-content)

- [Why Go arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Case Studies](/solutions/case-studies)

Common problems companies solve with Go

  - [Use Cases](/solutions/use-cases)

Stories about how and why companies use Go

  - [Security](/security/)

How Go can help keep you secure by default

- [Learn](/learn/) Press Enter to activate/deactivate dropdown 
- [Docs arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Go Spec](/ref/spec)

The official Go language specification

  - [Go User Manual](/doc)

A complete introduction to building software with Go

  - [Standard library](https://pkg.go.dev/std)

Reference documentation for Go's standard library

  - [Release Notes](/doc/devel/release)

Learn what's new in each Go release

  - [Effective Go](/doc/effective_go)

Tips for writing clear, performant, and idiomatic Go code

- [Packages](https://pkg.go.dev) Press Enter to activate/deactivate dropdown 
- [Community arrow_drop_down](#) Press Enter to activate/deactivate dropdown 

  - [Recorded Talks](/talks/)

Videos from prior events

  - [Meetups
                           open_in_new](https://www.meetup.com/pro/go)

Meet other local Go developers

  - [Conferences
                           open_in_new](/wiki/Conferences)

Learn and network with Go developers from around the world

  - [Go blog](/blog)

The Go project's official blog.

  - [Go project](/help)

Get help and stay informed from Go

  -  Get connected 

https://groups.google.com/g/golang-nutshttps://github.com/golanghttps://twitter.com/golanghttps://www.reddit.com/r/golang/https://invite.slack.golangbridge.org/https://stackoverflow.com/tags/go

/

- [Why Go navigate_next](#)[navigate_beforeWhy Go](#)

  - [Case Studies](/solutions/case-studies)
  - [Use Cases](/solutions/use-cases)
  - [Security](/security/)

- [Learn](/learn/)
- [Docs navigate_next](#)[navigate_beforeDocs](#)

  - [Go Spec](/ref/spec)
  - [Go User Manual](/doc)
  - [Standard library](https://pkg.go.dev/std)
  - [Release Notes](/doc/devel/release)
  - [Effective Go](/doc/effective_go)

- [Packages](https://pkg.go.dev)
- [Community navigate_next](#)[navigate_beforeCommunity](#)

  - [Recorded Talks](/talks/)
  - [Meetups
                           open_in_new](https://www.meetup.com/pro/go)
  - [Conferences
                           open_in_new](/wiki/Conferences)
  - [Go blog](/blog)
  - [Go project](/help)
  - Get connectedhttps://groups.google.com/g/golang-nutshttps://github.com/golanghttps://twitter.com/golanghttps://www.reddit.com/r/golang/https://invite.slack.golangbridge.org/https://stackoverflow.com/tags/go

1. [Documentation](/doc/)
2. [Security](/doc/security/)
3. [Go Security Policy](/doc/security/policy)

# Go Security Policy

## Overview

This document explains the Go Security team’s process for handling issues reported and what to expect in return.

## Reporting a Security Bug

All security bugs in the Go distribution should be reported by email to [security@golang.org](mailto:security@golang.org). This mail is delivered to the Go Security team.

To ensure your report is not marked as spam, please include the word “vulnerability” anywhere in your email. Please use a descriptive subject line for your report email.

Your email will be acknowledged within 7 days, and you’ll be kept up to date with the progress until resolution. Your issue will be fixed or made public within 90 days.

If you have not received a reply to your email within 7 days, please follow up with the Go Security team again at [security@golang.org](mailto:security@golang.org). Please make sure the word vulnerability is in your email.

If after 3 more days you have still not received an acknowledgement of your report, it is possible that your email might have been marked as spam. In that case, please [file an issue here](https://g.co/vulnz). Select “I want to report a technical security or an abuse risk related bug in a Google product (SQLi, XSS, etc.)”, and list “Go” as the affected product.

## Tracks

Depending on the nature of your issue, it will be categorized by the Go Security team as an issue in the PUBLIC, PRIVATE, or URGENT track. All security issues will be issued CVE numbers.

The Go Security team does not assign traditional fine-grained severity labels (e.g CRITICAL, HIGH, MEDIUM, LOW) to security issues because severity depends highly on how a user is using the affected API or functionality.

For example, the impact of a resource exhaustion issue in the `encoding/json` parser depends on what is being parsed. If the user is parsing trusted JSON files from their local filesystem, the impact is likely to be low. If the user is parsing untrusted arbitrary JSON from an HTTP request body, the impact may be much higher.

That said, the following issue tracks do signal how severe and/or wide-reaching the Security team believes an issue to be. For example, an issue with medium to significant impact for many users is a PRIVATE track issue in this policy, and an issue with negligible to minor impact, or which affects only a small subset of users, is a PUBLIC track issue.

### PUBLIC

Issues in the PUBLIC track affect niche configurations, have very limited impact, or are already widely known.

PUBLIC track issues are labeled with [Proposal-Security](https://github.com/golang/go/labels/Proposal-Security), discussed through the [Go proposal review process](https://go.googlesource.com/proposal/+/master/README.md#proposal-review)fixed in public, and get backported to the next scheduled [minor
releases](/wiki/MinorReleases) (which occur ~monthly). The release announcement includes details of these issues, but there is no pre-announcement.

Examples of past PUBLIC issues include:

- [#44916](/issue/44916): archive/zip: can panic when calling Reader.Open
- [#44913](/issue/44913): encoding/xml: infinite loop when using xml.NewTokenDecoder with a custom TokenReader
- [#43786](/issue/43786): crypto/elliptic: incorrect operations on the P-224 curve
- [#40928](/issue/40928): net/http/cgi,net/http/fcgi: Cross-Site Scripting (XSS) when Content-Type is not specified
- [#40618](/issue/40618): encoding/binary: ReadUvarint and ReadVarint can read an unlimited number of bytes from invalid inputs
- [#36834](/issue/36834): crypto/x509: certificate validation bypass on Windows 10

### PRIVATE

Issues in the PRIVATE track are violations of committed security properties.

PRIVATE track issues are fixed in the next scheduled [minor
releases](/wiki/MinorReleases), and are kept private until then.

Three to seven days before the release, a pre-announcement is sent to golang-announce, announcing the presence of one or more security fixes in the upcoming releases, and whether the issues affect the standard library, the toolchain, or both, as well as reserved CVE IDs for each of the fixes.

For issues that are present in a [major version release candidate](/s/release), we follow the same process, including fixes in the next scheduled release candidate.

Some examples of past PRIVATE issues include:

- [#53416](/issue/53416): path/filepath: stack exhaustion in Glob
- [#53616](/issue/53616): go/parser: stack exhaustion in all Parse* functions
- [#54658](/issue/54658): net/http: handle server errors after sending GOAWAY
- [#56284](/issue/56284): syscall, os/exec: unsanitized NUL in environment variables

### URGENT

URGENT track issues are a threat to the Go ecosystem’s integrity, or are being actively exploited in the wild leading to severe damage. There are no recent examples, but they would include remote code execution in net/http, or practical key recovery in crypto/tls.

URGENT track issues are fixed in private, and trigger an immediate dedicated security release, possibly with no pre-announcement.

## Flagging Existing Issues as Security-related

If you believe that an [existing issue](/issue) is security-related, we ask that you send an email to [security@golang.org](mailto:security@golang.org). The email should include the issue ID and a short description of why it should be handled according to this security policy.

## Disclosure Process

The Go project uses the following disclosure process:

1. 

Once the security report is received it is assigned a primary handler. This person coordinates the fix and release process.

2. 

The issue is confirmed and a list of affected software is determined.

3. 

Code is audited to find any potential similar problems.

4. 

If it is determined, in consultation with the submitter, that a CVE number is required, the primary handler will obtain one.

5. 

Fixes are prepared for the two most recent major releases and the head/master revision. Fixes are prepared for the two most recent major releases and merged to head/master.

6. 

On the date that the fixes are applied, announcements are sent to [golang-announce](https://groups.google.com/group/golang-announce), [golang-dev](https://groups.google.com/group/golang-dev), and [golang-nuts](https://groups.google.com/group/golang-nuts).

This process can take some time, especially when coordination is required with maintainers of other projects. Every effort will be made to handle the bug in as timely a manner as possible, however it’s important that we follow the process described above to ensure that disclosures are handled consistently.

For security issues that include the assignment of a CVE number, the issue is listed publicly under the [“Golang” product on the CVEDetails website](https://www.cvedetails.com/vulnerability-list/vendor_id-14185/Golang.html) as well as the [National Vulnerability Disclosure site](https://web.nvd.nist.gov/view/vuln/search).

## Receiving Security Updates

The best way to receive security announcements is to subscribe to the [golang-announce](https://groups.google.com/forum/#!forum/golang-announce) mailing list. Any messages pertaining to a security issue will be prefixed with `[security]`.

## Comments on This Policy

If you have any suggestions to improve this policy, please [file an issue](/issue/new) for discussion.

[Why Go](/solutions/)[Use Cases](/solutions/use-cases)[Case Studies](/solutions/case-studies)[Get Started](/learn/)[Playground](/play)[Tour](/tour/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](/help/)[Packages](https://pkg.go.dev)[Standard Library](/pkg/)[About Go Packages](https://pkg.go.dev/about)[About](/project)[Download](/dl/)[Blog](/blog/)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](/doc/devel/release)[Brand Guidelines](/brand)[Code of Conduct](/conduct)[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/) Opens in new window. 

- [Copyright](/copyright)
- [Terms of Service](/tos)
- [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
- [Report an Issue](/s/website-issue)
- 

https://google.comgo.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)Okay
