#read file
f=open("sample.txt", "r")
data=f.read()
print(data)
f.close()


#read(n) – Read only n characters
f=open("sample.txt", "r")
print(f.read(10))
f.close()


#readline() – Read one line at a time
f=open("sample.txt", "r")
print(f.readline())
print(f.readline())
f.close()

#readlines() – Read all lines as a list
f=open("sample.txt", "r")
print(f.readlines())
f.close()   

f=open ("sample.txt", "r")
lines=f.readlines()
print(lines[1])

#Loop through a file (Best for large files)
f=open("sample.txt", "r")
for line in f:
    print(line)
f.close()

#seek() – Move the file pointer
f=open("sample.txt", "r")
print(f.read(10))
f.seek(0)
print(f.read(5))
f.close()


#tell() – Check the current position
f=open("sample.txt", "r")
print(f.tell())
f.read(5)
print(f.tell())
f.close