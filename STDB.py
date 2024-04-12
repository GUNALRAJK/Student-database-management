import mysql.connector
""" ...To create table in database...

con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")

cur=con.cursor()
sql="create table student(Sino int primary key auto_increment,Rollno int unique,name varchar(30),dob varchar(10),address varchar(50),phno varchar(10))"
result=cur.execute(sql)
cur.fetchall()
print(result)
con.commit()
"""


def display():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    sql="select * from student"
    cur.execute(sql)
    result=cur.fetchall()
    con.commit()
    print(result)

def create():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=[]
    n.append(int(input("Enter the roll no: ")))
    n.append(input("Enter the name: "))
    n.append(input("Enter the dob: "))
    n.append(input("Enter the address: "))
    n.append(input("Enter the phno: "))
    sql="insert into student values(NULL,%s,%s,%s,%s,%s)"
    cur.execute(sql,n)
    result=cur.fetchall()
    con.commit()
    con.close()
    print(n)
        
def update():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=int(input("\n1.roll no \n2.name\n3.dob \n4.address\n5.phno \n select your choise: "))
    if(n==1):
        i=[]
        i.append(int(input("Enter the update Rollno")))
        i.append(int(input("Enter the pre Rollno")))
        sql="update student set rollno=(%s) where rollno=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==2):
        i=[]
        i.append(input("Enter the update name"))
        i.append(input("Enter the pre name"))
        sql="update student set name=(%s) where name=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==3):
        i=[]
        i.append(input("Enter the update dob"))
        i.append(input("Enter the pre dob"))
        sql="update student set dob=(%s) where dob=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==4):
        i=[]
        i.append(input("Enter the update address"))
        i.append(input("Enter the pre address"))
        sql="update student set address=(%s) where address=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()
    if(n==5):
        i=[]
        i.append(int(input("Enter the update phno")))
        i.append(int(input("Enter the pre phno")))
        sql="update student set phno=(%s) where phno=(%s)"
        cur.execute(sql,i)
        con.commit()
        con.close()

def view():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=[]
    n.append(int(input("Enter your Roll no: ")))
    sql="select * from student where rollno=(%s)"
    cur.execute(sql,n)
    result=cur.fetchall()
    print(result)
    con.close()

def delete():
    con=mysql.connector.connect(host="127.0.0.1",
                            username="root",
                            password="4788",
                            database="school")
    cur=con.cursor()
    n=[]
    n.append(int(input("Enter the Roll no: ")))
    sql="delete from student where rollno=(%s)"
    cur.execute(sql,n)
    con.commit()
    con.close()
    
m=0    
while(m!=6):
    print("\n1.view student database \n2.create \n3.update \n4.delete \n5.view \n6.exit")
    m=int(input("Enter your choice:"))
    if m==1:
        display()
    elif m==2:
        create()
    elif m==3:
        update()
    elif m==4:
        delete()
    elif m==5:
        view()
    elif m==6:
        print("...Exist...")
    else:
        print("...Invaild choise...")
    



    
