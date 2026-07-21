##tell() – Find the current position of the file pointer
with open("sample.txt" , "r") as f:
    print (f.tell())
    data=f.read(5)
    print(data)
    print(f.tell())

##seek() – Move the file pointer
with open ("sample.txt" , "r") as f:
    print (f.read(6))
    print (f.tell( ))
    f.seek(1)
    print (f.tell())
    print (f.read(4))

##truncate() – Cut the file
with open ("sample.txt", "r+") as f:
    f.truncate (12)
    print (f.read())