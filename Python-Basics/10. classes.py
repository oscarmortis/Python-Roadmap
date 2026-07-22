#Create Class
class Person:
    pass


#Create Object
class Person:
    pass

person = Person()

print(person)


#Class Attribute
class Person:

    species = "Human"

print(Person.species)


#Instance Attribute
class Person:

    def __init__(self):
        self.name = "Oscar"

person = Person()

print(person.name)


#Constructor (__init__)
class Person:

    def __init__(self):
        print("Object Created")

person = Person()


#Constructor Parameters
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

person = Person("Oscar",23)

print(person.name)
print(person.age)


#self Keyword
class Person:

    def __init__(self,name):
        self.name = name

person = Person("Oscar")

print(person.name)


#Instance Method
class Person:

    def greet(self):
        print("Hello")

person = Person()

person.greet()


#Method with Parameters
class Person:

    def greet(self,name):
        print("Hello",name)

person = Person()

person.greet("Alex")


#Method Returning Value
class Calculator:

    def add(self,a,b):
        return a+b

calc = Calculator()

print(calc.add(10,20))


#Access Instance Variables
class Person:

    def __init__(self):
        self.name = "Oscar"

    def show(self):
        print(self.name)

person = Person()

person.show()


#Modify Instance Variable
class Person:

    def __init__(self):
        self.name = "Oscar"

person = Person()

person.name = "Alex"

print(person.name)


#Delete Instance Variable
class Person:

    def __init__(self):
        self.name = "Oscar"

person = Person()

del person.name


#Check Attribute
class Person:

    def __init__(self):
        self.name = "Oscar"

person = Person()

print(hasattr(person,"name"))


#Get Attribute
class Person:

    def __init__(self):
        self.name = "Oscar"

person = Person()

print(getattr(person,"name"))


#Set Attribute
class Person:
    pass

person = Person()

setattr(person,"age",23)

print(person.age)


#Delete Attribute
class Person:

    def __init__(self):
        self.age = 23

person = Person()

delattr(person,"age")


#Class Method
class Person:

    country = "India"

    @classmethod
    def show(cls):
        print(cls.country)

Person.show()


#Static Method
class Math:

    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(5,6))


#Class Variable
class Person:

    country = "India"

print(Person.country)


#Change Class Variable
class Person:

    country = "India"

Person.country = "USA"

print(Person.country)


#Instance vs Class Variable
class Person:

    country = "India"

    def __init__(self,name):
        self.name = name

person = Person("Oscar")

print(person.name)
print(person.country)


#Object Identity
class Person:
    pass

person = Person()

print(id(person))


#Object Type
class Person:
    pass

person = Person()

print(type(person))


#isinstance()
class Person:
    pass

person = Person()

print(isinstance(person,Person))


#Class Name
class Person:
    pass

print(Person.__name__)


#Class Documentation
class Person:
    """Person Class"""

print(Person.__doc__)


#Object Dictionary
class Person:

    def __init__(self):
        self.name = "Oscar"
        self.age = 23

person = Person()

print(person.__dict__)


#Class Dictionary
class Person:

    country = "India"

print(Person.__dict__)


#Multiple Objects
class Person:

    def __init__(self,name):
        self.name = name

p1 = Person("Oscar")
p2 = Person("Alex")

print(p1.name)
print(p2.name)


#Object Comparison
class Person:

    def __init__(self,name):
        self.name = name

p1 = Person("Oscar")
p2 = Person("Oscar")

print(p1 == p2)


#Method Calling Another Method
class Person:

    def greet(self):
        print("Hello")

    def welcome(self):
        self.greet()

person = Person()

person.welcome()


#Default Parameters
class Person:

    def __init__(self,name="Unknown"):
        self.name = name

person = Person()

print(person.name)


#Calculator Class
class Calculator:

    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

calc = Calculator()

print(calc.add(5,2))
print(calc.subtract(5,2))


#Bank Account
class Bank:

    def __init__(self,balance):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

account = Bank(1000)

account.deposit(500)

print(account.balance)

#Single Inheritance
class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):
    pass


dog = Dog()

dog.speak()


