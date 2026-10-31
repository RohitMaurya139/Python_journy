from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def resolve_path(name):
    p = Path(name)
    if not p.is_absolute():
        p = BASE_DIR / p
    return p


def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid number")
        return None


def readFileFolder():
    path = BASE_DIR
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item} ")


def createfile():
    try:
        readFileFolder()
        name = input("Please tell me your file Name: ")
        p = resolve_path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Enter the file data: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This File Already exist")
    except Exception as err:
        print(err)


def readFile():
    try:
        readFileFolder()
        name = input("Please tell me your file Name: ")
        p = resolve_path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
        else:
            print("This File does not exist")
    except Exception as err:
        print(err)


def updateFile():
    try:
        readFileFolder()
        name = input("Please tell me your file Name: ")
        p = resolve_path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of the file")
            print("Press 2 for overwriting the data of the file")
            print("Press 3 for appending some content in the file")
            res = get_int("Please tell your response :- ")

            if res == 1:
                newName = input("Enter new Name of the file: ")
                p2 = resolve_path(newName)
                p.rename(p2)
                p = p2
            elif res == 2:
                with open(p, "w") as fs:
                    data = input("Enter the data: ")
                    fs.write(data)
            elif res == 3:
                with open(p, "a") as fs:
                    data = input("Enter the data: ")
                    fs.write(data)
            else:
                print("Invalid response")
                return

            with open(p, "r") as fs:
                data = fs.read()
                print(data)
        else:
            print("This File does not exist")
    except Exception as err:
        print(err)


def deleteFile():
    try:
        readFileFolder()
        name = input("Enter the file name: ")
        p = resolve_path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("This File does not exist")
    except Exception as err:
        print(err)


def main():
    while True:
        print("Press 1 for creating the file")
        print("Press 2 for reading the file")
        print("Press 3 for updating the file")
        print("Press 4 for deleting the file")
        print("Press 5 for exit")

        check = get_int("Please tell your response :- ")

        if check == 1:
            createfile()
        elif check == 2:
            readFile()
        elif check == 3:
            updateFile()
        elif check == 4:
            deleteFile()
        elif check == 5:
            break
        else:
            print("Invalid response")


if __name__ == "__main__":
    main()
