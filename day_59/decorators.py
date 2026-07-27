def deco(func): 
    def wrapper():
        print ("good morning")
        func()
        print ("thanks")
    return wrapper

@deco
def hello ():
    print ("hello")

hello()


    
