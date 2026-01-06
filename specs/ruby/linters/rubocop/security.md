# RuboCop Security Cops

Security cops detect potential security vulnerabilities.

Source: https://docs.rubocop.org/rubocop/cops_security.html

### Security/CompoundHash
Checks for compound hash operations that may be vulnerable.

### Security/Eval
Detects uses of code evaluation methods which can lead to code injection vulnerabilities. This cop flags dangerous patterns and recommends safer alternatives.

### Security/IoMethods
Checks for dangerous IO method uses.

### Security/JSONLoad
Checks for `JSON.load` which is unsafe with untrusted data. Recommends using `JSON.parse` instead.

### Security/MarshalLoad
Checks for `Marshal.load` which is unsafe with untrusted data due to deserialization vulnerabilities.

### Security/Open
Checks for `Kernel#open` with dynamic input which can lead to command injection. Recommends using `File.open` or `URI.open` with validated input.

### Security/YAMLLoad
Checks for `YAML.load` which is unsafe with untrusted data. Recommends using `YAML.safe_load` instead.
