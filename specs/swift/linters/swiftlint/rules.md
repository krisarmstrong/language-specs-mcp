# SwiftLint Rules

## Style Rules

### closure_parameter_position

Closure parameters should be on same line as opening brace.

```swift
// BAD
doSomething {
    param in
    print(param)
}

// GOOD
doSomething { param in
    print(param)
}
```

### colon

Colon spacing rules.

```swift
// BAD
let dict:Dictionary<String,Int> = [:]
func foo(bar :Int) { }

// GOOD
let dict: Dictionary<String, Int> = [:]
func foo(bar: Int) { }
```

### comma

No space before comma, one space after.

```swift
// BAD
let arr = [1 ,2 ,3]
let arr = [1,2,3]

// GOOD
let arr = [1, 2, 3]
```

### control_statement

No parentheses around conditions.

```swift
// BAD
if (condition) { }
while (condition) { }
switch (value) { }

// GOOD
if condition { }
while condition { }
switch value { }
```

### empty_parentheses_with_trailing_closure

No empty parentheses with trailing closure.

```swift
// BAD
array.map() { $0 * 2 }

// GOOD
array.map { $0 * 2 }
```

### implicit_getter

Read-only computed properties don't need get.

```swift
// BAD
var computed: Int {
    get {
        return 0
    }
}

// GOOD
var computed: Int {
    return 0
}
```

### leading_whitespace

Files shouldn't start with whitespace.

### mark

MARK comments should be formatted correctly.

```swift
// BAD
//MARK: Section
// MARK:Section
// MARK :Section

// GOOD
// MARK: - Section
// MARK: Section
```

### opening_brace

Opening brace on same line with one space.

```swift
// BAD
if condition
{
}
func foo(){}

// GOOD
if condition {
}
func foo() {
}
```

### operator_usage_whitespace

Operators should have spacing.

```swift
// BAD
let sum=1+2
let range = 1...10

// GOOD
let sum = 1 + 2
let range = 1...10  // exception for range operators
```

### return_arrow_whitespace

Spacing around return arrow.

```swift
// BAD
func foo()->Int { }
func bar()-> Int { }

// GOOD
func foo() -> Int { }
```

### sorted_imports

Imports should be sorted.

```swift
// BAD
import UIKit
import Foundation
import CoreData

// GOOD
import CoreData
import Foundation
import UIKit
```

### statement_position

else/catch on same line as closing brace.

```swift
// BAD
if condition {
}
else {
}

// GOOD
if condition {
} else {
}
```

### trailing_comma

Trailing commas in arrays/dictionaries.

```swift
// Depends on configuration
// With trailing_comma enabled:
let array = [
    1,
    2,
    3,  // trailing comma
]
```

### trailing_newline

Files should end with single newline.

### trailing_semicolon

No trailing semicolons.

```swift
// BAD
let x = 1;

// GOOD
let x = 1
```

### trailing_whitespace

No trailing whitespace on lines.

### vertical_whitespace

Limit consecutive empty lines.

```swift
// BAD
func foo() {


    doSomething()
}

// GOOD
func foo() {
    doSomething()
}
```

## Lint Rules

### class_delegate_protocol

Delegate protocols should be class-only.

```swift
// BAD
protocol MyDelegate {
    func didUpdate()
}

// GOOD
protocol MyDelegate: AnyObject {
    func didUpdate()
}
```

### closing_brace

Closing brace shouldn't have blank line before.

### computed_accessors_order

Get should come before set.

```swift
// BAD
var value: Int {
    set { _value = newValue }
    get { _value }
}

// GOOD
var value: Int {
    get { _value }
    set { _value = newValue }
}
```

### empty_enum_arguments

Don't specify empty arguments in enum cases.

```swift
// BAD
switch result {
case .success():
    break
}

// GOOD
switch result {
case .success:
    break
}
```

### empty_parameters

Use Void -> instead of () ->.

```swift
// BAD
let closure: () -> Int

// GOOD
let closure: Void -> Int
```

### empty_string

Prefer isEmpty over comparison to "".

```swift
// BAD
if string == "" { }
if string != "" { }

// GOOD
if string.isEmpty { }
if !string.isEmpty { }
```

### force_cast

Avoid force casting.

```swift
// BAD
let x = object as! String

// GOOD
if let x = object as? String { }
guard let x = object as? String else { return }
```

### force_try

Avoid force try.

```swift
// BAD
let result = try! riskyOperation()

// GOOD
do {
    let result = try riskyOperation()
} catch {
    handleError(error)
}
```

### force_unwrapping

Avoid force unwrapping.

```swift
// BAD
let value = optional!

// GOOD
if let value = optional { }
guard let value = optional else { return }
let value = optional ?? defaultValue
```

### implicit_return

Prefer implicit return in single-expression functions.

```swift
// BAD
var computed: Int {
    return 0
}

func double(_ x: Int) -> Int {
    return x * 2
}

// GOOD
var computed: Int { 0 }

func double(_ x: Int) -> Int { x * 2 }
```

### legacy_cggeometry_functions

Use modern CGRect methods.

```swift
// BAD
CGRectGetWidth(rect)
CGRectGetHeight(rect)

// GOOD
rect.width
rect.height
```

### legacy_constant

Use modern constant syntax.

```swift
// BAD
CGPointZero
CGSizeZero
CGRectZero

// GOOD
CGPoint.zero
CGSize.zero
CGRect.zero
```

### legacy_constructor

Use Swift constructors.

```swift
// BAD
CGPointMake(1, 2)
CGSizeMake(10, 20)
CGRectMake(0, 0, 100, 100)

// GOOD
CGPoint(x: 1, y: 2)
CGSize(width: 10, height: 20)
CGRect(x: 0, y: 0, width: 100, height: 100)
```

### multiple_closures_with_trailing_closure

Don't use trailing closure with multiple closures.

```swift
// BAD
animate(duration: 0.3) {
    // animations
} completion: { _ in
    // completion
}

// GOOD
animate(
    duration: 0.3,
    animations: {
        // animations
    },
    completion: { _ in
        // completion
    }
)
```

### notification_center_detachment

Unregister from NotificationCenter in deinit.

```swift
// GOOD
deinit {
    NotificationCenter.default.removeObserver(self)
}
```

### private_outlet

IBOutlets should be private.

```swift
// BAD
@IBOutlet weak var label: UILabel!

// GOOD
@IBOutlet private weak var label: UILabel!
```

### private_unit_test

Unit test methods/properties should be private.

### redundant_discardable_let

Don't use let _ = when function returns discardable result.

```swift
// BAD
let _ = doSomething()

// GOOD
_ = doSomething()
// Or if return value is truly unused:
doSomething()
```

### redundant_nil_coalescing

Don't use ?? nil.

```swift
// BAD
let x = optional ?? nil

// GOOD
let x = optional
```

### redundant_optional_initialization

Don't explicitly initialize optionals to nil.

```swift
// BAD
var name: String? = nil

// GOOD
var name: String?
```

### redundant_set_access_control

Don't specify set access if same as get.

```swift
// BAD
private(set) private var value: Int

// GOOD
private var value: Int
```

### redundant_string_enum_value

Don't specify enum raw value if same as case name.

```swift
// BAD
enum Direction: String {
    case north = "north"
    case south = "south"
}

// GOOD
enum Direction: String {
    case north
    case south
}
```

### redundant_void_return

Don't specify Void return type.

```swift
// BAD
func doSomething() -> Void { }
func doSomething() -> () { }

// GOOD
func doSomething() { }
```

### self_in_property_initialization

Don't use self in property initialization.

```swift
// BAD
class Foo {
    var bar = self.baz()  // self not available yet
}
```

### shorthand_operator

Use shorthand operators.

```swift
// BAD
count = count + 1
count = count - 1

// GOOD
count += 1
count -= 1
```

