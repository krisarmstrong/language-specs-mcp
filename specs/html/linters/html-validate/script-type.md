## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require valid type for `<script>` element

Rule ID:script-typeCategory:HTML syntax and conceptsStandards:

- HTML5

The [HTML5 standard encourages](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-type) omitting the `type` attribute when the script is a JavaScript resource and only use it to specify `module` or other non-javascript MIME types.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<script type=""></script>
<script type="text/javascript"></script>
<script type="application/javascript"></script>
```

```
error: "type" attribute is unnecessary for javascript resources (script-type) at inline:1:9:
> 1 | <script type=""></script>
    |         ^^^^
  2 | <script type="text/javascript"></script>
  3 | <script type="application/javascript"></script>

error: "type" attribute is unnecessary for javascript resources (script-type) at inline:2:9:
  1 | <script type=""></script>
> 2 | <script type="text/javascript"></script>
    |         ^^^^
  3 | <script type="application/javascript"></script>

error: "type" attribute is unnecessary for javascript resources (script-type) at inline:3:9:
  1 | <script type=""></script>
  2 | <script type="text/javascript"></script>
> 3 | <script type="application/javascript"></script>
    |         ^^^^

3 errors found.
```

Examples of correct code for this rule:

```
<script></script>
<script type="module"></script>
<script type="text/plain"></script>
<script type="text/x-custom"></script>
```
