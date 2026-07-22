# ==========================================
# USEFUL PYTHON TRICKS
# PART 1
# ==========================================



# ==========================================
# SWAPPING VARIABLES
# ==========================================


a = 10
b = 20


a, b = b, a


print(a)
print(b)



# ==========================================
# MULTIPLE VARIABLE ASSIGNMENT
# ==========================================


x, y, z = 1, 2, 3


print(x,y,z)



# ==========================================
# SAME VALUE TO MULTIPLE VARIABLES
# ==========================================


a = b = c = 100


print(a,b,c)



# ==========================================
# UNPACKING LIST
# ==========================================


numbers = [1,2,3]


a,b,c = numbers


print(a)
print(b)
print(c)



# ==========================================
# STAR UNPACKING
# ==========================================


numbers = [1,2,3,4,5]


first, *middle, last = numbers


print(first)
print(middle)
print(last)



# ==========================================
# IGNORE VALUES USING _
# ==========================================


numbers = [10,20,30]


first, _, third = numbers


print(first)
print(third)



# ==========================================
# ENUMERATE INSTEAD OF RANGE
# ==========================================


names = [
    "Oscar",
    "Alex",
    "John"
]


for index,name in enumerate(names):

    print(index,name)



# ==========================================
# ENUMERATE START VALUE
# ==========================================


for index,name in enumerate(names,start=1):

    print(index,name)



# ==========================================
# ZIP TWO LISTS
# ==========================================


names = [
    "Oscar",
    "Alex"
]


ages = [
    23,
    25
]


for name,age in zip(names,ages):

    print(name,age)



# ==========================================
# ZIP WITH DIFFERENT LENGTH
# ==========================================


from itertools import zip_longest


a = [1,2,3]

b = ["A","B"]


print(
    list(zip_longest(a,b))
)



# ==========================================
# LIST COMPREHENSION
# ==========================================


numbers = [
    1,2,3,4,5
]


squares = [
    x*x for x in numbers
]


print(squares)



# ==========================================
# LIST COMPREHENSION WITH CONDITION
# ==========================================


numbers = range(10)


even = [
    x for x in numbers if x%2==0
]


print(even)



# ==========================================
# IF ELSE IN COMPREHENSION
# ==========================================


numbers = range(5)


result = [
    "Even" if x%2==0 else "Odd"
    for x in numbers
]


print(result)



# ==========================================
# DICTIONARY COMPREHENSION
# ==========================================


numbers = range(5)


square_dict = {
    x:x*x
    for x in numbers
}


print(square_dict)



# ==========================================
# SET COMPREHENSION
# ==========================================


numbers = [
    1,1,2,3,3
]


unique = {
    x for x in numbers
}


print(unique)



# ==========================================
# GENERATOR EXPRESSION
# ==========================================


numbers = (
    x*x
    for x in range(5)
)


print(next(numbers))
print(next(numbers))



# ==========================================
# CHECK ANY VALUE TRUE
# ==========================================


numbers = [
    False,
    True,
    False
]


print(
    any(numbers)
)



# ==========================================
# CHECK ALL VALUES TRUE
# ==========================================


numbers = [
    True,
    True,
    True
]


print(
    all(numbers)
)



# ==========================================
# SORT USING KEY
# ==========================================


students = [
    ("Oscar",23),
    ("Alex",20),
    ("John",25)
]


students.sort(
    key=lambda x:x[1]
)


print(students)



# ==========================================
# SORT REVERSE
# ==========================================


numbers = [
    5,2,8,1
]


print(
    sorted(numbers,reverse=True)
)



# ==========================================
# REVERSE ITERATION
# ==========================================


numbers = [
    1,2,3,4
]


for number in reversed(numbers):

    print(number)



# ==========================================
# STRING JOIN
# ==========================================


words = [
    "Python",
    "is",
    "powerful"
]


sentence = " ".join(words)


print(sentence)



# ==========================================
# STRING SPLIT
# ==========================================


text = "Python Java C++"


languages = text.split()


print(languages)



# ==========================================
# MULTIPLE STRING CHECK
# ==========================================


text = "Python is amazing"


print(
    text.startswith("Python")
)


print(
    text.endswith("amazing")
)



# ==========================================
# F STRING FORMATTING
# ==========================================


name = "Oscar"

age = 23


print(
    f"My name is {name} and age is {age}"
)



