#Simple Function
def greet():

    print("Hello")


greet()


#Function Assigned to Variable
def greet():

    print("Hello")


say_hello = greet

say_hello()


#Function Inside Function
def outer():

    def inner():
        print("Inner Function")

    inner()


outer()


#Function Returning Function
def outer():

    def inner():
        print("Returned Function")

    return inner


function = outer()

function()


#Simple Decorator
def decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper


@decorator
def greet():

    print("Hello")


greet()


#Decorator Without @ Syntax
def decorator(function):

    def wrapper():

        print("Before")

        function()

        print("After")

    return wrapper


def greet():

    print("Hello")


greet = decorator(greet)

greet()


#Decorator with Arguments
def decorator(function):

    def wrapper(name):

        print("Before")

        function(name)

        print("After")

    return wrapper


@decorator
def greet(name):

    print("Hello", name)


greet("Oscar")


#Decorator with Multiple Arguments
def decorator(function):

    def wrapper(a,b):

        print("Numbers:",a,b)

        function(a,b)

    return wrapper


@decorator
def add(a,b):

    print(a+b)


add(5,10)


#Decorator Using *args
def decorator(function):

    def wrapper(*args):

        print("Arguments:",args)

        return function(*args)

    return wrapper


@decorator
def multiply(a,b):

    return a*b


print(multiply(5,6))


#Decorator Using **kwargs
def decorator(function):

    def wrapper(**kwargs):

        print(kwargs)

        return function(**kwargs)

    return wrapper


@decorator
def student(name,age):

    print(name,age)


student(name="Oscar",age=23)


#Decorator Using *args and **kwargs
def decorator(function):

    def wrapper(*args,**kwargs):

        print("Function Called")

        return function(*args,**kwargs)

    return wrapper


@decorator
def greet(name):

    print("Hello",name)


greet("Oscar")


#Return Value
def decorator(function):

    def wrapper(*args,**kwargs):

        result = function(*args,**kwargs)

        return result

    return wrapper


@decorator
def square(number):

    return number**2


print(square(5))


#Logging Decorator
def logger(function):

    def wrapper(*args,**kwargs):

        print("Running:",function.__name__)

        return function(*args,**kwargs)

    return wrapper


@logger
def greet():

    print("Hello")


greet()


#Timing Decorator
import time

def timer(function):

    def wrapper(*args,**kwargs):

        start = time.time()

        result = function(*args,**kwargs)

        end = time.time()

        print(end-start)

        return result

    return wrapper


@timer
def test():

    for i in range(1000000):
        pass


test()


#Permission Decorator
def admin_only(function):

    def wrapper(user):

        if user == "admin":
            function(user)

        else:
            print("Access Denied")

    return wrapper


@admin_only
def dashboard(user):

    print("Welcome",user)


dashboard("admin")
dashboard("guest")


#Repeat Function
def repeat(function):

    def wrapper():

        for i in range(3):
            function()

    return wrapper


@repeat
def hello():

    print("Hello")


hello()


#Decorator with Prefix
def prefix(function):

    def wrapper():

        print(">>>",end=" ")

        function()

    return wrapper


@prefix
def greet():

    print("Python")


greet()


#Uppercase Output
def uppercase(function):

    def wrapper():

        return function().upper()

    return wrapper


@uppercase
def message():

    return "hello python"


print(message())


#Decorator Chaining
def decorator1(function):

    def wrapper():

        print("Decorator 1")

        function()

    return wrapper


def decorator2(function):

    def wrapper():

        print("Decorator 2")

        function()

    return wrapper


@decorator1
@decorator2
def greet():

    print("Hello")


greet()


#Preserve Function Name
from functools import wraps

def decorator(function):

    @wraps(function)
    def wrapper():

        print("Before")

        function()

    return wrapper


@decorator
def greet():

    print("Hello")


print(greet.__name__)

