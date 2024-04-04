bill = int(input('Hello! I am a tip calculator. Please enter the total bill: $'))
percentage = int(input('How much tip would you like to give, 10%, 12% or 15%?\n'))
people = int(input('Please enter the number of people who have to split the bill: '))
tip = ((int(bill) / 100) * percentage) / people
print(f'Each person should pay an amount of ${tip}. Have a great day!')