# ==========================================
# FORMAT NUMBERS
# ==========================================


price = 1234567.89


print(
    f"{price:,.2f}"
)



# ==========================================
# CONDITIONAL EXPRESSIONS
# ==========================================


age = 20


status = "Adult" if age>=18 else "Child"


print(status)



# ==========================================
# CHAIN COMPARISON
# ==========================================


age = 23


print(
    18 <= age <= 60
)



# ==========================================
# SWALLOW EXCEPTION
# ==========================================


try:

    number = int("abc")

except:

    pass



# ==========================================
# ELSE WITH LOOP
# ==========================================


numbers = [1,2,3]


for number in numbers:

    if number == 5:
        break

else:

    print("Not Found")



# ==========================================
# DICTIONARY GET
# ==========================================


person = {
    "name":"Oscar"
}


print(
    person.get("age","Unknown")
)



# ==========================================
# DICTIONARY MERGING
# ==========================================


a = {
    "x":1
}


b = {
    "y":2
}


combined = {
    **a,
    **b
}


print(combined)



# ==========================================
# MATCH CASE (PYTHON 3.10)
# ==========================================


command = "start"


match command:

    case "start":

        print("Starting")

    case "stop":

        print("Stopping")

    case _:

        print("Unknown")

# ==========================================
# USEFUL PYTHON TRICKS
# PART 3
# ==========================================



# ==========================================
# CONTEXT MANAGER USING WITH
# ==========================================


with open("example.txt","w") as file:

    file.write("Hello Python")



# ==========================================
# READ FILE SAFELY
# ==========================================


with open("example.txt","r") as file:

    content = file.read()

    print(content)



# ==========================================
# EXCEPTION HANDLING SHORTCUT
# ==========================================


try:

    number = int("123")

except ValueError:

    print("Invalid")



# ==========================================
# MULTIPLE EXCEPTIONS
# ==========================================


try:

    result = 10 / 0


except (ValueError,ZeroDivisionError):

    print("Error")



# ==========================================
# EXCEPTION ELSE
# ==========================================


try:

    number = int("100")


except ValueError:

    print("Error")


else:

    print("Success")



# ==========================================
# EXCEPTION FINALLY
# ==========================================


try:

    print("Running")


finally:

    print("Always Executes")



# ==========================================
# CUSTOM EXCEPTION
# ==========================================


class AgeError(Exception):

    pass



try:

    raise AgeError("Invalid Age")


except AgeError as error:

    print(error)



# ==========================================
# USE ASSERT
# ==========================================


age = 20


assert age >= 18



# ==========================================
# TYPE CHECKING
# ==========================================


number = 10


print(
    isinstance(number,int)
)



# ==========================================
# CHECK ATTRIBUTE
# ==========================================


class Person:

    name = "Oscar"



person = Person()


print(
    hasattr(person,"name")
)



# ==========================================
# GET ATTRIBUTE
# ==========================================


print(
    getattr(person,"name")
)



# ==========================================
# SET ATTRIBUTE
# ==========================================


setattr(
    person,
    "age",
    23
)


print(person.age)



# ==========================================
# DELETE ATTRIBUTE
# ==========================================


delattr(
    person,
    "age"
)



# ==========================================
# OBJECT INSPECTION
# ==========================================


print(
    dir(person)
)



# ==========================================
# HELP FUNCTION
# ==========================================


#help(str)



# ==========================================
# DYNAMIC CLASS CREATION
# ==========================================


Person = type(
    "Person",
    (),
    {
        "name":"Oscar"
    }
)


person = Person()


print(person.name)



# ==========================================
# CLASS DECORATOR
# ==========================================


def add_method(cls):

    def hello(self):

        print("Hello")

    cls.hello = hello

    return cls



@add_method
class Person:

    pass



Person().hello()



# ==========================================
# PROPERTY TRICK
# ==========================================


class Temperature:


    def __init__(self,value):

        self._value = value



    @property
    def value(self):

        return self._value



    @value.setter
    def value(self,new):

        if new < 0:

            raise ValueError

        self._value = new



temperature = Temperature(20)

temperature.value = 30


print(
    temperature.value
)



# ==========================================
# STATIC METHOD
# ==========================================


class Math:


    @staticmethod
    def add(a,b):

        return a+b



print(
    Math.add(5,5)
)



