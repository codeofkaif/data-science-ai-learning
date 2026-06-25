
class BankAccount:
    def __init__ (self , AccountNumber , Balance):
        self.AccountNumber = AccountNumber
        self.Balance = Balance
    def deposit(self , amount):
        self.Balance += amount
    def getbalance(self):
        return self.Balance


class Employee(BankAccount):
    def __init__(self, name, salary, empId, AccountNumber, Balance):
        super().__init__(AccountNumber, Balance)
        self.name = name
        self.salary = salary
        self.empId = empId

    def employeeInfo(self):
        print(f"Employee name: {self.name},\n Employee Salary: {self.salary},\nEmployee Id:  {self.empId}, \n Employee Account Number: {self.AccountNumber}, \n Employee Balance: {self.Balance}")
obj = Employee("kaif khan" , 5000000, 4321, 12345678910 , 8000000 )
obj.employeeInfo()
obj.deposit(300000)
obj.employeeInfo()