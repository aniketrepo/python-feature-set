import

print('Welcome to the Library! What do you want to do?')
print('1. Add Member')
print('2. Remove Member.')
print('3. Display Members.')
print('4. Quit.')
choice = int(input('Please enter the index number of your choice: '))

if choice == 1:
    username = input('Please enter the name of the soon to be Member: ')
    email= input('Please enter the e-mail of the soon to be Member: ')
    passsword= input('Please enter the preferred password of the soon to be Member: ')

elif choice == 2:
