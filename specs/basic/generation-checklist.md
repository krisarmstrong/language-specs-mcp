# BASIC Generation Checklist

**Read this BEFORE writing BASIC code. Modern BASIC variants have structure—use it.**

Note: This checklist applies to modern BASIC dialects (FreeBASIC, QB64, VB.NET).
For classic BASIC (GW-BASIC, QBasic), some features may not be available.

## Critical: You Must Do These

### 1. Use `Option Explicit` (or Equivalent)
```basic
' BAD - typos create new variables silently
DIM counter AS INTEGER
counter = 10
conter = counter + 1  ' Typo creates new variable!

' GOOD - require variable declaration
OPTION EXPLICIT  ' FreeBASIC
' or
Option Explicit  ' VB.NET

DIM counter AS INTEGER
counter = 10
conter = counter + 1  ' Error: variable not declared
```

### 2. Use Proper Data Types
```basic
' BAD - implicit types or Variant
DIM x       ' Variant in VB, could be anything
DIM y$      ' Old string suffix notation

' GOOD - explicit types
DIM count AS INTEGER
DIM name AS STRING
DIM value AS DOUBLE
DIM flag AS BOOLEAN

' GOOD - use appropriate size
DIM smallNum AS BYTE        ' 0-255
DIM index AS INTEGER        ' -32768 to 32767
DIM bigNum AS LONG          ' Larger range
DIM precise AS DOUBLE       ' Floating point
```

### 3. Initialize Variables Before Use
```basic
' BAD - using uninitialized variable
DIM total AS INTEGER
total = total + 5  ' What was total before?

' GOOD - initialize explicitly
DIM total AS INTEGER = 0
' or
DIM total AS INTEGER
total = 0
total = total + 5
```

### 4. Use Structured Control Flow
```basic
' BAD - GOTO spaghetti
10 IF x > 10 THEN GOTO 50
20 x = x + 1
30 GOTO 10
50 PRINT "Done"

' GOOD - structured loops
DIM x AS INTEGER = 0
DO WHILE x <= 10
    x = x + 1
LOOP
PRINT "Done"

' GOOD - FOR loop
FOR i AS INTEGER = 1 TO 10
    PRINT i
NEXT i

' GOOD - SELECT CASE
SELECT CASE grade
    CASE "A"
        PRINT "Excellent"
    CASE "B", "C"
        PRINT "Good"
    CASE ELSE
        PRINT "Needs improvement"
END SELECT
```

### 5. Use SUB and FUNCTION Properly
```basic
' BAD - all code in main with GOSUB
100 GOSUB 500
110 END
500 ' Subroutine code
510 RETURN

' GOOD - proper SUB procedures
SUB PrintGreeting(name AS STRING)
    PRINT "Hello, "; name
END SUB

' GOOD - FUNCTION with return value
FUNCTION Square(x AS DOUBLE) AS DOUBLE
    RETURN x * x
END FUNCTION

' Call them
PrintGreeting("World")
DIM result AS DOUBLE = Square(5)
```

## Important: Strong Recommendations

### 6. Use Meaningful Variable Names
```basic
' BAD - cryptic names
DIM a, b, c AS INTEGER
DIM x$ AS STRING

' GOOD - descriptive names
DIM itemCount AS INTEGER
DIM totalPrice AS DOUBLE
DIM customerName AS STRING
```

### 7. Handle Errors Properly
```basic
' GOOD - structured error handling (VB.NET / modern BASIC)
TRY
    DIM file AS INTEGER = FREEFILE
    OPEN "data.txt" FOR INPUT AS #file
    ' ... read file ...
    CLOSE #file
CATCH ex AS Exception
    PRINT "Error reading file: "; ex.Message
FINALLY
    ' Cleanup code
END TRY

' FreeBASIC style
ON ERROR GOTO ErrorHandler
' ... code ...
EXIT SUB

ErrorHandler:
    PRINT "Error occurred: "; ERR
    RESUME NEXT
```

