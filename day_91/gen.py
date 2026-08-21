def gen():
    for i in range(1, 6):
        yield i
for i in gen():
    print(i)
        
    