print("************ Menu Driven operations:************ ")
while True:
    print("Choose from the following option: \n 1. Set Operation \n 2. List Operation \n 3. Exit \n")
    i1 = int(input())
    
    if i1 == 1:
        set1 = set(input("Enter the elements of set 1: ").split())
        print(set1)
        set2 = set(input("Enter the elements of set 2: ").split())
        print(set2)
        
        while True:
            print("Choose from the following operations: \n")
            print("1. Union \n")
            print("2. Intersection \n")
            print("3. Symmetric Difference \n")
            print("4. Check for subset \n")
            print("5. Difference \n")
            print("6. Type \n")
            print("7. Length \n")
            print("8. Minimum \n")
            print("9. Maximum \n")
            print("10. Proper subset or not \n")
            print("11. Exit \n")
            i2 = int(input())
            
            if i2 == 1:
                print(set1.union(set2))
            elif i2 == 2:
                print(set1.intersection(set2))
            elif i2 == 3:
                print(set1 ^ set2)
            elif i2 == 4:
                print(set1 <= set2)
            elif i2 == 5:
                print(set1.difference(set2))
            elif i2 == 6:
                print(type(set1))
            elif i2 == 7:
                print(len(set1))
            elif i2 == 8:
                print(min(set1))
            elif i2 == 9:
                print(max(set1))
            elif i2 == 10:
                print(set1 > set2)
            else:
                break
    
    elif i1 == 2:
        l1 = list(input("Enter elements of the 1st list: ").split())
        print(l1)
        print(type(l1))
        l2 = list(input("Enter elements of the 2nd list: ").split())
        print(l2)
        print(type(l2))
        
        while True:
            print("Choose from the following operations: \n")
            print("1. Concatenation \n")
            print("2. Nested List \n")
            print("3. Iterating through Elements \n")
            print("4. Length \n")
            print("5. Check for Equivalence \n")
            print("6. Changing an Element \n")
            print("7. Appending an Element \n")
            print("8. Inserting Multiple Elements \n")
            print("9. Popping an Element \n")
            print("10. Printing an Element using Index Number \n")
            i3 = int(input())
            
            if i3 == 1:
                print(l1 + l2)
            elif i3 == 2:
                print([l1] + [l2])
            elif i3 == 3:
                for i in l1:
                    print(i)
            elif i3 == 4:
                print("The length is", len(l1))
            elif i3 == 5:
                print(l1 == l2)
            elif i3 == 6:
                print("Enter the index number of the element you want to change:")
                i4 = int(input())
                d = input("Enter the changed element: ")
                l1[i4] = d
                print(l1)
            elif i3 == 7:
                e = input("Enter the element you want to append: ")
                l1.append(e)
                print(l1)
            elif i3 == 8:
                print("Enter the elements:")
                l3 = list(input().split())
                print(l1 + l3)
            elif i3 == 9:
                print("Enter the index number of the element you want to pop:")
                f = int(input())
                print(l1.pop(f))
            elif i3 == 10:
                print("Enter the index number you want to print:")
                g = int(input())
                print(l1[g])
            else:
                break

    elif i1 == 3:
        break
