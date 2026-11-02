# List, Dictionary and Set comprehension, lambda, map, filter, modules and packages


# ============================================================
# 1. LIST COMPREHENSION
# Instead of writing a loop + append, you build a list in ONE line.
# Form: [expression for item in iterable if condition]
# ============================================================
for i in range(1,21):
    if i%2==0:
        print(i)

print("---------------------------------------------")
l=[i for i in range(1,21) if i%2==0]  #List Comprehension
print(l)
#   i          -> expression: what to store
#   for i ...  -> loop
#   if i%2==0  -> optional filter

print([i*10 for i in range(1,6)])          # [10, 20, 30, 40, 50]
print([i for i in range(10) if i > 5])     # [6, 7, 8, 9]


# ============================================================
# 2. DICTIONARY COMPREHENSION
# Form: {key: value for item in iterable if condition}
# ============================================================
l={i: i**2 for i in range(1,21) if i%2==0}  #dictionary Comprehension
print(l)
# {2: 4, 4: 16, 6: 36, ...}

print({name: len(name) for name in ["Rohit", "Ram", "Amit"]})
# {'Rohit': 5, 'Ram': 3, 'Amit': 4}


# ============================================================
# 3. SET COMPREHENSION
# Form: {expression for item in iterable if condition}
# A set stores UNIQUE values (duplicates removed automatically).
# ============================================================
s={i**2 for i in range(1,11)}
print(s)                                   # {1, 4, 9, 16, 25, 36, 49, 64, 81, 100}

print({i % 3 for i in range(10)})          # {0, 1, 2}  duplicates gone
print({i for i in range(5) if i % 2 == 0}) # {0, 2, 4}


# ============================================================
# 4. LAMBDA FUNCTION
# An anonymous (nameless) one-line function.
# Form: lambda arguments: expression
# Used when you need a small function only once (like in map/filter).
# ============================================================
def add(a,b):
    print(a+b)

add(12,12)

sum = lambda a,b : a+b
print(sum(13,13))

check = lambda a : "Even" if a % 2 ==0 else "odd"
print(check(13))

# A lambda can only contain ONE expression, no statements/loops.


# ============================================================
# 5. MAP
# map(function, iterable) applies the function to EACH element.
# It returns an iterator, so wrap it with list() to print all values.
# ============================================================
number=[1,2,3,4,5,6]

res= map(lambda x: x*x,number)
print(list(res))                           # [1, 4, 9, 16, 25, 36]


# ============================================================
# 6. FILTER
# filter(function, iterable) keeps only elements where function is True.
# ============================================================
res1= filter(lambda x: x % 2==0,number)
print(list(res1))                          # [2, 4, 6]

# map vs filter
print(list(map(lambda x: x*10, number)))       # [10, 20, 30, 40, 50, 60]
print(list(filter(lambda x: x > 3, number)))   # [4, 5, 6]

# map + filter together: square only the even numbers
print(list(map(lambda x: x*x, filter(lambda x: x%2==0, number))))  # [4, 16, 36]


# ============================================================
# 7. MODULES
# A module is simply a .py file whose functions/variables you can import.
# Use "import" to reuse code instead of rewriting it.
# ============================================================

# import whole module
import math
print(math.sqrt(25))            # 5.0
print(math.pi)                  # 3.141592653589793

# import only what you need
from math import sqrt, factorial
print(sqrt(81), factorial(5))   # 9.0 120

# import with a short alias
import math as m
print(m.floor(3.7))             # 3

# Your OWN module:
# Create a file "mymodule.py" in the same folder:
#     def greet(name):
#         return "Hello " + name
#     PI = 3.14
# Then here you can write:
#     import mymodule
#     print(mymodule.greet("Rohit"))   # Hello Rohit
#     print(mymodule.PI)               # 3.14


# ============================================================
# 8. PACKAGES
# A package is a FOLDER of related modules (a module is a .py file).
# It usually contains an __init__.py file so Python treats it as a package.
#
# mypackage/
#     __init__.py
#     math_utils.py        -> def square(n): return n*n
#     string_utils.py      -> def upper(s): return s.upper()
#
# Usage:
#     from mypackage import math_utils
#     print(math_utils.square(4))          # 16
#
#     from mypackage.string_utils import upper
#     print(upper("python"))               # PYTHON
#
#     import mypackage.math_utils as mu
#     print(mu.square(5))                  # 25
# ============================================================


# Every module has a __name__. When a file is run directly it is "__main__",
# when it is imported its value is the module name. This is why we write:
if __name__ == "__main__":
    print("This runs only when 20_advance_python.py is executed directly")


# ------------------------------------------------------------
# QUICK SUMMARY
#   list comp     [expr for x in it if cond]
#   dict comp     {key: val for x in it if cond}
#   set comp      {expr for x in it if cond}   (unique values)
#   lambda        lambda args: expression      (small one-line function)
#   map           map(func, iterable)  -> transform each item
#   filter        filter(func, iterable) -> keep items where True
#   module        a single .py file you import
#   package       a folder of modules (with __init__.py)
# ------------------------------------------------------------
