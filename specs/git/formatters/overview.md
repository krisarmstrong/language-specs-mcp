Commitizen[Skip to content](#about). Commitizen  Introduction  Initializing search 

[commitizen-tools/commitizen](https://github.com/commitizen-tools/commitizen). Commitizen [commitizen-tools/commitizen](https://github.com/commitizen-tools/commitizen)

-  Introduction [Introduction](.) Table of contents 

  - [About](#about)

    - [What Commitizen Does](#what-commitizen-does)
    - [Key Benefits](#key-benefits)
    - [Features](#features)

  - [Getting Started](#getting-started)

    - [Requirements](#requirements)
    - [Installation](#installation)

      - [Global Installation (Recommended)](#global-installation-recommended)
      - [Project-Specific Installation](#project-specific-installation)

    - [Basic Commands](#basic-commands)

      - [Initialize Commitizen](#initialize-commitizen)
      - [Create Commits](#create-commits)
      - [Version Management](#version-management)

    - [Advanced Usage](#advanced-usage)

      - [Get Project Version](#get-project-version)
      - [Pre-commit Integration](#pre-commit-integration)

  - [Help & Reference](#help-reference)

    - [Command Line Interface](#command-line-interface)
    - [Quick Reference](#quick-reference)
    - [Additional Resources](#additional-resources)
    - [Getting Help](#getting-help)

  - [Setting up bash completion](#setting-up-bash-completion)

    - [Supported Shells](#supported-shells)
    - [Installation Methods](#installation-methods)

      - [Global Installation (Recommended)](#global-installation-recommended_1)
      - [User-Specific Installation](#user-specific-installation)
      - [Temporary Installation](#temporary-installation)

    - [Verification](#verification)

  - [Sponsors](#sponsors)

-  Commands  Commands 

  - [init](commands/init/)
  - [commit](commands/commit/)
  - [bump](commands/bump/)
  - [check](commands/check/)
  - [changelog](commands/changelog/)
  - [example](commands/example/)
  - [info](commands/info/)
  - [ls](commands/ls/)
  - [schema](commands/schema/)
  - [version](commands/version/)

-  Configuration  Configuration 

  - [Configuration File](config/configuration_file/)
  - [Version Provider](config/version_provider/)
  - [bump](config/bump/)
  - [commit](config/commit/)
  - [check](config/check/)
  - [changelog](config/changelog/)
  - [Misc Options](config/option/)

-  Advanced Customization  Advanced Customization 

  - [Configuration File](customization/config_file/)
  - [Customized Python Class](customization/python_class/)
  - [Changelog Template](customization/changelog_template/)

-  Tutorials  Tutorials 

  - [Commit Message Best Practices](tutorials/writing_commits/)
  - [Managing tags formats](tutorials/tag_format/)
  - [Auto check commits](tutorials/auto_check/)
  - [Auto prepare commit message](tutorials/auto_prepare_commit_message/)
  - [GitLab CI](tutorials/gitlab_ci/)
  - [GitHub Actions](tutorials/github_actions/)
  - [Jenkins pipeline](tutorials/jenkins_pipeline/)
  - [Developmental releases](tutorials/dev_releases/)
  - [Monorepo support](tutorials/monorepo_guidance/)

- [FAQ](faq/)
- [Features we won't add](features_wont_add/)
- [Exit Codes](exit_codes/)
-  Third-Party Commitizen Plugins  Third-Party Commitizen Plugins 

  - [About](third-party-plugins/about/)
  - [commitizen-deno-provider](third-party-plugins/commitizen-deno-provider/)
  - [Commitizen emoji (Unmaintained)](third-party-plugins/commitizen-emoji/)
  - [Conventional JIRA](third-party-plugins/conventional-jira/)
  - [cz-ai](third-party-plugins/cz-ai/)
  - [cz-conventional-gitmoji](third-party-plugins/cz-conventional-gitmoji/)
  - [cz-emoji](third-party-plugins/cz-emoji/)
  - [Conventional Legacy (cz_legacy)](third-party-plugins/cz-legacy/)
  - [cz-path](third-party-plugins/cz-path/)
  - [GitHub JIRA Conventional](third-party-plugins/github-jira-conventional/)

- [Contributing](contributing/)
- [Contributing TL;DR](contributing_tldr/)
- [Resources](external_links/)

 Table of contents 

- [About](#about)

  - [What Commitizen Does](#what-commitizen-does)
  - [Key Benefits](#key-benefits)
  - [Features](#features)

- [Getting Started](#getting-started)

  - [Requirements](#requirements)
  - [Installation](#installation)

    - [Global Installation (Recommended)](#global-installation-recommended)
    - [Project-Specific Installation](#project-specific-installation)

  - [Basic Commands](#basic-commands)

    - [Initialize Commitizen](#initialize-commitizen)
    - [Create Commits](#create-commits)
    - [Version Management](#version-management)

  - [Advanced Usage](#advanced-usage)

    - [Get Project Version](#get-project-version)
    - [Pre-commit Integration](#pre-commit-integration)

- [Help & Reference](#help-reference)

  - [Command Line Interface](#command-line-interface)
  - [Quick Reference](#quick-reference)
  - [Additional Resources](#additional-resources)
  - [Getting Help](#getting-help)

- [Setting up bash completion](#setting-up-bash-completion)

  - [Supported Shells](#supported-shells)
  - [Installation Methods](#installation-methods)

    - [Global Installation (Recommended)](#global-installation-recommended_1)
    - [User-Specific Installation](#user-specific-installation)
    - [Temporary Installation](#temporary-installation)

  - [Verification](#verification)

- [Sponsors](#sponsors)

# Introduction

https://github.com/commitizen-tools/commitizen/actionshttps://github.com/commitizen-tools/commitizen/actions/workflows/links.ymlhttps://conventionalcommits.orghttps://pypi.org/project/commitizen/https://pypi.org/project/commitizen/https://pypi.org/project/commitizen/https://anaconda.org/conda-forge/commitizenhttps://formulae.brew.sh/formula/commitizenhttps://codecov.io/gh/commitizen-tools/commitizenhttps://github.com/pre-commit/pre-commit

[Commitizen Documentation Site](https://commitizen-tools.github.io/commitizen/)

## About[¶](#about)

Commitizen is a powerful release management tool that helps teams maintain consistent and meaningful commit messages while automating version management.

### What Commitizen Does[¶](#what-commitizen-does)

By enforcing standardized commit conventions (defaulting to [Conventional Commits](https://www.conventionalcommits.org)), Commitizen helps teams:

- Write clear, structured commit messages
- Automatically manage version numbers using semantic versioning
- Generate and maintain changelogs
- Streamline the release process

### Key Benefits[¶](#key-benefits)

With just a simple `cz bump` command, Commitizen handles:

1. Version Management: Automatically bumps version numbers and updates version files based on your commit history
2. Changelog Generation: Creates and updates changelogs following the [Keep a changelog](https://keepachangelog.com/) format
3. Commit Standardization: Enforces consistent commit message formats across your team

This standardization makes your commit history more readable and meaningful, while the automation reduces manual work and potential errors in the release process.

### Features[¶](#features)

- Interactive CLI for standardized commits with default [Conventional Commits](https://www.conventionalcommits.org) support
- Intelligent [version bumping](https://commitizen-tools.github.io/commitizen/commands/bump/) using [Semantic Versioning](https://semver.org/)
- Automatic [keep a changelog](https://keepachangelog.com/) generation
- Built-in commit validation with pre-commit hooks
- [Customizable](https://commitizen-tools.github.io/commitizen/customization/config_file/) commit rules and templates
- Multi-format version file support
- Custom rules and plugins via pip

## Getting Started[¶](#getting-started)

### Requirements[¶](#requirements)

Before installing Commitizen, ensure you have:

- [Python](https://www.python.org/downloads/)`3.10+`
- [Git](https://git-scm.com/downloads)`1.8.5.2+`

### Installation[¶](#installation)

#### Global Installation (Recommended)[¶](#global-installation-recommended)

The recommended way to install Commitizen is using [pipx](https://pipx.pypa.io/) or [uv](https://docs.astral.sh/uv/), which ensures a clean, isolated installation:

Using pipx:

```
# Install Commitizen
pipx install commitizen

# Keep it updated
pipx upgrade commitizen
```

Using uv:

```
# Install commitizen
uv tool install commitizen

# Keep it updated
uv tool upgrade commitizen
```

(For macOS users) Using Homebrew:

```
brew install commitizen
```

#### Project-Specific Installation[¶](#project-specific-installation)

You can add Commitizen to your Python project using any of these package managers:

Using pip:

```
pip install -U commitizen
```

Using conda:

```
conda install -c conda-forge commitizen
```

Using Poetry:

```
# For Poetry >= 1.2.0
poetry add commitizen --group dev

# For Poetry < 1.2.0
poetry add commitizen --dev
```

Using uv:

```
uv add --dev commitizen
```

Using pdm:

```
pdm add -d commitizen
```

### Basic Commands[¶](#basic-commands)

#### Initialize Commitizen[¶](#initialize-commitizen)

To get started, you'll need to set up your configuration. You have two options:

1. 

Use the interactive setup: 

```
cz init
```

2. 

Manually create a configuration file (`.cz.toml` or `cz.toml`): 

```
[tool.commitizen]
version = "0.1.0"
update_changelog_on_bump = true
```

#### Create Commits[¶](#create-commits)

Create standardized commits using: 

```
cz commit
# or use the shortcut
cz c
```

To sign off your commits: 

```
cz commit -- --signoff
# or use the shortcut
cz commit -- -s
```

For more commit options, run `cz commit --help`.

#### Version Management[¶](#version-management)

The most common command you'll use is: 

```
cz bump
```

This command:

- Bumps your project's version
- Creates a git tag
- Updates the changelog (if `update_changelog_on_bump` is enabled)
- Updates version files

You can customize:

- [Version files](https://commitizen-tools.github.io/commitizen/commands/bump/#version_files)
- [Version scheme](https://commitizen-tools.github.io/commitizen/commands/bump/#version_scheme)
- [Version provider](https://commitizen-tools.github.io/commitizen/config/version_provider/)

For all available options, see the [bump command documentation](https://commitizen-tools.github.io/commitizen/commands/bump/).

### Advanced Usage[¶](#advanced-usage)

#### Get Project Version[¶](#get-project-version)

```
# Get your project's version (instead of Commitizen's version)
cz version -p
# Preview changelog changes
cz changelog --dry-run "$(cz version -p)"
```

This command is particularly useful for automation scripts and CI/CD pipelines.

For example, you can use the output of the command `cz changelog --dry-run "$(cz version -p)"` to notify your team about a new release in Slack.

#### Pre-commit Integration[¶](#pre-commit-integration)

Commitizen can automatically validate your commit messages using pre-commit hooks.

1. 

Add to your `.pre-commit-config.yaml`: 

```
---
repos:
  - repo: https://github.com/commitizen-tools/commitizen
    rev: master  # Replace with latest tag
    hooks:
      - id: commitizen
      - id: commitizen-branch
        stages: [pre-push]
```

2. 

Install the hooks: 

```
pre-commit install --hook-type commit-msg --hook-type pre-push
```

HookRecommended Stagecommitizencommit-msgcommitizen-branchpre-push

Note: Replace `master` with the [latest tag](https://github.com/commitizen-tools/commitizen/tags) to avoid warnings. You can automatically update this with: 

```
pre-commit autoupdate
```

For more details about commit validation, see the [check command documentation](https://commitizen-tools.github.io/commitizen/commands/check/).

## Help & Reference[¶](#help-reference)

### Command Line Interface[¶](#command-line-interface)

Commitizen provides a comprehensive CLI with various commands. Here's the complete reference:

### Quick Reference[¶](#quick-reference)

CommandDescriptionAlias`cz init`Initialize Commitizen configuration-`cz commit`Create a new commit`cz c``cz bump`Bump version and update changelog-`cz changelog`Generate changelog`cz ch``cz check`Validate commit messages-`cz version`Show version information-

### Additional Resources[¶](#additional-resources)

- [Conventional Commits Specification](https://www.conventionalcommits.org)
- [Exit Codes Reference](https://commitizen-tools.github.io/commitizen/exit_codes/)
- [Configuration Guide](https://commitizen-tools.github.io/commitizen/config/configuration_file/)
- [Command Documentation](https://commitizen-tools.github.io/commitizen/commands/init/)

### Getting Help[¶](#getting-help)

For each command, you can get detailed help by adding `--help`:

```
cz commit --help
cz bump --help
cz changelog --help
```

For more details, visit our [documentation site](https://commitizen-tools.github.io/commitizen/).

## Setting up bash completion[¶](#setting-up-bash-completion)

Commitizen supports command-line completion through [argcomplete](https://kislyuk.github.io/argcomplete/), which is automatically installed as a dependency. This feature provides intelligent auto-completion for all Commitizen commands and options.

### Supported Shells[¶](#supported-shells)

- Bash: Full support
- Zsh: Limited support
- Fish: Limited support
- Tcsh: Limited support

### Installation Methods[¶](#installation-methods)

#### Global Installation (Recommended)[¶](#global-installation-recommended_1)

If you installed Commitizen globally (e.g., using `pipx` or `brew`), you can enable global completion:

```
# Enable global completion for all Python applications
sudo activate-global-python-argcomplete
```

#### User-Specific Installation[¶](#user-specific-installation)

For a user-specific installation that persists across sessions:

```
# Add to your shell's startup file (e.g., ~/.bashrc, ~/.zshrc)
register-python-argcomplete cz >> ~/.bashrc
```

#### Temporary Installation[¶](#temporary-installation)

For one-time activation in your current shell session:

```
# Activate completion for current session only
eval "$(register-python-argcomplete cz)"
```

### Verification[¶](#verification)

After installation, you can verify the completion is working by:

1. Opening a new terminal session
2. Typing `cz` followed by a space and pressing `TAB` twice
3. You should see a list of available commands

For more detailed information about argcomplete configuration and troubleshooting, visit the [argcomplete documentation](https://kislyuk.github.io/argcomplete/).

## Sponsors[¶](#sponsors)

These are our cool sponsors!

https://github.com/numberly

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
