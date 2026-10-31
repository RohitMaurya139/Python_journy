"""
Project: Simple File Manager (CRUD)
===================================

CRUD means:
    C -> Create a file
    R -> Read a file
    U -> Update a file (rename, overwrite or append)
    D -> Delete a file

Concepts used:
    - pathlib.Path   : modern way to work with file paths.
    - with open(...) : automatically closes files.
    - functions      : break the program into small reusable pieces.
    - exceptions     : handle errors (for example, permission denied) gracefully.
    - while loop     : keep showing the menu until the user chooses Exit.

How to run:
    python 20_file_manager.py
"""

from pathlib import Path

# Folder where this script lives. All relative paths are resolved from here.
BASE_DIR = Path(__file__).resolve().parent


def resolve_path(name):
    """Return an absolute Path for `name`.

    If `name` is relative, it is placed inside BASE_DIR.
    If `name` is already absolute, it is returned unchanged.

    Example:
        resolve_path("notes.txt") -> D:\\...\\project\\notes.txt
    """
    path = Path(name)
    if not path.is_absolute():
        path = BASE_DIR / path
    return path


def get_int(prompt):
    """Ask for an integer; return None if the user enters something else."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number")
        return None


def list_files():
    """Print every file and folder inside BASE_DIR."""
    print("\nFiles and folders:")
    items = list(BASE_DIR.rglob("*"))
    for i, item in enumerate(items, start=1):
        print(f"{i} : {item}")


def create_file():
    """Create a new file and write one line of text into it."""
    try:
        list_files()
        name = input("Please tell me your file name: ").strip()
        if not name:
            print("File name cannot be empty")
            return

        path = resolve_path(name)
        if path.exists():
            print("This file already exists")
            return

        data = input("Enter the file data: ")
        with open(path, "w", encoding="utf-8") as file:
            file.write(data)
        print("FILE CREATED SUCCESSFULLY")
    except Exception as error:
        print(error)


def read_file():
    """Read and print the contents of an existing file."""
    try:
        list_files()
        name = input("Please tell me your file name: ").strip()
        path = resolve_path(name)

        if path.exists() and path.is_file():
            with open(path, "r", encoding="utf-8") as file:
                print(file.read())
        else:
            print("This file does not exist")
    except Exception as error:
        print(error)


def update_file():
    """Rename, overwrite or append to an existing file."""
    try:
        list_files()
        name = input("Please tell me your file name: ").strip()
        path = resolve_path(name)

        if not (path.exists() and path.is_file()):
            print("This file does not exist")
            return

        print("Press 1 for changing the name of the file")
        print("Press 2 for overwriting the data of the file")
        print("Press 3 for appending some content in the file")
        choice = get_int("Please tell your response: ")

        if choice == 1:
            new_name = input("Enter new name of the file: ").strip()
            if not new_name:
                print("New file name cannot be empty")
                return
            new_path = resolve_path(new_name)
            path.rename(new_path)
            path = new_path
        elif choice == 2:
            data = input("Enter the data: ")
            with open(path, "w", encoding="utf-8") as file:
                file.write(data)
        elif choice == 3:
            data = input("Enter the data: ")
            with open(path, "a", encoding="utf-8") as file:
                file.write(data)
        else:
            print("Invalid response")
            return

        # Show the file after the update.
        with open(path, "r", encoding="utf-8") as file:
            print(file.read())
    except Exception as error:
        print(error)


def delete_file():
    """Delete an existing file."""
    try:
        list_files()
        name = input("Enter the file name: ").strip()
        path = resolve_path(name)

        if path.exists() and path.is_file():
            path.unlink()
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("This file does not exist")
    except Exception as error:
        print(error)


def main():
    """Show the menu until the user chooses to exit."""
    while True:
        print("\nPress 1 for creating the file")
        print("Press 2 for reading the file")
        print("Press 3 for updating the file")
        print("Press 4 for deleting the file")
        print("Press 5 for exit")

        choice = get_int("Please tell your response: ")

        if choice == 1:
            create_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            update_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid response")


# This guard makes sure main() runs only when this file is executed directly,
# not when it is imported as a module by another file.
if __name__ == "__main__":
    main()
