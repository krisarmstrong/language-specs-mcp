## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Require elements to be closed in correct order

Rule ID:close-orderCategory:HTML syntax and conceptsStandards:

- HTML5

HTML requires elements to be closed in the correct order.

## [Rule details](#rule-details)

Examples of incorrect code for this rule:

```
<main>
		<label>Lorem ipsum</label>
	</div> <!-- div closed but never opened -->
</main>
```

```
error: Stray end tag '</div>' (close-order) at inline:3:3:
  1 | <main>
  2 | 		<label>Lorem ipsum</label>
> 3 | 	</div> <!-- div closed but never opened -->
    | 	 ^^^^
  4 | </main>

1 error found.
```

```
<main>
	<h1> <!-- h1 opened but not closed -->
		Lorem ipsum <small>dolor sit amet</small>
</main>
```

```
error: Unclosed element '<h1>' (close-order) at inline:2:3:
  1 | <main>
> 2 | 	<h1> <!-- h1 opened but not closed -->
    | 	 ^^
  3 | 		Lorem ipsum <small>dolor sit amet</small>
  4 | </main>

error: End tag '</main>' seen but there were open elements (close-order) at inline:4:2:
  2 | 	<h1> <!-- h1 opened but not closed -->
  3 | 		Lorem ipsum <small>dolor sit amet</small>
> 4 | </main>
    |  ^^^^^

2 errors found.
```

```
<main>
	<h1>
		Lorem ipsum <small>dolor sit amet</small>
	</h1>
</div> <!-- opened as main but closed as div -->
```

```
error: Unclosed element '<main>' (close-order) at inline:1:2:
> 1 | <main>
    |  ^^^^
  2 | 	<h1>
  3 | 		Lorem ipsum <small>dolor sit amet</small>
  4 | 	</h1>

error: Stray end tag '</div>' (close-order) at inline:5:2:
  3 | 		Lorem ipsum <small>dolor sit amet</small>
  4 | 	</h1>
> 5 | </div> <!-- opened as main but closed as div -->
    |  ^^^^

2 errors found.
```

```
<div>
	<!-- closed in wrong order -->
	<p>
		<strong>
	</p>
		</strong>
</div>
```

```
error: Unclosed element '<strong>' (close-order) at inline:4:4:
  2 | 	<!-- closed in wrong order -->
  3 | 	<p>
> 4 | 		<strong>
    | 		 ^^^^^^
  5 | 	</p>
  6 | 		</strong>
  7 | </div>

error: End tag '</p>' seen but there were open elements (close-order) at inline:5:3:
  3 | 	<p>
  4 | 		<strong>
> 5 | 	</p>
    | 	 ^^
  6 | 		</strong>
  7 | </div>

2 errors found.
```

```
<p>
	<address></address>
</p> <!-- p is already implicitly closed by address tag -->
```

```
error: Stray end tag '</p>' (close-order) at inline:3:2:
  1 | <p>
  2 | 	<address></address>
> 3 | </p> <!-- p is already implicitly closed by address tag -->
    |  ^^

1 error found.
```

Examples of correct code for this rule:

```
<p><strong></strong></p>
```

```
<div></div>
```
