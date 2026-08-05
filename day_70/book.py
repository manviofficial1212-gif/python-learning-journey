class book:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    @classmethod
    def fromStr(cls , book_str):
            return cls(book_str.split("-")[0], book_str.split("-")[1])
book1 = book.fromStr("Python-500")

print(book1.name)
print(book1.price)