# #Use 'pass' keyword to make a function use later and prevent showin error.
# def hello_func():
#     pass
# print(hello_func())


# def hello_func():
#     print('hello function!')

# hello_func()
# hello_func()
# hello_func()
# hello_func()


#To make it print 4 times without typing function name 4 times.
# def hello_func():
#     print('hello function!')
# for i in range (4):
#     hello_func()


#to 
# def hello_func():
#     print ('hello functions!')
# hello_func()


#to print the string 
# def hello_func():
#     return 'hello functions!'
# print(hello_func())


# #greeting
# def hello_func(greeting):
#     return '{} function.'.format(greeting)
# print(hello_func("hey"))


# #with name
# def hello_func(greeting, name = 'you'):
#      return '{}, {}'.format(greeting, name)
# print(hello_func('Hi', name = 'Corey'))


# #simpler method with f'string
# def hello_func(greeting, name = 'you'):
#      return f'{greeting}, {name}'
# print(hello_func('Hi', name = 'corey'))
     
# #more simpler
# greeting = "Hi"
# name = "Corey"
# print(f"{greeting}, {name}")

# #mroe simpler
# greeting = "Hi"
# name = "Corey"
# print("{}, {}".format(greeting, name))


# def student_info(*a, **b):
#      print(a)
#      print(b)
# student_info('Math', 'Art', Name = 'John', Age = 25)


#same thing
# def student_info(*a, **b):
#     print(a)
#     print(b)
# curses = ['maths', 'science']
# info = {'name':'john', 'age': 22}

# student_info(*curses, **info)

def hello():
    print("Hello")

a = hello

b = a

b()