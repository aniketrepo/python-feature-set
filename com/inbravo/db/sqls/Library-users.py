import mysql.connector

def start(): connectToMySQL()

def connectToMySQL():
    print("--------------------------------------------------------")
    print(" -*- Connecting to MySQL DB  -*- ")
    print("--------------------------------------------------------")
    cnx = mysql.connector.connect(user='root', password='pilkhuwa01!', host='127.0.0.1', database='default_db')
    df = pd.read_sql_query('select * from pet', cnx)
    print(df)
    cnx.close()

start()

print('Welcome to the Library! What do you want to do?')
print('1. Add Member')
print('2. Remove Member.')
print('3. Display Members.')
print('4. Quit.')
choice = int(input('Please enter the index number of your choice: '))

if choice == 1:
    username = input('Please enter the name of the soon to be Member: ')
    email= input('Please enter the e-mail of the soon to be Member: ')
    password= input('Please enter the preferred password of the soon to be Member: ')

elif choice == 2:
