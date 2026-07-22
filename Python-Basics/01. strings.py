#Create String
message = "Hello World"
print(message)


#Single Quotes
message = 'Hello World'
print(message)


#Double Quotes
message = "Hello World"
print(message)


#Triple Quotes (Multiline String)
message = """Hello
World
Python"""
print(message)


#String with Quotes Inside
message = "I'm learning Python"
print(message)

message = 'He said "Hello"'
print(message)


#Escape Characters
print("I'm learning Python")
print('I\'m learning Python')
print("He said \"Hello\"")
print("C:\\Users\\Oscar")
print("Hello\nWorld")
print("Hello\tWorld")


#Raw String (Ignores Escape Characters)
path = r"C:\Users\Oscar\Desktop"
print(path)


#Type of String
message = "Gravity"
print(type(message))


#String Length
message = "Gravity Works"
print(len(message))


#Access First Character
message = "Gravity"
print(message[0])


#Access Last Character
message = "Gravity"
print(message[-1])


#Negative Indexing
message = "Gravity"
print(message[-2])
print(message[-3])


#String Slicing
message = "GravityWorks"
print(message[0:7])


#Slice From Beginning
message = "GravityWorks"
print(message[:7])


#Slice To End
message = "GravityWorks"
print(message[7:])


#Copy Entire String
message = "GravityWorks"
print(message[:])


#Every Second Character
message = "GravityWorks"
print(message[::2])


#Every Third Character
message = "GravityWorks"
print(message[::3])


#Reverse String
message = "GravityWorks"
print(message[::-1])


#Reverse Every Second Character
message = "GravityWorks"
print(message[::-2])


#Slice Using Negative Indexes
message = "GravityWorks"
print(message[-5:])
print(message[:-5])


#Strings are Immutable
message = "Gravity"
#message[0] = "g"      #Error
#print(message)


#Concatenate Strings
first = "Gravity"
second = "Works"

print(first + second)
print(first + " " + second)


#Repeat String
print("Hi " * 3)
print("=" * 40)


#Membership Operator
message = "Gravity Works"

print("Gravity" in message)
print("Python" in message)
print("Python" not in message)


#Compare Strings
print("apple" == "apple")
print("apple" != "banana")
print("apple" < "banana")
print("zebra" > "apple")
print("ABC" == "abc")


#ASCII Comparison
print("A" < "a")
print(ord("A"))
print(ord("a"))


#Minimum Character
message = "gravity"
print(min(message))


#Maximum Character
message = "gravity"
print(max(message))


#Sort Characters
message = "gravity"
print(sorted(message))


#Reverse Iterator
message = "Python"
print(list(reversed(message)))


#Convert String to List
message = "Python"
print(list(message))


#Convert String to Tuple
message = "Python"
print(tuple(message))


#Convert String to Set
message = "banana"
print(set(message))


#Enumerate String
message = "Python"

for item in enumerate(message):
    print(item)


#Better Enumerate
message = "Python"

for index, letter in enumerate(message):
    print(index, letter)


#Start Enumerate at 1
message = "Python"

for index, letter in enumerate(message, start=1):
    print(index, letter)


#Loop Through String
message = "Python"

for letter in message:
    print(letter)


#Loop Using Index
message = "Python"

for index in range(len(message)):
    print(message[index])


#Count Characters Using len()
message = "Gravity Works"
print(len(message))


#Unicode Character
print(chr(65))
print(chr(97))
print(chr(9731))


#Unicode Value
print(ord("A"))
print(ord("a"))
print(ord("☃"))


#ASCII Representation
print(ascii("Hello"))
print(ascii("नमस्ते"))


#Official Representation
message = "Gravity\nWorks"
print(repr(message))


#Binary of Character
print(bin(ord("A")))


#Hexadecimal of Character
print(hex(ord("A")))


#Octal of Character
print(oct(ord("A")))


#Uppercase
message = "gravity works"
print(message.upper())


#Lowercase
message = "GRAVITY WORKS"
print(message.lower())


#Capitalize First Letter
message = "gravity works"
print(message.capitalize())


#Title Case
message = "gravity works ai"
print(message.title())


#Swap Uppercase and Lowercase
message = "GrAvItY WoRkS"
print(message.swapcase())


#Casefold (Better Lowercase)
message = "Straße"
print(message.casefold())


