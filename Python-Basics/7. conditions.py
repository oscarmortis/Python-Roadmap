#Simple if
age = 20

if age >= 18:
    print("Adult")


#if else
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


#if elif else
marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")


#Compare Numbers
a = 20
b = 10

if a > b:
    print("A is Greater")


#Less Than
a = 5
b = 10

if a < b:
    print("A is Smaller")


#Greater Than or Equal
a = 10
b = 10

if a >= b:
    print(True)


#Less Than or Equal
a = 5
b = 10

if a <= b:
    print(True)


#Equal
a = 100
b = 100

if a == b:
    print("Equal")


#Not Equal
a = 10
b = 20

if a != b:
    print("Different")


#Boolean Variable
is_logged_in = True

if is_logged_in:
    print("Welcome")


#Boolean False
is_logged_in = False

if not is_logged_in:
    print("Login First")


#and Operator
age = 25
country = "India"

if age >= 18 and country == "India":
    print("Eligible")


#or Operator
role = "admin"

if role == "admin" or role == "owner":
    print("Access Granted")


#not Operator
logged_in = False

if not logged_in:
    print("Please Login")


#Nested if
age = 22

if age >= 18:

    if age >= 21:
        print("Can Enter")


#Multiple Conditions
age = 25
salary = 50000

if age > 18 and salary >= 30000:
    print("Approved")


#Check Empty List
numbers = []

if not numbers:
    print("Empty List")


#Check Empty String
text = ""

if not text:
    print("Empty String")


#Check Empty Dictionary
student = {}

if not student:
    print("Empty Dictionary")


#Check Empty Set
numbers = set()

if not numbers:
    print("Empty Set")


#Membership
course = "Python"

if "P" in course:
    print("Found")


#Not Membership
course = "Python"

if "J" not in course:
    print("Not Found")


#Identity
a = [1,2,3]
b = a

if a is b:
    print("Same Object")


#Not Identity
a = [1,2]
b = [1,2]

if a is not b:
    print("Different Objects")


#Truthy Values
value = [1]

if value:
    print("True")


#Falsy Values
value = 0

if not value:
    print("False")


#None Check
name = None

if name is None:
    print("No Name")


#is not None
name = "Oscar"

if name is not None:
    print(name)


#One-line if
age = 20

if age >= 18: print("Adult")


#One-line if else
age = 15

print("Adult") if age >= 18 else print("Minor")


#Ternary Operator
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


#Maximum Number
a = 20
b = 30

maximum = a if a > b else b

print(maximum)


#Minimum Number
a = 20
b = 30

minimum = a if a < b else b

print(minimum)


#Even or Odd
number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


#Positive Negative Zero
number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


#Leap Year
year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")


#Divisible by Both
number = 30

if number % 3 == 0 and number % 5 == 0:
    print("Divisible")


#Password Check
password = "python123"

if password == "python123":
    print("Correct Password")
else:
    print("Wrong Password")


#Age Category
age = 65

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")


#Check Character
letter = "A"

if letter.isupper():
    print("Uppercase")
else:
    print("Lowercase")


#Check Digit
text = "8"

if text.isdigit():
    print("Number")


#Check Alphabet
text = "P"

if text.isalpha():
    print("Alphabet")


#Check Alphanumeric
text = "Python3"

if text.isalnum():
    print("Alphanumeric")


#Chained Comparison
age = 25

if 18 <= age <= 60:
    print("Eligible")


#Multiple Chained Comparison
number = 15

if 10 < number < 20:
    print("Between")


#Compare Strings
a = "apple"
b = "banana"

if a < b:
    print("apple comes first")


#Compare Lists
a = [1,2,3]
b = [1,2,4]

if a < b:
    print(True)


#Compare Tuples
a = (1,2)
b = (1,3)

if a < b:
    print(True)


#Compare Sets
a = {1,2}
b = {1,2,3}

if a < b:
    print("Subset")


#Compare Dictionaries
a = {"name":"Oscar"}
b = {"name":"Oscar"}

