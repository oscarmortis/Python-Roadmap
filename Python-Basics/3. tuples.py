#Create Tuple
numbers = (1,2,3,4,5)

print(numbers)


#Tuple without Parentheses
numbers = 1,2,3,4,5

print(numbers)


#Single Item Tuple
numbers = (10,)

print(numbers)


#Without Comma it's an Integer
numbers = (10)

print(type(numbers))


#Tuple Type
numbers = (1,2,3)

print(type(numbers))


#Length of Tuple
numbers = (1,2,3,4,5)

print(len(numbers))


#Access First Item
numbers = (1,2,3,4,5)

print(numbers[0])


#Access Last Item
numbers = (1,2,3,4,5)

print(numbers[-1])


#Negative Indexing
numbers = (10,20,30,40,50)

print(numbers[-2])


#Tuple Slicing
numbers = (1,2,3,4,5)

print(numbers[1:4])


#Slice from Beginning
numbers = (1,2,3,4,5)

print(numbers[:3])


#Slice to End
numbers = (1,2,3,4,5)

print(numbers[2:])


#Reverse Tuple
numbers = (1,2,3,4,5)

print(numbers[::-1])


#Every Second Item
numbers = (1,2,3,4,5,6,7,8)

print(numbers[::2])


#Copy Tuple
numbers = (1,2,3,4)

copy = numbers[:]

print(copy)


#Tuple is Immutable
numbers = (1,2,3)

#numbers[0] = 10

#print(numbers)


#Concatenate Tuples
a = (1,2,3)
b = (4,5,6)

print(a + b)


#Repeat Tuple
numbers = (1,2)

print(numbers * 3)


#Membership Operator
numbers = (1,2,3,4)

print(2 in numbers)
print(10 in numbers)


#Not in Operator
numbers = (1,2,3)

print(10 not in numbers)


#Loop Through Tuple
numbers = (10,20,30)

for number in numbers:
    print(number)


#Loop with Enumerate
numbers = (10,20,30)

for index, value in enumerate(numbers):
    print(index, value)


#Enumerate Starting from 1
numbers = (10,20,30)

for index, value in enumerate(numbers, start=1):
    print(index, value)


#Tuple Unpacking
numbers = (10,20,30)

a,b,c = numbers

print(a)
print(b)
print(c)


#Unpacking with *
numbers = (1,2,3,4,5)

first,*middle,last = numbers

print(first)
print(middle)
print(last)


#Ignore Values while Unpacking
numbers = (1,2,3,4,5)

first,*_,last = numbers

print(first)
print(last)
print(_)


#Count Occurrences
numbers = (1,2,2,3,2)

print(numbers.count(2))


#Find Index
numbers = (10,20,30,40)

print(numbers.index(30))


#Maximum Value
numbers = (10,20,30,40)

print(max(numbers))


#Minimum Value
numbers = (10,20,30,40)

print(min(numbers))


#Sum of Tuple
numbers = (10,20,30)

print(sum(numbers))


#Sorted Tuple
numbers = (5,2,4,1,3)

print(sorted(numbers))


#Convert Tuple to List
numbers = (1,2,3)

print(list(numbers))


#Convert List to Tuple
numbers = [1,2,3]

print(tuple(numbers))


#Convert String to Tuple
text = "Python"

print(tuple(text))


#Convert Set to Tuple
letters = {"a","b","c"}

print(tuple(letters))


#Nested Tuple
numbers = (
    (1,2),
    (3,4),
    (5,6)
)

print(numbers)


#Access Nested Tuple
numbers = (
    (1,2),
    (3,4),
    (5,6)
)

print(numbers[1][0])


#Tuple inside List
numbers = [
    (1,2),
    (3,4),
    (5,6)
]

print(numbers[2])


#List inside Tuple
numbers = (
    [1,2],
    [3,4]
)

print(numbers)


#Modify List inside Tuple
numbers = (
    [1,2],
    [3,4]
)

numbers[0].append(100)

print(numbers)


#Tuple Equality
a = (1,2,3)
b = (1,2,3)

print(a == b)


#Tuple Identity
a = (1,2,3)
b = a

print(a is b)


#Reverse using reversed()
numbers = (1,2,3,4)

print(tuple(reversed(numbers)))


#Zip to Tuple
names = ("Oscar","Alex","John")
ages = (23,22,21)

print(tuple(zip(names, ages)))


#Dictionary from Tuples
pairs = (
    ("name","Oscar"),
    ("age",23),
    ("course","Python")
)

print(dict(pairs))


#Print Memory Address
numbers = (1,2,3)

print(id(numbers))


#Tuple Size in Memory
numbers = (1,2,3)

print(numbers.__sizeof__())

#Tuple Packing
person = "Oscar", 23, "Python"

print(person)


#Tuple Unpacking
person = ("Oscar", 23, "Python")

