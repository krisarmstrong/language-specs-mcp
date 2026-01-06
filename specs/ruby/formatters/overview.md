1.82/index.html

- [RuboCop](index.html)
- [Home](index.html)

default[default](index.html)[1.82](1.82/index.html)[1.81](1.81/index.html)[1.80](1.80/index.html)[1.79](1.79/index.html)[1.78](1.78/index.html)[1.77](1.77/index.html)[1.76](1.76/index.html)[1.75](1.75/index.html)[1.74](1.74/index.html)[1.73](1.73/index.html)[1.72](1.72/index.html)[1.71](1.71/index.html)[1.70](1.70/index.html)[1.69](1.69/index.html)[1.68](1.68/index.html)[1.67](1.67/index.html)[1.66](1.66/index.html)[1.65](1.65/index.html)[1.64](1.64/index.html)[1.63](1.63/index.html)[1.62](1.62/index.html)[1.61](1.61/index.html)[1.60](1.60/index.html)[1.0](1.0/index.html)[Edit this Page](https://github.com/rubocop/rubocop/edit/master/docs/modules/ROOT/pages/index.adoc)

# RuboCop

Role models are important.

 — Officer Alex J. Murphy / RoboCop 

## #overviewOverview

RuboCop is a Ruby static code analyzer (a.k.a. linter) and code formatter. Out of the box it will enforce many of the guidelines outlined in the community [Ruby Style Guide](https://rubystyle.guide).

RuboCop packs a lot of features on top of what you’d normally expect from a linter:

- 

Works with every major Ruby implementation

- 

Autocorrection of many of the code offenses it detects

- 

Robust code formatting capabilities

- 

Multiple result formatters for both interactive use and for feeding data into other tools

- 

Ability to have different configuration for different parts of your codebase

- 

Ability to disable certain cops only for specific files or parts of files

- 

Extremely flexible configuration that allows you to adapt RuboCop to pretty much every style and preference

- 

It’s easy to extend RuboCop with custom cops and formatters

- 

A vast number of ready-made [extensions](extensions.html) (e.g. `rubocop-rails`, `rubocop-rspec`, `rubocop-performance` and `rubocop-minitest`)

- 

Wide editor/IDE support

- 

Many online services use RuboCop internally (e.g. HoundCI and CodeClimate)

- 

Best logo/stickers ever

The project is closely tied to several efforts to document and promote the best practices of the Ruby community:

- 

[Ruby Style Guide](https://rubystyle.guide/)

- 

[Rails Style Guide](https://rails.rubystyle.guide/)

- 

[RSpec Style Guide](https://rspec.rubystyle.guide/)

- 

[Minitest Style Guide](https://minitest.rubystyle.guide/)

A long-term goal of RuboCop (and its core extensions) is to cover with cops all the guidelines from the community style guides.

## #philosophyPhilosophy

Early on RuboCop aimed to be an opinionated linter/formatter that adhered very closely to the Ruby Style Guide (think `gofmt` and the like). In those days cops supported just a single style and you couldn’t even turn individual cops off. Eventually, we realized that in the Ruby community there were so many competing styles and preferences that it was going to be really challenging to find one set of defaults that makes everyone happy. Part of this was Ruby’s own culture and philosophy, part was the lack of common standards for almost 20 years. It’s hard to undo any of those, but it’s also not really necessary.

The early feedback we got led us to adopt a philosophy of (extreme) configurability and flexibility, and trying to account for every common style of programming in Ruby. While we still believe that there’s a lot of merit to just sticking to the community style guides, we acknowledge that Ruby is all about diversity and doing things the way that makes you happy. Whatever style preferences you have RuboCop is there for you. That’s our promises and our guarantee. Within the subjective limits of sanity that is.

## #next-stepsNext Steps

So, what to do next? While you can peruse the documentation in whatever way you’d like, here are a few recommendations:

- 

See ["Basic Usage"](usage/basic_usage.html) to get yourself familiar with RuboCop’s capabilities.

- 

Adjust RuboCop to your style/preferences. RuboCop is an extremely flexible tool and most aspects of its behavior can be tweaked via various [configuration
options](https://github.com/rubocop/rubocop/blob/master/config/default.yml). See ["Configuration"](configuration.html) for more details.

- 

See ["Versioning"](versioning.html) for information about RuboCop versioning, updates, and the process of introducing new cops.

- 

Explore the [existing extensions](extensions.html).

[Installation](installation.html)
