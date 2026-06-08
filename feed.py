#!/usr/bin/env python3
import sys
import datetime
import os
import re

# Configuration
FEED_FILE = os.path.expanduser("~/feed.txt")

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def log_entry(sigil, message):
    timestamp = get_timestamp()
    line = f"{timestamp} {sigil} {message}\n"
    with open(FEED_FILE, "a") as f:
        f.write(line)
    print(f"Logged to {FEED_FILE}")

def list_entries(filter_trash=True):
    if not os.path.exists(FEED_FILE):
        print("Feed file not found.")
        return

    with open(FEED_FILE, "r") as f:
        for line in f:
            if filter_trash and "#trash" in line:
                continue
            print(line.strip())

def show_stats():
    if not os.path.exists(FEED_FILE):
        return

    stats = {".": 0, "!": 0, "?": 0, "~": 0}
    total = 0
    with open(FEED_FILE, "r") as f:
        for line in f:
            if "#trash" in line:
                continue
            sigil = line[17:18]
            if sigil in stats:
                stats[sigil] += 1
                total += 1

    print(f"Total Entries: {total}")
    print(f"Pulse (.): {stats['.']}")
    print(f"Spark (!): {stats['!']}")
    print(f"Inquiry (?): {stats['?']}")
    print(f"Flow (~): {stats['~']}")

def usage():
    print("Usage: feed [command] [args]")
    print("Commands:")
    print("  pulse <msg>   Log a Pulse (.)")
    print("  spark <msg>   Log a Spark (!)")
    print("  ask <msg>     Log an Inquiry (?)")
    print("  flow <msg>    Log a Flow (~)")
    print("  list          List entries (excludes #trash)")
    print("  all           List all entries (includes #trash)")
    print("  stats         Show feed statistics")

def main():
    if len(sys.argv) < 2:
        usage()
        return

    cmd = sys.argv[1]
    
    if cmd == "pulse":
        log_entry(".", " ".join(sys.argv[2:]))
    elif cmd == "spark":
        log_entry("!", " ".join(sys.argv[2:]))
    elif cmd == "ask":
        log_entry("?", " ".join(sys.argv[2:]))
    elif cmd == "flow":
        log_entry("~", " ".join(sys.argv[2:]))
    elif cmd == "list":
        list_entries(filter_trash=True)
    elif cmd == "all":
        list_entries(filter_trash=False)
    elif cmd == "stats":
        show_stats()
    else:
        usage()

if __name__ == "__main__":
    main()
