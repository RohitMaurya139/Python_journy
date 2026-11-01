"""
Topic: Object-Oriented Programming (OOP) - classes and objects
==============================================================

Definition:
    A class is a blueprint for creating objects.
    An object (instance) is a real value built from that blueprint.
    OOP groups related data (attributes) and behaviour (methods) together.

Vocabulary:
    - class     : the blueprint, e.g. Factory.
    - object    : an instance, e.g. reebok = Factory(...).
    - attribute : data stored on an object, e.g. self.material.
    - method    : a function defined inside a class, e.g. show().
    - self      : refers to the current object inside a method.
    - __init__  : the constructor, called automatically when an object is created.

Example:
    class Dog:
        def __init__(self, name):
            self.name = name

        def bark(self):
            print(self.name, "says woof")

    d = Dog("Tommy")
    d.bark()        # Tommy says woof
"""


class Factory:
    """A simple blueprint for a bag."""

    # Class attribute: shared by every object.
    a = 12

    def __init__(self, material, zips, pockets):
        """Constructor: store the given values on the current object."""
        self.material = material    # instance attribute
        self.zips = zips            # instance attribute
        self.pockets = pockets      # instance attribute

    def show(self):
        """Print the details of this bag."""
        print(f"Your object details are {self.material}, {self.zips}, {self.pockets}")


if __name__ == "__main__":
    # Accessing a class attribute without creating an object.
    print(Factory.a)

    # Creating objects (instances).
    reebok = Factory("leather", 3, 2)
    campus = Factory("nylon", 3, 3)

    print("\nreebok object")
    print(reebok.material)
    print(reebok.zips)
    print(reebok.pockets)
    reebok.show()

    print("\ncampus object")
    print(campus.material)
    print(campus.zips)
    print(campus.pockets)
    campus.show()





