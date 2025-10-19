from models.Member import Member
#student class is a child class of Member class
class Student(Member):
    def __init__(self, name, user_id, phone_number):
        super().__init__(name, user_id)
        self.phone_number = phone_number

    def dummyFunction(self):
        print("I am a dummy function")

    def display_role(self):
        print("This refers to a Student")
        #overriding is an example of 'Polymorphism'

