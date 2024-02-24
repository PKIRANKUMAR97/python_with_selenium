"""
class RateofInterest:
    def __init__(self, name, amount, interest):
        self.name = name
        self.amount = amount
        self.interest = interest

    def total_interest(self):
        print("total interest :", self.amount * self.interest) # this self.interest will take the values from the created objects p1,p2


p1 = RateofInterest("Ramesh", 100000, 0.05)
p1.total_interest()
p2 = RateofInterest("Raghav", 50000, 0.025)
p2.total_interest()

"""
"""
class RateofInterest:
    interest=0.09 # if the interest is same for all ,we can use class variable instead of instance variable
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def total_interest(self):
        print("total interest :", self.amount * RateofInterest.interest)  # here we use class variable for calculating interest 


p1 = RateofInterest("Ramesh", 100000)
p1.total_interest()
p2 = RateofInterest("Raghav", 50000)
p2.total_interest()
"""


class RateofInterest:
    interest = 0.09  # if the interest is same for all ,we can use class variable instead of instance variable

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def total_interest(self):
        print("total interest :",
              self.amount * RateofInterest.interest)  # here for both the p1,p2 only 0.2 is used as interest


p1 = RateofInterest("Ramesh", 100000)
RateofInterest.interest = 0.2
p1.total_interest()
p2 = RateofInterest("Raghav", 50000)
p2.interest = 0.1
p2.total_interest()