#Center String
message = "Gravity"
print(message.center(20))


#Center with Fill Character
message = "Gravity"
print(message.center(20, "-"))


#Left Justify
message = "Gravity"
print(message.ljust(20))
print(message.ljust(20, "-"))


#Right Justify
message = "Gravity"
print(message.rjust(20))
print(message.rjust(20, "-"))


#Fill String with Leading Zeros
number = "25"
print(number.zfill(5))


#Check Memory Address
message = "Gravity"
print(id(message))


#Changing String Creates New Object
message = "Gravity"
print(id(message))

message = message.upper()
print(id(message))

#Find First Occurrence
message = "Hello World"
print(message.find("World"))


#Find Character
message = "banana"
print(message.find("a"))


#Find From Specific Index
message = "banana"
print(message.find("a", 2))


#Returns -1 if Not Found
message = "Hello"
print(message.find("Python"))


#Find Last Occurrence
message = "banana"
print(message.rfind("a"))


#Index Method
message = "Hello World"
print(message.index("World"))


#Index Character
message = "banana"
print(message.index("a"))


#Index Raises Error if Not Found
message = "Hello"
#print(message.index("Python"))


#Last Index
message = "banana"
print(message.rindex("a"))


#Count Occurrences
message = "banana"
print(message.count("a"))


#Count Substring
message = "hello hello hello"
print(message.count("hello"))


#Replace Word
message = "Hello World"
print(message.replace("World", "Python"))


#Replace Character
message = "banana"
print(message.replace("a", "@"))


#Replace Limited Times
message = "banana"
print(message.replace("a", "@", 2))


#Remove Prefix
message = "Mr.Oscar"
print(message.removeprefix("Mr."))


#Remove Suffix
message = "photo.png"
print(message.removesuffix(".png"))


#Remove Spaces
message = "    Hello World    "
print(message.strip())


#Remove Left Spaces
message = "    Hello"
print(message.lstrip())


#Remove Right Spaces
message = "Hello    "
print(message.rstrip())


#Strip Specific Characters
message = "****Hello****"
print(message.strip("*"))


#Strip Multiple Characters
message = "##@@Hello@@##"
print(message.strip("#@"))


#Startswith
message = "Gravity Works"
print(message.startswith("Gravity"))


#Startswith False
message = "Gravity Works"
print(message.startswith("Python"))


#Endswith
message = "Gravity Works"
print(message.endswith("Works"))


#Endswith False
message = "Gravity Works"
print(message.endswith("Python"))


#Split by Spaces
message = "Python Java C++"
print(message.split())


#Split by Comma
message = "Apple,Banana,Mango"
print(message.split(","))


#Split Only Once
message = "one,two,three,four"
print(message.split(",", 1))


#Split From Right
message = "one,two,three,four"
print(message.rsplit(",", 1))


#Split Lines
message = "Hello\nWorld\nPython"
print(message.splitlines())


#Join List into String
words = ["Gravity", "Works", "AI"]
print(" ".join(words))


#Join with Dash
words = ["2026", "07", "20"]
print("-".join(words))


#Join Without Space
letters = ['P', 'Y', 'T', 'H', 'O', 'N']
print("".join(letters))


#Partition String
message = "Python is Awesome"
print(message.partition("is"))


#Partition if Not Found
message = "Python"
print(message.partition("Java"))


#Partition From Right
message = "Python is Awesome"
print(message.rpartition("is"))


#Expand Tabs
message = "Python\tJava\tC++"
print(message.expandtabs())


#Expand Tabs with Size
message = "Python\tJava\tC++"
print(message.expandtabs(20))


#Encode String
message = "Python"
print(message.encode())


#Encode UTF-8
message = "नमस्ते"
print(message.encode("utf-8"))


#Translate Characters
table = str.maketrans("aeiou", "12345")
message = "education"
print(message.translate(table))


#Remove Characters Using Translate
table = str.maketrans("", "", "aeiou")
message = "education"
print(message.translate(table))


#Replace Multiple Characters
table = str.maketrans({
    "a":"@",
    "e":"3",
    "i":"1",
    "o":"0",
    "u":"_"
})

message = "education"
print(message.translate(table))


#Format Method
name = "Oscar"
age = 23

print("My name is {}.".format(name))
print("My name is {} and I am {}.".format(name, age))


