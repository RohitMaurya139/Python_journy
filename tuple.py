"""
Topic: Tuples (tuple)
=====================

Definition:
    A tuple is an ordered but immutable (unchangeable) collection of items.
    Once a tuple is created, you cannot add, remove or replace its items.

Key points:
    - Written with parentheses: (1, 2, 3).
    - Supports indexing and slicing, just like a list.
    - A one-item tuple needs a trailing comma: (5,).
    - Often used for fixed data such as coordinates or RGB colours.

Example:
    point = (10, 20)
    print(point[0])     # 10
    point[0] = 5        # TypeError: tuple does not support item assignment
"""

a = (1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10)

print("Tuple:", a)
print("Item at index 2:", a[2])
print("Last item:", a[-1])
print("Slice a[2:5]:", a[2:5])

# Uncommenting the next line would raise a TypeError, because tuples are immutable.
# a[2] = 24

# ---- Useful tuple methods ----
print("Count of 2:", a.count(2))    # how many times 2 appears
print("Index of 3:", a.index(3))    # first position of 3

# ---- A one-item tuple needs a comma ----
single = (5,)
not_a_tuple = (5)

print(type(single))        # <class 'tuple'>
print(type(not_a_tuple))   # <class 'int'>

# ---- Unpacking a tuple into variables ----
first, second, *rest = a
print("First:", first)
print("Second:", second)
print("Rest:", rest)
