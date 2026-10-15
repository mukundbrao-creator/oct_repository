class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Now, {self.title} is borrowed!")
        else:
            print(f"{self.title} is already borrowed.")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed yet.")


book1 = Book("Harry Potter", "J. K. Rowley", False)
book1.borrow()
book1.return_book()

book2 = Book("Kingdom of Fantasy", "Geronimo Stilton", True)
book2.borrow()
book2.return_book()

book3 = Book("Noble Stilts", "Jake Perry", False)
book3.borrow()
book3.return_book()