print('Welcome to the rollercoaster!')
height = int(input('Please enter your height in cm: '))

# can ride
if height >= 120:
    age = int(input('You are tall enough to ride the rollercoaster, please enter your age: '))
    if age <= 12:
        print('Please pay a sum of $5')
    elif age == 13:
        print('Please pay a sum of $10')
    elif age == 14:
        print('Please pay a sum of $10')
    elif age == 15:
        print('Please pay a sum of $10')
    elif age == 16:
        print('Please pay a sum of $10')
    elif age == 17:
        print('Please pay a sum of $10')
    else:
        print('Please pay a sum of $12')

# can't ride
else:
    print('You are not tall enough to ride the rollercoaster.')