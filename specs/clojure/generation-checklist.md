# Clojure Generation Checklist

**Read this BEFORE writing Clojure code. Embrace immutability and functional design.**

## Critical: You Must Do These

### 1. Prefer Pure Functions
```clojure
;; BAD - side effects mixed with logic
(defn process-user [user]
  (println "Processing user")  ; Side effect!
  (db/save! user)              ; Side effect!
  (transform user))

;; GOOD - separate pure logic from side effects
(defn transform-user [user]
  (-> user
      (assoc :processed true)
      (update :name str/upper-case)))

(defn process-user! [user]
  (let [transformed (transform-user user)]
    (db/save! transformed)))
```

### 2. Use Threading Macros for Readability
```clojure
;; BAD - nested function calls
(filter even? (map inc (take 10 (range))))

;; GOOD - threading macro
(->> (range)
     (take 10)
     (map inc)
     (filter even?))

;; Use -> for object-first operations
(-> user
    (assoc :active true)
    (update :login-count inc))
```

### 3. Destructure in Function Parameters
```clojure
;; BAD - manual extraction
(defn greet [user]
  (let [name (:name user)
        age (:age user)]
    (str "Hello, " name)))

;; GOOD - destructure in parameters
(defn greet [{:keys [name age]}]
  (str "Hello, " name))

;; With defaults
(defn greet [{:keys [name age] :or {age 0}}]
  (str "Hello, " name " (age: " age ")"))
```

### 4. Use Keywords for Map Keys
```clojure
;; BAD - string keys
{"name" "Alice" "age" 30}

;; GOOD - keyword keys
{:name "Alice" :age 30}

;; Keywords are functions
(:name user)  ; => "Alice"
```

### 5. Handle Nil Explicitly
```clojure
;; BAD - nil propagation causes issues
(defn get-upper-name [user]
  (.toUpperCase (:name user)))  ; NPE if name is nil!

;; GOOD - use some-> for nil-safe chaining
(defn get-upper-name [user]
  (some-> user :name str/upper-case))

;; GOOD - use fnil for default values
(defn safe-inc [x]
  ((fnil inc 0) x))
```

## Important: Strong Recommendations

### 6. Use `let` for Local Bindings
```clojure
;; GOOD - clear intermediate values
(defn calculate-total [items]
  (let [prices (map :price items)
        subtotal (reduce + prices)
        tax (* subtotal 0.1)]
    (+ subtotal tax)))
```

### 7. Use `cond` for Multiple Conditions
```clojure
;; BAD - nested if
(if (< x 0)
  "negative"
  (if (= x 0)
    "zero"
    "positive"))

;; GOOD - cond
(cond
  (< x 0) "negative"
  (= x 0) "zero"
  :else   "positive")
```

### 8. Use Multimethods for Polymorphism
```clojure
;; GOOD - dispatch on type
(defmulti process-event :type)

(defmethod process-event :user-created
  [{:keys [user]}]
  (send-welcome-email user))

(defmethod process-event :order-placed
  [{:keys [order]}]
  (process-order order))

(defmethod process-event :default
  [event]
  (log/warn "Unknown event type" event))
```

### 9. Use Protocols for Type-Based Dispatch
```clojure
;; GOOD - protocol for shared behavior
(defprotocol Serializable
  (to-json [this])
  (from-json [this data]))

(defrecord User [id name email]
  Serializable
  (to-json [this]
    (json/write-str this))
  (from-json [this data]
    (map->User (json/read-str data :key-fn keyword))))
```

### 10. Use Records for Domain Entities
```clojure
;; BAD - plain maps for everything
(def user {:id 1 :name "Alice"})

;; GOOD - records for domain entities
(defrecord User [id name email])

(def user (->User 1 "Alice" "alice@test.com"))
;; Or with map syntax
(def user (map->User {:id 1 :name "Alice" :email "alice@test.com"}))
```

## Functional Patterns

### 11. Use `reduce` for Accumulation
```clojure
;; GOOD - reduce with initial value
(defn sum-prices [items]
  (reduce (fn [total item]
            (+ total (:price item)))
          0
          items))

;; GOOD - using +
(reduce + 0 (map :price items))
```

### 12. Use `comp` for Function Composition
```clojure
;; GOOD - compose functions
(def process-name
  (comp str/upper-case str/trim))

(process-name "  alice  ")  ; => "ALICE"

;; Equivalent to
(defn process-name [s]
  (-> s str/trim str/upper-case))
```

### 13. Use `partial` for Partial Application
```clojure
;; GOOD - partial application
(def add-ten (partial + 10))
(add-ten 5)  ; => 15

(def greet-hello (partial str "Hello, "))
(greet-hello "World")  ; => "Hello, World"
```

### 14. Use Transducers for Efficient Transformations
```clojure
;; BAD - multiple intermediate collections
(->> data
     (map transform)
     (filter valid?)
     (take 10))

;; GOOD - transducer (single pass, no intermediate collections)
(into []
      (comp
        (map transform)
        (filter valid?)
        (take 10))
      data)
```

## Concurrency

### 15. Use Atoms for Shared State
```clojure
;; GOOD - atomic state updates
(def counter (atom 0))

(swap! counter inc)        ; Increment atomically
(swap! counter + 10)       ; Add 10 atomically
(reset! counter 0)         ; Reset to 0
@counter                   ; Dereference to get value
```

### 16. Use Refs and STM for Coordinated State
```clojure
;; GOOD - coordinated updates
(def account-a (ref 100))
(def account-b (ref 200))

(defn transfer [from to amount]
  (dosync
    (alter from - amount)
    (alter to + amount)))
```

### 17. Use `future` for Async Work
```clojure
;; GOOD - async computation
(def result (future (expensive-computation)))

;; Blocks until complete
@result

;; With timeout
(deref result 5000 :timeout)
```

---

**Quick Reference - Copy This Mental Model:**
- Pure functions, separate side effects
- Threading macros (`->`, `->>`)
- Destructure in parameters
- Keywords for map keys
- `some->` for nil safety
- `cond` over nested `if`
- Multimethods for polymorphism
- Records for domain entities
- `reduce` for accumulation
- Transducers for efficiency
- Atoms for shared state
- `future` for async
