# The feed.txt Format
A human-centric, plain-text format for chronological logging.

The first and most important rule of `feed.txt`:
**Every entry occupies exactly one line and begins with a full timestamp.**

---

## 1. Why feed.txt?
Most productivity tools focus on the "Anxiety of the Unfinished" (the to-do list). `feed.txt` celebrates the **Joy of the Accomplished**. 

It is a "flight recorder" for your thoughts and actions—an append-only ledger designed to turn your daily momentum into a searchable, permanent legacy of growth.

| Feature | The Feed | The Todo List |
| :--- | :--- | :--- |
| **Perspective** | Looking at what's built | Looking at what's missing |
| **Feeling** | Motivation to continue | Pressure to finish |
| **Output** | A growing legacy | A shrinking list |
| **Role** | Reflection & Growth | Management |

---

## 2. Format Rules
To ensure your feed is both human-readable and machine-sortable, follow these five simple rules.

### Rule 1: One line per entry
A single line in your text file represents a single log entry.

### Rule 2: The Temporal Anchor
Every line must begin with a date and time in `YYYY-MM-DD HH:MM` format.
*Example:* `2026-06-08 14:30`
*Why:* This ensures a simple alphabetical sort matches the chronological order of your life.

### Rule 3: The Modality Sigil
Immediately following the timestamp and a single space, a single character defines the "mode" of the entry:
*   `.` **The Pulse:** Routine events, objective facts, and daily rhythms.
*   `!` **The Spark:** Wins, breakthroughs, and major milestones.
*   `?` **The Inquiry:** Curiosity, questions, and unsolved problems.
*   `~` **The Flow:** Raw creativity, unfiltered thoughts, and ephemeral ideas.

### Rule 4: The Record (Prose)
The descriptive text follows the sigil and a single space. It can contain any UTF-8 characters but **must not** contain newlines.

### Rule 5: Tags and Metadata
Structured extensions should be placed at the end of the line:
*   **Hashtags:** Preceded by a `#` for categorization (e.g., `#work`, `#health`).
*   **Key:Value pairs:** Use `key:value` for numeric or state tracking (e.g., `dist:5km`, `ups:60`).

---

## 3. Quickstart Tooling (Reference CLI)

To make logging instant, add these functions to your `.bashrc` or `.zshrc`. This removes the friction of manual timestamping.

```bash
# Core logging function
feed() {
  local sigil=$1
  shift
  echo "$(date +'%Y-%m-%d %H:%M') $sigil $*" >> ~/feed.txt
}

# Modality shortcuts
alias pulse='feed .'
alias spark='feed !'
alias ask='feed ?'
alias flow='feed ~'
```

**Usage:**
`spark Fixed the race condition in the scheduler! #work`

---

## 4. FAQ (Why not...?)

### Why not just use todo.txt?
`todo.txt` manages your **debt** (what you haven't done). `feed.txt` manages your **assets** (what you have done). They are perfect companions: use one to plan your day, and the other to record your progress.

### Why not a digital journal or Obsidian?
`feed.txt` is built for **zero-friction capture**. Opening an app or navigating folders is a barrier for a 5-second thought. `feed.txt` lives in your terminal and is 100% portable—a single file that will be readable for decades.

### Why the specific date format?
`YYYY-MM-DD HH:MM` ensures that a standard alphabetical sort (the default for text tools and file systems) is identical to a chronological sort.

---

## 5. Example File
See [sample-feed.txt](sample-feed.txt) for a real-world example of a lived-in feed.

---

## 6. Acknowledgments
`feed.txt` stands on the shoulders of giants: Gina Trapani’s `todo.txt`, Ryder Carroll’s *Bullet Journal*, and the timeless Unix philosophy of "simple tools, working together."
