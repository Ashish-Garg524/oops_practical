print("************ Menu Driven operations:************ ")
while True:
    print("choose from the following option: \n 1. String Operation \n 2.Tuple Operation \n 3. Exit \n")
    i1 = int(input("Enter your choice : "))
    if i1 == 1:
        while True:
            print("choose from the following operations: \n 1. Slicing \n 2. Length \n 3. Uppercase \n 4. Lowercase \n 5. Title \n 6. Character Count \n 7. Reverse \n 8. Find \n 9. Swapping \n 10. Strip \n 11. Exit")
            i2 = int(input())
            if i2 <= 0:
                print("Invalid input")
            elif i2 == 1:
                str1 = input("Enter string: ")
                a = int(input("Enter first index: "))
                b = int(input("Enter last index: "))
                print("The sliced string is", str1[a:b])
            elif i2 == 2:
                str1 = input("Enter string: ")
                print(len(str1))
            elif i2 == 3:
                str1 = input("Enter string: ")
                print(str1.upper())
            elif i2 == 4:
                str1 = input("Enter string: ")
                print(str1.lower())
            elif i2 == 5:
                str1 = input("Enter string: ")
                print(str1.title())
            elif i2 == 6:
                str1 = input("Enter string: ")
                ch = input("Enter the character: ")
                print("The character %c appears %d times in %s string" % (ch, str1.count(ch), str1))
            elif i2 == 7:
                str1 = input("Enter string: ")
                print(str1[::-1])
            elif i2 == 8:
                str1 = input("Enter string: ")
                ch = input("Enter the character to find: ")
                print(str1.find(ch))
            elif i2 == 9:
                str1 = input("Enter string: ")
                print(str1.swapcase())
            elif i2 == 10:
                str1 = input("Enter string: ")
                str2 = input("Enter the string to remove: ")
                print("The string after removing %s is %s" % (str2, str1.strip(str2)))
            elif i2 >= 11:
                break

    elif i1 == 2:
        while True:
            print("Following are the operations: \n 1. Concatenation \n 2. Nested Tuple \n 3. Slicing of Tuple \n 4. Reverse of Tuple \n 5. Finding an Element using Index Number \n 6. Finding Index of a Number \n 7. Length of a Tuple \n 8. Type \n 9. Count \n 10. Maximum of Tuple \n 11. Exit \n")
            i3 = int(input())
            if i3 == 1:
                tup1 = tuple(input("Enter the first tuple: ").split())
                print("Tuple 1 is:", tup1)
                tup2 = tuple(input("Enter the second tuple: ").split())
                print("Tuple 2 is:", tup2)
                print(tup1 + tup2)
            elif i3 == 2:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                tup2 = tuple(input("Enter the tuple: ").split())
                print("Tuple 2 is:", tup2)
                print((tup1,) + (tup2,))
            elif i3 == 3:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                a = int(input("Enter the starting index: "))
                b = int(input("Enter the ending index: "))
                print(tup1[a:b])
            elif i3 == 4:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                print(tup1[::-1])
            elif i3 == 5:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                a = int(input("Enter the index number: "))
                print(tup1[a])
            elif i3 == 6:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                a = input("Enter the entry you want to find: ")
                print(tup1.index(a))
            elif i3 == 7:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                print(len(tup1))
            elif i3 == 8:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                print(type(tup1))
            elif i3 == 9:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                a = input("Enter the character you want to count: ")
                print(tup1.count(a))
            elif i3 == 10:
                tup1 = tuple(input("Enter the tuple: ").split())
                print("Tuple 1 is:", tup1)
                print(max(tup1))
            elif i3 >= 11:
                break

    elif i1 == 3:
        exit()
