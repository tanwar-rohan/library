import mysql.connector
import random

def sign_in():
    
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="root",
      database="library"
    )
    x='1'

    mycursor = mydb.cursor()
    while x=='1':
        global username    
        username=input("enter username: ")
        mycursor.execute("SELECT * FROM user WHERE username='{}'".format(username))
        uname = mycursor.fetchall()
        for x in uname:
            if username in x:
                password=input("enter password: ")
                for x in uname:
                    if password in x:
                        if username == password:
                            print("'{}' is wrong password ".format(password))
                            x='1'
                            
                        else:
                            import user
                            x='0'
                    else:
                        print("'{}' is wrong password".format(password))
                        a=input("forgot password. 'y'or 'n' : ")
                        if a=='y':
                            email=input("enter email: ")
                            for x in uname:
                                if email in x:
                                    if username != email:
                                        n1=random.randint(1,9)
                                        n2=random.randint(1,9)
                                        n3=random.randint(1,9)
                                        n4=random.randint(1,9)
                                        n=n1+n2+n3+n4
                                        no=int(input("solve the eq: '{}'+'{}'+'{}'+'{}': ".format(n1,n2,n3,n4)))
                                        if n==no:
                                            mycursor.execute("SELECT password FROM user WHERE username='{}'".format(username))
                                            p= mycursor.fetchall()
                                            print("{} is your password ".format(p))
                                            
                                else:
                                    print("you entered wrong email")
                        x='1'
    return username


