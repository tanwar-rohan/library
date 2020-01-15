import sys
import time
import database
done='1'
while done=='1':
    def design(char,no=1):
        design=str(char)*int(no)
        print(design.center(80))
    design('*',25)
    design('LIBRARY',1)
    design('*',25)
    design('_',80)

    print()
    menu=[' ADMIN',' USER',' EXIT']
    for x in range (len(menu)):
        print('\t',x+1,'. ',menu[x])


    design('_',80)
    choice=int(input("Enter Choice:"))
    if choice==1:
        a_password=input("enter admin password: ")
        if a_password=='admin':
            import admin
    elif choice==2:
        u_ans='1'
    
        u_choice=int(input(""" ======USER MENU=======
            1. New user(Sign up)
            2. Existing user(sign in)
            """))

        if u_choice==1:
           
            import signup
            time.sleep(0.9)
            print("remember your username & password")
            time.sleep(0.9)
            import signin as s
            s.sign_in()
        elif u_choice==2:
            import signin as s
            s.sign_in()
        else:
            sys.exit()
            break
        
    elif choice==3:
        sys.exit()
    else:
        print("choose a valid option")
    time.sleep(0.7)
    done=input("""want to continue...
                1.continue
                2.exit
                """)
