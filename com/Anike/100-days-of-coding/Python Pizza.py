print("Thank you for choosing Python Pizza Deliveries!")

size = input("Please enter the size of your pizza (small(S), medium(M) or large(L)): ")
add_pepperoni = input("Do you want Pepperoni on your pizza (Y or N): ")
extra_cheese = input("Do you want extra cheese on your pizza (Y or N): ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}.")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}.")
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your final bill is: ${bill}.")