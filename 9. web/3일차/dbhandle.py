from mysql.connector import connect

def insertStudentDB(name, age, birth):
    try:
        sql = "insert into student values(%s, %s, %s)"
        conn = connect(host='localhost', user='root', password='1234', 
            db='flaskdb', charset='utf-8')
        cur = conn.cursor()
        cur.execute( sql, (name, age, birth) )
        conn.commit()
        conn.close()
        print('추가성공')
        return '추가성공'
    except Exception as err:
        print('실패', err)
        return '실패:' +err

def selectStudent():
    try:
        sql = "select* from student"
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

def deleteStudentDB(name):
    try:
        sql = "delete from student where name = %s"
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