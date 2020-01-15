import sys
import mysql.connector
import random
import re
signup={}
flag='y'
while flag=='y':
    fname=input("enter first name: ")
    lname=input("enter last name: ")
    age=input("enter age: ")
    email=input("""enter email:
    (example=abc@xyz.com): """)
    
    if (age.isnumeric()):
        flag='n'
        if('@' in email):   
            x = re.search(".com$",email)
            if(x):
                flag='n'
            else:
                print("invalid email")
                del email
                flag='y'
    else:
        print("invalid age")
        flag='y'
    
if flag=='n':
    z=random.randrange(1,9)
    z=str(z)
    q=random.randrange(1,9)
    q=str(q)
    p=random.randrange(0,20)
    p=str(p)
    username=(fname +"."+ lname+q+p+z)
    y=random.randrange(10,100)
    y=str(y)
    password=(fname+p+"_"+q+lname+q+p+z)
    flag=='1'
else:
    print("enter correct detail")
name=fname+lname
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="library"
)
mycursor = mydb.cursor()
sql = """INSERT INTO user (name ,age , email , username , password) VALUES (%s,%s,%s,%s,%s)"""
val=(name,age,email,username,password)
mycursor.execute(sql,val)
mydb.commit()
print("""
        NOW
    you have signup""")
print("'{}' is your username".format(username))
print("'{}' is your password".format(password))




