import sys
sys.path.append(r'C:\Users\hp\Desktop\Python prog')
import library

#connecting to sql
sys.path.append(r'C:\Users\hp\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import mysql.connector as sqlc                      
mycon=sqlc.connect(host="localhost",user="root",password="lcs@123",database="project")
if mycon.is_connected():
    print("Welcome\n")
cursor=mycon.cursor()    

#involvement of the user    

while True:
    cust = input("Enter 'hello' to activate the library system:\n")
    if cust.lower() == "hello":
        a = "HELLO THERE! Welcome to DELHI PUBLIC LIBRARY"
        print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("*", a, "*")
        print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        break
    else:
        print("Please enter a valid response!")

print("======================================================================")
while True:
    print("\nChoose from the following options:-\n")    
    abc={1:"SEARCH for your record",2:"ISSUE a book",3:"UPDATE your record",
         4:"DELETE your record",5:"EXIT from the system"}
    print("====================================================")
    for name in abc:
        print("|",name,":",abc[name],)
    print("====================================================")
    print()

    cust16=int(input("ENTER THE CODE OF THE OPERATION WHICH YOU WANT TO PERFORM :-"))

    if cust16==1:
        library.r_search()
        print()
    elif cust16==2:
        library.insert()
        print()
    elif cust16==3:
        library.update()
        print()
    elif cust16==4:
        library.delete()
        print()
    elif cust16==5:
        print()
        library.exit()
        break
    else:
        print("\nINVALID CODE ENTERED\n")
    
