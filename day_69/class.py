class student :
    school = "ABC School"
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
student.change_school("XYZ School")
print(student.school)  