### 8. Close Files After Opening
```basic
' BAD - forgetting to close
DIM f AS INTEGER = FREEFILE
OPEN "data.txt" FOR INPUT AS #f
' ... use file ...
' Forgot to close!

' GOOD - always close
DIM f AS INTEGER = FREEFILE
OPEN "data.txt" FOR INPUT AS #f
' ... use file ...
CLOSE #f

' BETTER - use pattern that ensures cleanup
SUB ProcessFile(filename AS STRING)
    DIM f AS INTEGER = FREEFILE
    OPEN filename FOR INPUT AS #f

    DO UNTIL EOF(f)
        LINE INPUT #f, lineText$
        ' Process line
    LOOP

    CLOSE #f  ' Always executed
END SUB
```

### 9. Use Arrays Properly
```basic
' Declare with bounds
DIM numbers(1 TO 100) AS INTEGER
DIM matrix(0 TO 9, 0 TO 9) AS DOUBLE

' Check bounds before access
IF index >= LBOUND(numbers) AND index <= UBOUND(numbers) THEN
    PRINT numbers(index)
END IF

' Use FOR EACH when available (VB.NET)
FOR EACH item IN collection
    PRINT item
NEXT
```

### 10. Comment Your Code
```basic
' GOOD - file header comment
' =====================================================
' Program: InventoryManager
' Author:  Development Team
' Date:    2024-01-15
' Purpose: Manage product inventory
' =====================================================

' GOOD - function documentation
' Calculates the total price with tax
' Parameters:
'   basePrice - The price before tax
'   taxRate   - Tax rate as decimal (e.g., 0.08 for 8%)
' Returns: Total price including tax
FUNCTION CalculateTotal(basePrice AS DOUBLE, taxRate AS DOUBLE) AS DOUBLE
    RETURN basePrice * (1 + taxRate)
END FUNCTION
```

## Modern BASIC Features

### 11. Use Type Definitions (Structures)
```basic
' GOOD - define custom types
TYPE Customer
    id AS INTEGER
    name AS STRING * 50
    balance AS DOUBLE
END TYPE

DIM cust AS Customer
cust.id = 1
cust.name = "Alice"
cust.balance = 100.50
```

### 12. Use Constants for Magic Numbers
```basic
' BAD - magic numbers
IF temperature > 100 THEN ...
price = amount * 1.08

' GOOD - named constants
CONST BOILING_POINT AS INTEGER = 100
CONST TAX_RATE AS DOUBLE = 0.08

IF temperature > BOILING_POINT THEN ...
price = amount * (1 + TAX_RATE)
```

### 13. Modularize Code with Includes/Modules
```basic
' GOOD - separate files for organization
' In main.bas:
#INCLUDE "utilities.bi"
#INCLUDE "database.bi"

' Or use modules (VB.NET)
IMPORTS MyProject.Utilities
```

## Security

### 14. Validate Input
```basic
' BAD - using input directly
INPUT "Enter filename: ", filename$
OPEN filename$ FOR INPUT AS #1

' GOOD - validate input
INPUT "Enter filename: ", filename$

' Check for path traversal
IF INSTR(filename$, "..") > 0 THEN
    PRINT "Invalid filename"
    END
END IF

' Check file exists
IF DIR$(filename$) = "" THEN
    PRINT "File not found"
    END
END IF

OPEN filename$ FOR INPUT AS #1
```

### 15. Handle String Overflow
```basic
' Be careful with fixed-length strings
DIM fixedStr AS STRING * 10

' BAD - may truncate silently
fixedStr = "This is a very long string"  ' Truncated!

' GOOD - use variable-length strings when possible
DIM varStr AS STRING
varStr = "This is a very long string"  ' OK

' Or validate length
IF LEN(inputStr) <= 10 THEN
    fixedStr = inputStr
ELSE
    PRINT "Input too long"
END IF
```

---

**Quick Reference - Copy This Mental Model:**
- `Option Explicit` always
- Explicit data types
- Initialize variables
- Structured control flow (no GOTO)
- SUB and FUNCTION for procedures
- Meaningful variable names
- Close all opened files
- Array bounds checking
- Named constants for magic numbers
- Validate all input
- Comment code and functions
