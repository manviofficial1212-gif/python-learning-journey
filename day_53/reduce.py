from functools import reduce
list = [1,2,3,4,5]
r=reduce(lambda x,y:x+y, list)
print(r)
