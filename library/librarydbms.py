import mysql.connector
def table():
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="root",
      database="library"
    )
    mycursor = mydb.cursor()
    2
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS `library`.`book` (
      `username` VARCHAR(45) NOT NULL,
      `issue_date` VARCHAR(32) NOT NULL,
      `return_date` VARCHAR(45) NOT NULL,
      `bname` VARCHAR(32) NOT NULL,
      PRIMARY KEY (`username`))""")

    #book_entry
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS `library`.`book_entry` (
      `bid` VARCHAR(16) NOT NULL,
      `bname` VARCHAR(255) NOT NULL,
      `stock` VARCHAR(32) NOT NULL,
      PRIMARY KEY (`bname`))""")

 

    #user_signup
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS `library`.`user` (
      `name` VARCHAR(45) NOT NULL,
      `age` VARCHAR(45) NOT NULL,
      `email` VARCHAR(255) NOT NULL,
      `username` VARCHAR(116) NOT NULL,
      `password` VARCHAR(132) NOT NULL,
      PRIMARY KEY (`username`),
      UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)""")


table()


