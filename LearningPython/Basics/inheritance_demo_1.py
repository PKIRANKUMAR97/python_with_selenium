"""
class Parentclass:
    def __init__(self):
        print("Parentclass instance")

    def parent_method(self):
        print("parent money")


class Childclass(Parentclass):
    pass


c = Childclass()
c.parent_method()    # inherits property from parent class

p = Parentclass()
p.parent_method()
"""

"""
class RateofInterest:
    interest = 0.06

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def total_interest(self):
        print("total interest :", self.amount * self.interest)


class Student(RateofInterest):
    pass


s = Student("AMAR", 500000)
s.total_interest()

"""

class RateofInterest:
    interest = 0.06

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def total_interest(self):
        print("total interest :", self.amount * self.interest)


class Student(RateofInterest):
    interest = 0.03


s = Student("AMAR", 500000)
s.total_interest()     # this method uses the interest 0.03 defined in the Student class

