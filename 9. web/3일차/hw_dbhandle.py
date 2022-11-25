from mysql.connector import connect

def insertProductDB(name, quantity, date):
    try:
        sql = "insert into product values(%s, %s, %s)"
        conn = connect(host='localhost', user='root', password='1234', 
            db='flaskdb', charset='utf-8')
        cur = conn.cursor()
        cur.execute( sql, (name, quantity, date) )
        conn.commit()
        conn.close()
        return '입력되었습니다.'
    except Exception as err:
        print('실패', err)
        return '실패:' +err

def selectProduct():
    try:
        sql = "select * from product"
        conn = connect(host='localhost', user='root', password='1234', 
            db='flaskdb', charset='utf-8')
        cur = conn.cursor()
        cur.execute( sql)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except Exception as err:
        return '실패:' +err

def deleteProductDB(name):
    try:
        sql = "delete from product where name = %s"
        conn = connect(host='localhost', user='root', password='1234', 
            db='flaskdb', charset='utf-8')
        cur = conn.cursor()
        cur.execute( sql, (name,))
        nrow = cur.rowcount
        conn.commit()
        conn.close()
        return f'결과: {nrow}개가 삭제되었습니다.'
    except Exception as err:
        return '실패:' +err