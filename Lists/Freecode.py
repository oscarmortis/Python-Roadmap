nums = [1,2,3,4,5,6,7,8,9,10]
# mylist = filter(lambda n: n*n, nums)
# print(mylist)
mylist = []
for n in nums:
    mylist.append(n*n)
print(mylist)

mylist = [n*n for n in nums]
print(mylist)

mylist2 = map(lambda n: n*n, nums)
print(mylist2)