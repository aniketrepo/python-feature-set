import Return
import ListSplit
import Borrow
import os

#   This is the main class of the Aniket's LMS
#   All rights owned by Aniket Dixit
#   This project/solution involves 4 Python classes and a CSV file

def start(): confirmTheUser()

def confirmTheUser():
        print("--------------------------------------------------------")
        print(" -*- Welcome to Aniket's library management system  -*- ")
        print("--------------------------------------------------------")
        print("Enter 1. If You Are a Teacher")
        print("Enter 2. If You Are a Student")
        print("Enter 3. To exit")
        try:
            userInput = int(input("Select a choice from 1-2: "))
            print
            if (userInput == 1):
                borrowerType = "Teacher"
                print("Thanks for confirming that you are a " + borrowerType)
                print("------------------------------------------------------")
            elif (userInput == 2):
                borrowerType = "Student"
                print("Thanks for confirming that you are a " + borrowerType)
                print("------------------------------------------------------")
            else:
                print("Please enter a valid choice from 1 Or 2")
        except ValueError:
            print("Please input as suggested.")

        performTheLibraryFunction(borrowerType)

def performTheLibraryFunction(borrowerType):
    while (True):
        print("------------------------------------------------------")
        print("Enter 1. To Display the Available Book Titles")
        print("Enter 2. To Borrow a Book")
        print("Enter 3. To return a Book")
        print("Enter 4. To Exit")
        try:

            a = int(input("Select a choice from 1-4: "))
            print
            if (a == 1):
                with open(os.getcwd() + "/stock.csv", "r") as f:
                    lines = f.read()
                    print("------------------------------------------------------")
                    print("The following book titles are available: ")
                    print(lines)
                    print("------------------------------------------------------")

            elif (a == 2):
                ListSplit.listSplit()
                Borrow.borrowBook(borrowerType)
            elif (a == 3):
                ListSplit.listSplit()
                Return.returnBook()
            elif (a == 4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")

start()
