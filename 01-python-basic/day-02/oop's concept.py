# with basic salary TA DA
class Employee:
    def __init__(self, name, salary , ta , da):
        self.name = name
        self.salary = salary
        self.ta = ta
        self.da = da
    def fixedSalary(self):
        print(self.salary+self.da+self.ta)
obj = Employee("kaif khan" , 1000 , 2000 , 10)
obj.fixedSalary()

        