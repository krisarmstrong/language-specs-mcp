## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Prefer to wrap `<tr>` inside `<tbody>`

Rule ID:prefer-tbodyCategory:StyleStandards:-

While `<tbody>` is optional is relays semantic information about its contents.

Where applicable it should also be combined with `<thead>` and `<tfoot>`.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<table>
	<tr><td>...</td></tr>
</table>
```

```
error: Prefer to wrap <tr> elements in <tbody> (prefer-tbody) at inline:2:3:
  1 | <table>
> 2 | 	<tr><td>...</td></tr>
    | 	 ^^
  3 | </table>

1 error found.
```

Examples of correct code for this rule:

```
<table>
	<tbody>
		<tr><td>...</td></tr>
	</tbody>
</table>
```
