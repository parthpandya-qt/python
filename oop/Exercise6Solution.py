class library_class:
    def __init__(self):
        self.No_of_books= 0
        self.books = []

    def add_book(self,book_name):
        self.No_of_books += 1
        self.books.append(book_name)

    def info(self):
        print(f"Library has {self.No_of_books} books.")
        for i in range(self.No_of_books):
            print(f"{i+1}. {self.books[i]}")


a=library_class()

a.add_book("To Kill a Mockingbird")
a.add_book("ring of fire")
a.info()