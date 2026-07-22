#Create Dictionary
student = {
    "name": "Oscar",
    "age": 23,
    "course": "Python"
}

print(student)


#Dictionary using dict()
student = dict(name="Oscar", age=23, course="Python")

print(student)


#Access Value
student = {
    "name": "Oscar",
    "age": 23
}

print(student["name"])


#Access using get()
student = {
    "name": "Oscar",
    "age": 23
}

print(student.get("name"))


#get() Returns None if Key Doesn't Exist
student = {
    "name": "Oscar"
}

print(student.get("phone"))


#get() with Default Value
student = {
    "name": "Oscar"
}

print(student.get("phone", "Not Found"))


#Change Value
student = {
    "name": "Oscar",
    "age": 23
}

student["age"] = 24

print(student)


#Add New Key
student = {
    "name": "Oscar"
}

student["phone"] = "9876543210"

print(student)


#update() Existing Key
student = {
    "name": "Oscar",
    "age":23
}

student.update({"age":24})

print(student)


#update() Multiple Keys
student = {
    "name":"Oscar"
}

student.update({
    "age":23,
    "course":"Python"
})

print(student)


#Length of Dictionary
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

print(len(student))


#Keys
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

print(student.keys())


#Values
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

print(student.values())


#Items
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

print(student.items())


#Loop Through Keys
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

for key in student:
    print(key)


#Loop Through Values
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

for value in student.values():
    print(value)


#Loop Through Keys using keys()
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

for key in student.keys():
    print(key)


#Loop Through Items
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

for item in student.items():
    print(item)


#Better Loop Through Items
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

for key, value in student.items():
    print(key, value)


#Check if Key Exists
student = {
    "name":"Oscar",
    "age":23
}

print("name" in student)
print("phone" in student)


#Check if Key Doesn't Exist
student = {
    "name":"Oscar"
}

print("phone" not in student)


#Delete Key using del
student = {
    "name":"Oscar",
    "age":23
}

del student["age"]

print(student)


#Delete using pop()
student = {
    "name":"Oscar",
    "age":23
}

student.pop("age")

print(student)


#pop() Returns Removed Value
student = {
    "name":"Oscar",
    "age":23
}

age = student.pop("age")

print(age)
print(student)


#Remove Last Item
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

print(student.popitem())
print(student)


#Clear Dictionary
student = {
    "name":"Oscar",
    "age":23
}

student.clear()

print(student)


#Copy Dictionary
student = {
    "name":"Oscar",
    "age":23
}

student2 = student.copy()

print(student2)


#Assignment Creates Same Object
student = {
    "name":"Oscar"
}

student2 = student

student2["name"] = "Gravity"

print(student)
print(student2)


#copy() Creates New Object
student = {
    "name":"Oscar"
}

student2 = student.copy()

student2["name"] = "Gravity"

print(student)
print(student2)


#Dictionary from List
keys = ["name","age","course"]

student = dict.fromkeys(keys)

print(student)


#Dictionary from List with Default Value
keys = ["name","age","course"]

student = dict.fromkeys(keys, "Unknown")

print(student)


#Nested Dictionary
students = {
    "student1":{
        "name":"Oscar",
        "age":23
    },
    "student2":{
        "name":"Alex",
        "age":22
    }
}

print(students)


#Access Nested Dictionary
students = {
    "student1":{
        "name":"Oscar",
        "age":23
    }
}

print(students["student1"]["name"])


#Mixed Data Types
student = {
    "name":"Oscar",
    "age":23,
    "marks":[90,80,95],
    "active":True
}

print(student)


#Dictionary with List
student = {
    "name":"Oscar",
    "languages":["Python","Java","C++"]
}

print(student["languages"])
print(student["languages"][0])


#Dictionary with Tuple
student = {
    "position":(10,20)
}

print(student["position"])


#Dictionary with Set
student = {
    "subjects":{"Math","Physics","AI"}
}

print(student)


#Dictionary with Another Dictionary
student = {
    "address":{
        "city":"Delhi",
        "country":"India"
    }
}

print(student["address"]["city"])


#Maximum Key
numbers = {
    10:"A",
    50:"B",
    30:"C"
}

print(max(numbers))


#Minimum Key
numbers = {
    10:"A",
    50:"B",
    30:"C"
}

print(min(numbers))


#Sorted Keys
student = {
    "name":"Oscar",
    "course":"Python",
    "age":23
}

print(sorted(student))


#Sorted Items
student = {
    "name":"Oscar",
    "course":"Python",
    "age":23
}

print(sorted(student.items()))

#setdefault() Returns Existing Value
student = {
    "name":"Oscar",
    "age":23
}

print(student.setdefault("name","Unknown"))
print(student)


#setdefault() Adds New Key
student = {
    "name":"Oscar"
}

print(student.setdefault("age",23))
print(student)


#Dictionary Comprehension
squares = {x:x*x for x in range(1,6)}

print(squares)


#Dictionary Comprehension with Condition
numbers = {x:x*x for x in range(10) if x % 2 == 0}

print(numbers)


#Swap Keys and Values
student = {
    "name":"Oscar",
    "course":"Python"
}

new_dict = {value:key for key,value in student.items()}

print(new_dict)


#Merge Dictionaries (Python 3.9+)
student = {
    "name":"Oscar"
}

