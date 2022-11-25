from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(pool_name='mypool', pool_reset_session=True, pool_size=3,
                                   host='localhost', port='3306', database='flaskdb',
                                   user='root', password='1234')
                            
def insert_product_pool(name, quantity, date):
    try:
        conn = pool.get_connection()
        cur = conn.cursor()
        cur.execute('insert into product values (%s, %s, %s)', (name, quantity, date))
        conn.commit()
        conn.close()
        return '입력되었습니다.'
    except:
        return '오류입니다.'

                            
def update_product_pool(name, new_name, new_quantity, new_date):
    try:
        conn = pool.get_connection()
        cur = conn.cursor()
        cur.execute(f'update product set name="{name}", quantity="{new_name}", date="{new_quantity}" where name="{new_date}"')
        conn.commit()
        conn.close()
        return '입력되었습니다.'
    except:
        return '오류입니다.'

                            
def select_all_product_pool():
    conn = pool.get_connection()
    cur = conn.cursor()
    cur.execute('select * from product')
    data = cur.fetchall()
    conn.close()
    return data
    

def select_product_pool():
    conn = pool.get_connection()
    cur = conn.cursor()
    cur.execute('select * from product')
    data = cur.fetchall()
    conn.close()
    return data