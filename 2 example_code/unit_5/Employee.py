import random
class Employee:

    num_employees = 0

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.id = random.randint(0,500)
        num_employees += 1
    
    def __str__(self):
        return f'{self.fname} {self.lname}'

    def calculate_pay(self):
        return 0

class Salaried(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
    def __str__(self):
        return super().__str__() + f' makes ${self.salary}'

    def calculate_pay(self):
        return self.salary
    
    def give_raise(self, bump):
        if bump > 1:
            bump /= 100
        self.salary = self.salary + self.salary*bump

class Hourly(Employee):
    def __init__(self, fname, lname, rate, num_hours):
        super().__init__(fname, lname)
        self.rate = rate
        self.num_hours = num_hours

    def __str__(self):
        return super().__str__() + f' makes ${self.rate} per hour.'

    def calculate_pay(self):
        return self.rate * self.num_hours
    
    def give_raise(self, bump):
        if bump > 1:
            bump /= 100
        self.rate = self.rate + self.rate*bump

