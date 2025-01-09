#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.
"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0

    def __init__(self, P, r, n):
        self.principal = P
        self.rate = r/100
        self.nPeriods = n

    def interest(self, t, Ttype = "years"):
        return round(self.amount(t, Ttype) - self.principal, 2)
    
    def amount(self, t, Ttype = "years"):
        if Ttype == 'years':
            return round(self.principal * ((1 + (self.rate / self.nPeriods))**(self.nPeriods * t)), 2)
        elif Ttype == 'months':
            t = t/12
            return round(self.principal * ((1 + (self.rate / self.nPeriods))**(self.nPeriods * t)), 2)
        elif Ttype == 'days':
            t = t/365
            return round(self.principal * ((1 + (self.rate / self.nPeriods))**(self.nPeriods * t)), 2)
        elif Ttype == 'weeks':
            t = t/52
            return round(self.principal * ((1 + (self.rate / self.nPeriods))**(self.nPeriods * t)), 2)
        else:
            print(f"{Ttype} is to a specified Time frame.")
            return None
    
    def __str__(self):
        return f"Principal of ${self.principal}, Rate of {self.rate}%, With {self.nPeriods} compound periods per year."

a = Calc(P=1000,r=4,n=2)
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(P=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62

#add the ability to input time as years mounths and days

c = Calc(1000, 4, 2)
print(c.interest(36, 'months'))
print(c)