class ope:

        def __init__(self):
                self.l1=[]

        def accept(self):
                n=int(input("Enter the number of element: "))
                for i in range(0,n):
                        e=int(input("Enter the element"))
                        self.l1.append(e)
                print("The Element are : ",self.l1)

        def __add__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]+other.l1[i])
                print("The addition is : ", newlist)

        def __sub__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]-other.l1[i])
                print("The subtraction is : ", newlist)

        def __mul__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]*other.l1[i])
                print("The multiplication is : ", newlist)

        def __floordiv__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]//other.l1[i])
                print("The floor division is : ", newlist)

        def __pow__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]**other.l1[i])
                print("The power is : ", newlist)

        def __lt__(self,other):
                newlist=[]
                for i in range(0,len(self.l1)):
                        newlist.append(self.l1[i]<other.l1[i])
                print("The lesser than of 2 list is : ", newlist)