# ==========================================
# CLASS METHOD
# ==========================================


class Person:


    count = 0


    def __init__(self):

        Person.count += 1



    @classmethod
    def total(cls):

        return cls.count



Person()

Person()


print(
    Person.total()
)



# ==========================================
# DATETIME SHORTCUTS
# ==========================================


from datetime import datetime


now = datetime.now()


print(now)



# ==========================================
# FORMAT DATE
# ==========================================


date = datetime.now()


print(
    date.strftime("%d-%m-%Y")
)



# ==========================================
# PARSE DATE
# ==========================================


date = datetime.strptime(
    "20-07-2026",
    "%d-%m-%Y"
)


print(date)



# ==========================================
# TIME DIFFERENCE
# ==========================================


from datetime import timedelta


today = datetime.now()


future = today + timedelta(days=10)


print(future)



# ==========================================
# RANDOM TRICKS
# ==========================================


import random



# Random Number

print(
    random.randint(1,10)
)



# Random Choice

names = [
    "Oscar",
    "Alex",
    "John"
]


print(
    random.choice(names)
)



# Random Multiple Choices

print(
    random.choices(
        names,
        k=3
    )
)



# Shuffle List


numbers = [
    1,2,3,4,5
]


random.shuffle(numbers)


print(numbers)



# ==========================================
# GENERATOR FUNCTION
# ==========================================


def numbers():

    for i in range(5):

        yield i



for number in numbers():

    print(number)



# ==========================================
# GENERATOR PIPELINE
# ==========================================


numbers = (
    x*x
    for x in range(10)
)


print(
    next(numbers)
)



# ==========================================
# FUNCTION ARGUMENT INSPECTION
# ==========================================


import inspect


def add(a,b):

    return a+b



print(
    inspect.signature(add)
)



# ==========================================
# TIME EXECUTION TEST
# ==========================================


import time



start = time.time()


for i in range(1000000):

    pass


end = time.time()


print(
    end-start
)



# ==========================================
# PERFORMANCE COUNTER
# ==========================================


start = time.perf_counter()


sum(range(100000))


end = time.perf_counter()


print(
    end-start
)



# ==========================================
# CACHE RESULTS
# ==========================================


from functools import lru_cache



@lru_cache(maxsize=None)
def fibonacci(n):

    if n < 2:

        return n

    return fibonacci(n-1)+fibonacci(n-2)



print(
    fibonacci(20)
)

# ==========================================
# USEFUL PYTHON TRICKS
# PART 4 (FINAL)
# ==========================================



# ==========================================
# WALRUS OPERATOR :=
# Python 3.8+
# ==========================================


numbers = [1,2,3,4,5]


if (length := len(numbers)) > 3:

    print(
        "Length:",
        length
    )



# ==========================================
# MULTIPLE CONDITION CHECK
# ==========================================


value = 10


if value in [1,5,10]:

    print("Found")



# ==========================================
# SWAP WITHOUT TEMP VARIABLE
# ==========================================


x = 100
y = 200


x,y = y,x


print(x,y)



# ==========================================
# REPEAT STRING
# ==========================================


print(
    "Python " * 3
)



# ==========================================
# REVERSE STRING
# ==========================================


text = "Python"


print(
    text[::-1]
)



# ==========================================
# REVERSE LIST
# ==========================================


numbers = [1,2,3,4]


print(
    numbers[::-1]
)



# ==========================================
# COPY LIST QUICKLY
# ==========================================


numbers = [1,2,3]


copy = numbers[:]


print(copy)



# ==========================================
# CHECK EMPTY VALUES
# ==========================================


items = []


if not items:

    print("Empty")



# ==========================================
# MULTIPLE VALUES CHECK
# ==========================================


value = "python"


if value in (
    "python",
    "java",
    "cpp"
):

    print("Language")



# ==========================================
# ANY OBJECT TO BOOLEAN
# ==========================================


print(
    bool([])
)


print(
    bool([1])
)



# ==========================================
# SORT DICTIONARY
# ==========================================


data = {
    "c":3,
    "a":1,
    "b":2
}


print(
    sorted(data.items())
)



# ==========================================
# SORT DICTIONARY BY VALUE
# ==========================================


data = {
    "apple":5,
    "banana":2,
    "orange":8
}


result = sorted(
    data.items(),
    key=lambda x:x[1]
)


