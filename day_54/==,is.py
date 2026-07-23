a=[1,2,3,4]
b=[1,2,3,4]
c=a
print(a is b)
print(a is c)
print(a==b)
print(a==c)
c.append(5)
print(a)
print(b)
print(c)