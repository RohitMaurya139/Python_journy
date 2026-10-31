"""
Topic: Data types, strings and type conversion
==============================================

1. Data types
-------------
Definition:
    A data type tells Python what kind of value something is and what
    operations can be performed on it.

Basic types:
    int      : whole numbers              -> 10, -7, 0
    float    : decimal numbers            -> 3.14, -0.5
    str      : text                       -> "Python"
    bool     : truth values               -> True, False
    NoneType : absence of a value         -> None
    complex  : complex numbers            -> 2 + 3j

Collection types (covered in separate files):
    list, tuple, set, dict

2. Strings
----------
Definition:
    A string is an ordered sequence of characters used for text.
    Strings are immutable: methods return new strings instead of changing
    the original one.

3. Type conversion
------------------
Definition:
    Type conversion (casting) changes a value from one type to another.
    - Implicit conversion happens automatically (e.g. int + float -> float).
    - Explicit conversion uses functions such as int(), float(), str(), bool().

Example:
    print(int("42"))       # 42
    print(float("3.14"))   # 3.14
    print(str(100))        # "100"
"""

# ---- 1. Basic data types ----
integer_number = 10
decimal_number = 3.14
text = "Python"
is_learning = True
nothing = None

print(type(integer_number))    # <class 'int'>
print(type(decimal_number))    # <class 'float'>
print(type(text))              # <class 'str'>
print(type(is_learning))       # <class 'bool'>
print(type(nothing))           # <class 'NoneType'>

# ---- 2. Collection data types ----
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"name": "Rohit", "age": 25}

print(type(my_list), type(my_tuple), type(my_set), type(my_dict))

# ---- 3. Creating strings ----
single_quotes = 'Python'
double_quotes = "Python"
multi_line = """This is
a multi-line
string."""

print(single_quotes, double_quotes)
print(multi_line)

# ---- 4. Escape characters ----
print("He said, \"Python is fun\".")
print("First line\nSecond line")
print("Column1\tColumn2")
print("C:\\Users\\Rohit")

# A raw string treats backslashes literally.
print(r"C:\Users\Rohit")

# ---- 5. Indexing and slicing ----
word = "Python"

print(word[0])       # P
print(word[-1])      # n
print(word[0:3])     # Pyt
print(word[:3])      # Pyt
print(word[3:])      # hon
print(word[::-1])    # nohtyP (reverse)

# ---- 6. Length, concatenation and repetition ----
print(len(word))         # 6
print("Py" + "thon")     # Python
print("Hi " * 3)         # Hi Hi Hi

# ---- 7. Membership ----
print("th" in word)      # True
print("z" not in word)   # True

# ---- 8. f-strings ----
name = "Rohit"
age = 25

print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")

# ---- 9. Common string methods ----
message = "  Hello Python  "

print(message.strip())                          # remove spaces at both ends
print(message.upper())                          # HELLO PYTHON
print(message.lower())                          # hello python
print(message.replace("Python", "World"))       # replace text
print(message.split())                          # split on whitespace -> list
print("-".join(["a", "b", "c"]))                # a-b-c
print("Python".startswith("Py"))                # True
print("Python".endswith("on"))                  # True
print("Python".find("t"))                       # index of first match

# Strings are immutable: this would raise a TypeError.
# word[0] = "J"

# Creating a new string is fine; it does not modify the old one.
word = "Jython"
print(word)

# ---- 10. Type conversion ----
# Implicit conversion: int is converted to float automatically.
print(10 + 2.5)     # 12.5

# Explicit conversion (casting).
print(int("42"))         # 42
print(int(3.99))         # 3 (truncates, does not round)
print(float("3.14"))     # 3.14
print(str(100))          # "100"
print(bool(1))           # True
print(bool(0))           # False
print(list("abc"))       # ['a', 'b', 'c']
print(tuple([1, 2, 3]))  # (1, 2, 3)
print(set([1, 2, 2, 3])) # {1, 2, 3}

# Careful with bool(): any non-empty string is True.
print(bool("False"))     # True
print(bool(""))          # False

# Invalid conversions raise ValueError.
try:
    print(int("3.5"))
except ValueError as error:
    print(f"Conversion failed: {error}")

# Correct way: convert to float first, then to int.
print(int(float("3.5")))    # 3

# Rounding vs truncating.
print(round(3.99))    # 4
print(int(3.99))      # 3