#Inheritance with Constructor
class Animal:

    def __init__(self,name):
        self.name = name


class Dog(Animal):
    pass


dog = Dog("Tommy")

print(dog.name)


#Method Overriding
class Animal:

    def speak(self):
        print("Animal Sound")


class Dog(Animal):

    def speak(self):
        print("Bark")


dog = Dog()

dog.speak()


#super()
class Animal:

    def __init__(self,name):
        self.name = name


class Dog(Animal):

    def __init__(self,name,breed):

        super().__init__(name)

        self.breed = breed


dog = Dog("Tommy","Labrador")

print(dog.name)
print(dog.breed)


#super() Method
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):

        super().speak()

        print("Dog")


dog = Dog()

dog.speak()


#Multilevel Inheritance
class A:

    def show(self):
        print("A")


class B(A):
    pass


class C(B):
    pass


obj = C()

obj.show()


#Multiple Inheritance
class Father:

    def money(self):
        print("Money")


class Mother:

    def love(self):
        print("Love")


class Child(Father,Mother):
    pass


child = Child()

child.money()
child.love()


#Hierarchical Inheritance
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


Dog().eat()
Cat().eat()


#issubclass()
class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog,Animal))


#isinstance()
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog,Dog))
print(isinstance(dog,Animal))


#Private Variable
class Person:

    def __init__(self):
        self.__salary = 50000


person = Person()

#print(person.__salary)


#Private Method
class Person:

    def __hello(self):
        print("Hello")


    def greet(self):
        self.__hello()


person = Person()

person.greet()


#Protected Variable
class Person:

    def __init__(self):
        self._age = 23


person = Person()

print(person._age)


#Getter
class Person:

    def __init__(self):
        self.__age = 23


    def get_age(self):
        return self.__age


person = Person()

print(person.get_age())


#Setter
class Person:

    def __init__(self):
        self.__age = 23


    def set_age(self,age):
        self.__age = age


person = Person()

person.set_age(30)

print(person.get_age())


#Property Getter
class Person:

    def __init__(self):
        self.__age = 23


    @property
    def age(self):
        return self.__age


person = Person()

print(person.age)


#Property Setter
class Person:

    def __init__(self):
        self.__age = 23


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self,value):
        self.__age = value


person = Person()

person.age = 30

print(person.age)


#Property Deleter
class Person:

    def __init__(self):
        self.__age = 23


    @property
    def age(self):
        return self.__age


    @age.deleter
    def age(self):
        del self.__age


person = Person()

del person.age


#Read Only Property
class Circle:

    def __init__(self,radius):
        self.radius = radius


    @property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)

print(circle.area)


#Method Resolution Order
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B,C):
    pass


print(D.mro())


#Override Class Variable
class Animal:

    species = "Animal"


class Dog(Animal):

    species = "Dog"


print(Dog.species)


#Call Parent Method
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def eat(self):

        super().eat()

        print("Dog Eats")


Dog().eat()


#Constructor Overriding
class Animal:

    def __init__(self):
        print("Animal")


class Dog(Animal):

    def __init__(self):

        super().__init__()

        print("Dog")


Dog()


#Employee Example
class Employee:

    def __init__(self,name,salary):

        self.name = name

        self.salary = salary


class Manager(Employee):

    def display(self):

        print(self.name)

        print(self.salary)


manager = Manager("Oscar",50000)

manager.display()

#String Representation
class Person:

    def __str__(self):
        return "Person Object"

person = Person()

print(person)


#Official Representation
class Person:

    def __repr__(self):
        return "Person()"

person = Person()

print(repr(person))


#Object Length
class Team:

    def __len__(self):
        return 5

team = Team()

print(len(team))


#Object Boolean
class User:

    def __bool__(self):
        return True

user = User()

print(bool(user))


#Callable Object
class Calculator:

    def __call__(self,a,b):
        return a+b

calc = Calculator()

print(calc(10,20))


#Equality
class Person:

    def __init__(self,name):
        self.name = name

    def __eq__(self,other):
        return self.name == other.name

p1 = Person("Oscar")
p2 = Person("Oscar")

