# Check Language Standards

Before writing code in a specific language, use this command to get the generation checklist and relevant standards.

## Usage

When user asks to check a language or before writing code, use the specforge MCP tools:

1. Call `get_checklist` with the language parameter to get the generation checklist
2. If the user has a specific framework, call `get_framework_checklist`
3. If dealing with user input or authentication, call `get_security_checklist`

## Example

User: "Check go standards before I start coding"

Response pattern:
1. Use specforge's `get_checklist` tool with language="go"
2. Summarize the key points for the user
3. Remind about relevant linter rules if applicable
