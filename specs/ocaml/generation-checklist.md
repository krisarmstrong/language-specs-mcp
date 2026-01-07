# OCaml Generation Checklist

**Read this BEFORE writing OCaml code. Let the type system work for you.**

## Critical: You Must Do These

### 1. Use Pattern Matching Exhaustively
```ocaml
(* BAD - non-exhaustive warning *)
let describe_status status =
  match status with
  | Active -> "Active"
  | Pending -> "Pending"
  (* Missing: Completed, Failed *)

(* GOOD - exhaustive matching *)
let describe_status status =
  match status with
  | Active -> "Active"
  | Pending -> "Pending"
  | Completed -> "Completed"
  | Failed -> "Failed"

(* If you must have a catch-all, be explicit about intent *)
let describe_status status =
  match status with
  | Active -> "Active"
  | Pending -> "Pending"
  | _ -> "Other"  (* Document why this is OK *)
```

### 2. Use Option Instead of Exceptions for Expected Cases
```ocaml
(* BAD - exception for normal control flow *)
let find_user id =
  if id_exists id then get_user id
  else raise Not_found

(* GOOD - Option for expected absence *)
let find_user id : user option =
  if id_exists id then Some (get_user id)
  else None

(* Use Result for errors with information *)
let find_user id : (user, string) result =
  if id_exists id then Ok (get_user id)
  else Error (Printf.sprintf "User %d not found" id)
```

### 3. Make Invalid States Unrepresentable
```ocaml
(* BAD - allows invalid combinations *)
type user = {
  name: string;
  email: string option;
  email_verified: bool;  (* What if email is None? *)
}

(* GOOD - impossible to have invalid state *)
type email_status =
  | NoEmail
  | Unverified of string
  | Verified of string

type user = {
  name: string;
  email: email_status;
}
```

### 4. Use Type Annotations for Module Boundaries
```ocaml
(* GOOD - explicit types at module boundaries *)
module User : sig
  type t
  val create : string -> string -> t
  val name : t -> string
  val email : t -> string
end = struct
  type t = { name: string; email: string }
  let create name email = { name; email }
  let name u = u.name
  let email u = u.email
end
```

### 5. Avoid Mutable State When Possible
```ocaml
(* BAD - mutable accumulator *)
let sum_list lst =
  let total = ref 0 in
  List.iter (fun x -> total := !total + x) lst;
  !total

(* GOOD - functional fold *)
let sum_list lst =
  List.fold_left ( + ) 0 lst

(* BAD - in-place mutation *)
let arr = [| 1; 2; 3 |]
let () = arr.(0) <- 10

(* GOOD - immutable data structures *)
let lst = [1; 2; 3]
let new_lst = 10 :: List.tl lst
```

## Important: Strong Recommendations

### 6. Use Named Arguments for Clarity
```ocaml
(* BAD - unclear what each argument means *)
let create_user "Alice" "alice@test.com" true false 30

(* GOOD - labeled arguments *)
let create_user ~name ~email ?(admin=false) ?(verified=false) ~age () =
  { name; email; admin; verified; age }

let user = create_user
  ~name:"Alice"
  ~email:"alice@test.com"
  ~verified:true
  ~age:30
  ()
```

### 7. Use the Pipeline Operator
```ocaml
(* BAD - nested function calls *)
List.map String.uppercase_ascii (List.filter (fun s -> String.length s > 3) (String.split_on_char ' ' text))

(* GOOD - pipeline operator |> *)
text
|> String.split_on_char ' '
|> List.filter (fun s -> String.length s > 3)
|> List.map String.uppercase_ascii
```

### 8. Prefer Records Over Tuples for Multiple Values
```ocaml
(* BAD - tuple is unclear *)
let get_stats () = (42, 3.14, "active")  (* What do these mean? *)

(* GOOD - record is self-documenting *)
type stats = {
  count: int;
  average: float;
  status: string;
}

let get_stats () = { count = 42; average = 3.14; status = "active" }
```

