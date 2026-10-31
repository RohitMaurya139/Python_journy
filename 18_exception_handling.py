"""
Topic: Exception handling
=========================

Definition:
    An exception is an error that happens while the program is running.
    If it is not handled, the program stops and shows a traceback.

Keywords:
    - try     : code that might raise an exception.
    - except  : runs when a matching exception occurs.
    - else    : runs only if no exception occurred.
    - finally : always runs, whether an exception occurred or not.
    - raise   : manually create an exception.

Common exceptions:
    - ZeroDivisionError : dividing by zero.
    - ValueError        : right type, wrong value (e.g. int("abc")).
    - TypeError         : wrong type used in an operation.
    - FileNotFoundError : the file does not exist.

Example:
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")
"""


def safe_divide(a, b):
    """Demonstrate try / except / else / finally."""
    try:
        print("Result:", a / b)
    except ZeroDivisionError as error:
        print(f"Sorry, there is an error: {error}")
    else:
        print("Good, no exception occurred")
    finally:
        print("I am finally; I always run")


def check_admission(age):
    """Raise ValueError when age is outside the allowed range (10 to 19)."""
    try:
        if age < 10 or age > 19:
            raise ValueError(
                f"You cannot get admission because your age {age} is not "
                "within our permitted range (10 to 19)."
            )
    except Exception as error:
        print(f"Sorry, an error occurred: {error}")
    else:
        print("All the best! You will get admission.")


if __name__ == "__main__":
    safe_divide(10, 0)
    safe_divide(10, 2)

    try:
        age = int(input("Tell me your age: "))
    except ValueError:
        print("Please enter a valid whole number.")
    else:
        check_admission(age)

    print("The school will start soon")
