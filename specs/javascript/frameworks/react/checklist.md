# React Generation Checklist

**Read this BEFORE generating React code. These are mistakes you WILL make otherwise.**

## Critical Rules

### 1. Never Mutate State Directly
```jsx
// BAD - Mutates state, React won't re-render
const [items, setItems] = useState([]);
items.push(newItem);  // WRONG
setItems(items);      // Still wrong - same reference

// GOOD - Create new array
setItems([...items, newItem]);
setItems(prev => [...prev, newItem]);
```

### 2. Dependencies Array in useEffect
```jsx
// BAD - Runs on every render (infinite loop risk)
useEffect(() => {
  fetchData();
});

// BAD - Missing dependency
useEffect(() => {
  fetchData(userId);
}, []);  // userId is missing!

// GOOD - All dependencies listed
useEffect(() => {
  fetchData(userId);
}, [userId]);
```

### 3. Stable References for Callbacks
```jsx
// BAD - New function every render, breaks memoization
<MemoizedChild onClick={() => handleClick(id)} />

// GOOD - Stable reference
const handleItemClick = useCallback(() => {
  handleClick(id);
}, [id, handleClick]);
<MemoizedChild onClick={handleItemClick} />
```

### 4. Keys Must Be Stable and Unique
```jsx
// BAD - Index as key (breaks on reorder/filter)
{items.map((item, index) => <Item key={index} {...item} />)}

// GOOD - Stable unique identifier
{items.map(item => <Item key={item.id} {...item} />)}
```

### 5. Cleanup Effects
```jsx
// BAD - Memory leak
useEffect(() => {
  const sub = subscribe(callback);
  // No cleanup!
}, []);

// GOOD - Cleanup on unmount
useEffect(() => {
  const sub = subscribe(callback);
  return () => sub.unsubscribe();
}, [callback]);
```

### 6. Async Effects Need Cancellation
```jsx
// GOOD - Cancel stale requests
useEffect(() => {
  const controller = new AbortController();
  fetch(url, { signal: controller.signal })
    .then(res => res.json())
    .then(setData);
  return () => controller.abort();
}, [url]);
```

### 7. Conditional Hooks Are Forbidden
```jsx
// BAD - Hooks must be unconditional
if (isLoggedIn) {
  const [user] = useState(null);  // FORBIDDEN
}

// GOOD - Always call, conditionally use result
const [user] = useState(null);
```

### 8. Derive State, Don't Sync It
```jsx
// BAD - Extra state and render
const [items, setItems] = useState([]);
const [filtered, setFiltered] = useState([]);
useEffect(() => setFiltered(items.filter(x => x.active)), [items]);

// GOOD - Derive during render
const filtered = useMemo(() => items.filter(x => x.active), [items]);
```

## Performance Checklist
- [ ] Large lists use virtualization (react-window)
- [ ] Expensive computations wrapped in useMemo
- [ ] Callbacks wrapped in useCallback when passed to memo children
- [ ] Components split to minimize re-render scope

## Security Checklist
- [ ] Sanitize HTML before rendering raw content
- [ ] URLs validated before use in href/src
- [ ] Sensitive data not in localStorage
- [ ] CSRF tokens in forms

## TypeScript
```tsx
interface Props { title: string; children: React.ReactNode; }
const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {};
const inputRef = useRef<HTMLInputElement>(null);
```
