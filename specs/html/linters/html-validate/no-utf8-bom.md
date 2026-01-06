## Rules

Rules

1. [Rules reference](index.html)
2. [Configuration presets](presets.html)
3. [Third-party rules](third-party.html)

# Disallow documents from having UTF-8 BOM

Rule ID:no-utf8-bomCategory:DocumentStandards:-

A unicode byte order mark (BOM) is needed in UTF-16 and UTF-32 to determine endiannes but for UTF-8 it has no meaning. Browsers are required to handle the BOM under all circumstances but tooling might not handle it properly and is therefor best left out.

Instead the document should be served with the `Content-Type: application/javascript; charset=utf-8` header and/or the `<meta charset="utf-8">` meta-tag.
