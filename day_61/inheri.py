class person:
    def __init__(self,name):
        self.name=name
    def introduction (self):
        print("my name is ",self.name)
class Teacher(person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
    def teach (self):
        print("I teach",self.subject)
teacher = Teacher ("manvi","python")
teacher.introduction()
teacher.teach ()