#Format with Index
print("{1} is {0} years old.".format(23, "Oscar"))


#Format with Keywords
print("Name : {name}, Age : {age}".format(name="Oscar", age=23))


#Format Numbers
price = 99.45678
print("{:.2f}".format(price))


#Thousands Separator
number = 1000000000
print("{:,}".format(number))


#Center Fill
message = "Python"
print("{:*^20}".format(message))


#Left Align
message = "Python"
print("{:<20}".format(message))


#Right Align
message = "Python"
print("{:>20}".format(message))


#Percentage Formatting
value = 0.875
print("{:.2%}".format(value))


#Binary Formatting
number = 20
print("{:b}".format(number))


#Octal Formatting
number = 20
print("{:o}".format(number))


#Hexadecimal Formatting
number = 20
print("{:x}".format(number))


#Uppercase Hex
number = 20
print("{:X}".format(number))

#Returns True if All Characters are Alphabetic
message = "Python"
print(message.isalpha())


#Returns False if Numbers Exist
message = "Python123"
print(message.isalpha())


#Returns True if All Characters are AlphaNumeric
message = "Python123"
print(message.isalnum())


#Returns False if Spaces Exist
message = "Python 123"
print(message.isalnum())


#Returns True if String Contains Only Digits
message = "123456"
print(message.isdigit())


#Returns False if Decimal Exists
message = "123.45"
print(message.isdigit())


#Returns True if String Contains Decimal Numbers
message = "12345"
print(message.isdecimal())


#Returns False for Superscript Numbers
message = "²"
print(message.isdecimal())


#Returns True for Numeric Characters
message = "²"
print(message.isnumeric())


#Returns True for Fractions
message = "½"
print(message.isnumeric())


#Returns True if All Characters are Lowercase
message = "python"
print(message.islower())


#Returns True if All Characters are Uppercase
message = "PYTHON"
print(message.isupper())


#Returns True if Every Word Starts with Capital Letter
message = "Gravity Works Ai"
print(message.istitle())


#Returns False
message = "gravity Works"
print(message.istitle())


#Returns True if String Contains Only Spaces
message = "     "
print(message.isspace())


#Returns False
message = " Hello "
print(message.isspace())


#Returns True if All Characters are Printable
message = "Hello"
print(message.isprintable())


#Returns False
message = "Hello\nWorld"
print(message.isprintable())


#Returns True if Valid Variable Name
message = "gravity"
print(message.isidentifier())


#Returns False
message = "123gravity"
print(message.isidentifier())


#Returns True if All Characters are ASCII
message = "Python"
print(message.isascii())


#Returns False
message = "नमस्ते"
print(message.isascii())


#f-Strings
name = "Oscar"
age = 23

print(f"My name is {name}")
print(f"I am {age} years old.")


#Expressions Inside f-Strings
a = 10
b = 20

print(f"{a} + {b} = {a+b}")


#Mathematical Operations
radius = 7
print(f"Area = {3.14159 * radius ** 2}")


#Formatting Decimal Places
pi = 3.14159265359
print(f"{pi:.2f}")
print(f"{pi:.4f}")


#Thousands Separator
number = 123456789
print(f"{number:,}")


#Percentage
value = 0.8547
print(f"{value:.2%}")


#Binary
number = 15
print(f"{number:b}")


#Octal
number = 15
print(f"{number:o}")


#Hexadecimal
number = 15
print(f"{number:x}")


#Uppercase Hex
number = 15
print(f"{number:X}")


#Center Alignment
word = "Python"
print(f"{word:^20}")


#Left Alignment
word = "Python"
print(f"{word:<20}")


#Right Alignment
word = "Python"
print(f"{word:>20}")


#Fill Character
word = "Python"
print(f"{word:-^20}")


#Old Style Formatting
name = "Oscar"

print("Hello %s" % name)


#Integer Formatting
age = 23
print("Age : %d" % age)


#Float Formatting
pi = 3.1415926
print("%.2f" % pi)


#Multiple Values
name = "Oscar"
age = 23

print("%s is %d years old." % (name, age))


#Convert String to Bytes
message = "Python"
data = bytes(message, "utf-8")
print(data)


#Decode Bytes
data = b'Python'
print(data.decode())


#UTF-8 Encoding
message = "नमस्ते"
data = message.encode("utf-8")
print(data)


