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
sql = "DROP TABLE `TB_hj`;"
cur.execute(sql)
con.commit()
con.close()