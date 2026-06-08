# feed.txt: The Flight Recorder for your Life 🚀
**A human-centric, plain-text format for capturing your daily momentum.**

`feed.txt` is a simple, sortable, and future-proof system for documenting your breakthroughs, daily rhythms, and the evolution of your thoughts. 

While most productivity tools focus on the **"Anxiety of the Unfinished"** (the to-do list), `feed.txt` celebrates the **"Presence of Execution."** It is a **Living Ledger**—a durable record designed to turn your daily activity into a searchable, permanent legacy of growth.

---

## 1. 💡 Philosophy: Momentum over Debt
In traditional task management, a "completed" task disappears. This leaves you with a deficit—a mountain of unfinished work and no visible record of your wins. `feed.txt` reverses this. It replaces future anxiety with a chronological proof of execution.

| Feature | The Feed | The Todo List |
| :--- | :--- | :--- |
| **Perspective** | 🏗️ Looking at what's built | 📉 Looking at what's missing |
| **Feeling** | 🔥 Motivation to continue | 😰 Pressure to finish |
| **Output** | 📜 A growing legacy | 🗑️ A shrinking list |
| **Role** | 🌱 Reflection & Growth | 📋 Management |

---

## 2. 🏛️ The 3 Axes of a Living Ledger
Using the `feed.txt` notation, you create a log that is sliceable by 3 key axes:

### I. ⚓ The Temporal Anchor (Time)
Your feed tells you exactly *when* an insight or achievement occurred. Every entry is anchored to a specific moment, creating a perfect chronological thread that never breaks across devices or years.

### II. 🎭 The Four Modalities (Sigils)
A single character defines the *cognitive mode* of the entry. This limits choices to prevent decision paralysis:
*   `.` **The Pulse:** 💓 Your daily rhythm. Facts, routine updates, and steady progress.
*   `!` **The Spark:** ✨ Your wins! Breakthroughs, core memories, and major achievements.
*   `?` **The Inquiry:** 🔍 Your curiosity. Active questions and unsolved problems.
*   `~` **The Flow:** 🌊 Your raw creativity. Unfiltered thoughts and experimental ideas.

### III. 🏷️ The Context (Metadata)
Extend your log with structured data without cluttering the prose. Use `#tags` for categorization and `key:value` pairs to link your daily log to external assets.

---

## 3. 🛠️ Features for the Long Haul

### 📝 The "Living Ledger" (Editing Allowed)
Unlike a blockchain or a system log, `feed.txt` is a personal document. You are encouraged to edit, refine, and prune your entries. Typo in a breakthrough? Missing a tag? Just open the file and fix it.

### ♻️ The Trash Convention
To keep your feed clean without destroying history, use the `#trash` convention. Simply append `#trash` to any entry to mark it as stale. This allows tools to filter noise while preserving the historical record.

### 🔗 Deep Linking & Threading
Using reserved keys like `ref:`, `id:`, and `par:`, you can create a graph of your thoughts. Link a **Spark** back to the **Inquiry** that triggered it, or point to an external essay.

---

## 4. 📜 The Format Rules
Your `feed.txt` is a standard UTF-8 plain text file. To ensure it remains human-readable for decades, follow these five rules:

1.  **Strictly Single-Line:** One entry per line. No newlines allowed.
2.  **Timestamps First:** Every line MUST begin with `YYYY-MM-DD HH:MM`.
3.  **Sigil follows Timestamp:** A single space, then your modality character (`.`, `!`, `?`, or `~`).
4.  **Prose follows Sigil:** Your free-form text comes after the sigil and a space.
5.  **Metadata at the End:** All tags and key:value pairs must be appended at the end of the line.

---

## 5. ✨ Examples
### The Feed in Action
```text
2026-06-08 07:15 . Morning yoga focus on hip mobility. #health
2026-06-08 08:45 ! Milestone: The new sandbox build is live and stable. #ship-it
2026-06-08 10:15 ~ Thinking about the intersection of CLI and AI. #ideas
2026-06-08 12:30 ? How can I improve the latency of the packet parser? #growth
2026-06-08 21:10 ! Shared a beautiful dinner to celebrate our anniversary. #life
2026-06-09 09:00 . Old routine check. #trash
```

---

## 6. 💻 Tooling & Implementation
While `feed.txt` can be managed in any text editor, it is designed for a zero-friction CLI experience.

*   **Reference CLI:** See `feed.py` for a Python implementation with logging and stats.
*   **Formal Specification:** See [SPEC.md](SPEC.md) for the formal EBNF grammar and parsing rules.

---

## Acknowledgments
`feed.txt` stands on the shoulders of giants: Gina Trapani’s `todo.txt`, Ryder Carroll’s *Bullet Journal*, and the timeless Unix philosophy.