#UTF-8 Decoding
message = "नमस्ते"
data = message.encode("utf-8")
print(data.decode("utf-8"))


#Compare Strings
print("apple" == "apple")
print("apple" != "banana")
print("apple" < "banana")
print("apple" > "banana")


#Case Sensitive Comparison
print("Python" == "python")


#Case Insensitive Comparison
print("Python".lower() == "python".lower())


#Sort Strings
names = ["Charlie","Bob","Alice"]
print(sorted(names))


#Reverse Sort
names = ["Charlie","Bob","Alice"]
print(sorted(names, reverse=True))


#Sort Ignoring Case
names = ["banana","Apple","cat"]
print(sorted(names, key=str.lower))


#Maximum Character
print(max("gravity"))


#Minimum Character
print(min("gravity"))


#Sum ASCII Values
text = "ABC"

total = 0

for letter in text:
    total += ord(letter)

print(total)


#Character Frequency
message = "banana"

for letter in set(message):
    print(letter, message.count(letter))


#Remove Spaces
message = "G r a v i t y"

print(message.replace(" ", ""))


#Repeat Characters
print("=" * 50)
print("*" * 10)


#Reverse Using reversed()
message = "Python"

print("".join(reversed(message)))


#Reverse Using Slicing
message = "Python"

print(message[::-1])


#Convert Every Character to Uppercase Using Loop
message = "gravity"

for letter in message:
    print(letter.upper())


#Enumerate Every Character
message = "Python"

for index, letter in enumerate(message):
    print(index, letter)


#Convert Characters to ASCII
message = "ABC"

for letter in message:
    print(letter, ord(letter))


#Convert ASCII Back to Character
numbers = [65,66,67]

for number in numbers:
    print(chr(number))


#Check if Character is Vowel
letter = "a"

print(letter.lower() in "aeiou")


#Check if Character is Consonant
letter = "g"

print(letter.isalpha() and letter.lower() not in "aeiou")


#Count Vowels
message = "Gravity Works"

count = 0

for letter in message.lower():
    if letter in "aeiou":
        count += 1

print(count)


#Count Consonants
message = "Gravity Works"

count = 0

for letter in message.lower():
    if letter.isalpha() and letter not in "aeiou":
        count += 1

print(count)

#Reverse Words
message = "Gravity Works AI"

print(" ".join(message.split()[::-1]))


#Palindrome Check
message = "madam"

print(message == message[::-1])


#Palindrome Ignore Case
message = "Madam"

print(message.lower() == message.lower()[::-1])


#Count Words
message = "Gravity Works AI"

print(len(message.split()))


#Longest Word
message = "Gravity Works Artificial Intelligence"

print(max(message.split(), key=len))


#Shortest Word
message = "Gravity Works Artificial Intelligence"

print(min(message.split(), key=len))


#Remove All Spaces
message = "G r a v i t y"

print(message.replace(" ", ""))


#Remove Duplicate Characters
message = "banana"

result = ""

for letter in message:
    if letter not in result:
        result += letter

print(result)


#Character Frequency
message = "banana"

frequency = {}

for letter in message:
    frequency[letter] = frequency.get(letter, 0) + 1

print(frequency)


#Most Frequent Character
message = "banana"

print(max(set(message), key=message.count))


#Least Frequent Character
message = "banana"

print(min(set(message), key=message.count))


#Word Frequency
message = "python java python c java python"

frequency = {}

for word in message.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


#Remove Digits
message = "Python123AI456"

result = ""

for letter in message:
    if not letter.isdigit():
        result += letter

print(result)


#Keep Only Digits
message = "Python123AI456"

result = ""

for letter in message:
    if letter.isdigit():
        result += letter

print(result)


#Keep Only Letters
message = "Python123AI456"

result = ""

for letter in message:
    if letter.isalpha():
        result += letter

print(result)


#Keep AlphaNumeric
message = "Python@123#AI!"

result = ""

for letter in message:
    if letter.isalnum():
        result += letter

print(result)


#Remove Vowels
message = "Gravity Works"

result = ""

for letter in message:
    if letter.lower() not in "aeiou":
        result += letter

print(result)


#Extract Vowels
message = "Gravity Works"

result = ""

for letter in message:
    if letter.lower() in "aeiou":
        result += letter

print(result)


#Swap First and Last Character
message = "Python"

