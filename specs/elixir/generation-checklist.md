# Elixir Generation Checklist

**Read this BEFORE writing Elixir code. Embrace immutability and pattern matching.**

## Critical: You Must Do These

### 1. Use Pattern Matching Everywhere
```elixir
# BAD - imperative style
def process(user) do
  if user != nil do
    if user.active do
      # do work
    end
  end
end

# GOOD - pattern matching
def process(%User{active: true} = user) do
  # do work with active user
end

def process(%User{active: false}) do
  {:error, :inactive_user}
end

def process(nil) do
  {:error, :no_user}
end
```

### 2. Use the Pipe Operator for Data Transformation
```elixir
# BAD - nested function calls
String.downcase(String.trim(String.replace(input, "  ", " ")))

# GOOD - pipe operator
input
|> String.replace("  ", " ")
|> String.trim()
|> String.downcase()
```

### 3. Return Tagged Tuples for Results
```elixir
# BAD - returning nil or raising
def find_user(id) do
  # returns nil if not found - caller might forget to check
end

# GOOD - tagged tuples
def find_user(id) do
  case Repo.get(User, id) do
    nil -> {:error, :not_found}
    user -> {:ok, user}
  end
end

# GOOD - handle with case or with
case find_user(id) do
  {:ok, user} -> process(user)
  {:error, reason} -> handle_error(reason)
end
```

### 4. Use `with` for Happy Path
```elixir
# BAD - nested case statements
case fetch_user(id) do
  {:ok, user} ->
    case validate_user(user) do
      {:ok, valid_user} ->
        case save_user(valid_user) do
          {:ok, saved} -> {:ok, saved}
          {:error, reason} -> {:error, reason}
        end
      {:error, reason} -> {:error, reason}
    end
  {:error, reason} -> {:error, reason}
end

# GOOD - with statement
with {:ok, user} <- fetch_user(id),
     {:ok, valid_user} <- validate_user(user),
     {:ok, saved} <- save_user(valid_user) do
  {:ok, saved}
else
  {:error, reason} -> {:error, reason}
end
```

### 5. Always Handle All Message Types in GenServer
```elixir
# GOOD - handle unknown messages
def handle_info(msg, state) do
  Logger.warning("Unknown message: #{inspect(msg)}")
  {:noreply, state}
end

def handle_call(msg, _from, state) do
  Logger.warning("Unknown call: #{inspect(msg)}")
  {:reply, {:error, :unknown_call}, state}
end
```

## Important: Strong Recommendations

### 6. Use Structs for Domain Data
```elixir
# BAD - plain maps with typo risk
user = %{naem: "Alice"}  # Typo goes unnoticed

# GOOD - struct with defined keys
defmodule User do
  defstruct [:id, :name, :email, :active]
end

user = %User{name: "Alice"}  # Compiler warns about unknown keys
```

### 7. Use Module Attributes for Constants
```elixir
# BAD - magic values scattered in code
def timeout, do: 5000

# GOOD - module attribute
@default_timeout 5_000

def timeout, do: @default_timeout
```

### 8. Use Guards for Type Validation
```elixir
# BAD - runtime type checking
def process(value) do
  if is_integer(value) do
    # ...
  end
end

# GOOD - guards
def process(value) when is_integer(value) and value > 0 do
  # Only matches positive integers
end

def process(value) when is_binary(value) do
  # Only matches strings
end
```

### 9. Prefer Keyword Lists for Options
```elixir
# GOOD - keyword list for options
def fetch(url, opts \\ []) do
  timeout = Keyword.get(opts, :timeout, 5_000)
  headers = Keyword.get(opts, :headers, [])
  # ...
end

fetch("http://example.com", timeout: 10_000, headers: [{"Accept", "application/json"}])
```

### 10. Use Stream for Large Collections
```elixir
# BAD - loads everything into memory
File.read!("large.csv")
|> String.split("\n")
|> Enum.map(&parse_line/1)
|> Enum.filter(&valid?/1)

# GOOD - lazy streaming
File.stream!("large.csv")
|> Stream.map(&parse_line/1)
|> Stream.filter(&valid?/1)
|> Enum.to_list()  # Only materializes at the end
```

## OTP Patterns

### 11. Use Supervisors for Fault Tolerance
```elixir
# GOOD - supervised processes
defmodule MyApp.Application do
  use Application

  def start(_type, _args) do
    children = [
      {MyApp.Worker, []},
      {MyApp.Cache, []}
    ]

    opts = [strategy: :one_for_one, name: MyApp.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

### 12. Use GenServer for Stateful Processes
```elixir
defmodule Counter do
  use GenServer

  # Client API
  def start_link(initial) do
    GenServer.start_link(__MODULE__, initial, name: __MODULE__)
  end

  def increment do
    GenServer.call(__MODULE__, :increment)
  end

  # Server Callbacks
  @impl true
  def init(initial), do: {:ok, initial}

  @impl true
  def handle_call(:increment, _from, count) do
    {:reply, count + 1, count + 1}
  end
end
```

### 13. Use Task for One-Off Async Work
```elixir
# GOOD - async task with supervision
task = Task.Supervisor.async(MyApp.TaskSupervisor, fn ->
  expensive_operation()
end)

result = Task.await(task, 30_000)
```

## Testing

### 14. Use ExUnit Tags for Test Organization
```elixir
# GOOD - tagged tests
@tag :integration
test "connects to database" do
  # ...
end

@tag :slow
test "processes large file" do
  # ...
end

# Run only fast tests: mix test --exclude slow
```

### 15. Use Mox for Mocking
```elixir
# In test_helper.exs
Mox.defmock(MyApp.HTTPClientMock, for: MyApp.HTTPClient)

# In tests
test "handles API error" do
  expect(MyApp.HTTPClientMock, :get, fn _url ->
    {:error, :timeout}
  end)

  assert {:error, :api_unavailable} = MyApp.fetch_data()
end
```

---

**Quick Reference - Copy This Mental Model:**
- Pattern matching everywhere
- Pipe operator for transformations
- Tagged tuples `{:ok, value}` / `{:error, reason}`
- `with` for happy path
- Structs for domain data
- Guards for type validation
- Stream for large collections
- Supervisors for fault tolerance
- GenServer for state
- Task for async work
