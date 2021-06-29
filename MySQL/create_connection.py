import mysql.connector
import traceback

try:
    mydb = mysql.connector.connect(
    enter your host port ="localhost",
    user="enter user  of system",
    password="enter user  of systeenter your password"
    )
    print(mydb)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE enter your database name")
except Exception as e:
    print(e)
    


