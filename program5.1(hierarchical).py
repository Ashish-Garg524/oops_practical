class STUDENT:
        def __init__(self):
                self.USN=input("Enter the USN Number")
                self.Name=input("Enter the Name")
                self.Age=int(input("Enter the Age"))
        def display(self):
                print("USN     : ", self.USN)
                print("Name    : ", self.Name)
                print("Age     : ", self.Age)
class UGSTUDENT(STUDENT):
        def __init__(self):
                super().__init__()
                self.semester=int(input("Enter the semester"))
                self.fees=int(input("Enter the fees"))
                self.stipened=int(input("Enter the Stipened"))
                STUDENT.display(self)
                print("Semester: ", self.semester)
                print("Fees    : ", self.fees)
                print("Stipened: ", self.stipened)
class PGSTUDENT(STUDENT):
        def __init__(self):
                super().__init__()
                self.semester=int(input("Enter the semester"))
                self.fees=int(input("Enter the fees"))
                self.stipened=int(input("Enter the Stipened"))
                STUDENT.display(self)
                print("Semester: ", self.semester)
                print("Fees    : ", self.fees)
                print("Stipened: ", self.stipened)
while(True):
        print("choose from following option")
        print("1.UGSTUDENT")
        print("2.PGSTUDENT")
        print("3.exit")
        ch=int(input("Enter the choice number"))
        if(ch==1):
                ug=UGSTUDENT()
        elif(ch==2):
                pg=PGSTUDENT()
        elif(ch==3):
                break
        else:
                print("Thank You")
                break