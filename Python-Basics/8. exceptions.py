#Simple try except
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot Divide by Zero")


#Catch Any Exception
try:
    print(10 / 0)

except Exception as e:
    print(e)


#Multiple Exceptions
try:
    number = int("Python")

except ValueError:
    print("Value Error")

except TypeError:
    print("Type Error")


#One except for Multiple Errors
try:
    number = int("Python")

except (ValueError, TypeError):
    print("Error")


#Else Block
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print(number)


#Finally Block
try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Finished")


#Else and Finally
try:
    print(100 / 2)

except ZeroDivisionError:
    print("Error")

else:
    print("Success")

finally:
    print("Done")


#ValueError
try:
    number = int("abc")

except ValueError:
    print("Invalid Number")


#TypeError
try:
    print("10" + 20)

except TypeError:
    print("Wrong Type")


#IndexError
numbers = [1,2,3]

try:
    print(numbers[10])

except IndexError:
    print("Invalid Index")


#KeyError
student = {
    "name":"Oscar"
}

try:
    print(student["age"])

except KeyError:
    print("Key Missing")


#AttributeError
text = "Python"

try:
    text.append("A")

except AttributeError:
    print("Attribute Error")


## ImportError

try:
    from math import xyz
except ImportError:
    print("Cannot import xyz from math")


#FileNotFoundError
try:
    open("unknown.txt")

except FileNotFoundError:
    print("File Not Found")


#ZeroDivisionError
try:
    print(100 / 0)

except ZeroDivisionError:
    print("Division Error")


#OverflowError
try:
    print(10.0 ** 1000)

except OverflowError:
    print("Overflow")


#AssertionError
try:
    assert 5 > 10

except AssertionError:
    print("Assertion Failed")


#UnicodeError
try:
    "Python".encode("ascii").decode("utf-16")

except UnicodeError:
    print("Unicode Error")


#Raise Exception
raise Exception("Something Went Wrong")


#Raise ValueError
#raise ValueError("Invalid Age")


#Raise TypeError
#raise TypeError("Wrong Type")


#Raise RuntimeError
#raise RuntimeError("Runtime Error")


#Raise Custom Message
age = 15

if age < 18:
    raise Exception("Must be 18+")


#Exception Object
try:
    print(10 / 0)

except Exception as error:
    print(type(error))
    print(error)


#Nested try
try:

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner")

except:
    print("Outer")


#Return from try
def divide(a,b):

    try:
        return a/b

    except ZeroDivisionError:
        return None

print(divide(10,0))


#Return from finally
def test():

    try:
        return "Try"

    finally:
        print("Finally")

print(test())


#Input Validation
try:
    age = int(input("Age : "))

except ValueError:
    print("Enter Numbers Only")


#Dictionary Lookup
student = {
    "name":"Oscar"
}

try:
    print(student["age"])

except KeyError:
    print("Age Missing")


#List Lookup
numbers = [10,20]

try:
    print(numbers[5])

except IndexError:
    print("Out of Range")


#Safe Division
def divide(a,b):

    try:
        return a/b

    except ZeroDivisionError:
        return "Cannot Divide"

print(divide(20,0))


#Safe File Open
try:

    file = open("notes.txt")

except FileNotFoundError:
    print("No File")


#Convert Input
try:
    number = float("12.5")

    print(number)

except ValueError:
    print("Invalid")


#KeyboardInterrupt
#try:
#    input("Press Ctrl+C : ")
#
#except KeyboardInterrupt:
#    print("Stopped")


#Pass Exception
try:
    print(10/0)

except ZeroDivisionError:
    pass


#Print Full Exception
try:
    print(10/0)

except Exception as e:
    print(repr(e))

#Custom Exception
class InvalidAgeError(Exception):
    pass

raise InvalidAgeError("Age Must be 18+")


#Raise Custom Exception
class InvalidMarks(Exception):
    pass

marks = -10

if marks < 0:
    raise InvalidMarks("Marks Cannot be Negative")


#Catch Custom Exception
class InvalidSalary(Exception):
    pass

try:
    raise InvalidSalary("Invalid Salary")

except InvalidSalary as e:
    print(e)


#Custom Exception with __init__
class InvalidAge(Exception):

    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid Age : {age}")

try:
    raise InvalidAge(15)

except InvalidAge as e:
    print(e)


#Raise from Another Exception
try:
    int("Python")

