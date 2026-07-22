#Count Iterator
from itertools import count

counter = count(1)

print(next(counter))
print(next(counter))
print(next(counter))


#Count with Step
from itertools import count

counter = count(10,5)

print(next(counter))
print(next(counter))
print(next(counter))


#Cycle Iterator
from itertools import cycle

letters = cycle(["A","B","C"])

print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))


#Repeat Object
from itertools import repeat

numbers = repeat(100,5)

print(list(numbers))


#Accumulate Sum
from itertools import accumulate

numbers = [1,2,3,4,5]

print(list(accumulate(numbers)))


#Accumulate Multiplication
from itertools import accumulate
import operator

numbers = [1,2,3,4]

print(list(accumulate(numbers, operator.mul)))


#Chain Lists
from itertools import chain

result = chain([1,2],[3,4],[5,6])

print(list(result))


#Chain from Iterable
from itertools import chain

lists = [
    [1,2],
    [3,4],
    [5,6]
]

print(list(chain.from_iterable(lists)))


#Compress
from itertools import compress

letters = ["A","B","C","D"]
selectors = [1,0,1,0]

print(list(compress(letters,selectors)))


#Dropwhile
from itertools import dropwhile

numbers = [1,2,3,4,1,2]

print(list(dropwhile(lambda x:x<3,numbers)))


#Takewhile
from itertools import takewhile

numbers = [1,2,3,4,1]

print(list(takewhile(lambda x:x<4,numbers)))


#Filterfalse
from itertools import filterfalse

numbers = [1,2,3,4,5]

print(list(filterfalse(lambda x:x%2==0,numbers)))


#Islice
from itertools import islice

numbers = range(20)

print(list(islice(numbers,5)))
print(list(islice(range(20),5,10)))
print(list(islice(range(20),0,20,3)))


#Pairwise (Python 3.10+)
from itertools import pairwise

numbers = [10,20,30,40]

print(list(pairwise(numbers)))


#Batched (Python 3.12+)
#from itertools import batched
#
#numbers = range(10)
#
#print(list(batched(numbers,3)))


#Zip Longest
from itertools import zip_longest

names = ["Oscar","Alex"]
ages = [23]

print(list(zip_longest(names,ages,fillvalue=0)))


#Product
from itertools import product

print(list(product([1,2],["A","B"])))


#Product Repeat
from itertools import product

print(list(product([0,1], repeat=3)))


#Permutations
from itertools import permutations

print(list(permutations([1,2,3])))


#Permutations Length
from itertools import permutations

print(list(permutations([1,2,3],2)))


#Combinations
from itertools import combinations

print(list(combinations([1,2,3,4],2)))


#Combinations with Replacement
from itertools import combinations_with_replacement

print(list(combinations_with_replacement([1,2,3],2)))

#Count Iterator
from itertools import count

counter = count(1)

print(next(counter))
print(next(counter))
print(next(counter))


#Count with Step
from itertools import count

counter = count(10,5)

print(next(counter))
print(next(counter))
print(next(counter))


#Cycle Iterator
from itertools import cycle

letters = cycle(["A","B","C"])

print(next(letters))
print(next(letters))
print(next(letters))
print(next(letters))


#Repeat Object
from itertools import repeat

numbers = repeat(100,5)

print(list(numbers))


#Accumulate Sum
from itertools import accumulate

numbers = [1,2,3,4,5]

print(list(accumulate(numbers)))


#Accumulate Multiplication
from itertools import accumulate
import operator

numbers = [1,2,3,4]

print(list(accumulate(numbers, operator.mul)))


#Chain Lists
from itertools import chain

result = chain([1,2],[3,4],[5,6])

print(list(result))


#Chain from Iterable
from itertools import chain

lists = [
    [1,2],
    [3,4],
    [5,6]
]

print(list(chain.from_iterable(lists)))


#Compress
from itertools import compress

letters = ["A","B","C","D"]
selectors = [1,0,1,0]

print(list(compress(letters,selectors)))


#Dropwhile
from itertools import dropwhile

numbers = [1,2,3,4,1,2]

print(list(dropwhile(lambda x:x<3,numbers)))


#Takewhile
from itertools import takewhile

numbers = [1,2,3,4,1]

print(list(takewhile(lambda x:x<4,numbers)))


#Filterfalse
from itertools import filterfalse

numbers = [1,2,3,4,5]

print(list(filterfalse(lambda x:x%2==0,numbers)))


#Islice
from itertools import islice

numbers = range(20)

print(list(islice(numbers,5)))
print(list(islice(range(20),5,10)))
print(list(islice(range(20),0,20,3)))


#Pairwise (Python 3.10+)
from itertools import pairwise

numbers = [10,20,30,40]

print(list(pairwise(numbers)))


#Batched (Python 3.12+)
#from itertools import batched
#
#numbers = range(10)
#
#print(list(batched(numbers,3)))


#Zip Longest
from itertools import zip_longest

names = ["Oscar","Alex"]
ages = [23]

print(list(zip_longest(names,ages,fillvalue=0)))


#Product
from itertools import product

print(list(product([1,2],["A","B"])))


#Product Repeat
from itertools import product

print(list(product([0,1], repeat=3)))


#Permutations
from itertools import permutations

print(list(permutations([1,2,3])))


#Permutations Length
from itertools import permutations

print(list(permutations([1,2,3],2)))


#Combinations
from itertools import combinations

print(list(combinations([1,2,3,4],2)))


#Combinations with Replacement
from itertools import combinations_with_replacement

print(list(combinations_with_replacement([1,2,3],2)))