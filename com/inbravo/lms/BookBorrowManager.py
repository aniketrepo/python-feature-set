import Utility


#   All rights owned by Aniket Dixit
#   This project/solution involves 4 Python classes and a CSV file
#   https://github.com/aniketrepo/python-feature-set

def borrowBook(borrowerType):
    success = False
    while (True):
        firstName = input("Enter the first name of the borrower: ")
        if firstName.isalpha():
            break
        print("please input alphabet from A-Z")
    while (True):
        lastName = input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input alphabet from A-Z")

    t = "Borrow-" + firstName + ".csv"
    with open(t, "w+") as f:
        f.write("Library Management System  \n")
        f.write("Borrowed By : " + borrowerType + " - " + firstName + " " + lastName + "\n")
        f.write("Date: " + Utility.getDate() + "    Time:" + Utility.getTime() + "\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n")

    while success == False:
        print("Please select a option below:")
        for i in range(len(Utility.bookname)):
            print("Enter", i, "to borrow book", Utility.bookname[i])

        try:
            a = int(input())
            try:
                if (int(Utility.quantity[a]) > 0):
                    print("Book is available")
                    with open(t, "a") as f:
                        f.write("1. \t\t" + Utility.bookname[a] + "\t\t  " + Utility.authorname[a] + "\n")

                    Utility.quantity[a] = int(Utility.quantity[a]) - 1
                    with open("Stock.csv", "w+") as f:
                        for i in range(3):
                            f.write(Utility.bookname[i] + "," + Utility.authorname[i] + "," + str(
                                Utility.quantity[i]) + "," + "$" + Utility.cost[i] + "\n")

                    # multiple book borrowing code
                    loop = True
                    count = 1
                    while loop == True:
                        choice = str(input(
                            "Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        if (choice.upper() == "Y"):
                            count = count + 1
                            print("Please select an option below:")
                            for i in range(len(Utility.bookname)):
                                print("Enter", i, "to borrow book", Utility.bookname[i])
                            a = int(input())
                            if (int(Utility.quantity[a]) > 0):
                                print("Book is available")
                                with open(t, "a") as f:
                                    f.write(str(count) + ". \t\t" + Utility.bookname[a] + "\t\t  " + Utility.authorname[
                                        a] + "\n")

                                Utility.quantity[a] = int(Utility.quantity[a]) - 1
                                with open("Stock.csv", "w+") as f:
                                    for i in range(3):
                                        f.write(Utility.bookname[i] + "," + Utility.authorname[i] + "," + str(
                                            Utility.quantity[i]) + "," + "$" + Utility.cost[i] + "\n")
                                        success = False
                            else:
                                loop = False
                                break
                        elif (choice.upper() == "N"):
                            print("Thank you for borrowing books from us. ")
                            print("")
                            loop = False
                            success = True
                        else:
                            print("Please choose as instructed")

                else:
                    print("Book is not available")
                    borrowBook()
                    success = False
            except IndexError:
                print("")
                print("Please choose book according to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
