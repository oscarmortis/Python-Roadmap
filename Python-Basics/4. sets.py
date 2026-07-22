#Create Set
numbers = {1,2,3,4,5}

print(numbers)


#Create Set using set()
numbers = set([1,2,3,4,5])

print(numbers)


#Create Empty Set
numbers = set()

print(numbers)


#Empty Braces Create Dictionary
numbers = {}

print(type(numbers))


#Set Removes Duplicates
numbers = {1,2,2,3,3,4,5,5}

print(numbers)


#Length of Set
numbers = {1,2,3,4,5}

print(len(numbers))


#Mixed Data Types
data = {1,"Python",True,3.14}

print(data)


#Set is Unordered
numbers = {5,2,1,4,3}

print(numbers)


#Cannot Access by Index
numbers = {1,2,3,4}

#print(numbers[0])


#Add Item
numbers = {1,2,3}

numbers.add(4)

print(numbers)


#Add Existing Item
numbers = {1,2,3}

numbers.add(3)

print(numbers)


#Update Set
numbers = {1,2,3}

numbers.update([4,5,6])

print(numbers)


#Update using Another Set
numbers = {1,2,3}

numbers.update({4,5})

print(numbers)


#Update using Tuple
numbers = {1,2}

numbers.update((3,4))

print(numbers)


#Update using String
letters = {"a","b"}

letters.update("cd")

print(letters)


#Loop Through Set
numbers = {1,2,3,4}

for number in numbers:
    print(number)


#Membership Operator
numbers = {1,2,3,4}

print(2 in numbers)
print(10 in numbers)


#Not in Operator
numbers = {1,2,3}

print(10 not in numbers)


#Remove Item
numbers = {1,2,3,4}

numbers.remove(3)

print(numbers)


#remove() Raises Error
numbers = {1,2,3}

#numbers.remove(10)


#Discard Item
numbers = {1,2,3}

numbers.discard(10)

print(numbers)


#Pop Random Item
numbers = {1,2,3,4}

print(numbers.pop())
print(numbers)


#Clear Set
numbers = {1,2,3}

numbers.clear()

print(numbers)


#Copy Set
numbers = {1,2,3}

copy = numbers.copy()

print(copy)


#Assignment Creates Same Object
numbers = {1,2,3}

copy = numbers

copy.add(10)

print(numbers)
print(copy)


#copy() Creates New Object
numbers = {1,2,3}

copy = numbers.copy()

copy.add(10)

print(numbers)
print(copy)


#Union
a = {1,2,3}
b = {3,4,5}

print(a.union(b))


#Union using |
a = {1,2,3}
b = {3,4,5}

print(a | b)


#Intersection
a = {1,2,3}
b = {3,4,5}

print(a.intersection(b))


#Intersection using &
a = {1,2,3}
b = {3,4,5}

print(a & b)


#Difference
a = {1,2,3}
b = {3,4,5}

print(a.difference(b))


#Difference using -
a = {1,2,3}
b = {3,4,5}

print(a - b)


#Symmetric Difference
a = {1,2,3}
b = {3,4,5}

print(a.symmetric_difference(b))


#Symmetric Difference using ^
a = {1,2,3}
b = {3,4,5}

print(a ^ b)


#Intersection Update
a = {1,2,3}
b = {3,4,5}

a.intersection_update(b)

print(a)


#Difference Update
a = {1,2,3}
b = {3,4,5}

a.difference_update(b)

print(a)


#Symmetric Difference Update
a = {1,2,3}
b = {3,4,5}

a.symmetric_difference_update(b)

print(a)


#Update using Union
a = {1,2}
b = {3,4}

a.update(b)

print(a)


#Subset
a = {1,2}
b = {1,2,3,4}

print(a.issubset(b))


#Subset using <=
a = {1,2}
b = {1,2,3}

print(a <= b)


#Superset
a = {1,2,3,4}
b = {1,2}

print(a.issuperset(b))


#Superset using >=
a = {1,2,3}
b = {1,2}

print(a >= b)


#Disjoint Sets
a = {1,2}
b = {3,4}

print(a.isdisjoint(b))


#Not Disjoint
a = {1,2}
b = {2,3}

print(a.isdisjoint(b))


#Maximum Value
numbers = {10,20,30}

print(max(numbers))


#Minimum Value
numbers = {10,20,30}

print(min(numbers))


#Sum of Set
numbers = {10,20,30}

print(sum(numbers))


#Sorted Set
numbers = {5,2,4,1,3}

print(sorted(numbers))


#Convert List to Set
numbers = [1,2,2,3,3,4]

print(set(numbers))


#Convert Tuple to Set
numbers = (1,2,2,3)

print(set(numbers))


#Convert String to Set
text = "banana"

print(set(text))


#Convert Set to List
numbers = {1,2,3}

print(list(numbers))


#Convert Set to Tuple
numbers = {1,2,3}

print(tuple(numbers))


#Enumerate Set
letters = {"a","b","c"}

for index, letter in enumerate(letters):
    print(index, letter)


#Memory Address
numbers = {1,2,3}

print(id(numbers))


#Memory Size
numbers = {1,2,3}