print(p1 == p2)


#Less Than
class Number:

    def __init__(self,value):
        self.value = value

    def __lt__(self,other):
        return self.value < other.value

print(Number(10) < Number(20))


#Greater Than
class Number:

    def __init__(self,value):
        self.value = value

    def __gt__(self,other):
        return self.value > other.value

print(Number(20) > Number(10))


#Addition Operator
class Number:

    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return self.value + other.value

print(Number(10) + Number(20))


#Subtraction Operator
class Number:

    def __init__(self,value):
        self.value = value

    def __sub__(self,other):
        return self.value - other.value

print(Number(20) - Number(5))


#Multiplication Operator
class Number:

    def __init__(self,value):
        self.value = value

    def __mul__(self,other):
        return self.value * other.value

print(Number(5) * Number(4))


#Division Operator
class Number:

    def __init__(self,value):
        self.value = value

    def __truediv__(self,other):
        return self.value / other.value

print(Number(20) / Number(5))


#Contains
class Team:

    def __contains__(self,item):
        return item in ["Oscar","Alex"]

team = Team()

print("Oscar" in team)


#Item Access
class Numbers:

    def __getitem__(self,index):
        return [10,20,30][index]

numbers = Numbers()

print(numbers[1])


#Item Assignment
class Numbers:

    def __init__(self):
        self.data = [1,2,3]

    def __setitem__(self,index,value):
        self.data[index] = value

numbers = Numbers()

numbers[1] = 100

print(numbers.data)


#Iterator
class Counter:

    def __iter__(self):
        return iter([1,2,3])

for number in Counter():
    print(number)


#Next
class Counter:

    def __iter__(self):
        return self

    def __next__(self):

        raise StopIteration

counter = Counter()

print(list(counter))


#Destructor
class Person:

    def __del__(self):
        print("Object Destroyed")

person = Person()

del person


#Abstract Class
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Bark")

Dog().speak()


#Composition
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()

car = Car()

car.engine.start()


#Aggregation
class Teacher:

    def __init__(self,name):
        self.name = name


class School:

    def __init__(self,teacher):
        self.teacher = teacher

teacher = Teacher("Oscar")

school = School(teacher)

print(school.teacher.name)


#Shallow Copy
import copy

numbers = [[1],[2]]

new_numbers = copy.copy(numbers)

print(new_numbers)


#Deep Copy
import copy

numbers = [[1],[2]]

new_numbers = copy.deepcopy(numbers)

print(new_numbers)


#Dataclass
from dataclasses import dataclass

@dataclass
class Person:

    name:str
    age:int

person = Person("Oscar",23)

print(person)


#Slots
class Person:

    __slots__ = ("name","age")

    def __init__(self):

        self.name = "Oscar"

        self.age = 23

person = Person()

print(person.name)


#Class Decorator
def decorate(cls):

    cls.country = "India"

    return cls

@decorate
class Person:
    pass

print(Person.country)


#Static Variable Counter
class Person:

    count = 0

    def __init__(self):

        Person.count += 1

Person()

Person()

print(Person.count)


#Factory Method
class Person:

    def __init__(self,name):
        self.name = name

    @classmethod
    def create(cls):
        return cls("Oscar")

person = Person.create()

print(person.name)


#Object Copy
class Person:

    def __init__(self,name):
        self.name = name

import copy

p1 = Person("Oscar")

p2 = copy.copy(p1)

print(p2.name)


#Check Attribute
class Person:

    pass

print(hasattr(Person,"__dict__"))


#Dynamic Attribute
class Person:
    pass

person = Person()

person.city = "Delhi"

print(person.city)


#Delete Object
class Person:
    pass

person = Person()

del person


#Object Hash
class Person:
    pass

person = Person()

print(hash(person))

#Not Equal
class Number:

    def __init__(self,value):
        self.value = value

    def __ne__(self,other):
        return self.value != other.value

print(Number(10) != Number(20))


#Less Than or Equal
class Number:

    def __init__(self,value):
        self.value = value

    def __le__(self,other):
        return self.value <= other.value

print(Number(10) <= Number(20))


