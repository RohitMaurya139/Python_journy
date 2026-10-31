"""
Topic: Lists (list)
===================

Definition:
    A list is an ordered, mutable (changeable) collection of items.
    It can store items of different types and it allows duplicates.

Key points:
    - Indexing starts at 0; negative indexes count from the end (-1 is last).
    - Lists are mutable: you can add, remove or change items.
    - Lists are written with square brackets: [1, 2, 3].

Example:
    fruits = ["apple", "banana"]
    fruits.append("mango")      # ["apple", "banana", "mango"]
    print(fruits[0])            # apple
"""

# ---- 1. Create, access and update ----
a = [12, 13, 14, 15, 16, 17, 18]
a[2] = 100                        # change the item at index 2 (the third item)

print("List after update:", a)
print("Last item (a[-1]):", a[-1])
print("Second last item (a[-2]):", a[-2])

# ---- 2. Iterate over a list (two common ways) ----
print("\nUsing range(len(a)):")
for i in range(len(a)):
    print(a[i])

print("\nUsing direct iteration:")
for element in a:
    print(element)

# ---- 3. Common list methods ----
numbers = [12, 13, 14, 15, 16, 17, 18]

numbers.append(24)                 # add one item at the end
numbers.insert(2, 30)              # insert 30 at index 2
numbers.extend([100, 200, 300])    # add many items at the end
numbers.remove(15)                 # remove the first matching value
popped = numbers.pop(4)            # remove and return the item at index 4
count_18 = numbers.count(18)       # count how many times 18 appears

print("\nAfter list methods:", numbers)
print("Popped item:", popped)
print("Count of 18:", count_18)
print("Is 100 in the list?", 100 in numbers)

# ---- 4. Practice: small helper functions ----


def print_positive(numbers):
    """Print every positive number in a list."""
    for ele in numbers:
        if ele > 0:
            print(ele)


def print_negative(numbers):
    """Print every negative number in a list."""
    for ele in numbers:
        if ele < 0:
            print(ele)


def total(numbers):
    """Return the sum of all numbers in a list."""
    result = 0
    for ele in numbers:
        result = result + ele
    return result


def average(numbers):
    """Return the average (mean) of all numbers in a list."""
    return total(numbers) / len(numbers)


def largest(numbers):
    """Return the largest number using a manual loop."""
    maximum = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum


def second_largest(numbers):
    """Return the second largest number in a list.

    The list must contain at least two different values.
    Example: [1, 3, 4, 7, 9] -> 7

    How it works:
        maximum keeps the biggest number seen so far.
        second keeps the second biggest number seen so far.
        When a new bigger number appears, the old maximum becomes `second`.
    """
    maximum = numbers[0]
    second = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > maximum:
            second = maximum
            maximum = numbers[i]
        elif numbers[i] > second:
            second = numbers[i]

    return second


if __name__ == "__main__":
    b = [1, 3, 4, -1, -2, -5, 7, 8, 9, -9, -11]

    print("\nList b:", b)

    print("Positive numbers:")
    print_positive(b)

    print("Negative numbers:")
    print_negative(b)

    print("Sum:", total(b))
    print("Average:", average(b))
    print("Largest:", largest(b))
    print("Second largest:", second_largest(b))
