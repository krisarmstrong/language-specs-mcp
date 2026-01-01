# JavaScript Idioms

## Prefer const/let over var

```javascript
const id = "abc";
let count = 0;
```

## Use async/await for async control flow

```javascript
const data = await fetch(url).then((res) => res.json());
```

## Avoid implicit globals

```javascript
"use strict";
```
