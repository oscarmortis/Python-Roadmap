#Define Function
def greet():
    print("Hello World")

greet()


#Function with Parameter
def greet(name):
    print(f"Hello {name}")

greet("Oscar")


#Function with Multiple Parameters
def introduce(name, age):
    print(name)
    print(age)

introduce("Oscar", 23)


#Return Value
def square(number):
    return number * number

print(square(5))


#Return Multiple Values
def get_user():
    return "Oscar", 23, "Python"

print(get_user())


#Store Return Value
def cube(number):
    return number ** 3

result = cube(4)

print(result)


#Function without Return
def hello():
    print("Hello")

print(hello())


#Default Parameter
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Oscar")


#Multiple Default Parameters
def introduce(name="Guest", age=18):
    print(name)
    print(age)

introduce()
introduce("Oscar", 23)


#Keyword Arguments
def student(name, age):
    print(name)
    print(age)

student(age=23, name="Oscar")


#Positional Arguments
def student(name, age):
    print(name)
    print(age)

student("Oscar", 23)


#Mixed Arguments
def student(name, age):
    print(name)
    print(age)

student("Oscar", age=23)


#Return String
def message():
    return "Hello Python"

print(message())


#Return List
def numbers():
    return [1,2,3,4]

print(numbers())


#Return Dictionary
def person():
    return {
        "name":"Oscar",
        "age":23
    }

print(person())


#Return Boolean
def is_even(number):
    return number % 2 == 0

print(is_even(8))


#Multiple Return Statements
def check(number):
    if number > 0:
        return "Positive"
    return "Negative"

print(check(5))


#Early Return
def login(user):
    if user == "":
        return

    print("Welcome", user)

login("")
login("Oscar")


#Pass Statement
def future_function():
    pass


#Docstring
def add(a, b):
    """Returns Sum"""

    return a + b

print(add.__doc__)


#Local Variable
def test():
    number = 100
    print(number)

test()


#Global Variable
name = "Oscar"

def show():
    print(name)

show()


#global Keyword
count = 0

def increase():
    global count
    count += 1

increase()

print(count)


#Built-in Function
print(len("Python"))


#Function Calling Another Function
def hello():
    print("Hello")

def world():
    hello()
    print("World")

world()


#Check Function Type
def hello():
    pass

print(type(hello))


#Assign Function to Variable
def greet():
    print("Hello")

message = greet

message()


#Function inside Function
def outer():

    def inner():
        print("Inner Function")

    inner()

outer()


#Function Returning Function
def outer():

    def inner():
        print("Hello")

    return inner

func = outer()

func()


#Callable
def hello():
    print("Hello")

print(callable(hello))
print(callable(100))


#Function with Expression
def add(a, b):
    return a + b

print(add(10 + 5, 20))


#Keyword-only Style
def student(name, age):
    print(name)
    print(age)

student(name="Oscar", age=23)


#Return None
def test():
    return

print(test())


#Boolean Function
def is_positive(number):
    return number > 0

print(is_positive(10))


#Even or Odd
def even(number):
    if number % 2 == 0:
        return True

    return False

print(even(8))


#Maximum Number
def maximum(a, b):
    return max(a, b)

print(maximum(10, 20))


#Minimum Number
def minimum(a, b):
    return min(a, b)

print(minimum(10, 20))


#Absolute Value
def absolute(number):
    return abs(number)

print(absolute(-100))


#Power Function
def power(base, exponent):
    return pow(base, exponent)

print(power(2, 5))


#Round Number
def rounding(number):
    return round(number, 2)

print(rounding(3.1415926))


#Function Returning Tuple
def data():
    return 1,2,3

a,b,c = data()

print(a)
print(b)
print(c)


#Variable Length Arguments (*args)
def add(*numbers):
    print(numbers)

add(1,2,3,4,5)


#Loop Through *args
def add(*numbers):

    for number in numbers:
        print(number)

add(10,20,30)


#Sum using *args
def add(*numbers):
    return sum(numbers)

print(add(10,20,30,40))


#Length of *args
def test(*numbers):
    print(len(numbers))

test(1,2,3,4,5)


#Unpacking into *args
def add(a,b,c):
    print(a+b+c)

numbers = [10,20,30]

add(*numbers)


#Keyword Arguments (**kwargs)
def student(**info):
    print(info)

