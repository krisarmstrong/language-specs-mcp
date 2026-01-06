Git - git Documentation/

- [About](/about)

  - [Trademark](/about/trademark)

- [Learn](/learn)

  - [Book](/book)
  - [Cheat Sheet](/cheat-sheet)
  - [Videos](/videos)
  - [External Links](/doc/ext)

- [Tools](/tools)

  - [Command Line](/tools/command-line)
  - [GUIs](/tools/guis)
  - [Hosting](/tools/hosting)

- [Reference](/docs)
- [Install](/install)
- [Community](/community)

-  Table of Contents 

  - [NAME](#_name)
  - [SYNOPSIS](#_synopsis)
  - [DESCRIPTION](#_description)
  - [OPTIONS](#_options)
  - [GIT COMMANDS](#_git_commands)
  - [High-level commands (porcelain)](#_high_level_commands_porcelain)
  - [Low-level commands (plumbing)](#_low_level_commands_plumbing)
  - [Guides](#_guides)
  - [Repository, command and file interfaces](#_repository_command_and_file_interfaces)
  - [File formats, protocols and other developer interfaces](#_file_formats_protocols_and_other_developer_interfaces)
  - [Configuration Mechanism](#_configuration_mechanism)
  - [Identifier Terminology](#_identifier_terminology)
  - [Symbolic Identifiers](#_symbolic_identifiers)
  - [File/Directory Structure](#_filedirectory_structure)
  - [Terminology](#_terminology)
  - [Environment Variables](#_environment_variables)
  - [Discussion](#_discussion)
  - [SECURITY](#_security)
  - [FURTHER DOCUMENTATION](#_further_documentation)
  - [Authors](#_authors)
  - [Reporting Bugs](#_reporting_bugs)
  - [SEE ALSO](#_see_also)
  - [GIT](#_git)

[English ▾](#)Localized versions of git manual

1. [English](/docs/git)
2. [Deutsch](/docs/git/de)
3. [Español](/docs/git/es)
4. [Français](/docs/git/fr)
5. [Português (Brasil)](/docs/git/pt_BR)
6. [українська мова](/docs/git/uk)
7. [简体中文](/docs/git/zh_HANS-CN)

 Want to read in your language or fix typos?
[You can help translate this page](https://github.com/jnavila/git-manpages-l10n). [Topics ▾](#)

### Setup and Config

- [git](/docs/git)
- [config](/docs/git-config)
- [help](/docs/git-help)
- [bugreport](/docs/git-bugreport)
- [Credential helpers](/doc/credential-helpers)

### Getting and Creating Projects

- [init](/docs/git-init)
- [clone](/docs/git-clone)

### Basic Snapshotting

- [add](/docs/git-add)
- [status](/docs/git-status)
- [diff](/docs/git-diff)
- [commit](/docs/git-commit)
- [notes](/docs/git-notes)
- [restore](/docs/git-restore)
- [reset](/docs/git-reset)
- [rm](/docs/git-rm)
- [mv](/docs/git-mv)

### Branching and Merging

- [branch](/docs/git-branch)
- [checkout](/docs/git-checkout)
- [switch](/docs/git-switch)
- [merge](/docs/git-merge)
- [mergetool](/docs/git-mergetool)
- [log](/docs/git-log)
- [stash](/docs/git-stash)
- [tag](/docs/git-tag)
- [worktree](/docs/git-worktree)

### Sharing and Updating Projects

- [fetch](/docs/git-fetch)
- [pull](/docs/git-pull)
- [push](/docs/git-push)
- [remote](/docs/git-remote)
- [submodule](/docs/git-submodule)

### Inspection and Comparison

- [show](/docs/git-show)
- [log](/docs/git-log)
- [diff](/docs/git-diff)
- [difftool](/docs/git-difftool)
- [range-diff](/docs/git-range-diff)
- [shortlog](/docs/git-shortlog)
- [describe](/docs/git-describe)

### Patching

- [apply](/docs/git-apply)
- [cherry-pick](/docs/git-cherry-pick)
- [diff](/docs/git-diff)
- [rebase](/docs/git-rebase)
- [revert](/docs/git-revert)

### Debugging

- [bisect](/docs/git-bisect)
- [blame](/docs/git-blame)
- [grep](/docs/git-grep)

### Email

- [am](/docs/git-am)
- [apply](/docs/git-apply)
- [imap-send](/docs/git-imap-send)
- [format-patch](/docs/git-format-patch)
- [send-email](/docs/git-send-email)
- [request-pull](/docs/git-request-pull)

### External Systems

- [svn](/docs/git-svn)
- [fast-import](/docs/git-fast-import)

### Server Admin

- [daemon](/docs/git-daemon)
- [update-server-info](/docs/git-update-server-info)

### Guides

- [gitattributes](/docs/gitattributes)
- [Command-line interface conventions](/docs/gitcli)
- [Everyday Git](/docs/giteveryday)
- [Frequently Asked Questions (FAQ)](/docs/gitfaq)
- [Glossary](/docs/gitglossary)
- [Hooks](/docs/githooks)
- [gitignore](/docs/gitignore)
- [gitmodules](/docs/gitmodules)
- [Revisions](/docs/gitrevisions)
- [Submodules](/docs/gitsubmodules)
- [Tutorial](/docs/gittutorial)
- [Workflows](/docs/gitworkflows)
- [All guides...](/docs/git#_guides)

### Administration

- [clean](/docs/git-clean)
- [gc](/docs/git-gc)
- [fsck](/docs/git-fsck)
- [reflog](/docs/git-reflog)
- [filter-branch](/docs/git-filter-branch)
- [instaweb](/docs/git-instaweb)
- [archive](/docs/git-archive)
- [bundle](/docs/git-bundle)

### Plumbing Commands

- [cat-file](/docs/git-cat-file)
- [check-ignore](/docs/git-check-ignore)
- [checkout-index](/docs/git-checkout-index)
- [commit-tree](/docs/git-commit-tree)
- [count-objects](/docs/git-count-objects)
- [diff-index](/docs/git-diff-index)
- [for-each-ref](/docs/git-for-each-ref)
- [hash-object](/docs/git-hash-object)
- [ls-files](/docs/git-ls-files)
- [ls-tree](/docs/git-ls-tree)
- [merge-base](/docs/git-merge-base)
- [read-tree](/docs/git-read-tree)
- [rev-list](/docs/git-rev-list)
- [rev-parse](/docs/git-rev-parse)
- [show-ref](/docs/git-show-ref)
- [symbolic-ref](/docs/git-symbolic-ref)
- [update-index](/docs/git-update-index)
- [update-ref](/docs/git-update-ref)
- [verify-pack](/docs/git-verify-pack)
- [write-tree](/docs/git-write-tree)

[Latest version
   ▾](#)git last updated in 2.52.0Changes in the git manual

1. [2.52.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2025-11-17](/docs/git/2.52.0)
2. 2.51.2 no changes
3. [2.51.1
          
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
              
            
          
          2025-10-15](/docs/git/2.51.1)
4. 2.50.1 → 2.51.0 no changes
5. [2.50.0
          
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
          
          2025-06-16](/docs/git/2.50.0)
6. 2.49.1 no changes
7. [2.49.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2025-03-14](/docs/git/2.49.0)
8. 2.48.1 → 2.48.2 no changes
9. [2.48.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2025-01-10](/docs/git/2.48.0)
10. 2.47.1 → 2.47.3 no changes
11. [2.47.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-10-06](/docs/git/2.47.0)
12. 2.46.1 → 2.46.4 no changes
13. [2.46.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-07-29](/docs/git/2.46.0)
14. 2.45.2 → 2.45.4 no changes
15. [2.45.1
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-04-29](/docs/git/2.45.1)
16. [2.45.0
          
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2024-04-29](/docs/git/2.45.0)
17. 2.44.2 → 2.44.4 no changes
18. [2.44.1
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-04-19](/docs/git/2.44.1)
19. [2.44.0
          
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2024-02-23](/docs/git/2.44.0)
20. 2.43.5 → 2.43.7 no changes
21. [2.43.4
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-04-19](/docs/git/2.43.4)
22. 2.43.2 → 2.43.3 no changes
23. [2.43.1
          
            
              
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2024-02-09](/docs/git/2.43.1)
24. [2.43.0
          
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2023-11-20](/docs/git/2.43.0)
25. 2.42.3 → 2.42.4 no changes
26. [2.42.2
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-04-19](/docs/git/2.42.2)
27. [2.42.1
          
            
              
            
            
              
            
            
              
            
              
            
              
            
              
            
              
            
              
            
          
          2023-11-02](/docs/git/2.42.1)
28. [2.42.0
          
            
              
            
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2023-08-21](/docs/git/2.42.0)
29. 2.41.2 → 2.41.3 no changes
30. [2.41.1
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-04-19](/docs/git/2.41.1)
31. [2.41.0
          
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2023-06-01](/docs/git/2.41.0)
32. 2.40.3 → 2.40.4 no changes
33. [2.40.2
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-04-19](/docs/git/2.40.2)
34. 2.40.1 no changes
35. 2.40.0 no changes
36. 2.39.5 no changes
37. [2.39.4
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2024-04-19](/docs/git/2.39.4)
38. 2.39.1 → 2.39.3 no changes
39. [2.39.0
          
            
              
            
            
              
            
            
              
            
              
            
              
            
              
            
              
            
              
            
          
          2022-12-12](/docs/git/2.39.0)
40. 2.38.3 → 2.38.5 no changes
41. [2.38.2
          
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
              
            
            
              
            
              
            
          
          2022-12-11](/docs/git/2.38.2)
42. 2.38.1 no changes
43. [2.38.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2022-10-02](/docs/git/2.38.0)
44. 2.37.3 → 2.37.7 no changes
45. [2.37.2
          
            
              
            
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
          
          2022-08-11](/docs/git/2.37.2)
46. 2.37.1 no changes
47. [2.37.0
          
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
              
            
              
            
          
          2022-06-27](/docs/git/2.37.0)
48. 2.36.1 → 2.36.6 no changes
49. [2.36.0
          
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
              
            
          
          2022-04-18](/docs/git/2.36.0)
50. 2.35.1 → 2.35.8 no changes
51. [2.35.0
          
            
              
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2022-01-24](/docs/git/2.35.0)
52. 2.34.1 → 2.34.8 no changes
53. [2.34.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2021-11-15](/docs/git/2.34.0)
54. 2.33.3 → 2.33.8 no changes
55. [2.33.2
          
            
              
            
            
              
            
            
              
            
              
            
              
            
              
            
              
            
              
            
          
          2022-03-23](/docs/git/2.33.2)
56. [2.33.1
          
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
              
            
              
            
          
          2021-10-12](/docs/git/2.33.1)
57. 2.32.1 → 2.33.0 no changes
58. [2.32.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2021-06-06](/docs/git/2.32.0)
59. 2.31.1 → 2.31.8 no changes
60. [2.31.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2021-03-15](/docs/git/2.31.0)
61. 2.30.1 → 2.30.9 no changes
62. [2.30.0
          
            
              
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2020-12-27](/docs/git/2.30.0)
63. 2.29.1 → 2.29.3 no changes
64. [2.29.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2020-10-19](/docs/git/2.29.0)
65. 2.28.1 no changes
66. [2.28.0
          
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2020-07-27](/docs/git/2.28.0)
67. 2.27.1 no changes
68. [2.27.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2020-06-01](/docs/git/2.27.0)
69. 2.26.1 → 2.26.3 no changes
70. [2.26.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2020-03-22](/docs/git/2.26.0)
71. 2.25.2 → 2.25.5 no changes
72. [2.25.1
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2020-02-17](/docs/git/2.25.1)
73. [2.25.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2020-01-13](/docs/git/2.25.0)
74. 2.23.1 → 2.24.4 no changes
75. [2.23.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2019-08-16](/docs/git/2.23.0)
76. 2.22.2 → 2.22.5 no changes
77. [2.22.1
          
            
              
            
              
            
            
              
            
            
              
            
              
            
              
            
              
            
              
            
          
          2019-08-11](/docs/git/2.22.1)
78. [2.22.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2019-06-07](/docs/git/2.22.0)
79. 2.20.1 → 2.21.4 no changes
80. [2.20.0
          
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
              
            
          
          2018-12-09](/docs/git/2.20.0)
81. 2.19.3 → 2.19.6 no changes
82. [2.19.2
          
            
              
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2018-11-21](/docs/git/2.19.2)
83. 2.19.1 no changes
84. [2.19.0
          
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
          
          2018-09-10](/docs/git/2.19.0)
85. 2.18.1 → 2.18.5 no changes
86. [2.18.0
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
              
            
          
          2018-06-21](/docs/git/2.18.0)
87. 2.17.1 → 2.17.6 no changes
88. [2.17.0
          
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
              
            
              
            
              
            
          
          2018-04-02](/docs/git/2.17.0)
89. [2.16.6
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2019-12-06](/docs/git/2.16.6)
90. [2.15.4
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2019-12-06](/docs/git/2.15.4)
91. [2.14.6
          
            
              
            
              
            
            
              
            
            
              
            
              
            
              
            
              
            
              
            
          
          2019-12-06](/docs/git/2.14.6)
92. 2.13.7 no changes
93. [2.12.5
          
            
              
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2017-09-22](/docs/git/2.12.5)
94. [2.11.4
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2017-09-22](/docs/git/2.11.4)
95. [2.10.5
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2017-09-22](/docs/git/2.10.5)
96. [2.9.5
          
            
              
            
              
            
              
            
              
            
            
              
            
              
            
              
            
              
            
            
              
            
              
            
          
          2017-07-30](/docs/git/2.9.5)
97. [2.8.6
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2017-07-30](/docs/git/2.8.6)
98. [2.7.6
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2017-07-30](/docs/git/2.7.6)
99. [2.6.7
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2017-05-05](/docs/git/2.6.7)
100. [2.5.6
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2017-05-05](/docs/git/2.5.6)
101. [2.4.12
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2017-05-05](/docs/git/2.4.12)
102. [2.3.10
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2015-09-28](/docs/git/2.3.10)
103. [2.2.3
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
            
              
            
              
            
          
          2015-09-04](/docs/git/2.2.3)
104. [2.1.4
          
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2014-12-17](/docs/git/2.1.4)
105. [2.0.5
          
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
              
            
            
              
            
              
            
            
              
            
              
            
          
          2014-12-17](/docs/git/2.0.5)
106. 

Check your version of git by running

`git --version`

## #_nameNAME

git - the stupid content tracker

## #_synopsisSYNOPSIS

```
git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
    [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
    [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--no-lazy-fetch]
    [--no-optional-locks] [--no-advice] [--bare] [--git-dir=<path>]
    [--work-tree=<path>] [--namespace=<name>] [--config-env=<name>=<envvar>]
    <command> [<args>]
```

## #_descriptionDESCRIPTION

Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.

See [gittutorial[7]](/docs/gittutorial) to get started, then see [giteveryday[7]](/docs/giteveryday) for a useful minimum set of commands. The [Git User’s Manual](/docs/user-manual) has a more in-depth introduction.

After you mastered the basic concepts, you can come back to this page to learn what commands Git offers. You can learn more about individual Git commands with "git help command". [gitcli[7]](/docs/gitcli) manual page gives you an overview of the command-line command syntax.

A formatted and hyperlinked copy of the latest Git documentation can be viewed at [https://git.github.io/htmldocs/git.html](https://git.github.io/htmldocs/git.html) or [https://git-scm.com/docs](https://git-scm.com/docs).

## #_optionsOPTIONS

#Documentation/git.txt--v-v #Documentation/git.txt---version--version 

Prints the Git suite version that the git program came from.

This option is internally converted to `git``version` ... and accepts the same options as the [git-version[1]](/docs/git-version) command. If `--help` is also given, it takes precedence over `--version`.

#Documentation/git.txt--h-h #Documentation/git.txt---help--help 

Prints the synopsis and a list of the most commonly used commands. If the option `--all` or `-a` is given then all available commands are printed. If a Git command is named this option will bring up the manual page for that command.

Other options are available to control how the manual page is displayed. See [git-help[1]](/docs/git-help) for more information, because `git``--help` ... is converted internally into `git``help` ....

#Documentation/git.txt--Cpath-C <path> 

Run as if git was started in <path> instead of the current working directory. When multiple `-C` options are given, each subsequent non-absolute `-C`<path> is interpreted relative to the preceding `-C`<path>. If <path> is present but empty, e.g. `-C``""`, then the current working directory is left unchanged.

This option affects options that expect path name like `--git-dir` and `--work-tree` in that their interpretations of the path names would be made relative to the working directory caused by the `-C` option. For example the following invocations are equivalent:

```
git --git-dir=a.git --work-tree=b -C c status
git --git-dir=c/a.git --work-tree=c/b status
```

#Documentation/git.txt--cnamevalue-c <name>=<value> 

Pass a configuration parameter to the command. The value given will override values from configuration files. The <name> is expected in the same format as listed by git config (subkeys separated by dots).

Note that omitting the `=` in `git``-c``foo.bar` ... is allowed and sets `foo.bar` to the boolean true value (just like [`foo`]`bar` would in a config file). Including the equals but with an empty value (like `git``-c``foo.bar=` ...) sets `foo.bar` to the empty string which `git``config``--type=bool` will convert to `false`.

#Documentation/git.txt---config-envnameenvvar--config-env=<name>=<envvar> 

Like `-c`<name>`=`<value>, give configuration variable <name> a value, where <envvar> is the name of an environment variable from which to retrieve the value. Unlike `-c` there is no shortcut for directly setting the value to an empty string, instead the environment variable itself must be set to the empty string. It is an error if the <envvar> does not exist in the environment. <envvar> may not contain an equals sign to avoid ambiguity with <name> containing one.

This is useful for cases where you want to pass transitory configuration options to git, but are doing so on operating systems where other processes might be able to read your command line (e.g. `/proc/self/cmdline`), but not your environment (e.g. `/proc/self/environ`). That behavior is the default on Linux, but may not be on your system.

Note that this might add security for variables such as `http.extraHeader` where the sensitive information is part of the value, but not e.g. `url.`<base>`.insteadOf` where the sensitive information can be part of the key.

#Documentation/git.txt---exec-pathpath--exec-path[=<path>] 

Path to wherever your core Git programs are installed. This can also be controlled by setting the GIT_EXEC_PATH environment variable. If no path is given, git will print the current setting and then exit.

#Documentation/git.txt---html-path--html-path 

Print the path, without trailing slash, where Git’s HTML documentation is installed and exit.

#Documentation/git.txt---man-path--man-path 

Print the manpath (see `man`(`1`)) for the man pages for this version of Git and exit.

#Documentation/git.txt---info-path--info-path 

Print the path where the Info files documenting this version of Git are installed and exit.

#Documentation/git.txt--p-p #Documentation/git.txt---paginate--paginate 

Pipe all output into less (or if set, $PAGER) if standard output is a terminal. This overrides the `pager.`<cmd> configuration options (see the "Configuration Mechanism" section below).

#Documentation/git.txt--P-P #Documentation/git.txt---no-pager--no-pager 

Do not pipe Git output into a pager.

#Documentation/git.txt---git-dirpath--git-dir=<path> 

Set the path to the repository (".git" directory). This can also be controlled by setting the `GIT_DIR` environment variable. It can be an absolute path or relative path to current working directory.

Specifying the location of the ".git" directory using this option (or `GIT_DIR` environment variable) turns off the repository discovery that tries to find a directory with ".git" subdirectory (which is how the repository and the top-level of the working tree are discovered), and tells Git that you are at the top level of the working tree. If you are not at the top-level directory of the working tree, you should tell Git where the top-level of the working tree is, with the `--work-tree=`<path> option (or `GIT_WORK_TREE` environment variable)

If you just want to run git as if it was started in <path> then use `git``-C`<path>.

#Documentation/git.txt---work-treepath--work-tree=<path> 

Set the path to the working tree. It can be an absolute path or a path relative to the current working directory. This can also be controlled by setting the GIT_WORK_TREE environment variable and the core.worktree configuration variable (see core.worktree in [git-config[1]](/docs/git-config) for a more detailed discussion).

#Documentation/git.txt---namespacepath--namespace=<path> 

Set the Git namespace. See [gitnamespaces[7]](/docs/gitnamespaces) for more details. Equivalent to setting the `GIT_NAMESPACE` environment variable.

#Documentation/git.txt---bare--bare 

Treat the repository as a bare repository. If GIT_DIR environment is not set, it is set to the current working directory.

#Documentation/git.txt---no-replace-objects--no-replace-objects 

Do not use replacement refs to replace Git objects. This is equivalent to exporting the `GIT_NO_REPLACE_OBJECTS` environment variable with any value. See [git-replace[1]](/docs/git-replace) for more information.

#Documentation/git.txt---no-lazy-fetch--no-lazy-fetch 

Do not fetch missing objects from the promisor remote on demand. Useful together with `git``cat-file``-e`<object> to see if the object is locally available. This is equivalent to setting the `GIT_NO_LAZY_FETCH` environment variable to `1`.

#Documentation/git.txt---no-optional-locks--no-optional-locks 

Do not perform optional operations that require locks. This is equivalent to setting the `GIT_OPTIONAL_LOCKS` to `0`.

#Documentation/git.txt---no-advice--no-advice 

Disable all advice hints from being printed.

#Documentation/git.txt---literal-pathspecs--literal-pathspecs 

Treat pathspecs literally (i.e. no globbing, no pathspec magic). This is equivalent to setting the `GIT_LITERAL_PATHSPECS` environment variable to `1`.

#Documentation/git.txt---glob-pathspecs--glob-pathspecs 

Add "glob" magic to all pathspec. This is equivalent to setting the `GIT_GLOB_PATHSPECS` environment variable to `1`. Disabling globbing on individual pathspecs can be done using pathspec magic ":(literal)"

#Documentation/git.txt---noglob-pathspecs--noglob-pathspecs 

Add "literal" magic to all pathspec. This is equivalent to setting the `GIT_NOGLOB_PATHSPECS` environment variable to `1`. Enabling globbing on individual pathspecs can be done using pathspec magic ":(glob)"

#Documentation/git.txt---icase-pathspecs--icase-pathspecs 

Add "icase" magic to all pathspec. This is equivalent to setting the `GIT_ICASE_PATHSPECS` environment variable to `1`.

#Documentation/git.txt---list-cmdsgroupgroup--list-cmds=<group>[,<group>…​] 

List commands by group. This is an internal/experimental option and may change or be removed in the future. Supported groups are: builtins, parseopt (builtin commands that use parse-options), deprecated (deprecated builtins), main (all commands in libexec directory), others (all other commands in `$PATH` that have git- prefix), list-<category> (see categories in command-list.txt), nohelpers (exclude helper commands), alias and config (retrieve command list from config variable completion.commands)

#Documentation/git.txt---attr-sourcetree-ish--attr-source=<tree-ish>

Read gitattributes from <tree-ish> instead of the worktree. See [gitattributes[5]](/docs/gitattributes). This is equivalent to setting the `GIT_ATTR_SOURCE` environment variable.

## #_git_commandsGIT COMMANDS

We divide Git into high level ("porcelain") commands and low level ("plumbing") commands.

## #_high_level_commands_porcelainHigh-level commands (porcelain)

We separate the porcelain commands into the main commands and some ancillary user utilities.

### #_main_porcelain_commandsMain porcelain commands

#Documentation/git.txt-git-add1[git-add[1]](/docs/git-add)

Add file contents to the index

#Documentation/git.txt-git-am1[git-am[1]](/docs/git-am)

Apply a series of patches from a mailbox

#Documentation/git.txt-git-archive1[git-archive[1]](/docs/git-archive)

Create an archive of files from a named tree

#Documentation/git.txt-git-backfill1[git-backfill[1]](/docs/git-backfill)

Download missing objects in a partial clone

#Documentation/git.txt-git-bisect1[git-bisect[1]](/docs/git-bisect)

Use binary search to find the commit that introduced a bug

#Documentation/git.txt-git-branch1[git-branch[1]](/docs/git-branch)

List, create, or delete branches

#Documentation/git.txt-git-bundle1[git-bundle[1]](/docs/git-bundle)

Move objects and refs by archive

#Documentation/git.txt-git-checkout1[git-checkout[1]](/docs/git-checkout)

Switch branches or restore working tree files

#Documentation/git.txt-git-cherry-pick1[git-cherry-pick[1]](/docs/git-cherry-pick)

Apply the changes introduced by some existing commits

#Documentation/git.txt-git-citool1[git-citool[1]](/docs/git-citool)

Graphical alternative to git-commit

#Documentation/git.txt-git-clean1[git-clean[1]](/docs/git-clean)

Remove untracked files from the working tree

#Documentation/git.txt-git-clone1[git-clone[1]](/docs/git-clone)

Clone a repository into a new directory

#Documentation/git.txt-git-commit1[git-commit[1]](/docs/git-commit)

Record changes to the repository

#Documentation/git.txt-git-describe1[git-describe[1]](/docs/git-describe)

Give an object a human readable name based on an available ref

#Documentation/git.txt-git-diff1[git-diff[1]](/docs/git-diff)

Show changes between commits, commit and working tree, etc

#Documentation/git.txt-git-fetch1[git-fetch[1]](/docs/git-fetch)

Download objects and refs from another repository

#Documentation/git.txt-git-format-patch1[git-format-patch[1]](/docs/git-format-patch)

Prepare patches for e-mail submission

#Documentation/git.txt-git-gc1[git-gc[1]](/docs/git-gc)

Cleanup unnecessary files and optimize the local repository

#Documentation/git.txt-git-grep1[git-grep[1]](/docs/git-grep)

Print lines matching a pattern

#Documentation/git.txt-git-gui1[git-gui[1]](/docs/git-gui)

A portable graphical interface to Git

#Documentation/git.txt-git-init1[git-init[1]](/docs/git-init)

Create an empty Git repository or reinitialize an existing one

#Documentation/git.txt-git-log1[git-log[1]](/docs/git-log)

Show commit logs

#Documentation/git.txt-git-maintenance1[git-maintenance[1]](/docs/git-maintenance)

Run tasks to optimize Git repository data

#Documentation/git.txt-git-merge1[git-merge[1]](/docs/git-merge)

Join two or more development histories together

#Documentation/git.txt-git-mv1[git-mv[1]](/docs/git-mv)

Move or rename a file, a directory, or a symlink

#Documentation/git.txt-git-notes1[git-notes[1]](/docs/git-notes)

Add or inspect object notes

#Documentation/git.txt-git-pull1[git-pull[1]](/docs/git-pull)

Fetch from and integrate with another repository or a local branch

#Documentation/git.txt-git-push1[git-push[1]](/docs/git-push)

Update remote refs along with associated objects

#Documentation/git.txt-git-range-diff1[git-range-diff[1]](/docs/git-range-diff)

Compare two commit ranges (e.g. two versions of a branch)

#Documentation/git.txt-git-rebase1[git-rebase[1]](/docs/git-rebase)

Reapply commits on top of another base tip

#Documentation/git.txt-git-reset1[git-reset[1]](/docs/git-reset)

Reset current HEAD to the specified state

#Documentation/git.txt-git-restore1[git-restore[1]](/docs/git-restore)

Restore working tree files

#Documentation/git.txt-git-revert1[git-revert[1]](/docs/git-revert)

Revert some existing commits

#Documentation/git.txt-git-rm1[git-rm[1]](/docs/git-rm)

Remove files from the working tree and from the index

#Documentation/git.txt-git-shortlog1[git-shortlog[1]](/docs/git-shortlog)

Summarize git log output

#Documentation/git.txt-git-show1[git-show[1]](/docs/git-show)

Show various types of objects

#Documentation/git.txt-git-sparse-checkout1[git-sparse-checkout[1]](/docs/git-sparse-checkout)

Reduce your working tree to a subset of tracked files

#Documentation/git.txt-git-stash1[git-stash[1]](/docs/git-stash)

Stash the changes in a dirty working directory away

#Documentation/git.txt-git-status1[git-status[1]](/docs/git-status)

Show the working tree status

#Documentation/git.txt-git-submodule1[git-submodule[1]](/docs/git-submodule)

Initialize, update or inspect submodules

#Documentation/git.txt-git-switch1[git-switch[1]](/docs/git-switch)

Switch branches

#Documentation/git.txt-git-tag1[git-tag[1]](/docs/git-tag)

Create, list, delete or verify tags

#Documentation/git.txt-git-worktree1[git-worktree[1]](/docs/git-worktree)

Manage multiple working trees

#Documentation/git.txt-gitk1[gitk[1]](/docs/gitk)

The Git repository browser

#Documentation/git.txt-scalar1[scalar[1]](/docs/scalar)

A tool for managing large Git repositories

### #_ancillary_commandsAncillary Commands

Manipulators:

#Documentation/git.txt-git-config1[git-config[1]](/docs/git-config)

Get and set repository or global options

#Documentation/git.txt-git-fast-export1[git-fast-export[1]](/docs/git-fast-export)

Git data exporter

#Documentation/git.txt-git-fast-import1[git-fast-import[1]](/docs/git-fast-import)

Backend for fast Git data importers

#Documentation/git.txt-git-filter-branch1[git-filter-branch[1]](/docs/git-filter-branch)

Rewrite branches

#Documentation/git.txt-git-mergetool1[git-mergetool[1]](/docs/git-mergetool)

Run merge conflict resolution tools to resolve merge conflicts

#Documentation/git.txt-git-pack-refs1[git-pack-refs[1]](/docs/git-pack-refs)

Pack heads and tags for efficient repository access

#Documentation/git.txt-git-prune1[git-prune[1]](/docs/git-prune)

Prune all unreachable objects from the object database

#Documentation/git.txt-git-reflog1[git-reflog[1]](/docs/git-reflog)

Manage reflog information

#Documentation/git.txt-git-refs1[git-refs[1]](/docs/git-refs)

Low-level access to refs

#Documentation/git.txt-git-remote1[git-remote[1]](/docs/git-remote)

Manage set of tracked repositories

#Documentation/git.txt-git-repack1[git-repack[1]](/docs/git-repack)

Pack unpacked objects in a repository

#Documentation/git.txt-git-replace1[git-replace[1]](/docs/git-replace)

Create, list, delete refs to replace objects

Interrogators:

#Documentation/git.txt-git-annotate1[git-annotate[1]](/docs/git-annotate)

Annotate file lines with commit information

#Documentation/git.txt-git-blame1[git-blame[1]](/docs/git-blame)

Show what revision and author last modified each line of a file

#Documentation/git.txt-git-bugreport1[git-bugreport[1]](/docs/git-bugreport)

Collect information for user to file a bug report

#Documentation/git.txt-git-count-objects1[git-count-objects[1]](/docs/git-count-objects)

Count unpacked number of objects and their disk consumption

#Documentation/git.txt-git-diagnose1[git-diagnose[1]](/docs/git-diagnose)

Generate a zip archive of diagnostic information

#Documentation/git.txt-git-difftool1[git-difftool[1]](/docs/git-difftool)

Show changes using common diff tools

#Documentation/git.txt-git-fsck1[git-fsck[1]](/docs/git-fsck)

Verifies the connectivity and validity of the objects in the database

#Documentation/git.txt-git-help1[git-help[1]](/docs/git-help)

Display help information about Git

#Documentation/git.txt-git-instaweb1[git-instaweb[1]](/docs/git-instaweb)

Instantly browse your working repository in gitweb

#Documentation/git.txt-git-merge-tree1[git-merge-tree[1]](/docs/git-merge-tree)

Perform merge without touching index or working tree

#Documentation/git.txt-git-rerere1[git-rerere[1]](/docs/git-rerere)

Reuse recorded resolution of conflicted merges

#Documentation/git.txt-git-show-branch1[git-show-branch[1]](/docs/git-show-branch)

Show branches and their commits

#Documentation/git.txt-git-verify-commit1[git-verify-commit[1]](/docs/git-verify-commit)

Check the GPG signature of commits

#Documentation/git.txt-git-verify-tag1[git-verify-tag[1]](/docs/git-verify-tag)

Check the GPG signature of tags

#Documentation/git.txt-git-version1[git-version[1]](/docs/git-version)

Display version information about Git

#Documentation/git.txt-git-whatchanged1[git-whatchanged[1]](/docs/git-whatchanged)

Show logs with differences each commit introduces

#Documentation/git.txt-gitweb1[gitweb[1]](/docs/gitweb)

Git web interface (web frontend to Git repositories)

### #_interacting_with_othersInteracting with Others

These commands are to interact with foreign SCM and with other people via patch over e-mail.

#Documentation/git.txt-git-archimport1[git-archimport[1]](/docs/git-archimport)

Import a GNU Arch repository into Git

#Documentation/git.txt-git-cvsexportcommit1[git-cvsexportcommit[1]](/docs/git-cvsexportcommit)

Export a single commit to a CVS checkout

#Documentation/git.txt-git-cvsimport1[git-cvsimport[1]](/docs/git-cvsimport)

Salvage your data out of another SCM people love to hate

#Documentation/git.txt-git-cvsserver1[git-cvsserver[1]](/docs/git-cvsserver)

A CVS server emulator for Git

#Documentation/git.txt-git-imap-send1[git-imap-send[1]](/docs/git-imap-send)

Send a collection of patches from stdin to an IMAP folder

#Documentation/git.txt-git-p41[git-p4[1]](/docs/git-p4)

Import from and submit to Perforce repositories

#Documentation/git.txt-git-quiltimport1[git-quiltimport[1]](/docs/git-quiltimport)

Applies a quilt patchset onto the current branch

#Documentation/git.txt-git-request-pull1[git-request-pull[1]](/docs/git-request-pull)

Generates a summary of pending changes

#Documentation/git.txt-git-send-email1[git-send-email[1]](/docs/git-send-email)

Send a collection of patches as emails

#Documentation/git.txt-git-svn1[git-svn[1]](/docs/git-svn)

Bidirectional operation between a Subversion repository and Git

### #_reset_restore_and_revertReset, restore and revert

There are three commands with similar names: `git``reset`, `git``restore` and `git``revert`.

- 

[git-revert[1]](/docs/git-revert) is about making a new commit that reverts the changes made by other commits.

- 

[git-restore[1]](/docs/git-restore) is about restoring files in the working tree from either the index or another commit. This command does not update your branch. The command can also be used to restore files in the index from another commit.

- 

[git-reset[1]](/docs/git-reset) is about updating your branch, moving the tip in order to add or remove commits from the branch. This operation changes the commit history.

`git``reset` can also be used to restore the index, overlapping with `git``restore`.

## #_low_level_commands_plumbingLow-level commands (plumbing)

Although Git includes its own porcelain layer, its low-level commands are sufficient to support development of alternative porcelains. Developers of such porcelains might start by reading about [git-update-index[1]](/docs/git-update-index) and [git-read-tree[1]](/docs/git-read-tree).

The interface (input, output, set of options and the semantics) to these low-level commands are meant to be a lot more stable than Porcelain level commands, because these commands are primarily for scripted use. The interface to Porcelain commands on the other hand are subject to change in order to improve the end user experience.

The following description divides the low-level commands into commands that manipulate objects (in the repository, index, and working tree), commands that interrogate and compare objects, and commands that move objects and references between repositories.

### #_manipulation_commandsManipulation commands

#Documentation/git.txt-git-apply1[git-apply[1]](/docs/git-apply)

Apply a patch to files and/or to the index

#Documentation/git.txt-git-checkout-index1[git-checkout-index[1]](/docs/git-checkout-index)

Copy files from the index to the working tree

#Documentation/git.txt-git-commit-graph1[git-commit-graph[1]](/docs/git-commit-graph)

Write and verify Git commit-graph files

#Documentation/git.txt-git-commit-tree1[git-commit-tree[1]](/docs/git-commit-tree)

Create a new commit object

#Documentation/git.txt-git-hash-object1[git-hash-object[1]](/docs/git-hash-object)

Compute object ID and optionally create an object from a file

#Documentation/git.txt-git-index-pack1[git-index-pack[1]](/docs/git-index-pack)

Build pack index file for an existing packed archive

#Documentation/git.txt-git-merge-file1[git-merge-file[1]](/docs/git-merge-file)

Run a three-way file merge

#Documentation/git.txt-git-merge-index1[git-merge-index[1]](/docs/git-merge-index)

Run a merge for files needing merging

#Documentation/git.txt-git-mktag1[git-mktag[1]](/docs/git-mktag)

Creates a tag object with extra validation

#Documentation/git.txt-git-mktree1[git-mktree[1]](/docs/git-mktree)

Build a tree-object from ls-tree formatted text

#Documentation/git.txt-git-multi-pack-index1[git-multi-pack-index[1]](/docs/git-multi-pack-index)

Write and verify multi-pack-indexes

#Documentation/git.txt-git-pack-objects1[git-pack-objects[1]](/docs/git-pack-objects)

Create a packed archive of objects

#Documentation/git.txt-git-prune-packed1[git-prune-packed[1]](/docs/git-prune-packed)

Remove extra objects that are already in pack files

#Documentation/git.txt-git-read-tree1[git-read-tree[1]](/docs/git-read-tree)

Reads tree information into the index

#Documentation/git.txt-git-replay1[git-replay[1]](/docs/git-replay)

EXPERIMENTAL: Replay commits on a new base, works with bare repos too

#Documentation/git.txt-git-symbolic-ref1[git-symbolic-ref[1]](/docs/git-symbolic-ref)

Read, modify and delete symbolic refs

#Documentation/git.txt-git-unpack-objects1[git-unpack-objects[1]](/docs/git-unpack-objects)

Unpack objects from a packed archive

#Documentation/git.txt-git-update-index1[git-update-index[1]](/docs/git-update-index)

Register file contents in the working tree to the index

#Documentation/git.txt-git-update-ref1[git-update-ref[1]](/docs/git-update-ref)

Update the object name stored in a ref safely

#Documentation/git.txt-git-write-tree1[git-write-tree[1]](/docs/git-write-tree)

Create a tree object from the current index

### #_interrogation_commandsInterrogation commands

#Documentation/git.txt-git-cat-file1[git-cat-file[1]](/docs/git-cat-file)

Provide contents or details of repository objects

#Documentation/git.txt-git-cherry1[git-cherry[1]](/docs/git-cherry)

Find commits yet to be applied to upstream

#Documentation/git.txt-git-diff-files1[git-diff-files[1]](/docs/git-diff-files)

Compares files in the working tree and the index

#Documentation/git.txt-git-diff-index1[git-diff-index[1]](/docs/git-diff-index)

Compare a tree to the working tree or index

#Documentation/git.txt-git-diff-pairs1[git-diff-pairs[1]](/docs/git-diff-pairs)

Compare the content and mode of provided blob pairs

#Documentation/git.txt-git-diff-tree1[git-diff-tree[1]](/docs/git-diff-tree)

Compares the content and mode of blobs found via two tree objects

#Documentation/git.txt-git-for-each-ref1[git-for-each-ref[1]](/docs/git-for-each-ref)

Output information on each ref

#Documentation/git.txt-git-for-each-repo1[git-for-each-repo[1]](/docs/git-for-each-repo)

Run a Git command on a list of repositories

#Documentation/git.txt-git-get-tar-commit-id1[git-get-tar-commit-id[1]](/docs/git-get-tar-commit-id)

Extract commit ID from an archive created using git-archive

#Documentation/git.txt-git-last-modified1[git-last-modified[1]](/docs/git-last-modified)

EXPERIMENTAL: Show when files were last modified

#Documentation/git.txt-git-ls-files1[git-ls-files[1]](/docs/git-ls-files)

Show information about files in the index and the working tree

#Documentation/git.txt-git-ls-remote1[git-ls-remote[1]](/docs/git-ls-remote)

List references in a remote repository

#Documentation/git.txt-git-ls-tree1[git-ls-tree[1]](/docs/git-ls-tree)

List the contents of a tree object

#Documentation/git.txt-git-merge-base1[git-merge-base[1]](/docs/git-merge-base)

Find as good common ancestors as possible for a merge

#Documentation/git.txt-git-name-rev1[git-name-rev[1]](/docs/git-name-rev)

Find symbolic names for given revs

#Documentation/git.txt-git-pack-redundant1[git-pack-redundant[1]](/docs/git-pack-redundant)

Find redundant pack files

#Documentation/git.txt-git-repo1[git-repo[1]](/docs/git-repo)

Retrieve information about the repository

#Documentation/git.txt-git-rev-list1[git-rev-list[1]](/docs/git-rev-list)

Lists commit objects in reverse chronological order

#Documentation/git.txt-git-rev-parse1[git-rev-parse[1]](/docs/git-rev-parse)

Pick out and massage parameters

#Documentation/git.txt-git-show-index1[git-show-index[1]](/docs/git-show-index)

Show packed archive index

#Documentation/git.txt-git-show-ref1[git-show-ref[1]](/docs/git-show-ref)

List references in a local repository

#Documentation/git.txt-git-unpack-file1[git-unpack-file[1]](/docs/git-unpack-file)

Creates a temporary file with a blob’s contents

#Documentation/git.txt-git-var1[git-var[1]](/docs/git-var)

Show a Git logical variable

#Documentation/git.txt-git-verify-pack1[git-verify-pack[1]](/docs/git-verify-pack)

Validate packed Git archive files

In general, the interrogate commands do not touch the files in the working tree.

### #_syncing_repositoriesSyncing repositories

#Documentation/git.txt-git-daemon1[git-daemon[1]](/docs/git-daemon)

A really simple server for Git repositories

#Documentation/git.txt-git-fetch-pack1[git-fetch-pack[1]](/docs/git-fetch-pack)

Receive missing objects from another repository

#Documentation/git.txt-git-http-backend1[git-http-backend[1]](/docs/git-http-backend)

Server side implementation of Git over HTTP

#Documentation/git.txt-git-send-pack1[git-send-pack[1]](/docs/git-send-pack)

Push objects over Git protocol to another repository

#Documentation/git.txt-git-update-server-info1[git-update-server-info[1]](/docs/git-update-server-info)

Update auxiliary info file to help dumb servers

The following are helper commands used by the above; end users typically do not use them directly.

#Documentation/git.txt-git-http-fetch1[git-http-fetch[1]](/docs/git-http-fetch)

Download from a remote Git repository via HTTP

#Documentation/git.txt-git-http-push1[git-http-push[1]](/docs/git-http-push)

Push objects over HTTP/DAV to another repository

#Documentation/git.txt-git-receive-pack1[git-receive-pack[1]](/docs/git-receive-pack)

Receive what is pushed into the repository

#Documentation/git.txt-git-shell1[git-shell[1]](/docs/git-shell)

Restricted login shell for Git-only SSH access

#Documentation/git.txt-git-upload-archive1[git-upload-archive[1]](/docs/git-upload-archive)

Send archive back to git-archive

#Documentation/git.txt-git-upload-pack1[git-upload-pack[1]](/docs/git-upload-pack)

Send objects packed back to git-fetch-pack

### #_internal_helper_commandsInternal helper commands

These are internal helper commands used by other commands; end users typically do not use them directly.

#Documentation/git.txt-git-check-attr1[git-check-attr[1]](/docs/git-check-attr)

Display gitattributes information

#Documentation/git.txt-git-check-ignore1[git-check-ignore[1]](/docs/git-check-ignore)

Debug gitignore / exclude files

#Documentation/git.txt-git-check-mailmap1[git-check-mailmap[1]](/docs/git-check-mailmap)

Show canonical names and email addresses of contacts

#Documentation/git.txt-git-check-ref-format1[git-check-ref-format[1]](/docs/git-check-ref-format)

Ensures that a reference name is well formed

#Documentation/git.txt-git-column1[git-column[1]](/docs/git-column)

Display data in columns

#Documentation/git.txt-git-credential1[git-credential[1]](/docs/git-credential)

Retrieve and store user credentials

#Documentation/git.txt-git-credential-cache1[git-credential-cache[1]](/docs/git-credential-cache)

Helper to temporarily store passwords in memory

#Documentation/git.txt-git-credential-store1[git-credential-store[1]](/docs/git-credential-store)

Helper to store credentials on disk

#Documentation/git.txt-git-fmt-merge-msg1[git-fmt-merge-msg[1]](/docs/git-fmt-merge-msg)

Produce a merge commit message

#Documentation/git.txt-git-hook1[git-hook[1]](/docs/git-hook)

Run git hooks

#Documentation/git.txt-git-interpret-trailers1[git-interpret-trailers[1]](/docs/git-interpret-trailers)

Add or parse structured information in commit messages

#Documentation/git.txt-git-mailinfo1[git-mailinfo[1]](/docs/git-mailinfo)

Extracts patch and authorship from a single e-mail message

#Documentation/git.txt-git-mailsplit1[git-mailsplit[1]](/docs/git-mailsplit)

Simple UNIX mbox splitter program

#Documentation/git.txt-git-merge-one-file1[git-merge-one-file[1]](/docs/git-merge-one-file)

The standard helper program to use with git-merge-index

#Documentation/git.txt-git-patch-id1[git-patch-id[1]](/docs/git-patch-id)

Compute unique ID for a patch

#Documentation/git.txt-git-sh-i18n1[git-sh-i18n[1]](/docs/git-sh-i18n)

Git’s i18n setup code for shell scripts

#Documentation/git.txt-git-sh-setup1[git-sh-setup[1]](/docs/git-sh-setup)

Common Git shell script setup code

#Documentation/git.txt-git-stripspace1[git-stripspace[1]](/docs/git-stripspace)

Remove unnecessary whitespace

## #_guidesGuides

The following documentation pages are guides about Git concepts.

#Documentation/git.txt-gitcore-tutorial7[gitcore-tutorial[7]](/docs/gitcore-tutorial)

A Git core tutorial for developers

#Documentation/git.txt-gitcredentials7[gitcredentials[7]](/docs/gitcredentials)

Providing usernames and passwords to Git

#Documentation/git.txt-gitcvs-migration7[gitcvs-migration[7]](/docs/gitcvs-migration)

Git for CVS users

#Documentation/git.txt-gitdiffcore7[gitdiffcore[7]](/docs/gitdiffcore)

Tweaking diff output

#Documentation/git.txt-giteveryday7[giteveryday[7]](/docs/giteveryday)

A useful minimum set of commands for Everyday Git

#Documentation/git.txt-gitfaq7[gitfaq[7]](/docs/gitfaq)

Frequently asked questions about using Git

#Documentation/git.txt-gitglossary7[gitglossary[7]](/docs/gitglossary)

A Git Glossary

#Documentation/git.txt-gitnamespaces7[gitnamespaces[7]](/docs/gitnamespaces)

Git namespaces

#Documentation/git.txt-gitremote-helpers7[gitremote-helpers[7]](/docs/gitremote-helpers)

Helper programs to interact with remote repositories

#Documentation/git.txt-gitsubmodules7[gitsubmodules[7]](/docs/gitsubmodules)

Mounting one repository inside another

#Documentation/git.txt-gittutorial7[gittutorial[7]](/docs/gittutorial)

A tutorial introduction to Git

#Documentation/git.txt-gittutorial-27[gittutorial-2[7]](/docs/gittutorial-2)

A tutorial introduction to Git: part two

#Documentation/git.txt-gitworkflows7[gitworkflows[7]](/docs/gitworkflows)

An overview of recommended workflows with Git

## #_repository_command_and_file_interfacesRepository, command and file interfaces

This documentation discusses repository and command interfaces which users are expected to interact with directly. See `--user-formats` in [git-help[1]](/docs/git-help) for more details on the criteria.

#Documentation/git.txt-gitattributes5[gitattributes[5]](/docs/gitattributes)

Defining attributes per path

#Documentation/git.txt-gitcli7[gitcli[7]](/docs/gitcli)

Git command-line interface and conventions

#Documentation/git.txt-githooks5[githooks[5]](/docs/githooks)

Hooks used by Git

#Documentation/git.txt-gitignore5[gitignore[5]](/docs/gitignore)

Specifies intentionally untracked files to ignore

#Documentation/git.txt-gitmailmap5[gitmailmap[5]](/docs/gitmailmap)

Map author/committer names and/or E-Mail addresses

#Documentation/git.txt-gitmodules5[gitmodules[5]](/docs/gitmodules)

Defining submodule properties

#Documentation/git.txt-gitrepository-layout5[gitrepository-layout[5]](/docs/gitrepository-layout)

Git Repository Layout

#Documentation/git.txt-gitrevisions7[gitrevisions[7]](/docs/gitrevisions)

Specifying revisions and ranges for Git

## #_file_formats_protocols_and_other_developer_interfacesFile formats, protocols and other developer interfaces

This documentation discusses file formats, over-the-wire protocols and other git developer interfaces. See `--developer-interfaces` in [git-help[1]](/docs/git-help).

#Documentation/git.txt-gitformat-bundle5[gitformat-bundle[5]](/docs/gitformat-bundle)

The bundle file format

#Documentation/git.txt-gitformat-chunk5[gitformat-chunk[5]](/docs/gitformat-chunk)

Chunk-based file formats

#Documentation/git.txt-gitformat-commit-graph5[gitformat-commit-graph[5]](/docs/gitformat-commit-graph)

Git commit-graph format

#Documentation/git.txt-gitformat-index5[gitformat-index[5]](/docs/gitformat-index)

Git index format

#Documentation/git.txt-gitformat-pack5[gitformat-pack[5]](/docs/gitformat-pack)

Git pack format

#Documentation/git.txt-gitformat-signature5[gitformat-signature[5]](/docs/gitformat-signature)

Git cryptographic signature formats

#Documentation/git.txt-gitprotocol-capabilities5[gitprotocol-capabilities[5]](/docs/gitprotocol-capabilities)

Protocol v0 and v1 capabilities

#Documentation/git.txt-gitprotocol-common5[gitprotocol-common[5]](/docs/gitprotocol-common)

Things common to various protocols

#Documentation/git.txt-gitprotocol-http5[gitprotocol-http[5]](/docs/gitprotocol-http)

Git HTTP-based protocols

#Documentation/git.txt-gitprotocol-pack5[gitprotocol-pack[5]](/docs/gitprotocol-pack)

How packs are transferred over-the-wire

#Documentation/git.txt-gitprotocol-v25[gitprotocol-v2[5]](/docs/gitprotocol-v2)

Git Wire Protocol, Version 2

## #_configuration_mechanismConfiguration Mechanism

Git uses a simple text format to store customizations that are per repository and are per user. Such a configuration file may look like this:

```
#
# A '#' or ';' character indicates a comment.
#

; core variables
[core]
	; Don't trust file modes
	filemode = false

; user identity
[user]
	name = "Junio C Hamano"
	email = "gitster@pobox.com"
```

Various commands read from the configuration file and adjust their operation accordingly. See [git-config[1]](/docs/git-config) for a list and more details about the configuration mechanism.

## #_identifier_terminologyIdentifier Terminology

#Documentation/git.txt-object<object>

Indicates the object name for any type of object.

#Documentation/git.txt-blob<blob> 

Indicates a blob object name.

#Documentation/git.txt-tree<tree>

Indicates a tree object name.

#Documentation/git.txt-commit<commit>

Indicates a commit object name.

#Documentation/git.txt-tree-ish<tree-ish>

Indicates a tree, commit or tag object name. A command that takes a <tree-ish> argument ultimately wants to operate on a <tree> object but automatically dereferences <commit> and <tag> objects that point at a <tree>.

#Documentation/git.txt-commit-ish<commit-ish> 

Indicates a commit or tag object name. A command that takes a <commit-ish> argument ultimately wants to operate on a <commit> object but automatically dereferences <tag> objects that point at a <commit>.

#Documentation/git.txt-type<type> 

Indicates that an object type is required. Currently one of: `blob`, `tree`, `commit`, or `tag`.

#Documentation/git.txt-file<file> 

Indicates a filename - almost always relative to the root of the tree structure `GIT_INDEX_FILE` describes.

## #_symbolic_identifiersSymbolic Identifiers

Any Git command accepting any <object> can also use the following symbolic notation:

#Documentation/git.txt-HEADHEAD 

indicates the head of the current branch.

#Documentation/git.txt-tag<tag>

a valid tag name (i.e. a `refs/tags/`<tag> reference).

#Documentation/git.txt-head<head>

a valid head name (i.e. a `refs/heads/`<head> reference).

For a more complete list of ways to spell object names, see "SPECIFYING REVISIONS" section in [gitrevisions[7]](/docs/gitrevisions).

## #_filedirectory_structureFile/Directory Structure

Please see the [gitrepository-layout[5]](/docs/gitrepository-layout) document.

Read [githooks[5]](/docs/githooks) for more details about each hook.

Higher level SCMs may provide and manage additional information in the `$GIT_DIR`.

## #_terminologyTerminology

Please see [gitglossary[7]](/docs/gitglossary).

## #_environment_variablesEnvironment Variables

Various Git commands pay attention to environment variables and change their behavior. The environment variables marked as "Boolean" take their values the same way as Boolean valued configuration variables, i.e., "true", "yes", "on" and positive numbers are taken as "yes", while "false", "no", "off", and "0" are taken as "no".

Here are the variables:

### #_systemSystem

#Documentation/git.txt-HOME`HOME`

Specifies the path to the user’s home directory. On Windows, if unset, Git will set a process environment variable equal to: `$HOMEDRIVE$HOMEPATH` if both `$HOMEDRIVE` and `$HOMEPATH` exist; otherwise `$USERPROFILE` if `$USERPROFILE` exists.

### #_the_git_repositoryThe Git Repository

These environment variables apply to all core Git commands. Nb: it is worth noting that they may be used/overridden by SCMS sitting above Git so take care if using a foreign front-end.

#Documentation/git.txt-GITINDEXFILE`GIT_INDEX_FILE`

This environment variable specifies an alternate index file. If not specified, the default of `$GIT_DIR/index` is used.

#Documentation/git.txt-GITINDEXVERSION`GIT_INDEX_VERSION`

This environment variable specifies what index version is used when writing the index file out. It won’t affect existing index files. By default index file version 2 or 3 is used. See [git-update-index[1]](/docs/git-update-index) for more information.

#Documentation/git.txt-GITOBJECTDIRECTORY`GIT_OBJECT_DIRECTORY`

If the object storage directory is specified via this environment variable then the sha1 directories are created underneath - otherwise the default `$GIT_DIR/objects` directory is used.

#Documentation/git.txt-GITALTERNATEOBJECTDIRECTORIES`GIT_ALTERNATE_OBJECT_DIRECTORIES`

Due to the immutable nature of Git objects, old objects can be archived into shared, read-only directories. This variable specifies a ":" separated (on Windows ";" separated) list of Git object directories which can be used to search for Git objects. New objects will not be written to these directories.

Entries that begin with `"` (double-quote) will be interpreted as C-style quoted paths, removing leading and trailing double-quotes and respecting backslash escapes. E.g., the value "path-with-\"-and-:-in-it":vanilla-path has two paths: `path-with-"-and-:-in-it` and `vanilla-path`.

#Documentation/git.txt-GITDIR`GIT_DIR`

If the `GIT_DIR` environment variable is set then it specifies a path to use instead of the default `.git` for the base of the repository. The `--git-dir` command-line option also sets this value.

#Documentation/git.txt-GITWORKTREE`GIT_WORK_TREE`

Set the path to the root of the working tree. This can also be controlled by the `--work-tree` command-line option and the core.worktree configuration variable.

#Documentation/git.txt-GITNAMESPACE`GIT_NAMESPACE`

Set the Git namespace; see [gitnamespaces[7]](/docs/gitnamespaces) for details. The `--namespace` command-line option also sets this value.

#Documentation/git.txt-GITCEILINGDIRECTORIES`GIT_CEILING_DIRECTORIES`

This should be a colon-separated list of absolute paths. If set, it is a list of directories that Git should not chdir up into while looking for a repository directory (useful for excluding slow-loading network directories). It will not exclude the current working directory or a GIT_DIR set on the command line or in the environment. Normally, Git has to read the entries in this list and resolve any symlink that might be present in order to compare them with the current directory. However, if even this access is slow, you can add an empty entry to the list to tell Git that the subsequent entries are not symlinks and needn’t be resolved; e.g., `GIT_CEILING_DIRECTORIES=/maybe/symlink::/very/slow/non/symlink`.

#Documentation/git.txt-GITDISCOVERYACROSSFILESYSTEM`GIT_DISCOVERY_ACROSS_FILESYSTEM`

When run in a directory that does not have ".git" repository directory, Git tries to find such a directory in the parent directories to find the top of the working tree, but by default it does not cross filesystem boundaries. This Boolean environment variable can be set to true to tell Git not to stop at filesystem boundaries. Like `GIT_CEILING_DIRECTORIES`, this will not affect an explicit repository directory set via `GIT_DIR` or on the command line.

#Documentation/git.txt-GITCOMMONDIR`GIT_COMMON_DIR`

If this variable is set to a path, non-worktree files that are normally in $GIT_DIR will be taken from this path instead. Worktree-specific files such as HEAD or index are taken from $GIT_DIR. See [gitrepository-layout[5]](/docs/gitrepository-layout) and [git-worktree[1]](/docs/git-worktree) for details. This variable has lower precedence than other path variables such as GIT_INDEX_FILE, GIT_OBJECT_DIRECTORY…​

#Documentation/git.txt-GITDEFAULTHASH`GIT_DEFAULT_HASH`

If this variable is set, the default hash algorithm for new repositories will be set to this value. This value is ignored when cloning and the setting of the remote repository is always used. The default is "sha1". See `--object-format` in [git-init[1]](/docs/git-init).

#Documentation/git.txt-GITDEFAULTREFFORMAT`GIT_DEFAULT_REF_FORMAT`

If this variable is set, the default reference backend format for new repositories will be set to this value. The default is "files". See `--ref-format` in [git-init[1]](/docs/git-init).

### #_git_commitsGit Commits

#Documentation/git.txt-GITAUTHORNAME`GIT_AUTHOR_NAME`

The human-readable name used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.name` and `author.name` configuration settings.

#Documentation/git.txt-GITAUTHOREMAIL`GIT_AUTHOR_EMAIL`

The email address used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.email` and `author.email` configuration settings.

#Documentation/git.txt-GITAUTHORDATE`GIT_AUTHOR_DATE`

The date used for the author identity when creating commit or tag objects, or when writing reflogs. See [git-commit[1]](/docs/git-commit) for valid formats.

#Documentation/git.txt-GITCOMMITTERNAME`GIT_COMMITTER_NAME`

The human-readable name used in the committer identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.name` and `committer.name` configuration settings.

#Documentation/git.txt-GITCOMMITTEREMAIL`GIT_COMMITTER_EMAIL`

The email address used in the author identity when creating commit or tag objects, or when writing reflogs. Overrides the `user.email` and `committer.email` configuration settings.

#Documentation/git.txt-GITCOMMITTERDATE`GIT_COMMITTER_DATE`

The date used for the committer identity when creating commit or tag objects, or when writing reflogs. See [git-commit[1]](/docs/git-commit) for valid formats.

#Documentation/git.txt-EMAIL`EMAIL`

The email address used in the author and committer identities if no other relevant environment variable or configuration setting has been set.

### #_git_diffsGit Diffs

#Documentation/git.txt-GITDIFFOPTS`GIT_DIFF_OPTS`

Only valid setting is "--unified=??" or "-u??" to set the number of context lines shown when a unified diff is created. This takes precedence over any "-U" or "--unified" option value passed on the Git diff command line.

#Documentation/git.txt-GITEXTERNALDIFF`GIT_EXTERNAL_DIFF`

When the environment variable `GIT_EXTERNAL_DIFF` is set, the program named by it is called to generate diffs, and Git does not use its builtin diff machinery. For a path that is added, removed, or modified, `GIT_EXTERNAL_DIFF` is called with 7 parameters:

```
path old-file old-hex old-mode new-file new-hex new-mode
```

where:

#Documentation/git.txt-oldnew-file<old|new>-file 

are files GIT_EXTERNAL_DIFF can use to read the contents of <old|new>,

#Documentation/git.txt-oldnew-hex<old|new>-hex 

are the 40-hexdigit SHA-1 hashes,

#Documentation/git.txt-oldnew-mode<old|new>-mode 

are the octal representation of the file modes.

The file parameters can point at the user’s working file (e.g. `new-file` in "git-diff-files"), `/dev/null` (e.g. `old-file` when a new file is added), or a temporary file (e.g. `old-file` in the index). `GIT_EXTERNAL_DIFF` should not worry about unlinking the temporary file — it is removed when `GIT_EXTERNAL_DIFF` exits.

For a path that is unmerged, `GIT_EXTERNAL_DIFF` is called with 1 parameter, <path>.

For each path `GIT_EXTERNAL_DIFF` is called, two environment variables, `GIT_DIFF_PATH_COUNTER` and `GIT_DIFF_PATH_TOTAL` are set.

#Documentation/git.txt-GITEXTERNALDIFFTRUSTEXITCODE`GIT_EXTERNAL_DIFF_TRUST_EXIT_CODE`

If this Boolean environment variable is set to true then the `GIT_EXTERNAL_DIFF` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(`1`). If it is set to false, which is the default, then the command is expected to return exit code 0 regardless of equality. Any other exit code causes Git to report a fatal error.

#Documentation/git.txt-GITDIFFPATHCOUNTER`GIT_DIFF_PATH_COUNTER`

A 1-based counter incremented by one for every path.

#Documentation/git.txt-GITDIFFPATHTOTAL`GIT_DIFF_PATH_TOTAL`

The total number of paths.

### #_otherother

#Documentation/git.txt-GITMERGEVERBOSITY`GIT_MERGE_VERBOSITY`

A number controlling the amount of output shown by the recursive merge strategy. Overrides merge.verbosity. See [git-merge[1]](/docs/git-merge)

#Documentation/git.txt-GITPAGER`GIT_PAGER`

This environment variable overrides `$PAGER`. If it is set to an empty string or to the value "cat", Git will not launch a pager. See also the `core.pager` option in [git-config[1]](/docs/git-config).

#Documentation/git.txt-GITPROGRESSDELAY`GIT_PROGRESS_DELAY`

A number controlling how many seconds to delay before showing optional progress indicators. Defaults to 1.

#Documentation/git.txt-GITEDITOR`GIT_EDITOR`

This environment variable overrides `$EDITOR` and `$VISUAL`. It is used by several Git commands when, on interactive mode, an editor is to be launched. See also [git-var[1]](/docs/git-var) and the `core.editor` option in [git-config[1]](/docs/git-config).

#Documentation/git.txt-GITSEQUENCEEDITOR`GIT_SEQUENCE_EDITOR`

This environment variable overrides the configured Git editor when editing the todo list of an interactive rebase. See also [git-rebase[1]](/docs/git-rebase) and the `sequence.editor` option in [git-config[1]](/docs/git-config).

#Documentation/git.txt-GITSSH`GIT_SSH`#Documentation/git.txt-GITSSHCOMMAND`GIT_SSH_COMMAND`

If either of these environment variables is set then git fetch and git push will use the specified command instead of ssh when they need to connect to a remote system. The command-line parameters passed to the configured command are determined by the ssh variant. See `ssh.variant` option in [git-config[1]](/docs/git-config) for details.

`$GIT_SSH_COMMAND` takes precedence over `$GIT_SSH`, and is interpreted by the shell, which allows additional arguments to be included. `$GIT_SSH` on the other hand must be just the path to a program (which can be a wrapper shell script, if additional arguments are needed).

Usually it is easier to configure any desired options through your personal `.ssh/config` file. Please consult your ssh documentation for further details.

#Documentation/git.txt-GITSSHVARIANT`GIT_SSH_VARIANT`

If this environment variable is set, it overrides Git’s autodetection whether `GIT_SSH`/`GIT_SSH_COMMAND`/`core.sshCommand` refer to OpenSSH, plink or tortoiseplink. This variable overrides the config setting `ssh.variant` that serves the same purpose.

#Documentation/git.txt-GITSSLNOVERIFY`GIT_SSL_NO_VERIFY`

Setting and exporting this environment variable to any value tells Git not to verify the SSL certificate when fetching or pushing over HTTPS.

#Documentation/git.txt-GITATTRSOURCE`GIT_ATTR_SOURCE`

Sets the treeish that gitattributes will be read from.

#Documentation/git.txt-GITASKPASS`GIT_ASKPASS`

If this environment variable is set, then Git commands which need to acquire passwords or passphrases (e.g. for HTTP or IMAP authentication) will call this program with a suitable prompt as command-line argument and read the password from its STDOUT. See also the `core.askPass` option in [git-config[1]](/docs/git-config).

#Documentation/git.txt-GITTERMINALPROMPT`GIT_TERMINAL_PROMPT`

If this Boolean environment variable is set to false, git will not prompt on the terminal (e.g., when asking for HTTP authentication).

#Documentation/git.txt-GITCONFIGGLOBAL`GIT_CONFIG_GLOBAL`#Documentation/git.txt-GITCONFIGSYSTEM`GIT_CONFIG_SYSTEM`

Take the configuration from the given files instead from global or system-level configuration files. If `GIT_CONFIG_SYSTEM` is set, the system config file defined at build time (usually `/etc/gitconfig`) will not be read. Likewise, if `GIT_CONFIG_GLOBAL` is set, neither `$HOME/.gitconfig` nor `$XDG_CONFIG_HOME/git/config` will be read. Can be set to `/dev/null` to skip reading configuration files of the respective level.

#Documentation/git.txt-GITCONFIGNOSYSTEM`GIT_CONFIG_NOSYSTEM`

Whether to skip reading settings from the system-wide `$`(`prefix`)`/etc/gitconfig` file. This Boolean environment variable can be used along with `$HOME` and `$XDG_CONFIG_HOME` to create a predictable environment for a picky script, or you can set it to true to temporarily avoid using a buggy `/etc/gitconfig` file while waiting for someone with sufficient permissions to fix it.

#Documentation/git.txt-GITFLUSH`GIT_FLUSH`

If this Boolean environment variable is set to true, then commands such as git blame (in incremental mode), git rev-list, git log, git check-attr and git check-ignore will force a flush of the output stream after each record have been flushed. If this variable is set to false, the output of these commands will be done using completely buffered I/O. If this environment variable is not set, Git will choose buffered or record-oriented flushing based on whether stdout appears to be redirected to a file or not.

#Documentation/git.txt-GITTRACE`GIT_TRACE`

Enables general trace messages, e.g. alias expansion, built-in command execution and external command execution.

If this variable is set to "1", "2" or "true" (comparison is case insensitive), trace messages will be printed to stderr.

If the variable is set to an integer value greater than 2 and lower than 10 (strictly) then Git will interpret this value as an open file descriptor and will try to write the trace messages into this file descriptor.

Alternatively, if the variable is set to an absolute path (starting with a / character), Git will interpret this as a file path and will try to append the trace messages to it.

Unsetting the variable, or setting it to empty, "0" or "false" (case insensitive) disables trace messages.

#Documentation/git.txt-GITTRACEFSMONITOR`GIT_TRACE_FSMONITOR`

Enables trace messages for the filesystem monitor extension. See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACEPACKACCESS`GIT_TRACE_PACK_ACCESS`

Enables trace messages for all accesses to any packs. For each access, the pack file name and an offset in the pack is recorded. This may be helpful for troubleshooting some pack-related performance problems. See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACEPACKET`GIT_TRACE_PACKET`

Enables trace messages for all packets coming in or out of a given program. This can help with debugging object negotiation or other protocol issues. Tracing is turned off at a packet starting with "PACK" (but see `GIT_TRACE_PACKFILE` below). See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACEPACKFILE`GIT_TRACE_PACKFILE`

Enables tracing of packfiles sent or received by a given program. Unlike other trace output, this trace is verbatim: no headers, and no quoting of binary data. You almost certainly want to direct into a file (e.g., `GIT_TRACE_PACKFILE=/tmp/my.pack`) rather than displaying it on the terminal or mixing it with other trace output.

Note that this is currently only implemented for the client side of clones and fetches.

#Documentation/git.txt-GITTRACEPERFORMANCE`GIT_TRACE_PERFORMANCE`

Enables performance related trace messages, e.g. total execution time of each Git command. See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACEREFS`GIT_TRACE_REFS`

Enables trace messages for operations on the ref database. See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACESETUP`GIT_TRACE_SETUP`

Enables trace messages printing the .git, working tree and current working directory after Git has completed its setup phase. See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACESHALLOW`GIT_TRACE_SHALLOW`

Enables trace messages that can help debugging fetching / cloning of shallow repositories. See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACECURL`GIT_TRACE_CURL`

Enables a curl full trace dump of all incoming and outgoing data, including descriptive information, of the git transport protocol. This is similar to doing curl `--trace-ascii` on the command line. See `GIT_TRACE` for available trace output options.

#Documentation/git.txt-GITTRACECURLNODATA`GIT_TRACE_CURL_NO_DATA`

When a curl trace is enabled (see `GIT_TRACE_CURL` above), do not dump data (that is, only dump info lines and headers).

#Documentation/git.txt-GITTRACE2`GIT_TRACE2`

Enables more detailed trace messages from the "trace2" library. Output from `GIT_TRACE2` is a simple text-based format for human readability.

If this variable is set to "1", "2" or "true" (comparison is case insensitive), trace messages will be printed to stderr.

If the variable is set to an integer value greater than 2 and lower than 10 (strictly) then Git will interpret this value as an open file descriptor and will try to write the trace messages into this file descriptor.

Alternatively, if the variable is set to an absolute path (starting with a / character), Git will interpret this as a file path and will try to append the trace messages to it. If the path already exists and is a directory, the trace messages will be written to files (one per process) in that directory, named according to the last component of the SID and an optional counter (to avoid filename collisions).

In addition, if the variable is set to `af_unix:`[<socket-type>`:`]<absolute-pathname>, Git will try to open the path as a Unix Domain Socket. The socket type can be either `stream` or `dgram`.

Unsetting the variable, or setting it to empty, "0" or "false" (case insensitive) disables trace messages.

See [Trace2 documentation](/docs/api-trace2) for full details.

#Documentation/git.txt-GITTRACE2EVENT`GIT_TRACE2_EVENT`

This setting writes a JSON-based format that is suited for machine interpretation. See `GIT_TRACE2` for available trace output options and [Trace2 documentation](/docs/api-trace2) for full details.

#Documentation/git.txt-GITTRACE2PERF`GIT_TRACE2_PERF`

In addition to the text-based messages available in `GIT_TRACE2`, this setting writes a column-based format for understanding nesting regions. See `GIT_TRACE2` for available trace output options and [Trace2 documentation](/docs/api-trace2) for full details.

#Documentation/git.txt-GITTRACEREDACT`GIT_TRACE_REDACT`

By default, when tracing is activated, Git redacts the values of cookies, the "Authorization:" header, the "Proxy-Authorization:" header and packfile URIs. Set this Boolean environment variable to false to prevent this redaction.

#Documentation/git.txt-GITNOREPLACEOBJECTS`GIT_NO_REPLACE_OBJECTS`

Setting and exporting this environment variable tells Git to ignore replacement refs and do not replace Git objects.

#Documentation/git.txt-GITLITERALPATHSPECS`GIT_LITERAL_PATHSPECS`

Setting this Boolean environment variable to true will cause Git to treat all pathspecs literally, rather than as glob patterns. For example, running `GIT_LITERAL_PATHSPECS=1``git``log``--``*.c'` will search for commits that touch the path `*.c`, not any paths that the glob `*.c` matches. You might want this if you are feeding literal paths to Git (e.g., paths previously given to you by `git``ls-tree`, `--raw` diff output, etc).

#Documentation/git.txt-GITGLOBPATHSPECS`GIT_GLOB_PATHSPECS`

Setting this Boolean environment variable to true will cause Git to treat all pathspecs as glob patterns (aka "glob" magic).

#Documentation/git.txt-GITNOGLOBPATHSPECS`GIT_NOGLOB_PATHSPECS`

Setting this Boolean environment variable to true will cause Git to treat all pathspecs as literal (aka "literal" magic).

#Documentation/git.txt-GITICASEPATHSPECS`GIT_ICASE_PATHSPECS`

Setting this Boolean environment variable to true will cause Git to treat all pathspecs as case-insensitive.

#Documentation/git.txt-GITNOLAZYFETCH`GIT_NO_LAZY_FETCH`

Setting this Boolean environment variable to true tells Git not to lazily fetch missing objects from the promisor remote on demand.

#Documentation/git.txt-GITREFLOGACTION`GIT_REFLOG_ACTION`

When a ref is updated, reflog entries are created to keep track of the reason why the ref was updated (which is typically the name of the high-level command that updated the ref), in addition to the old and new values of the ref. A scripted Porcelain command can use set_reflog_action helper function in `git-sh-setup` to set its name to this variable when it is invoked as the top level command by the end user, to be recorded in the body of the reflog.

#Documentation/git.txt-GITREFPARANOIA`GIT_REF_PARANOIA`

If this Boolean environment variable is set to false, ignore broken or badly named refs when iterating over lists of refs. Normally Git will try to include any such refs, which may cause some operations to fail. This is usually preferable, as potentially destructive operations (e.g., [git-prune[1]](/docs/git-prune)) are better off aborting rather than ignoring broken refs (and thus considering the history they point to as not worth saving). The default value is `1` (i.e., be paranoid about detecting and aborting all operations). You should not normally need to set this to `0`, but it may be useful when trying to salvage data from a corrupted repository.

#Documentation/git.txt-GITCOMMITGRAPHPARANOIA`GIT_COMMIT_GRAPH_PARANOIA`

When loading a commit object from the commit-graph, Git performs an existence check on the object in the object database. This is done to avoid issues with stale commit-graphs that contain references to already-deleted commits, but comes with a performance penalty.

The default is "false", which disables the aforementioned behavior. Setting this to "true" enables the existence check so that stale commits will never be returned from the commit-graph at the cost of performance.

#Documentation/git.txt-GITALLOWPROTOCOL`GIT_ALLOW_PROTOCOL`

If set to a colon-separated list of protocols, behave as if `protocol.allow` is set to `never`, and each of the listed protocols has `protocol.`<name>`.allow` set to `always` (overriding any existing configuration). See the description of `protocol.allow` in [git-config[1]](/docs/git-config) for more details.

#Documentation/git.txt-GITPROTOCOLFROMUSER`GIT_PROTOCOL_FROM_USER`

Set this Boolean environment variable to false to prevent protocols used by fetch/push/clone which are configured to the `user` state. This is useful to restrict recursive submodule initialization from an untrusted repository or for programs which feed potentially-untrusted URLS to git commands. See [git-config[1]](/docs/git-config) for more details.

#Documentation/git.txt-GITPROTOCOL`GIT_PROTOCOL`

For internal use only. Used in handshaking the wire protocol. Contains a colon : separated list of keys with optional values <key>[=<value>]. Presence of unknown keys and values must be ignored.

Note that servers may need to be configured to allow this variable to pass over some transports. It will be propagated automatically when accessing local repositories (i.e., `file://` or a filesystem path), as well as over the `git://` protocol. For git-over-http, it should work automatically in most configurations, but see the discussion in [git-http-backend[1]](/docs/git-http-backend). For git-over-ssh, the ssh server may need to be configured to allow clients to pass this variable (e.g., by using `AcceptEnv``GIT_PROTOCOL` with OpenSSH).

This configuration is optional. If the variable is not propagated, then clients will fall back to the original "v0" protocol (but may miss out on some performance improvements or features). This variable currently only affects clones and fetches; it is not yet used for pushes (but may be in the future).

#Documentation/git.txt-GITOPTIONALLOCKS`GIT_OPTIONAL_LOCKS`

If this Boolean environment variable is set to false, Git will complete any requested operation without performing any optional sub-operations that require taking a lock. For example, this will prevent `git``status` from refreshing the index as a side effect. This is useful for processes running in the background which do not want to cause lock contention with other operations on the repository. Defaults to `1`.

#Documentation/git.txt-GITREDIRECTSTDIN`GIT_REDIRECT_STDIN`#Documentation/git.txt-GITREDIRECTSTDOUT`GIT_REDIRECT_STDOUT`#Documentation/git.txt-GITREDIRECTSTDERR`GIT_REDIRECT_STDERR`

Windows-only: allow redirecting the standard input/output/error handles to paths specified by the environment variables. This is particularly useful in multi-threaded applications where the canonical way to pass standard handles via `CreateProcess`() is not an option because it would require the handles to be marked inheritable (and consequently every spawned process would inherit them, possibly blocking regular Git operations). The primary intended use case is to use named pipes for communication (e.g. \\.\pipe\my-git-stdin-123).

Two special values are supported: `off` will simply close the corresponding standard handle, and if `GIT_REDIRECT_STDERR` is 2>&1, standard error will be redirected to the same handle as standard output.

#Documentation/git.txt-GITPRINTSHA1ELLIPSISdeprecated`GIT_PRINT_SHA1_ELLIPSIS` (deprecated) 

If set to `yes`, print an ellipsis following an (abbreviated) SHA-1 value. This affects indications of detached HEADs ([git-checkout[1]](/docs/git-checkout)) and the raw diff output ([git-diff[1]](/docs/git-diff)). Printing an ellipsis in the cases mentioned is no longer considered adequate and support for it is likely to be removed in the foreseeable future (along with the variable).

#Documentation/git.txt-GITADVICE`GIT_ADVICE`

If set to `0`, then disable all advice messages. These messages are intended to provide hints to human users that may help them get out of problematic situations or take advantage of new features. Users can disable individual messages using the `advice.*` config keys. These messages may be disruptive to tools that execute Git processes, so this variable is available to disable the messages. (The `--no-advice` global option is also available, but old Git versions may fail when this option is not understood. The environment variable will be ignored by Git versions that do not understand it.)

## #_discussionDiscussion

More detail on the following is available from the [Git concepts chapter of the
user-manual](/docs/user-manual#git-concepts) and [gitcore-tutorial[7]](/docs/gitcore-tutorial).

A Git project normally consists of a working directory with a ".git" subdirectory at the top level. The .git directory contains, among other things, a compressed object database representing the complete history of the project, an "index" file which links that history to the current contents of the working tree, and named pointers into that history such as tags and branch heads.

The object database contains objects of three main types: blobs, which hold file data; trees, which point to blobs and other trees to build up directory hierarchies; and commits, which each reference a single tree and some number of parent commits.

The commit, equivalent to what other systems call a "changeset" or "version", represents a step in the project’s history, and each parent represents an immediately preceding step. Commits with more than one parent represent merges of independent lines of development.

All objects are named by the SHA-1 hash of their contents, normally written as a string of 40 hex digits. Such names are globally unique. The entire history leading up to a commit can be vouched for by signing just that commit. A fourth object type, the tag, is provided for this purpose.

When first created, objects are stored in individual files, but for efficiency may later be compressed together into "pack files".

Named pointers called refs mark interesting points in history. A ref may contain the SHA-1 name of an object or the name of another ref (the latter is called a "symbolic ref"). Refs with names beginning `refs/head/` contain the SHA-1 name of the most recent commit (or "head") of a branch under development. SHA-1 names of tags of interest are stored under `refs/tags/`. A symbolic ref named `HEAD` contains the name of the currently checked-out branch.

The index file is initialized with a list of all paths and, for each path, a blob object and a set of attributes. The blob object represents the contents of the file as of the head of the current branch. The attributes (last modified time, size, etc.) are taken from the corresponding file in the working tree. Subsequent changes to the working tree can be found by comparing these attributes. The index may be updated with new content, and new commits may be created from the content stored in the index.

The index is also capable of storing multiple entries (called "stages") for a given pathname. These stages are used to hold the various unmerged version of a file when a merge is in progress.

## #_securitySECURITY

Some configuration options and hook files may cause Git to run arbitrary shell commands. Because configuration and hooks are not copied using `git``clone`, it is generally safe to clone remote repositories with untrusted content, inspect them with `git``log`, and so on.

However, it is not safe to run Git commands in a `.git` directory (or the working tree that surrounds it) when that `.git` directory itself comes from an untrusted source. The commands in its config and hooks are executed in the usual way.

By default, Git will refuse to run when the repository is owned by someone other than the user running the command. See the entry for `safe.directory` in [git-config[1]](/docs/git-config). While this can help protect you in a multi-user environment, note that you can also acquire untrusted repositories that are owned by you (for example, if you extract a zip file or tarball from an untrusted source). In such cases, you’d need to "sanitize" the untrusted repository first.

If you have an untrusted `.git` directory, you should first clone it with `git``clone``--no-local` to obtain a clean copy. Git does restrict the set of options and hooks that will be run by `upload-pack`, which handles the server side of a clone or fetch, but beware that the surface area for attack against `upload-pack` is large, so this does carry some risk. The safest thing is to serve the repository as an unprivileged user (either via [git-daemon[1]](/docs/git-daemon), ssh, or using other tools to change user ids). See the discussion in the `SECURITY` section of [git-upload-pack[1]](/docs/git-upload-pack).

## #_further_documentationFURTHER DOCUMENTATION

See the references in the "description" section to get started using Git. The following is probably more detail than necessary for a first-time user.

The [Git concepts chapter of the
user-manual](/docs/user-manual#git-concepts) and [gitcore-tutorial[7]](/docs/gitcore-tutorial) both provide introductions to the underlying Git architecture.

See [gitworkflows[7]](/docs/gitworkflows) for an overview of recommended workflows.

See also the [howto](/docs/howto-index) documents for some useful examples.

The internals are documented in the [Git API documentation](/docs/api-index).

Users migrating from CVS may also want to read [gitcvs-migration[7]](/docs/gitcvs-migration).

## #_authorsAuthors

Git was started by Linus Torvalds, and is currently maintained by Junio C Hamano. Numerous contributions have come from the Git mailing list <[git@vger.kernel.org](mailto:git@vger.kernel.org)>. [https://openhub.net/p/git/contributors/summary](https://openhub.net/p/git/contributors/summary) gives you a more complete list of contributors.

If you have a clone of git.git itself, the output of [git-shortlog[1]](/docs/git-shortlog) and [git-blame[1]](/docs/git-blame) can show you the authors for specific parts of the project.

## #_reporting_bugsReporting Bugs

Report bugs to the Git mailing list <[git@vger.kernel.org](mailto:git@vger.kernel.org)> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there. See the list archive at [https://lore.kernel.org/git](https://lore.kernel.org/git) for previous bug reports and other discussions.

Issues which are security relevant should be disclosed privately to the Git Security mailing list <[git-security@googlegroups.com](mailto:git-security@googlegroups.com)>.

## #_see_alsoSEE ALSO

[gittutorial[7]](/docs/gittutorial), [gittutorial-2[7]](/docs/gittutorial-2), [giteveryday[7]](/docs/giteveryday), [gitcvs-migration[7]](/docs/gitcvs-migration), [gitglossary[7]](/docs/gitglossary), [gitcore-tutorial[7]](/docs/gitcore-tutorial), [gitcli[7]](/docs/gitcli), [The Git User’s Manual](/docs/user-manual), [gitworkflows[7]](/docs/gitworkflows)

## #_gitGIT

Part of the [git[1]](/docs/git) suite

### git

[About this site](/site)
 Patches, suggestions, and comments are welcome.  Git is a member of [Software Freedom Conservancy](/sfc)
