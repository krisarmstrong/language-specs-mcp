Go Wiki: PortingPolicy - The Go Programming Language/[Skip to Main Content](#main-content)

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

# Go Wiki: PortingPolicy

## Introduction

This document is about the policy for adding a new port to the main Go repository. By port we mean an operating system + architecture combination, such as linux/386.

The goal of this policy is to clarify what the Go project tries to promise for ports and to avoid the accumulation of incomplete or broken ports.

## Requirements for a new port

Before any code relating to a port can be added to the main Go repository, the following must all be done:

- 

A [proposal](https://go.dev/s/proposal) must be filed and accepted in which the Go team accepts overall responsibility for having the new port in the core Go tree. In general, each new port carries an upkeep cost separate from the direct maintenance. That cost varies by port, depending on how similar a new port is to existing ones. The cost must be balanced by an overall benefit in the form of potential new users or use cases for Go.

- 

At least two developers must be named (and agree) to maintain the port, by making required updates in a timely manner as architecture or operating system requirements change.

  - Port maintainers are listed in the subteams of [@golang/port-maintainers](https://github.com/orgs/golang/teams/port-maintainers). To be added or removed as a maintainer for an existing port, please [file an issue](https://go.dev/issue/new).
  - Changes that are specific to a particular port should normally be reviewed first by one of the port maintainers (though not the one who wrote the change, of course). We currently require two reviews for each change, so changes will still typically be reviewed by someone who is not a port maintainer, but ideally that can be a more casual review by someone less familiar with the port details.

- 

A developer must be named (and agree) to maintain the builder, the machine trying each git revision and providing data for [https://build.golang.org](https://build.golang.org).

  - Builder maintainers are listed in [x/build/dashboard/builders.go](https://cs.opensource.google/go/x/build/+/master:dashboard/builders.go). To update the owners for a builder, please [send a change](https://go.dev/doc/contribute) to that file.

- 

The builder must already be running (and failing, because the code is not yet in the main repository).

- 

All CLs necessary to run all.bash successfully must have been sent for review. Typically this will be a handful of CLs split by the part of the tree they change.

Once those conditions are satisfied, the Go team can accept the port and begin to merge the CLs. Once the CLs are all submitted, all.bash must pass, so that the builder reports “ok” in the dashboard.

## Other repositories

Although it is not part of the core repository, the x/sys repository should add support for the new port before the release happens because it is the official place to add new system calls. It’s OK to add support for a new port in the x/sys repository before working on the main repository.

## First class ports

Some ports are considered “first class”. The distinction is mostly about releases.

A first class port has these properties:

- Broken builds block releases 

  - All contributors are effectively responsible for these ports (You break it, you fix it, or find someone who can.)
  - Requires Google’s Go team to own the builder machine

- Installation is documented at [https://go.dev/doc/install](https://go.dev/doc/install)

Graduating a port to “first class” is at the discretion of the Go team at Google, and requires an accepted proposal.

The current first class ports are:

- darwin/amd64
- darwin/arm64
- linux/386
- linux/amd64
- linux/arm
- linux/arm64
- windows/386
- windows/amd64

All Linux first class ports are for systems using glibc only. Linux systems using other C libraries are not fully supported and are not treated as first class.

## Maintaining a port

In general, people changing the Go tools and standard library must not break any of the first class ports listed above. A change that breaks a first class port must be fixed or rolled back.

A change that breaks a secondary port will not necessarily be rolled back. If there is some reasonable possibility of breaking a secondary port developers are encouraged to make sure that the ports continue to work (for example, by running [port-specific trybots](/wiki/SlowBots)). Developers are also encouraged to notify secondary port maintainers of any possible port-specific problems, which they can do by reaching out to the appropriate [GitHub team(s)](https://github.com/orgs/golang/teams/port-maintainers/teams). That said, ultimately the port maintainers are responsible for keeping their ports working.

## Broken ports

- If a port stops working, including the case where a builder stops working, we can decide to mark the port as broken. 

  - Or in some cases we can roll back the change that broke it; this is a judgement call.

- In general, a port can be considered broken if its builder has failed multiple times in a development cycle with a failure mode that does not occur for first class ports, and that failure mode is not believed to have been fixed or suppressed by a change in either a Go repository or the builder’s configuration, and maintainers are not actively working on a solution.
- Any approver can declare that a port that meets these criteria is broken.
- If a port is broken in release 1.N, then the core Go team can choose to remove the port from release 1.N+1. 

  - This is not obligatory and will depend on whether anybody is willing and able to maintain the port going forward.

The goal here is not to get ports out of the tree; if people are actively working on the port they should have as much as latitude as possible to fix it. Removing a formerly working port should be a last resort. Finding a new maintainer is always preferable.

## Removing old operating system and architecture versions

To allow development effort to focus on systems that are widely available to Go users, over time we may remove support for older operating systems and architectures, especially older operating system versions and architecture revisions.

The important considerations when deciding whether to remove support for an old operating system or architecture version are:

- Availability. If the operating system is no longer distributed or the hardware is no longer manufactured, for example, there’s not a clear need to keep it going. For example, Go’s ppc64 port no longer supports the IBM POWER5 architecture.
- Manufacturer support. If the operating system or architecture is no longer supported by its manufacturer, that is a strong signal that a future version of Go can remove support as well. For example, each year, Apple typically issues one new version of macOS and deprecates one old version. [Go typically deprecates old macOS versions at the same rate](https://github.com/golang/go/issues/23011#issuecomment-738395341).
- Actual or expected user base. If there are relatively few users, significant effort to maintain a port may not be worthwhile.
- Ongoing costs. Ports that require significant ongoing debugging or implementation efforts will be scrutinized more than ports that don’t.

When the considerations weigh in favor of removing a port and a [proposal is accepted](https://go.dev/s/proposal-process), Go 1.N’s release notes will announce that support for a given operating system or architecture will be dropped in Go 1.(N+1).

Announcements for end of support are tracked in: [issue 23011 for macOS](https://go.dev/issue/23011), [issue 52188 for Windows](https://go.dev/issue/52188), and [issue 60792 for Linux](https://go.dev/issue/60792).

## Getting started

See [https://groups.google.com/forum/#!topic/golang-dev/SRUK7yJVA0c](https://groups.google.com/forum/#!topic/golang-dev/SRUK7yJVA0c) for some discussion on how to go about writing a new port.

## Comments and Questions

Comments or questions about the policy should be sent to golang-dev.

This content is part of the [Go Wiki](/wiki/).

[Why Go](/solutions/)[Use Cases](/solutions/use-cases)[Case Studies](/solutions/case-studies)[Get Started](/learn/)[Playground](/play)[Tour](/tour/)[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)[Help](/help/)[Packages](https://pkg.go.dev)[Standard Library](/pkg/)[About Go Packages](https://pkg.go.dev/about)[About](/project)[Download](/dl/)[Blog](/blog/)[Issue Tracker](https://github.com/golang/go/issues)[Release Notes](/doc/devel/release)[Brand Guidelines](/brand)[Code of Conduct](/conduct)[Connect](https://www.twitter.com/golang)[Twitter](https://www.twitter.com/golang)[GitHub](https://github.com/golang)[Slack](https://invite.slack.golangbridge.org/)[r/golang](https://reddit.com/r/golang)[Meetup](https://www.meetup.com/pro/go)[Golang Weekly](https://golangweekly.com/) Opens in new window. 

- [Copyright](/copyright)
- [Terms of Service](/tos)
- [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
- [Report an Issue](/s/website-issue)
- 

https://google.comgo.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)Okay
