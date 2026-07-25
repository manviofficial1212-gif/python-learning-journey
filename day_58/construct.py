class book:
    def __init__(self , title , author, price):
        self.title = title
        self.author = author
        self.price = price
book1 = book ("Python Basics", "CodeWithHarry", 499)
book2 = book("Atomic Habits", "James Clear", 699)
print (book1.title , book1.author , book1.price)
print (book2.title , book2.author , book2.price)

class student:
    def __init__(self , name ,branch , cgpa):
        self.name = name
        self.branch = branch
        self.cgpa = cgpa
s1 = student ("manvi", " ece" , "8.5")
s2 = student("Rahul", "CSE", 9.1)
print (s1.name , s1.branch , s1.cgpa)
print (s2.name , s2.branch , s2.cgpa)

