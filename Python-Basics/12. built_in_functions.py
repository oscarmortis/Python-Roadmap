#abs()
print(abs(-25))


#all()
numbers = [True, True, True]

print(all(numbers))


#any()
numbers = [False, False, True]

print(any(numbers))


#ascii()
print(ascii("Pythön"))


#bin()
print(bin(25))


#bool()
print(bool(1))
print(bool(0))


#bytearray()
data = bytearray([65,66,67])

print(data)


#bytes()
data = bytes([65,66,67])

print(data)


#callable()
def greet():
    pass

print(callable(greet))


#chr()
print(chr(65))


#ord()
print(ord("A"))


#complex()
print(complex(5,3))


#dict()
student = dict(name="Oscar", age=23)

print(student)


#dir()
print(dir(str))


#divmod()
print(divmod(17,5))


#enumerate()
letters = ["a","b","c"]

for index, letter in enumerate(letters):
    print(index, letter)


#filter()
numbers = [1,2,3,4,5,6]

even = list(filter(lambda x:x%2==0,numbers))

print(even)


#float()
print(float(10))


#format()
print(format(255,"x"))


#frozenset()
numbers = frozenset([1,2,3])

print(numbers)


#hash()
print(hash("Python"))


#hex()
print(hex(255))


#id()
numbers = [1,2,3]

print(id(numbers))


#input()
#name = input("Name : ")
#print(name)


#int()
print(int("100"))


#isinstance()
print(isinstance(10,int))


#issubclass()
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog,Animal))


#iter()
numbers = [1,2,3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))


#len()
print(len("Python"))


#list()
numbers = list(range(5))

print(numbers)


#locals()
name = "Oscar"

print(locals())

#map()
numbers = [1,2,3,4]

square = list(map(lambda x:x*x, numbers))

print(square)


#max()
numbers = [10,5,20,8]

print(max(numbers))


#min()
numbers = [10,5,20,8]

print(min(numbers))


#memoryview()
data = bytes([65,66,67])

view = memoryview(data)

print(view[0])


#next()
numbers = iter([10,20,30])

print(next(numbers))
print(next(numbers))


#object()
obj = object()

print(obj)


#oct()
print(oct(64))


#open()
file = open("test.txt","w")

file.write("Hello Python")

file.close()


#pow()
print(pow(2,5))
print(pow(2,5,3))


#print()
print("Hello")
print("Python", end="!")
print()


#property()
class Person:

    def __init__(self):
        self.__age = 23

    @property
    def age(self):
        return self.__age

person = Person()

print(person.age)


#range()
for i in range(5):
    print(i)


#repr()
text = "Python"

print(repr(text))


#reversed()
numbers = [1,2,3,4]

print(list(reversed(numbers)))


#round()
print(round(3.14159,2))


#set()
numbers = set([1,2,2,3])

print(numbers)


#setattr()
class Person:
    pass

person = Person()

setattr(person,"name","Oscar")

print(person.name)


#slice()
text = "Python"

print(text[slice(1,4)])


#sorted()
numbers = [5,1,4,2]

print(sorted(numbers))


#sorted() Reverse
numbers = [5,1,4,2]

print(sorted(numbers, reverse=True))


#sorted() with Key
words = ["apple","kiwi","banana"]

print(sorted(words, key=len))


#staticmethod()
class Math:

    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(5,6))


#str()
print(str(100))


#sum()
numbers = [10,20,30]

print(sum(numbers))


#super()
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):

        super().speak()

        print("Dog")


Dog().speak()


#tuple()
numbers = tuple([1,2,3])

print(numbers)


#type()
print(type(100))
print(type("Python"))


#vars()
class Person:

    def __init__(self):

        self.name = "Oscar"

person = Person()

print(vars(person))


#zip()
names = ["Oscar","Alex"]
ages = [23,21]

print(list(zip(names,ages)))

#map()
numbers = [1,2,3,4]

square = list(map(lambda x:x*x, numbers))

print(square)


#max()
numbers = [10,5,20,8]

print(max(numbers))


#min()
numbers = [10,5,20,8]

print(min(numbers))


#memoryview()
data = bytes([65,66,67])

view = memoryview(data)

print(view[0])


#next()
numbers = iter([10,20,30])

print(next(numbers))
print(next(numbers))


#object()
obj = object()

print(obj)


#oct()
print(oct(64))


#open()
file = open("test.txt","w")

file.write("Hello Python")

file.close()


