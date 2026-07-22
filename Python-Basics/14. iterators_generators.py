#Iterator from List
numbers = [1,2,3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


#Iterator from String
text = "Python"

iterator = iter(text)

print(next(iterator))
print(next(iterator))


#Iterator from Tuple
numbers = (10,20,30)

iterator = iter(numbers)

print(next(iterator))


#Iterator from Dictionary
student = {
    "name":"Oscar",
    "age":23
}

iterator = iter(student)

print(next(iterator))


#Iterator from Set
numbers = {1,2,3}

iterator = iter(numbers)

print(next(iterator))


#StopIteration
numbers = [1]

iterator = iter(numbers)

print(next(iterator))

# print(next(iterator))


#Loop Using next()
numbers = [10,20,30]

iterator = iter(numbers)

while True:

    try:
        print(next(iterator))

    except StopIteration:
        break


#Iterator Type
numbers = [1,2,3]

iterator = iter(numbers)

print(type(iterator))


#Generator Expression
numbers = (
    x*x
    for x in range(5)
)

print(next(numbers))
print(next(numbers))


#Generator Loop
numbers = (
    x*x
    for x in range(5)
)

for number in numbers:
    print(number)


#Simple Generator
def numbers():

    yield 1
    yield 2
    yield 3

for number in numbers():
    print(number)


#Generator with Loop
def count():

    for i in range(5):
        yield i

for number in count():
    print(number)


#Generator Return
def greet():

    yield "Hello"
    yield "Python"

generator = greet()

print(next(generator))
print(next(generator))


#Yield Square Numbers
def squares():

    for i in range(6):
        yield i*i

print(list(squares()))


#Yield Even Numbers
def even():

    for i in range(10):

        if i % 2 == 0:
            yield i

print(list(even()))


#Yield Odd Numbers
def odd():

    for i in range(10):

        if i % 2:
            yield i

print(list(odd()))


#Yield Characters
def letters():

    for letter in "Python":
        yield letter

print(list(letters()))


#Yield from List
def fruits():

    data = [
        "Apple",
        "Mango",
        "Orange"
    ]

    for item in data:
        yield item

print(list(fruits()))


#Generator Object
def numbers():

    yield 10
    yield 20

generator = numbers()

print(generator)


#Generator Type
def numbers():

    yield 1

generator = numbers()

print(type(generator))


#Generator Sum
def numbers():

    for i in range(6):
        yield i

print(sum(numbers()))


#Generator Max
def numbers():

    for i in range(20):
        yield i

print(max(numbers()))


#Generator Min
def numbers():

    for i in range(20):
        yield i

print(min(numbers()))


#Generator Any
def numbers():

    yield False
    yield False
    yield True

print(any(numbers()))


#Generator All
def numbers():

    yield True
    yield True
    yield True

print(all(numbers()))


#Generator Enumeration
def numbers():

    for i in range(3):
        yield i

for index,value in enumerate(numbers()):
    print(index,value)


#Generator Length
generator = (x for x in range(5))

print(list(generator))

#Custom Iterator
class Counter:

    def __init__(self):

        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > 5:
            raise StopIteration

        number = self.current

        self.current += 1

        return number


for number in Counter():
    print(number)


#Iterator Object
counter = Counter()

iterator = iter(counter)

print(next(iterator))
print(next(iterator))


#Reset Iterator
class Counter:

    def __iter__(self):

        self.current = 1

        return self

    def __next__(self):

        if self.current > 3:
            raise StopIteration

        number = self.current

        self.current += 1

        return number


counter = Counter()

for number in counter:
    print(number)


#yield from List
def numbers():

    yield from [1,2,3,4]

print(list(numbers()))


#yield from String
def letters():

    yield from "Python"

print(list(letters()))


#yield from Another Generator
def first():

    yield 1
    yield 2


def second():

    yield from first()

    yield 3
    yield 4


print(list(second()))


#Infinite Generator
def infinite():

    number = 1

    while True:

        yield number

        number += 1


generator = infinite()

print(next(generator))
print(next(generator))
print(next(generator))


#Generator send()
def greeting():

    name = yield

    print("Hello",name)


generator = greeting()

next(generator)

generator.send("Oscar")


#Generator close()
def numbers():

    yield 1
    yield 2
    yield 3


generator = numbers()

print(next(generator))

generator.close()

#print(next(generator))


#Generator throw()
def test():

    try:

        yield 1

    except ValueError:
        print("ValueError Caught")


generator = test()

next(generator)

generator.throw(ValueError)


#Generator State
def numbers():

    yield 10
    yield 20


generator = numbers()

print(next(generator))
print(next(generator))


#Generator Expression
square = (
    x*x
    for x in range(10)
)

for number in square:
    print(number)


#Lazy Evaluation
numbers = (
    x*x
    for x in range(1000000)
)

print(next(numbers))
print(next(numbers))


#Compare List vs Generator
numbers = [x*x for x in range(5)]

generator = (
    x*x
    for x in range(5)
)

print(numbers)
print(generator)


#Generator with if
numbers = (
    x
    for x in range(20)
    if x % 2 == 0
)

print(list(numbers))


#Nested Generator
def rows():

    for row in range(3):

        yield (
            col
            for col in range(3)
        )


for row in rows():
    print(list(row))


#Generator Pipeline
def numbers():

    for i in range(10):
        yield i


def even(data):

    for number in data:

        if number % 2 == 0:
            yield number


def square(data):

    for number in data:
        yield number * number


result = square(even(numbers()))

print(list(result))


#Reverse Iterator
numbers = [1,2,3,4]

iterator = reversed(numbers)

print(next(iterator))
print(next(iterator))


#Zip Iterator
names = ["Oscar","Alex"]
ages = [23,21]

iterator = zip(names,ages)

print(next(iterator))
print(next(iterator))


#Map Iterator
numbers = [1,2,3]

iterator = map(lambda x:x*x,numbers)

print(next(iterator))
print(list(iterator))


#Filter Iterator
numbers = [1,2,3,4]

iterator = filter(
    lambda x:x%2==0,
    numbers
)

print(next(iterator))
print(list(iterator))


#Iterator Exhaustion
numbers = iter([1,2,3])

print(list(numbers))
print(list(numbers))


#Generator Exhaustion
def count():

    yield 1
    yield 2
    yield 3


generator = count()

print(list(generator))
print(list(generator))


#Multiple Iterators
numbers = [10,20,30]

iterator1 = iter(numbers)
iterator2 = iter(numbers)

print(next(iterator1))
print(next(iterator2))


#Manual Iteration
text = "Python"

iterator = iter(text)

while True:

    try:
        print(next(iterator))

    except StopIteration:
        break


#Read Large File Lazily
#with open("test.txt") as file:
#
#    for line in file:
#        print(line.strip())


#Generator for File Lines
#def read_file(filename):
#
#    with open(filename) as file:
#
#        for line in file:
#            yield line.strip()
#
#
#for line in read_file("test.txt"):
#    print(line)