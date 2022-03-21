# Author: Francisco
# Module: AddressBook.py
#
# Based on the code at https://www.youtube.com/watch?v=PxZE0e-ePoI

class Person:
    def __init__(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number

    def full_name(self):
        print(f'{self.first} {self.last}')

    def __str__(self):
        return f"{self.first} {self.last} : {self.age} : {self.phone_number}"

    contact = list()


print("Welcome to the Address Book Program")
print("Enter your contact's information")

first_name = input('Fist Name = ')
last_name = input('Last Name = ')
age = input('Age = ')
phone_number = input("Phone Number = ")

print('Contact Saved!')

our_contact = Person(first_name, last_name, age, phone_number)
print(our_contact)
