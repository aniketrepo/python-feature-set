print("Welcome to the rollercoaster!")
height = int(input("Please enter your height in cm: "))
bill = 0

# can ride
if height >= 120:
    age = int(input("You are tall enough to ride the rollercoaster, please enter your age: "))
    if age < 12:
        print("Child Tickets are $5")
        bill = 5
    elif age < 18:
        print("Teenager Tickets are $10")
        bill = 10
    elif age >= 45 or age <= 55:
        bill = 0
        print("You've most probably got midlife crisis so you can ride for free.")
    else:
        print("Adult Tickets are $12")
        bill = 12

    #for picture
    choice = str(input("Pictures cost an additional of $3. Do you want a picture taken (Y or N): "))
    if choice == "Y":
        bill += 3
        print(f"Your total bill is {bill}.")
    else:
        print(f"Your total bill is {bill}.")


# can"t ride
else:
    print("You are not tall enough to ride the rollercoaster.")