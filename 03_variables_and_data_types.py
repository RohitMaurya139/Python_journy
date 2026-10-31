"""
Topic: Variables and basic data types
=====================================

Definition:
    A variable is a named reference to a value stored in memory.
    Python creates the variable automatically when you assign a value to it,
    so you do not need to declare a type first (this is called dynamic typing).

Common basic types:
    int      -> whole numbers          : 25, -7, 0
    float    -> decimal numbers        : 3.14, 99.5
    str      -> text                   : "red", 'Rohit'
    bool     -> True or False          : True, False
    NoneType -> absence of a value     : None

Naming rules:
    - Start with a letter or underscore (_), not a number.
    - Use only letters, numbers and underscores.
    - Names are case-sensitive (age and Age are different).
    - Use snake_case for normal variables: total_marks, first_name.

Example:
    name = "Rohit"
    age = 25
    print(name, age)   ->  Rohit 25
"""

# ---- 1. Creating variables ----
age = 25            # int
height = 178        # int (height in centimetres)
color = "red"       # str

print(age + 25, height, color)

# ---- 2. Checking the type of a value ----
print(type(age))      # <class 'int'>
print(type(height))   # <class 'int'>
print(type(color))    # <class 'str'>

# ---- 3. Python is dynamically typed ----
# The same variable name can later hold a value of a different type.
value = 10
print(type(value))    # <class 'int'>

value = "ten"
print(type(value))    # <class 'str'>

# ---- 4. Multiple assignment ----
a, b, c = 1, 2, 3
print(a, b, c)

# ---- 5. Converting between types (type casting) ----
number_text = "42"
number = int(number_text)        # str -> int
print(number + 8)                # 50
print(str(number) + " is now text")
