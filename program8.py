while(True):
        print("**************choose from the given option**************")
        print("1.check Value Error")
        print("2.check File Not Found Error")
        print("3.check Type Error")
        print("4.check Name Error")
        print("5.check Input output Error")
        print("6.Exit")
        ch=int(input("Enter Your Choice: "))
        if(ch==1):
                try:
                        f=open('file1.txt','z')
                        print("successful")
                except ValueError:
                        print("Value Error")
        elif(ch==2):
                try:
                        f=open('file1.txt','r')
                        print("successful")
                except FileNotFoundError:
                        print("File Not Found Error")
        elif(ch==3):
                try:
                        f=open('file1.txt','r',"w")
                        print("successful")
                except TypeError:
                        print("Type Error")
        elif(ch==4):
                try:
                        f=opens('file1.txt','r')
                        print("successful")
                except NameError:
                        print("Name Error")
        elif(ch==5):
                try:
                        f=open('file1.txt','r')
                        f.write("sample")
                        print("successful")
                except IOError:
                        print("Input Output Error")
        elif(ch==6):
                break
        else:
                break