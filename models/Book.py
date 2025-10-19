class Book:
    #Constructor
    def __init__(self, title, author, isbn):
        self.__title = title #encapsulation, in this case private variable
        self.__author = author
        self.isbn = isbn
        self.is_issued = False

    #getters and setters methods
    #encapsulation

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_is_issued(self):
        return self.__is_issued

    def issue(self):
        self.is_issued = True

    def return_the_book(self):
        self.is_issued = False


