"""
Topic: Dictionaries (dict)
==========================

Definition:
    A dictionary stores data as key-value pairs.
    Each key must be unique and hashable; values can be of any type.

Key points:
    - Written with curly braces: {"name": "Rohit", "age": 25}.
    - Access a value with square brackets: student["name"].
    - Dictionaries are mutable: you can add, update or delete pairs.
    - From Python 3.7 onward, dictionaries remember insertion order.

Example:
    student = {"name": "Rohit", "age": 25}
    print(student["name"])       # Rohit
    student["age"] = 26          # update
    student["city"] = "Delhi"    # add
"""

# ---- 1. Create, read and update ----
a = {
    1: "hello",
    2: 56,
    3: "Rohit",
}

print(a[1])
print(a[2])
print(a[3])

a[1] = "maurya"        # update the value for key 1
a.update({4: 600})     # add a new key-value pair
del a[2]               # delete key 2

print("Updated dictionary:", a)

# ---- 2. Loop through a dictionary ----
print("Values:")
for value in a.values():
    print(value)

print("Keys:", list(a.keys()))
print("Items (key, value):", list(a.items()))

# ---- 3. Safe access with get() ----
print("Value of key 3:", a.get(3))
print("Value of missing key 99:", a.get(99, "not found"))

# ---- 4. Merging two dictionaries ----
d = {"a": 12, "b": 13, "c": 14}
d2 = {"d": 12, "e": 13, "f": 14}

for key in d2:
    d[key] = d2[key]

print("Merged dictionary:", d)

# The same merge can be done with: d.update(d2)

# ---- 5. Sum of all values ----
total = 0
for value in d.values():
    total = total + value

print("Sum of values:", total)

# ---- 6. Important: lists and dicts are referenced, not copied ----
numbers = [1, 2, 3, 4, 5]
alias = numbers          # alias points to the SAME list in memory
alias[0] = 100

print("numbers:", numbers)   # [100, 2, 3, 4, 5]
print("alias:", alias)       # [100, 2, 3, 4, 5]

# Use copy() when you need an independent copy.
real_copy = numbers.copy()
real_copy[0] = 999
print("numbers after editing the copy:", numbers)
print("real_copy:", real_copy)
