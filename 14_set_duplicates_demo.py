"""
Topic: Removing duplicates with a set
=====================================

Definition:
    A set stores only unique values. Converting a list (or another
    collection) to a set removes all duplicate values automatically.

Example:
    marks = [90, 80, 90, 70, 80]
    print(set(marks))    # {80, 90, 70}  (order may change)

Note:
    Sets are unordered, so do not rely on the printed order.
"""

# A set written directly: duplicates are removed as it is created.
a = {2, 4, 5, 5, 5, 5, 5, 1, 1, 1, 1, "hello", 3, 4, 5, 6}
print("Set with duplicates removed:", a)

for item in a:
    print(item)

# The same idea using a list -> set conversion.
marks = [90, 80, 90, 70, 80]
print("Original list:", marks)
print("Unique values:", set(marks))
