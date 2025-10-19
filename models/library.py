class Library:

    # Attributes: name, collection of books
    #add new book
    #display the books
    #issue books
    #return the book

    def __init__(self, name):
        self.name = name
        self.books = [] #list of books

# function to add new books in the library
    def add_book(self, book):
        self.books.append(book)

# function to display all the books in the library

    def display_books(self):
        print("**********************")
        print(f"Books : {self.name}")
        print("**********************")

        for book in self.books:
            print(book.name)

    def issue_book(self, book):
        if book in self.books and not book.is_issued():
            book.issued()
            print("Book was issued")
            return True # confirmation for issuing the book
        print("failed to issue the book")
        return False # fail to issue the book

    def return_book(self, book):
        if book in self.books and book.is_issued():
            book.return_the_book()
            print("returning the book was successful")
            return True # confirmation for returning the book
        print("failed to return the book")
        return False # fail to return the book