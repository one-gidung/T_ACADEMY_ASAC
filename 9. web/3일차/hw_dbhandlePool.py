from mysql.connector import  pooling



pool= pooling.MySQLConnectionPool(pool_name = "mypool",pool_reset_session=True,
                              pool_size = 3, host='localhost',port='3306',
                              database='flaskdb',user='root', password='1234')

def insertProductPool(name, quantity, date):
    con = pool.get_connection()
    c = con.cursor()
    c.execute('insert into product values(%s,%s,%s)',(name, quantity, date))
    con.commit()
    nRow = c.rowcount
    con.close()
    return f'추가성공:{nRow}'

