[xojs](/xojs)/[xo](/xojs/xo)Public

- 

###  Uh oh! 

There was an error while loading. Please reload this page.

- [Notifications](/login?return_to=%2Fxojs%2Fxo)You must be signed in to change notification settings
- [Fork
    301](/login?return_to=%2Fxojs%2Fxo)
- [Star
          7.9k](/login?return_to=%2Fxojs%2Fxo)

 ❤️ JavaScript/TypeScript linter (ESLint wrapper) with great defaults 

### License

[MIT license](/xojs/xo/blob/main/license)[7.9k
          stars](/xojs/xo/stargazers)[301
          forks](/xojs/xo/forks)[Branches](/xojs/xo/branches)[Tags](/xojs/xo/tags)[Activity](/xojs/xo/activity)[Star](/login?return_to=%2Fxojs%2Fxo)[Notifications](/login?return_to=%2Fxojs%2Fxo)You must be signed in to change notification settings

- [Code](/xojs/xo)
- [Issues
          60](/xojs/xo/issues)
- [Pull requests
          1](/xojs/xo/pulls)
- [Actions](/xojs/xo/actions)
- 

### 

[Security
          
  
  
    
  
    
      

              Uh oh!

              There was an error while loading. Please reload this page](/xojs/xo/security).

- [Insights](/xojs/xo/pulse)

Additional navigation options

- [Code](/xojs/xo)
- [Issues](/xojs/xo/issues)
- [Pull requests](/xojs/xo/pulls)
- [Actions](/xojs/xo/actions)
- [Security](/xojs/xo/security)
- [Insights](/xojs/xo/pulse)

# xojs/xo
Version: latest

Source: https://github.com/xojs/xo


main[Branches](/xojs/xo/branches)[Tags](/xojs/xo/tags)/xojs/xo/branches/xojs/xo/tagsGo to fileCodeOpen more actions menu

## Folders and files

NameNameLast commit messageLast commit date

## Latest commit

## History

[664 Commits](/xojs/xo/commits/main/)/xojs/xo/commits/main/[.github/workflows](/xojs/xo/tree/main/.github/workflows)[.github/workflows](/xojs/xo/tree/main/.github/workflows)[lib](/xojs/xo/tree/main/lib)[lib](/xojs/xo/tree/main/lib)[media](/xojs/xo/tree/main/media)[media](/xojs/xo/tree/main/media)[scripts](/xojs/xo/tree/main/scripts)[scripts](/xojs/xo/tree/main/scripts)[test](/xojs/xo/tree/main/test)[test](/xojs/xo/tree/main/test)[.editorconfig](/xojs/xo/blob/main/.editorconfig)[.editorconfig](/xojs/xo/blob/main/.editorconfig)[.gitattributes](/xojs/xo/blob/main/.gitattributes)[.gitattributes](/xojs/xo/blob/main/.gitattributes)[.gitignore](/xojs/xo/blob/main/.gitignore)[.gitignore](/xojs/xo/blob/main/.gitignore)[.npmrc](/xojs/xo/blob/main/.npmrc)[.npmrc](/xojs/xo/blob/main/.npmrc)[cli.ts](/xojs/xo/blob/main/cli.ts)[cli.ts](/xojs/xo/blob/main/cli.ts)[code-of-conduct.md](/xojs/xo/blob/main/code-of-conduct.md)[code-of-conduct.md](/xojs/xo/blob/main/code-of-conduct.md)[contributing.md](/xojs/xo/blob/main/contributing.md)[contributing.md](/xojs/xo/blob/main/contributing.md)[index.ts](/xojs/xo/blob/main/index.ts)[index.ts](/xojs/xo/blob/main/index.ts)[license](/xojs/xo/blob/main/license)[license](/xojs/xo/blob/main/license)[package.json](/xojs/xo/blob/main/package.json)[package.json](/xojs/xo/blob/main/package.json)[readme.md](/xojs/xo/blob/main/readme.md)[readme.md](/xojs/xo/blob/main/readme.md)[tsconfig.json](/xojs/xo/blob/main/tsconfig.json)[tsconfig.json](/xojs/xo/blob/main/tsconfig.json)[types.d.ts](/xojs/xo/blob/main/types.d.ts)[types.d.ts](/xojs/xo/blob/main/types.d.ts)View all files

## Repository files navigation