### syntactic_sugar

Use syntactic sugar for types.

```swift
// BAD
let array: Array<Int>
let dict: Dictionary<String, Int>
let optional: Optional<String>

// GOOD
let array: [Int]
let dict: [String: Int]
let optional: String?
```

### todo

TODO/FIXME comments trigger warnings.

```swift
// TODO: This triggers a warning
// FIXME: This too
```

### unavailable_function

Unavailable functions should have body with fatalError.

```swift
@available(*, unavailable)
func deprecated() {
    fatalError()
}
```

### unneeded_break_in_switch

Don't use break in non-empty switch cases.

```swift
// BAD
switch value {
case 0:
    doSomething()
    break
default:
    break
}

// GOOD
switch value {
case 0:
    doSomething()
default:
    break  // OK in empty case
}
```

### unused_closure_parameter

Replace unused closure parameters with _.

```swift
// BAD
array.map { item in 0 }

// GOOD
array.map { _ in 0 }
```

### unused_enumerated

Don't use enumerated() if only using index or element.

```swift
// BAD - not using index
for (_, item) in array.enumerated() { }

// BAD - not using element
for (index, _) in array.enumerated() { }

// GOOD
for item in array { }
for index in array.indices { }
```

### unused_optional_binding

Don't use optional binding just to discard.

```swift
// BAD
if let _ = optional { }

// GOOD
if optional != nil { }
```

### valid_ibinspectable

IBInspectable must have explicit type.

```swift
// BAD
@IBInspectable var color = UIColor.red

// GOOD
@IBInspectable var color: UIColor = .red
```

### void_return

Use Void instead of ().

```swift
// BAD
func foo() -> () { }

// GOOD
func foo() -> Void { }
func foo() { }  // best
```

### weak_delegate

Delegates should be weak.

```swift
// BAD
var delegate: MyDelegate?

// GOOD
weak var delegate: MyDelegate?
```

## Metrics

### cyclomatic_complexity

Function complexity limit.

```swift
// Configure threshold
cyclomatic_complexity:
  warning: 10
  error: 20
```

### file_length

File line count limit.

### function_body_length

Function line count limit.

### function_parameter_count

Parameter count limit.

### line_length

Line character count limit.

### nesting

Type/statement nesting limit.

### type_body_length

Type line count limit.

## Opt-in Rules

### array_init

Use Array(seq) instead of seq.map { $0 }.

```swift
// BAD
let array = sequence.map { $0 }

// GOOD
let array = Array(sequence)
```

### attributes

Attribute placement rules.

### closure_body_length

Closure line count limit.

### closure_end_indentation

Closure end should align with start.

### collection_alignment

Elements in multiline collections should align.

### conditional_returns_on_newline

Conditional return should be on separate line.

```swift
// BAD
guard condition else { return }

// GOOD
guard condition else {
    return
}
```

### contains_over_filter_count

Use contains instead of filter.count.

```swift
// BAD
array.filter { $0 == target }.count > 0

// GOOD
array.contains { $0 == target }
```

### contains_over_filter_is_empty

Use contains instead of filter.isEmpty.

```swift
// BAD
array.filter { $0 == target }.isEmpty

// GOOD
!array.contains { $0 == target }
```

### contains_over_first_not_nil

Use contains instead of first != nil.

```swift
// BAD
array.first { $0 == target } != nil

// GOOD
array.contains { $0 == target }
```

### discouraged_object_literal

Avoid #colorLiteral and #imageLiteral.

### empty_collection_literal

Use isEmpty instead of == [].

```swift
// BAD
if array == [] { }

// GOOD
if array.isEmpty { }
```

### empty_count

Use isEmpty instead of count == 0.

```swift
// BAD
if array.count == 0 { }

// GOOD
if array.isEmpty { }
```

### empty_xctest_method

Test methods shouldn't be empty.

### enum_case_associated_values_count

Limit associated values per case.

### expiring_todo

TODOs with dates trigger errors after expiry.

