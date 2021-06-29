import mysql.connector

mydb = mysql.connector.connect(
  enter your host port ="localhost",
  user="enter user  of system",
  password="enter user  of systeenter your password",
  database="enter your database name"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)