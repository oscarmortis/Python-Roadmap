language = 'java'
if language == 'python':
    print ('language is python')
elif language == 'java':
    print('language is java')
else:
    print('no match')


user = 'Admin'
logged_in = True

if not logged_in:
    print('please log in')
else: 
    print('welcome')


condition = None
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')
    

condition = ''
if condition:
    print('evaluated to true')
else:
    print('evaluated to false')