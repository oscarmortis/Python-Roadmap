student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
print(student['name'])


#by default this git method returns none instead of Error.
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
print(student.get('phone'))


#we can also specify a default value for keys that dont exist. 
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
print(student.get('phone', 'Not Found'))


#how we can add a new entry to our dictionary 
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))


#method to update values.
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
student['phone'] = '555-5555'
student['name'] = 'jane'
print(student)


#we can also update values using the update method (supports updating multiple values at a time)
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
student.update({'name': 'jimmy', 'age': 23, 'phone': '555-6666'})
print (student)


#to delete a specific key and its value. (Del keyword)
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
del student['age']
print(student)


#you can also remove it with pop method if you want to use it in future.
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
age = student.pop('age')
print(student)
print(age)


#to see the length of the keys.
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
print(len(student))


#to see all of this keys
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
print(student.keys())


#to see all of our values
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
print(student.values())


#to see the keys and values.
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
print(student.items())


#to loop through all of the keys and values
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
for key in student:
    print(key)


#loop through items and values both.
student = {'name': 'john', 'age':25, 'courses': ['math', 'compsci']}
for key, value in student.items():
    print(key, value)