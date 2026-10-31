"""
Topic: while loops
==================

Definition:
    A while loop repeats a block of code as long as its condition is True.
    Use it when you do not know in advance how many repetitions are needed.

Key points:
    - Always update the condition variable, otherwise the loop runs forever.
    - `break` stops the loop immediately.
    - `continue` skips the rest of the current iteration.
    - `while True:` is a common pattern when the loop must run until a break.

Example:
    count = 0
    while count <= 3:
        print(count)
        count = count + 1
"""

import random


def simple_count():
    """Print numbers 0 to 10 using a while loop."""
    a = 0
    while a <= 10:
        print(a)
        a = a + 1


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.

    Example:
        is_palindrome("madam") -> True
        is_palindrome("rohit") -> False
    """
    i = 0
    j = len(text) - 1

    while i < j:
        if text[i] != text[j]:
            return False
        i = i + 1
        j = j - 1

    return True


def play_guessing_game():
    """Ask the user to guess a random number between 1 and 100."""
    number = random.randint(1, 100)
    tries = 0

    while True:
        try:
            guess = int(input("Please guess the number between 1 to 100: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        tries = tries + 1

        if guess > number:
            print("Higher! Guess a lower number.")
        elif guess < number:
            print("Lower! Guess a higher number.")
        else:
            print(f"Hurray! You guessed the number in {tries} tries.")
            break


if __name__ == "__main__":
    simple_count()

    print("Rohit is a palindrome?", is_palindrome("Rohit"))
    print("madam is a palindrome?", is_palindrome("madam"))

    play_guessing_game()
