class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # write __str__ here
    def __str__(self):
        return self.title + " has " + str (self.pages) + " pages "
        


book = Book("Python", 300)

print(book)