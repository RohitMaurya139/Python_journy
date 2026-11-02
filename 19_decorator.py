# DECORATORS
# A decorator is a function that takes another function and returns a new
# function, adding extra behavior WITHOUT changing the original function code.
#
# Why possible? In Python functions are first-class objects:
# you can pass a function as an argument, return it, and assign it to a name.

# ============================================================
# 1. BASIC DECORATOR
# ============================================================
def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()                      # call the original function
        print("After the function")
    return wrapper                  # return the new function


@my_decorator                       # same as: greet = my_decorator(greet)
def greet():
    print("Hello!")


greet()                             # Before / Hello! / After


# ============================================================
# 2. DECORATOR FOR FUNCTIONS THAT TAKE ARGUMENTS + RETURN VALUES
# Use *args and **kwargs so it works for ANY function.
# functools.wraps keeps the original function's name/docstring.
# ============================================================
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log
def add(a, b):
    "Adds two numbers"
    return a + b


print(add(2, 3))
print(add.__name__)                 # add (thanks to @wraps)


# ============================================================
# 3. DECORATOR WITH ITS OWN ARGUMENTS -> needs one extra function layer
# @repeat(3) means: repeat(3) first returns a decorator, then that
# decorator is applied to the function.
# ============================================================
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi")


say_hi()                            # Hi Hi Hi


# ============================================================
# 4. PRACTICAL EXAMPLE: TIMING DECORATOR
# ============================================================
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def slow_square(n):
    time.sleep(0.1)
    return n * n


print(slow_square(5))


# ============================================================
# 5. CLASS-BASED DECORATOR
# A class can be a decorator if it has __call__.
# This is useful when the decorator needs to keep state (like a counter).
# ============================================================
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def hello():
    print("hello")


hello()
hello()


# ============================================================
# 6. MULTIPLE DECORATORS -> applied bottom-up
# @a
# @b
# def f(): ...    is the same as    f = a(b(f))
# So @b is applied first, then @a.
# ============================================================
def bold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper


def italic(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper


@bold
@italic
def text():
    return "Python"


print(text())                       # <b><i>Python</i></b>


# ============================================================
# 7. BUILT-IN DECORATORS
# ============================================================
class Student:
    college = "ABC College"

    def __init__(self, name):
        self._name = name

    @property                       # use method like an attribute
    def name(self):
        return self._name

    @staticmethod                   # no self / cls needed
    def add(a, b):
        return a + b

    @classmethod                    # gets the class (cls), not the instance
    def get_college(cls):
        return cls.college


s = Student("Rohit")
print(s.name)                       # Rohit   (property)
print(Student.add(2, 3))            # 5       (staticmethod)
print(Student.get_college())        # ABC College (classmethod)


# ------------------------------------------------------------
# QUICK SUMMARY
#   concept              meaning
#   decorator            function that wraps another function
#   @decorator           shorthand for func = decorator(func)
#   *args, **kwargs      make wrapper accept any arguments
#   functools.wraps      preserve original name/docstring
#   decorator(args)      needs 3 layers (args -> decorator -> wrapper)
#   class decorator      class with __call__
#   @property            method behaves like attribute
#   @staticmethod        method without self/cls
#   @classmethod         method that receives the class
# ------------------------------------------------------------
