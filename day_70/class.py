class employee:
    def __init__(self , name ,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls , emp_str):
            return cls(emp_str.split("-")[0], emp_str.split("-")[1])
emp_str = "John-50000"
e1 = employee.fromStr(emp_str)
print(e1.name)
print(e1.salary)