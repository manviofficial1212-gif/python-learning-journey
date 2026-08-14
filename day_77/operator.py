class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__ (self,value):
        
        return self.marks+value.marks  


s1 = Student(80)
s2 = Student(15)

print(s1 + s2)