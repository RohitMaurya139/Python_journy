"""
Topic: Functions
================

Definition:
    A function is a reusable block of code that performs a task.
    You define it once with `def` and call it whenever you need it.

Vocabulary:
    - Parameter         : the variable listed inside the function definition.
    - Argument          : the actual value passed when calling the function.
    - Default parameter : used when the caller does not provide a value.
    - Keyword argument  : passed by name, e.g. greet(first_name="Rohit").
    - return            : sends a value back to the caller and exits the function.

Example:
    def add(a, b):
        return a + b

    print(add(2, 3))    # 5
"""


def greet(first_name, last_name):
    """Print a greeting using positional parameters."""
    print(f"Hello {first_name} {last_name}")


def greet_with_age(first_name, last_name, age=14):
    """Print a greeting; age has a default value of 14."""
    print(f"Hello {first_name} {last_name}, age {age}")


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.

    Example:
        is_palindrome("madam") -> True
        is_palindrome("Rohit") -> False
    """
    i = 0
    j = len(text) - 1

    while i < j:
        if text[i] != text[j]:
            return False
        i = i + 1
        j = j - 1

    return True


if __name__ == "__main__":
    # Positional arguments: values are matched by their order.
    greet("Rohit", "Maurya")

    # Keyword arguments: values are matched by their names.
    greet(first_name="Rohit", last_name="Maurya")

    # The default parameter is used when age is not passed.
    greet_with_age("Rohit", "Maurya")
    greet_with_age("Rohit", "Maurya", 25)

    # Use the value returned by a function.
    result = add(10, 20)
    print("10 + 20 =", result)

    print("Rohit is a palindrome?", is_palindrome("Rohit"))
    print("madam is a palindrome?", is_palindrome("madam"))
