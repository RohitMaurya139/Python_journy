"""
Topic: Inheritance in Python (17.2)
===================================

Definition:
    Inheritance is an object-oriented feature in which a new class
    (the child / derived / subclass) acquires the attributes and methods
    of an existing class (the parent / base / superclass).

    The child class can:
        - reuse the parent's code,
        - add new attributes and methods,
        - override parent methods to change their behaviour.

Terms:
    Parent / base / superclass     : the class being inherited from.
    Child / derived / subclass     : the class that inherits.
    Overriding                     : redefining a parent method in the child
                                     with the same name.
    super()                        : calls the parent version of a method.
    MRO (Method Resolution Order)  : the order in which Python searches
                                     parent classes for a method. This matters
                                     most in multiple inheritance.

Syntax:
    class Child(Parent):
        pass

Example:
    class Animal:
        def speak(self):
            return "Some sound"

    class Dog(Animal):
        def speak(self):
            return "Woof"

Types of inheritance:
    Type           Description                          Example
    -------------  -----------------------------------  ---------------------------
    Single         one child, one parent                Dog(Animal)
    Multiple       one child, more than one parent      Duck(Flyer, Swimmer)
    Multilevel     child -> parent -> grandparent       SportsCar(Car(Vehicle))
    Hierarchical   one parent, more than one child      Dog(Animal), Cat(Animal)
    Hybrid         a combination of the above types     e.g. multiple + multilevel

Method overriding vs method overloading:
    Overriding : the child replaces a parent method that has the same name.
    Overloading: several methods with the same name but different parameters.
                 Python does not support this directly. Use default arguments
                 or *args instead.

super() vs Parent.method(self):
    super() follows the MRO and is the safer choice, especially with
    multiple inheritance.
    Parent.method(self) calls one specific parent directly.

Useful checks:
    isinstance(object, Class)  -> is this object an instance of the class
                                  (or of one of its children)?
    issubclass(Child, Parent)  -> is Child a subclass of Parent?

Benefits:
    - Code reuse: common behaviour stays in the parent class.
    - Extensibility: add new features without rewriting the parent.
    - Polymorphism: different child classes can be used through the same
      parent interface.

Caution:
    Inheritance models an "is-a" relationship (a Dog is an Animal).
    If the relationship is "has-a" (a Car has an Engine), prefer composition.
"""


# ---- 1. Single inheritance ----
class Animal:
    """Parent class."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

    def info(self):
        return f"I am {self.name}"


class Dog(Animal):
    """Child class: inherits name, info and speak from Animal."""

    def speak(self):
        """Override the parent method."""
        return "Woof"


class Cat(Animal):
    """Another child of Animal: this is also hierarchical inheritance."""

    def speak(self):
        return "Meow"


def demo_single_inheritance():
    dog = Dog("Tommy")
    cat = Cat("Kitty")

    print("Dog info:", dog.info())        # inherited method
    print("Dog speak:", dog.speak())      # overridden method
    print("Cat info:", cat.info())
    print("Cat speak:", cat.speak())


# ---- 2. super() and extending __init__ ----
class Employee:
    """Parent class with common employee data."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        return f"{self.name} earns {self.salary}"


class Manager(Employee):
    """Child class that adds team_size."""

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # call Employee.__init__
        self.team_size = team_size

    def details(self):
        base_details = super().details()  # call Employee.details
        return f"{base_details} and manages {self.team_size} people"


def demo_super():
    manager = Manager("Rohit", 80000, 5)
    print(manager.details())


# ---- 3. Multilevel inheritance ----
class Vehicle:
    """Grandparent class."""

    wheels = 4      # class attribute, inherited by children

    def start(self):
        return "Vehicle started"


class Car(Vehicle):
    """Parent class: inherits from Vehicle."""

    def wheels_info(self):
        return f"Car has {self.wheels} wheels"


class SportsCar(Car):
    """Child class: inherits from Car, which inherits from Vehicle."""

    def speed(self):
        return "Sports car can go very fast"


def demo_multilevel():
    car = SportsCar()

    print(car.start())          # from Vehicle
    print(car.wheels_info())    # from Car
    print(car.speed())          # from SportsCar
    print("Inherited wheels:", car.wheels)


# ---- 4. Multiple inheritance and MRO ----
class Flyer:
    def move(self):
        return "Flying"


class Swimmer:
    def move(self):
        return "Swimming"


class Duck(Flyer, Swimmer):
    """Inherits from two parent classes."""

    def move(self):
        # Call both parent versions explicitly.
        return f"{Flyer.move(self)} and {Swimmer.move(self)}"


def demo_multiple_inheritance():
    duck = Duck()

    print("Duck move:", duck.move())
    print("MRO:", [cls.__name__ for cls in Duck.__mro__])


# ---- 5. The diamond problem and MRO ----
class A:
    def show(self):
        return "A"


class B(A):
    def show(self):
        return "B"


class C(A):
    def show(self):
        return "C"


class D(B, C):
    """D inherits from B and C, and both inherit from A."""

    pass


def demo_diamond():
    print("D().show():", D().show())
    print("D MRO:", [cls.__name__ for cls in D.__mro__])
    print("Explanation: Python searches D -> B -> C -> A -> object.")


# ---- 6. isinstance() and issubclass() ----
def demo_type_checks():
    dog = Dog("Tommy")
    duck = Duck()

    print("isinstance(dog, Dog):", isinstance(dog, Dog))          # True
    print("isinstance(dog, Animal):", isinstance(dog, Animal))    # True
    print("issubclass(Dog, Animal):", issubclass(Dog, Animal))    # True
    print("issubclass(Animal, Dog):", issubclass(Animal, Dog))    # False
    print("isinstance(duck, Flyer):", isinstance(duck, Flyer))    # True
    print("isinstance(duck, Swimmer):", isinstance(duck, Swimmer))  # True


# ---- 7. Polymorphism ----
def demo_polymorphism():
    animals = [Dog("Tommy"), Cat("Kitty")]

    for animal in animals:
        print(f"{animal.name} says {animal.speak()}")


def main():
    print("---- 1. Single inheritance ----")
    demo_single_inheritance()

    print("\n---- 2. super() ----")
    demo_super()

    print("\n---- 3. Multilevel inheritance ----")
    demo_multilevel()

    print("\n---- 4. Multiple inheritance and MRO ----")
    demo_multiple_inheritance()

    print("\n---- 5. Diamond problem and MRO ----")
    demo_diamond()

    print("\n---- 6. isinstance() and issubclass() ----")
    demo_type_checks()

    print("\n---- 7. Polymorphism ----")
    demo_polymorphism()


if __name__ == "__main__":
    main()
