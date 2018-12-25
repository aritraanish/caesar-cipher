print("What do you want to do?")
print("1. ENCRYPT")
print("2. DECRYPT")
print("3. QUIT")
print("Choose the corresponding number.")
print("")


incorrect = True
retry = True


while(retry == True):
    choice = str(input("Enter choice number:- "))

    if (choice=="1"):

        inp = str(input("Enter the string:- "))
        k = int(input("Enter the Caesar Key:- "))
        print("")

        for i in range(0, len(inp)):
            a = ord(inp[i])

            for j in range (0, k):
                a = a + 1

                if (a>122):
                    a = 97

            print(chr(a), end="")

        print("")
        print("")

        while (incorrect == True):

            print("Do you want to try again?")
            print("1. Yes")
            print("2. No")
            y=str(input())

            if (y=="1" or y=="y" or y=="Y" or y=="yes" or y=="Yes"):
                retry = True
                incorrect = False

            elif (y=="2" or y=="n" or y=="N" or y=="no" or y=="No"):
                retry = False
                incorrect = False

            else:
                incorrect = True

    elif (choice=="2"):
        inp = str(input("Enter the string:-"))
        k = int(input("Enter the Caesar Key:- "))

        for i in range(0, len(inp)):
            a = ord(inp[i])

            for k in range (0, k):
                a = a - 1

                if (a<97):
                    a = 122

            print(chr(a), end="")

        print("")
        print("")

        incorrect = True

        while (incorrect == True):

            print("Do you want to try again?")
            print("1. Yes")
            print("2. No")
            y=str(input())

            if (y=="1" or y=="y" or y=="Y" or y=="yes" or y=="Yes"):
                retry = True
                incorrect = False

            elif (y=="2" or y=="n" or y=="N" or y=="no" or y=="No"):
                retry = False
                incorrect = False

            else:
                incorrect = True

    elif (choice=="3"):
        retry = False

    else:
        print("Wrong Choice")
        