#Greater Than or Equal
class Number:

    def __init__(self,value):
        self.value = value

    def __ge__(self,other):
        return self.value >= other.value

print(Number(20) >= Number(10))


#Hash
class Person:

    def __init__(self,name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

person = Person("Oscar")

print(hash(person))


#Context Manager
class File:

    def __enter__(self):
        print("Opened")
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        print("Closed")

with File():
    print("Working")


#__new__
class Person:

    def __new__(cls):
        print("Creating Object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing")

person = Person()


#Descriptor
class Positive:

    def __set_name__(self,owner,name):
        self.name = name

    def __get__(self,instance,owner):
        return instance.__dict__[self.name]

    def __set__(self,instance,value):

        if value < 0:
            raise ValueError("Positive Only")

        instance.__dict__[self.name] = value


class Product:

    price = Positive()


product = Product()

product.price = 100

print(product.price)


#Singleton Pattern
class Database:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


db1 = Database()
db2 = Database()

print(db1 is db2)


#Class Inheritance Chain
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.__mro__)


#Object Copy Method
import copy

class Person:

    def __init__(self,name):
        self.name = name


person = Person("Oscar")

new_person = copy.deepcopy(person)

print(new_person.name)


#Inheritance Check
class Animal:
    pass


class Dog(Animal):
    pass


print(Dog.__bases__)


#Subclass List
class Animal:
    pass


class Dog(Animal):
    pass


print(Animal.__subclasses__())


#Object Variables
class Person:

    def __init__(self):
        self.name = "Oscar"
        self.age = 23


person = Person()

print(vars(person))


#Class Variables
class Person:

    country = "India"


print(vars(Person))


#Delete Attribute
class Person:

    age = 23


del Person.age


#Dynamic Method
class Person:
    pass


def greet(self):
    print("Hello")


Person.greet = greet

person = Person()

person.greet()


#Lambda Method
class Math:

    square = lambda self,x: x*x


math = Math()

print(math.square(5))


#Property Validation
class Person:

    def __init__(self):
        self.__age = 18


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self,value):

        if value < 0:
            raise ValueError("Invalid Age")

        self.__age = value


person = Person()

person.age = 25

print(person.age)


#Inheritance with Property
class Animal:

    @property
    def sound(self):
        return "Animal"


class Dog(Animal):

    @property
    def sound(self):
        return "Bark"


dog = Dog()

print(dog.sound)


#Class Counter
class Student:

    total = 0

    def __init__(self):

        Student.total += 1


Student()
Student()
Student()

print(Student.total)


#Simple Iterator Class
class Counter:

    def __init__(self):
        self.value = 1


    def __iter__(self):
        return self


    def __next__(self):

        if self.value > 5:
            raise StopIteration

        number = self.value

        self.value += 1

        return number


for i in Counter():
    print(i)


#Generator Method
class Counter:

    def numbers(self):

        for i in range(5):
            yield i


counter = Counter()

for number in counter.numbers():
    print(number)


#Employee Example
class Employee:

    def __init__(self,name,salary):

        self.name = name

        self.salary = salary


    def display(self):

        print(self.name)
        print(self.salary)


employee = Employee("Oscar",50000)

employee.display()


#Student Example
class Student:

    def __init__(self,name,marks):

        self.name = name
        self.marks = marks


    def grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        return "Fail"


student = Student("Oscar",88)

print(student.grade())


#Bank Account Example
class BankAccount:

    def __init__(self,balance):

        self.balance = balance


    def deposit(self,amount):

        self.balance += amount


    def withdraw(self,amount):

        if amount <= self.balance:
            self.balance -= amount


    def show(self):

        print(self.balance)


account = BankAccount(1000)

account.deposit(500)
account.withdraw(300)

account.show()


#Rectangle Example
class Rectangle:

    def __init__(self,length,width):

        self.length = length
        self.width = width


    def area(self):
        return self.length * self.width


    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10,5)

print(rectangle.area())
print(rectangle.perimeter())


#Circle Example
class Circle:

    def __init__(self,radius):

        self.radius = radius


    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)

print(circle.area())