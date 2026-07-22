# ==========================================
# PATHLIB MODULE
# ==========================================


#Import Path
from pathlib import Path


#Current Directory
path = Path.cwd()

print(path)


#Home Directory
home = Path.home()

print(home)


#Creating Path Object
path = Path("test.txt")

print(path)


#Path Name
path = Path("folder/test.txt")

print(path.name)


#File Extension
path = Path("document.pdf")

print(path.suffix)


#File Stem (Name Without Extension)
path = Path("document.pdf")

print(path.stem)


#Parent Directory
path = Path("folder/test.txt")

print(path.parent)


#Absolute Path
path = Path("test.txt")

print(path.absolute())


#Joining Paths
folder = Path("documents")

file = folder / "notes.txt"

print(file)


#Multiple Path Join
path = Path("folder") / "subfolder" / "file.txt"

print(path)


#Check Exists
path = Path("test.txt")

print(path.exists())


#Check File
path = Path("test.txt")

print(path.is_file())


#Check Directory
path = Path("folder")

print(path.is_dir())


#Create Directory
folder = Path("new_folder")

folder.mkdir()


#Create Nested Directories
folder = Path("main/subfolder/data")

folder.mkdir(
    parents=True,
    exist_ok=True
)


#Remove Directory
#folder.rmdir()


#Rename File
file = Path("old.txt")

#file.rename("new.txt")


#Replace File
file = Path("old.txt")

#file.replace("new.txt")


#File Size
file = Path("test.txt")

if file.exists():
    print(file.stat().st_size)


#File Information
file = Path("test.txt")

if file.exists():

    info = file.stat()

    print(info)


#Iterate Directory
folder = Path(".")

for item in folder.iterdir():

    print(item)


#List Files
folder = Path(".")

for file in folder.iterdir():

    if file.is_file():
        print(file)


#List Folders
folder = Path(".")

for item in folder.iterdir():

    if item.is_dir():
        print(item)


#Glob Search
folder = Path(".")

files = folder.glob("*.py")

for file in files:
    print(file)


#Recursive Glob
folder = Path(".")

files = folder.rglob("*.py")

for file in files:
    print(file)


#Read Text File
file = Path("example.txt")

#content = file.read_text()
#print(content)


#Write Text File
file = Path("example.txt")

#file.write_text("Hello Python")


#Read Lines
file = Path("example.txt")

#if file.exists():
#
#    lines = file.read_text().splitlines()
#
#    print(lines)


#Touch Create File
file = Path("new.txt")

file.touch()


#Change Suffix
file = Path("image.txt")

new = file.with_suffix(".jpg")

print(new)


#Change Name
file = Path("old.txt")

new = file.with_name("new.txt")

print(new)


#Absolute vs Relative
path = Path("test.txt")

print(path)

print(path.resolve())


#Parts of Path
path = Path("folder/file.txt")

print(path.parts)


#Parent Parents
path = Path("a/b/c/file.txt")

print(path.parents)


#Path Comparison
path1 = Path("test.txt")

path2 = Path("test.txt")

print(path1 == path2)


#Path Suffixes
path = Path("archive.tar.gz")

print(path.suffixes)


#File Match
path = Path("hello.py")

print(path.match("*.py"))


#Iterate Parent
path = Path("a/b/c/file.txt")

for parent in path.parents:

    print(parent)

# ==========================================
# ADVANCED PATHLIB
# ==========================================


from pathlib import Path


#Open File Using Path
file = Path("example.txt")

#with file.open("w") as f:
#    f.write("Hello Python")


#Read File Using Open
file = Path("example.txt")

#with file.open("r") as f:
#    print(f.read())


#Append Text
file = Path("example.txt")

#with file.open("a") as f:
#    f.write("\nNew Line")


#Read Bytes
file = Path("image.png")

#if file.exists():
#    data = file.read_bytes()
#    print(data)


#Write Bytes
file = Path("data.bin")

#file.write_bytes(b"Python")


#File Owner
file = Path("example.txt")

#if file.exists():
#    print(file.owner())


#File Group
file = Path("example.txt")

#if file.exists():
#    print(file.group())


#Access Permission
file = Path("example.txt")

if file.exists():

    print(file.stat().st_mode)


#Resolve Symbolic Path
path = Path("../test.txt")

