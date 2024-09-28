# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

from datetime import date


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

