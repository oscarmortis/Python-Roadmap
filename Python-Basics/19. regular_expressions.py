# ==========================================
# REGULAR EXPRESSIONS (re MODULE)
# ==========================================


import re



#Simple Search

text = "Python is powerful"

result = re.search(
    "Python",
    text
)

print(result)



#Search Result Position

text = "Python is powerful"

result = re.search(
    "Python",
    text
)

print(result.start())
print(result.end())



#Search Group

text = "Python is powerful"

result = re.search(
    "Python",
    text
)

print(result.group())



#Search Without Match

text = "Java is powerful"

result = re.search(
    "Python",
    text
)

print(result)



#Match Function
#Checks only beginning

text = "Python language"

result = re.match(
    "Python",
    text
)

print(result)



#Match Failure

text = "I love Python"

result = re.match(
    "Python",
    text
)

print(result)



#Findall

text = "Python Java Python C++"

result = re.findall(
    "Python",
    text
)

print(result)



#Finditer

text = "Python Java Python"

result = re.finditer(
    "Python",
    text
)


for item in result:

    print(item.group())
    print(item.start())



#Replace Using sub()

text = "I love Java"

result = re.sub(
    "Java",
    "Python",
    text
)

print(result)



#Replace Multiple

text = "cat dog cat"

result = re.sub(
    "cat",
    "bird",
    text
)

print(result)



#Split Using Regex

text = "apple,banana;orange"

result = re.split(
    "[,;]",
    text
)

print(result)



#Raw String

text = r"\n"

print(text)



# ==========================================
# SPECIAL CHARACTERS
# ==========================================



#Dot (.)
#Any Character Except New Line

text = "cat cot cut"

result = re.findall(
    "c.t",
    text
)

print(result)



#Caret (^)
#Starts With

text = "Python is great"

result = re.findall(
    "^Python",
    text
)

print(result)



#Dollar ($)
#Ends With

text = "I love Python"

result = re.findall(
    "Python$",
    text
)

print(result)



#Star (*)
#Zero or More

text = "color colour colouur"

result = re.findall(
    "colou*r",
    text
)

print(result)



#Plus (+)
#One or More

text = "go goo gooo"

result = re.findall(
    "go+",
    text
)

print(result)



#Question Mark (?)
#Zero or One

text = "color colour"

result = re.findall(
    "colou?r",
    text
)

print(result)



#Curly Braces {}

text = "aaa aa a"

result = re.findall(
    "a{2}",
    text
)

print(result)



#Range

text = "a aa aaa aaaa"

result = re.findall(
    "a{2,3}",
    text
)

print(result)



#Exactly Range

text = "123 12 12345"

result = re.findall(
    "\d{3}",
    text
)

print(result)



# ==========================================
# CHARACTER CLASSES
# ==========================================



#Digits \d

text = "My age is 23"

result = re.findall(
    "\d",
    text
)

print(result)



#All Digits Together

text = "Phone 9876543210"

result = re.findall(
    "\d+",
    text
)

print(result)



#Non Digit \D

text = "abc123"

result = re.findall(
    "\D",
    text
)

print(result)



#Word Character \w

text = "Python_123"

result = re.findall(
    "\w",
    text
)

print(result)



#Non Word Character \W

text = "Python@123"

result = re.findall(
    "\W",
    text
)

print(result)



#Whitespace \s

text = "Hello World"

result = re.findall(
    "\s",
    text
)

print(result)



#Non Whitespace \S

text = "Hello World"

result = re.findall(
    "\S",
    text
)

print(result)



#Any Character Class []

text = "apple bat cat"

result = re.findall(
    "[abc]",
    text
)

print(result)



#Range Inside []

text = "abc123XYZ"

result = re.findall(
    "[a-z]",
    text
)

print(result)



#Uppercase Range

text = "abcXYZ"

result = re.findall(
    "[A-Z]",
    text
)

print(result)



#Numbers Range

text = "123 abc 456"

result = re.findall(
    "[0-9]",
    text
)

print(result)



#Multiple Ranges

text = "abc123XYZ"

result = re.findall(
    "[a-zA-Z0-9]",
    text
)

print(result)

# ==========================================
# GROUPS IN REGULAR EXPRESSIONS
# ==========================================


import re



#Basic Group

text = "My phone number is 9876543210"

result = re.search(
    "(\d+)",
    text
)

print(result.group())



#Access Group

text = "Name: Oscar Age: 23"

result = re.search(
    "Name: (\w+) Age: (\d+)",
    text
)


print(result.group(1))
print(result.group(2))



#All Groups

text = "Name: Oscar Age: 23"

result = re.search(
    "Name: (\w+) Age: (\d+)",
    text
)

print(result.groups())



#Multiple Capturing Groups

text = "2026-07-20"

result = re.search(
    "(\d{4})-(\d{2})-(\d{2})",
    text
)

print(result.group(1))
print(result.group(2))
print(result.group(3))



#Non Capturing Group