print(path.resolve())


#Relative Path
path = Path("/home/user/project/file.txt")

base = Path("/home/user")

print(path.relative_to(base))


#Same File Check
file1 = Path("test1.txt")
file2 = Path("test2.txt")

#if file1.samefile(file2):
#    print("Same File")


#Create Temporary Path
import tempfile

with tempfile.TemporaryDirectory() as folder:

    path = Path(folder)

    print(path)


#Temporary File
import tempfile

with tempfile.NamedTemporaryFile() as file:

    print(file.name)



# ==========================================
# OS MODULE
# ==========================================


import os


#Current Working Directory

print(os.getcwd())


#Change Directory

#os.chdir("folder")


#List Directory

print(os.listdir())


#List Specific Folder

#print(os.listdir("C:/"))


#Create Directory

#os.mkdir("new_folder")


#Create Multiple Directories

#os.makedirs("folder/subfolder/data")


#Remove Directory

#os.rmdir("new_folder")


#Remove Multiple Directories

#os.removedirs("folder/subfolder/data")


#Rename File

#os.rename(
#    "old.txt",
#    "new.txt"
#)


#Remove File

#os.remove("test.txt")


#File Exists

print(os.path.exists("test.txt"))


#Check File

print(os.path.isfile("test.txt"))


#Check Folder

print(os.path.isdir("folder"))


#File Size

if os.path.exists("test.txt"):

    print(os.path.getsize("test.txt"))


#Absolute Path

print(os.path.abspath("test.txt"))


#Relative Path

print(os.path.relpath("test.txt"))


#Join Paths

path = os.path.join(
    "folder",
    "file.txt"
)

print(path)


#Split Path

path = os.path.split(
    "folder/file.txt"
)

print(path)


#Split Extension

path = os.path.splitext(
    "file.txt"
)

print(path)


#Get File Name

path = "/home/user/file.txt"

print(os.path.basename(path))


#Get Directory Name

path = "/home/user/file.txt"

print(os.path.dirname(path))


#Normalize Path

path = "folder/../file.txt"

print(os.path.normpath(path))


#Environment Variables

print(os.environ)


#Get Specific Environment Variable

print(
    os.environ.get("PATH")
)


#Set Environment Variable

#os.environ["APP_NAME"] = "Python"


#Delete Environment Variable

#del os.environ["APP_NAME"]


#System Information

print(os.name)


#CPU Count

print(os.cpu_count())


#Process ID

print(os.getpid())


#Parent Process ID

print(os.getppid())


#System Command

#os.system("echo Hello")


#Execute Command

#os.popen("dir").read()


#Walk Directory

for root,dirs,files in os.walk("."):

    print(root)

    print(dirs)

    print(files)


#Find Python Files

for root,dirs,files in os.walk("."):

    for file in files:

        if file.endswith(".py"):

            print(file)


#Directory Tree

for root,dirs,files in os.walk("."):

    level = root.count(os.sep)

    print(
        " "*level,
        root
    )


#File Rename Using OS

old = "old.txt"
new = "new.txt"

#os.rename(old,new)


#Copy File (using shutil)
import shutil

#shutil.copy(
#    "source.txt",
#    "destination.txt"
#)


#Move File

#shutil.move(
#    "source.txt",
#    "folder/"
#)


#Delete Folder

#shutil.rmtree(
#    "folder"
#)

# ==========================================
# ADVANCED OS.PATH
# ==========================================


import os


#Join Multiple Paths
path = os.path.join(
    "home",
    "user",
    "documents",
    "file.txt"
)

print(path)


#Check Absolute Path

print(
    os.path.isabs("/home/user/file.txt")
)


#Check Relative Path

print(
    os.path.isabs("file.txt")
)


#Common Path

paths = [
    "/home/user/file1.txt",
    "/home/user/file2.txt"
]

print(
    os.path.commonpath(paths)
)


#Common Prefix

paths = [
    "/home/user/file1.txt",
    "/home/user/file2.txt"
]

print(
    os.path.commonprefix(paths)
)


#Expand User Directory

path = "~/documents"

print(
    os.path.expanduser(path)
)


#Expand Environment Variable

path = "$HOME/documents"

print(
    os.path.expandvars(path)
)