info = {
    "age":23,
    "course":"Python"
}

print(student | info)


#Merge using update()
student = {
    "name":"Oscar"
}

info = {
    "age":23
}

student.update(info)

print(student)


#Merge using **
student = {
    "name":"Oscar"
}

info = {
    "age":23
}

new_dict = {**student, **info}

print(new_dict)


#Enumerate Dictionary
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

for index, item in enumerate(student.items(), start=1):
    print(index, item)


#Reverse Dictionary Keys
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

for key in reversed(student):
    print(key)


#Sort Dictionary by Keys
student = {
    "course":"Python",
    "age":23,
    "name":"Oscar"
}

for key in sorted(student):
    print(key, student[key])


#Sort Dictionary by Values
student = {
    "A":90,
    "B":70,
    "C":80
}

print(sorted(student.items(), key=lambda item:item[1]))


#Sort Dictionary by Values Descending
student = {
    "A":90,
    "B":70,
    "C":80
}

print(sorted(student.items(), key=lambda item:item[1], reverse=True))


#Largest Value
student = {
    "A":90,
    "B":70,
    "C":80
}

print(max(student.values()))


#Smallest Value
student = {
    "A":90,
    "B":70,
    "C":80
}

print(min(student.values()))


#Key with Maximum Value
student = {
    "A":90,
    "B":70,
    "C":80
}

print(max(student, key=student.get))


#Key with Minimum Value
student = {
    "A":90,
    "B":70,
    "C":80
}

print(min(student, key=student.get))


#Sum of Values
student = {
    "A":90,
    "B":70,
    "C":80
}

print(sum(student.values()))


#Average of Values
student = {
    "A":90,
    "B":70,
    "C":80
}

print(sum(student.values()) / len(student))


#Count Frequency
text = "banana"

frequency = {}

for letter in text:
    frequency[letter] = frequency.get(letter,0) + 1

print(frequency)


#Word Frequency
sentence = "python java python ai python"

frequency = {}

for word in sentence.split():
    frequency[word] = frequency.get(word,0) + 1

print(frequency)


#Remove Key Safely
student = {
    "name":"Oscar"
}

student.pop("age",None)

print(student)


#Dictionary Length
student = {
    "name":"Oscar",
    "age":23
}

print(len(student))


#Check Empty Dictionary
student = {}

print(not student)


#Nested Loop
students = {
    "student1":{"name":"Oscar","age":23},
    "student2":{"name":"Alex","age":22}
}

for student,data in students.items():
    print(student)

    for key,value in data.items():
        print(key,value)


#Dictionary inside List
students = [
    {"name":"Oscar","age":23},
    {"name":"Alex","age":22}
]

for student in students:
    print(student["name"])


#List inside Dictionary
student = {
    "subjects":["Math","Physics","AI"]
}

for subject in student["subjects"]:
    print(subject)


#Get Multiple Values
student = {
    "name":"Oscar",
    "age":23,
    "course":"Python"
}

print(student.get("name"))
print(student.get("course"))


#Dictionary Equality
a = {"x":1,"y":2}
b = {"y":2,"x":1}

print(a == b)


#Dictionary Identity
a = {"x":1}
b = a

print(a is b)


#Copy Identity
a = {"x":1}
b = a.copy()

print(a is b)


#Dictionary Keys as Tuple
student = {
    "name":"Oscar",
    "age":23
}

print(tuple(student.keys()))


#Dictionary Values as List
student = {
    "name":"Oscar",
    "age":23
}

print(list(student.values()))


#Dictionary Items as List
student = {
    "name":"Oscar",
    "age":23
}

print(list(student.items()))


#Build Dictionary from Two Lists
keys = ["name","age","course"]
values = ["Oscar",23,"Python"]

student = dict(zip(keys,values))

print(student)


#Zip Dictionary
student = {
    "name":"Oscar",
    "age":23
}

for key,value in zip(student.keys(),student.values()):
    print(key,value)


#Dictionary from Enumeration
letters = ["a","b","c","d"]

print(dict(enumerate(letters)))


#Dictionary from Range
numbers = {x:x*x for x in range(1,11)}

print(numbers)


#Filter Dictionary
numbers = {
    "a":10,
    "b":25,
    "c":30,
    "d":15
}

filtered = {k:v for k,v in numbers.items() if v >= 20}

print(filtered)


#Common Keys
a = {"a":1,"b":2,"c":3}
b = {"b":10,"c":20,"d":30}

print(a.keys() & b.keys())


#Common Items
a = {"a":1,"b":2}
b = {"a":1,"b":3}

print(a.items() & b.items())


#Different Keys
a = {"a":1,"b":2}
b = {"b":2,"c":3}

print(a.keys() - b.keys())


#Dictionary Union of Keys
a = {"a":1,"b":2}
b = {"c":3,"d":4}

print(a.keys() | b.keys())


#Print Keys Only
student = {
    "name":"Oscar",
    "age":23
}

print(*student)


#Print Values Only
student = {
    "name":"Oscar",
    "age":23
}

print(*student.values())


#Print Items
student = {
    "name":"Oscar",
    "age":23
}

print(*student.items())


#Dictionary Size in Memory
student = {
    "name":"Oscar",
    "age":23
}

print(student.__sizeof__())