student(name="Oscar", age=23, course="Python")


#Access **kwargs
def student(**info):
    print(info["name"])
    print(info["age"])

student(name="Oscar", age=23)


#Loop Through **kwargs
def student(**info):

    for key,value in info.items():
        print(key, value)

student(name="Oscar", age=23, course="Python")


#Mix Parameters
def student(name, *marks):
    print(name)
    print(marks)

student("Oscar",90,80,95)


#Mix Parameters 2
def student(name, *marks, age):
    print(name)
    print(marks)
    print(age)

student("Oscar",90,80,95, age=23)


#Mix Parameters 3
def student(name, age, **info):
    print(name)
    print(age)
    print(info)

student("Oscar",23, course="Python", city="Delhi")


#Combine *args and **kwargs
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(1,2,3,name="Oscar",age=23)


#Unpack Dictionary
def student(name, age):
    print(name)
    print(age)

data = {
    "name":"Oscar",
    "age":23
}

student(**data)


#Positional-only Parameters (/)
def add(a, b, /):
    print(a+b)

add(10,20)


#Keyword-only Parameters (*)
def student(*, name, age):
    print(name)
    print(age)

student(name="Oscar", age=23)


#Positional + Keyword-only
def student(name, *, age):
    print(name)
    print(age)

student("Oscar", age=23)


#Lambda Function
square = lambda x: x*x

print(square(5))


#Lambda with Multiple Parameters
add = lambda a,b: a+b

print(add(10,20))


#Lambda with sort()
students = [
    ("Oscar",23),
    ("Alex",21),
    ("John",25)
]

students.sort(key=lambda student: student[1])

print(students)


#Lambda with max()
numbers = [10,50,20,80]

print(max(numbers, key=lambda x:x))


#Lambda with min()
numbers = [10,50,20,80]

print(min(numbers, key=lambda x:x))


#Recursive Function
def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number-1)

countdown(5)


#Factorial using Recursion
def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number-1)

print(factorial(5))


#Recursive Sum
def total(number):

    if number == 1:
        return 1

    return number + total(number-1)

print(total(5))


#LEGB Rule
name = "Global"

def outer():

    name = "Outer"

    def inner():
        name = "Inner"
        print(name)

    inner()

outer()


#Access Global Variable
name = "Oscar"

def hello():
    print(name)

hello()


#Modify Global Variable
count = 0

def increase():

    global count

    count += 1

increase()

print(count)


#nonlocal Keyword
def outer():

    count = 0

    def inner():

        nonlocal count

        count += 1

    inner()

    print(count)

outer()


#Function Annotation
def add(a:int, b:int) -> int:
    return a+b

print(add(10,20))


#Annotation Information
def greet(name:str) -> str:
    return "Hello " + name

print(greet.__annotations__)


#Anonymous Function
cube = lambda x:x**3

print(cube(3))


#Function as Argument
def greet(name):
    return f"Hello {name}"

def display(func):
    print(func("Oscar"))

display(greet)


#Function Returning Function
def outer():

    def inner():
        print("Hello")

    return inner

hello = outer()

hello()


#Nested Functions
def outer():

    print("Outer")

    def inner():
        print("Inner")

    inner()

outer()


#Check __name__
def greet():
    print("Hello")

print(greet.__name__)


#Documentation
def greet():
    """Greets User"""

print(greet.__doc__)


#Help Function
def greet():
    """Greets User"""

help(greet)


#Callable Function
def greet():
    pass

print(callable(greet))


#Callable Object
number = 100

print(callable(number))


#Function Object
def hello():
    print("Hello")

print(hello)

hello()


#Store Functions in List
def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

operations = [add, multiply]

for operation in operations:
    print(operation(10,5))


#Store Functions in Dictionary
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

operations = {
    "add":add,
    "subtract":subtract
}

print(operations["add"](20,10))


#Pass Function to map()
numbers = [1,2,3,4]

def square(number):
    return number**2

print(list(map(square, numbers)))


#Pass Function to filter()
numbers = [1,2,3,4,5,6]

def even(number):
    return number % 2 == 0

print(list(filter(even, numbers)))

#reduce()
from functools import reduce

numbers = [1,2,3,4,5]

result = reduce(lambda x,y: x+y, numbers)

print(result)


#reduce() Multiplication
from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda x,y: x*y, numbers)

print(result)


