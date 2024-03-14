import mysql.connector
import pandas as pd

#   This is the main class of the Aniket's LMS(MySQL)
#   All rights owned by Aniket Dixit
#   https://github.com/aniketrepo/python-feature-set

#def start(): connectToMySQL()

#def connectToMySQL():
#    print("--------------------------------------------------------")
#    print(" -*- Connecting to MySQL DB  -*- ")
#    print("--------------------------------------------------------")
#    cnx = mysql.connector.connect(user='root', password='pilkhuwa01!', host='127.0.0.1', database='default_db')
#    df = pd.read_sql_query('select * from pet', cnx)
#    print(df)
#    cnx.close()

def confirmTheUser():
    print("--------------------------------------------------------")
    print(" -*- Welcome to Aniket's library management system  -*- ")
    print("--------------------------------------------------------")
    print("Enter 1. If You Are a Teacher")
    print("Enter 2. If You Are a Student")
    print("Enter 3. To exit")
    try:
