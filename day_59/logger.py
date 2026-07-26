def logger (func):
    def wrapper():
        print("======loding======")
        func()
        print ("======thanks======")
    return (wrapper)
@logger
def welcome():
    print ("wlcome manvi")
@logger
def add():
    print ("sum =", 20+10)

welcome()
print()
add()
