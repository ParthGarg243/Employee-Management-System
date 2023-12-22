import pymysql as x

def employee_view():
    a=input('Please enter EmpID again for confirmation: ')
    rows=()
    db=x.connect(host='localhost',user='root',password='root',db='Employee')
    c=db.cursor()
    c.execute('SELECT * FROM emp;')
    rows=c.fetchall()
    c.close()
    db.close()
    for item in rows:
        if item[0]==a:
            print('+-----+--------------------+-----------+----------+')
            print('|EmpID|        Name        |    DOB    |   Dept   |')
            print('+-----+--------------------+-----------+----------+')
            print('|'+item[0]+' |'+item[1]+' '*(20-len(item[1]))+'|'+str(item[2])+' |'+item[3]+' '*(10-len(item[3]))+'|')
            print('+-----+--------------------+-----------+----------+')
        else:
            pass
            
def employee_modify():
    try:
        a=input('Please enter EmpID again for confirmation: ')
        db=x.connect(host='localhost',user='root',password='root',db="Employee")
        c=db.cursor()
        y=input('What would you like to edit (Name/DOB/Dept): ')
        z=input('Enter new value (YYYY-MM-DD for DOB): ')
        query="UPDATE emp SET "+y+" = '"+z+"' WHERE EmpID = '"+a+"';"
        c.execute(query)
        print('Record has been modified')
        db.commit()
        c.close()
        db.close()
    except:
        print('An error occured')
