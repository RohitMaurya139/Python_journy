"""
Topic: File handling
====================

Definition:
    File handling means reading from and writing to files on disk.
    Python uses the built-in open() function, usually inside a `with` block.

Common modes:
    "r"  : read (default; error if the file does not exist)
    "w"  : write (creates the file or overwrites it completely)
    "a"  : append (creates the file or adds to the end)
    "x"  : create (error if the file already exists)
    "r+" : read and write (the file must exist)
    "b"  : binary mode, e.g. "rb" or "wb" (for images, PDFs, ...)

Why use `with`?
    The `with` block closes the file automatically, even if an error happens.
    This prevents data loss and resource leaks.

Example:
    with open("notes.txt", "w") as file:
        file.write("Hello\\n")

    with open("notes.txt", "r") as file:
        print(file.read())
"""

from pathlib import Path

# Build the path relative to this script, so it works from any directory.
FILE_PATH = Path(__file__).parent / "superman.txt"

# ---- 1. Write (overwrite/create) ----
with open(FILE_PATH, "w", encoding="utf-8") as file:
    file.write("Hello, I am writing in superman.txt from fileHandel.py using Python.\n")

# ---- 2. Append (add to the end) ----
with open(FILE_PATH, "a", encoding="utf-8") as file:
    file.write("I am appending more text data in superman.txt.\n")

# ---- 3. Read the whole file ----
with open(FILE_PATH, "r", encoding="utf-8") as file:
    print(file.read())

# ---- 4. Read line by line ----
print("Reading line by line:")
with open(FILE_PATH, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