new = message[-1] + message[1:-1] + message[0]

print(new)


#Capitalize Every Word
message = "gravity works artificial intelligence"

print(" ".join(word.capitalize() for word in message.split()))


#Lower Every Word
message = "Gravity Works AI"

print(" ".join(word.lower() for word in message.split()))


#Upper Every Word
message = "Gravity Works AI"

print(" ".join(word.upper() for word in message.split()))


#Snake Case
message = "Gravity Works AI"

print(message.lower().replace(" ", "_"))


#Kebab Case
message = "Gravity Works AI"

print(message.lower().replace(" ", "-"))


#Camel Case
message = "gravity works ai"

words = message.split()

camel = words[0] + "".join(word.capitalize() for word in words[1:])

print(camel)


#Pascal Case
message = "gravity works ai"

print("".join(word.capitalize() for word in message.split()))


#Title Case
message = "gravity works ai"

print(message.title())


#Check Anagram
a = "listen"
b = "silent"

print(sorted(a) == sorted(b))


#Sort Characters
message = "python"

print("".join(sorted(message)))


#Random String Comparison
a = "abc"
b = "abd"

print(a < b)


#Mirror String
message = "Python"

print(message + message[::-1])


#Duplicate Every Character
message = "Python"

print("".join(letter * 2 for letter in message))


#Remove Consecutive Duplicate Characters
message = "aaabbbccdd"

result = message[0]

for letter in message[1:]:
    if letter != result[-1]:
        result += letter

print(result)


#First Non-Repeating Character
message = "swiss"

for letter in message:
    if message.count(letter) == 1:
        print(letter)
        break


#First Repeating Character
message = "swiss"

seen = set()

for letter in message:
    if letter in seen:
        print(letter)
        break
    seen.add(letter)


#Mask Email
email = "gravityworks@gmail.com"

name, domain = email.split("@")

print(name[:2] + "*" * (len(name)-2) + "@" + domain)


#Mask Phone Number
phone = "9876543210"

print("*" * 6 + phone[-4:])


#Check Email
email = "test@gmail.com"

print("@" in email and "." in email)


#Check URL
url = "https://gravityworks.ai"

print(url.startswith("http"))


#Extract File Extension
filename = "python.pdf"

print(filename.split(".")[-1])


#Remove File Extension
filename = "python.pdf"

print(filename.rsplit(".",1)[0])


#Initials
name = "Gravity Works Artificial Intelligence"

print("".join(word[0] for word in name.split()))


#Abbreviation
sentence = "World Health Organization"

print("".join(word[0].upper() for word in sentence.split()))


#Count Uppercase Letters
message = "GravityWorksAI"

count = 0

for letter in message:
    if letter.isupper():
        count += 1

print(count)


#Count Lowercase Letters
message = "GravityWorksAI"

count = 0

for letter in message:
    if letter.islower():
        count += 1

print(count)


#Alternate Upper Lower
message = "gravity"

result = ""

for i, letter in enumerate(message):
    if i % 2 == 0:
        result += letter.upper()
    else:
        result += letter.lower()

print(result)


#Check Empty String
message = ""

print(message == "")
print(not message)


#String Compression
message = "aaabbcccc"

result = ""

count = 1

for i in range(len(message)-1):
    if message[i] == message[i+1]:
        count += 1
    else:
        result += message[i] + str(count)
        count = 1

result += message[-1] + str(count)

print(result)


#Reverse Each Word
message = "Gravity Works AI"

print(" ".join(word[::-1] for word in message.split()))


#Print ASCII of Every Character
message = "Python"

for letter in message:
    print(letter, ord(letter))


#Print Unicode Character from Numbers
numbers = [9731, 9733, 9829]

for number in numbers:
    print(chr(number))


#Check if String Contains Only English Letters
message = "Python"

print(all(letter.isalpha() and letter.isascii() for letter in message))


#Find Common Characters
a = "gravity"
b = "artificial"

print(set(a) & set(b))


#Unique Characters
message = "banana"

print(set(message))


#Print Every Prefix
message = "Python"

for i in range(1, len(message)+1):
    print(message[:i])


#Print Every Suffix
message = "Python"

for i in range(len(message)):
    print(message[i:])


#Print Every Substring
message = "Python"

for i in range(len(message)):
    for j in range(i+1, len(message)+1):
        print(message[i:j])