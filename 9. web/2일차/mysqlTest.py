from mysql.connector import connect

try:
    sql = "insert into student values('홍길동', 20, '1999-11-12')"
    conn = connect(host = 'localhost', user='root', password='1234',
    db='flaskdb', charset='utf8')
    cur = conn.cursor()
    cur.execute( sql )
    conn.commit()
    conn.close()
    print('추가성공')
except Exception as err:
    print('실패', err)