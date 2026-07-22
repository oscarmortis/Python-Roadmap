#Counter
from collections import Counter

text = "banana"

count = Counter(text)

print(count)


#Counter Most Common
from collections import Counter

numbers = [1,2,2,3,3,3]

count = Counter(numbers)

print(count.most_common())
print(count.most_common(2))


#Counter Elements
from collections import Counter

count = Counter({
    "a":2,
    "b":3
})

print(list(count.elements()))


#Counter Update
from collections import Counter

count = Counter("apple")

count.update("banana")

print(count)


#Counter Subtract
from collections import Counter

count = Counter("banana")

count.subtract("ana")

print(count)


#Counter Total (Python 3.10+)
from collections import Counter

count = Counter([1,1,2,2,2])

print(count.total())


#Counter Arithmetic
from collections import Counter

a = Counter("apple")
b = Counter("banana")

print(a + b)
print(a - b)
print(a & b)
print(a | b)


#DefaultDict
from collections import defaultdict

numbers = defaultdict(int)

numbers["a"] += 1

print(numbers)


#DefaultDict List
from collections import defaultdict

students = defaultdict(list)

students["Python"].append("Oscar")
students["Python"].append("Alex")

print(students)


#DefaultDict Set
from collections import defaultdict

courses = defaultdict(set)

courses["Python"].add("Oscar")
courses["Python"].add("Oscar")
courses["Python"].add("Alex")

print(courses)


#DefaultDict Lambda
from collections import defaultdict

scores = defaultdict(lambda:100)

print(scores["Math"])


#OrderedDict
from collections import OrderedDict

student = OrderedDict()

student["name"] = "Oscar"
student["age"] = 23

print(student)


#Move to End
from collections import OrderedDict

numbers = OrderedDict([
    ("a",1),
    ("b",2),
    ("c",3)
])

numbers.move_to_end("a")

print(numbers)


#Pop Last
from collections import OrderedDict

numbers = OrderedDict([
    ("a",1),
    ("b",2),
    ("c",3)
])

print(numbers.popitem())


#Pop First
from collections import OrderedDict

numbers = OrderedDict([
    ("a",1),
    ("b",2),
    ("c",3)
])

print(numbers.popitem(last=False))


#NamedTuple
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"]
)

student = Student("Oscar",23)

print(student)


#NamedTuple Fields
from collections import namedtuple

Point = namedtuple(
    "Point",
    ["x","y"]
)

point = Point(10,20)

print(point.x)
print(point.y)


#NamedTuple _asdict()
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"]
)

student = Student("Oscar",23)

print(student._asdict())


#NamedTuple _replace()
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"]
)

student = Student("Oscar",23)

student = student._replace(age=24)

print(student)


#NamedTuple Defaults
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"],
    defaults=[18]
)

student = Student("Oscar")

print(student)


#Deque
from collections import deque

numbers = deque([1,2,3])

print(numbers)


#Append Right
from collections import deque

numbers = deque([1,2,3])

numbers.append(4)

print(numbers)


#Append Left
from collections import deque

numbers = deque([1,2,3])

numbers.appendleft(0)

print(numbers)


#Pop Right
from collections import deque

numbers = deque([1,2,3])

numbers.pop()

print(numbers)


#Pop Left
from collections import deque

numbers = deque([1,2,3])

numbers.popleft()

print(numbers)


#Reverse Deque
from collections import deque

numbers = deque([1,2,3])

numbers.reverse()

print(numbers)


#Rotate Right
from collections import deque

numbers = deque([1,2,3,4])

numbers.rotate(1)

print(numbers)


#Rotate Left
from collections import deque

numbers = deque([1,2,3,4])

numbers.rotate(-1)

print(numbers)

#Counter
from collections import Counter

text = "banana"

count = Counter(text)

print(count)


#Counter Most Common
from collections import Counter

numbers = [1,2,2,3,3,3]

count = Counter(numbers)

print(count.most_common())
print(count.most_common(2))


#Counter Elements
from collections import Counter

count = Counter({
    "a":2,
    "b":3
})

print(list(count.elements()))


#Counter Update
from collections import Counter

count = Counter("apple")

count.update("banana")

print(count)


#Counter Subtract
from collections import Counter

count = Counter("banana")

count.subtract("ana")

print(count)


#Counter Total (Python 3.10+)
from collections import Counter

count = Counter([1,1,2,2,2])

print(count.total())


#Counter Arithmetic
from collections import Counter

a = Counter("apple")
b = Counter("banana")

print(a + b)
print(a - b)
print(a & b)
print(a | b)


#DefaultDict
from collections import defaultdict

numbers = defaultdict(int)

numbers["a"] += 1

print(numbers)


#DefaultDict List
from collections import defaultdict

students = defaultdict(list)

students["Python"].append("Oscar")
students["Python"].append("Alex")

print(students)


#DefaultDict Set
from collections import defaultdict

courses = defaultdict(set)

courses["Python"].add("Oscar")
courses["Python"].add("Oscar")
courses["Python"].add("Alex")

print(courses)


#DefaultDict Lambda
from collections import defaultdict

scores = defaultdict(lambda:100)

print(scores["Math"])


#OrderedDict
from collections import OrderedDict

student = OrderedDict()

student["name"] = "Oscar"
student["age"] = 23

print(student)


#Move to End
from collections import OrderedDict

numbers = OrderedDict([
    ("a",1),
    ("b",2),
    ("c",3)
])

numbers.move_to_end("a")

print(numbers)


#Pop Last
from collections import OrderedDict

numbers = OrderedDict([
    ("a",1),
    ("b",2),
    ("c",3)
])

print(numbers.popitem())


#Pop First
from collections import OrderedDict

numbers = OrderedDict([
    ("a",1),
    ("b",2),
    ("c",3)
])

print(numbers.popitem(last=False))


#NamedTuple
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"]
)

student = Student("Oscar",23)

print(student)


#NamedTuple Fields
from collections import namedtuple

Point = namedtuple(
    "Point",
    ["x","y"]
)

point = Point(10,20)

print(point.x)
print(point.y)


#NamedTuple _asdict()
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"]
)

student = Student("Oscar",23)

print(student._asdict())


#NamedTuple _replace()
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"]
)

student = Student("Oscar",23)

student = student._replace(age=24)

print(student)


#NamedTuple Defaults
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name","age"],
    defaults=[18]
)

student = Student("Oscar")

print(student)


#Deque
from collections import deque

numbers = deque([1,2,3])

print(numbers)


#Append Right
from collections import deque

numbers = deque([1,2,3])

numbers.append(4)

print(numbers)


#Append Left
from collections import deque

numbers = deque([1,2,3])

numbers.appendleft(0)

print(numbers)


#Pop Right
from collections import deque

numbers = deque([1,2,3])

numbers.pop()

print(numbers)


#Pop Left
from collections import deque

numbers = deque([1,2,3])

numbers.popleft()

print(numbers)


#Reverse Deque
from collections import deque

numbers = deque([1,2,3])

numbers.reverse()

print(numbers)


#Rotate Right
from collections import deque

numbers = deque([1,2,3,4])

numbers.rotate(1)

print(numbers)


#Rotate Left
from collections import deque

numbers = deque([1,2,3,4])

numbers.rotate(-1)

print(numbers)