```swift
// TODO: [2024-01-01] Fix this before release
```

### explicit_acl

Require explicit access control.

### explicit_enum_raw_value

Require explicit raw values.

### explicit_init

Don't call .init explicitly.

```swift
// BAD
let x = Foo.init()

// GOOD
let x = Foo()
```

### explicit_self

Require self for instance members.

### explicit_top_level_acl

Top-level declarations need access control.

### explicit_type_interface

Properties need type annotation.

### extension_access_modifier

Extension access modifier rules.

### fallthrough

Avoid fallthrough.

### fatal_error_message

fatalError needs message.

```swift
// BAD
fatalError()

// GOOD
fatalError("Unexpected state")
```

### file_header

File header format rules.

### file_name

File name should match type name.

### file_name_no_space

No spaces in file names.

### file_types_order

Ordering of types in file.

### first_where

Use first(where:) instead of filter.first.

```swift
// BAD
array.filter { $0.isValid }.first

// GOOD
array.first { $0.isValid }
```

### flatmap_over_map_reduce

Use flatMap instead of map.reduce.

### for_where

Use for-where instead of if inside for.

```swift
// BAD
for item in array {
    if item.isValid {
        process(item)
    }
}

// GOOD
for item in array where item.isValid {
    process(item)
}
```

### force_unwrapping

(also in lint rules above)

### function_default_parameter_at_end

Default parameters should be at end.

```swift
// BAD
func foo(a: Int = 0, b: Int) { }

// GOOD
func foo(b: Int, a: Int = 0) { }
```

### ibinspectable_in_extension

No IBInspectable in extensions.

### identical_operands

Don't compare identical operands.

```swift
// BAD
if x == x { }
```

### implicit_return

(also in lint rules above)

### implicitly_unwrapped_optional

Avoid implicitly unwrapped optionals.

```swift
// BAD
var name: String!

// GOOD
var name: String?
```

### indentation_width

Consistent indentation.

### joined_default_parameter

Use default separator for joined().

```swift
// BAD
array.joined(separator: "")

// GOOD
array.joined()
```

### last_where

Use last(where:) instead of filter.last.

### legacy_multiple

Use isMultiple(of:).

```swift
// BAD
x % 2 == 0

// GOOD
x.isMultiple(of: 2)
```

### legacy_random

Use Swift random.

```swift
// BAD
arc4random()
arc4random_uniform(10)

// GOOD
Int.random(in: 0..<10)
```

### let_var_whitespace

Blank line after let/var declarations.

### literal_expression_end_indentation

Literal closing should align with opening.

### lower_acl_than_parent

Child access can't exceed parent.

### missing_docs

Public declarations need documentation.

### modifier_order

Consistent modifier order.

### multiline_arguments

Function call arguments on separate lines.

### multiline_arguments_brackets

Brackets on separate lines for multiline.

### multiline_function_chains

Each chain call on separate line.

### multiline_literal_brackets

Brackets on separate lines for multiline literals.

### multiline_parameters

Parameters on separate lines.

### multiline_parameters_brackets

Brackets on separate lines.

### nimble_operator

Use Nimble operator matchers.

### no_extension_access_modifier

No access modifiers on extensions.

### no_fallthrough_only

Don't use fallthrough as only statement.

### no_grouping_extension

No extensions that only add same-module conformance.

### nslocalizedstring_key

NSLocalizedString key must be static string.

### nslocalizedstring_require_bundle

NSLocalizedString needs bundle.

### number_separator

Use _ for number grouping.

```swift
// BAD
let million = 1000000

// GOOD
let million = 1_000_000
```

### object_literal

Use object literals.

### operator_whitespace

Operator declaration spacing.

### optional_enum_case_matching

Match optional enum without ?.

```swift
// BAD
switch optional {
case .some(.value)?:
    break
}

// GOOD
switch optional {
case .value:
    break
}
```

### overridden_super_call

Override must call super.

### override_in_extension

Don't override in extensions.

