#!/usr/bin/env python3
"""
mdrender - A streaming Markdown renderer for terminal using the rich library.

This script is intended to be invoked like:

    cat test.md | mdrender

It reads from stdin line-by-line (i.e. in a streaming fashion) and
renders Markdown using rich, but it buffers lines for “special blocks” such
as code fences, lists, tables, or blockquotes so that they are rendered properly.
Normal lines (including headers) are flushed immediately.

Usage:
    pip install rich
    chmod +x mdrender
    cat test.md | ./mdrender
"""

import sys
import re
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# Global state for code block tracking.
in_code_block = False

def flush_buffer(buffer):
    """Render the accumulated lines (as a Markdown block) if there is any content."""
    if buffer:
        block = "".join(buffer)
        # Only render if there is non-empty content.
        if block.strip():
            md = Markdown(block, code_theme="monokai")
            console.print(md)
        buffer.clear()

def is_header(line):
    """Return True if the line is a Markdown header."""
    return line.lstrip().startswith("#")

def is_code_fence(line):
    """Return True if the line is a code fence (start or end)."""
    return line.lstrip().startswith("```")

def is_list_line(line):
    """Return True if the line starts with a common list marker."""
    # Remove leading whitespace.
    stripped = line.lstrip()
    # Unordered list markers.
    if stripped.startswith(("* ", "- ", "+ ")):
        return True
    # Ordered list: e.g., "1. " or "1) " (a simple heuristic)
    if re.match(r"\d+[\.\)]\s+", stripped):
        return True
    return False

def is_blockquote(line):
    """Return True if the line starts with a blockquote marker."""
    return line.lstrip().startswith(">")

def is_table_line(line):
    """Return True if the line looks like a table row (contains '|' with non-blank items)."""
    # This is a heuristic: if the line contains a pipe and some text around it.
    if "|" in line:
        # Also catch markdown table separator lines.
        if re.match(r"\s*[-:| ]+\s*$", line):
            return True
        # Or if there's text on each side.
        return True
    return False

def is_horizontal_rule(line):
    """Return True if the line is a horizontal rule."""
    stripped = line.strip()
    return stripped in ("---", "***", "___")

def is_special_line(line):
    """
    Determines if a line is considered part of a special block.
    For our purposes, if it’s a code fence, a list line, a blockquote,
    a table row, or a horizontal rule, we treat it as special.
    """
    if is_code_fence(line):
        return True
    if is_list_line(line):
        return True
    if is_blockquote(line):
        return True
    if is_table_line(line):
        return True
    if is_horizontal_rule(line):
        return True
    return False

def is_normal_line(line):
    """
    A “normal” line is one that is not identified as a special line.
    (Headers are treated as normal, so they are rendered immediately.)
    Blank lines are considered normal.
    """
    return not is_special_line(line)

def main():
    buffer = []  # Buffer for accumulating special block lines.
    global in_code_block
    for line in sys.stdin:

        # For code fences, we use a state toggle.
        if is_code_fence(line):
            # If we're not already in a code block,
            # flush any pending buffered content and start the block.
            if not in_code_block:
                flush_buffer(buffer)
                in_code_block = True
                buffer.append(line)
            else:
                # If we're in a code block, add the line and then finish the block.
                buffer.append(line)
                in_code_block = False
                flush_buffer(buffer)
            continue

        # If we're inside a code block, simply collect all lines.
        if in_code_block:
            buffer.append(line)
            continue

        # For lines outside of code blocks:
        if is_normal_line(line):
            # Before rendering a normal line, flush any accumulated special block.
            flush_buffer(buffer)
            # If line is just newline dont render, just use normal print
            if line == '\n':
                print()
            else:
                # Render the normal line immediately.
                # (We render it as a Markdown block to preserve inline formatting.)
                md = Markdown(line, code_theme="monokai")
                console.print(md)
        else:
            # The line is part of a special block (lists, table rows, blockquotes, HR, etc.)
            buffer.append(line)

    # End of input; flush any remaining buffer.
    flush_buffer(buffer)

if __name__ == '__main__':
    main()
