from enum import member

from models.Book import Book
from models.Member import Member
from models.librarian import Librarian
from models.student import Student

if __name__=='__main__':
    god_of_Small_Things = Book("God of Small Things", "Arundhati Roy", 'abc002')
    print(god_of_Small_Things.isbn)
    print(god_of_Small_Things.is_issued)
    print(god_of_Small_Things.get_title())

   # member1=Member("Mammukka","2322")
    #print(member1.name)
    student1=Student("Anand","2323",'9545555002')
    print(student1)
    #student1.dummyFunction()
    #print(student1.dummyFunction())
    student1.display_role()

    librarian_obj=Librarian("vinod","2323")
    print(librarian_obj.name)
    librarian_obj.display_role()


