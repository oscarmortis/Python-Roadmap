#List Comprehension
numbers = [x for x in range(5)]

print(numbers)


#List Comprehension with Expression
numbers = [x * 2 for x in range(5)]

print(numbers)


#List Comprehension with if
numbers = [x for x in range(10) if x % 2 == 0]

print(numbers)


#List Comprehension with if-else
numbers = ["Even" if x % 2 == 0 else "Odd" for x in range(6)]

print(numbers)


#Square Numbers
numbers = [x ** 2 for x in range(6)]

print(numbers)


#Cube Numbers
numbers = [x ** 3 for x in range(6)]

print(numbers)


#String to List
letters = [letter for letter in "Python"]

print(letters)


#Lowercase
words = ["PYTHON","JAVA","C++"]

lower = [word.lower() for word in words]

print(lower)


#Uppercase
words = ["python","java","c++"]

upper = [word.upper() for word in words]

print(upper)


#Strip Spaces
words = ["  Python  "," Java "," C++ "]

clean = [word.strip() for word in words]

print(clean)


#Length of Strings
words = ["Python","Java","C++"]

lengths = [len(word) for word in words]

print(lengths)


#Filter Positive Numbers
numbers = [-2,-1,0,1,2,3]

positive = [x for x in numbers if x > 0]

print(positive)


#Filter Negative Numbers
numbers = [-2,-1,0,1,2,3]

negative = [x for x in numbers if x < 0]

print(negative)


#Filter Odd Numbers
numbers = [1,2,3,4,5,6]

odd = [x for x in numbers if x % 2]

print(odd)


#Nested Loop
pairs = [(x,y) for x in [1,2] for y in [3,4]]

print(pairs)


#Flatten List
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = [item for row in matrix for item in row]

print(flat)


#List of Tuples
numbers = [(x,x*x) for x in range(5)]

print(numbers)


#Character ASCII
letters = [ord(letter) for letter in "ABC"]

print(letters)


#Boolean List
numbers = [1,2,3,4]

result = [x > 2 for x in numbers]

print(result)


#Dictionary Comprehension
student = {
    x : x * 10
    for x in range(5)
}

print(student)


#Dictionary Square
square = {
    x : x ** 2
    for x in range(6)
}

print(square)


#Dictionary Filter
numbers = {
    x : x
    for x in range(10)
    if x % 2 == 0
}

print(numbers)


#Swap Dictionary
student = {
    "name":"Oscar",
    "age":23
}

swap = {
    value:key
    for key,value in student.items()
}

print(swap)


#Set Comprehension
numbers = {
    x
    for x in [1,2,2,3,3,4]
}

print(numbers)


#Set Squares
numbers = {
    x*x
    for x in range(5)
}

print(numbers)


#Set Filter
numbers = {
    x
    for x in range(10)
    if x > 5
}

print(numbers)


#Generator Expression
numbers = (
    x*x
    for x in range(5)
)

print(numbers)

for number in numbers:
    print(number)


#Generator Sum
numbers = (
    x
    for x in range(101)
)

print(sum(numbers))


#Nested List Comprehension
matrix = [
    [x for x in range(3)]
    for y in range(3)
]

print(matrix)


#Create Identity Matrix
size = 3

matrix = [
    [
        1 if row == col else 0
        for col in range(size)
    ]
    for row in range(size)
]

print(matrix)

#Filter None Values
data = [1,None,2,None,3]

result = [x for x in data if x is not None]

print(result)


#Remove Empty Strings
words = ["Python","","Java","","C++"]

result = [word for word in words if word]

print(result)


#Capitalize Words
words = ["python","java","c++"]

result = [word.capitalize() for word in words]

print(result)


#First Letter
words = ["Python","Java","C++"]

result = [word[0] for word in words]

print(result)


#Reverse Strings
words = ["Python","Java","Code"]

result = [word[::-1] for word in words]

print(result)


#Numbers to Strings
numbers = [1,2,3,4]

result = [str(number) for number in numbers]

print(result)


#String to Integers
numbers = ["10","20","30"]

result = [int(number) for number in numbers]

print(result)


#Unique Word Lengths
words = ["apple","banana","kiwi","apple"]

result = {len(word) for word in words}

print(result)


#Dictionary from Two Lists
names = ["Oscar","Alex","John"]
ages = [23,21,20]

students = {
    name:age
    for name,age in zip(names,ages)
}

print(students)


#Dictionary Keys
student = {
    "name":"Oscar",
    "age":23,
    "city":"Delhi"
}

keys = [key for key in student]

print(keys)


#Dictionary Values
student = {
    "name":"Oscar",
    "age":23,
    "city":"Delhi"
}

values = [value for value in student.values()]

print(values)


#Dictionary Items
student = {
    "name":"Oscar",
    "age":23
}

items = [
    (key,value)
    for key,value in student.items()
]

print(items)


#Dictionary Filter by Value
scores = {
    "Math":95,
    "Physics":80,
    "English":60
}

result = {
    subject:score
    for subject,score in scores.items()
    if score >= 80
}

print(result)


#Dictionary Keys Uppercase
student = {
    "name":"Oscar",
    "city":"Delhi"
}

result = {
    key.upper():value
    for key,value in student.items()
}

print(result)


#Dictionary Values Uppercase
student = {
    "name":"oscar",
    "city":"delhi"
}

result = {
    key:value.upper()
    for key,value in student.items()
}

print(result)


#Transpose Matrix
matrix = [
    [1,2,3],
    [4,5,6]
]

transpose = [
    [row[i] for row in matrix]
    for i in range(len(matrix[0]))
]

print(transpose)


#Cartesian Product
letters = ["A","B"]
numbers = [1,2,3]

result = [
    (letter,number)
    for letter in letters
    for number in numbers
]

print(result)


#Multiplication Table
table = [
    [row*col for col in range(1,6)]
    for row in range(1,6)
]

print(table)


#Nested if
numbers = [
    x
    for x in range(50)
    if x % 2 == 0
    if x % 5 == 0
]

print(numbers)


#Flatten Deep List
matrix = [
    [[1,2],[3,4]],
    [[5,6],[7,8]]
]

flat = [
    item
    for group in matrix
    for row in group
    for item in row
]

print(flat)


#Conditional Dictionary Values
numbers = {
    x:(
        "Even"
        if x % 2 == 0
        else "Odd"
    )
    for x in range(6)
}

print(numbers)


#Conditional Set
numbers = {
    x*2
    for x in range(10)
    if x % 2 == 0
}

print(numbers)


#Generator Max
numbers = (
    x*x
    for x in range(10)
)

print(max(numbers))


#Generator Any
numbers = (
    x > 5
    for x in range(10)
)

print(any(numbers))


#Generator All
numbers = (
    x < 10
    for x in range(10)
)

print(all(numbers))


#Generator Filter
numbers = (
    x
    for x in range(20)
    if x % 3 == 0
)

print(list(numbers))


#Nested Dictionary
table = {
    row:{
        col:row*col
        for col in range(1,6)
    }
    for row in range(1,6)
}

print(table)


#Character Frequency
text = "banana"

frequency = {
    char:text.count(char)
    for char in set(text)
}

print(frequency)


#Word Length Dictionary
words = [
    "Python",
    "Java",
    "C++"
]

result = {
    word:len(word)
    for word in words
}

print(result)


#Even and Odd Dictionary
numbers = {
    x:(
        "Even"
        if x % 2 == 0
        else "Odd"
    )
    for x in range(10)
}

print(numbers)


#Remove Duplicates
numbers = [1,2,2,3,4,4,5]

unique = list({
    number
    for number in numbers
})

print(unique)