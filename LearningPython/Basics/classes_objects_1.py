class Employee:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def complete_details(self):
        print("my first name is: " + self.fname)
        print("my last name is: " + self.lname)
        print("my age is: " + self.age)
        return ''


emp1 = Employee("KIRAN", "KUMAR", str(34))
emp2 = Employee("SAI", "KIRAN", str(67))
print(emp1.complete_details())
print(emp2.complete_details())