print(result)



# ==========================================
# CREATE DICTIONARY FROM TWO LISTS
# ==========================================


keys = [
    "name",
    "age"
]


values = [
    "Oscar",
    23
]


data = dict(
    zip(keys,values)
)


print(data)



# ==========================================
# DEFAULT DICTIONARY WITH SETDEFAULT
# ==========================================


data = {}


data.setdefault(
    "skills",
    []
).append(
    "Python"
)


print(data)



# ==========================================
# CHAIN DICTIONARY VALUES
# ==========================================


from itertools import chain


data = {
    "a":[1,2],
    "b":[3,4]
}


print(
    list(
        chain.from_iterable(
            data.values()
        )
    )
)



# ==========================================
# ENUMERATE WITH CUSTOM INDEX
# ==========================================


names = [
    "A",
    "B",
    "C"
]


for i,name in enumerate(
    names,
    start=100
):

    print(i,name)



# ==========================================
# USE MAP WITH MULTIPLE LISTS
# ==========================================


a = [1,2,3]

b = [4,5,6]


result = list(
    map(
        lambda x,y:x+y,
        a,
        b
    )
)


print(result)



# ==========================================
# FUNCTION ARGUMENT VALIDATION
# ==========================================


def divide(a,b):

    if b == 0:

        raise ValueError(
            "Cannot divide by zero"
        )

    return a/b



print(
    divide(10,2)
)



# ==========================================
# CONTEXT MANAGER CUSTOM
# ==========================================


class OpenFile:


    def __enter__(self):

        print("Opening")

        return self



    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        print("Closing")



with OpenFile():

    print("Working")



# ==========================================
# ASYNC FUNCTION
# ==========================================


import asyncio



async def hello():

    print("Hello")



#asyncio.run(hello())



# ==========================================
# ASYNC WAIT
# ==========================================


async def task():

    await asyncio.sleep(1)

    print("Done")



#asyncio.run(task())



# ==========================================
# THREADING BASIC
# ==========================================


import threading



def worker():

    print("Running Thread")



thread = threading.Thread(
    target=worker
)


thread.start()

thread.join()



# ==========================================
# MULTIPROCESSING BASIC
# ==========================================


from multiprocessing import Process



def process_task():

    print("Process Running")



process = Process(
    target=process_task
)


#process.start()
#process.join()



# ==========================================
# ENVIRONMENT VARIABLES
# ==========================================


import os


print(
    os.environ.get(
        "PATH"
    )
)



# ==========================================
# RANDOM SECRET VALUES
# ==========================================


import secrets


print(
    secrets.token_hex(16)
)



# ==========================================
# HASHING DATA
# ==========================================


import hashlib


password = "python"


hashed = hashlib.sha256(
    password.encode()
).hexdigest()


print(hashed)



# ==========================================
# DEBUGGING WITH BREAKPOINT
# ==========================================


number = 10


#breakpoint()


print(number)



# ==========================================
# PRINT VARIABLE NAME
# ==========================================


name = "Oscar"


print(
    f"{name=}"
)



# ==========================================
# MULTILINE STRING
# ==========================================


text = """
Python
is
powerful
"""


print(text)



# ==========================================
# ENUMERATION USING ZIP
# ==========================================


names = [
    "Python",
    "Java"
]


for index,name in zip(
    range(len(names)),
    names
):

    print(index,name)



# ==========================================
# SAFE DICTIONARY ACCESS
# ==========================================


data = {
    "user":{
        "name":"Oscar"
    }
}


print(
    data.get(
        "user",
        {}
    ).get(
        "name"
    )
)



# ==========================================
# CREATE CLASS USING DATACLASS
# ==========================================


from dataclasses import dataclass



@dataclass
class Person:

    name:str

    age:int



person = Person(
    "Oscar",
    23
)


print(person)



# ==========================================
# ENUM CLASS
# ==========================================


from enum import Enum



class Status(Enum):

    START = 1

    STOP = 2



print(
    Status.START
)



# ==========================================
# TYPE HINTING
# ==========================================


def add(
    a:int,
    b:int
) -> int:

    return a+b



print(
    add(5,10)
)



# ==========================================
# FINAL PYTHONIC LOOP
# ==========================================


numbers = [
    1,2,3,4,5
]


squares = {
    number:number**2
    for number in numbers
}


print(squares)