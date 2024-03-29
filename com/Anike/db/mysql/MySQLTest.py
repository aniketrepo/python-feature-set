import mysql.connector

#   This is the test class to connect with MySQL
#   All rights owned by Aniket Dixit
#   https://github.com/aniketrepo/python-feature-set

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