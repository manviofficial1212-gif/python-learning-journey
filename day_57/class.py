class person:
    name = "John"
    branch = "CSE"
    def info(self):
        print(f"{self.name} have {self.branch}")
a=person()
a.name = "manvi"
a.branch = "ece"
a.info()
b=person()
b.info()
c=person()
c.name = "shiv"
c.branch = "cse"
c.info()


        