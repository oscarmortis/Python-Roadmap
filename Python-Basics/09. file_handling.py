#Open File (Read Mode)
file = open("test.txt", "r")

print(file)


#Read Entire File
file = open("test.txt", "r")

print(file.read())

file.close()


#Read First 10 Characters
file = open("test.txt", "r")

print(file.read(10))

file.close()


#Read One Line
file = open("test.txt", "r")

print(file.readline())

file.close()


#Read All Lines
file = open("test.txt", "r")

print(file.readlines())

file.close()


#Loop Through File
file = open("test.txt", "r")

for line in file:
    print(line.strip())

file.close()


#Close File
file = open("test.txt", "r")

file.close()

print(file.closed)


#Write Mode
file = open("test.txt", "w")

file.write("Hello Python")

file.close()


#Write Multiple Lines
file = open("test.txt", "w")

file.writelines([
    "First Line\n",
    "Second Line\n",
    "Third Line\n"
])

file.close()


#Append Mode
file = open("test.txt", "a")

file.write("\nNew Line")

file.close()


#Read and Write Mode
file = open("test.txt", "r+")

print(file.read())

file.close()


#Write and Read Mode
file = open("test.txt", "w+")

file.write("Python")

file.seek(0)

print(file.read())

file.close()


#Append and Read Mode
file = open("test.txt", "a+")

file.write("\nAppend")

file.seek(0)

print(file.read())

file.close()


#Create File if Not Exists
file = open("newfile.txt", "a")

file.close()


#Exclusive Creation
#Raises FileExistsError if file already exists
file = open("unique.txt", "x")

file.close()


#File Exists Check
import os

print(os.path.exists("test.txt"))


#File Name
file = open("test.txt", "r")

print(file.name)

file.close()


#File Mode
file = open("test.txt", "r")

print(file.mode)

file.close()


#File Readable
file = open("test.txt", "r")

print(file.readable())

file.close()


#File Writable
file = open("test.txt", "a")

print(file.writable())

file.close()


#Current Position
file = open("test.txt", "r")

print(file.tell())

file.close()


#Move Cursor
file = open("test.txt", "r")

file.seek(5)

print(file.tell())

file.close()


#Read After seek()
file = open("test.txt", "r")

file.seek(5)

print(file.read())

file.close()


#Flush File
file = open("test.txt", "a")

file.write("Hello")

file.flush()

file.close()


#Overwrite File
file = open("test.txt", "w")

file.write("New Content")

file.close()


#Binary Write
file = open("image.bin", "wb")

file.write(b"Python")

file.close()


#Binary Read
file = open("image.bin", "rb")

print(file.read())

file.close()


#UTF-8 Encoding
file = open("test.txt", "r", encoding="utf-8")

print(file.read())

file.close()


#ASCII Encoding
file = open("test.txt", "r", encoding="ascii", errors="ignore")

print(file.read())

file.close()


#Ignore Encoding Errors
file = open(
    "test.txt",
    "r",
    encoding="utf-8",
    errors="ignore"
)

print(file.read())

file.close()


#Replace Encoding Errors
file = open(
    "test.txt",
    "r",
    encoding="ascii",
    errors="replace"
)

print(file.read())

file.close()


#Check File Closed
file = open("test.txt", "r")

print(file.closed)

file.close()

print(file.closed)


#Read Character by Character
file = open("test.txt", "r")

while True:

    char = file.read(1)

    if not char:
        break

    print(char)

file.close()


#Read Line by Line
file = open("test.txt", "r")

while True:

    line = file.readline()

    if not line:
        break

    print(line.strip())

file.close()


#Write Numbers
file = open("numbers.txt", "w")

for i in range(1,6):
    file.write(f"{i}\n")

file.close()


#Copy File
source = open("test.txt", "r")
destination = open("copy.txt", "w")

destination.write(source.read())

source.close()
destination.close()


#Count Lines
file = open("test.txt", "r")

count = 0

for line in file:
    count += 1

print(count)

file.close()


#Count Characters
file = open("test.txt", "r")

text = file.read()

print(len(text))

file.close()


#Count Words
file = open("test.txt", "r")

text = file.read()

print(len(text.split()))

file.close()

#with Statement
with open("test.txt", "r") as file:
    print(file.read())


#Write using with
with open("test.txt", "w") as file:
    file.write("Hello Python")


#Append using with
with open("test.txt", "a") as file:
    file.write("\nNew Line")


#Read Line by Line using with
with open("test.txt") as file:

    for line in file:
        print(line.strip())


#Read File into List
with open("test.txt") as file:
    lines = file.readlines()

print(lines)


#Path Exists
from pathlib import Path

path = Path("test.txt")

print(path.exists())


#Is File
from pathlib import Path

path = Path("test.txt")