#Get Access Time

if os.path.exists("test.txt"):

    print(
        os.path.getatime("test.txt")
    )


#Get Modification Time

if os.path.exists("test.txt"):

    print(
        os.path.getmtime("test.txt")
    )


#Get Creation Time

if os.path.exists("test.txt"):

    print(
        os.path.getctime("test.txt")
    )


#Same File

#print(
#    os.path.samefile(
#        "file1.txt",
#        "file2.txt"
#    )
#)



# ==========================================
# FILE SEARCH SYSTEM
# ==========================================


from pathlib import Path


#Find All Python Files

folder = Path(".")

python_files = list(
    folder.rglob("*.py")
)

print(python_files)


#Find Images

images = list(
    folder.rglob("*.png")
)

print(images)


#Find Large Files

for file in folder.rglob("*"):

    if file.is_file():

        if file.stat().st_size > 1000000:

            print(file)



# ==========================================
# FILE ORGANIZER PROJECT
# ==========================================


from pathlib import Path


downloads = Path("Downloads")


extensions = {

    ".jpg":"Images",
    ".png":"Images",

    ".pdf":"Documents",

    ".mp4":"Videos",

    ".mp3":"Music"

}


for file in downloads.iterdir():

    if file.is_file():

        folder = extensions.get(
            file.suffix
        )


        if folder:

            target = downloads / folder

            target.mkdir(
                exist_ok=True
            )

            file.rename(
                target / file.name
            )


# ==========================================
# BACKUP SYSTEM
# ==========================================


import shutil


source = Path("important")


backup = Path("backup")


#backup.mkdir(
#    exist_ok=True
#)


#for file in source.iterdir():

#    shutil.copy(
#        file,
#        backup
#    )



# ==========================================
# DIRECTORY SIZE CALCULATOR
# ==========================================


def folder_size(folder):

    total = 0

    for file in Path(folder).rglob("*"):

        if file.is_file():

            total += file.stat().st_size

    return total



print(
    folder_size(".")
)



# ==========================================
# DUPLICATE FILE FINDER
# ==========================================


from collections import defaultdict


files = defaultdict(list)


folder = Path(".")


for file in folder.rglob("*"):

    if file.is_file():

        size = file.stat().st_size

        files[size].append(file)



for size,items in files.items():

    if len(items)>1:

        print(
            "Possible duplicates:",
            items
        )



# ==========================================
# CREATE PROJECT STRUCTURE
# ==========================================


from pathlib import Path


folders = [

    "project",

    "project/src",

    "project/tests",

    "project/docs",

    "project/data"

]


for folder in folders:

    Path(folder).mkdir(
        exist_ok=True
    )



# ==========================================
# PATH LIB CROSS PLATFORM
# ==========================================


from pathlib import Path


# Windows Example

windows = Path(
    "C:/Users/Oscar/Desktop/file.txt"
)


print(windows)


# Linux Example

linux = Path(
    "/home/user/file.txt"
)


print(linux)



# ==========================================
# FILE EXTENSION CHANGER
# ==========================================


file = Path(
    "photo.txt"
)


new_file = file.with_suffix(
    ".jpg"
)


print(new_file)



# ==========================================
# DIRECTORY TREE VIEWER
# ==========================================


def tree(directory,level=0):

    path = Path(directory)

    for item in path.iterdir():

        print(
            " "*level,
            item.name
        )

        if item.is_dir():

            tree(
                item,
                level+1
            )


#tree(".")



# ==========================================
# SAFE FILE DELETE
# ==========================================


def delete_file(filename):

    file = Path(filename)

    if file.exists():

        file.unlink()

        print(
            "Deleted"
        )

    else:

        print(
            "File not found"
        )


#delete_file("test.txt")



# ==========================================
# FILE COUNT SYSTEM
# ==========================================


def count_files(folder):

    count = 0

    for file in Path(folder).rglob("*"):

        if file.is_file():

            count += 1

    return count



print(
    count_files(".")
)



# ==========================================
# MONITOR FILE CHANGE
# ==========================================


from pathlib import Path
import time


file = Path("test.txt")


#old = file.stat().st_mtime


#while True:

#    new = file.stat().st_mtime

#    if new != old:

#        print("File Changed")

#        break

#    time.sleep(1)