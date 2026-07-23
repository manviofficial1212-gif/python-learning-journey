x = [2,5,3,8,6,9,1]
even = list(filter(lambda x: x%2==0, x))
print(even)

y = list (filter(lambda x:x>3,x))
print (y)
names = ["Manvi","Rahul","Ananya","Aman","Karan"]
x=list(filter(lambda x : len(x)>=5,names))
print(x)