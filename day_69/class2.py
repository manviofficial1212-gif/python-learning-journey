class college:
    college = "Banasthali University"
    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college
college.change_college("MIT University")
print("my college is:", college.college)

        