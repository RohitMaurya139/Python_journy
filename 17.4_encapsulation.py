# class Factory:
#     a="pune" # public attribute
#     _b="mumbai" # protected attribute (in python public and projected is same)
#     __c="thane" # private attribute only accessible inside their own class 
#     def show(self):
#        print(f"hello i am pune factory {Factory.__c}")


# class DelhiFactory(Factory):
#     b="Delhi"
#     def show(self):
#        print("hello i am Delhi Factory")
# obj=DelhiFactory()
# obj1=Factory()
# print(obj.a)  # child class also access paraent property
# print(obj._b)  # child class also access paraent property
# obj1.show()


class demo:
    def __init__(self,name,age,salary):
        self.name=name
        self._age=age
        self.__salary=salary
    def show(self):
        print("Inside the class:")
        print("Public: ", self.name)
        print("Protected: ", self._age)
        print("Private: ", self.__salary)


obj=demo("Rohit",26,45000)
obj.show()

# ============================================================
# ENCAPSULATION = wrapping data + the methods that use it into one unit
# (a class) and controlling/restricting direct access to that data.
# Python uses naming conventions instead of strict access modifiers.
#
# Your demo class shows the 3 levels:
#   name       -> public    : accessible anywhere
#   _age       -> protected : "internal use" by convention (still accessible)
#   __salary   -> private   : name-mangled to _demo__salary (not truly hidden)
# ============================================================

print(obj.name)          # Rohit
print(obj._age)          # 26  -> still works, just a warning to devs
print(obj.__salary)      # AttributeError
print(obj._demo__salary) # 45000 -> mangled name, so not truly private

# ------------------------------------------------------------
# WAY 1: NAME MANGLING
# Python renames __salary to _demo__salary. It is not real security, it just
# avoids accidental access/override in subclasses.
# ------------------------------------------------------------

# ------------------------------------------------------------
# WAY 2: GETTERS & SETTERS (controlled access + validation)
# ------------------------------------------------------------
class demo:
    def __init__(self, salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")
obj = demo(45000)
print(obj.get_salary())   # 45000
obj.set_salary(-5)        # Invalid salary

# ------------------------------------------------------------
# WAY 3: @property (Pythonic getter/setter)
# ------------------------------------------------------------
class demo:
    def __init__(self, salary):
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Invalid salary")
obj = demo(45000)
print(obj.salary)    # 45000 (getter)
obj.salary = 50000   # setter with validation

# ------------------------------------------------------------
# WAY 4: PROTECTED IS ONLY A CONVENTION
# Unlike Java/C++, _age (and even __salary via _demo__salary) can still be
# reached. Python's philosophy: "we are all consenting adults".
# ------------------------------------------------------------
       