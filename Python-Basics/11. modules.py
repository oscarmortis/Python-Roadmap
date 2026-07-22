#Import Module
import math

print(math.sqrt(25))


#Import Specific Function
from math import sqrt

print(sqrt(64))


#Import Multiple Functions
from math import sqrt, ceil, floor

print(sqrt(16))
print(ceil(4.2))
print(floor(4.8))


#Import Everything (Not Recommended)
from math import *

print(pi)
print(sqrt(100))


#Module Alias
import math as m

print(m.factorial(5))


#Function Alias
from math import factorial as fact

print(fact(5))


#Import Custom Module
#import mymodule
#
#mymodule.greet()


#Import Specific Function from Custom Module
#from mymodule import greet
#
#greet()


#Import Custom Module with Alias
#import mymodule as mm
#
#mm.greet()


#Module Name
import math

print(math.__name__)


#Built-in Module
import random

print(random.randint(1,10))


#Random Choice
import random

names = ["Oscar","Alex","John"]

print(random.choice(names))


#Random Sample
import random

numbers = [1,2,3,4,5]

print(random.sample(numbers,3))


#Shuffle List
import random

numbers = [1,2,3,4,5]

random.shuffle(numbers)

print(numbers)


#Random Float
import random

print(random.random())


#Random Range
import random

print(random.randrange(1,100,5))


#Math Module
import math

print(math.pi)
print(math.e)


#Power
import math

print(math.pow(2,5))


#Square Root
import math

print(math.sqrt(49))


#Factorial
import math

print(math.factorial(6))


#GCD
import math

print(math.gcd(24,36))


#LCM
import math

print(math.lcm(12,18))


#Ceil
import math

print(math.ceil(4.2))


#Floor
import math

print(math.floor(4.8))


#Truncate
import math

print(math.trunc(4.9))


#Absolute
import math

print(math.fabs(-25))


#Log
import math

print(math.log(100))


#Log Base 10
import math

print(math.log10(1000))


#Log Base 2
import math

print(math.log2(64))


#Exponent
import math

print(math.exp(2))


#Sin
import math

print(math.sin(math.radians(90)))


#Cos
import math

print(math.cos(math.radians(0)))


#Tan
import math

print(math.tan(math.radians(45)))


#Degrees
import math

print(math.degrees(math.pi))


#Radians
import math

print(math.radians(180))


#Statistics Mean
import statistics

numbers = [10,20,30,40]

print(statistics.mean(numbers))


#Statistics Median
import statistics

numbers = [10,20,30,40]

print(statistics.median(numbers))


#Statistics Mode
import statistics

numbers = [1,2,2,3]

print(statistics.mode(numbers))


#Statistics Sum
numbers = [10,20,30]

print(sum(numbers))


#Maximum
numbers = [5,20,10]

print(max(numbers))


#Minimum
numbers = [5,20,10]

print(min(numbers))

#Current Date
from datetime import date

print(date.today())


#Current Date and Time
from datetime import datetime

print(datetime.now())


#Create Date
from datetime import date

birthday = date(2003,7,30)

print(birthday)


#Create Time
from datetime import time

current = time(10,30,15)

print(current)


#Timedelta
from datetime import datetime, timedelta

today = datetime.now()

print(today + timedelta(days=7))


#Date Formatting
from datetime import datetime

today = datetime.now()

print(today.strftime("%d-%m-%Y"))


#String to Date
from datetime import datetime

date = datetime.strptime("30-07-2003","%d-%m-%Y")

print(date)


#Time Module
import time

print(time.time())


#Sleep
import time

#time.sleep(2)

print("Done")


#Performance Timer
import time

start = time.time()

for i in range(100000):
    pass

end = time.time()

print(end-start)


#OS Name
import os

print(os.name)


#Current Working Directory
import os

print(os.getcwd())


#List Directory
import os

print(os.listdir())


#Environment Variables
import os

print(os.environ)


#System Platform
import sys

print(sys.platform)


#Python Version
import sys

print(sys.version)


#Command Line Arguments
import sys

print(sys.argv)


#Exit Program
import sys

#sys.exit()


#Platform Information
import platform

print(platform.system())
print(platform.release())


#Machine Information
import platform

print(platform.machine())


#Processor
import platform

print(platform.processor())


#Calendar
import calendar

print(calendar.month(2026,7))


#Leap Year
import calendar

print(calendar.isleap(2024))


#Counter
from collections import Counter

text = "banana"

print(Counter(text))


#Default Dictionary
from collections import defaultdict

numbers = defaultdict(int)

numbers["a"] += 1

print(numbers)


#Deque
from collections import deque

queue = deque([1,2,3])

queue.append(4)

queue.appendleft(0)

print(queue)


#Named Tuple
from collections import namedtuple

Student = namedtuple("Student",["name","age"])

student = Student("Oscar",23)

print(student)


#Chain
from itertools import chain

print(list(chain([1,2],[3,4])))


#Count Iterator
from itertools import count

counter = count(1)

print(next(counter))
print(next(counter))


#Cycle Iterator
from itertools import cycle

letters = cycle("AB")

print(next(letters))
print(next(letters))
print(next(letters))


#Accumulate
from itertools import accumulate

print(list(accumulate([1,2,3,4])))


#Product
from itertools import product

print(list(product([1,2],["A","B"])))


#Reduce
from functools import reduce

print(reduce(lambda x,y:x+y,[1,2,3,4]))


#Partial
from functools import partial

def power(a,b):
    return a**b

square = partial(power,b=2)

print(square(5))


#Item Getter
from operator import itemgetter

students = [
    ("Oscar",23),
    ("Alex",21)
]

print(sorted(students,key=itemgetter(1)))


#String Constants
import string

print(string.ascii_lowercase)
print(string.digits)


#Keywords
import keyword

print(keyword.kwlist)


#Regular Expression
import re

text = "Python 123"

print(re.findall(r"\d+",text))


#Substitute
import re

text = "Python123"

print(re.sub(r"\d+","",text))


#Split
import re

text = "apple,banana;orange"

print(re.split("[,;]",text))


#Decimal
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))


#Fraction
from fractions import Fraction

print(Fraction(1,3) + Fraction(1,6))


#UUID
import uuid

print(uuid.uuid4())


#MD5 Hash
import hashlib

text = "Python"

print(hashlib.md5(text.encode()).hexdigest())


#SHA256 Hash
import hashlib

text = "Python"

print(hashlib.sha256(text.encode()).hexdigest())


#JSON Encode
import json

student = {
    "name":"Oscar",
    "age":23
}

print(json.dumps(student))


#JSON Decode
import json

text = '{"name":"Oscar","age":23}'

print(json.loads(text))


#CSV Write
import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Age"])


#CSV Read
import csv

with open("students.csv") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


#Pickle Save
import pickle

numbers = [1,2,3]

with open("numbers.pkl","wb") as file:
    pickle.dump(numbers,file)


#Pickle Load
import pickle

with open("numbers.pkl","rb") as file:
    print(pickle.load(file))


#Path Object
from pathlib import Path

path = Path("test.txt")

print(path.exists())


#Glob Files
from pathlib import Path

for file in Path(".").glob("*.py"):
    print(file)