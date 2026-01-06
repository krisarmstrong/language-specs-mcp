# PHPStan

PHPStan is a static analysis tool for PHP that finds bugs without running code.

Version: 2.1
Source: https://phpstan.org/

## Installation

```bash
composer require --dev phpstan/phpstan
```

## Usage

```bash
# Analyze at default level
vendor/bin/phpstan analyse src/

# Specify level (0-10)
vendor/bin/phpstan analyse src/ --level=5

# With config file
vendor/bin/phpstan analyse -c phpstan.neon
```

## Configuration

Create `phpstan.neon`:

```neon
parameters:
    level: 6
    paths:
        - src
        - tests
    excludePaths:
        - src/legacy
    ignoreErrors:
        - '#Call to an undefined method#'
```

## Rule Levels

PHPStan offers 11 progressive levels (0-10):

### Level 0
- Basic checks
- Unknown classes, functions
- Unknown methods on `$this`

### Level 1
- Possibly undefined variables
- Magic methods and properties

### Level 2
- All expressions method checking
- PHPDocs validation

### Level 3
- Return type validation
- Property assignment checks

### Level 4
- Basic dead code checking
- Always false instanceof
- Type checks

### Level 5
- Argument type validation
- Methods and functions

### Level 6
- Missing typehints reported

### Level 7
- Partially incorrect union types
- Methods on some union members

### Level 8
- Nullable type method calls
- Strict checking

### Level 9
- Mixed type restrictions
- Operations must pass to mixed

### Level 10
- Strictest mixed handling
- Implicit mixed errors

## Extensions

```neon
includes:
    - vendor/phpstan/phpstan-strict-rules/rules.neon
    - vendor/phpstan/phpstan-deprecation-rules/rules.neon
```

### Popular Extensions
- `phpstan-strict-rules` - Extra strict checks
- `phpstan-deprecation-rules` - Deprecation warnings
- `phpstan-symfony` - Symfony framework
- `phpstan-doctrine` - Doctrine ORM
- `phpstan-phpunit` - PHPUnit testing

## Ignoring Errors

```php
/** @phpstan-ignore-next-line */
$foo = $bar->unknownMethod();

/** @phpstan-ignore argument.type */
doSomething($value);
```

## Baseline

```bash
# Generate baseline for existing errors
vendor/bin/phpstan analyse --generate-baseline

# Use baseline
vendor/bin/phpstan analyse --baseline=phpstan-baseline.neon
```
