import pymysql as x

def employer_add():
    try:
        db=x.connect(host='localhost',user='root',password='root',db="Employee")
        cur=db.cursor()
        a=input('Enter new EmpId (xxxx format): ')
        b=input('Enter name: ')
        c=input('Enter DOB (YYYY-MM-DD): ')
        d=input('Enter department: ')
        query="INSERT INTO emp VALUES('"+a+"','"+b+"','"+c+"','"+d+"');"
        cur.execute(query)
        db.commit()
        cur.close()
        db.close()
        print('Record added')
    except:
        print('An error occured(either wrong DOB format or duplicate primary key)')

def employer_view_all():
    db=x.connect(host='localhost',user='root',password='root',db="Employee")
    c=db.cursor()
    c.execute('SELECT * FROM emp;')
    rows=c.fetchall()
    if len(rows)>0:
        print('+-----+--------------------+-----------+----------+')
        print('|EmpID|        Name        |    DOB    |   Dept   |')
        print('+-----+--------------------+-----------+----------+')
        for item in rows:
            print('|'+item[0]+' |'+item[1]+' '*(20-len(item[1]))+'|'+str(item[2])+' |'+item[3]+' '*(10-len(item[3]))+'|')
        print('+-----+--------------------+-----------+----------+')
    else:
        print('No records available to display')
    c.close()
    db.close()
        
def employer_view_one():
    db=x.connect(host='localhost',user='root',password='root',db="Employee")
    c=db.cursor()
    c.execute('SELECT * FROM emp;')
    rows=c.fetchall()
    xyz=input('Enter EmpID to be searched: ')
    abc=()
    for item in rows:
        if item[0]==xyz:
            abc=item
        else:
            pass
    if len(abc)>0:
        print('+-----+--------------------+-----------+----------+')
        print('|EmpID|        Name        |    DOB    |   Dept   |')
        print('+-----+--------------------+-----------+----------+')
        print('|'+abc[0]+' |'+abc[1]+' '*(20-len(abc[1]))+'|'+str(abc[2])+' |'+abc[3]+' '*(10-len(abc[3]))+'|')
        print('+-----+--------------------+-----------+----------+')
    else:
        print('Record not found')
    c.close()
    db.close()

def employer_modify():
    try:
        db=x.connect(host='localhost',user='root',password='root',db="Employee")
        c=db.cursor()
        c.execute('SELECT * FROM emp;')
        rows=c.fetchall()
        abc=()
        a=input('Enter EmpID to modify: ')
        for item in rows:
            if item[0]==a:
                abc=item
            else:
                pass
        if len(abc)>0:
            b=input('What would you like to edit (Name/DOB/Dept): ')
            z=input('Enter new value (YYYY-MM-DD if DOB): ')
            query="UPDATE emp SET "+b+" = '"+z+"' WHERE EmpID = '"+a+"';"
            c.execute(query)
            print('Record has been modified')
        else:
            print('Record not found')
        db.commit()
        c.close()
        db.close()
    except:
        print('An Error Occured')
        
def employer_delete():
    db=x.connect(host='localhost',user='root',password='root',db="Employee")
    c=db.cursor()
    c.execute('SELECT * FROM emp;')
    rows=c.fetchall()
    abc=()
    a=input('Enter EmpID to delete: ')
    for item in rows:
        if item[0]==a:
            abc=item
        else:
            pass
    if len(abc)>0:
        query="DELETE FROM emp WHERE EmpID = '"+a+"';"
        c.execute(query)
        print('Record has been deleted')
    else:
        print('Record not found')
    db.commit()
    c.close()
    db.close()
