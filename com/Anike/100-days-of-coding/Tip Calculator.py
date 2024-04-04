bill = int(input('Hello! I am a tip calculator. Please enter the total bill: $'))
tip = int(input('How much tip would you like to give, 10%, 12% or 15%?\n'))
people = int(input('Please enter the number of people who have to split the bill: '))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f'Each person should pay an amount of ${final_amount}. Have a great day!')