text = "cat dog"

result = re.findall(
    "(?:cat|dog)",
    text
)

print(result)



#OR Operator |

text = "Python Java C++"

result = re.findall(
    "Python|Java",
    text
)

print(result)



#OR With Groups

text = "cat dog bird"

result = re.findall(
    "(cat|dog)",
    text
)

print(result)



#Named Groups

text = "Name: Oscar Age:23"


result = re.search(
    "Name: (?P<name>\w+) Age:(?P<age>\d+)",
    text
)


print(result.group("name"))
print(result.group("age"))



#Group Dictionary

text = "Name: Oscar Age:23"


result = re.search(
    "Name: (?P<name>\w+) Age:(?P<age>\d+)",
    text
)


print(result.groupdict())



# ==========================================
# GREEDY AND NON GREEDY MATCHING
# ==========================================



#Greedy *

text = "<h1>Hello</h1>"

result = re.findall(
    "<.*>",
    text
)

print(result)



#Non Greedy *

text = "<h1>Hello</h1>"

result = re.findall(
    "<.*?>",
    text
)

print(result)



#Greedy +

text = "aaaa"

result = re.findall(
    "a+",
    text
)

print(result)



#Non Greedy +

text = "aaaa"

result = re.findall(
    "a+?",
    text
)

print(result)



#Greedy {}

text = "123456"

result = re.findall(
    "\d{2,}",
    text
)

print(result)



#Non Greedy {}

text = "123456"

result = re.findall(
    "\d{2,}?",
    text
)

print(result)



# ==========================================
# FLAGS
# ==========================================



#IGNORECASE

text = "Python PYTHON python"


result = re.findall(
    "python",
    text,
    re.IGNORECASE
)

print(result)



#MULTILINE

text = """
Python
Java
Python
"""


result = re.findall(
    "^Python",
    text,
    re.MULTILINE
)

print(result)



#DOTALL

text = """
Hello
World
"""


result = re.findall(
    "Hello.*World",
    text,
    re.DOTALL
)

print(result)



#VERBOSE

pattern = re.compile(
    r"""
    \d+
    -
    \w+
    """,
    re.VERBOSE
)


text = "123-python"

print(
    pattern.findall(text)
)



#Compile Pattern

pattern = re.compile(
    r"\d+"
)

text = "Age 23"

print(
    pattern.findall(text)
)



#Compiled Search

pattern = re.compile(
    "Python"
)

text = "I love Python"

result = pattern.search(text)

print(result.group())



# ==========================================
# LOOKAHEAD
# ==========================================



#Positive Lookahead

text = "Python3 Java8"


result = re.findall(
    "\w+(?=\d)",
    text
)

print(result)



#Negative Lookahead

text = "Python Java"


result = re.findall(
    "\w+(?!\d)",
    text
)

print(result)



#Positive Lookbehind

text = "$100 $200"


result = re.findall(
    "(?<=\$)\d+",
    text
)

print(result)



#Negative Lookbehind

text = "100 200"


result = re.findall(
    "(?<!\$)\d+",
    text
)

print(result)



# ==========================================
# PRACTICAL VALIDATIONS
# ==========================================



#Check Username

username = "Oscar_123"


pattern = r"^[a-zA-Z0-9_]+$"


print(
    bool(
        re.match(pattern,username)
    )
)



#Validate Phone Number

phone = "9876543210"


pattern = r"^\d{10}$"


print(
    bool(
        re.match(pattern,phone)
    )
)



#Validate PIN Code

pin = "492001"


pattern = r"^\d{6}$"


print(
    bool(
        re.match(pattern,pin)
    )
)



#Validate Date

date = "20-07-2026"


pattern = r"^\d{2}-\d{2}-\d{4}$"


print(
    bool(
        re.match(pattern,date)
    )
)



#Extract Numbers

text = "Price is 500 dollars"


numbers = re.findall(
    "\d+",
    text
)

print(numbers)



#Extract Emails

text = """
Contact:
abc@gmail.com
test@yahoo.com
"""


emails = re.findall(
    r"\w+@\w+\.\w+",
    text
)


print(emails)

# ==========================================
# ADVANCED REGULAR EXPRESSIONS
# ==========================================


import re



# ==========================================
# EMAIL VALIDATION
# ==========================================


email = "oscar123@gmail.com"


pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


result = re.match(
    pattern,
    email
)


print(bool(result))



#Extract Multiple Emails

text = """
Emails:
oscar@gmail.com
alex@yahoo.com
test123@company.org
"""


pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


print(
    re.findall(pattern,text)
)



# ==========================================
# URL VALIDATION
# ==========================================


url = "https://www.google.com"


pattern = r"https?://(www\.)?\w+\.\w+"


print(
    bool(
        re.match(pattern,url)
    )
)



#Extract URLs

text = """
Visit:
https://google.com
https://github.com
"""


pattern = r"https?://[^\s]+"


print(
    re.findall(pattern,text)
)