print(a == b)


#Nested Ternary
marks = 85

grade = (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "Fail"
)

print(grade)


#Conditional Expression
age = 22

message = "Adult" if age >= 18 else "Minor"

print(message)


#any()
numbers = [0,0,1]

if any(numbers):
    print("At least one True")


#all()
numbers = [1,2,3]

if all(numbers):
    print("All True")


#all() Example
marks = [90,80,70]

if all(mark >= 35 for mark in marks):
    print("Pass")


#any() Example
marks = [20,25,90]

if any(mark >= 90 for mark in marks):
    print("Topper Exists")


#assert
age = 20

assert age >= 18

print("Allowed")


#Walrus Operator
if (length := len("Python")) > 5:
    print(length)


#Walrus in While
count = 0

while (count := count + 1) <= 5:
    print(count)


#match-case
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Unknown")


#match Multiple Values
command = "start"

match command:
    case "run" | "start":
        print("Running")
    case "stop":
        print("Stopped")
    case _:
        print("Unknown")


#match with Variable
point = (2,3)

match point:
    case (x,y):
        print(x,y)


#match List Pattern
numbers = [1,2,3]

match numbers:
    case [a,b,c]:
        print(a,b,c)


#match with Guard
age = 25

match age:
    case value if value >= 18:
        print("Adult")
    case _:
        print("Minor")


#Guard Clause
def login(user):

    if not user:
        return

    print("Welcome", user)

login("Oscar")


#Check Type
value = 100

if isinstance(value, int):
    print("Integer")


#Check Multiple Types
value = 3.14

if isinstance(value, (int,float)):
    print("Number")


#Check Object
numbers = [1,2,3]

if isinstance(numbers, list):
    print("List")


#Dictionary Key Exists
student = {
    "name":"Oscar"
}

if "name" in student:
    print(student["name"])


#Dictionary Key Missing
student = {
    "name":"Oscar"
}

if "age" not in student:
    print("Missing")


#String Startswith
text = "Python"

if text.startswith("Py"):
    print(True)


#String Endswith
text = "Python.py"

if text.endswith(".py"):
    print(True)


#Multiple Conditions in List
numbers = [10,20,30]

if len(numbers) > 0 and max(numbers) > 25:
    print(True)


#Compare Length
text = "Gravity"

if len(text) > 5:
    print("Long String")


#Check Empty Collection
items = []

if items:
    print("Has Items")
else:
    print("Empty")


#Complex Boolean
age = 25
salary = 50000
experience = 3

if age >= 21 and salary >= 30000 and experience >= 2:
    print("Approved")


#Exclusive Condition
a = True
b = False

if a != b:
    print("Only One True")


#Boolean Conversion
text = ""

print(bool(text))


#Short Circuit and
username = ""

username and print("Welcome")


#Short Circuit or
username = ""

print(username or "Guest")


#Default Value
name = None

name = name or "Unknown"

print(name)


#Conditional List
numbers = []

if numbers:
    print(max(numbers))
else:
    print("Empty")


#Conditional Dictionary
student = {}

if student:
    print(student)
else:
    print("No Data")


#Check File Extension
filename = "notes.txt"

if filename.endswith(".txt"):
    print("Text File")


#Check Email
email = "oscar@gmail.com"

if "@" in email and "." in email:
    print("Valid")


#Check Range
number = 55

if 50 <= number <= 100:
    print("Inside Range")


#Compare Two Strings
password = "python"
confirm = "python"

if password == confirm:
    print("Matched")


#Case-insensitive Comparison
a = "Python"
b = "python"

if a.lower() == b.lower():
    print("Equal")


#Find Largest of Three
a = 10
b = 40
c = 25

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


#Check Prime Number
number = 17

if number > 1:

    for i in range(2, number):

        if number % i == 0:
            print("Not Prime")
            break

    else:
        print("Prime")


#Simple Login
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Success")
else:
    print("Login Failed")