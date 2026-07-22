letters = ['a', 'b', 'c', 'd']
letters[0]  = 'A'
print(letters)


numbers = list(range(20))
print (numbers[::2])


#unpack lists
nomb = [1,2,3,4,5]
first, second, third = nomb[0], nomb[1], nomb[2]
print(first, second, third)


#unpack 2 Print individuals as it is and the rest of the list as *other.
#you dont have to assign that to a variable, you can just print it directly.
Nomb2 = [1,2,3,4,5]
first, second, *other = Nomb2
nuum = first, second, *other
print(nuum)


#if you care only about the first and last elements of a list, you can unpack them like this:
Nomb3 = [1,2,3,4,5]
first, *_, last = Nomb3
print(first, last)
print(_)


#how to loop over a list. Its read only, we cannot add new items to it.
letters = ['a', 'b', 'c', 'd']
for letter in enumerate(letters):
    print(letter[0], letter[1])
    #But this is little bit ugly.

#this is better method to do same.
letters1 = ['a', 'b', 'c', 'd']
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters1):
    print(index, letter)


letters2 = ['a', 'b', 'c']

#Add 
letters2.append('d')
#If you want to add an item at a specific position you should use the insert() method
letters2.insert(0, "-")
print(letters2) 

#this will remove the last item from the list.
letters2.pop()
#or letters2.pop(0) for specific index.
#if you dont know the index of the item you want to remove, you can use the remove() method.
letters2.remove('b')
#Another method is to use the del keyword. This will remove the item at the specified index.
del letters2[0:2]
#to remove all the items from the list, you can use the clear() method.
letters2.clear()
#finding items. how to find index of an item in a list. You can use the index() method.
print(letters2.index('c')) #this will return the index of the first occurrence of the item in the list.


motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycle = ['hero', 'maybach']
motorcycles.insert(0, motorcycle)
print(motorcycles[0])


motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.reverse()
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
numbers = [1,5,2,4,3]
motorcycles.sort()
numbers.sort()
print(motorcycles)
print(numbers)


motorcycles = ['honda', 'yamaha', 'suzuki']
numbers = [1,5,2,4,3]
motorcycles.sort(reverse = True)
numbers.sort(reverse = True)
print(motorcycles)
print(numbers)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles.index('yamaha'))


motorcycles = ['honda', 'yamaha', 'suzuki']
print('honda' in motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
for nigga in enumerate(motorcycles):
    print(nigga)


motorcycles = ['honda', 'yamaha', 'suzuki']
for index, nigga in enumerate(motorcycles, start = 1):
    print(index , nigga) 


courses = {'History', 'Math', 'Physics', 'CompSci'}
course2 = {'History', 'Math', 'art', 'design'}

print(courses.difference(course2))
