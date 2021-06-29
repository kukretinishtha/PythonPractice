import mysql.connector

mydb = mysql.connector.connect(
  enter your host port ="localhost",
  user="enter user  of system",
  password="enter user  of systeenter your password",
  database="enter your database name"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 