#partial()
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)

print(square(5))


#Another partial()
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

print(double(10))


#Closure
def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner

hello = outer()

hello()


#Closure with Parameter
def power(exponent):

    def calculate(number):
        return number ** exponent

    return calculate

square = power(2)

print(square(6))


#Simple Decorator
def decorator(function):

    def wrapper():
        print("Before")

        function()

        print("After")

    return wrapper


@decorator
def hello():
    print("Hello")

hello()


#Decorator with Arguments
def decorator(function):

    def wrapper(name):
        print("Before")

        function(name)

        print("After")

    return wrapper


@decorator
def hello(name):
    print(name)

hello("Oscar")


#Multiple Decorators
def first(function):

    def wrapper():
        print("First")

        function()

    return wrapper


def second(function):

    def wrapper():
        print("Second")

        function()

    return wrapper


@first
@second
def hello():
    print("Hello")

hello()


#Timing Decorator
import time

def timer(function):

    def wrapper():

        start = time.time()

        function()

        end = time.time()

        print(end - start)

    return wrapper


@timer
def task():

    for i in range(1000000):
        pass

task()


#Generator Function
def numbers():

    yield 1
    yield 2
    yield 3

print(numbers())


#Loop Generator
def numbers():

    yield 10
    yield 20
    yield 30

for number in numbers():
    print(number)


#next()
def numbers():

    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))


#Generator Expression
numbers = (x*x for x in range(5))

print(numbers)

for number in numbers:
    print(number)


#iter()
numbers = [1,2,3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


#StopIteration
numbers = [1]

iterator = iter(numbers)

print(next(iterator))

#next(iterator)


#locals()
name = "Oscar"

def test():

    age = 23

    print(locals())

test()


#globals()
country = "India"

print(globals()["country"])


#eval()
expression = "10 + 20 * 5"

print(eval(expression))


#compile()
code = compile("print('Hello Python')", "", "exec")

exec(code)


#exec()
code = """
for i in range(3):
    print(i)
"""

exec(code)


#Function Attribute
def greet():
    print("Hello")

greet.language = "Python"

print(greet.language)


#Function as Class Attribute
class Math:

    def add(self, a, b):
        return a+b

obj = Math()

print(obj.add(10,20))


#Recursive Fibonacci
def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(8))


#Memoization
cache = {}

def fibonacci(number):

    if number in cache:
        return cache[number]

    if number <= 1:
        return number

    cache[number] = fibonacci(number-1) + fibonacci(number-2)

    return cache[number]

print(fibonacci(20))


#Function Inside Dictionary
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

operations = {
    "+":add,
    "-":subtract
}

print(operations["+"](10,5))


#Dispatch Table
def home():
    print("Home")

def about():
    print("About")

pages = {
    "home":home,
    "about":about
}

pages["home"]()


#Recursive Directory Structure
tree = {
    "A":{
        "B":{
            "C":{}
        }
    }
}

def walk(node):

    for key,value in node.items():

        print(key)

        walk(value)

walk(tree)


#Yield from
def first():

    yield 1
    yield 2

def second():

    yield from first()

    yield 3

for number in second():
    print(number)


#Send Value to Generator
def counter():

    number = 0

    while True:

        received = yield number

        if received is not None:
            number = received
        else:
            number += 1

gen = counter()

print(next(gen))
print(next(gen))
print(gen.send(100))
print(next(gen))


#Generator to List
def numbers():

    yield 1
    yield 2
    yield 3

print(list(numbers()))


#Generator Sum
def numbers():

    for i in range(1,6):
        yield i

print(sum(numbers()))


#Function with Exception
def divide(a,b):

    try:
        return a/b

    except ZeroDivisionError:
        return "Cannot Divide by Zero"

print(divide(10,0))


#Function with finally
def hello():

    try:
        print("Hello")

    finally:
        print("Finished")

hello()


#Function Timer without Decorator
import time

def task():

    start = time.time()

    for i in range(1000000):
        pass

    end = time.time()

    print(end-start)

task()


#Function Reference
def hello():
    print("Hello")

a = hello             

b = a

b()


#Delete Function
def hello():
    print("Hello")

del hello

#print(hello)


#Function Equality
def a():
    pass

def b():
    pass

print(a == b)


#Function Identity
def hello():
    pass

another = hello

print(hello is another)