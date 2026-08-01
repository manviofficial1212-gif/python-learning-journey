class student ():
    college = "banasthali"
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
s1 = student("Riya", "CSE")
s2 = student("manisha", "ECE")
print(s1.name)
print(s1.branch)    
print(s2.name)
print(s2.branch)
print(s1.college)
print(s2.college)