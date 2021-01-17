class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.printName()
