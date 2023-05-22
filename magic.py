from magic1 import*

obj1 = ope()
obj2 = ope()

obj1.accept()
obj2.accept()

while(True):
        print("Choose from following option")
        print("1.Addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.Floor division")
        print("5.power")
        print("6.lesser than 2 list")
        ch=int(input("Enter the choice"))
        if(ch==1):
                obj1 + obj2
        elif(ch==2):
                obj1 - obj2
        elif(ch==3):
                obj1 * obj2
        elif(ch==4):
                obj1 // obj2
        elif(ch==5):
                obj1 ** obj2
        elif(ch==6):
                obj1 < obj2
        else:
                print("Thank you")
                break