dict1={}
class Employee:
        def input(self):
                self.name=input("Enter your name ")
                self.address=input("Enter your address ")
                self.pan=input("Enter your pan number ")
                self.basic=int(input("Enter your basic salary "))
                self.da=0.40*self.basic
                self.hra=0.25*self.basic
                self.deductions=0.20*self.basic
                self.cca = 300
                self.gross_sal=self.basic + self.da + self.hra + self.cca
                self.tds=0.17*self.gross_sal
                self.net_pay= self.gross_sal - self.tds
                self.update()
        def update(self):
                dict1.update({ self.name:{
                "Name":self.name,
                "Address":self.address,
                "PAN":self.pan,
                "Basic Salary":self.basic,
                "TDS":self.tds,
                "DA":self.da,
                "HRA":self.hra,
                "Deductions":self.deductions,
                "Gross salary":self.gross_sal,
                "Net pay":self.net_pay
                }})
        def search(self,name):

                for key in dict1:
                        if(key == name):
                                print("Employee found")
                                for i in dict1[key]:
                                        print(i,dict1[key][i])
                        else:
                                print("No employee found")
        def empprint(self):
                for key in dict1:
                        for i in dict1[key]:
                                print(i,dict1[key][i])
while(True):
        emp=Employee()
        print("\n1.Add employee details\n2.Searh Employee by name\n3.Print employee details\n4.Exit\n")
        ch=int(input("Enter your choice "))
        if(ch == 1):
                emp.input()
        elif ch == 2:
                name=input("Enter the name to search")
                emp.search(name)
        elif ch == 3:
                emp.empprint()
        elif ch == 4:
                break
        else:
                print("Enter correct choice")
print("Thank you")
#       for i in d[key]:
#               print(i,d[key][i])
#       for key in d:
#               print(key,d[key])