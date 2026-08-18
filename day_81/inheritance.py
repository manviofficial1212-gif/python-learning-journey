class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_details(self):
        print(self.name)
        print(self.salary)
class developer(employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

dev = developer("Manvi", 50000, "Python")
mgr = manager("Rahul", 70000, "IT")
dev.show_details()
mgr.show_details()



    