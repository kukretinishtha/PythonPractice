import mysql.connector

mydb = mysql.connector.connect(
  enter your host port ="localhost",
  user="enter user  of system",
  password="enter user  of systeenter your password",
  database="enter your database name"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Highway 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")