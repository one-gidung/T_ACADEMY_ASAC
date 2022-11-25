from mysql.connector import  pooling



pool= pooling.MySQLConnectionPool(pool_name = "mypool",pool_reset_session=True,
                              pool_size = 3, host='localhost',port='3306',
                              database='flaskdb',user='root', password='1234')

# con = pool.get_connection()
# c = con.cursor()
# c.execute('insert into student values(%s,%s,%s)',('이순신',50,'1989-05-12'))
# con.commit()
# print( c.rowcount)
# con.close()

'''
con = pool.get_connection()
c = con.cursor()
    #x.fetchall
c.callproc('selectProc')
for result in c.stored_results():
    print(result.fetchall())
con.close()
'''
con = pool.get_connection()
c = con.cursor()
c.callproc('insertProc', ('마이프록', 60, '1999-11-19'))
print(c.rowcount)
con.close()