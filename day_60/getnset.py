class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
    @property
    def salary (self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value>=0:
            self._salary= value
        else :
            print("invalid")
emp = employee("Manvi",50000)
print(emp.name)
print(emp.salary)
emp.salary=45000
print(emp.salary)
emp.salary=-5000
print(emp.salary)



        
        