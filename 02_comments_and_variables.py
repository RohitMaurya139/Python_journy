"""
Topic: Comments and variables in Python
=======================================

1. Comments
-----------
Definition:
    A comment is text that Python ignores while running the program.
    Comments explain code, leave notes, or temporarily disable code.

Types:
    - Single-line comment: starts with #
    - Inline comment: a # comment placed after code on the same line
    - Multi-line note: use a triple-quoted string (called a docstring when it
      is the first statement in a module, function, class or method)

Example:
    # This is a comment
    age = 25          # inline comment
    print(age)        # 25

2. Variables
------------
Definition:
    A variable is a name that refers to a value stored in memory.
    You create it with the assignment operator (=).

Rules for names:
    - Start with a letter or underscore (_), not a number.
    - Use only letters, numbers and underscores.
    - Names are case-sensitive: age and Age are different.
    - Do not use Python keywords such as if, for, class, def, True.

Conventions:
    - snake_case for normal variables: first_name, total_marks.
    - UPPER_CASE for constants: MAX_SPEED, PI.
    - A leading underscore (_private) means "internal use" by convention.

Example:
    name = "Rohit"
    age = 25
    print(name, age)    # Rohit 25
"""

# ---- 1. Comments ----
# This is a single-line comment. Python ignores this line entirely.

name = "Rohit"      # inline comment: explains the code on this line
age = 25

"""
This is a multi-line note.
It is not assigned to a variable, so Python ignores it.
When placed at the top of a file, function or class, it is called a docstring.
"""

# ---- 2. Creating variables ----
first_name = "Rohit"
last_name = "Maurya"
full_name = first_name + " " + last_name

print("Full name:", full_name)

# ---- 3. Naming conventions ----
total_marks = 450       # snake_case for normal variables
MAX_SPEED = 120         # UPPER_CASE for constants (by convention)
_private_value = 99     # leading underscore means internal use

print(total_marks, MAX_SPEED, _private_value)

# ---- 4. Multiple assignment ----
x, y, z = 10, 20, 30
print(x, y, z)

# ---- 5. Swapping two variables ----
a = 1
b = 2
a, b = b, a
print("After swap: a =", a, "b =", b)

# ---- 6. Reassignment and dynamic typing ----
value = 10
print(type(value))      # <class 'int'>

value = "ten"           # the same name can refer to a different type
print(type(value))      # <class 'str'>

count = 0
count = count + 1
count += 1              # shorthand for count = count + 1
print("Count:", count)  # 2
