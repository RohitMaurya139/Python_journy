from abc import ABC, abstractmethod

class Abstract(ABC):          # abstract class -> cannot be instantiated directly
    @abstractmethod           # must be implemented by every subclass
    def perimeter(self):
        pass 
    @abstractmethod           # must be implemented by every subclass
    def area(self):
        pass 

class Square(Abstract):
    def __init__(self,side):
        self.side=side
    # NOTE: Square does NOT implement perimeter() and area(),
    # so Square(5) would raise TypeError (missing abstract methods).
    # To fix it, uncomment the two methods below:
    # def perimeter(self):
    #     print("Square perimeter =", 4 * self.side)
    # def area(self):
    #     print("Square area =", self.side ** 2)

class Circle(Abstract):
    def __init__(self,radius):
        self.side=radius
    def perimeter(self):         # implementation of abstract method
        print("i have created perimeter")
    def area(self):              # implementation of abstract method
        print("i have created area")

obj=Circle(7)        # only creates the object; methods are not called yet
obj.perimeter()      # i have created perimeter
obj.area()           # i have created area

# ============================================================
# ABSTRACTION = hiding implementation details and exposing only the
# essential interface. You say WHAT a class must do, not HOW it does it.
# In Python this is done with ABC + @abstractmethod.
#
# Your file:
#   Abstract(ABC) -> the contract: every shape MUST have perimeter() + area()
#   Circle        -> implements both -> can be created
#   Square        -> implements neither -> Square(5) would raise TypeError
#   Circle(7)     -> just creates the object, methods are not called yet
# ============================================================

# Abstract()     # TypeError: Can't instantiate abstract class
# Square(5)      # TypeError: missing perimeter(), area()

# ------------------------------------------------------------
# WAY 1: ABC + @abstractmethod (what you used above)
# Best for enforcing a contract at object-creation time.
# ------------------------------------------------------------
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): ...
    @abstractmethod
    def perimeter(self): ...
class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

# ------------------------------------------------------------
# WAY 2: RAISING NotImplementedError (manual, old-style)
# No instantiation blocking -> fails only when the method is called.
# ------------------------------------------------------------
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2

# ------------------------------------------------------------
# WAY 3: DUCK TYPING / Protocol (interface without inheritance)
# Anything with an area() method satisfies the interface.
# ------------------------------------------------------------
from typing import Protocol
class Shape(Protocol):
    def area(self) -> float: ...
class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r ** 2
def show_area(s: Shape):
    print(s.area())
show_area(Circle(7))   # 153.86

# ------------------------------------------------------------
# ABSTRACTION vs ENCAPSULATION
# Encapsulation protects data (__salary).
# Abstraction hides behavior/complexity and forces a contract
# (@abstractmethod).
# ------------------------------------------------------------