#pow()
print(pow(2,5))
print(pow(2,5,3))


#print()
print("Hello")
print("Python", end="!")
print()


#property()
class Person:

    def __init__(self):
        self.__age = 23

    @property
    def age(self):
        return self.__age

person = Person()

print(person.age)


#range()
for i in range(5):
    print(i)


#repr()
text = "Python"

print(repr(text))


#reversed()
numbers = [1,2,3,4]

print(list(reversed(numbers)))


#round()
print(round(3.14159,2))


#set()
numbers = set([1,2,2,3])

print(numbers)


#setattr()
class Person:
    pass

person = Person()

setattr(person,"name","Oscar")

print(person.name)


#slice()
text = "Python"

print(text[slice(1,4)])


#sorted()
numbers = [5,1,4,2]

print(sorted(numbers))


#sorted() Reverse
numbers = [5,1,4,2]

print(sorted(numbers, reverse=True))


#sorted() with Key
words = ["apple","kiwi","banana"]

print(sorted(words, key=len))


#staticmethod()
class Math:

    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(5,6))


#str()
print(str(100))


#sum()
numbers = [10,20,30]

print(sum(numbers))


#super()
class Animal:

    def speak(self):
        print("Animal")


class Dog(Animal):

    def speak(self):

        super().speak()

        print("Dog")


Dog().speak()


#tuple()
numbers = tuple([1,2,3])

print(numbers)


#type()
print(type(100))
print(type("Python"))


#vars()
class Person:

    def __init__(self):

        self.name = "Oscar"

person = Person()

print(vars(person))


#zip()
names = ["Oscar","Alex"]
ages = [23,21]

print(list(zip(names,ages)))

#eval()
expression = "10 + 20 * 2"

print(eval(expression))


#compile()
code = compile("print('Hello Python')", "test", "exec")

exec(code)


#exec()
code = """
for i in range(3):
    print(i)
"""

exec(code)


#globals()
x = 100

print(globals()["x"])


#help()
#print(help(str))


#breakpoint()
#breakpoint()


#__import__()
math = __import__("math")

print(math.sqrt(25))


#aiter() (Python 3.10+)
#async def example():
#    iterator = aiter([1,2,3])


#anext() (Python 3.10+)
#async def example():
#    iterator = aiter([1,2,3])
#    print(await anext(iterator))


#license()
#print(license())


#copyright()
#print(copyright())


#credits()
#print(credits())


#quit()
#quit()


#exit()
#exit()


#help() for Module
#import math
#
#help(math)


#help() for Function
#print(help(len))


#globals() Modify Variable
count = 10

globals()["count"] = 50

print(count)


#locals()
name = "Oscar"

print(locals())


#exec() with Variables
x = 10

exec("print(x)")


#eval() with Variables
x = 20

print(eval("x + 5"))


#compile() Expression
code = compile("5 + 10", "", "eval")

print(eval(code))


#compile() Single Statement
code = compile("print('Python')", "", "single")

exec(code)


#compile() Multiple Statements
code = compile("""
a = 10
b = 20
print(a+b)
""", "", "exec")

exec(code)


#globals() Keys
print(globals().keys())


#locals() Keys
city = "Delhi"

print(locals().keys())


#Dynamic Function
code = """
def greet():
    print("Hello")
"""

exec(code)

greet()


#Dynamic Class
code = """
class Person:

    def show(self):
        print("Person")
"""

exec(code)

person = Person()

person.show()


#Dynamic Dictionary
student = {}

exec("student['name']='Oscar'")

print(student)


#Dynamic Loop
exec("""
for i in range(5):
    print(i)
""")


#Dynamic Import
module = __import__("random")

print(module.randint(1,10))


#Check Built-in
print(callable(len))


#Check Namespace
print("__name__" in globals())


#Execute Expression
expression = compile("100*2", "", "eval")

print(eval(expression))


#Execute Script
script = compile("""
print("Python")
print("Programming")
""", "", "exec")

exec(script)


#eval() Boolean
print(eval("10 > 5"))


#eval() List
print(eval("[1,2,3]"))


#eval() Dictionary
print(eval("{'name':'Oscar'}"))


#eval() Tuple
print(eval("(10,20)"))


#eval() Arithmetic
print(eval("100/5"))


#Dynamic Assignment
exec("number = 500")

print(exec("number"))


#Dynamic List
exec("numbers = [1,2,3]")

print(numbers)


#Dynamic Object
exec("""
class Student:

    pass
""")

student = student()

print(student)