# ==========================================
# PASSWORD VALIDATION
# ==========================================


password = "Oscar@123"


pattern = r"""
^
(?=.*[A-Z])
(?=.*[a-z])
(?=.*\d)
(?=.*[@#$%^&+=])
.{8,}
$
"""


result = re.match(
    pattern,
    password,
    re.VERBOSE
)


print(bool(result))



# ==========================================
# IP ADDRESS VALIDATION
# ==========================================


ip = "192.168.1.1"


pattern = r"""
^
(
25[0-5]|
2[0-4][0-9]|
[01]?[0-9][0-9]?
)
\.
(
25[0-5]|
2[0-4][0-9]|
[01]?[0-9][0-9]?
)
\.
(
25[0-5]|
2[0-4][0-9]|
[01]?[0-9][0-9]?
)
\.
(
25[0-5]|
2[0-4][0-9]|
[01]?[0-9][0-9]?
)
$
"""


print(
    bool(
        re.match(
            pattern,
            ip,
            re.VERBOSE
        )
    )
)



# ==========================================
# CREDIT CARD PATTERN
# ==========================================


card = "1234-5678-9012-3456"


pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}$"


print(
    bool(
        re.match(pattern,card)
    )
)



# ==========================================
# PHONE NUMBER EXTRACTION
# ==========================================


text = """
Call:
9876543210
+91-9876543210
"""


pattern = r"\+?\d{2}[- ]?\d{10}|\d{10}"


print(
    re.findall(pattern,text)
)



# ==========================================
# DATE EXTRACTION
# ==========================================


text = """
Dates:
20-07-2026
01-01-2025
"""


pattern = r"\d{2}-\d{2}-\d{4}"


print(
    re.findall(pattern,text)
)



# ==========================================
# TIME EXTRACTION
# ==========================================


text = """
Meeting at 10:30 AM
Lunch at 2:45 PM
"""


pattern = r"\d{1,2}:\d{2}\s?(AM|PM)"


print(
    re.findall(pattern,text)
)



# ==========================================
# REMOVE EXTRA SPACES
# ==========================================


text = "Python     is      powerful"


result = re.sub(
    r"\s+",
    " ",
    text
)


print(result)



# ==========================================
# REMOVE SPECIAL CHARACTERS
# ==========================================


text = "Hello@#$ Python!!!"


result = re.sub(
    r"[^a-zA-Z0-9 ]",
    "",
    text
)


print(result)



# ==========================================
# EXTRACT HASHTAGS
# ==========================================


text = """
Learning #Python
Building #AI
"""


hashtags = re.findall(
    r"#\w+",
    text
)


print(hashtags)



# ==========================================
# EXTRACT MENTIONS
# ==========================================


text = """
Hello @Oscar
"""


mentions = re.findall(
    r"@\w+",
    text
)


print(mentions)



# ==========================================
# WORD FREQUENCY CLEANING
# ==========================================


text = """
Python, Python!
Python.
Java.
"""


clean = re.sub(
    r"[^a-zA-Z ]",
    "",
    text
)


words = clean.split()


print(words)



# ==========================================
# SPLIT CAMEL CASE
# ==========================================


text = "RegularExpression"


result = re.sub(
    r"([a-z])([A-Z])",
    r"\1 \2",
    text
)


print(result)



# ==========================================
# PASSWORD MASKING
# ==========================================


text = "Password=secret123"


result = re.sub(
    r"Password=\w+",
    "Password=******",
    text
)


print(result)



# ==========================================
# LOG FILE PARSING
# ==========================================


log = """
ERROR 2026-07-20 Database Failed
INFO 2026-07-20 Server Started
"""


pattern = r"(ERROR|INFO)\s(\d{4}-\d{2}-\d{2})"


print(
    re.findall(pattern,log)
)



# ==========================================
# HTML TAG REMOVAL
# ==========================================


html = "<h1>Hello</h1>"


text = re.sub(
    r"<.*?>",
    "",
    html
)


print(text)



# ==========================================
# HTML TAG EXTRACTION
# ==========================================


html = """
<h1>Hello</h1>
<p>Python</p>
"""


tags = re.findall(
    r"<(.*?)>",
    html
)


print(tags)



# ==========================================
# SENTENCE SPLITTER
# ==========================================


text = """
Hello world.
Python is great.
Regex is powerful.
"""


sentences = re.split(
    r"\.",
    text
)


print(sentences)



# ==========================================
# WORD SEARCH IGNORING CASE
# ==========================================


text = "Python python PYTHON"


result = re.findall(
    "python",
    text,
    re.IGNORECASE
)


print(result)



# ==========================================
# COMPILED VALIDATOR
# ==========================================


phone_pattern = re.compile(
    r"^\d{10}$"
)


print(
    bool(
        phone_pattern.match("9876543210")
    )
)



# ==========================================
# REGEX DEBUGGING
# ==========================================


pattern = re.compile(
    r"\d+",
    re.DEBUG
)