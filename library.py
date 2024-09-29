#inserting the records
import sys
sys.path.append(r'C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages')   


def insert():
    import mysql.connector as sqlc                      
    mycon=sqlc.connect(host="localhost",user="root",password="lcs@123",database="project")
    cursor=mycon.cursor()    

    cust2= input("\nTo view the book choices enter show :-\n")
    if cust2=="show":
        choice={1:"Adventures of Tom Sawyer - Mark Twain",2:"Ancient Mariner - Coleridge",3:"Mein                                                               Kampf -     Adolf Hitler",
                4:"Discovery of India - Pandit Jawaharlal Nehru",5:"Origin of species - Charles Darwin",
                6:"Around the World in eighty days - Jules Verne",
                7:"The Merchant of Venice - Shakespeare",8:"A Tale of Two Cities – Charles Dickens",
                9:"Geetanjali - Rabindra Nath Tagore",10:"Shakuntala- Kalidas"}
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        for name in choice:
            print("|",name,":",choice[name],)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print()
    
    cust3=int(input("Enter the code of the book you want to issue:-\n"))
    if cust3>10:
        print("INVALID CODE!\n")
    elif cust3<=10:
        print("The book you want to issue is: ",choice[cust3])
        rules="""\n1.The library is open from 8:00am to midnight on weekdays and from 9:00am to 5:30pm   on Sundays.
2. Books can be issued up to 5:00pm on Weekdays and up to 4:00pm on Saturdays. Books cannot be issued
on Sundays and national holidays.
3. Only 1 book will be issued at a time for a period of 15 days.
4. The issued book can be renewed for the return period for another 15 days for a maximum of 8 times by reissuing it.\n"""
        print(rules)
        cust4=input("Are you sure you want to issue this book? Enter 'yes' or 'no' :-\n")

        from datetime import date
        x=date.today()
        if cust4=="no":
            print("Book not issued.Thank you for coming here!Have a great day ahead!\n")
        elif cust4=="yes":

            st="insert into library(reg_no,name,age,book_issued,date_of_issue) values(%s,%s,%s,%s,%s)"
            rno=input("Enter your registration number :-\n")
            name=input("Enter your name :-\n")
            age=int(input("Enter your age :-\n"))
            book=choice[cust3]
            row=(rno,name,age,book,x)
            cursor.execute(st,row)
            mycon.commit()
            cursor.execute("select * from library")
            data=cursor.fetchall()
            
            reg1=[]


            for me in data:
                row1=(list(me))
                for i in row1:
                    reg1.append(i)

            if rno in reg1:
                search="select * from library where reg_no='%s'"%(rno)
                cursor.execute(search)
                data=cursor.fetchall()
                
                for row in data:
                    print("\nThe customer details are as follows:-\n")
                    print("=======================================================")
                    print("\nCustomer name     :-",me[1])
                    print("Age                :-",me[2])
                    print("Registration number:-",me[0])
                    print("Book issued        :-",me[3])
                    print("Date of issue      :-",me[4])
                    print("=======================================================")
                    print()
            
       
        

#searching for the record

def r_search():
    import mysql.connector as sqlc                      
    mycon=sqlc.connect(host="localhost",user="root",password="lcs@123",database="project")
    cursor=mycon.cursor() 
    
    cust15=input("Enter your registration number:-\n")
    sql="select reg_no from library"
    cursor.execute(sql)
    data=cursor.fetchall()
    reg1=[]

    for row in data:
        row1=(list(row))
        for i in row1:
            reg1.append(i)

    if cust15 in reg1:
        search="select * from library where reg_no='%s'"%(cust15)
        cursor.execute(search)
        data=cursor.fetchall()
        for row in data:
            print("\nThe customer details are as follows:-\n")
            print("=======================================================")
            print("\nCustomer name     :-",row[1])
            print("Age                :-",row[2])
            print("Registration number:-",row[0])
            print("Book issued        :-",row[3])
            print("Date of issue      :-",row[4])
            print("=======================================================")
            print()
            
#updating the records

def update():
    import mysql.connector as sqlc                      
    mycon=sqlc.connect(host="localhost",user="root",password="lcs@123",database="project")
    cursor=mycon.cursor()
    cust6=int(input("""Which field to you want to update?*Enter one of the following*
                     1 ~ for registration number
                     2 ~ for your age
                     3 ~ for your name
                      :-\n"""))
    cust7=input("Enter the name entered in the record :-\n")
    if cust6==1:
        cust9=input("Enter the correct reg_no :-\n")
        sql="update library set reg_no=%s where name=%s"
        st2=(cust9,cust7)
        cursor.execute(sql,st2)
        mycon.commit()
        print("RECORD SUCCESSFULLY UPDATED....")
        

    elif cust6==2:
        cust8=int(input("Enter the correct age :-\n"))
        sql="update library set age=%s where name=%s"
        st3=(cust8,cust7)
        cursor.execute(sql,st3)
        mycon.commit()
        print("RECORD SUCCESSFULLY UPDATED....")
        
        
    elif cust6==3:
        cust11=input("Enter the registration number entered in the record\n")
        cust12=input("Enter the correct name :-\n")
        sql="update library set name=%s where reg_no=%s"
        st4=(cust12,cust11)
        cursor.execute(sql,st4)
        mycon.commit()
        print("RECORD SUCCESSFULLY UPDATED....")
           
            
    
#deleting the records
           
def delete():
    import mysql.connector as sqlc                      
    mycon=sqlc.connect(host="localhost",user="root",password="lcs@123",database="project")
    cursor=mycon.cursor() 
    
    cust14=input("Do you want to delete your record? Enter 'yes' or 'no':-\n")
    if cust14=="no":
        print("# No record to be deleted.Thank you for coming here!Have a great day ahead! #\n")
    elif cust14=="yes":
        cust15=input("Enter your name registered in the record:-")
        sql="delete from library where name='%s'"%(cust15)
        cursor.execute(sql)
        mycon.commit()
        print("Your record has been successfully deleted\n")

#exiting from the prog

def exit():
    print("HAVE A GREAT DAY AHEAD! THANK YOU FOR COMING HERE :-)\n")
