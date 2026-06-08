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

def parse_line(line):
    """
    Precisely parses a feed.txt line into its components.
    Returns: (timestamp, sigil, prose, tags, extensions)
    """
    line = line.strip()
    if not line: return None
    
    timestamp = line[:16]
    sigil = line[17:18]
    body = line[19:]
    
    # Regex to find all metadata tokens (tags or key:value) at the END of the line
    # Supports quoted values: key:"value with spaces"
    meta_regex = r'(?:\s+)(?:#(?P<tag>\S+)|(?P<key>[a-zA-Z0-9_-]+):(?:"(?P<qval>[^"]*)"|(?P<uval>\S+)))'
    
    metadata_tokens = list(re.finditer(meta_regex, body))
    
    tags = []
    extensions = {}
    
    # Identify the start of the continuous metadata block at the end
    meta_start_index = len(body)
    for match in reversed(metadata_tokens):
        if match.end() == meta_start_index:
            meta_start_index = match.start()
            if match.group('tag'):
                tags.insert(0, match.group('tag'))
            else:
                key = match.group('key')
                val = match.group('qval') if match.group('qval') is not None else match.group('uval')
                extensions[key] = val
        else:
            # Metadata block is broken by prose
            break
            
    prose = body[:meta_start_index].strip()
    return timestamp, sigil, prose, tags, extensions

def show_stats():
    if not os.path.exists(FEED_FILE):
        return

    stats = {".": 0, "!": 0, "?": 0, "~": 0}
    total = 0
    with open(FEED_FILE, "r") as f:
        for line in f:
            parsed = parse_line(line)
            if not parsed or "trash" in parsed[3]:
                continue
            sigil = parsed[1]
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