except ValueError as e:
    raise RuntimeError("Conversion Failed") from e


#Exception Chaining
try:

    try:
        10/0

    except ZeroDivisionError as e:
        raise ValueError("Inner Error") from e

except Exception as e:
    print(e)


#Re-raise Exception
try:
    10/0

except ZeroDivisionError:
    print("Logging Error")
    raise


#Suppress Exception
from contextlib import suppress

with suppress(FileNotFoundError):
    open("unknown.txt")


#Suppress Multiple Exceptions
from contextlib import suppress

with suppress(FileNotFoundError, ZeroDivisionError):
    open("unknown.txt")
    print(10/0)


#Traceback
import traceback

try:
    10/0

except Exception:
    traceback.print_exc()


#Print Exception Only
import traceback

try:
    int("Python")

except Exception:
    print(traceback.format_exc())


#Logging Exception
import logging

logging.basicConfig(level=logging.ERROR)

try:
    10/0

except Exception:
    logging.exception("Something Failed")


#Warning
import warnings

warnings.warn("This is a Warning")


#Ignore Warning
import warnings

warnings.filterwarnings("ignore")

warnings.warn("Ignored")


#Create Warning
import warnings

warnings.warn("Use New Function", UserWarning)


#Resource Handling
try:

    file = open("test.txt")

except FileNotFoundError:
    print("Missing File")

else:
    file.close()


#with Statement
try:

    with open("test.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("Missing")


#finally Always Runs
try:
    print("Try")

finally:
    print("Finally")


#Exception in Function
def divide(a,b):

    if b == 0:
        raise ZeroDivisionError("Cannot Divide")

    return a/b

try:
    print(divide(10,0))

except ZeroDivisionError as e:
    print(e)


#Validate Function
def validate(age):

    if age < 18:
        raise ValueError("Invalid Age")

try:
    validate(15)

except ValueError as e:
    print(e)


#Nested Function Exception
def first():
    second()

def second():
    raise Exception("Error")

try:
    first()

except Exception as e:
    print(e)


#Check Exception Type
try:
    int("abc")

except Exception as e:
    print(type(e))


#Access Exception Arguments
try:
    raise ValueError("Wrong Input")

except ValueError as e:
    print(e.args)


#Multiple except Order
try:
    int("abc")

except ValueError:
    print("Value Error")

except Exception:
    print("General")


#Generic Exception Last
try:
    10/0

except ZeroDivisionError:
    print("Division")

except Exception:
    print("General")


#Raise if Condition Fails
password = "123"

if len(password) < 6:
    raise ValueError("Password Too Short")


#Use assert
number = 10

assert number > 0

print("Valid")


#assert with Message
age = 10

assert age >= 18, "Must be Adult"


#Safe Dictionary
student = {
    "name":"Oscar"
}

try:
    print(student["age"])

except KeyError:
    print(student.get("age"))


#Safe List Access
numbers = [10,20]

try:
    print(numbers[5])

except IndexError:
    print("Default Value")


#Safe Integer Conversion
text = "100"

try:
    number = int(text)

except ValueError:
    number = 0

print(number)


#Retry Logic
count = 0

while True:

    try:
        print(10/0)

    except ZeroDivisionError:
        count += 1

        if count == 3:
            break


#Break on Success
while True:

    try:
        number = int("100")
        print(number)
        break

    except ValueError:
        print("Retry")


#Exception in Loop
numbers = [10,20,0,5]

for number in numbers:

    try:
        print(100/number)

    except ZeroDivisionError:
        print("Skipped")


#Continue after Exception
numbers = [1,2,0,4]

for number in numbers:

    try:
        print(10/number)

    except ZeroDivisionError:
        continue


#finally in Loop
numbers = [2,1,0]

for number in numbers:

    try:
        print(10/number)

    except ZeroDivisionError:
        print("Error")

    finally:
        print("Finished")


#Exception with Input
#try:
#    age = int(input("Age : "))
#    print(age)
#
#except ValueError:
#    print("Numbers Only")


#Catch OSError
try:
    open("/invalid/path/file.txt")

except OSError:
    print("OS Error")


#Catch MemoryError
#try:
#    huge = [0] * (10**20)
#
#except MemoryError:
#    print("Out of Memory")


#Catch RecursionError
def test():
    return test()

#try:
#    test()
#
#except RecursionError:
#    print("Maximum Recursion Reached")