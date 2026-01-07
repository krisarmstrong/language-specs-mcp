What is Prettier? · Prettier[Skip to main content](#__docusaurus_skipToContent_fallback)[Prettier](/)[stable](/docs/)

- [next](/docs/next/)
- [stable](/docs/)

[Playground](/playground/)[Docs](/docs/)[Blog](/blog)[Donate](https://opencollective.com/prettier)https://github.com/prettier/prettierSearch

- [About](/docs/)

  - [What is Prettier?](/docs/)
  - [Why Prettier?](/docs/why-prettier)
  - [Prettier vs. Linters](/docs/comparison)
  - [Option Philosophy](/docs/option-philosophy)
  - [Rationale](/docs/rationale)

- [Usage](/docs/install)

  - [Install](/docs/install)
  - [Ignoring Code](/docs/ignore)
  - [Integrating with Linters](/docs/integrating-with-linters)
  - [Pre-commit Hook](/docs/precommit)
  - [Plugins](/docs/plugins)
  - [CLI](/docs/cli)
  - [API](/docs/api)
  - [Browser](/docs/browser)
  - [Run Prettier on CI](/docs/ci)

- [Configuring Prettier](/docs/options)

  - [Options](/docs/options)
  - [Configuration File](/docs/configuration)
  - [Sharing configurations](/docs/sharing-configurations)

- [Editors](/docs/editors)

  - [Editor Integration](/docs/editors)
  - [WebStorm Setup](/docs/webstorm)
  - [Vim Setup](/docs/vim)
  - [Watching For Changes](/docs/watching-files)

- [Misc](/docs/technical-details)

  - [Technical Details](/docs/technical-details)
  - [Related Projects](/docs/related-projects)
  - [For Enterprise](/docs/for-enterprise)

On this page

# What is Prettier?

Prettier is an opinionated code formatter with support for:

- JavaScript (including experimental features)
- [JSX](https://facebook.github.io/jsx/)
- [Angular](https://angular.dev/)
- [Vue](https://vuejs.org/)
- [Flow](https://flow.org/)
- [TypeScript](https://www.typescriptlang.org/)
- CSS, [Less](https://lesscss.org/), and [SCSS](https://sass-lang.com)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [Ember/Handlebars](https://handlebarsjs.com/)
- [JSON](https://json.org/)
- [GraphQL](https://graphql.org/)
- [Markdown](https://commonmark.org/), including [GFM](https://github.github.com/gfm/) and [MDX v1](https://mdxjs.com/)
- [YAML](https://yaml.org/)

It removes all original styling[*](#footnotes) and ensures that all outputted code conforms to a consistent style. (See this [blog post](https://jlongster.com/A-Prettier-Formatter))

Prettier takes your code and reprints it from scratch by taking the line length into account.

For example, take the following code:

```
foo(arg1, arg2, arg3, arg4);
```

It fits in a single line so it’s going to stay as is. However, we've all run into this situation:

```
foo(reallyLongArg(), omgSoManyParameters(), IShouldRefactorThis(), isThereSeriouslyAnotherOne());
```

Suddenly our previous format for calling function breaks down because this is too long. Prettier is going to do the painstaking work of reprinting it like that for you:

```
foo(
  reallyLongArg(),
  omgSoManyParameters(),
  IShouldRefactorThis(),
  isThereSeriouslyAnotherOne(),
);
```

Prettier enforces a consistent code style (i.e. code formatting that won’t affect the AST) across your entire codebase because it disregards the original styling[*](#footnotes) by parsing it away and re-printing the parsed AST with its own rules that take the maximum line length into account, wrapping code when necessary.

If you want to learn more, these two conference talks are great introductions:

https://www.youtube.com/watch?v=hkfBvpEfWdA

https://www.youtube.com/watch?v=0Q4kUNx85_4

#### Footnotes[​](#footnotes)

* Well actually, some original styling is preserved when practical—see [empty lines](/docs/rationale#empty-lines) and [multi-line objects](/docs/rationale#multi-line-objects).[Edit this page](https://github.com/prettier/prettier/edit/main/docs/index.md)[NextWhy Prettier?](/docs/why-prettier)Docs

- [About](/docs)
- [Usage](/docs/install)
- https://www.netlify.com

Community

- [User Showcase](/users)
- [Stack Overflow](http://stackoverflow.com/questions/tagged/prettier)
- [@PrettierCode on X](https://x.com/PrettierCode)

More

- [Blog](/blog)
- [GitHub](https://github.com/prettier/prettier)
- [Issues](https://github.com/prettier/prettier/issues)
- https://github.com/prettier/prettier
