import mysql.connector

mydb  =mysql.connector.connect(host="localhost",user="root", password="", database="networkchecker")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

results = mycursor.fetchall()

print (results)