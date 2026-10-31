"""
Topic: Operators in Python
==========================

Definition:
    An operator performs an operation on one or more values (operands).
    In 2 + 3, "+" is the operator and 2 and 3 are the operands.

Types:
    1. Arithmetic       : +  -  *  /  //  %  **
    2. Comparison       : ==  !=  >  <  >=  <=
    3. Logical          : and  or  not
    4. Assignment       : =  +=  -=  *=  /=  //=  %=  **=
    5. Membership       : in  not in
    6. Identity         : is  is not
    7. Bitwise          : &  |  ^  ~  <<  >>

Precedence (high to low, simplified):
    **
    *  /  //  %
    +  -
    comparisons (==, !=, <, >, <=, >=)
    not
    and
    or

Parentheses () can always be used to change the order.

Example:
    print(2 + 3 * 4)     # 14
    print((2 + 3) * 4)   # 20
"""

# ---- 1. Arithmetic operators ----
a = 10
b = 3

print("a + b  =", a + b)     # 13
print("a - b  =", a - b)     # 7
print("a * b  =", a * b)     # 30
print("a / b  =", a / b)     # 3.333... (true division returns float)
print("a // b =", a // b)    # 3 (floor division)
print("a % b  =", a % b)     # 1 (remainder)
print("a ** b =", a ** b)    # 1000 (10 to the power 3)

# ---- 2. Comparison operators ----
print("a == b:", a == b)     # False
print("a != b:", a != b)     # True
print("a > b :", a > b)      # True
print("a < b :", a < b)      # False
print("a >= b:", a >= b)     # True
print("a <= b:", a <= b)     # False

# ---- 3. Logical operators ----
age = 20
has_id = True

print(age >= 18 and has_id)      # True
print(age < 18 or has_id)        # True
print(not has_id)                # False

# Short-circuit behaviour:
# `and` stops at the first falsy value.
# `or` stops at the first truthy value.

# ---- 4. Assignment operators ----
count = 10

count += 5      # count = count + 5
print("count after += :", count)

count -= 3      # count = count - 3
print("count after -= :", count)

count *= 2      # count = count * 2
print("count after *= :", count)

count //= 4     # count = count // 4
print("count after //= :", count)

count %= 3      # count = count % 3
print("count after %= :", count)

count **= 2     # count = count ** 2
print("count after **= :", count)

# ---- 5. Membership operators ----
text = "Rohit"
numbers = [10, 20, 30]

print("R in text:", "R" in text)
print("z not in text:", "z" not in text)
print("20 in numbers:", 20 in numbers)
print("50 not in numbers:", 50 not in numbers)

# ---- 6. Identity operators ----
x = [1, 2]
y = [1, 2]
z = x

print("x == y:", x == y)    # True: same values
print("x is y:", x is y)    # False: different objects
print("x is z:", x is z)    # True: same object

# ---- 7. Bitwise operators ----
print("5 & 3 =", 5 & 3)       # 1  (AND)
print("5 | 3 =", 5 | 3)       # 7  (OR)
print("5 ^ 3 =", 5 ^ 3)       # 6  (XOR)
print("~5    =", ~5)          # -6 (NOT)
print("1 << 3 =", 1 << 3)     # 8  (left shift)
print("16 >> 2 =", 16 >> 2)   # 4  (right shift)

# ---- 8. Operator precedence ----
print("2 + 3 * 4 =", 2 + 3 * 4)       # 14
print("(2 + 3) * 4 =", (2 + 3) * 4)   # 20
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)   # 512 (right-associative)
