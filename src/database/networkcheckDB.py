import re
from tkinter.font import nametofont
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="networkchecker")
mycursor = mydb.cursor()


def InsertData(name, email, registerd):
    sql = "INSERT INTO users (name,email,registerd) VALUES (%s,%s,%s)"
    var = (name, email, registerd)
    mycursor.execute(sql, var)

    mydb.commit()


def GetRegisterd(name):
    mycursor.execute("SELECT registerd FROM users WHERE name = %s"(name))

    results = mycursor.fetchall()
    return results
