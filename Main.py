import pymysql as x
from Employer import *
from Employee import *

db_pass=input('Enter database password: ') #Check if db password is correct
db=x.connect(host='localhost',user='root',password=db_pass)
db.close()

try:
    db=x.connect(host='localhost',user='root',password=db_pass)
    c=db.cursor()
    c.execute('CREATE DATABASE Employee;')
    db.commit()
    c.close()
    db.close()
    print('Database created')
except:
    print('Database already exists')

try:
    db=x.connect(host='localhost',user='root',password=db_pass,db='Employee')
    c=db.cursor()
    c.execute('CREATE TABLE emp(EmpID CHAR(4) PRIMARY KEY,Name VARCHAR(20),DOB DATE,Dept VARCHAR(10));')
    db.commit()
    c.close()
    db.close()
    print('Table created')
    print()
except:
    print('Table already exists')
    print()

def employee_menu():
    id_list=[]
    rows=()
    db=x.connect(host='localhost',user='root',password='root',db='Employee')
    c=db.cursor()
    c.execute('SELECT * FROM emp;')
    rows=c.fetchall()
    c.close()
    db.close()
    for item in rows:
        id_list.append(item[0])

    a=input('Enter EmpID: ')
    b=input('Enter Password: ')
    if (a in id_list) and (a==b):
        print('Successfully logged in')
        print()
        while True:
            print('\tEmployee Menu')
            print('1) View Data')
            print('2) Modify Data')
            print('3) Exit to main menu')
            print()
            choice=int(input('Enter Choice: '))
            print()
            if choice==1:
                employee_view()
                print()
            elif choice==2:
                employee_modify()
                print()
            elif choice==3:
                print('Exiting to main menu()')
                print()
                break
            else:
                print('Invalid Choice')
                print()
    else:
        print('Wrong credentials entered, going back to main menu')
        print()
        main_menu()

def employer_menu():
    a=input('Enter admin username: ')
    b=input('Enter admin password: ')
    if a==b and a=='root':
        print('Successfully logged in')
        print()
        while True:
            print('\tEmployer Menu')
            print('1) Add a record')
            print('2) View all records')
            print('3) View one record')
            print('4) Modify a record')
            print('5) Delete a record')
            print('6) Exit to main menu')
            print()
            choice=int(input('Enter Choice: '))
            print()
            if choice==1:
                employer_add()
                print()
            elif choice==2:
                employer_view_all()
                print()
            elif choice==3:
                employer_view_one()
                print()
            elif choice==4:
                employer_modify()
                print()
            elif choice==5:
                employer_delete()
                print()
            elif choice==6:
                print('Exiting to main menu')
                print()
                break
            else:
                print('Invalid Choice')
                print()
    else:
        print('Wrong credentials entered, going back to main menu')
        print()
        main_menu()        

def main_menu():
    while True:
        print('\t\tMain Menu')
        print('\t\t---------------')
        print("Welcome to the organisation's database\n","\tWhere would u like to go?")
        print('1) Employee Menu')
        print('2) Employer Menu')
        print('3) Exit')
        print()
        choice=int(input('Enter Choice: '))
        print()
        if choice==1:
            employee_menu()
            print()
        elif choice==2:
            employer_menu()
            print()
        elif choice==3:
            print('Thank You!')
            break
        else:
            print('Invalid Choice')

main_menu()
