import mysql.connector
import time
import sys
flag='1'
while flag=='1':
    time.sleep(1)
    def design(char,no=1):
        design=str(char)*int(no)
        print(design.center(80))
    design('*',25)
    design('Administrative Menu',1)
    design('*',25)
    time.sleep(0.3)
    design('_',80)

    mydb = mysql.connector.connect(
          host="127.0.0.1",
          user="root",
          passwd="root",
          database="library"
        )
    mycursor = mydb.cursor()

    menu=[' Display All Student Record',' Create Book',' Display All Books',' stock status',' View Issued Books',' Stock prediction',' Back to Main Menu',]
    for x in range (len(menu)):
        print('\t',x+1,'. ',menu[x])


    design('_',80)
    select=input("Enter Your Selection: ")



    if select=='1':
        mycursor.execute("SELECT * FROM book")
        result = mycursor.fetchall()
        for x in result:
            print(x)
        
        
    elif select=='2':
        bname=input("enter book name: ")
        stock=input("enter stock: ")
        n=bname[-2:]
        m=bname[:3]
        bid=m+n
        sql="INSERT INTO book_entry (bid, bname, stock) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE stock='{}'".format(stock)
        val=(bid,bname,stock)
        mycursor.execute(sql,val)
        mydb.commit()
        
        
        
    elif select=='3':
        mycursor.execute("SELECT * FROM book_entry ORDER BY bname")
        result = mycursor.fetchall()
        for x in result:
            print(x)
        
        
    #error    
    elif select=='4':
        mycursor.execute("SELECT * FROM book_entry where stock='0'")
        result = mycursor.fetchall()
        flag='1'
        for x in result:
            print(x)
            choice=input("""want to
                         1.update stock
                         2.delete book
                         : """)
            if choice=='1':
                    flag='2'
                    stock=input("enter stock: ")
                    sql = "update book_entry set stock ='{}' where exists (SELECT bname FROM book_entry WHERE stock = '0')".format(stock)
                    mycursor.execute(sql)
                    mydb.commit()
            elif choice=='2':
                    flag='2'
                    sql = "Delete from book_entry where exists (SELECT bname FROM book_entry WHERE stock = '0')"
                    mycursor.execute(sql)
                    mydb.commit()
            else:
                print("stock is unchanged")
                flag='2'
        if flag=='1':
            print("No book out of stock")
      
        
    elif select=='5':
        sql = "SELECT * FROM book ORDER BY issue_date"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
          print(x)
        
    elif select=='6':
        import prediction
    elif select=='7':
        import main
    time.sleep(1)
