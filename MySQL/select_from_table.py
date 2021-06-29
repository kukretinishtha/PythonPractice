import mysql.connector

mydb = mysql.connector.connect(
  enter your host port ="localhost",
  user="enter user  of system",
  password="enter user  of systeenter your password",
  database="enter your database name"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)