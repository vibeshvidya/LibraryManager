from models.Member import Member

class Librarian(Member): #inheritance

    def display_role(self):
        print('This refers to a Librarian')
        #overriding