### pattern_matching_keywords

Keywords in pattern matching.

### prefer_nimble

Prefer Nimble matchers over XCTAssert.

### prefer_self_in_static_references

Use Self instead of type name.

```swift
// BAD
class Foo {
    static func create() -> Foo { }
}

// GOOD
class Foo {
    static func create() -> Self { }
}
```

### prefer_self_type_over_type_of_self

Use Self instead of type(of: self).

### prefer_zero_over_explicit_init

Use .zero over explicit init.

```swift
// BAD
CGPoint(x: 0, y: 0)
CGRect(x: 0, y: 0, width: 0, height: 0)

// GOOD
CGPoint.zero
CGRect.zero
```

### prefixed_toplevel_constant

Top-level constants should have prefix.

### private_action

IBActions should be private.

### private_outlet

(also in lint rules above)

### private_subject

Combine subjects should be private.

### prohibited_interface_builder

Avoid Interface Builder.

### prohibited_super_call

Don't call super in certain methods.

### quick_discouraged_call

Avoid function calls in Quick describes.

### quick_discouraged_focused_test

No focused Quick tests.

### quick_discouraged_pending_test

No pending Quick tests.

### raw_value_for_camel_cased_codable_enum

Camel case enums need raw values for Codable.

### reduce_boolean

Use allSatisfy/contains instead of reduce for bools.

```swift
// BAD
array.reduce(true) { $0 && $1.isValid }

// GOOD
array.allSatisfy { $0.isValid }
```

### reduce_into

Use reduce(into:) for efficiency.

```swift
// BAD
array.reduce([]) { $0 + [$1] }

// GOOD
array.reduce(into: []) { $0.append($1) }
```

### redundant_objc_attribute

Don't use @objc when implied.

### redundant_type_annotation

Don't specify type when inferrable.

```swift
// BAD
let name: String = "Alice"

// GOOD
let name = "Alice"
```

### required_deinit

Classes should have deinit.

### required_enum_case

Protocol enums need certain cases.

### single_test_class

One test class per file.

### sorted_first_last

Use min/max instead of sorted.first/last.

```swift
// BAD
array.sorted().first
array.sorted().last

// GOOD
array.min()
array.max()
```

### static_operator

Operators should be static.

### strict_fileprivate

Prefer private over fileprivate.

### strong_iboutlet

Outlets shouldn't be weak.

### switch_case_on_newline

Case body on new line.

### toggle_bool

Use toggle().

```swift
// BAD
flag = !flag

// GOOD
flag.toggle()
```

### trailing_closure

Use trailing closure when possible.

### type_contents_order

Order of type contents.

### typesafe_array_init

Use type-safe array init.

### unavailable_condition

Use #unavailable.

```swift
// BAD
if #available(iOS 15, *) { } else { old() }

// GOOD
if #unavailable(iOS 15) { old() }
```

### unneeded_parentheses_in_closure_argument

No parentheses for single closure param.

```swift
// BAD
array.map({ (item) in item })

// GOOD
array.map({ item in item })
array.map { $0 }
```

### unowned_variable_capture

Prefer weak over unowned.

### untyped_error_in_catch

Catch should have typed error.

```swift
// BAD
catch { }

// GOOD
catch let error { }
catch let error as MyError { }
```

### unused_declaration

Unused private declarations.

### unused_import

Unused imports.

### vertical_parameter_alignment

Parameters should align.

### vertical_parameter_alignment_on_call

Call arguments should align.

### vertical_whitespace_between_cases

Blank line between switch cases.

### vertical_whitespace_closing_braces

No blank line before closing brace.

### vertical_whitespace_opening_braces

No blank line after opening brace.

### xct_specific_matcher

Use specific XCT matchers.

```swift
// BAD
XCTAssertTrue(x == y)

// GOOD
XCTAssertEqual(x, y)
```

### yoda_condition

Avoid Yoda conditions.

```swift
// BAD
if 5 == x { }

// GOOD
if x == 5 { }
```