print(path.is_file())


#Is Directory
from pathlib import Path

path = Path("Documents")

print(path.is_dir())


#Create Directory
from pathlib import Path

Path("NewFolder").mkdir(exist_ok=True)


#Create Nested Directories
from pathlib import Path

Path("Folder1/Folder2").mkdir(parents=True, exist_ok=True)


#Remove Empty Directory
from pathlib import Path

Path("NewFolder").rmdir()


#Rename File
from pathlib import Path

Path("test.txt").rename("notes.txt")


#Rename Back
from pathlib import Path

Path("notes.txt").rename("test.txt")


#Delete File
from pathlib import Path

#Path("temp.txt").unlink()


#File Size
from pathlib import Path

path = Path("test.txt")

print(path.stat().st_size)


#Absolute Path
from pathlib import Path

path = Path("test.txt")

print(path.resolve())


#Current Working Directory
import os

print(os.getcwd())


#Change Working Directory
import os

#os.chdir("C:/Users")


#List Files
import os

print(os.listdir())


#List Files using pathlib
from pathlib import Path

for item in Path(".").iterdir():
    print(item)


#Find txt Files
from pathlib import Path

for file in Path(".").glob("*.txt"):
    print(file)


#Find Python Files Recursively
from pathlib import Path

for file in Path(".").rglob("*.py"):
    print(file)


#JSON Write
import json

student = {
    "name":"Oscar",
    "age":23
}

with open("student.json","w") as file:
    json.dump(student,file)


#JSON Read
import json

with open("student.json") as file:
    data = json.load(file)

print(data)


#JSON String
import json

student = {
    "name":"Oscar",
    "age":23
}

text = json.dumps(student)

print(text)


#JSON from String
import json

text = '{"name":"Oscar","age":23}'

print(json.loads(text))


#Pretty JSON
import json

student = {
    "name":"Oscar",
    "age":23
}

print(json.dumps(student, indent=4))


#CSV Write
import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name","Age"])
    writer.writerow(["Oscar",23])


#CSV Read
import csv

with open("students.csv") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


#CSV Dictionary Writer
import csv

with open("students.csv","w",newline="") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["Name","Age"]
    )

    writer.writeheader()

    writer.writerow({
        "Name":"Oscar",
        "Age":23
    })


#CSV Dictionary Reader
import csv

with open("students.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row)


#Pickle Save
import pickle

numbers = [1,2,3,4]

with open("numbers.pkl","wb") as file:
    pickle.dump(numbers,file)


#Pickle Load
import pickle

with open("numbers.pkl","rb") as file:
    data = pickle.load(file)

print(data)


#Temporary File
import tempfile

with tempfile.TemporaryFile(mode="w+") as file:

    file.write("Python")

    file.seek(0)

    print(file.read())


#Named Temporary File
import tempfile

with tempfile.NamedTemporaryFile(delete=True) as file:
    print(file.name)


#Read Large File
with open("test.txt") as file:

    for line in file:
        print(line.strip())


#Read Chunks
with open("test.txt") as file:

    while True:

        chunk = file.read(10)

        if not chunk:
            break

        print(chunk)


#Copy Binary File
with open("image.jpg","rb") as source:

    with open("copy.jpg","wb") as destination:

        destination.write(source.read())


#Search Word
word = "Python"

with open("test.txt") as file:

    for line in file:

        if word in line:
            print(line.strip())


#Replace Word
with open("test.txt") as file:
    text = file.read()

text = text.replace("Python","Java")

with open("test.txt","w") as file:
    file.write(text)


#Count Word Frequency
from collections import Counter

with open("test.txt") as file:
    words = file.read().split()

print(Counter(words))


#Merge Two Files
with open("a.txt") as a:

    with open("b.txt") as b:

        with open("merged.txt","w") as output:

            output.write(a.read())
            output.write("\n")
            output.write(b.read())


#Read Specific Lines
with open("test.txt") as file:

    for index,line in enumerate(file,start=1):

        if index <= 5:
            print(line.strip())


#Skip Blank Lines
with open("test.txt") as file:

    for line in file:

        if line.strip():
            print(line.strip())


#File Extension
from pathlib import Path

path = Path("report.pdf")

print(path.suffix)


#File Name Only
from pathlib import Path

path = Path("report.pdf")

print(path.stem)


#Parent Directory
from pathlib import Path

path = Path("folder/report.pdf")

print(path.parent)


#Touch File
from pathlib import Path

Path("empty.txt").touch()


#Read Bytes
from pathlib import Path

path = Path("image.jpg")

#print(path.read_bytes())


#Write Text
from pathlib import Path

Path("hello.txt").write_text("Hello Python")


#Read Text
from pathlib import Path

print(Path("hello.txt").read_text())