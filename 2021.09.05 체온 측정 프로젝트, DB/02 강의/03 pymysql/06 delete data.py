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
sql = "DELETE FROM `TB_hj` WHERE ID = %s"
cur.execute(sql, (10,))
con.commit()
con.close()