name, age, course = person

print(name)
print(age)
print(course)


#Nested Unpacking
data = (1, (2, 3))

a, (b, c) = data

print(a)
print(b)
print(c)


#Swap Variables
a = 10
b = 20

a, b = b, a

print(a)
print(b)


#Return Multiple Values
def get_user():
    return "Oscar", 23, "Python"

name, age, course = get_user()

print(name)
print(age)
print(course)


#Ignore Returned Values
def get_user():
    return "Oscar", 23, "Python"

name, *_ = get_user()

print(name)


#Ignore Middle Values
numbers = (10,20,30,40,50)

first, *_, last = numbers

print(first)
print(last)


#Nested Loop
matrix = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

for row in matrix:
    for value in row:
        print(value)


#Flatten Nested Tuple
matrix = (
    (1,2),
    (3,4),
    (5,6)
)

flat = ()

for row in matrix:
    flat += row

print(flat)


#Tuple Comparison
print((1,2,3) == (1,2,3))
print((1,2,3) != (1,2,4))


#Lexicographical Comparison
print((1,2,3) < (1,2,4))
print((1,5) > (1,2))


#Find Maximum Tuple
data = (
    (1,20),
    (5,10),
    (3,15)
)

print(max(data))


#Find Minimum Tuple
data = (
    (1,20),
    (5,10),
    (3,15)
)

print(min(data))


#Sort Tuples
data = (
    (3,"C"),
    (1,"A"),
    (2,"B")
)

print(sorted(data))


#Sort by Second Value
data = (
    (3,"C"),
    (1,"A"),
    (2,"B")
)

print(sorted(data, key=lambda x: x[1]))


#Tuple in Set
points = {
    (10,20),
    (30,40),
    (50,60)
}

print(points)


#Tuple as Dictionary Key
locations = {
    (10,20):"Home",
    (30,40):"School"
}

print(locations[(10,20)])


#Why Tuple Can Be Dictionary Key
point = (10,20)

print(hash(point))


#List Cannot Be Dictionary Key
#point = [10,20]

#print(hash(point))


#Enumerate Tuple
letters = ("a","b","c","d")

print(tuple(enumerate(letters)))


#Zip Creates Tuples
names = ["Oscar","Alex","John"]
ages = [23,22,21]

print(list(zip(names, ages)))


#Unzip Tuples
pairs = (
    ("Oscar",23),
    ("Alex",22),
    ("John",21)
)

names, ages = zip(*pairs)

print(names)
print(ages)


#Tuple from Range
numbers = tuple(range(10))

print(numbers)


#Tuple from Map
numbers = tuple(map(str, range(5)))

print(numbers)


#Tuple from Filter
numbers = tuple(filter(lambda x: x % 2 == 0, range(10)))

print(numbers)


#Generator Expression
numbers = tuple(x*x for x in range(6))

print(numbers)


#Any
numbers = (0,0,1)

print(any(numbers))


#All
numbers = (1,2,3)

print(all(numbers))


#Slice Equality
a = (1,2,3,4)
b = (1,2)

print(a[:2] == b)


#Check Empty Tuple
numbers = ()

print(not numbers)


#Reverse Nested Tuples
data = (
    (1,2),
    (3,4),
    (5,6)
)

print(tuple(reversed(data)))


#Join Tuples
a = (1,2)
b = (3,4)
c = (5,6)

print(a + b + c)


#Count Total Elements
data = (
    (1,2),
    (3,4),
    (5,6)
)

count = 0

for row in data:
    count += len(row)

print(count)


#namedtuple
from collections import namedtuple

Student = namedtuple("Student", ["name","age","course"])

student = Student("Oscar",23,"Python")

print(student)


#Access namedtuple by Name
from collections import namedtuple

Student = namedtuple("Student", ["name","age"])

student = Student("Oscar",23)

print(student.name)
print(student.age)


#Access namedtuple by Index
from collections import namedtuple

Student = namedtuple("Student", ["name","age"])

student = Student("Oscar",23)

print(student[0])
print(student[1])


#Convert namedtuple to Dictionary
from collections import namedtuple

Student = namedtuple("Student", ["name","age"])

student = Student("Oscar",23)

print(student._asdict())


#Replace Value in namedtuple
from collections import namedtuple

Student = namedtuple("Student", ["name","age"])

student = Student("Oscar",23)

student = student._replace(age=24)

print(student)


#Fields of namedtuple
from collections import namedtuple

Student = namedtuple("Student", ["name","age"])

print(Student._fields)


#Memory Comparison
numbers_list = [1,2,3]
numbers_tuple = (1,2,3)

print(numbers_list.__sizeof__())
print(numbers_tuple.__sizeof__())


#Tuple is Hashable
print(hash((1,2,3)))


#List is Not Hashable
#print(hash([1,2,3]))