# RuboCop

RuboCop is a Ruby static code analyzer (linter) and formatter that enforces the community Ruby Style Guide.

Version: 1.72.2
Source: https://docs.rubocop.org/rubocop/

## Installation

```bash
gem install rubocop
```

Or in Gemfile:
```ruby
gem 'rubocop', require: false
```

## Configuration

RuboCop uses `.rubocop.yml` for configuration:

```yaml
AllCops:
  TargetRubyVersion: 3.2
  NewCops: enable

Style/StringLiterals:
  EnforcedStyle: double_quotes

Metrics/MethodLength:
  Max: 20
```

## Cop Categories

RuboCop organizes cops into departments:

| Department | Description | Cop Count |
|------------|-------------|-----------|
| Bundler | Gemfile conventions | 7 |
| Gemspec | Gemspec file conventions | 10 |
| Layout | Code formatting and whitespace | 90+ |
| Lint | Potential errors and code smells | 150+ |
| Metrics | Code complexity measurements | 10 |
| Naming | Naming conventions | 19 |
| Security | Security vulnerabilities | 7 |
| Style | Code style enforcement | 270+ |

## Usage

```bash
# Analyze current directory
rubocop

# Analyze specific files
rubocop app/models/*.rb

# Auto-correct offenses
rubocop -a

# Auto-correct including unsafe corrections
rubocop -A

# Generate TODO configuration
rubocop --auto-gen-config
```

## Extensions

- `rubocop-rails` - Rails-specific cops
- `rubocop-rspec` - RSpec-specific cops
- `rubocop-performance` - Performance optimization cops
- `rubocop-minitest` - Minitest-specific cops
- `rubocop-rake` - Rake-specific cops

## Disabling Cops

```ruby
# rubocop:disable Style/StringLiterals
"double quotes"
# rubocop:enable Style/StringLiterals

# rubocop:disable all
# rubocop:enable all

# rubocop:todo Metrics/MethodLength
```
