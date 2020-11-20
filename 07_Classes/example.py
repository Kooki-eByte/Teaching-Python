#  Classes
class Person:
    # __ init __ (sometimes referred to as dunder init)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # class method
    # def walking(self):
    #     print(f"{self.name} is now walking")


p1 = Person("Bob", 28)

print(p1.name)
print(p1.age)
# p1.walking()


# Inheritance
class Student(Person):
    # We use pass here if we dont want to to give Student any properties of its own
    pass


s1 = Student("John", 30)

print(f" Hi, my name is {s1.name} and I am {s1.age} years old")