#Decorator with Parameters
def repeat(times):

    def decorator(function):

        def wrapper(*args,**kwargs):

            for i in range(times):
                function(*args,**kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():

    print("Hello")


greet()


#Decorator with Message
def message(text):

    def decorator(function):

        def wrapper():

            print(text)

            function()

        return wrapper

    return decorator


@message("Welcome")
def hello():

    print("Python")


hello()


#Memoization Decorator
def memoize(function):

    cache = {}

    def wrapper(number):

        if number not in cache:
            cache[number] = function(number)

        return cache[number]

    return wrapper


@memoize
def square(number):

    print("Calculating...")

    return number * number


print(square(5))
print(square(5))


#Singleton Decorator
def singleton(cls):

    instances = {}

    def wrapper(*args,**kwargs):

        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)

        return instances[cls]

    return wrapper


@singleton
class Database:
    pass


db1 = Database()
db2 = Database()

print(db1 is db2)


#Retry Decorator
def retry(function):

    def wrapper(*args,**kwargs):

        for attempt in range(3):

            try:
                return function(*args,**kwargs)

            except Exception:
                print("Retry",attempt+1)

    return wrapper


count = 0

@retry
def test():

    global count

    count += 1

    if count < 3:
        raise ValueError

    print("Success")


test()


#Class Decorator
def add_method(cls):

    def greet(self):
        print("Hello")

    cls.greet = greet

    return cls


@add_method
class Person:
    pass


person = Person()

person.greet()


#Decorating Instance Method
def logger(function):

    def wrapper(self,*args,**kwargs):

        print("Method:",function.__name__)

        return function(self,*args,**kwargs)

    return wrapper


class Student:

    @logger
    def study(self):

        print("Studying")


Student().study()


#Decorating Class Method
def logger(function):

    def wrapper(*args,**kwargs):

        print("Class Method")

        return function(*args,**kwargs)

    return wrapper


class Person:

    @classmethod
    @logger
    def show(cls):

        print("Hello")


Person.show()


#Decorating Static Method
def logger(function):

    def wrapper(*args):

        print("Static Method")

        return function(*args)

    return wrapper


class Math:

    @staticmethod
    @logger
    def add(a,b):

        return a+b


print(Math.add(5,10))


#Property Decorator
class Person:

    def __init__(self):

        self.__age = 18


    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self,value):
        self.__age = value


person = Person()

person.age = 25

print(person.age)


#Read Only Property
class Circle:

    def __init__(self,radius):

        self.radius = radius


    @property
    def area(self):

        return 3.14 * self.radius ** 2


circle = Circle(5)

print(circle.area)


#Cached Property
from functools import cached_property

class Circle:

    def __init__(self,radius):

        self.radius = radius


    @cached_property
    def area(self):

        print("Calculating...")

        return 3.14 * self.radius ** 2


circle = Circle(5)

print(circle.area)
print(circle.area)


#lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(number):

    if number < 2:
        return number

    return fibonacci(number-1) + fibonacci(number-2)


print(fibonacci(10))


#Authenticate Decorator
def login_required(function):

    def wrapper(user):

        if user["logged_in"]:
            return function(user)

        print("Please Login")

    return wrapper


@login_required
def profile(user):

    print("Welcome",user["name"])


profile({
    "name":"Oscar",
    "logged_in":True
})


#Validate Input
def positive(function):

    def wrapper(number):

        if number < 0:
            raise ValueError("Positive Number Required")

        return function(number)

    return wrapper


@positive
def square(number):

    return number * number


print(square(5))


#Measure Execution Time
import time

def timer(function):

    def wrapper(*args,**kwargs):

        start = time.perf_counter()

        result = function(*args,**kwargs)

        end = time.perf_counter()

        print(end-start)

        return result

    return wrapper


@timer
def work():

    sum(range(1000000))


work()


#Count Function Calls
def counter(function):

    count = 0

    def wrapper(*args,**kwargs):

        nonlocal count

        count += 1

        print("Calls:",count)

        return function(*args,**kwargs)

    return wrapper


@counter
def hello():

    print("Hello")


hello()
hello()
hello()


#Register Functions
functions = {}

def register(function):

    functions[function.__name__] = function

    return function


@register
def greet():

    print("Hello")


functions["greet"]()


#HTML Tag Decorator
def bold(function):

    def wrapper():

        return "<b>" + function() + "</b>"

    return wrapper


@bold
def text():

    return "Python"


print(text())


#Decorator Factory
def prefix(symbol):

    def decorator(function):

        def wrapper():

            print(symbol,end=" ")

            function()

        return wrapper

    return decorator


@prefix(">>>")
def start():

    print("Application Started")


start()