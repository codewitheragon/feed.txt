# feed.txt Protocol Specification (v1.0.0)

## 1. Introduction
`feed.txt` is a plain-text format for chronological logging. It is designed to be human-readable, machine-parsable, and fully compatible with standard Unix text processing tools.

## 2. Format Definition (EBNF)

A `feed.txt` file consists of zero or more lines. Each line must conform to the following grammar:

```ebnf
line           ::= timestamp space sigil space record [space metadata_list] newline
timestamp      ::= date space time
date           ::= year "-" month "-" day
time           ::= hour24 ":" minute
sigil          ::= "." | "!" | "?" | "~"
record         ::= { utf8_character - (metadata_trigger | newline) }
metadata_list  ::= metadata_item {space metadata_item}
metadata_item  ::= tag | extension
tag            ::= "#" non_whitespace_chars
extension      ::= key ":" value
key            ::= [a-zA-Z0-9_-]+
value          ::= non_whitespace_chars | quoted_string
quoted_string  ::= '"' { utf8_character - '"' } '"'
metadata_trigger ::= " #" | space key ":"
space          ::= " "
newline        ::= "\n"
```

## 3. Parsing Rules

### 3.1 Right-to-Left (RTL) Metadata Scanning
To maintain a clean separation between human prose and machine data, parsers MUST implement an RTL scan. 
- **Intermingling:** `#tags` and `key:value` pairs can be intermingled in any order within the metadata block.
- **Termination:** The metadata block ends when a token is encountered that is neither a tag nor a valid extension.
- **Quoted Values:** Values containing spaces MUST be wrapped in double quotes (e.g., `title:"My Great Essay"`). Parsers MUST handle these as single atomic tokens.

### 3.2 Robust Extraction Regex
To safely extract the components of a line, use the following logic:
1. Identify the metadata block at the end of the string.
2. Use a regex to capture tags: `(?<=\s|^)#(\S+)`
3. Use a regex to capture extensions (handling quotes): `(?<=\s|^)([a-zA-Z0-9_-]+):(?:"([^"]*)"|(\S+))`

### 3.2 Timestamp Invariant
The timestamp MUST be the first 16 characters of the line. This ensures that a standard alphabetical sort (`LC_ALL=C sort`) is equivalent to a chronological sort.

### 3.3 Sigils (The Modalities)
- `.` **The Pulse:** Routine events, facts, and daily rhythms.
- `!` **The Spark:** Wins, breakthroughs, and milestones.
- `?` **The Inquiry:** Questions and unsolved problems.
- `~` **The Flow:** Raw creativity and ephemeral thoughts.

## 4. Metadata Conventions

### 4.1 The Trash Convention
Entries marked with the `#trash` tag should be ignored by default by reporting and analysis tools. This is a non-destructive way to deprecate entries while maintaining the historical record.

### 4.2 Reserved Extensions
- `ref:` Reference to an external URI or file path.
- `id:` A unique identifier for the entry (e.g., UUID or hash).
- `par:` Reference to a parent `id` to create threads of thought.
- `tz:` ISO 8601 UTC offset (e.g., `+0200`).

## 5. Implementor Guidelines
- **Encoding:** Files MUST be UTF-8 encoded.
- **Line Endings:** Files SHOULD use Unix-style LF (`\n`) line endings.
- **Sorting:** Tools SHOULD assume the file is sorted chronologically but MUST be able to sort the file if requested.
