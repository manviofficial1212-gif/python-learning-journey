class library :
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            print(book)
    def total_books(self):
        print("Total number of books:",len(self.books))
lib = library()
lib.add_book("Python Programming")
lib.add_book("Java Programming")
lib.add_book("C++ Programming")
lib.total_books()
lib.show_books()
while True:
    print("1. Add Book")
    print("2. Show Books")
    print("3. Total Books")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book = input("Enter book name: ")
        lib.add_book(book)
    elif choice == 2:
        lib.show_books()
    elif choice == 3:
        lib.total_books()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
            
        