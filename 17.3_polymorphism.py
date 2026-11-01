# class Animal:
#     def show(self):
#         print("hello i am Animal")
#     def show(self,name): # this is method overloading (like we create different method with same name but different parameters )in other complie type lang. like c,c++,java etc. but in python it is not possible  because it overwrite the existing method
#         pass

# class Human(Animal):
#     def show(self):  #method overRiding
#         print("hello i am  Human")

# obj= Human()
# obj.show()

#  duck TYping 
class Animal:
    def show(self):
       print("hello i am Animal")
class Human:
    def show(self):
       print("hello i am Human")


obj=Animal()
obj2=Human()

obj.show()
obj2.show()

# ============================================================
# POLYMORPHISM = "many forms". The same method/operator call behaves
# differently depending on the object that receives it.
# Your code above already shows it: obj.show() and obj2.show() call the
# SAME method name but print different messages.
# ============================================================

for obj in (Animal(), Human()):
    obj.show()   # hello i am Animal / hello i am Human

# ------------------------------------------------------------
# WAY 1: DUCK TYPING (no inheritance needed)
# Your Animal and Human (lines 15-20) have NO parent-child relation,
# but both define show(), so the same call works on both. That is exactly
# the duck typing below. "If it walks like a duck and quacks like a duck,
# it's a duck." Python only cares that the method exists.
# ------------------------------------------------------------
class Duck:
    def sound(self): print("Quack")
class Dog:
    def sound(self): print("Woof")
for a in (Duck(), Dog()):
    a.sound()   # Quack / Woof

# ------------------------------------------------------------
# WAY 2: METHOD OVERRIDING (inheritance, runtime polymorphism)
# Your commented code at the top (lines 7-12) is this: Human(Animal)
# redefines show(), so the child version wins.
# ------------------------------------------------------------
class Animal:
    def show(self): print("hello i am Animal")
class Human(Animal):
    def show(self): print("hello i am Human")   # overrides parent
Animal().show()   # hello i am Animal
Human().show()    # hello i am Human

# ------------------------------------------------------------
# WAY 3: METHOD OVERLOADING -> NOT supported directly in Python
# Your lines 2-5: defining show() again with (self, name) overwrites the
# first show(). Only ONE method survives. Emulate it with default args:
# ------------------------------------------------------------
class Animal:
    def show(self, name=None):
        if name:
            print("hello i am", name)
        else:
            print("hello i am Animal")
Animal().show()          # hello i am Animal
Animal().show("Rohit")   # hello i am Rohit

# ------------------------------------------------------------
# WAY 4: OPERATOR OVERLOADING (dunder / magic methods)
# Extending your Animal with __add__ so '+' does something new.
# ------------------------------------------------------------
class Animal:
    def __init__(self, age): self.age = age
    def __add__(self, other): return Animal(self.age + other.age)
a = Animal(2) + Animal(3)
print(a.age)   # 5

# ------------------------------------------------------------
# WAY 5: BUILT-IN POLYMORPHISM
# len("abc"), len([1,2,3]), len({"a":1}); '+' for int/str/list.
# Same function/operator, different behavior per type.
# ------------------------------------------------------------

# ------------------------------------------------------------
# WAY 6: POLYMORPHISM WITH ABSTRACT CLASSES (enforced interface)
# Same Animal/Human idea, but now Animal forces every child to
# implement show() its own way.
# ------------------------------------------------------------
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def show(self): ...
class Human(Animal):
    def show(self): print("hello i am Human")
class Robot(Animal):
    def show(self): print("hello i am Robot")
for a in (Human(), Robot()):
    a.show()   # hello i am Human / hello i am Robot