### 9. Use Variants for Finite Sets of Values
```ocaml
(* BAD - string for fixed set *)
let handle_status (status: string) =
  if status = "active" then ...
  else if status = "pending" then ...  (* Typo? Runtime error? *)

(* GOOD - variant *)
type status = Active | Pending | Completed | Failed

let handle_status = function
  | Active -> ...
  | Pending -> ...
  | Completed -> ...
  | Failed -> ...  (* Compiler ensures all cases handled *)
```

### 10. Use GADTs for Type-Level Constraints
```ocaml
(* GOOD - type-safe expression evaluator *)
type _ expr =
  | Int : int -> int expr
  | Bool : bool -> bool expr
  | Add : int expr * int expr -> int expr
  | If : bool expr * 'a expr * 'a expr -> 'a expr

let rec eval : type a. a expr -> a = function
  | Int n -> n
  | Bool b -> b
  | Add (e1, e2) -> eval e1 + eval e2
  | If (cond, then_, else_) ->
      if eval cond then eval then_ else eval else_

(* Type error at compile time: *)
(* eval (Add (Int 1, Bool true))  (* Won't compile! *) *)
```

## Functional Patterns

### 11. Use `let*` and `let+` Syntax (OCaml 4.08+)
```ocaml
(* BAD - nested binds *)
let fetch_user_data id =
  match find_user id with
  | None -> None
  | Some user ->
      match find_profile user.id with
      | None -> None
      | Some profile -> Some (user, profile)

(* GOOD - let* for monadic bind *)
let ( let* ) = Option.bind
let ( let+ ) opt f = Option.map f opt

let fetch_user_data id =
  let* user = find_user id in
  let* profile = find_profile user.id in
  Some (user, profile)
```

### 12. Use `Result.bind` for Error Handling
```ocaml
let ( let* ) = Result.bind

let process_data input =
  let* validated = validate input in
  let* parsed = parse validated in
  let* transformed = transform parsed in
  Ok transformed

(* Handle at the boundary *)
match process_data raw_input with
| Ok result -> use_result result
| Error msg -> log_error msg
```

### 13. Prefer `List.rev` Over Appending
```ocaml
(* BAD - O(n²) complexity *)
let rec map_bad f = function
  | [] -> []
  | x :: xs -> map_bad f xs @ [f x]

(* GOOD - O(n) with accumulator *)
let map_good f lst =
  let rec aux acc = function
    | [] -> List.rev acc
    | x :: xs -> aux (f x :: acc) xs
  in
  aux [] lst

(* BEST - use standard library *)
let map_best f lst = List.map f lst
```

### 14. Use Modules for Namespacing and Abstraction
```ocaml
(* GOOD - module for related types and functions *)
module Money : sig
  type t
  val of_cents : int -> t
  val to_cents : t -> int
  val add : t -> t -> t
  val ( + ) : t -> t -> t
end = struct
  type t = int  (* cents *)
  let of_cents x = x
  let to_cents x = x
  let add a b = a + b
  let ( + ) = add
end

(* Usage *)
let total = Money.(of_cents 100 + of_cents 250)
```

## Performance

### 15. Use Tail Recursion
```ocaml
(* BAD - not tail recursive (stack overflow on large lists) *)
let rec sum = function
  | [] -> 0
  | x :: xs -> x + sum xs  (* + is pending *)

(* GOOD - tail recursive *)
let sum lst =
  let rec aux acc = function
    | [] -> acc
    | x :: xs -> aux (acc + x) xs
  in
  aux 0 lst
```

### 16. Consider Hashtbl for Large Mutable Lookups
```ocaml
(* For immutable, small to medium: Map *)
module StringMap = Map.Make(String)
let m = StringMap.(empty |> add "key" 42)

(* For mutable, large datasets: Hashtbl *)
let h = Hashtbl.create 1000
let () = Hashtbl.add h "key" 42
let value = Hashtbl.find_opt h "key"
```

---

**Quick Reference - Copy This Mental Model:**
- Exhaustive pattern matching
- Option/Result for expected absence/errors
- Make invalid states unrepresentable
- Type annotations at module boundaries
- Immutable by default
- Labeled arguments for clarity
- Pipeline operator `|>`
- Records over tuples
- Variants for finite sets
- `let*` syntax for monadic code
- `List.rev` pattern for accumulation
- Modules for abstraction
- Tail recursion for lists
