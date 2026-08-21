from functools import cache
@cache
def square(n):
    print ("calculating")
    return n*n
print (square(5))
print (square(5))
print (square(3))
print (square(5))