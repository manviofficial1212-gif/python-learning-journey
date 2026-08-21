from functools import cache 
import time
@cache
def sq (n):
    print("calculating")
    time.sleep(2)
    return n*n
print (sq(5))
print (sq(6))
print (sq(5))