#For Loop
for i in range(5):
    print(i)


#For Loop with Start and Stop
for i in range(2,7):
    print(i)


#For Loop with Step
for i in range(0,11,2):
    print(i)


#Reverse Loop
for i in range(10,0,-1):
    print(i)


#Loop Through List
numbers = [10,20,30,40]

for number in numbers:
    print(number)


#Loop Through Tuple
numbers = (10,20,30)

for number in numbers:
    print(number)


#Loop Through Set
numbers = {10,20,30}

for number in numbers:
    print(number)


#Loop Through Dictionary Keys
student = {
    "name":"Oscar",
    "age":23
}

for key in student:
    print(key)


#Loop Through Dictionary Values
student = {
    "name":"Oscar",
    "age":23
}

for value in student.values():
    print(value)


#Loop Through Dictionary Items
student = {
    "name":"Oscar",
    "age":23
}

for key,value in student.items():
    print(key,value)


#Loop Through String
text = "Python"

for letter in text:
    print(letter)


#Enumerate List
letters = ["a","b","c"]

for index,letter in enumerate(letters):
    print(index,letter)


#Enumerate Starting from 1
letters = ["a","b","c"]

for index,letter in enumerate(letters,start=1):
    print(index,letter)


#While Loop
count = 1

while count <= 5:
    print(count)
    count += 1


#Infinite Loop
#while True:
#    print("Hello")


#Break
for i in range(10):

    if i == 5:
        break

    print(i)


#Continue
for i in range(10):

    if i == 5:
        continue

    print(i)


#Pass
for i in range(5):

    pass


#Else with For
for i in range(5):
    print(i)

else:
    print("Finished")


#Else with Break
for i in range(5):

    if i == 3:
        break

else:
    print("Finished")


#Else with While
count = 1

while count <= 3:
    print(count)
    count += 1

else:
    print("Done")


#Nested Loop
for i in range(3):

    for j in range(3):
        print(i,j)


#Nested Loop with List
names = ["Oscar","Alex"]

ages = [23,22]

for name in names:

    for age in ages:
        print(name,age)


#Multiplication Table
for i in range(1,6):

    for j in range(1,6):
        print(i*j,end=" ")

    print()


#Loop Through Index
numbers = [10,20,30]

for i in range(len(numbers)):
    print(numbers[i])


#Zip Loop
names = ["Oscar","Alex"]
ages = [23,22]

for name,age in zip(names,ages):
    print(name,age)


#Reversed Loop
numbers = [10,20,30]

for number in reversed(numbers):
    print(number)


#Sorted Loop
numbers = [4,1,3,2]

for number in sorted(numbers):
    print(number)


#Reverse Sorted Loop
numbers = [4,1,3,2]

for number in sorted(numbers,reverse=True):
    print(number)


#Loop with Condition
numbers = [1,2,3,4,5]

for number in numbers:

    if number % 2 == 0:
        print(number)


#Count Even Numbers
numbers = [1,2,3,4,5,6]

count = 0

for number in numbers:

    if number % 2 == 0:
        count += 1

print(count)


#Sum Numbers
numbers = [10,20,30]

total = 0

for number in numbers:
    total += number

print(total)


#Maximum Number
numbers = [10,80,20,50]

maximum = numbers[0]

for number in numbers:

    if number > maximum:
        maximum = number

print(maximum)


#Minimum Number
numbers = [10,80,20,50]

minimum = numbers[0]

for number in numbers:

    if number < minimum:
        minimum = number

print(minimum)


#Count Characters
text = "Gravity"

count = 0

for letter in text:
    count += 1

print(count)


#Character Frequency
text = "banana"

for letter in set(text):
    print(letter,text.count(letter))


#Find First Match
numbers = [10,20,30,40]

for number in numbers:

    if number > 25:
        print(number)
        break


#Search Item
numbers = [10,20,30]

target = 20

for number in numbers:

    if number == target:
        print("Found")
        break


#Countdown
for i in range(10,0,-1):
    print(i)

print("Lift Off!")


#Loop Through Two Lists
names = ["Oscar","Alex"]
courses = ["Python","Java"]

for name,course in zip(names,courses):
    print(name,course)


#Loop Through Dictionary with Enumerate
student = {
    "name":"Oscar",
    "age":23
}

for index,(key,value) in enumerate(student.items(),start=1):
    print(index,key,value)


#Loop Through File
#with open("test.txt") as file:
#    for line in file:
#        print(line.strip())


#Loop Variable after Loop
for i in range(5):
    pass

print(i)


#Repeat String
for i in range(5):
    print("*"*i)


#Triangle Pattern
for i in range(1,6):
    print("*"*i)


#Reverse Triangle
for i in range(5,0,-1):
    print("*"*i)

#List Comprehension
numbers = [x for x in range(10)]

print(numbers)


#List Comprehension with Condition
numbers = [x for x in range(10) if x % 2 == 0]

