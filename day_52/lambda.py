double = lambda x: x+2
print(double(3))  
##Find Maximum
max = lambda a,b: a if (a>b) else b
print (max(5,8))
##Lambda Inside a Function
def cal(x) :
    
    return lambda a : a*x
double = cal(2)
print (double(5))