print(numbers.__sizeof__())

#Set Comprehension
numbers = {x for x in range(10)}

print(numbers)


#Set Comprehension with Squares
numbers = {x*x for x in range(6)}

print(numbers)


#Set Comprehension with Condition
numbers = {x for x in range(20) if x % 2 == 0}

print(numbers)


#Remove Duplicates from List
numbers = [1,2,2,3,4,4,5,5]

unique = list(set(numbers))

print(unique)


#Unique Characters
text = "banana"

print(set(text))


#Common Characters
a = "gravity"
b = "artificial"

print(set(a) & set(b))


#Different Characters
a = "gravity"
b = "artificial"

print(set(a) - set(b))


#Unique Characters from Both Strings
a = "gravity"
b = "artificial"

print(set(a) ^ set(b))


#Union of Multiple Sets
a = {1,2}
b = {3,4}
c = {5,6}

print(a.union(b, c))


#Intersection of Multiple Sets
a = {1,2,3,4}
b = {2,3,5}
c = {3,6}

print(a.intersection(b, c))


#Difference of Multiple Sets
a = {1,2,3,4,5}
b = {2,3}
c = {5}

print(a.difference(b, c))


#Update with Multiple Collections
numbers = {1,2}

numbers.update([3,4], (5,6), {7,8})

print(numbers)


#Remove Multiple Items
numbers = {1,2,3,4,5}

numbers.difference_update({2,4})

print(numbers)


#Filter Even Numbers
numbers = {1,2,3,4,5,6,7,8}

even = {x for x in numbers if x % 2 == 0}

print(even)


#Filter Odd Numbers
numbers = {1,2,3,4,5,6,7,8}

odd = {x for x in numbers if x % 2 != 0}

print(odd)


#Largest Set
sets = [{1,2}, {1,2,3,4}, {1}]

print(max(sets, key=len))


#Smallest Set
sets = [{1,2}, {1,2,3,4}, {1}]

print(min(sets, key=len))


#Length of Every Set
sets = [{1,2}, {1,2,3}, {1,2,3,4}]

for item in sets:
    print(len(item))


#Flatten Nested Sets
sets = [{1,2}, {3,4}, {5,6}]

flat = set()

for item in sets:
    flat.update(item)

print(flat)


#Set Equality
a = {1,2,3}
b = {3,2,1}

print(a == b)


#Set Identity
a = {1,2,3}
b = a

print(a is b)


#Copy Identity
a = {1,2,3}
b = a.copy()

print(a is b)


#Frozen Set
numbers = frozenset([1,2,3,4])

print(numbers)


#Frozen Set is Immutable
numbers = frozenset([1,2,3])

#numbers.add(4)


#Frozen Set Union
a = frozenset({1,2})
b = frozenset({2,3})

print(a | b)


#Frozen Set Intersection
a = frozenset({1,2})
b = frozenset({2,3})

print(a & b)


#Frozen Set Difference
a = frozenset({1,2})
b = frozenset({2,3})

print(a - b)


#Frozen Set Symmetric Difference
a = frozenset({1,2})
b = frozenset({2,3})

print(a ^ b)


#Frozen Set as Dictionary Key
points = {
    frozenset({1,2}): "A",
    frozenset({3,4}): "B"
}

print(points)


#Hash of Frozen Set
numbers = frozenset({1,2,3})

print(hash(numbers))


#Any
numbers = {0,0,1}

print(any(numbers))


#All
numbers = {1,2,3}

print(all(numbers))


#Check Empty Set
numbers = set()

print(not numbers)


#Build Set from Range
numbers = set(range(10))

print(numbers)


#Zip to Set
names = ["Oscar","Alex","John"]
ages = [23,22,21]

print(set(zip(names, ages)))


#Enumerate to Set
letters = ["a","b","c"]

print(set(enumerate(letters)))


#Filter with Set
numbers = set(filter(lambda x: x % 2 == 0, range(10)))

print(numbers)


#Map with Set
numbers = set(map(lambda x: x*x, range(6)))

print(numbers)


#Cartesian Product using Set Comprehension
a = {1,2}
b = {"A","B"}

pairs = {(x, y) for x in a for y in b}

print(pairs)


#Find Missing Values
all_numbers = set(range(1,11))
present = {1,2,3,5,6,8,10}

print(all_numbers - present)


#Find Duplicate Values
numbers = [1,2,2,3,4,4,5]

seen = set()
duplicates = set()

for number in numbers:
    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print(duplicates)


#Check Unique Elements
numbers = [1,2,3,4]

print(len(numbers) == len(set(numbers)))


#Remove Common Elements
a = {1,2,3,4}
b = {3,4,5,6}

print(a - b)
print(b - a)


#Toggle Membership
numbers = {1,2,3}

value = 2

if value in numbers:
    numbers.remove(value)
else:
    numbers.add(value)

print(numbers)


#Print Set
numbers = {1,2,3,4}

print(*numbers)


#Sort Before Printing
numbers = {5,1,4,2,3}

print(*sorted(numbers))


#Reverse Sorted Set
numbers = {5,1,4,2,3}

print(sorted(numbers, reverse=True))