print(numbers)


#Dictionary Comprehension
numbers = {x:x*x for x in range(5)}

print(numbers)


#Set Comprehension
numbers = {x for x in range(10)}

print(numbers)


#Generator Expression
numbers = (x*x for x in range(5))

for number in numbers:
    print(number)


#Nested List Comprehension
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]

print(matrix)


#Flatten Nested List
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = [number for row in matrix for number in row]

print(flat)


#Nested Loop Pattern
for i in range(1,6):

    for j in range(i):
        print("*", end="")

    print()


#Number Pattern
for i in range(1,6):

    for j in range(1,i+1):
        print(j, end=" ")

    print()


#Reverse Number Pattern
for i in range(5,0,-1):

    for j in range(1,i+1):
        print(j, end=" ")

    print()


#Multiplication Table
for i in range(1,11):

    for j in range(1,11):
        print(f"{i*j:4}", end="")

    print()


#Count Vowels
text = "Gravity Works AI"

count = 0

for letter in text.lower():

    if letter in "aeiou":
        count += 1

print(count)


#Count Consonants
text = "Gravity Works AI"

count = 0

for letter in text.lower():

    if letter.isalpha() and letter not in "aeiou":
        count += 1

print(count)


#Reverse String
text = "Python"

for letter in reversed(text):
    print(letter, end="")

print()


#Palindrome
text = "madam"

print(text == text[::-1])


#Find Duplicates
numbers = [1,2,2,3,4,4,5]

seen = set()

for number in numbers:

    if number in seen:
        print(number)

    seen.add(number)


#Remove Duplicates
numbers = [1,2,2,3,4,4,5]

unique = []

for number in numbers:

    if number not in unique:
        unique.append(number)

print(unique)


#Frequency Counter
text = "banana"

frequency = {}

for letter in text:
    frequency[letter] = frequency.get(letter,0) + 1

print(frequency)


#Largest Element
numbers = [15,90,25,40]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print(largest)


#Smallest Element
numbers = [15,90,25,40]

smallest = numbers[0]

for number in numbers:

    if number < smallest:
        smallest = number

print(smallest)


#Average
numbers = [10,20,30,40]

total = 0

for number in numbers:
    total += number

print(total / len(numbers))


#Any
numbers = [0,0,1]

print(any(numbers))


#All
numbers = [1,2,3]

print(all(numbers))


#Iter
numbers = [10,20,30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


#Loop using next()
numbers = [1,2,3]

iterator = iter(numbers)

while True:

    try:
        print(next(iterator))

    except StopIteration:
        break


#Infinite Counter
count = 0

while True:

    print(count)

    count += 1

    if count == 5:
        break


#Skip Odd Numbers
for i in range(10):

    if i % 2 != 0:
        continue

    print(i)


#While with Continue
count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)


#While with Break
count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1


#Enumerate String
text = "Python"

for index,letter in enumerate(text):
    print(index,letter)


#Zip Three Lists
names = ["Oscar","Alex"]
ages = [23,22]
courses = ["Python","Java"]

for name,age,course in zip(names,ages,courses):
    print(name,age,course)


#Loop Through Multiple Dictionaries
a = {"x":1,"y":2}
b = {"a":10,"b":20}

for item1,item2 in zip(a.items(),b.items()):
    print(item1,item2)


#Cartesian Product
letters = ["A","B"]
numbers = [1,2,3]

for letter in letters:

    for number in numbers:
        print(letter,number)


#Transpose Matrix
matrix = [
    [1,2,3],
    [4,5,6]
]

for row in zip(*matrix):
    print(row)


#Loop Through Range Object
numbers = range(5)

for number in numbers:
    print(number)


#Loop with Lambda
numbers = [1,2,3,4]

for number in map(lambda x:x*x, numbers):
    print(number)


#Filter Loop
numbers = [1,2,3,4,5,6]

for number in filter(lambda x:x%2==0, numbers):
    print(number)


#Product using Loop
result = 1

for number in [1,2,3,4]:
    result *= number

print(result)


#Factorial
result = 1

for number in range(1,6):
    result *= number

print(result)


#Fibonacci
a,b = 0,1

for i in range(10):

    print(a)

    a,b = b,a+b


#Prime Number
number = 29

for i in range(2,number):

    if number%i==0:
        print("Not Prime")
        break

else:
    print("Prime")


#Nested Enumerate
matrix = [
    [10,20],
    [30,40]
]

for row_index,row in enumerate(matrix):

    for col_index,value in enumerate(row):
        print(row_index,col_index,value)


#Loop Until User Input
#while True:
#    text = input("Enter : ")
#
#    if text == "quit":
#        break
#
#    print(text)


#Loop Through Bytes
data = b"Python"

for byte in data:
    print(byte)


#Loop Through Unicode
text = "Python"

for letter in text:
    print(letter, ord(letter))