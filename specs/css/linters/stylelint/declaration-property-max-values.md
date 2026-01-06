On this page

# declaration-property-max-values

Limit the number of values for a list of properties within declarations.

## Options[​](#options)

### `Object<string, number>`[​](#objectstring-number)

```
{ "unprefixed-property-name": 0 }
```

Specify pairs of a property and a max value. In practice, you should specify any positive integers as max values.

You can specify a regex for a property name, such as `{ "/^margin/": 0 }`.

Given:

```
{
  "declaration-property-max-values": {
    "border": 2,
    "/^margin/": 1
  }
}
```

The following patterns are considered problems:

```
a { border: 1px solid blue; }
```

```
a { margin: 1px 2px; }
```

```
a { margin-inline: 1px 2px; }
```

The following patterns are not considered problems:

```
a { border: 1px solid; }
```

```
a { margin: 1px; }
```

```
a { margin-inline: 1px; }
```

[Previousdeclaration-no-important](/user-guide/rules/declaration-no-important)[Nextdeclaration-property-unit-allowed-list](/user-guide/rules/declaration-property-unit-allowed-list)

- [Options](#options)

  - [Object<string, number>](#objectstring-number)
