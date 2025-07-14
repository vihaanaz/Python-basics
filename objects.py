class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def myfunc(self):
            print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person:
    def __init__(mysillyobject, name, age) -> None:
        mysillyobject.name = name
        mysillyobject.age = age

        def myfunc(abc):
            print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Python inheritance split into parent class and child class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()


