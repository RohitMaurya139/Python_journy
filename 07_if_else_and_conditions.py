"""
Topic: if, elif, else and conditions
====================================

Definition:
    A condition is an expression that evaluates to True or False.
    if / elif / else runs different blocks of code based on those results.

Syntax:
    if condition:
        # runs when condition is True
    elif another_condition:
        # runs when the first condition is False and this one is True
    else:
        # runs when all conditions are False

Important:
    - Indentation (4 spaces) defines the block. It is required in Python.
    - Python treats these values as False (falsy):
          0, 0.0, "", [], (), {}, set(), None, False
      Everything else is truthy.

Example:
    age = 20
    if age >= 18:
        print("Adult")
    else:
        print("Minor")
"""


def check_number(number):
    """Return whether number is positive, negative or zero."""
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


def grade(marks):
    """Return a grade based on marks."""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


def is_even(number):
    """Return True when number is divisible by 2."""
    return number % 2 == 0


def can_vote(age, has_id):
    """A person can vote when age is at least 18 AND they have an ID."""
    if age >= 18 and has_id:
        return True
    return False


def main():
    number = int(input("Enter a number: "))

    # ---- if / elif / else ----
    print("The number is", check_number(number))

    # Ternary conditional expression: value_if_true if condition else value_if_false
    print("The number is", "even" if is_even(number) else "odd")

    # ---- Nested conditions ----
    if number >= 0:
        if number == 0:
            print("It is exactly zero.")
        else:
            print("It is a positive number.")
    else:
        print("It is a negative number.")

    # ---- Conditions with logical operators ----
    age = int(input("Enter your age: "))
    has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
    print("Can vote:", can_vote(age, has_id))

    # ---- Truthiness ----
    print("\nTruthiness examples:")
    for value in [0, 1, "", "hello", [], [1], None, False, True]:
        if value:
            print(repr(value), "is truthy")
        else:
            print(repr(value), "is falsy")

    # ---- Grades ----
    marks = int(input("\nEnter marks: "))
    print("Grade:", grade(marks))


if __name__ == "__main__":
    main()
