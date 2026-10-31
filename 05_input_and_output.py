"""
Topic: Input and output in Python
=================================

Output:
    print() displays values on the screen.
    Useful parameters:
        sep  -> separator between values (default " ")
        end  -> text printed after the last value (default "\\n")
        file -> where to write (default sys.stdout)

Input:
    input(prompt) reads one line from the keyboard.
    It ALWAYS returns a string, so convert it when you need a number:
        int(input(...))
        float(input(...))

Example:
    name = input("Name: ")
    print("Hello", name)
"""


def main():
    # ---- 1. Basic output ----
    print("Hello", "Rohit")
    print("2026", "01", "11", sep="-")
    print("This is printed", end=" ")
    print("on the same line.")

    # ---- 2. Formatted output ----
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"Hello {name}, you are {age} years old.")
    print(f"Next year you will be {age + 1}.")

    # Width, alignment and decimal formatting.
    pi = 3.14159
    print(f"Pi to 2 decimal places: {pi:.2f}")
    print(f"Right aligned in 10 spaces: |{name:>10}|")
    print(f"Left aligned in 10 spaces:  |{name:<10}|")
    print(f"Centred in 10 spaces:       |{name:^10}|")

    # ---- 3. Reading decimal numbers ----
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(f"Area = {length * width}")

    # ---- 4. Reading multiple values on one line ----
    numbers = input("Enter two numbers separated by a space: ").split()
    a = int(numbers[0])
    b = int(numbers[1])
    print(f"Sum = {a + b}")

    # Shorter version using map():
    # a, b = map(int, input("Enter two numbers: ").split())
    # print(f"Sum = {a + b}")

    # ---- 5. Handling invalid input ----
    try:
        number = int(input("Enter a whole number: "))
        print("You entered:", number)
    except ValueError:
        print("That was not a whole number.")


# This guard runs main() only when the file is executed directly.
if __name__ == "__main__":
    main()
