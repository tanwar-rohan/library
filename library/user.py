import sys
import time
import json
import mysql.connector
import datetime as DT
today = DT.date.today()
week_ago = today + DT.timedelta(days=10)

import signin as s
usernm=s.username


mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="root",
      database="library"
    )
mycursor = mydb.cursor()
mycursor.execute("SELECT bname FROM book_entry where stock !='0' ORDER BY bname")
myresult = mycursor.fetchall()
     

def displayAvailablebooks():
      print("The books we have in our library are as follows:")
      print("================================================")
      for x in myresult:
            print(x)
       
def lendBook():
      print("Enter the name of the book you'd like to borrow>>")
      book=input()
      flag='1'
      for x in myresult:
            if book in x:
                  mycursor.execute("UPDATE book_entry SET stock =stock - 1 WHERE bname='{}'".format(book)) 
                  print("The book you requested has now been borrowed")
                  mydb.commit()
                  flag='2'
      if flag=='2':
            sql = "INSERT INTO book (username ,issue_date ,return_date ,bname) VALUES ('"+usernm+"','"+str(today)+"','"+str(week_ago)+"','"+book+"')"
            mycursor.execute(sql)
            mydb.commit()
             
      if flag=='1' :
           print("Sorry the book you have requested is currently not in the library")
            
def addBook():
      print("Enter the name of the book you'd like to return>>")
      book=input()
      flag='1'
      for x in myresult:
            if book in x:
                  mycursor.execute("UPDATE book_entry SET stock =stock + 1 WHERE bname='{}'".format(book))
                  mydb.commit()
                  print("Thanks for returning your borrowed book")
                  flag='2'

      if flag=='2':
            sql = "DELETE FROM book WHERE bname = '{}' and username='{}'".format(book,usernm)
            mycursor.execute(sql)
            mydb.commit()            
                  
      if flag=='1' :
           print("Sorry the book you have enter is not borrowed from this library")

def design(char,no=1):
      design=str(char)*int(no)
      print(design.center(80))

def borrow():
      mycursor.execute("SELECT * FROM book where username='{}'".format(usernm))
      myresult = mycursor.fetchall()
      for x in myresult:
            print(x)

def maina(): 
      done=False
      while done==False:
            time.sleep(0.5)   
            design('*',25)
            design('USER MENU',1)
            design('*',25)
            design('_',80)

            print()
            menu=[' Display All availablebook',' Request a book',' Return a book',' View borrowed book',' Exit user menu']
            for x in range (len(menu)):
                  print('\t',x+1,'. ',menu[x])


            design('_',80)
      
            choice=int(input("Enter Choice:"))
            if choice==1:
                  displayAvailablebooks()
            elif choice==2:
                  lendBook()
            elif choice==3:
                  addBook()
            elif choice==4:
                  borrow()
            elif choice==5:
                  import main

            time.sleep(0.5) 
                  
maina()

                   


