class Employee:
        raise_amount=1.05
        def __init__(self):
                self.first=input("Enter the first Name: ")
                self.last=input("Enter the last Name: ")
                self.empid=input("Enter the employee id in number: ")
                self.pay=int(input("Enter the pay: "))
        def apply_raise(self):
                print("Appraised Amount for Employee is: ", self.pay * self.raise_amount)
class Developer(Employee):
        raise_amount=2.3
        def apply_raise(self):
                print("Appraised Amount for Developer is: ", self.pay * self.raise_amount)
class Manager(Employee):
        raise_amount=3.1
        def apply_raise(self):
                print("Appraised Amount for Manager is: ", self.pay * self.raise_amount)
obj1=Employee()
obj2=Manager()
obj3=Developer()
obj1.apply_raise()
obj2.apply_raise()
obj3.apply_raise()