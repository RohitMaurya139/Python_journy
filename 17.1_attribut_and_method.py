"""
Topic: Attributes and methods in a class (17.1)
===============================================

1. Attribute
------------
Definition:
    An attribute is a variable that stores data for a class or an object.
    It describes the "state" of the object.

Two main kinds:
    - Class attribute    : defined directly in the class body.
                           It is shared by every object of that class.
    - Instance attribute : created with self.<name>, usually inside __init__.
                           Every object gets its own separate copy.

Difference between class attribute and instance attribute:
    Feature          Class attribute                  Instance attribute
    ---------------  -------------------------------  ------------------------------
    Created in       the class body                   __init__ or another method
    Shared?          Yes, one copy for all objects    No, one copy per object
    Accessed with    ClassName.attr or obj.attr       obj.attr
    Changed with     ClassName.attr = value            self.attr = value
    Typical use      constants, counters, defaults     name, age, marks, etc.

Example:
    class Student:
        school = "ABC School"          # class attribute

        def __init__(self, name):
            self.name = name           # instance attribute

2. Method
---------
Definition:
    A method is a function defined inside a class. It describes the
    "behaviour" of the class or its objects.

Types of methods:
    - Instance method : works with one object. The first parameter is self.
    - Class method    : works with the class. The first parameter is cls.
                        It is decorated with @classmethod.
    - Static method   : receives neither self nor cls. It is a normal function
                        placed inside the class for organisation.
                        It is decorated with @staticmethod.
    - Property        : a method that is used like an attribute (no parentheses).
                        It is decorated with @property.
    - Dunder method   : a special method whose name starts and ends with "__",
                        for example __init__, __str__, __repr__, __len__, __eq__.

Difference between instance method, class method and static method:
    Feature             Instance method        Class method           Static method
    ------------------  ---------------------  ---------------------  --------------------
    Decorator           none                   @classmethod           @staticmethod
    First parameter     self                   cls                    none
    Works with          the object             the class              only its arguments
    Reads/writes
    instance attributes Yes                    No                     No
    Reads/writes
    class attributes    Yes (via self)         Yes (via cls)          Yes (via class name)
    Called as           obj.method()           Class.method()         Class.method()
    Common use          change object state    alternative            helper/utility
                                               constructors,          functions
                                               class-level state

Difference between an attribute and a method:
    Attribute stores data     : obj.name        (no parentheses)
    Method performs an action : obj.display()   (parentheses)

Example:
    class Student:
        def __init__(self, name):
            self.name = name

        def show(self):                # instance method
            print(self.name)

        @classmethod
        def create(cls, name):         # class method
            return cls(name)

        @staticmethod
        def is_pass(marks):            # static method
            return sum(marks) >= 40
"""


class Student:
    """A simple class that demonstrates attributes and methods."""

    # ---- Class attributes: shared by every object ----
    school_name = "ABC Public School"
    total_students = 0

    # ---- Constructor: a special (dunder) method ----
    def __init__(self, name, marks):
        # ---- Instance attributes: unique to each object ----
        self.name = name
        self.marks = marks
        Student.total_students += 1     # update the shared class attribute

    # ---- 1. Instance method ----
    def average(self):
        """Return the average marks of this student."""
        return sum(self.marks) / len(self.marks)

    def display(self):
        """Print this student's details."""
        print(f"{self.name} studies at {self.school_name} and scored {self.marks}")

    # ---- 2. Class method: alternative constructor ----
    @classmethod
    def from_string(cls, data):
        """Create a Student from text like 'Rohit,90-80-85'.

        cls refers to the class itself (Student), so this method can create
        and return a new object.
        """
        name, marks_text = data.split(",")
        marks = [int(mark) for mark in marks_text.split("-")]
        return cls(name, marks)

    # ---- 3. Class method: change class-level state ----
    @classmethod
    def change_school(cls, new_name):
        """Change the school name for every object."""
        cls.school_name = new_name

    # ---- 4. Static method: helper that needs no object/class data ----
    @staticmethod
    def is_pass(marks):
        """Return True when the average is at least 40.

        This method does not need self or cls because it only uses its argument.
        """
        return sum(marks) / len(marks) >= 40

    # ---- 5. Property: used like an attribute, computed by a method ----
    @property
    def grade(self):
        """Return the grade based on the average marks."""
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        return "Fail"

    # ---- 6. Dunder method: controls print(object) ----
    def __str__(self):
        return f"Student(name={self.name!r}, marks={self.marks})"


def main():
    # Create objects using __init__.
    s1 = Student("Rohit", [90, 80, 85])
    s2 = Student.from_string("Amit,70-65-80")   # class method as constructor

    # Instance methods.
    s1.display()
    s2.display()
    print("s1 average:", s1.average())
    print("s2 average:", s2.average())

    # Property: used without parentheses, like an attribute.
    print("s1 grade:", s1.grade)
    print("s2 grade:", s2.grade)

    # Static method: can be called on the class or on an object.
    print("Is s2 passing?", Student.is_pass(s2.marks))
    print("Is s1 passing?", s1.is_pass(s1.marks))

    # Class attributes are shared by all objects.
    print("Total students:", Student.total_students)
    print("Class school:", Student.school_name)
    print("s1 school:", s1.school_name)
    print("s2 school:", s2.school_name)

    # Setting an attribute on one object creates an INSTANCE attribute.
    # It shadows the class attribute for that object only.
    s1.school_name = "Changed for s1 only"
    print("\nAfter s1.school_name is changed:")
    print("Class school:", Student.school_name)
    print("s1 school:", s1.school_name)
    print("s2 school:", s2.school_name)

    # Deleting the instance attribute makes s1 use the class attribute again.
    del s1.school_name
    print("After deleting s1.school_name:", s1.school_name)

    # Changing the class attribute through a class method affects every object.
    Student.change_school("New ABC School")
    print("\nAfter Student.change_school(...):")
    print("Class school:", Student.school_name)
    print("s1 school:", s1.school_name)
    print("s2 school:", s2.school_name)

    # An instance method can also be called through the class by passing
    # the object explicitly as self.
    print("Average via class call:", Student.average(s1))

    # The dunder method __str__ is used automatically by print().
    print(s1)
    print(s2)


if __name__ == "__main__":
    main()
