print('Welcome to the rollercoaster!')
height = int(input('Please enter your height in cm: '))

if height >= 120:
    age = int(input('You are tall enough to ride the rollercoaster, please enter your age: '))
    if age >=18:
        print('Please pay a sum of $12 for the ticket.')
    else:
        print('Please pay a sum of $8 for the ticket.')
else:
    print('You are not tall enough to ride the rollercoaster.')