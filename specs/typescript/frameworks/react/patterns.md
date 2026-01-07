# React Patterns & Best Practices

## Component Structure

### Functional Components (Preferred)

```tsx
// GOOD - Modern functional component
interface UserCardProps {
  user: User;
  onSelect: (id: string) => void;
}

export function UserCard({ user, onSelect }: UserCardProps) {
  const handleClick = useCallback(() => {
    onSelect(user.id);
  }, [user.id, onSelect]);

  return (
    <div className="user-card" onClick={handleClick}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
    </div>
  );
}
```

### Custom Hooks for Logic Reuse

```tsx
// Extract reusable logic into custom hooks
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}

// Usage
function SearchInput() {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query, 300);

  useEffect(() => {
    if (debouncedQuery) {
      searchAPI(debouncedQuery);
    }
  }, [debouncedQuery]);

  return <input value={query} onChange={(e) => setQuery(e.target.value)} />;
}
```

## State Management

### useState for Simple State

```tsx
// GOOD - Simple, local state
const [isOpen, setIsOpen] = useState(false);
const [items, setItems] = useState<Item[]>([]);
```

### useReducer for Complex State

```tsx
// GOOD - Complex state logic
type State = { items: Item[]; loading: boolean; error: string | null };
type Action =
  | { type: "FETCH_START" }
  | { type: "FETCH_SUCCESS"; items: Item[] }
  | { type: "FETCH_ERROR"; error: string };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case "FETCH_START":
      return { ...state, loading: true, error: null };
    case "FETCH_SUCCESS":
      return { ...state, loading: false, items: action.items };
    case "FETCH_ERROR":
      return { ...state, loading: false, error: action.error };
  }
}

function ItemList() {
  const [state, dispatch] = useReducer(reducer, {
    items: [],
    loading: false,
    error: null,
  });
  // ...
}
```

## Performance Optimization

### Memoization

```tsx
// useMemo for expensive computations
const sortedItems = useMemo(
  () => items.slice().sort((a, b) => a.name.localeCompare(b.name)),
  [items]
);

// useCallback for stable function references
const handleSubmit = useCallback(
  (data: FormData) => {
    onSubmit(data);
  },
  [onSubmit]
);

// React.memo for component memoization
const ExpensiveComponent = memo(function ExpensiveComponent({ data }: Props) {
  return <div>{/* expensive render */}</div>;
});
```

### Avoid Unnecessary Re-renders

```tsx
// BAD - Creates new object every render
<Component style={{ color: "red" }} />

// GOOD - Stable reference
const style = useMemo(() => ({ color: "red" }), []);
<Component style={style} />

// BAD - Creates new function every render
<Button onClick={() => handleClick(id)} />

// GOOD - Stable callback
const handleButtonClick = useCallback(() => handleClick(id), [id, handleClick]);
<Button onClick={handleButtonClick} />
```

## Error Handling

### Error Boundaries

```tsx
class ErrorBoundary extends Component<Props, State> {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    logErrorToService(error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback error={this.state.error} />;
    }
    return this.props.children;
  }
}

// Usage
<ErrorBoundary>
  <MyComponent />
</ErrorBoundary>
```

## Data Fetching

### useEffect with Cleanup

```tsx
function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;

    async function fetchUser() {
      setLoading(true);
      try {
        const data = await api.getUser(userId);
        if (!cancelled) {
          setUser(data);
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    fetchUser();

    return () => {
      cancelled = true;
    };
  }, [userId]);

  if (loading) return <Spinner />;
  if (!user) return <NotFound />;
  return <UserCard user={user} />;
}
```

## Anti-Patterns to Avoid

### Don't Mutate State Directly

```tsx
// BAD
const [items, setItems] = useState([1, 2, 3]);
items.push(4); // Mutation!
setItems(items);

// GOOD
setItems([...items, 4]);
```

### Don't Call Hooks Conditionally

```tsx
// BAD
if (condition) {
  const [value, setValue] = useState(0); // Hook in conditional!
}

// GOOD
const [value, setValue] = useState(0);
// Use value conditionally instead
```

### Don't Use Index as Key for Dynamic Lists

```tsx
// BAD - Index keys cause issues with reordering
{
  items.map((item, index) => <Item key={index} {...item} />);
}

// GOOD - Use stable, unique identifier
{
  items.map((item) => <Item key={item.id} {...item} />);
}
```

### Don't Over-use Context

```tsx
// BAD - Too much in one context
const AppContext = createContext({
  user: null,
  theme: "light",
  notifications: [],
  cart: [],
  settings: {},
  // ... everything else
});

// GOOD - Separate contexts by concern
const UserContext = createContext<User | null>(null);
const ThemeContext = createContext<Theme>("light");
const CartContext = createContext<CartState>(initialCart);
```
