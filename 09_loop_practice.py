"""
Topic: Loop practice (homework)
===============================

Definition:
    A function is a reusable block of code with a name.
    Each exercise below is written as a function so it can be reused and tested.

Run this file and enter a number to see all the answers.
"""


def print_hello(n):
    """Print 'Hello Python' n times."""
    for _ in range(n):
        print("Hello Python")


def print_numbers(n):
    """Print numbers from 0 to n-1."""
    for i in range(n):
        print(i)


def print_reverse_numbers(n):
    """Print numbers from n down to 1."""
    for i in range(n, 0, -1):
        print(i)


def sum_upto(n):
    """Return 0 + 1 + ... + (n-1)."""
    total = 0
    for i in range(n):
        total += i
    return total


def factorial(n):
    """Return n! = n * (n-1) * ... * 1.

    Example:
        factorial(5) -> 120
    """
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact


def sum_even(n):
    """Return the sum of even numbers from 0 to n-1."""
    total = 0
    for i in range(n):
        if i % 2 == 0:
            total = total + i
    return total


def reverse_string(text):
    """Return text reversed.

    Example:
        reverse_string("Rohit") -> "tihoR"
    """
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result = result + text[i]
    return result


if __name__ == "__main__":
    n = int(input("Enter the number: "))

    print("1. Hello n times:")
    print_hello(n)

    print("2. Numbers 0 to n-1:")
    print_numbers(n)

    print("3. Numbers n to 1:")
    print_reverse_numbers(n)

    print("4. Sum:", sum_upto(n))
    print("5. Factorial:", factorial(n))
    print("6. Sum of even numbers:", sum_even(n))

    text = "Rohit"
    print("7. Reverse of", text, "is", reverse_string(text))
