import mysql.connector
conn=mysql.connector.connect(host="localhost", user="root", passwd="root")
cur=conn.cursor()
cur.execute('use employee;')
cur.execute('select * from emp1')
rec=cur.fetchall()
for i in rec:
    print(i)
cur.execute("insert into emp1 values(8900,'RADHIKA ', 'Clerk',98, '1991-12-3',950.00, 420.00, 30);")
cur.execute('select * from emp1')
rec=cur.fetchall()
for i in rec:
    print(i)

conn.close()
