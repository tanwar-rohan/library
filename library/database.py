import mysql.connector
mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="root"
    )
mycursor = mydb.cursor()
try:
    mycursor.execute("create database library")
except:
    print('')
import librarydbms
