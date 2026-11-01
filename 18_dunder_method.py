# Dunder Method
# "Dunder" = Double UNDERscore. Also called magic methods.
# They have __ before and after the name (e.g. __init__, __str__).
# We never call them directly; Python calls them automatically and that
# gives our objects special powers (printing, +, len(), [], for-loop, with...).

# ============================================================
# 1. __init__      -> constructor, runs when object is created
# 2. __str__       -> human-readable string, used by print()/str()
# 3. __repr__      -> developer/debug string, used by repr()
# 4. __add__       -> '+' operator
# 5. __eq__ / __lt__ / __gt__ -> comparison operators (==, <, >)
# 6. __len__       -> len(obj)
# 7. __getitem__ / __setitem__ -> obj[key] reading/writing
# 8. __contains__  -> 'in' operator
# 9. __iter__      -> makes object loop-able in for-loop
# 10. __call__     -> call object like a function: obj()
# 11. __enter__ / __exit__ -> with statement (context manager)
# ============================================================

class Book:
    def __init__(self, title, price):      # constructor
        self.title = title
        self.price = price

    def __str__(self):                     # print(book)
        return f"Book: {self.title} (Rs.{self.price})"

    def __repr__(self):                    # repr(book) / debug
        return f"Book('{self.title}', {self.price})"

    def __add__(self, other):              # book + book
        return Book(self.title + " & " + other.title, self.price + other.price)

    def __eq__(self, other):               # book == book
        return self.price == other.price

    def __lt__(self, other):               # book < book
        return self.price < other.price

    def __len__(self):                     # len(book) -> title length
        return len(self.title)

    def __call__(self, discount):          # book(10) -> call like a function
        return self.price - (self.price * discount / 100)


b1 = Book("Python", 500)
b2 = Book("DSA", 700)

print(b1)              # __str__   -> Book: Python (Rs.500)
print(repr(b1))        # __repr__  -> Book('Python', 500)
print(b1 + b2)         # __add__   -> Book: Python & DSA (Rs.1200)
print(b1 == b2)        # __eq__    -> False
print(b1 < b2)         # __lt__    -> True
print(len(b1))         # __len__   -> 6
print(b1(10))          # __call__  -> 450.0


# ------------------------------------------------------------
# Container / sequence dunder methods (make a class act like a list)
# ------------------------------------------------------------
class MyList:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):                     # len(m)
        return len(self.items)

    def __getitem__(self, index):          # m[0]
        return self.items[index]

    def __setitem__(self, index, value):   # m[1] = 99
        self.items[index] = value

    def __contains__(self, value):         # 99 in m
        return value in self.items

    def __iter__(self):                    # for x in m
        return iter(self.items)


m = MyList([10, 20, 30])
print(len(m))          # 3
print(m[0])            # 10
m[1] = 99
print(99 in m)         # True
for x in m:            # loop works because of __iter__
    print(x, end=" ")  # 10 99 30
print()


# ------------------------------------------------------------
# Context manager dunder methods (with statement)
# ------------------------------------------------------------
class Demo:
    def __enter__(self):                   # runs when 'with' starts
        print("Enter")
        return self

    def __exit__(self, exc_type, exc, tb): # runs when 'with' ends
        print("Exit")
        return False                       # False -> let errors propagate


with Demo():
    print("Inside")

# ------------------------------------------------------------
# QUICK SUMMARY
#   dunder        used by
#   __init__      obj = Class(...)
#   __str__       print(obj), str(obj)
#   __repr__      repr(obj)
#   __add__       obj + obj
#   __eq__/__lt__ obj == obj, obj < obj
#   __len__       len(obj)
#   __getitem__   obj[key]
#   __contains__  x in obj
#   __iter__      for x in obj
#   __call__      obj()
#   __enter__     with obj:
#   __exit__      end of with block
# ------------------------------------------------------------
