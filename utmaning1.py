class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = 267

    def read(self):
        print(f"Reading {self.title} by {self.author}")


book1 = Book("Book", "Gibbish")
book2 = Book("Sagan om Ringen", "J.R.R. Tolkien")

book1.read()
book2.read()