import time
import pymysql

con = pymysql.connect(
    user="seocho",
    #passwd="노션 참고",
    host="jeongps.com",
    port=3306,
    db="seocho",
    charset="utf8"
)

cur = con.cursor(pymysql.cursors.DictCursor)
sql = """
INSERT INTO `TB_hj` 
(TEMPERATURE, STATUS, DATETIME)
VALUES
(%s, %s, %s);
"""
datetime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
cur.execute(sql, ("36.5", "NORMAL", datetime))
con.commit()
con.close()