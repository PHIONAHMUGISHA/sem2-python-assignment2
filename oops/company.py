# class company:
#     # constructor
#     def _intit_(self, name,email, contact):
#         self.name =name
#         self.email =email
#         self.contact =contact

# # new intance
# company_one = company('Alexa,phionahtumusiime99@gamail.com,754969528')        
# print(company_one)

# To do : complete the
# Author 
# Book(maximum of 5 properties for each class)
# Add 2 functions and 2 classes each.

# Assignment 2
class Author:
    def __init__(self, name, email, book, contact, id):
        self.name =name
        self.email =email
        self.book =book
        self.contact =contact
        self.id =id
        
    def details(self):   
        print(f"{self.name} {self.email} {self.book} {self.contact} ({self.id}")

    def reference(self):
        print(26/0/2024)
author1 = Author("Mutabaazi" ,"tabazi99@gmail.com" ,"the evolution","754969528","043")
author1.details()
author1.reference()



