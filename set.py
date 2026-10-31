"""
Topic: Sets (set)
=================

Definition:
    A set is an unordered collection of unique items.
    Duplicate values are removed automatically.

Key points:
    - Written with curly braces: {1, 2, 3}.
    - Items must be hashable (immutable), so a list cannot be an item.
    - Sets do not support indexing (there is no a[0]).
    - Great for removing duplicates and comparing groups of data.
    - The printed order can change, because sets are unordered.

Example:
    numbers = {1, 2, 2, 3}
    print(numbers)          # {1, 2, 3}  (duplicates removed)
    print(2 in numbers)     # True
"""

# ---- 1. Creating a set (duplicates are removed) ----
mixed = {2, 4, 5, 5, 5, 5, 5, 1, 1, 1, 1, "hello", 3, 4, 5, 6}
print("Mixed set:", mixed)

for item in mixed:
    print(item)

# ---- 2. Set operations ----
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {6, 7, 8, 9, 10}

c = a.intersection(b)            # items in both a AND b
d = a.union(b)                   # items in a OR b
e = a.difference(b)              # items in a but NOT b
f = b.difference(a)              # items in b but NOT a
g = a.symmetric_difference(b)    # items in exactly one set
h = b.symmetric_difference(a)    # same result as g

print("Set A:", a)
print("Set B:", b)
print("Intersection (A & B):", c)
print("Union (A | B):", d)
print("Difference (A - B):", e)
print("Difference (B - A):", f)
print("Symmetric difference (A ^ B):", g)
print("Symmetric difference (B ^ A):", h)

# ---- 3. Adding and removing items ----
a.add(99)         # add one item
a.discard(99)     # remove it if present (no error if it is missing)
print("After add and discard:", a)

# ---- 4. Removing duplicates from a list ----
marks = [90, 80, 90, 70, 80]
unique_marks = set(marks)
print("Unique marks:", unique_marks)
