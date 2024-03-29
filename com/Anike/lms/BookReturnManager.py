import Utility


#   All rights owned by Aniket Dixit
#   This project/solution involves 4 Python classes and a CSV file
#   https://github.com/aniketrepo/python-feature-set

def returnBook():
    name = input("Enter name of borrower: ")
    a = "Borrow-" + name + ".csv"
    try:
        with open(a, "r") as f:
            lines = f.readlines()
            lines = [a.strip("$") for a in lines]

        with open(a, "r") as f:
            data = f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b = "Return-" + name + ".csv"
    with open(b, "w+") as f:
        f.write("Library Management System \n")
        f.write("Returned By: " + name + "\n")
        f.write("Date: " + Utility.getDate() + "    Time:" + Utility.getTime() + "\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")

    total = 0.0
    for i in range(3):
        if Utility.bookname[i] in data:
            with open(b, "a") as f:
                f.write(str(i + 1) + "\t\t" + Utility.bookname[i] + "\t\t$" + Utility.cost[i] + "\n")
                Utility.quantity[i] = int(Utility.quantity[i]) + 1
            total += float(Utility.cost[i])

    print("\t\t\t\t\t\t\t" + "$" + str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat = input()
    if (stat.upper() == "Y"):
        print("By how many days was the book returned late?")
        day = int(input())
        fine = 2 * day
        with open(b, "a") as f:
            f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
        total = total + fine

    print("Final Total: " + "$" + str(total))
    with open(b, "a") as f:
        f.write("\t\t\t\t\tTotal: $" + str(total))

    with open("Stock.csv", "w+") as f:
        for i in range(3):
            f.write(
                Utility.bookname[i] + "," + Utility.authorname[i] + "," + str(Utility.quantity[i]) + "," + "$" +
                Utility.cost[i] + "\n")