- [README](#)
- [Code of conduct](#)
- [Contributing](#)
- [MIT license](#)

# 
/xojs/xo/blob/main/media/logo.svg

#

JavaScript/TypeScript linter (ESLint wrapper) with great defaults

https://codecov.io/gh/xojs/xo/branch/mainhttps://github.com/xojs/xo

Opinionated but configurable ESLint wrapper with lots of goodies included. Enforces strict and readable code. Never discuss code style on a pull request again! No decision-making. No `eslint.config.js` to manage. It just works!

It uses [ESLint](https://eslint.org) underneath, so issues regarding built-in rules should be opened over [there](https://github.com/eslint/eslint/issues).

XO requires your project to be [ESM](https://gist.github.com/sindresorhus/a39789f98801d908bbc7ff3ecc99d99c).

https://raw.githubusercontent.com/sindresorhus/eslint-formatter-pretty/main/screenshot.png

## Highlights

#highlights

- Beautiful output.
- Zero-config, but [configurable when needed](#config).
- Enforces readable code, because you read more code than you write.
- No need to specify file paths to lint as it lints all JS/TS files except for [commonly ignored paths](#ignores).
- [Flat config customization.](#config)
- [TypeScript supported by default.](#typescript)
- Includes many useful ESLint plugins, like [unicorn](https://github.com/sindresorhus/eslint-plugin-unicorn), [import-x](https://github.com/un-ts/eslint-plugin-import-x), [ava](https://github.com/avajs/eslint-plugin-ava), [n](https://github.com/eslint-community/eslint-plugin-n) and more.
- Caches results between runs for much better performance.
- Super simple to add XO to a project with [$ npm init xo](https://github.com/xojs/create-xo).
- Fix many issues automagically with `$ xo --fix`.
- Open all files with errors at the correct line in your editor with `$ xo --open`.
- Specify [indent](#space) and [semicolon](#semicolon) preferences easily without messing with the rule config.
- Optionally use the [Prettier](https://github.com/prettier/prettier) code style or turn off all Prettier rules with the `compat` option.
- Optionally use `eslint-config-xo-react` for easy JSX and React linting with zero config.
- Optionally use with ESLint [directly](#usage-as-an-eslint-configuration)
- Great [editor plugins](#editor-plugins).

## Install

#install

```
npm install xo --save-dev
```

You must install XO locally. You can run it directly with `$ npx xo`.

You'll need [eslint-config-xo-vue](https://github.com/ChocPanda/eslint-config-xo-vue#use-with-xo) for specific linting in a Vue app.

## Usage

#usage

```
$ xo --help

	Usage
		$ xo [<file|glob> ...]

	Options
		--fix             Automagically fix issues
		--reporter        Reporter to use
		--space           Use space indent instead of tabs [Default: 2]
		--config          Path to a XO configuration file
		--semicolon       Use semicolons [Default: true]
		--react           Include React specific parsing and xo-react linting rules [Default: false]
		--prettier        Format with prettier or turn off prettier-conflicted rules when set to 'compat' [Default: false]
		--print-config    Print the effective ESLint config for the given file
		--version         Print XO version
		--open            Open files with issues in your editor
		--quiet           Show only errors and no warnings
		--stdin           Validate/fix code from stdin
		--stdin-filename  Specify a filename for the --stdin option
		--ignore          Ignore pattern globs, can be set multiple times
		--cwd=<dir>       Working directory for files [Default: process.cwd()]

	Examples
		$ xo
		$ xo index.js
		$ xo *.js !foo.js
		$ xo --space
		$ xo --print-config=index.js
		$ echo 'const x=true' | xo --stdin --fix

	Tips
		- Add XO to your project with `npm init xo`.
		- Put options in xo.config.js instead of using flags so other tools can read it.
```

## Default code style

#default-code-style

Any of these can be [overridden](#rules) if necessary.

- Tab indentation [(or space)](#space)
- Semicolons [(or not)](#semicolon)
- Single-quotes
- [Trailing comma](https://medium.com/@nikgraf/why-you-should-enforce-dangling-commas-for-multiline-statements-d034c98e36f8) for multiline statements
- No unused variables
- Space after keyword `if (condition) {}`
- Always `===` instead of `==`

Check out an [example](/xojs/xo/blob/main/index.ts) and the [ESLint rules](https://github.com/xojs/eslint-config-xo/blob/main/index.js).

## Workflow

#workflow

The recommended workflow is to add XO locally to your project and run it with the tests.

Simply run `$ npm init xo` (with any options) to add XO to create an `xo.config.js`.

## Config

#config

You can configure XO options by creating an `xo.config.js` or an `xo.config.ts` file in the root directory of your project, or you can add an `xo` field to your `package.json`. XO supports all js/ts file extensions (js,cjs,mjs,ts,cts,mts) and popular framework extensions (vue,svelte,astro) automatically. A XO config is an extension of ESLint's Flat Config. Like ESLint, an XO config exports an array of XO config objects. XO config objects extend [ESLint Configuration Objects](https://eslint.org/docs/latest/use/configure/configuration-files#configuration-objects). This means all the available configuration params for ESLint also work for `XO`. However, `XO` enhances and adds extra params to the configuration objects to make them easier to work with.

### Config types

#config-types

XO exports the types `FlatXoConfig`, `XoConfigItem`, and other types for you to get TypeScript validation on your config files.

examples: `xo.config.js`

```
/** @type {import('xo').FlatXoConfig} */
const xoConfig = [...]
```

`xo.config.ts`

```
import {type FlatXoConfig} from 'xo';

const xoConfig: FlatXoConfig = [...]
```

```
export default [...] satisfies import('xo').FlatXoConfig
```

### files

#files

Type: `string | string[] | undefined`
 Default: `**/*.{js,cjs,mjs,jsx,ts,cts,mts,tsx,vue,svelte,astro}`

A glob or array of glob strings which the config object will apply. By default `XO` will apply the configuration to [all files](/xojs/xo/blob/main/lib/constants.ts).

Tip: If you are adding additional `@typescript-eslint` rules to your config, these rules will apply to JS files as well unless you separate them appropriately with the `files` option. `@typescript-eslint` rules set to `'off'` or `0`, however, will have no effect on JS linting.

### ignores

#ignores

Type: `string[]`

Some [paths](/xojs/xo/blob/main/lib/constants.ts) are ignored by default, including paths in `.gitignore`. Additional ignores can be added here.

Tip: For global ignores, keep `ignores` as the only key in the config item. You can optionally set a `name` property. Adding more properties will cause ignores to be scoped down to your files selection, which may have unexpected effects.

### space

#space

Type: `boolean | number`
 Default: `false`(tab indentation)

Set it to `true` to get 2-space indentation or specify the number of spaces.

This option exists for pragmatic reasons, but I would strongly recommend you read [“Why tabs are superior”](http://lea.verou.me/2012/01/why-tabs-are-clearly-superior/).

### semicolon

#semicolon

Type: `boolean`
 Default: `true`(Semicolons required)

Set it to `false` to enforce no-semicolon style.

### prettier

#prettier

Type: `boolean | 'compat'`
 Default: `false`

Format code with [Prettier](https://github.com/prettier/prettier).

[Prettier options](https://prettier.io/docs/en/options.html) will be based on your [Prettier config](https://prettier.io/docs/en/configuration.html). XO will then merge your options with its own defaults:

- [semi](https://prettier.io/docs/en/options.html#semicolons): based on [semicolon](#semicolon) option
- [useTabs](https://prettier.io/docs/en/options.html#tabs): based on [space](#space) option
- [tabWidth](https://prettier.io/docs/en/options.html#tab-width): based on [space](#space) option
- [singleQuote](https://prettier.io/docs/en/options.html#quotes): `true`
- [bracketSpacing](https://prettier.io/docs/en/options.html#bracket-spacing): `false`

To stick with Prettier's defaults, add this to your Prettier config:

```
export default {
	singleQuote: false,
	bracketSpacing: true,
};
```

If contradicting options are set for both Prettier and XO, an error will be thrown.

#### Compat

#compat

If the Prettier option is set to `compat`, instead of formatting your code automatically, XO will turn off all rules that conflict with Prettier code style and allow you to pass your formatting to the Prettier tool directly.

### react

#react

Type: `boolean`
 Default: `false`

Adds `eslint-plugin-react`, `eslint-plugin-react-hooks`, and `eslint-config-xo-react` to get all the React best practices applied automatically.

## TypeScript

#typescript

XO will automatically lint TypeScript files (`.ts`, `.mts`, `.cts`, and `.tsx`) with the rules defined in [eslint-config-xo-typescript#use-with-xo](https://github.com/xojs/eslint-config-xo-typescript#use-with-xo).

XO will handle the [@typescript-eslint/parser project option](https://typescript-eslint.io/packages/parser/#project) automatically even if you don't have a `tsconfig.json` in your project.

You can opt out of XO's automatic tsconfig handling by specifying your own `languageOptions.parserOptions.project`, `languageOptions.parserOptions.projectService`, or `languageOptions.parserOptions.tsconfigRootDir`. Files in a config with these properties will be excluded from automatic tsconfig handling.

## Usage as an ESLint Configuration

#usage-as-an-eslint-configuration

With the introduction of the ESLint flat config, many of the original goals of `xo` were brought into the ESLint core, and shareable configs with plugins became possible. Although we highly recommend the use of the `xo` cli, we understand that some teams need to rely on ESLint directly.

For these purposes, you can still get most of the features of `xo` by using our ESLint configuration helpers.

### xoToEslintConfig

#xotoeslintconfig

The `xoToEslintConfig` function is designed for use in an `eslint.config.js` file. It is NOT for use in an `xo.config.js` file. This function takes a `FlatXoConfig` and outputs an ESLint config object. This function will neither be able to automatically handle TS integration for you nor automatic Prettier integration. You are responsible for configuring your other tools appropriately. The `xo` cli, will, however, handle all of these details for you.

`eslint.config.js`

```
import xo from 'xo';

export default xo.xoToEslintConfig([{space: true, prettier: 'compat'}]);
```

## Tips

#tips

### Monorepo

#monorepo

Put a `xo.config.js` with your config at the root and do not add a config to any of your bundled packages.

### Including files ignored by default

#including-files-ignored-by-default

To include files that XO [ignores by default](/xojs/xo/blob/main/lib/constants.ts), add them as negative globs in the [ignores option](#ignores):

```
const xoConfig = [{ignores: ['!vendor/**']}];

export default xoConfig;
```

## FAQ

#faq

#### What does XO mean?

#what-does-xo-mean

It means [hugs and kisses](https://en.wiktionary.org/wiki/xoxo).

#### Why not Standard?

#why-not-standard

The [Standard style](https://standardjs.com) is a really cool idea. I too wish we could have one style to rule them all! But the reality is that the JS community is just too diverse and opinionated to create one code style. They also made the mistake of pushing their own style instead of the most popular one. In contrast, XO is more pragmatic and has no aspiration of being the style. My goal with XO is to make it simple to enforce consistent code style with close to no config. XO comes with my code style preference by default, as I mainly made it for myself, but everything is configurable.

#### Why not ESLint?

#why-not-eslint

XO is based on ESLint. This project started out as just a shareable ESLint config, but it quickly grew out of that. I wanted something even simpler. Just typing `xo` and be done. No decision-making. No config. I also have some exciting future plans for it. However, you can still get most of the XO benefits while using ESLint directly with the [ESLint shareable config](https://github.com/xojs/eslint-config-xo).

## Editor plugins

#editor-plugins

- [Sublime Text](https://github.com/xojs/SublimeLinter-contrib-xo)
- [Atom](https://github.com/xojs/atom-linter-xo)
- [Vim](https://github.com/xojs/vim-xo)
- [TextMate 2](https://github.com/claylo/XO.tmbundle)
- [VSCode](https://github.com/SamVerschueren/vscode-linter-xo)
- [Emacs](https://github.com/j-em/xo-emacs)
- [WebStorm](https://github.com/jamestalmage/xo-with-webstorm)

## Build-system plugins

#build-system-plugins

- [Gulp](https://github.com/xojs/gulp-xo)
- [Grunt](https://github.com/xojs/grunt-xo)
- [webpack loader](https://github.com/Semigradsky/xo-loader)
- [webpack plugin](https://github.com/nstanard/xo-webpack-plugin)
- [Metalsmith](https://github.com/blainsmith/metalsmith-xo)
- [Fly](https://github.com/lukeed/fly-xo)

## Configs

#configs

- [eslint-config-xo](https://github.com/xojs/eslint-config-xo) - ESLint shareable config for XO with tab indent
- [eslint-config-xo-space](https://github.com/xojs/eslint-config-xo-space) - ESLint shareable config for XO with 2-space indent
- [eslint-config-xo-react](https://github.com/xojs/eslint-config-xo-react) - ESLint shareable config for React to be used with the above
- [eslint-config-xo-vue](https://github.com/ChocPanda/eslint-config-xo-vue) - ESLint shareable config for Vue to be used with the above
- [stylelint-config-xo](https://github.com/xojs/stylelint-config-xo) - Stylelint shareable config for XO with tab indent
- [stylelint-config-xo-space](https://github.com/xojs/stylelint-config-xo-space) - Stylelint shareable config for XO with 2-space indent
- [eslint-config-xo-typescript](https://github.com/xojs/eslint-config-xo-typescript) - ESLint shareable config for TypeScript

## Support

#support

- [Twitter](https://twitter.com/sindresorhus)

## Related

#related

- [eslint-plugin-unicorn](https://github.com/sindresorhus/eslint-plugin-unicorn) - Various awesome ESLint rules (Bundled in XO)
- [xo-summary](https://github.com/LitoMore/xo-summary) - Display output from `xo` as a list of style errors, ordered by count

## Badge

#badge

Show the world you're using XO → https://github.com/xojs/xo

```
[![XO code style](https://shields.io/badge/code_style-5ed9c7?logo=xo&labelColor=gray&logoSize=auto)](https://github.com/xojs/xo)
```

Or [customize the badge](https://github.com/xojs/xo/issues/689#issuecomment-1253127616).

You can also find some nice dynamic XO badges on [badgen.net](https://badgen.net/#xo).

## Team

#team

- [Sindre Sorhus](https://github.com/sindresorhus)

###### Former

#former

- [James Talmage](https://github.com/jamestalmage)
- [Michael Mayer](https://github.com/schnittstabil)
- [Mario Nebl](https://github.com/marionebl)
- [Pierre Vanduynslager](https://github.com/pvdlg)

## About

 ❤️ JavaScript/TypeScript linter (ESLint wrapper) with great defaults 

### Topics

[nodejs](/topics/nodejs)[eslint](/topics/eslint)[style-linter](/topics/style-linter)[eslint-plugin](/topics/eslint-plugin)[best-practices](/topics/best-practices)[linter](/topics/linter)[unicorns](/topics/unicorns)[shareable-configs](/topics/shareable-configs)[eslint-rules](/topics/eslint-rules)[xo](/topics/xo)[code-style](/topics/code-style)

### Resources

[Readme](#readme-ov-file)

### License

[MIT license](#MIT-1-ov-file)

### Code of conduct

[Code of conduct](#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

###  Uh oh! 

There was an error while loading. Please reload this page.

[Activity](/xojs/xo/activity)[Custom properties](/xojs/xo/custom-properties)

### Stars

[7.9k
        stars](/xojs/xo/stargazers)

### Watchers

[55
        watching](/xojs/xo/watchers)

### Forks

[301
        forks](/xojs/xo/forks)[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fxojs%2Fxo&report=xojs+%28user%29)

## [Releases
      98](/xojs/xo/releases)

[v1.2.3
        
          Latest
      
      Oct 7, 2025](/xojs/xo/releases/tag/v1.2.3)[+ 97 releases](/xojs/xo/releases)

## Sponsor this project

 Sponsor 

###  Uh oh! 

There was an error while loading. Please reload this page.

[Learn more about GitHub Sponsors](/sponsors)

## [Packages
      0](/orgs/xojs/packages?repo_name=xo)

 No packages published 

## [Used by 53k](/xojs/xo/network/dependents)

- 
- 
- 
- 

[+ 53,006](/xojs/xo/network/dependents)

## [Contributors
      93](/xojs/xo/graphs/contributors)

- https://github.com/sindresorhus
- https://github.com/pvdlg
- https://github.com/spence-s
- https://github.com/fisker
- https://github.com/jamestalmage
- https://github.com/kevva
- https://github.com/fregante
- https://github.com/schnittstabil
- https://github.com/LitoMore
- https://github.com/Richienb
- https://github.com/marionebl
- https://github.com/coreyfarrell
- https://github.com/andersk
- https://github.com/kevinastone

[+ 79 contributors](/xojs/xo/graphs/contributors)

## Languages

- [TypeScript
          94.5%](/xojs/xo/search?l=typescript)
- [JavaScript
          5.5%](/xojs/xo/search?l=javascript)
