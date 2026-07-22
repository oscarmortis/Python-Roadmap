nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print('found')
        break
    print(num)


#Letters
nums = [1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num, letter)


#while loop
x = 0
while x < 10:
    print(x)
    x += 1
    

#loop infinite
x = 0
while True:
    print(x)
    x += 1