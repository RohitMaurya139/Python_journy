"""
Topic: for loops and range()
============================

Definition:
    A for loop repeats a block of code once for each item in a sequence
    (a list, string, tuple, range, ...).

range(start, stop, step):
    - start is inclusive (default 0)
    - stop is exclusive (the loop stops before this number)
    - step is how much to add each time (default 1)
    Example: range(1, 6) -> 1, 2, 3, 4, 5

Example:
    for i in range(3):
        print(i)      # prints 0, 1, 2
"""

# ---- 1. range() with start, stop and step ----
print("range(1, 20, 4):")
for i in range(1, 20, 4):
    print(i)

print("range(20, 51):")
for i in range(20, 51):
    print(i)

print("range(16, -1, -1):")
for i in range(16, -1, -1):
    print(i)

# ---- 2. Multiplication table ----
# Change n if you want another table. You can also use:
# n = int(input("Enter the number to generate a table: "))
n = 5
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

# ---- 3. Looping over a string (two ways) ----
text = "Rohit"

print("By index:")
for i in range(len(text)):
    print(text[i])

print("Directly over characters:")
for char in text:
    print(char)

# ---- 4. break and continue ----
print("break example (stops when i is 6):")
for i in range(0, 10):
    if i == 6:
        break
    print(i)

print("continue example (skips even numbers):")
for i in range(0, 20):
    if i % 2 == 0:
        continue
    print(i)
