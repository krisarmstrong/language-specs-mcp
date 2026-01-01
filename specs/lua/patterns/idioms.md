# Lua Idioms

## Use local scope

```lua
local count = 0
```

## Prefer ipairs/pairs

```lua
for i, v in ipairs(items) do
  print(i, v)
end
```
